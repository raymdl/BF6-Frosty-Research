"""Build proposed.json (site-shaped fragments) for the four new weapons and the Actuated Module,
plus propose-notes.json (evidence, flags, validation of the extra rules used here)."""
import json, collections, re
from derive import *
import structure

ACE_ID = "actuated_module"
ACE_DESC = "6FC0BDFC"
P = {"data/attachments.json": {}, "data/attachment-tooltips.json": {}, "reference-data/provenance (research repo, optic category mapping)": {}}
A, T = P["data/attachments.json"], P["data/attachment-tooltips.json"]
N = {"weapons": {}, "validation": {}, "ace": {}}
S = strings()


def sig_wb(rec):
    return frozenset((a, o) for src, h, a, o in signature(rec) if src == "WB" and not a.startswith("local:"))


# ---- peers: raw package signatures and in-game names per site id on existing weapons
peers = collections.defaultdict(collections.Counter); namecheck = collections.Counter(); tipcheck = collections.Counter()
ace_rows = []
prec = collections.defaultdict(lambda: collections.defaultdict(list))
for w in ROSTER:
    gph = graph.weapon_graph(w["siteId"], w["folder"], w["stem"])
    hashes = {r["idHash"] & 0xFFFFFFFF: r["attachment"] for r in gph["attachments"]}
    for rec in gph["attachments"]:
        if rec["stem"] == "BTM_ACEModule":
            lb = live_branches(rec); f, notes = raw_fields(rec) if lb else ({}, [])
            dep = [e["source"] for e in gph["equipment"] if e["source"] == rec["attachment"] or (rec["idHash"] & 0xFFFFFFFF) in e["requires"]]
            ace_rows.append({"weapon": w["siteId"], "new": w["new"], "record": rec["route"], "storedCost": rec["cost"], "live": bool(lb),
                             "killSwitch": sorted({"%s/%s default %s" % (b["kill"]["registry"], b["kill"]["row"], b["kill"]["default"]) for b in rec["branches"]}),
                             "physicalSlots": sorted({b["slot"] for b in lb}), "selectors": list(id_selectors(rec)), "raw": f, "notes": notes,
                             "signature": sorted(map(list, sig_wb(rec))), "inOwnAam": own_name(w, rec["attachment"][11:]), "equipmentRules": dep,
                             "siteHasGripSlot": bool(not w["new"] and CAT["WEAPON_ATTS"][w["siteId"]].get("grip"))})
        if w["new"]: continue
        for slot, i in TRUTH.get((w["siteId"], rec["attachment"].lower()), []):
            peers[(slot, i)][sig_wb(rec)] += 1
            pn = own_name(w, rec["attachment"][11:])
            if pn: prec[(slot, id_selectors(rec), pn.lower())][i].append(w["siteId"])
            if slot in ("muzzle", "grip", "laser", "light", "ergo"):
                n = own_name(w, rec["attachment"][11:])
                if n: namecheck["in-game name == catalogue name" if n.lower() == BYID[slot][i]["name"].lower() else "in-game name != catalogue name"] += 1
    if not w["new"]:   # sight tooltip rule check
        d = derive(w)
        by = collections.defaultdict(set)
        for r in d["records"]:
            if r["slot"] == "sight" and r["siteId"] and r.get("uiAssets"):
                c = IDX.consensus(r["uiAssets"])
                if c: by[r["siteId"]].update(c[0])
        for c, site in (TIPS["byWeapon"].get(w["siteId"], {}).get("sight") or {}).items():
            tipcheck["sight tooltip == min id of category members" if by.get(c) and min(by[c]) == site else "sight tooltip differs"] += 1
N["validation"]["nameCheck"] = dict(namecheck); N["validation"]["sightTooltipRule"] = dict(tipcheck)

# ---- Actuated Module
sigs = collections.Counter(json.dumps(r["signature"]) for r in ace_rows if r["live"])
N["ace"] = {"rows": ace_rows, "distinctSignatures": len(sigs), "signature": json.loads(next(iter(sigs))) if sigs else None,
            "strings": {k: S.get(k) for k in ("FCC2C91E", "6FBF09F4", ACE_DESC)}}
A["GRIPS[+]"] = {"id": ACE_ID, "name": "Actuated Module", "pts": 10, "weaponSwayMult": 0.6666667, "frostyModifiers": {}}
T["descriptions/" + ACE_DESC] = S.get(ACE_DESC)
for r in ace_rows:
    if not r["live"]: continue
    f = raw_site_fields("grip", r["raw"])
    A["GRIPS[+]"]["frostyModifiers"][r["weapon"]] = {k: f[k] for k in ("adsTimeTierMod", "adsMoveSpeedTierShift", "sprintRecoveryTierShift", "deployTimeTierShift")}
    if not r["new"]:
        A["WEAPON_ATTS/%s/grip[+]" % r["weapon"]] = ACE_ID
        T["byWeapon/%s/grip/%s" % (r["weapon"], ACE_ID)] = ACE_DESC

