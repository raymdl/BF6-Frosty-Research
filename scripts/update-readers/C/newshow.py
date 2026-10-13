"""Compact view of the new weapons' records. python newshow.py [all]  (default: only unresolved / flagged)"""
import sys, json
from derive import *
import structure
full = len(sys.argv) > 1
print("tooltip slots on m4a1:", list(TIPS["byWeapon"]["m4a1"]), "| on m2010esr:", list(TIPS["byWeapon"]["m2010esr"]))
for w in ROSTER:
    if not w["new"]: continue
    d = derive(w); sel, unres = structure.assign(w, d)
    print("==", w["siteId"], "records", len(d["records"]), "skipped", [(s["stem"], s["cost"], s["reason"][:12]) for s in d["skipped"]])
    for r in d["records"]:
        if r["slot"] in ("sight", "accessory"): continue
        flag = r["siteId"] is None or r.get("notes") or not r.get("descriptionIds")
        if full or flag:
            raw = {k: v for k, v in r["raw"].items() if v not in (0, None)}
            print("  %-6s %-28s %3s -> %-16s %-22s name=%-22r desc=%s raw=%s %s" % (r["slot"], r["stem"][:28], r["cost"], r["siteId"], (r.get("identity") or "")[:22], r.get("inGameName"),
                  (r.get("descriptionIds") or ["-"])[0], json.dumps(raw)[:150], ("cand=%s" % sorted(r["candidates"]) if r["siteId"] is None and r.get("candidates") else "") + " ".join(r.get("notes", []))[:160]))
