"""Magazine capacity evidence and barrel default evidence, compact. python magshow.py <siteId> ..."""
import sys, json
from derive import *
import structure
for wid in sys.argv[1:]:
    w = BY_SITE[wid]; d = derive(w)
    print(wid, "base", structure.base_capacity(w), "site def", (CAT["WEAPON_MAG"].get(wid) or {}).get("def"), "barrelDef", (CAT["WEAPON_ATTS"].get(wid) or {}).get("barrelDef"))
    for r in d["records"]:
        if r["slot"] in ("mag", "barrel"):
            t = TRUTH.get((wid, r["attachment"].lower()), [])
            print("   %-6s %-22s cost %-3s capRaw %-5s site %-22s name=%r prog=%s raw=%s" % (r["slot"], r["stem"], r["cost"], r["raw"].get("magCapacityRaw"), t[0][1] if t else None, r.get("inGameName"),
                  r.get("progression"), {k: v for k, v in r["raw"].items() if v not in (0, None)}))
