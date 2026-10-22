"""Per-map, per-mode extraction from decoded raw gameplay layers.
usage: python -I modes_extract.py <scratchpad> <decoded.json> [<decoded.json> ...] --out <dir>
Generalises bt_extract.py: every _layers_gameplay/<mode>/ folder becomes one record per (mode, map).
Writes <out>/<Mode>-maps.json and <out>/<Mode>-maps.txt, plus <out>/gem-usage.json (GEM import names
seen per mode, with whether the variant table knows them)."""
import json, sys, pathlib, collections, re
args = sys.argv[1:]
sp = pathlib.Path(args[0]); out = pathlib.Path(args[args.index('--out') + 1]); out.mkdir(parents=True, exist_ok=True)
files = [a for a in args[1:args.index('--out')]]
cat = json.load(open(r'C:\Users\royal\Documents\BF6 Datamining\builds\2.1.1.0\capture\collection\asset-catalog.json'))
g2p = {x['guid']: x['path'] for x in cat['assets']}
d = {}
for f in files:
    d.update(json.load(open(f))['assets'])
NAMES = {int(k): v for k, v in json.load(open(sp / 'mi-names.json')).items()}
table = json.load(open(sp / 'gem-variant-table-all.json'))
ADT = json.load(open(sp / 'ad-tables-by-mode.json'))
ADMODE = {'Conquest': 'AD_Objective_Conquest', 'Rush': 'AD_Objective_Rush', 'Escalation': 'AD_Objective_Escalation', 'Domination': 'AD_Objective_Capture_Domination', 'TeamDeathMatch': 'AD_Objective_TeamDM', 'SquadDeathMatch': 'AD_Objective_SquadDM', 'KingOfTheHill': 'AD_Objective_KOTH', 'Strikepoint': 'AD_Objective_Strikepoint', 'Sabotage': 'AD_Objective_Sabotage', 'Obliteration': 'AD_Objective_Obliteration', 'Breakthrough': 'AD_Objective_Breakthrough', 'CarrierStrike': 'AD_Objective_CarrierStrike', 'SpookyRush': 'AD_Objective_SpookyRush', 'Operations': 'AD_Objective_Operations'}
FACTION = {607944106: 'Alliance/NATO', -1865993703: 'Coalition/Pax Armata'}
TEAM_SLOT = {227737705: 1, 227737706: 2}
MODE_NORM = {'koth': 'KingOfTheHill', 'freeroam0': 'Freeroam', 'shared_cq_esc': 'Shared_CQ_ESC', 'esc_cq_shared': 'Shared_CQ_ESC'}
CANON = {'conquest': 'Conquest', 'rush': 'Rush', 'escalation': 'Escalation', 'domination': 'Domination', 'teamdeathmatch': 'TeamDeathMatch',
         'squaddeathmatch': 'SquadDeathMatch', 'kingofthehill': 'KingOfTheHill', 'strikepoint': 'Strikepoint', 'payload': 'Payload',
         'sabotage': 'Sabotage', 'obliteration': 'Obliteration', 'squadobliteration': 'SquadObliteration', 'carrierstrike': 'CarrierStrike',
         'gauntlet': 'Gauntlet', 'spookyrush': 'SpookyRush', 'operations': 'Operations', 'freeroam': 'Freeroam', 'flag': 'Flag',
         'gameplay': 'Gameplay', 'breakthrough': 'Breakthrough'}

def imp(x):
    i = x.get('$import') if isinstance(x, dict) else None
    return g2p.get(i['fileGuid'], '?').rsplit('/', 1)[-1] if i else None

def pos(o):
    p = o['Field_d6351ede']['Field_bc4b07b4']
    return [round(p['Field_3901db14'], 1), round(p['Field_42fc0f5e'], 1), round(p['Field_32a99b9c'], 1)]

def pip(pt, poly):
    x, z = pt; inside = False; n = len(poly)
    for i in range(n):
        x1, z1 = poly[i]; x2, z2 = poly[(i + 1) % n]
        if (z1 > z) != (z2 > z):
            if x1 + (z - z1) * (x2 - x1) / (z2 - z1) > x: inside = not inside
    return inside

