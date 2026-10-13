"""Find imports in a file whose route contains a substring; print the containing dict's scalars.
python findimp.py <route> <substring>"""
import sys, json
from rawlib import *
objs = load(sys.argv[1])[0]
sub = sys.argv[2].lower()
def walk(x, path):
    if isinstance(x, dict):
        for k, c in x.items():
            i = imp(c)
            if i and i[0] and sub in i[0].lower():
                print(path, k, "->", i[0].rsplit("/", 1)[-1], "| siblings:", json.dumps({kk: vv for kk, vv in x.items() if not isinstance(vv, (dict, list))})[:300])
            walk(c, path + "/" + k.replace("Field_", ""))
    elif isinstance(x, list):
        for j, c in enumerate(x):
            i = imp(c)
            if i and i[0] and sub in i[0].lower():
                print(path, "[%d]" % j, "->", i[0].rsplit("/", 1)[-1])
            walk(c, path + "[%d]" % j)
for n, o in enumerate(objs):
    walk(o, "#%d:%s" % (n, o["$class"][6:]))
