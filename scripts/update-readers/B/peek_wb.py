"""python peek_wb.py <wb route> : show the primary-fire shot block (Class_35259f6b Field_58d70acb), with
every tweakable link (Field_6b28f68f) resolved to its registry row name and value."""
import sys, json
import common as c
objs, _ = c.load(sys.argv[1])


def show(x, path, depth=0):
    if isinstance(x, dict):
        if "Field_6b28f68f" in x:
            r, t = c.deref(x["Field_6b28f68f"], objs)
            rest = {k: v for k, v in x.items() if k != "Field_6b28f68f"}
            print(path, "TWEAK row:", (t or {}).get("Field_0c59fa06"), "=", json.dumps(c.unbox((t or {}).get("Field_42c8b257")))[:80] if t else ("unresolved " + str(r)),
                  "| local:", json.dumps(rest)[:200])
            return
        if "$import" in x or "$ref" in x:
            r, t = c.deref(x, objs)
            print(path, "->", r if r else "ref %s" % x.get("$ref"), t["$class"] if t else None)
            return
        for k, v in x.items():
            if not k.startswith("$"):
                show(v, path + "/" + k[6:], depth + 1)
    elif isinstance(x, list):
        if len(x) > 6:
            print(path, "list", len(x)); return
        for i, v in enumerate(x):
            show(v, path + "[%d]" % i, depth + 1)
    else:
        print(path, "=", x)


for i, o in enumerate(objs):
    if o["$class"] == "Class_35259f6b":
        print("== object", i)
        show(o.get("Field_58d70acb"), "58d70acb")
