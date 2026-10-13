"""Locate the deploy index: any import of DTA_Weapons/DTA_Sidearms in a WB; print holder object scalars."""
import sys, json
from rawlib import *
objs = load(sys.argv[1])[0]
dta = {g: p for g, p in byguid.items() if "/dta_" in p.lower()}
print(dta)
def has(x):
    if isinstance(x, dict):
        if "$import" in x:
            return x["$import"]["fileGuid"].lower() in dta
        return any(has(c) for c in x.values())
    if isinstance(x, list):
        return any(has(c) for c in x)
    return False
def fmt(v, d=0):
    if isinstance(v, dict) and "$import" in v:
        i = imp(v); return "import:" + str((i[0] or "?").rsplit("/", 1)[-1])
    if isinstance(v, dict) and "$ref" in v:
        return "ref#%d:%s" % (v["$ref"], objs[v["$ref"]]["$class"])
    if isinstance(v, dict):
        return {k: fmt(c, d + 1) for k, c in v.items()} if d < 4 else "{..}"
    if isinstance(v, list):
        return [fmt(c, d + 1) for c in v[:6]] if d < 4 else "[%d]" % len(v)
    return v
for n, o in enumerate(objs):
    if has(o):
        print(n, json.dumps(fmt(o))[:2500])
# who references those objects
