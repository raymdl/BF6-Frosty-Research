"""Raw Equipment_<W> dependency entries. python equipshow.py <siteId>"""
import sys, json
from derive import *
w = BY_SITE[sys.argv[1]]
gph = graph.weapon_graph(w["siteId"], w["folder"], w["stem"])
names = {r["idHash"] & 0xFFFFFFFF: r["stem"] for r in gph["attachments"]}
dup = {}
for r in gph["attachments"]: dup.setdefault(r["idHash"] & 0xFFFFFFFF, []).append(r["stem"])
print("duplicate hashes:", {k: v for k, v in dup.items() if len(v) > 1})
route = "common/hardware/weapons/" + w["folder"].lower() + "/equipment_" + w["stem"].lower()
objs = load(route)[0]
def short(v, d=0):
    if isinstance(v, dict) and "$import" in v:
        i = imp(v); return "imp:" + str(i[0]).rsplit("/", 1)[-1]
    if isinstance(v, dict) and "$ref" in v: return "ref#%d" % v["$ref"]
    if isinstance(v, dict): return {k[6:] if k.startswith("Field_") else k: short(c, d + 1) for k, c in v.items()}
    if isinstance(v, list):
        if v and all(isinstance(x, int) for x in v): return ["%s" % names.get(x & 0xFFFFFFFF, x) for x in v]
        return [short(c, d + 1) for c in v]
    return v
for o in objs:
    for e in o.get("Field_e70ce6be", []) or []:
        _, x = deref(e, objs) if isinstance(e, dict) and ("$ref" in e or "$import" in e) else (None, e)
        print(json.dumps(short(x))[:1500])
