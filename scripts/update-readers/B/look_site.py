"""Print the site shapes this part targets (read-only look)."""
import json, pathlib, sys
S = pathlib.Path("C:/Users/royal/Documents/BF6 Weapon Analyzer")
F = pathlib.Path("C:/Users/royal/Documents/BF6 Frosty Research")
what = sys.argv[1]
if what == "trace":
    t = json.load(open(F / "reference-data/provenance/frosty-global-compiled-trace-2026-09-13.json", encoding="utf-8"))
    for k, v in t.items():
        s = json.dumps(v)
        print("==", k, len(s)); print(s[:1800])
elif what == "ball":
    b = json.load(open(S / "data/ballistics.json", encoding="utf-8"))
    print(json.dumps(b["source"])[:600])
    for k, v in b["projectiles"].items(): print(k, v)
    for k, v in b["weapons"].items(): print(k, json.dumps(v))
elif what == "hz":
    b = json.load(open(S / "data/hit_zones.json", encoding="utf-8"))
    print(json.dumps(b["source"]))
    for k, v in b["weapons"].items(): print(k, json.dumps(v))
elif what == "weap":
    w = json.load(open(S / "data/weapons.json", encoding="utf-8"))
    print(json.dumps(w[0], indent=1))
    for x in w:
        print(x["id"], x["cls"], x.get("bulletVel"), x.get("damageSource"), json.dumps(x.get("dmg")), {k: x[k] for k in x if "pellet" in k.lower() or "regen" in k.lower() or "collat" in k.lower()})
elif what == "coll":
    b = json.load(open(S / "data/balance_tables.json", encoding="utf-8"))
    print(list(b.keys()))
    for k, v in b["COLLATERAL_MULT_OVERRIDE"].items(): print(k, json.dumps(v))
elif what == "file":
    t = json.load(open(sys.argv[2], encoding="utf-8"))
    def show(x, d=0, mx=int(sys.argv[3]) if len(sys.argv) > 3 else 2):
        if isinstance(x, dict):
            for k, v in list(x.items())[:40]:
                print("  " * d + str(k), "::", json.dumps(v)[:300] if d >= mx or not isinstance(v, (dict, list)) else "")
                if d < mx: show(v, d + 1, mx)
        elif isinstance(x, list):
            print("  " * d + "[%d]" % len(x), json.dumps(x[:2])[:600])
    show(t)
