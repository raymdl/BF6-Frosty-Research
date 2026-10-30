"""Stage 1 hotfix check (L4059 draft): registry diff + mutator watch + gameplay catalog SHA-1 diff.

Given an old and a new collection folder (each with asset-catalog.json and raw/ plus
raw-status.jsonl, as written by frosty-collect-raw.ps1 -Catalog), this:

  (i)   runs scripts/frosty-registry-diff.py (research repo) over every tweakable registry
        (files under a Tweakables folder plus GRX_*, MUT_*, MutatorDatabase* anywhere: GRX_Weapons,
        GRX_Vehicles, GRX_Gadgets_Glacier, GRX_Glacier_Soldier, every other GRX_*, KST_* and the
        MutatorDatabase_* collections), after checking that every registry the catalogs list has a
        raw file on its side (the --old-extra / --new-extra folders count); and runs
        scripts/frosty-mutator-values.py for the watched MutatorDatabase_CH1 settings;
  (ii)  diffs the two asset catalogs (added, removed, GUID, size, record SHA-1) restricted to the
        gameplay path shape of the L4059 route list (cosmetic trees excluded), plus, for
        information, the raw SHA-256 of gameplay routes captured successfully on both sides
        (from raw-status.jsonl; not re-hashed - frosty-capture-compare.py does that);
  (iii) prints counts and the changed rows and paths, writes TSVs into --out-dir and exits
        0  nothing gameplay changed and coverage is complete,
        1  something gameplay changed (registry row, watched mutator, or gameplay catalog/raw path),
        2  nothing changed in what was checked, but coverage is incomplete (a registry without raw
           bytes on one side, a helper failed, or the catalogs come from different cache states).

Read-only except for --out-dir (must not exist yet). Calls the repo scripts; does not copy them.

Usage:
  python frosty-hotfix-check.py <old collection> <new collection> --out-dir <new folder>
      --old-descriptors <SharedTypeDescriptors.ebx> --new-descriptors <SharedTypeDescriptors.ebx>
      [--old-extra <capture folder with raw\\>]... [--new-extra <capture folder>]...
      [--old-catalog <folder with asset-catalog.json>] [--new-catalog <folder>]
      [--route-list <route list>] [--repo <research repo>]
"""
import argparse
import collections
import csv
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_REPO = r"C:\Users\royal\Documents\BF6 Frosty Research"
MUTATOR_DB = "Common/GameSetup/Tweakables/Mutators/MutatorDatabase_CH1"
REDSEC_MARKERS = ("granite", "/br_", "_br_", "/rr_")


# ---------- gameplay path shape (L4059 route list rule, without the list-only "retained" group) ----------

def cosmetic(path):
    s = path.lower().split('/')
    dirs, name = s[:-1], s[-1]
    for i, d in enumerate(dirs[:-1]):
        if d == 'art' and dirs[i + 1] in ('skins', 'skin'):
            return 'art-skins'
    if '_charms' in dirs:
        return 'charms'
    if '/_textures/decals/' in path.lower():
        return 'textures-decals'
    if name.startswith('u_mdv_'):
        return 'u_mdv-skin'
    if 'sound' in dirs or path.lower().startswith('common/sound/'):
        return 'sound'
    return None


def under(low, *prefixes):
    return any(low.startswith(p + '/') for p in prefixes)


def shape_group(path):
    low = path.lower()
    name = low.rsplit('/', 1)[-1]
    if under(low, 'common/gamesetup/tweakables') or name.startswith(('grx_', 'kst_', 'mut_', 'mutatordatabase')):
        return 'tweakables-registries'
    if 'materialgrid' in name:
        return 'material-grids'
    if under(low, 'globals/materials/materialgrid'):
        return 'material-grid-curves'
    if under(low, 'common/hardware/weapons'):
        return 'weapons'
    if under(low, 'common/hardware/gadgets') or (under(low, 'common/gameplay') and 'gadget' in low):
        return 'gadgets'
    if under(low, 'common/hardware/vehicles'):
        return 'vehicles'
    if under(low, 'common/gameplay/soldier'):
        return 'soldier'
    if under(low, 'common/gameplay/affectors'):
        return 'affectors'
    if under(low, 'common/ui/static/metadata', 'common/ui/metadata'):
        return 'ui-metadata'
    if under(low, 'common/gameplay'):
        return 'gameplay-other'
    if under(low, 'common/hardware') and not under(low, 'common/hardware/_cosmeticslibrary', 'common/hardware/cineprops'):
        return 'hardware-other'
    return None


