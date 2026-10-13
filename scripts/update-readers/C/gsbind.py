"""List GS selector bindings with their container path. python gsbind.py <folder> <stem> [substring of modifier]"""
import sys, json
from rawlib import *
folder, stem = sys.argv[1], sys.argv[2]
sub = sys.argv[3].lower() if len(sys.argv) > 3 else ""
base = "common/hardware/weapons/" + folder.lower() + "/"
objs = load(base + "gs_" + stem.lower())[0]
# selector guid -> unlock name
selname = {}
ab = load(base + stem.lower() + "_ability")[0]
for o in ab:
    for u in o.get("Field_7e54e22c", []) or []:
        i = imp(u)
        if i and i[0]:
            selname[i[1]] = i[0].rsplit("/", 1)[-1]
out = collections.Counter()
def walk(x, path):
    if isinstance(x, dict):
        if "Field_2f0e5b83" in x and "Field_6d011165" in x:
            r, o = deref(x["Field_2f0e5b83"], objs)
            nm = (r or "local").rsplit("/", 1)[-1]
            if sub in nm.lower():
                print("%-60s %-38s %-34s extra=%s" % (path[-60:], nm, selname.get(str(x["Field_6d011165"]).lower(), str(x["Field_6d011165"])[:8]),
                      json.dumps({k: v for k, v in x.items() if k not in ("Field_2f0e5b83", "Field_6d011165")})[:120]))
            out[path] += 1
        for k, c in x.items():
            walk(c, path + "/" + k.replace("Field_", ""))
    elif isinstance(x, list):
        for i, c in enumerate(x):
            walk(c, path + "[]")
for i, o in enumerate(objs):
    walk(o, "#%d:%s" % (i, o["$class"][6:]))
print(dict(out))