# ---- new weapons
for w in ROSTER:
    if not w["new"]: continue
    wid = w["siteId"]; d = derive(w); sel, unres = structure.assign(w, d)
    note = N["weapons"][wid] = {"flags": [], "records": [], "unresolved": [], "skipped": d["skipped"], "peerSignature": collections.Counter()}
    # ACE as a resolved grip
    for r in list(unres):
        if r["stem"] == "BTM_ACEModule":
            r["siteId"] = ACE_ID; r["identity"] = "new catalogue entry (C2)"; sel["grip"][ACE_ID] = r; unres.remove(r)
            r["descriptionIds"] = [ACE_DESC]; r["description"] = S.get(ACE_DESC); r["descriptionBasis"] = "string-table text match; AD_ACEModule not captured"
    # ambiguous selector sets: an existing weapon with the same selector set and the same in-game name decides
    for r in list(unres):
        p = prec.get((r["slot"], tuple(r["selectors"]), (r.get("inGameName") or "").lower()))
        if r.get("candidates") and p and len(p) == 1:
            i, ws = next(iter(p.items()))
            r["siteId"] = i; r["identity"] = "selector + in-game name precedent (%s)" % ",".join(ws); sel[r["slot"]][i] = r; unres.remove(r)
            note["flags"].append("%s %s (%s, %r) identified as %s by precedent on %s (same selector set, same in-game name, same cost)" % (r["slot"], r["stem"], r["cost"], r["inGameName"], i, ",".join(ws)))
    # magazine id collisions
    mags = {}
    basecap = structure.base_capacity(w)
    for r in [r for r in d["records"] if r["slot"] == "mag"]:
        i, e, info = structure.mag_entry(w, r, basecap)
        if info["inGameCapacity"] is not None and info["inGameCapacity"] != e["mag"]:
            note["flags"].append("mag %s: capacity from raw-1 = %s but in-game name says %s" % (r["stem"], e["mag"], info["inGameCapacity"]))
        r["magEntry"], r["magInfo"], r["magId"] = e, info, i
    order = sorted([r for r in d["records"] if r["slot"] == "mag"], key=lambda r: (r["stem"].lower() != "mag_regular", r["stem"]))
    for r in order:
        i, e = r["magId"], r["magEntry"]
        if i in mags:
            if e["reloadSpeedTier"] == 1 and not i.endswith("_fast"):
                i = "%s_fast" % e["mag"]; e["name"] = "%s Fast" % e["mag"]
            if i in mags:
                word = re.sub(r"[^a-z]", "", (r["magInfo"]["inGameName"] or r["stem"]).split()[-1].lower())
                i = "%s_%s" % (e["mag"], word); e["name"] = "%s %s" % (e["mag"], word.capitalize())
            note["flags"].append("mag id collision on %s: %s (%r) given id %s - judgement call" % (wid, r["stem"], r["magInfo"]["inGameName"], i))
        mags[i] = r; r["siteId"] = i
    sel["mag"] = mags
    S_ = structure.build(w, d, sel)
    # per-record catalogue comparison
    for slot in ("muzzle", "barrel", "grip", "laser", "light", "ergo"):
        for i, r in sel.get(slot, {}).items():
            rf = raw_site_fields(slot, r["raw"])
            entry = {"slot": slot, "id": i, "stem": r["stem"], "record": r["attachment"], "cost": r["cost"], "identity": r.get("identity"), "inGameName": r.get("inGameName"), "raw": rf, "notes": r.get("notes")}
            note["records"].append(entry)
            if i == ACE_ID:
                continue
            cat = BYID[slot][i]
            if cat.get("pts") != r["cost"]:
                note["flags"].append("%s %s (%s): stored cost %s, catalogue pts %s" % (slot, i, r["stem"], r["cost"], cat.get("pts")))
            if r.get("inGameName") and slot != "barrel" and r["inGameName"].lower() != cat["name"].lower():
                note["flags"].append("%s %s (%s): in-game name %r differs from catalogue name %r" % (slot, i, r["stem"], r["inGameName"], cat["name"]))
            rec = next(x for x in graph.weapon_graph(wid, w["folder"], w["stem"])["attachments"] if x["attachment"] == r["attachment"])
            ok = sig_wb(rec) in peers[(slot, i)]
            note["peerSignature"]["package effects identical to an existing weapon's %s" % ("" if ok else "- NOT FOUND")] += 1
            if not ok:
                note["flags"].append("%s %s (%s): package effect signature not seen on any existing weapon with this id" % (slot, i, r["stem"]))
            generic = {k: cat.get(k, DEFAULT.get(k, 0)) for k in FIELDS[slot]}
            diff = {k: rf[k] for k in FIELDS[slot] if not eq(generic[k] if generic[k] is not None or k == "recoilDurationOverride" else 0, rf[k])}
            if slot == "grip":
                fm = {k: rf[k] for k in ("adsTimeTierMod", "adsMoveSpeedTierShift", "sprintRecoveryTierShift", "deployTimeTierShift")}
                for k in ("adsRecoilTierMod", "hipRecoilTierMod", "movingAdsSpreadTierMod", "hipSpreadTierMod"):
                    if k in diff:
                        if k == "hipSpreadTierMod" and any("NoBipod" in n for n in r.get("notes", [])):
                            entry["note"] = "catalogue hipSpreadTierMod %s comes from the _NoBipod hip array (kept at catalogue level as on the six existing LMGs)" % generic[k]
                            continue
                        fm = {k: rf[k], **fm}; note["flags"].append("grip %s: raw %s = %s, catalogue %s -> written into frostyModifiers" % (i, k, rf[k], generic[k]))
                A["GRIPS[id=%s]/frostyModifiers/%s" % (i, wid)] = fm
            elif slot == "laser":
                A["LASERS[id=%s]/frostyModifiers/%s" % (i, wid)] = {"hipSpreadTierMod": rf["hipSpreadTierMod"], "movingAdsSpreadTierMod": rf["movingAdsSpreadTierMod"]}
                for k in diff:
                    if k not in ("hipSpreadTierMod", "movingAdsSpreadTierMod"): note["flags"].append("laser %s: raw %s = %s, catalogue %s (no per-weapon field for it)" % (i, k, rf[k], generic[k]))
            elif slot == "barrel":
                A["BARRELS[id=%s]/adsTimeTierModByWeapon/%s" % (i, wid)] = rf["adsTimeTierMod"]
                for k in diff:
                    if k != "adsTimeTierMod": note["flags"].append("barrel %s: raw %s = %s, catalogue %s (no per-weapon field for it)" % (i, k, rf[k], generic[k]))
            elif slot in ("muzzle", "ergo"):
                if diff:
                    A["%s[id=%s]/weaponOverrides/%s" % (CATKEY[slot], i, wid)] = diff
                    entry["override"] = diff
            elif diff:
                note["flags"].append("light %s: raw differs from catalogue %s" % (i, diff))
    note["peerSignature"] = dict(note["peerSignature"])
    for r in unres:
        note["unresolved"].append({"slot": r["slot"], "stem": r["stem"], "record": r["attachment"], "cost": r["cost"], "identity": r.get("identity"), "candidates": sorted(r.get("candidates") or []),
                                   "inGameName": r.get("inGameName"), "selectors": r["selectors"], "raw": raw_site_fields(r["slot"], r["raw"]) if r["slot"] in FIELDS else r["raw"], "notes": r.get("notes"),
                                   "descriptionIds": r.get("descriptionIds")})
    order = lambda slot, ids: sorted(ids, key=lambda i: ORDER_[slot].index(i) if i in ORDER_[slot] else 999)
    ORDER_ = structure.ORDER
    atts = {s: order(s, sel.get(s, {})) for s in ("muzzle", "barrel")}
    atts["barrelDef"] = S_["barrelDef"]
    for s in ("grip", "laser", "light"): atts[s] = order(s, sel.get(s, {}))
    atts["slots"] = S_["slots"]; atts["dependencies"] = S_["dependencies"]
    if S_["sightPoints"]: atts["sightPoints"] = S_["sightPoints"]
    if S_["sightCategories"] != sorted(["iron", "std_optic", "var_low", "var_high", "thermal", "therm_hyb"]):
        atts["sight"] = S_["sightCategories"]; note["flags"].append("sight categories on %s: %s" % (wid, S_["sightCategories"]))
    A["WEAPON_ATTS/" + wid] = atts
    if sel.get("ergo"): A["WEAPON_ERGO/" + wid] = {"avail": order("ergo", sel["ergo"])}
    if S_["accessory"]: A["WEAPON_ACCESSORY/" + wid] = S_["accessory"]
    A["WEAPON_MAG/" + wid] = {"defAds": S_["defAds"], "defAms": S_["defAms"], "def": next((i for i, r in mags.items() if r["stem"].lower() == "mag_regular"), None),
                               "mags": {i: r["magEntry"] for i, r in mags.items()}, "sprintRecoveryBaseIndex": S_["sprintRecoveryBaseIndex"],
                               "deployBaseIndex": S_["deployBaseIndex"], "deployTimeTable": S_["deployTimeTable"]}
    if S_["ironSway"] is not None: A["SIGHTS[id=iron]/weaponSwayMultByWeapon/" + wid] = S_["ironSway"]
    note["structure"] = {k: S_[k] for k in ("sightCosts", "sightUncategorised", "defAdsAnim", "baseIndexSources", "ironSway")}
    note["mags"] = {i: {**r["magInfo"], "stem": r["stem"], "cost": r["cost"], "record": r["attachment"]} for i, r in mags.items()}
    if S_["defAdsAnim"] is not None and S_["defAdsAnim"] != S_["defAds"]: note["flags"].append("ADS animation base index %s != zoom transition index %s" % (S_["defAdsAnim"], S_["defAds"]))
    # tooltips
    tip = collections.defaultdict(dict); missing = []
    for slot in ("muzzle", "barrel", "laser", "light", "grip", "ammo", "mag", "ergo"):
        for i, r in sel.get(slot, {}).items():
            if r.get("descriptionIds"):
                tip[slot][i] = min(r["descriptionIds"])
                if min(r["descriptionIds"]) not in TIPS["descriptions"]: T["descriptions/" + min(r["descriptionIds"])] = r["description"]
            else:
                missing.append("%s/%s (%s; AD not held: %s)" % (slot, i, r["stem"], [a.rsplit("/", 1)[-1] for a in (r.get("uiAssetsNotHeld") or [])] or r.get("uiMethod")))
    by = collections.defaultdict(set); cats = []
    for r in d["records"]:
        if r["slot"] == "sight" and r["siteId"]:
            c = IDX.consensus(r["uiAssets"]) if r.get("uiAssets") else None
            if c: by[r["siteId"]].update(c[0])
    for c, ids in by.items():
        tip["sight"][c] = min(ids)
        if min(ids) not in TIPS["descriptions"]: T["descriptions/" + min(ids)] = S.get(min(ids))
    T["byWeapon/" + wid] = dict(tip); note["tooltipMissing"] = missing
    # optic category mapping fragment
    members = collections.defaultdict(list)
    for r in d["records"]:
        if r["slot"] == "sight":
            members[r["siteId"]].append({"source": next(x["route"] for x in graph.weapon_graph(wid, w["folder"], w["stem"])["attachments"] if x["attachment"] == r["attachment"]),
                                         "label": r["label"], "sourcePointCost": r["cost"], "labelBasis": r["uiMethod"]})
    P["reference-data/provenance (research repo, optic category mapping)"][wid] = [
        {"weapon": wid, "slot": "sight", "attachment": c, "sitePoints": S_["sightPoints"].get(c, structure.SIGHT_PTS.get(c)), "members": m} for c, m in sorted(members.items(), key=str)]
    note["counts"] = {s: len(sel.get(s, {})) for s in ("muzzle", "barrel", "grip", "laser", "light", "ergo", "mag", "ammo")}
    note["counts"]["sights"] = sum(len(m) for m in members.values()); note["counts"]["accessoryRecords"] = sum(r["slot"] == "accessory" for r in d["records"])

