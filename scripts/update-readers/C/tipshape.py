import json, collections
R = "C:/Users/royal/Documents/BF6 Weapon Analyzer/"
t = json.load(open(R + "data/attachment-tooltips.json", encoding="utf-8"))
print({k: (len(v) if isinstance(v, (dict, list)) else v) for k, v in t.items()})
print(json.dumps(t.get("coverage"))[:800])
print(json.dumps(t["byWeapon"]["m4a1"])[:3000])
print({k: len(v) for k, v in t["byWeapon"]["pw5a3"].items()})
ds = t["descriptions"]
print(list(ds.items())[:3], [k for k in ds if not k[:8].isalnum() or len(k) != 8][:30])
c = json.load(open(R + "data/attachments.json", encoding="utf-8"))
# site selections lacking a mapping row
import sys
sys.path.insert(0, ".")
from identity import load_choices
rows = load_choices()
mapped = {(r["weapon"], r["slot"], r["id"]) for r in rows}
cur = set()
for w, wa in c["WEAPON_ATTS"].items():
    for s in ("muzzle", "barrel", "grip", "laser", "light"):
        for i in wa.get(s, []):
            if i != "none": cur.add((w, s, i))
for w, e in c["WEAPON_ERGO"].items():
    for i in e["avail"]: cur.add((w, "ergo", i))
for w, m in c["WEAPON_MAG"].items():
    for i in m["mags"]: cur.add((w, "mag", i))
nonammo = {m for m in mapped if m[1] != "ammo"}
print("site selections", len(cur), "mapped", len(nonammo), "site-not-mapped", sorted(cur - nonammo)[:40], "mapped-not-site", sorted(nonammo - cur)[:40])
print(collections.Counter(s for _, s, _ in cur))