def gameplay_group(path, listed):
    """Group name when the path is gameplay by shape or listed in --route-list; None otherwise."""
    g = shape_group(path)
    if g and (g in ('tweakables-registries',) or not cosmetic(path)):
        return g
    if path.lower() in listed and not cosmetic(path):
        return 'route-list'
    return None


def redsec(path):
    low = '/' + path.lower()
    return any(m in low for m in REDSEC_MARKERS)


# ---------- inputs ----------

def load_catalog(folder):
    doc = json.load(open(Path(folder) / 'asset-catalog.json', encoding='utf-8-sig'))
    assets = {a['path'].lower(): a for a in doc['assets']}
    return {'head': doc.get('gameHead'), 'sdk': doc.get('sdkVersion'), 'count': len(doc['assets']), 'assets': assets}


def load_status(folder):
    p = Path(folder) / 'raw-status.jsonl'
    out = {}
    if p.exists():
        for line in open(p, encoding='utf-8-sig'):
            if line.strip():
                j = json.loads(line)
                if j.get('status') == 'success':
                    out[j['path'].lower()] = j.get('sha256')
    return out


def load_module(repo, name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), Path(repo) / 'scripts' / f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(cmd, log):
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    log.write('$ ' + subprocess.list2cmdline(cmd) + f'\n[exit {proc.returncode}]\n{proc.stdout}{proc.stderr}\n')
    return proc