def variant(gem, key, mode=None):
    t = ADT.get(ADMODE.get(mode, ''), {}).get('<' + gem + '>') or table.get('<' + gem + '>')
    if not t: return None
    return (t['variants'].get(str(key)) or t['default']).strip('<>')

def val(v):
    return v.get('value') if isinstance(v, dict) and 'value' in v else v

groups = collections.defaultdict(list)   # (mode, map) -> keys
SHARED = {'sharedassets_tdm_dom': ['teamdeathmatch', 'domination'], 'sharedassets_koth_sdm_tdm_dom': ['kingofthehill', 'squaddeathmatch', 'teamdeathmatch', 'domination'],
          'sharedassets_dom_tdm': ['domination', 'teamdeathmatch'], 'sharedassets_dom_tdm_sdm_rush_koth': ['domination', 'teamdeathmatch', 'squaddeathmatch', 'rush', 'kingofthehill'],
          'sharedassets_largemodes_cq_esc': ['conquest', 'escalation'], 'sharedassets_smallmodes_tdm_dom_strike': ['teamdeathmatch', 'domination', 'strikepoint'],
          'shared_cq_esc': ['conquest', 'escalation'], 'esc_cq_shared': ['conquest', 'escalation'], 'esc_cq_train': ['conquest', 'escalation'],
          'mp_sabotage': ['sabotage'], 'mp_koth0': ['kingofthehill'], 'winter_domination': ['domination']}
for k in d:
    m = re.match(r'game/glaciermp/levels/(mp_[^/]+)/_layers_gameplay/([^/]+)/', k.lower())
    if not m:
        # direct child of _layers_gameplay: the asset name carries the mode (e.g. Conquest0, Rush_Global)
        m2 = re.match(r'game/glaciermp/levels/(mp_[^/]+)/_layers_gameplay/([a-z]+?)(?:\d+|_[a-z0-9_]+)?$', k.lower())
        if not m2 or m2.group(2) not in CANON: continue
        groups[(CANON[m2.group(2)], m2.group(1).upper())].append(k)
        continue
    folder = m.group(2)
    if folder in SHARED:
        for md in SHARED[folder]:
            groups[(CANON[md], m.group(1).upper())].append(k)
        continue
    mode = CANON.get(MODE_NORM.get(folder, folder))
    if not mode: continue
    groups[(mode, m.group(1).upper())].append(k)
