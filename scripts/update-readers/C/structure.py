"""Site-shaped per-weapon structure (WEAPON_ATTS / WEAPON_ERGO / WEAPON_ACCESSORY / WEAPON_MAG / sight data)
built from derive() output.  python structure.py  -> compares all 63 existing weapons with the site."""
import sys, json, collections, re
from derive import *

ORDER = {s: [e["id"] for e in CAT[k]] for s, k in CATKEY.items()}
SIGHT_PTS = {e["id"]: e["pts"] for e in CAT["SIGHTS"]}


def base_capacity(w):
    found = []
    def walk(x):
        if isinstance(x, dict):
            if isinstance(x.get("Field_7f22bfb4"), int): found.append(x["Field_7f22bfb4"])
            for c in x.values(): walk(c)
        elif isinstance(x, list):
            for c in x: walk(c)
    for o in load("common/hardware/weapons/" + w["folder"].lower() + "/" + w["stem"].lower() + "_wb")[0]: walk(o)
    return sorted(set(found))


def mag_entry(w, r, basecap, minus_one=True):
    f = raw_site_fields("mag", r["raw"])
    raw = r["raw"].get("magCapacityRaw")
    src = "magazine package" if raw is not None else "weapon base"
    if raw is None:
        raw = basecap[0] if len(basecap) == 1 else None
    cap = None if raw is None else raw - (1 if minus_one else 0)
    if cap == 0:   # single-shot: the one stored round is the chambered round
        cap = raw
    fast = f["reloadSpeedTier"] == 1
    ign = r.get("inGameName") or ""
    m = re.match(r"(\d+)rnd", ign)
    info_name = {"inGameName": ign or None, "inGameCapacity": int(m.group(1)) if m else None}
    if ign:
        fast = "fast" in ign.lower()
    if m and cap is None:
        cap = int(m.group(1))
    e = {"name": "%s %s" % (cap, "Fast" if fast else "Rnd"), "pts": r["cost"], "mag": cap, "adsTimeTierShift": f["adsTimeTierShift"],
         "sprintRecoveryTierShift": f["sprintRecoveryTierShift"], "adsMoveSpeedTierShift": f["adsMoveSpeedTierShift"],
         "reloadSpeedTier": f["reloadSpeedTier"], "deployTimeTierShift": f["deployTimeTierShift"], "movingAdsSpreadTierMod": f["movingAdsSpreadTierMod"]}
    if f["weaponSwayMult"] != 1:
        e["weaponSwayMult"] = f["weaponSwayMult"]
    return "%s_%s" % (cap, "fast" if fast else "rnd"), e, {"capacityRaw": raw, "capacitySource": src, **info_name}


def assign(w, d):
    """slot -> id -> record.  Existing weapons: the reviewed mapping; new weapons: resolved identity."""
    out = collections.defaultdict(dict); unresolved = []
    basecap = base_capacity(w)
    for r in d["records"]:
        if r["slot"] in ("sight", "accessory"):
            continue
        if not w["new"]:
            for slot, i in TRUTH.get((w["siteId"], r["attachment"].lower()), []):
                out[slot][i] = r
        elif r["slot"] == "mag":
            i, e, info = mag_entry(w, r, basecap)
            r["magEntry"], r["magInfo"] = e, info
            out["mag"][i] = r
        elif r["siteId"]:
            out[r["slot"]][r["siteId"]] = r
        else:
            unresolved.append(r)
    return out, unresolved


