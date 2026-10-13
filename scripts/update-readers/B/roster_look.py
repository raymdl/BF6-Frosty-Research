"""Exploration: which ammunition attachments does the site offer, against what the files hold?"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import json, pathlib, sys
import common as c
HERE = settings.part("B")
d = json.load(open(HERE / "derived.json", encoding="utf-8"))
site = json.load(open(c.SITE / "data/ammo.json", encoding="utf-8"))["WEAPON_AMMO"]
MAP = {"FMJ": "standard", "Tungsten": "penetration", "Frangible": "frangible", "HollowPoint": "hollow_pt",
       "BallisticTip": "synthetic", "PolymerCase": "lightweight", "Polymer_Case": "lightweight", "PolymerLinks": "lightweight?",
       "Match": "long_range", "MatchTungsten": "range_pen", "Subsonic": "subsonic", "SubsonicHollowPoint": "subsonic_hp",
       "SubsonicTungsten": "subsonic_pen", "SubsonicFrangible": "subsonic_frangible?",
       "Buckshot": "buckshot", "No00Buckshot": "buckshot_00", "Flechette": "flechette", "Slugs": "slugs"}
for wid, w in d["weapons"].items():
    if len(sys.argv) > 1 and wid not in sys.argv[1:]:
        continue
    s = site.get(wid, {})
    print("==", wid, w["internalId"], "site def", s.get("def"), "site", s.get("ammo"), "presets", w["defaultPresetCount"])
    for a in w["ammo"]:
        br = a["branches"]
        print("   %-20s %-20s cost %-3s list %s branches %d kill %s local %s slot %s default %s anyPreset %s sel %s" % (
            a["suffix"], MAP.get(a["suffix"], "??"), a["pointCost"], a["pointCostList"], len(br),
            [b["killSwitchDefault"] for b in br], [b["killLocalFallback"] for b in br], [b["slot"] for b in br],
            a["inDefaultPreset"], a["inAnyPreset"], [b["selectors"] for b in br]))
