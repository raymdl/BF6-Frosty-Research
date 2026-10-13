"""Outline the provenance files that carry attachment identities."""
import json, sys, pathlib
def outline(x, depth=0, maxd=3, pre=""):
    if depth > maxd: return
    if isinstance(x, dict):
        for k, v in list(x.items())[:14]:
            t = type(v).__name__
            n = len(v) if isinstance(v, (dict, list, str)) else v
            print(pre + str(k)[:60], t, n if not isinstance(v, str) else repr(v[:100]))
            outline(v, depth + 1, maxd, pre + "  ")
    elif isinstance(x, list) and x:
        print(pre + "[0]:", json.dumps(x[0])[:500] if not isinstance(x[0], (dict, list)) else "")
        outline(x[0], depth + 1, maxd, pre + "  ")
for p in sys.argv[2:]:
    print("=====", p)
    outline(json.load(open(p, encoding="utf-8")), maxd=int(sys.argv[1]))
