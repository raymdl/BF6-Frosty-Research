"""Site convention check: weapon.mag versus the default magazine record in WEAPON_MAG."""
import json
import lib
w = {x["id"]: x for x in json.load(open(lib.SITE / "data/weapons.json", encoding="utf-8"))}
a = json.load(open(lib.SITE / "data/attachments.json", encoding="utf-8"))
M = a["WEAPON_MAG"]
bad = []
for k, v in M.items():
    d = v["mags"][v["def"]]
    if d.get("mag") != w[k]["mag"]:
        bad.append((k, v["def"], d.get("mag"), w[k]["mag"]))
print("weapons whose default magazine capacity differs from weapon.mag:", bad)
print(json.dumps(M["m2010esr"])[:1200])
print(json.dumps(M["brod3"])[:500])