json.dump(P, open("proposed.json", "w", encoding="utf-8"), indent=1)
json.dump(N, open("propose-notes.json", "w", encoding="utf-8"), indent=1)
print("validation:", N["validation"])
live = [r for r in ace_rows if r["live"]]
print("ACE records:", len(ace_rows), "live:", len(live), "existing live:", sum(not r["new"] for r in live), "distinct signatures:", len(sigs),
      "costs:", sorted({r["storedCost"] for r in live}), "no grip slot on site:", [r["weapon"] for r in live if not r["new"] and not r["siteHasGripSlot"]],
      "equipment rules:", sum(bool(r["equipmentRules"]) for r in live), "not live:", [r["weapon"] for r in ace_rows if not r["live"]])
for wid, n in N["weapons"].items():
    print("==", wid, n["counts"], n["peerSignature"])
    for f in n["flags"]: print("   FLAG", f[:230])
    for u in n["unresolved"]: print("   UNRESOLVED", u["slot"], u["stem"], u["cost"], u["inGameName"], u["candidates"], json.dumps({k: v for k, v in u["raw"].items() if v not in (0, 1, None)})[:120])
    print("   tooltip missing:", "; ".join(n["tooltipMissing"])[:700])
    print("   WEAPON_MAG:", json.dumps(A["WEAPON_MAG/" + wid])[:1100])
