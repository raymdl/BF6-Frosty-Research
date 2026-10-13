import json, collections
R = "C:/Users/royal/Documents/BF6 Weapon Analyzer/"
c = json.load(open(R + "data/attachments.json", encoding="utf-8"))
ks = collections.Counter()
for w, v in c["WEAPON_ATTS"].items():
    for k in v: ks[k] += 1
print(ks)
for w, v in c["WEAPON_ATTS"].items():
    ex = {k: v[k] for k in v if k not in ("muzzle", "barrel", "barrelDef", "grip", "laser", "light", "slots", "dependencies")}
    if ex or set(v["slots"]) != {"grip", "laser", "light"}: print(w, ex, json.dumps(v["slots"]))
ks = collections.Counter()
for w, v in c["WEAPON_MAG"].items():
    for k in v: ks["top." + k] += 1
    for m in v["mags"].values():
        for k in m: ks[k] += 1
print(ks)
for k in ["MUZZLES", "BARRELS", "GRIPS", "ERGOS", "LASERS", "LIGHTS", "SIGHTS"]:
    for e in c[k]:
        for w, o in (e.get("weaponOverrides") or {}).items():
            print(k, e["id"], w, o)
deps = collections.Counter()
for w, v in c["WEAPON_ATTS"].items():
    for d in v.get("dependencies", []):
        deps[json.dumps(d)] += 1
for d, n in deps.most_common(): print(n, d)
acc = collections.Counter()
for w, v in c["WEAPON_ACCESSORY"].items():
    acc[json.dumps(v)] += 1
for d, n in acc.most_common(): print(n, d)
print(sorted(set(c["WEAPON_ATTS"]) - set(c["WEAPON_ERGO"])), sorted(set(c["WEAPON_ATTS"]) - set(c["WEAPON_ACCESSORY"])))
wj = json.load(open(R + "data/weapons.json", encoding="utf-8"))
wl = wj if isinstance(wj, list) else wj.get("WEAPONS") or next(v for v in wj.values() if isinstance(v, list))
print(collections.Counter(w["cls"] for w in wl))
print({w["id"]: w["cls"] for w in wl})
