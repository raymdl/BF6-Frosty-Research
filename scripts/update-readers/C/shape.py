"""Print the site's attachment catalogue in a compact form (per-weapon maps collapsed)."""
import json, sys
R = "C:/Users/royal/Documents/BF6 Weapon Analyzer/"
c = json.load(open(R + "data/attachments.json", encoding="utf-8"))
ws = sys.argv[1:] or ["m2010", "m240l", "pw5a3", "psr"]
for k in ["WEAPON_ATTS", "WEAPON_ERGO", "WEAPON_ACCESSORY", "WEAPON_MAG"]:
    for w in ws:
        if w in c[k]:
            print(k, w, json.dumps(c[k][w])); print()
W = set(c["WEAPON_ATTS"])
for k in ["SIGHTS", "MUZZLES", "BARRELS", "GRIPS", "LASERS", "LIGHTS", "ERGOS", "ACCESSORIES"]:
    for e in c[k]:
        d = {}
        for kk, v in e.items():
            if isinstance(v, dict) and v and set(v) <= W:
                d[kk] = "{%d weapons e.g. %s}" % (len(v), json.dumps(dict(list(v.items())[:1])))
            else:
                d[kk] = v
        print(k, json.dumps(d))
print(json.dumps(c["GAME_BUGS"])[:3000])
