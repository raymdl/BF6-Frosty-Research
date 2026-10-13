"""Print the raw() summary and site-shaped record for the four new weapons (or names given)."""
import json, sys
import lib, extract
NEW = [("mk24", "MRGGA"), ("elr40", "CDX40"), ("z84m", "PKM"), ("rspr", "RSAR999")]
todo = [(a, a) for a in sys.argv[1:]] or NEW
for sid, internal in todo:
    r = extract.raw(internal)
    print("=====", sid, internal)
    for k, v in r.items():
        if k in ("log", "dmgFilePoints", "dmgFileFlat", "gsBindings", "recoil", "dyn", "minmax"):
            continue
        print("  ", k, "=", json.dumps(lib.named(v)) if not isinstance(v, (int, float, str)) else lib.f32(v))
    print("   bindings:", sorted(set((b[0], b[2]) for b in r["gsBindings"])))
    dis = [(l, lib.f32(f) if isinstance(f, float) else f, lib.f32(g) if isinstance(g, float) else g) for l, f, g, n in r["log"] if g is not None and not (extract.same(f, g) if not isinstance(f, list) else f == g)]
    print("   registry rows found:", sum(1 for l in r["log"] if l[2] is not None), "of", len(r["log"]), "| file != registry:", dis)
    print("   no registry row:", [l[0] for l in r["log"] if l[2] is None][:80])
    print(json.dumps(extract.record(r)))
