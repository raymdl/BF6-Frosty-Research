"""python dump.py <route> [object index|class substr] -> named JSON of objects."""
import sys, json
import lib
route = sys.argv[1]
objs, _, a = lib.load(route)
sel = sys.argv[2] if len(sys.argv) > 2 else None
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
print("objects", len(objs))
for i, o in enumerate(objs):
    if sel is None:
        print(i, o["$class"], str(o.get("Field_0c59fa06", ""))[:80], len(json.dumps(o)))
    elif sel.isdigit() and int(sel) == i or (not sel.isdigit() and sel in o["$class"]):
        print(i, json.dumps(lib.named(o), indent=1)[:mx])
