"""python peek.py obj <route> [index|all] [maxchars]   print decoded objects
python peek.py reg <substring> [max]                print GRX_Weapons rows whose name contains the substring
python peek.py routes <substring>                   list held routes"""
import sys, json
import common as c
mode = sys.argv[1]
if mode == "obj":
    objs, _ = c.load(sys.argv[2])
    which = sys.argv[3] if len(sys.argv) > 3 else "all"
    mx = int(sys.argv[4]) if len(sys.argv) > 4 else 1500
    print(len(objs), "objects")
    for i, o in enumerate(objs):
        if which == "all" or which == str(i) or o["$class"].endswith(which):
            print(i, json.dumps(o)[:mx])
elif mode == "reg":
    n = 0
    for k, rows in c.registry().items():
        if sys.argv[2].lower() in k.lower():
            n += 1
            if n <= (int(sys.argv[3]) if len(sys.argv) > 3 else 60):
                print(k, "|", [json.dumps(c.unbox(r.get("Field_42c8b257")))[:300] for r in rows])
    print(n, "rows")
elif mode == "routes":
    for k in sorted(c.held):
        if sys.argv[2].lower() in k:
            print(c.proper[k])
