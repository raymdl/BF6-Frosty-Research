import json, collections, sys
from derive import *
P = json.load(open("proposed.json", encoding="utf-8")); A = P["data/attachments.json"]
N = json.load(open("propose-notes.json", encoding="utf-8"))
for k, v in A.items():
    if "weaponOverrides" in k or "SIGHTS" in k or "BARRELS" in k: print(k, json.dumps(v))
for wid in ("mk24", "z84m"):
    for r in N["weapons"][wid]["records"]:
        if r["id"] in ("qd_grip_pod", "adj_angled", "full_angled"): print(wid, r["id"], r["stem"], [n for n in r["notes"] if "conditional" not in n])
print(json.dumps([{k: v for k, v in e.items() if k not in ("weaponOverrides",)} for e in CAT["MUZZLES"] if e["id"] in ("dp_brake", "tp_brake", "sp_brake", "light_supp", "cqb_supp")])[:2200])
c = collections.Counter()
for w in ROSTER:
    if w["new"]: continue
    gph = graph.weapon_graph(w["siteId"], w["folder"], w["stem"])
    for rec in gph["attachments"]:
        for slot, i in TRUTH.get((w["siteId"], rec["attachment"].lower()), []):
            if slot in ("muzzle", "grip", "laser", "light", "ergo"):
                n = own_name(w, rec["attachment"][11:])
                if n and n.lower() != BYID[slot][i]["name"].lower(): c[(slot, i, n)] += 1
            if rec["stem"] in ("BTM_BTGrippodQD", "BTM_BT_Grippod_QD", "BTM_HFGA", "BTM_MagpulAFG2", "BTM_Magpul_AFG2") and slot == "grip":
                f, _ = raw_fields(rec); c[("RAWRECOIL", w["cls"], i, f.get("adsRecoilTierMod"))] += 1
for k, v in sorted(c.items(), key=str): print(v, k)
w = BY_SITE["rspr"]; d = derive(w)
for r in d["records"]:
    if r["stem"] in ("RGT_ModuleMk3",): print(r["uiMethod"], [(a.rsplit("/", 1)[-1], IDX.desc.get(a, {}).get("description", {}).get("id")) for a in r["uiAssets"]])
print({w_: TIPS["byWeapon"][w_]["light"].get("ads_taclight") for w_ in ("m4a1", "kv9", "sgx", "ef88", "m240l")})
print({k: v[:90] for k, v in TIPS["descriptions"].items() if not re.fullmatch(r"[0-9A-F]{8}", k)}.__len__(), [k for k in TIPS["descriptions"] if not re.fullmatch(r"[0-9A-F]{8}", k)][:6])
