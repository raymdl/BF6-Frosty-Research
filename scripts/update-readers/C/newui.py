"""AAM records of the four new weapons whose AD asset is not held, plus string-table searches.
python newui.py [search text ...]"""
import sys, json
from rawlib import *
import ui
S = strings()
for r in ui.aam_records():
    if any(k in r["aam"] for k in ("MRGGA", "CDX40", "/PKM/", "RSAR999")) and not r["adHeld"]:
        print("%-12s %-36s %-60s name=%s" % (r["aam"].rsplit("_", 1)[-1], r["name"], (r["adRoute"] or r["adFileGuid"]).split("Attachments/")[-1], json.dumps(r["inGameName"])))
print()
seen = set()
for r in ui.aam_records():
    if "ACE Module" in r["name"] or "DD Vertical" in r["name"]:
        k = (r["name"].split(" - ")[-1], json.dumps(r["inGameName"]))
        if k not in seen:
            seen.add(k); print(k)
print(sorted({r["aam"].rsplit("_", 1)[-1] for r in ui.aam_records() if "ACE Module" in r["name"]}))
for q in sys.argv[1:]:
    for k, v in S.items():
        if q.lower() in v.lower():
            print(q, "|", k, "|", v[:160])
