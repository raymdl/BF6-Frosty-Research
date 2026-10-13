"""Print small struct fields of a WB root object (index selectors with array imports).
python wbroot.py <route>"""
import sys, json
from rawlib import *
objs = load(sys.argv[1])[0]
root = objs[0]
print(root["$class"], root.get("Field_0c59fa06"))
def fmt(v):
    if isinstance(v, dict) and "$import" in v:
        i = imp(v)
        return "import:" + str((i[0] or v["$import"]["fileGuid"]).rsplit("/", 1)[-1])
    if isinstance(v, dict) and "$ref" in v:
        return "ref#%d:%s" % (v["$ref"], objs[v["$ref"]]["$class"])
    if isinstance(v, dict):
        return {k: fmt(c) for k, c in list(v.items())[:8]}
    if isinstance(v, list):
        return "[%d]" % len(v)
    return v
for k, v in root.items():
    s = json.dumps(fmt(v))
    if len(s) < 400:
        print(k, s)
