"""Every per-weapon map inside catalogue entries, with coverage and an example."""
import json, collections, sys
from derive import *
wids = set(CAT["WEAPON_ATTS"])
ex = sys.argv[1] if len(sys.argv) > 1 else "m4a1"
for key in ("SIGHTS", "MUZZLES", "BARRELS", "GRIPS", "LASERS", "LIGHTS", "ERGOS", "ACCESSORIES"):
    for e in CAT[key]:
        for k, v in e.items():
            if isinstance(v, dict) and v and set(v) <= wids:
                avail = [w for w in wids if e["id"] in (CAT["WEAPON_ATTS"][w].get(key.lower()[:-1], []) or [])]
                print(key, e["id"], k, "n=%d avail=%d" % (len(v), len(avail)), ex, json.dumps(v.get(ex))[:200], "| any:", json.dumps(next(iter(v.values())))[:160])
print(json.dumps(CAT["ACCESSORIES"])[:1500])
print(json.dumps(CAT["SIGHTS"])[:2500])
print(json.dumps([e for e in CAT["GRIPS"] if e["id"] in ("fold_vert", "canted_vertical", "bipod")])[:2500])
print(json.dumps([e for e in CAT["BARRELS"]][:3])[:2500])
print(json.dumps([e for e in CAT["ERGOS"]][:3])[:1200])
