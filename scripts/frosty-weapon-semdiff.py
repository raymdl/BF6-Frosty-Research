"""Per-weapon change list between two builds: a semantic diff of every changed weapon file.

python -I scripts/frosty-weapon-semdiff.py --old-index <tsv> --new-index <tsv>
    --old-descriptors <SharedTypeDescriptors.ebx> --new-descriptors <SharedTypeDescriptors.ebx>
    --out <sem-changes.tsv> [--controls 2.1.2.0]

The index files are "route TAB path TAB sha256" per line, one per build, later capture folders
winning (the update run's raw-index-old.tsv and raw-index-new.tsv, written by make_inputs.py).

Steps:
1. Changed routes: in both indexes with different sha256, under Common/Hardware/Weapons/ or the
   soldier-class weapon traits (Common/Gameplay/InRoundProgression/WeaponTraits/, which the
   site's class row reads), not a mesh, material grid or cosmetic (skins, charms, decals) route.
2. Decode both sides with each build's own descriptors (exact floats).
3. Keep a route when a field-level diff has a row that is not noise. Noise is a string id,
   expression or effect reference field, or a field new or dropped in the layout at its default
   value. MD_*, T_* and Equipment_* routes are left out: the equipment lists have their own
   scripted diff (frosty-equipment-list-diff.py), which is where list additions and removals
   such as the DRS-IAR Synthetic Tip show.
4. Semantic diff of each kept route: objects matched by GUID (else class and position), local
   references written as class and GUID, every list compared as a multiset, so an index shift
   is not a change. List items that differ in one or two leaves are paired as a change.

Output columns: route, class, match, keypath, kind, old, new. Kinds: scalar, list-item-changed,
list-added, list-removed, obj-added, obj-removed, uncertain (a position-matched object where
most fields differ; old and new hold the row and field counts).

The worker's job is to classify these rows, not to produce them.

Reference result, 2.1.1.0 (client 5383516) to 2.1.2.0 (no trait route changed): 871 changed weapon routes, 447 kept,
4,105 rows (scalar 1,631, obj-added 1,110, list-added 986, list-item-changed 295, list-removed 57,
obj-removed 22, uncertain 4). --controls 2.1.2.0 checks the addition control (nine PD_*_Match
drag values 0.002 -> 0.0025) and the removal control (WPM_MAG_045Cpt1_Ultimax_W05 drops its
reload import) and exits 1 if either is missing.
"""
import argparse, collections, importlib.util, json, re, sys
from pathlib import Path

DEC = Path(__file__).resolve().parent / "frosty-ebx-decode.py"
spec = importlib.util.spec_from_file_location("frosty_ebx_decode", DEC)
dec = importlib.util.module_from_spec(spec); spec.loader.exec_module(dec)

ZERO = "00000000-0000-0000-0000-000000000000"
STRING = {"Field_8cf424e7", "Field_fefe9de1"}
EXPR = {"Field_0c18a620", "Field_aa4fa860", "Field_c7ffe639"}
FX = {"Field_0679f638"}
DEFAULTS = (None, 0, 0.0, False, "[]", "", ZERO)
PREFIXES = ("common/hardware/weapons/", "common/gameplay/inroundprogression/weapontraits/")


def cosmetic(route):
    l = route.lower()
    return any(s in l for s in ("/art/skins/", "/art/skin/", "_charms/", "/_textures/decals/"))


