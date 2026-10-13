"""Regenerate attachment data for existing site weapons from raw 2.1.1.0 files and diff against the site.
python validate.py [siteId ...]   (default: all 63).  Writes validate.json."""
import sys, json, collections
from derive import *

def base_capacity(wb):
    found = []
    def walk(x):
        if isinstance(x, dict):
            if isinstance(x.get("Field_7f22bfb4"), int): found.append(x["Field_7f22bfb4"])
            for c in x.values(): walk(c)
        elif isinstance(x, list):
            for c in x: walk(c)
    for o in load(wb)[0]: walk(o)
    return sorted(set(found))

def run(ids):
    C = collections.Counter(); mism = []
    per = {}
    for wid in ids:
        w = BY_SITE[wid]; d = derive(w)
        gph = graph.weapon_graph(wid, w["folder"], w["stem"])
        c = collections.Counter()
        def bad(kind, *a):
            c[kind + " MISMATCH"] += 1; mism.append((wid, kind) + a)
        got = collections.defaultdict(dict)
        basecap = base_capacity("common/hardware/weapons/" + w["folder"].lower() + "/" + w["stem"].lower() + "_wb")
        for r in d["records"]:
            slot = r["slot"]
            if slot in ("sight", "accessory"):
                continue
            truth = TRUTH.get((wid, r["attachment"].lower()), [])
            if not truth:
                bad("record not on site", r["stem"], r["cost"], r.get("siteId")); continue
            tslot, tid = truth[0]
            if len(truth) > 1:
                c["record mapped to %d site ids" % len(truth)] += 1
            if slot == "mag" and r["siteId"] is None:
                c["identity mag (by capacity)"] += 1
            elif r["siteId"] == tid and slot == tslot:
                c["identity ok"] += 1
            elif r["siteId"] is None:
                c["identity unresolved"] += 1; mism.append((wid, "identity unresolved", r["stem"], r["cost"], tid, r["identity"], sorted(r["candidates"])))
            else:
                bad("identity", r["stem"], r["cost"], "got " + str(r["siteId"]), "site " + tid, r["identity"])
            for tslot, tid in truth:
                got[tslot][tid] = r
                if tslot == "ammo":
                    continue
                # cost
                if tslot == "mag":
                    pts = CAT["WEAPON_MAG"][wid]["mags"][tid]["pts"]
                else:
                    e = BYID[tslot][tid]; pts = (e.get("weaponOverrides") or {}).get(wid, {}).get("pts", e.get("pts"))
                if pts == r["cost"]: c["cost ok"] += 1
                else: bad("cost", tslot, tid, "raw %s" % r["cost"], "site %s" % pts)
                # effects
                se = site_effective(wid, tslot, tid); rf = raw_site_fields(tslot, r["raw"])
                for k in FIELDS[tslot]:
                    sv = se.get(k, DEFAULT.get(k, 0))
                    if sv is None and k != "recoilDurationOverride": sv = 0
                    if eq(sv, rf[k]): c["field ok"] += 1
                    else: bad("field", tslot, tid, k, "raw %s" % rf[k], "site %s" % sv, "; ".join(r["notes"])[:160])
                if tslot == "mag":
                    m = CAT["WEAPON_MAG"][wid]["mags"][tid]["mag"]
                    raw = r["raw"].get("magCapacityRaw")
                    c["mag capacity: %s" % ("package raw-1" if raw is not None and raw - 1 == m else "package raw" if raw == m else
                                              "base raw-1" if raw is None and any(b - 1 == m for b in basecap) else "base raw" if raw is None and m in basecap else "OTHER")] += 1
                    if raw is not None and raw - 1 != m and raw != m or raw is None and not any(b - 1 == m or b == m for b in basecap):
                        mism.append((wid, "mag capacity", tid, "package %s" % raw, "base %s" % basecap, "site %s" % m))
                # tooltip
                tip = TIPS["byWeapon"].get(wid, {}).get(tslot, {}).get(tid)
                mine = min(r["descriptionIds"]) if r.get("descriptionIds") else None
                if tip == mine: c["tooltip ok" if tip else "tooltip absent both"] += 1
                else: bad("tooltip", tslot, tid, "raw %s" % mine, "site %s" % tip, str(r.get("uiMethod")), str(r.get("uiAssetsNotHeld"))[:120])
        # lists
        A = CAT["WEAPON_ATTS"][wid]
        for slot in ("muzzle", "barrel", "grip", "laser", "light"):
            s, g = set(A.get(slot, [])) - {"none"}, set(got[slot])
            if s == g: c["list ok"] += 1
            else: bad("list", slot, "site only %s" % sorted(s - g), "raw only %s" % sorted(g - s))
        s = set((CAT["WEAPON_ERGO"].get(wid) or {}).get("avail", [])) - {"none"}
        if s == set(got["ergo"]): c["list ok"] += 1
        else: bad("list", "ergo", "site only %s" % sorted(s - set(got["ergo"])), "raw only %s" % sorted(set(got["ergo"]) - s))
        s = set(CAT["WEAPON_MAG"][wid]["mags"])
        if s == set(got["mag"]): c["list ok"] += 1
        else: bad("list", "mag", "site only %s" % sorted(s - set(got["mag"])), "raw only %s" % sorted(set(got["mag"]) - s))
        per[wid] = dict(c); C.update(c)
    return C, mism, per

if __name__ == "__main__":
    ids = sys.argv[1:] or [w["siteId"] for w in ROSTER if not w["new"]]
    C, mism, per = run(ids)
    for k, v in sorted(C.items()): print("%6d  %s" % (v, k))
    kinds = collections.Counter(m[1] for m in mism)
    print(dict(kinds))
    for m in mism: print("  ", " | ".join(str(x) for x in m)[:330])
    json.dump({"totals": dict(C), "perWeapon": per, "mismatches": mism}, open("validate.json", "w", encoding="utf-8"), indent=1)
