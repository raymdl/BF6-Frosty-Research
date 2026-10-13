"""Print an AAM (attachment-to-UI-descriptor map) and, for each record, whether the AD asset is held,
its label and description. python peekaam.py <route of AAM>   or  python peekaam.py --obj <route> [n]"""
import sys, json
from rawlib import *
if sys.argv[1] == "--obj":
    objs = load(sys.argv[2])[0]
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    print(len(objs), "objects")
    for i, o in enumerate(objs[:n]):
        print(i, json.dumps(o)[:int(sys.argv[4]) if len(sys.argv) > 4 else 1500])
    sys.exit()
objs = load(sys.argv[1])[0]
print(len(objs), "objects;", objs[0].get("Field_0c59fa06"))
S = strings()
for o in objs:
    if o["$class"] != "Class_ccf7da47":
        continue
    r = imp(o.get("Field_85b318a1"))
    route = r[0] if r else None
    h = bool(route and route.lower() in held)
    lab = desc = None
    if h:
        ad = load(route)[0]
        root = ad[0]
        keys = {k: v for k, v in root.items() if k.startswith("Field_")}
        _, d = deref(root.get("Field_490f0dd0"), ad)
        desc = sid(d.get("Field_3d34898a")) if d else None
        lab = {k: (S.get(sid(v.get("Field_3d34898a")) or "") if isinstance(v, dict) else v) for k, v in keys.items() if k not in ("Field_490f0dd0",)}
    print("%-44s -> %-70s held=%s desc=%s %s" % (o.get("Field_55aded8d"), (route or "?").split("Metadata/")[-1], h, desc, (S.get(desc) or "")[:60] if desc else ""))
