"""Find dict keys / classes in a file. python findkey.py <route> <Field_x|Class_x> ..."""
import sys, json
from rawlib import *
objs = load(sys.argv[1])[0]
keys = set(sys.argv[2:])
def fmt(v, d=0):
    if isinstance(v, dict) and "$import" in v:
        i = imp(v)
        return "import:" + str((i[0] or v["$import"]["fileGuid"]).rsplit("/", 1)[-1])
    if isinstance(v, dict) and "$ref" in v:
        return "ref#%d:%s" % (v["$ref"], objs[v["$ref"]]["$class"])
    if isinstance(v, dict):
        return {k: fmt(c, d + 1) for k, c in list(v.items())[:14]} if d < 3 else "{..}"
    if isinstance(v, list):
        return [fmt(c, d + 1) for c in v[:4]] if d < 3 else "[%d]" % len(v)
    return v
def walk(x, path):
    if isinstance(x, dict):
        if x.get("$class") in keys:
            print(path, json.dumps(fmt(x))[:1500])
        for k, c in x.items():
            if k in keys:
                print(path, k, "=", json.dumps(fmt(c))[:500])
            walk(c, path + "/" + k.replace("Field_", ""))
    elif isinstance(x, list):
        for j, c in enumerate(x):
            walk(c, path + "[%d]" % j)
for n, o in enumerate(objs):
    walk(o, "#%d:%s" % (n, o["$class"][6:]))