def read_index(path):
    idx = {}
    for line in open(path, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 3:
            idx[p[0]] = (p[1], p[2])
    return idx


def changed_routes(old, new):
    out = []
    for r in sorted(old.keys() & new.keys()):
        l = r.lower()
        if old[r][1] == new[r][1] or not any(p in l for p in PREFIXES):
            continue
        if "materialgrid" in l or l.endswith("_mesh") or cosmetic(r):
            continue
        out.append(r)
    return out


def load(path, types):
    p = Path(path if path.endswith(".ebx") else path + ".ebx")
    return dec.Ebx(p, types, exact_floats=True).decode()


def flat(v, objs, prefix, out):
    if isinstance(v, dict):
        if set(v) == {"$ref"}:
            r = v["$ref"]
            t = objs[r] if isinstance(r, int) and 0 <= r < len(objs) else {}
            out[prefix] = f"ref:{t.get('$class')}@{t.get('$guid')}"
            return
        if "$import" in v and len(v) == 1:
            out[prefix] = "import:" + json.dumps(v["$import"], sort_keys=True)
            return
        for k, x in v.items():
            if k == "$guid":
                continue
            flat(x, objs, f"{prefix}.{k}" if prefix else k, out)
    elif isinstance(v, list):
        if not v:
            out[prefix] = "[]"
        for i, x in enumerate(v):
            flat(x, objs, f"{prefix}[{i}]", out)
    else:
        out[prefix] = v


def keyed(objs):
    res, pos = {}, {}
    for o in objs:
        g = o.get("$guid")
        if g and g != ZERO:
            res[("guid", g)] = o
        else:
            c = o.get("$class"); i = pos.get(c, 0); pos[c] = i + 1
            res[("position", f"{c}#{i}")] = o
    return res


def has_real_change(a, b):
    """Step 3: true when the field-level diff has a row that is not noise."""
    oa, ob = a["objects"], b["objects"]
    ka, kb = keyed(oa), keyed(ob)
    for k in ka.keys() | kb.keys():
        x, y = ka.get(k), kb.get(k)
        if x is None or y is None:
            return True
        fa, fb = {}, {}
        flat(x, oa, "", fa); flat(y, ob, "", fb)
        for p in fa.keys() | fb.keys():
            va, vb = fa.get(p, "<absent>"), fb.get(p, "<absent>")
            if va == vb:
                continue
            if va == "<absent>" and vb in DEFAULTS or vb == "<absent>" and va in DEFAULTS:
                continue
            if set(re.findall(r"Field_[0-9a-f]{8}", p)) & (STRING | EXPR | FX):
                continue
            return True
    return False


def isnum(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def eq(a, b):
    if isnum(a) and isnum(b):
        return abs(a - b) <= 1e-4 or a == b
    return a == b


def split_lists(fl):
    sc, ls = {}, collections.defaultdict(lambda: collections.defaultdict(dict))
    for p, v in fl.items():
        m = re.search(r"\[(\d+)\]", p)
        if not m:
            sc[p] = v
        else:
            ls[p[:m.start()]][int(m.group(1))][p[m.end():]] = v
    return sc, ls


def canon(item):
    def c(v):
        if not isnum(v):
            return json.dumps(v, sort_keys=True)
        return repr(round(v, 6)) if isinstance(v, float) else repr(v)
    return tuple(sorted((k, c(v)) for k, v in item.items()))


def semdiff(route, a, b, emit):
    oa, ob = a["objects"], b["objects"]
    ka, kb = keyed(oa), keyed(ob)
    for k in sorted(ka.keys() | kb.keys()):
        x, y = ka.get(k), kb.get(k)
        if x is None or y is None:
            emit(route, (x or y)["$class"], k[0], k[1], "obj-removed" if y is None else "obj-added", "", "")
            continue
        fa, fb = {}, {}
        flat(x, oa, "", fa); flat(y, ob, "", fb)
        sa, la = split_lists(fa); sb, lb = split_lists(fb)
        rows = []
        for p in sorted(sa.keys() | sb.keys()):
            va, vb = sa.get(p, "<absent>"), sb.get(p, "<absent>")
            if not eq(va, vb):
                rows.append((p, "scalar", va, vb))
        for pre in sorted(la.keys() | lb.keys()):
            A = [canon(i) for i in la.get(pre, {}).values()]
            B = [canon(i) for i in lb.get(pre, {}).values()]
            ca, cb = collections.Counter(A), collections.Counter(B)
            rem, add = list((ca - cb).elements()), list((cb - ca).elements())
            if not rem and not add:
                continue
            used = set()
            for r in rem[:]:
                dr, best = dict(r), None
                for j, ad in enumerate(add):
                    if j in used:
                        continue
                    da = dict(ad)
                    if set(da) != set(dr):
                        continue
                    diffs = [kk for kk in dr if dr[kk] != da[kk]]
                    if len(diffs) <= 2 and (best is None or len(diffs) < best[0]):
                        best = (len(diffs), j, diffs, da)
                if best:
                    used.add(best[1]); rem.remove(r)
                    for kk in best[2]:
                        rows.append((f"{pre}[]{kk}", "list-item-changed", dr[kk], best[3][kk]))
            add = [ad for j, ad in enumerate(add) if j not in used]
            for r in rem:
                rows.append((pre + "[]", "list-removed", "; ".join(f"{kk}={vv}" for kk, vv in r), ""))
            for r in add:
                rows.append((pre + "[]", "list-added", "", "; ".join(f"{kk}={vv}" for kk, vv in r)))
        tot = len(set(sa) | set(sb)) + 1
        if k[0] == "position" and len(rows) > 0.4 * tot and len(rows) > 6:
            emit(route, x["$class"], k[0], k[1], "uncertain", str(len(rows)), str(tot))
            continue
        for p, kind, va, vb in rows:
            emit(route, x["$class"], k[0], k[1] + "|" + p, kind, str(va), str(vb))


def controls_2120(rows):
    match = {r[0] for r in rows if re.search(r"/PD_[^/]*_Match$", r[0]) and r[4] == "scalar"
             and r[5].startswith("0.00200000") and r[6].startswith("0.00249999")}
    ultimax = [r for r in rows if r[0].endswith("/WPM_MAG_045Cpt1_Ultimax_W05") and r[4] == "list-removed"
               and "import:" in r[5]]
    ok = len(match) == 9 and len(ultimax) >= 1
    print(json.dumps({"control_add_match_drag_files": len(match), "expected": 9,
                      "control_remove_ultimax_045cpt1_reload_import": len(ultimax), "passed": ok}))
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--old-index", required=True)
    ap.add_argument("--new-index", required=True)
    ap.add_argument("--old-descriptors", required=True)
    ap.add_argument("--new-descriptors", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--controls", choices=["2.1.2.0"])
    a = ap.parse_args()
    old, new = read_index(a.old_index), read_index(a.new_index)
    to, tn = dec.type_descriptors(Path(a.old_descriptors)), dec.type_descriptors(Path(a.new_descriptors))
    routes = changed_routes(old, new)
    rows, kept, failed = [], 0, []
    emit = lambda *r: rows.append(r)
    for r in routes:
        stem = r.rsplit("/", 1)[-1]
        if stem.startswith(("MD_", "T_", "Equipment_")):
            continue
        try:
            x, y = load(old[r][0], to), load(new[r][0], tn)
        except Exception as e:
            failed.append(f"{r}: {type(e).__name__}: {e}")
            continue
        if has_real_change(x, y):
            kept += 1
            semdiff(r, x, y, emit)
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        f.write("route\tclass\tmatch\tkeypath\tkind\told\tnew\n")
        for r in rows:
            f.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in r) + "\n")
    print(json.dumps({"changed_weapon_routes": len(routes), "kept": kept, "rows": len(rows),
                      "kinds": collections.Counter(r[4] for r in rows), "decode_failed": failed}))
    if failed:
        return 1
    if a.controls == "2.1.2.0" and not controls_2120(rows):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
