"""Kill-switch rows whose name contains a substring, in every held Killswitches registry."""
import sys, json
import common as c
for k in sorted(c.held):
    if "/tweakables/killswitches/" in k:
        objs, _ = c.load(k)
        for o in objs:
            n = o.get("Field_0c59fa06")
            if isinstance(n, str) and sys.argv[1].lower() in n.lower():
                print(c.proper[k].rsplit("/", 1)[-1], "|", n, "|", o.get("$guid"), json.dumps({kk: vv for kk, vv in o.items() if kk.startswith("Field_") and kk != "Field_0c59fa06"})[:200])
