"""CDX40 (ELR-40) projectile routes: catalog entries for .375 bullets, the WB primary projectile import, every WB
modifier effect that references a bullet, and the Match modifier's projectile."""
import json
import common as c
print("catalog routes with 375En:", sorted(p for p in c.byguid.values() if "375en" in p.lower()))
print("held:", sorted(c.proper[k] for k in c.held if "375" in k))
wb, _ = c.load("Common/Hardware/Weapons/BoltAction/CDX40/CDX40_WB")
for o in wb:
    if o["$class"] == "Class_35259f6b":
        print("WB primary projectile import:", json.dumps(o["Field_58d70acb"]["Field_808dd66c"]), "->", c.imp(o["Field_58d70acb"]["Field_808dd66c"]))


def walk(x, path, objs, route):
    if isinstance(x, dict):
        i = c.imp(x)
        if i:
            if i[0] and "/_bullets/" in i[0].lower():
                print("   bullet reference at", route, path, "->", i[0].rsplit("/", 1)[-1], i[1])
            return
        for k, v in x.items():
            walk(v, path + "/" + k[-8:], objs, route)
    elif isinstance(x, list):
        for n, v in enumerate(x):
            walk(v, path + "[%d]" % n, objs, route)


for i, o in enumerate(wb):
    walk(o, "obj%d(%s)" % (i, o["$class"][-8:]), wb, "CDX40_WB")
for r in ("Common/Hardware/Weapons/_WeaponModifiers/_Ammo/Match/WPM_AMO_Match_CDX40_W10",
          "Common/Hardware/Weapons/_WeaponModifiers/_Ammo/Match/WPM_AMO_Match_L115A3_W10"):
    objs, _ = c.load(r)
    for o in objs:
        if o["$class"] == "Class_b1afeb65":
            print(r.rsplit("/", 1)[-1], "Class_b1afeb65 Field_808dd66c:", json.dumps(o.get("Field_808dd66c")), "->", c.imp(o.get("Field_808dd66c")),
                  "| in catalog:", ((o.get("Field_808dd66c") or {}).get("$import") or {}).get("fileGuid", "").lower() in c.byguid)
# the same check on a known weapon: L115A3 base and Match
wb2, _ = c.load("Common/Hardware/Weapons/BoltAction/L115A3/L115A3_WB")
for i, o in enumerate(wb2):
    walk(o, "obj%d(%s)" % (i, o["$class"][-8:]), wb2, "L115A3_WB")