def mutator_source(collection, extras):
    """Last folder (extras later win, like frosty-registry-diff) holding MutatorDatabase_CH1 raw and a catalog."""
    for folder in list(reversed(extras)) + [collection]:
        f = Path(folder)
        if (f / 'raw' / (MUTATOR_DB + '.ebx')).exists() and (f / 'asset-catalog.json').exists():
            return str(f)
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('old')
    ap.add_argument('new')
    ap.add_argument('--out-dir', required=True)
    ap.add_argument('--old-descriptors', required=True)
    ap.add_argument('--new-descriptors', required=True)
    ap.add_argument('--old-extra', action='append', default=[])
    ap.add_argument('--new-extra', action='append', default=[])
    ap.add_argument('--old-catalog', help='folder whose asset-catalog.json replaces the old collection catalog')
    ap.add_argument('--new-catalog', help='folder whose asset-catalog.json replaces the new collection catalog')
    ap.add_argument('--route-list', help='route list whose routes also count as gameplay (e.g. new-route-list-2110.txt)')
    ap.add_argument('--repo', default=DEFAULT_REPO)
    ap.add_argument('--show', type=int, default=60, help='max rows/paths printed per section (all are in the TSVs)')
    a = ap.parse_args()

    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=False)
    log = open(out / 'helper-runs.log', 'w', encoding='utf-8', newline='\n')
    incomplete, changed = [], []

    listed = set()
    if a.route_list:
        listed = {l.strip().lower() for l in open(a.route_list, encoding='utf-8-sig') if l.strip()}

    # ---- catalogs ----
    oc = load_catalog(a.old_catalog or a.old)
    nc = load_catalog(a.new_catalog or a.new)
    print(f'Old catalog: {a.old_catalog or a.old} (Head {oc["head"]}, {oc["count"]} assets)')
    print(f'New catalog: {a.new_catalog or a.new} (Head {nc["head"]}, {nc["count"]} assets)')
    if oc['count'] != nc['count']:
        print(f'  NOTE catalog sizes differ ({oc["count"]} vs {nc["count"]}). Frosty lists about 1,150 extra assets '
              'when it rebuilds its cache; compare a rebuilt-cache catalog only with a rebuilt-cache catalog '
              '(--old-catalog/--new-catalog), or treat added paths as possible cache artefacts.')
    rows = []
    for key in sorted(oc['assets'].keys() | nc['assets'].keys()):
        o, n = oc['assets'].get(key), nc['assets'].get(key)
        path = (n or o)['path']
        g = gameplay_group(path, listed)
        if g is None:
            continue
        if o is None:
            kind = 'added'
        elif n is None:
            kind = 'removed'
        else:
            kinds = [k for k, f in (('guid', 'guid'), ('originalBytes', 'originalBytes'), ('sha1', 'sha1')) if o.get(f) != n.get(f)]
            if not kinds:
                continue
            kind = 'changed:' + '+'.join(kinds)
        rows.append((path, g, kind, int(redsec(path)), (o or {}).get('sha1', ''), (n or {}).get('sha1', '')))
    with open(out / 'catalog-gameplay-diff.tsv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['path', 'group', 'change', 'redsec', 'oldSha1', 'newSha1'])
        w.writerows(rows)
    by_kind = collections.Counter(r[2].split(':')[0] for r in rows)
    by_group = collections.Counter(r[1] for r in rows)
    print(f'(ii) Catalog, gameplay paths: {len(rows)} differ {dict(by_kind)}; by group {dict(by_group)}; '
          f'REDSEC-named {sum(r[3] for r in rows)}')
    for r in rows[:a.show]:
        print(f'  {r[2]:<22} {r[1]:<22} {"REDSEC " if r[3] else ""}{r[0]}')
    if len(rows) > a.show:
        print(f'  ... {len(rows) - a.show} more in catalog-gameplay-diff.tsv')
    if rows:
        changed.append(f'{len(rows)} gameplay catalog paths')
        if oc['count'] != nc['count'] and set(by_kind) <= {'added', 'removed'}:
            print('  NOTE only additions/removals and the catalogs differ in size: check for cache-state artefacts.')

    # ---- raw SHA-256 (information; from raw-status.jsonl) ----
    os_, ns_ = load_status(a.old), load_status(a.new)
    for e in a.old_extra:
        os_.update(load_status(e))
    for e in a.new_extra:
        ns_.update(load_status(e))
    raw_rows = []
    for key in sorted(os_.keys() & ns_.keys()):
        if os_[key] != ns_[key]:
            path = (nc['assets'].get(key) or oc['assets'].get(key) or {'path': key})['path']
            g = gameplay_group(path, listed)
            if g:
                raw_rows.append((path, g, int(redsec(path)), os_[key], ns_[key]))
    with open(out / 'raw-gameplay-diff.tsv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['path', 'group', 'redsec', 'oldSha256', 'newSha256'])
        w.writerows(raw_rows)
    print(f'     Raw SHA-256 (raw-status.jsonl), gameplay routes captured on both sides: '
          f'{len(os_.keys() & ns_.keys())} compared, {len(raw_rows)} differ')
    for r in raw_rows[:a.show]:
        print(f'  raw changed            {r[1]:<22} {"REDSEC " if r[2] else ""}{r[0]}')
    if raw_rows:
        changed.append(f'{len(raw_rows)} gameplay raw files')

    # ---- (i) registry coverage + registry diff ----
    rd = load_module(a.repo, 'frosty-registry-diff')
    have_old = rd.registry_files(a.old, a.old_extra)
    have_new = rd.registry_files(a.new, a.new_extra)
    # A registry without raw bytes on a side is a coverage gap only when the catalog record
    # SHA-1 does not prove it unchanged (identical SHA-1 on both catalogs = identical bytes).
    cov, cov_by_sha1 = [], []
    for side, cat, have in (('old', oc, have_old), ('new', nc, have_new)):
        other = nc if side == 'old' else oc
        for key, asset in cat['assets'].items():
            if rd.in_scope(asset['path']) and key not in have:
                twin = other['assets'].get(key)
                if twin is not None and twin.get('sha1') == asset.get('sha1'):
                    cov_by_sha1.append((side, asset['path']))
                else:
                    cov.append((side, asset['path']))
    with open(out / 'registry-coverage-missing.tsv', 'w', encoding='utf-8', newline='') as f:
        f.write('side\tpath\tstatus\n' + ''.join(f'{s}\t{p}\tnot proven unchanged\n' for s, p in sorted(cov))
                + ''.join(f'{s}\t{p}\tcatalog SHA-1 unchanged\n' for s, p in sorted(cov_by_sha1)))
    reg_cat = sum(1 for c in (oc, nc) for k, x in c['assets'].items() if rd.in_scope(x['path']))
    print(f'(i)  Registries: catalogs list {sum(1 for x in oc["assets"].values() if rd.in_scope(x["path"]))} old / '
          f'{sum(1 for x in nc["assets"].values() if rd.in_scope(x["path"]))} new; raw files {len(have_old)} old / '
          f'{len(have_new)} new; without raw but catalog SHA-1 unchanged: {len(cov_by_sha1)} '
          f'(not decoded; route-list gap); without raw and not proven unchanged: {len(cov)}')
    for s, p in sorted(cov_by_sha1)[:a.show]:
        print(f'  no raw, SHA-1 unchanged ({s}): {p}')
    for s, p in sorted(cov)[:a.show]:
        print(f'  no raw ({s}): {p}')
    if cov:
        incomplete.append(f'{len(cov)} registries without raw bytes (capture them, or pass --old-extra/--new-extra)')

    tsv = out / 'registry-diff.tsv'
    cmd = [sys.executable, str(Path(a.repo) / 'scripts' / 'frosty-registry-diff.py'), a.old, a.new,
           '--old-descriptors', a.old_descriptors, '--new-descriptors', a.new_descriptors, '--out', str(tsv)]
    for e in a.old_extra:
        cmd += ['--old-extra', e]
    for e in a.new_extra:
        cmd += ['--new-extra', e]
    proc = run(cmd, log)
    if proc.returncode != 0 or not tsv.exists():
        incomplete.append(f'frosty-registry-diff.py failed (exit {proc.returncode}); see helper-runs.log')
        reg_rows = []
    else:
        with open(tsv, encoding='utf-8') as f:
            reg_rows = list(csv.DictReader(f, delimiter='\t'))
    rc = collections.Counter(r['change'] for r in reg_rows)
    rr = sum(1 for r in reg_rows if r['redsec'] == '1')
    assets = collections.Counter(r['asset'] for r in reg_rows)
    print(f'     Registry diff: {len(reg_rows)} TSV rows {dict(rc)}; REDSEC-flagged {rr}; assets {len(assets)}')
    for line in proc.stdout.splitlines()[:a.show]:
        print('  ' + line)
    shown = 0
    for r in reg_rows:
        if r['change'] == 'changed' and shown < a.show:
            print(f'  ~ {r["asset"].rsplit("/", 1)[-1]} | {r["row"]} | {r["field"]}: {r["old"][:60]} -> {r["new"][:60]}')
            shown += 1
    if reg_rows:
        changed.append(f'{len(reg_rows)} registry rows')

    # ---- (i) watched mutators ----
    osrc, nsrc = mutator_source(a.old, a.old_extra), mutator_source(a.new, a.new_extra)
    if not (osrc and nsrc):
        incomplete.append('MutatorDatabase_CH1 raw (with a catalog beside it) missing on one side; watched mutators not read')
        print('     Watched mutators: not read (MutatorDatabase_CH1 raw missing on one side)')
    else:
        proc = run([sys.executable, str(Path(a.repo) / 'scripts' / 'frosty-mutator-values.py'), osrc, nsrc,
                    '--descriptors', a.old_descriptors, a.new_descriptors], log)
        (out / 'watched-mutators.md').write_text(proc.stdout, encoding='utf-8')
        if proc.returncode != 0:
            incomplete.append(f'frosty-mutator-values.py failed (exit {proc.returncode})')
        diffs = []
        for line in proc.stdout.splitlines():
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) == 3 and cells[0].startswith('`'):
                if cells[1] != cells[2]:
                    diffs.append(f'{cells[0]}: {cells[1]} -> {cells[2]}')
        print(f'     Watched mutators (MutatorDatabase_CH1; old {osrc}, new {nsrc}): {len(diffs)} differ')
        for d in diffs:
            print('  ' + d)
        if diffs:
            changed.append(f'{len(diffs)} watched mutator settings')

    # ---- (iii) verdict ----
    print()
    if changed:
        print('GAMEPLAY CHANGE: ' + '; '.join(changed) + '. Not a "no gameplay change" hotfix until each is explained.')
    if incomplete:
        print('INCOMPLETE: ' + '; '.join(incomplete))
    if not changed and not incomplete:
        print('NO GAMEPLAY CHANGE in registries, watched mutators and gameplay catalog/raw paths.')
    summary = {'old': a.old, 'new': a.new, 'oldCatalog': a.old_catalog or a.old, 'newCatalog': a.new_catalog or a.new,
               'catalogCounts': [oc['count'], nc['count']], 'catalogGameplayDiff': dict(by_kind),
               'catalogGameplayByGroup': dict(by_group), 'rawGameplayDiff': len(raw_rows),
               'registryRows': dict(rc), 'registryRedsecRows': rr, 'registryAssets': len(assets),
               'registryCoverageMissing': len(cov), 'registryNoRawSha1Unchanged': len(cov_by_sha1), 'changed': changed, 'incomplete': incomplete}
    (out / 'summary.json').write_text(json.dumps(summary, indent=1), encoding='utf-8')
    log.close()
    sys.exit(1 if changed else 2 if incomplete else 0)


if __name__ == '__main__':
    main()
