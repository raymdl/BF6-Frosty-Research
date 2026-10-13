"""Compact view of the proposals and their supporting detail for the four new weapons."""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import json, pathlib
H = settings.part("B")
p = json.load(open(H / "proposed.json", encoding="utf-8")); v = json.load(open(H / "validation.json", encoding="utf-8"))
for wid in ("mk24", "elr40", "z84m", "rspr"):
    dt = v["newWeaponDetail"][wid]
    print("==", wid, "indices", json.dumps(dt["indices"]), "WB registry rows", dt["wbRegistryRows"], "unmapped", dt["unmapped"], "issues", dt["resolved"]["issues"])
    w = p["data/weapons.json"]["[id=%s]" % wid]
    print("   dmg", [(x["r"], x["d"]) for x in w["dmg"]], "|", w["damageSource"])
    print("   own", dt["curveOwn"], "registry", dt["curveRegistry"], "swap curves", dt["swapCurves"])
    for aid, c in dt["catalogueCheck"].items():
        print("   %-12s %s" % (aid, json.dumps(c)))