gem_usage = collections.defaultdict(collections.Counter)
by_mode = collections.defaultdict(dict)
for (mode, mp), keys in sorted(groups.items()):
    rec = {'assets': [re.split(r'/_layers_gameplay/[^/]+/', k, flags=re.I)[-1] for k in keys], 'factionOverrides': {}, 'namedOverrides': {},
           'instances': [], 'boxes': [], 'polygons': [], 'otherImports': collections.Counter()}
    for k in keys:
        objs = d[k]['objects']
        for o in objs:
            if o.get('$class') == 'Class_f5c6eb31':
                for v in o.get('Field_10cf85cd') or []:
                    n = NAMES.get(v['Field_93bf7d99'])
                    if n: rec['namedOverrides'][k.split('/')[-1] + ':' + n] = val(v['Field_8cf424e7'])
            for ent in o.get('Field_21943083', []) if isinstance(o.get('Field_21943083'), list) else []:
                cid = ent.get('Field_c1ad37da'); v = val(ent.get('Field_47f25917') or {})
                if cid in TEAM_SLOT and isinstance(v, int):
                    rec['factionOverrides'][f'team{TEAM_SLOT[cid]}'] = FACTION.get(v, v)
        root = objs[0] if objs else {}
        for c in root.get('Field_c78408a3', []) or []:
            if c.get('Field_2d7314c9') in TEAM_SLOT:
                src = c.get('Field_c41fb636')
                for o in objs:
                    for ent in (o.get('Field_21943083') or []):
                        if ent.get('Field_c1ad37da') == src:
                            v = val(ent.get('Field_47f25917') or {})
                            if isinstance(v, int): rec['factionOverrides'][f'team{TEAM_SLOT[c["Field_2d7314c9"]]}'] = FACTION.get(v, v)
        layer = re.split(r'/_layers_gameplay/[^/]+/', k, flags=re.I)[-1]
        for i, o in enumerate(objs):
            c = o.get('$class')
            if c == 'Class_2f332f01':
                gem = imp(o.get('Field_cbd4eb97'))
                if not gem: continue
                if gem.startswith('GEM_'):
                    key = (o.get('Field_cd465eb9') or {}).get('Field_8cf424e7', -1)
                    gem_usage[mode][gem] += 1
                    rec['instances'].append({'layer': layer, 'idx': i, 'gem': gem, 'key': key, 'variant': variant(gem, key, mode), 'pos': pos(o), 'id': o.get('Field_5645e663')})
                else:
                    rec['otherImports'][gem] += 1
            elif c == 'Class_78096792':
                pts = [(p['Field_3901db14'], p['Field_32a99b9c']) for p in o['Field_edfc6df6']]
                if not pts: continue
                xs = [p[0] for p in pts]; zs = [p[1] for p in pts]
                entry = {'layer': layer, 'idx': i, 'n': len(pts), 'bbox': [round(min(xs)), round(min(zs)), round(max(xs)), round(max(zs))], 'pts': pts}
                (rec['boxes'] if len(pts) == 4 else rec['polygons']).append(entry)
    for inst in rec['instances']:
        pt = (inst['pos'][0], inst['pos'][2])
        inst['inBoxes'] = [b['idx'] for b in rec['boxes'] if pip(pt, b['pts'])]
        inst['inPolys'] = [p['idx'] for p in rec['polygons'] if pip(pt, p['pts'])]
    for b in rec['boxes'] + rec['polygons']:
        b['contains'] = [f"{x['gem'][4:]}{'#'+str(x['key']) if x['key']!=-1 else ''}@{x['idx']}" for x in rec['instances'] if pip((x['pos'][0], x['pos'][2]), b['pts'])]
        del b['pts']
    rec['otherImports'] = dict(rec['otherImports'])
    by_mode[mode][mp] = rec
for mode, maps in by_mode.items():
    lines = []
    for mp, rec in maps.items():
        lines.append(f'===== {mp}')
        lines.append('assets: ' + ', '.join(rec['assets']))
        lines.append('factionOverrides: ' + json.dumps(rec['factionOverrides']))
        lines.append('namedOverrides: ' + json.dumps(rec['namedOverrides']))
        lines.append('gem counts: ' + json.dumps(collections.Counter(x['gem'] for x in rec['instances'])))
        lines.append('other imports: ' + json.dumps(rec['otherImports']))
        for x in rec['instances']:
            lines.append(f"  {x['layer']}@{x['idx']} {x['gem'][4:]} key={x['key']} variant={x['variant']} pos={x['pos']} boxes={x['inBoxes']} polys={x['inPolys']}")
        for b in rec['boxes']:
            lines.append(f"  BOX@{b['idx']} ({b['layer']}) bbox={b['bbox']} contains={b['contains']}")
        for b in rec['polygons']:
            lines.append(f"  POLY{b['n']}@{b['idx']} ({b['layer']}) bbox={b['bbox']} contains={b['contains']}")
    json.dump(maps, open(out / f'{mode}-maps.json', 'w'), indent=1)
    (out / f'{mode}-maps.txt').write_text('\n'.join(lines), encoding='utf-8')
    print(f'{mode}: {len(maps)} maps, {sum(len(r["instances"]) for r in maps.values())} GEM instances')
usage = {m: {g: {'n': n, 'inTable': ('<' + g + '>') in table} for g, n in c.items()} for m, c in gem_usage.items()}
json.dump(usage, open(out / 'gem-usage.json', 'w'), indent=1)
unknown = sorted({g for m in usage.values() for g, v in m.items() if not v['inTable']})
print('GEMs not in variant table:', unknown)
