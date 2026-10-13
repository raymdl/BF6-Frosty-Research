import json, sys
from rawlib import SITE
C = json.load(open(SITE / "data/attachments.json", encoding="utf-8"))
T = json.load(open(SITE / "data/attachment-tooltips.json", encoding="utf-8"))
for w in sys.argv[1:]:
    for k in ("WEAPON_ATTS", "WEAPON_ERGO", "WEAPON_ACCESSORY", "WEAPON_MAG"):
        print(w, k, json.dumps(C[k].get(w))[:1500])
    print(w, "tips", json.dumps(T["byWeapon"].get(w))[:900])
