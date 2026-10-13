import json, collections, sys
from derive import *
def recoil_effects(wid, stems):
    w = BY_SITE[wid]; gph = graph.weapon_graph(wid, w["folder"], w["stem"])
    for rec in gph["attachments"]:
        if rec["stem"] in stems:
            for b in live_branches(rec):
                for s in b["selectors"]:
                    for e in s["effects"]:
                        op = e.get("operand") or {}
                        if any(k in op for k in ("adsRecoil", "hipSpread", "movingAdsSpread")):
                            print(wid, rec["stem"], s["unlock"], e["src"], e.get("holder"), e["asset"], {k: op[k] for k in op if k not in ("scalars",)}, e.get("bindIndex"))
recoil_effects("mk24", {"BTM_HFGA", "BTM_MagpulAFG2", "BTM_BTGrippodQD"})
recoil_effects("m4a1", {"BTM_HFGA", "BTM_MagpulAFG2"})
recoil_effects("elr40", {"MZL_CDX-40CDX64Suppressor", "MZL_MagnusUltra50Suppressor"})
recoil_effects("l115", {"MZL_MagnusUltra50Suppressor"})
for e in CAT["GRIPS"]:
    if e["id"] == "qd_grip_pod":
        print({k: v for k, v in e.items() if k != "frostyModifiers"}, {w: f for w, f in e["frostyModifiers"].items() if len(f) > 4}, e.get("weaponOverrides"))
for w in ROSTER:
    if w["new"]: continue
    gph = graph.weapon_graph(w["siteId"], w["folder"], w["stem"])
    for rec in gph["attachments"]:
        for slot, i in TRUTH.get((w["siteId"], rec["attachment"].lower()), []):
            n = own_name(w, rec["attachment"][11:])
            if slot == "muzzle" and n in ("CQB Suppressor", "Multi-port Brake", "Long Suppressor") and w["cls"] == "Sniper Rifle":
                print(w["siteId"], rec["stem"], rec["cost"], i, n, id_selectors(rec))
w = BY_SITE["elr40"]
gph = graph.weapon_graph("elr40", w["folder"], w["stem"])
print([(r["stem"], r["cost"], id_selectors(r), own_name(w, r["attachment"][11:])) for r in gph["attachments"] if r["category"] == "Muzzle"])