def build(w, d, sel):
    wid = w["siteId"]; S = {}
    lookup = {}   # attachment name -> (slot, id)
    for slot, m in sel.items():
        for i, r in m.items():
            lookup.setdefault(r["attachment"], (slot, i))
    sights = [r for r in d["records"] if r["slot"] == "sight"]
    accs = [r for r in d["records"] if r["slot"] == "accessory"]
    for r in sights: lookup[r["attachment"]] = ("sight", r["siteId"])
    for r in accs: lookup[r["attachment"]] = ("accessory", r["siteId"])
    # slots
    phys = collections.defaultdict(set)
    for t in ("grip", "laser", "light"):
        for r in sel.get(t, {}).values():
            for p in r["physicalSlots"]: phys[p].add(t)
    groups = []
    for ts in phys.values():
        merged = set(ts)
        for g in [g for g in groups if g & merged]:
            merged |= g; groups.remove(g)
        groups.append(merged)
    for t in ("grip", "laser", "light"):
        if not any(t in g for g in groups): groups.append({t})
    S["slots"] = {(next(iter(g)) if len(g) == 1 else "rail"): {"accepts": sorted(g)} for g in sorted(groups, key=sorted)}
    # dependencies
    deps = collections.defaultdict(set); perm = collections.defaultdict(list)
    for e in d["equipment"]:
        src = lookup.get(e["source"])
        if not src or src[1] is None: continue
        names = {d["byHash"].get(h) for h in e["requires"]}
        perm[src].append(names)
        for n in names:
            t = lookup.get(n)
            if t and t[1]: deps[src].add(t)
    S["dependencies"] = [{"slot": s, "attachment": a, "requiresAny": [{"slot": x, "attachment": y} for x, y in sorted(v)]} for (s, a), v in sorted(deps.items())]
    # accessories
    avail = [a for a in ("canted_irons", "secondary_optic", "ag_coating") if any(r["siteId"] == a for r in accs)]
    exc = {}
    for a in sorted(avail):
        cats = {y for x, y in deps.get(("accessory", a), ()) if x == "sight"}
        allowed = set().union(*perm.get(("accessory", a), [set()]))
        for c in sorted(cats):
            labels = sorted({r["label"] for r in sights if r["siteId"] == c and r["label"] and r["attachment"] not in allowed})
            if labels: exc.setdefault(a, {})[c] = labels
    S["accessory"] = ({"avail": avail, **({"excludedSights": exc} if exc else {})}) if avail else None
    # sights
    cats = collections.defaultdict(set)
    for r in sights: cats[r["siteId"]].add(r["cost"])
    S["sightCategories"] = sorted(c for c in cats if c)
    S["sightUncategorised"] = sorted(r["stem"] for r in sights if not r["siteId"])
    S["sightCosts"] = {c: sorted(v) for c, v in sorted(cats.items(), key=str)}
    S["sightPoints"] = {c: min(v) for c, v in sorted(cats.items(), key=str) if c and len(v) == 1 and min(v) != SIGHT_PTS[c]}
    irons = [r for r in sights if r["siteId"] == "iron"]
    sw = {r["raw"].get("weaponSwayMult") for r in irons} - {None}
    S["ironSway"] = next(iter(sw)) if len(sw) == 1 else None
    # barrel / magazine defaults
    S["barrelDef"] = next((i for i in ("basic", "heavy") if i in sel.get("barrel", {})), None)
    reg = [i for i, r in sel.get("mag", {}).items() if r["stem"].lower() == "mag_regular"]
    S["magDef"] = reg[0] if len(reg) == 1 else None
    b = d["baseIndices"]
    def val(n):
        e = b.get(n) or {}
        return e.get("registry", e.get("file"))
    S["defAds"] = val("WeaponZoomTransitionIndex"); S["defAdsAnim"] = val("AnimationZoomSettingsIndex")
    S["defAms"] = val("WeaponZoomedMoveSpeedMultiplierIndex"); S["sprintRecoveryBaseIndex"] = val("SprintSettingsIndex")
    dp = d["deploy"]
    S["deployBaseIndex"] = dp[0]["index"] if len(dp) == 1 else None
    S["deployTimeTable"] = {"DTA_Weapons": "primary", "DTA_Sidearms": "sidearm"}.get(dp[0]["array"]) if len(dp) == 1 else None
    S["baseIndexSources"] = b
    return S


if __name__ == "__main__":
    C = collections.Counter(); bad = []
    for w in ROSTER:
        if w["new"]: continue
        wid = w["siteId"]; d = derive(w); sel, _ = assign(w, d); S = build(w, d, sel)
        A, M = CAT["WEAPON_ATTS"][wid], CAT["WEAPON_MAG"][wid]
        def cmp(name, got, site):
            if got == site: C[name + " ok"] += 1
            else: C[name + " MISMATCH"] += 1; bad.append((wid, name, json.dumps(got)[:260], json.dumps(site)[:260]))
        cmp("slots", S["slots"], A.get("slots"))
        cmp("dependencies", S["dependencies"] or None, A.get("dependencies"))
        cmp("accessory", S["accessory"], CAT["WEAPON_ACCESSORY"].get(wid))
        cmp("sight list", S["sightCategories"], sorted(A.get("sight", ["iron", "std_optic", "var_low", "var_high", "thermal", "therm_hyb"])))
        cmp("sightPoints", S["sightPoints"], A.get("sightPoints", {}))
        cmp("iron sway", S["ironSway"], CAT["SIGHTS"][0]["weaponSwayMultByWeapon"].get(wid))
        cmp("barrelDef", S["barrelDef"], A.get("barrelDef"))
        cmp("mag def", S["magDef"], M["def"])
        cmp("defAds", S["defAds"], M["defAds"]); cmp("defAms", S["defAms"], M["defAms"])
        if S["defAdsAnim"] is not None: cmp("defAds anim==fov", S["defAdsAnim"], S["defAds"])
        cmp("sprintRecoveryBaseIndex", S["sprintRecoveryBaseIndex"], M["sprintRecoveryBaseIndex"])
        cmp("deployBaseIndex", S["deployBaseIndex"], M["deployBaseIndex"]); cmp("deployTimeTable", S["deployTimeTable"], M["deployTimeTable"])
        basecap = base_capacity(w)
        for i, r in sel.get("mag", {}).items():
            a, e, info = mag_entry(w, r, basecap, True); b_, e2, _ = mag_entry(w, r, basecap, False)
            C["mag id %s" % ("raw-1" if a == i else "raw" if b_ == i else "OTHER")] += 1
            if a != i and b_ != i: bad.append((wid, "mag id", a, i, r["stem"]))
            site = M["mags"][i]
            C["mag name %s" % ("ok" if site["name"] in (e["name"], e2["name"]) else "OTHER")] += 1
            if site["name"] not in (e["name"], e2["name"]): bad.append((wid, "mag name", e["name"], site["name"]))
    for k, v in sorted(C.items()): print("%5d %s" % (v, k))
    for b in bad: print("  ", " | ".join(str(x) for x in b)[:600])
