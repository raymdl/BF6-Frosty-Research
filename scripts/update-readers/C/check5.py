import json, collections
from derive import *
print("coverage:", json.dumps(TIPS["coverage"])[:700])
print("source:", json.dumps(TIPS["source"])[:300])
# AAM-listed ACE Module vs attachment records
N = json.load(open("propose-notes.json", encoding="utf-8"))
rec = {r["weapon"] for r in N["ace"]["rows"] if r["live"]}
bystem = {w["stem"].lower(): w["siteId"] for w in ROSTER}
aam = collections.defaultdict(set)
for r in ui.aam_records():
    if "ACE Module" in r["name"] or "acemodule" in ui.normalized(r["name"]):
        aam[r["aam"].rsplit("/", 1)[-1][4:]].add(r["name"])
print("AAM stems listing ACE:", {k: bystem.get(k.lower()) for k in sorted(aam)})
listed = {bystem.get(k.lower()) for k in aam}
print("record+AAM:", sorted(rec & listed)); print("record, no AAM:", sorted(rec - listed)); print("AAM, no record:", sorted(x for x in listed - rec if x), "non-site:", [k for k in aam if k.lower() not in bystem])
print("site weapons with neither:", sorted(set(bystem.values()) - rec - listed))
# existing-weapon ammo records not on site, and elr40 / z84m ergos
for w in ("elr40",):
    print([(r["id"], r["stem"], r["cost"], r.get("override")) for r in N["weapons"][w]["records"] if r["slot"] in ("ergo", "light", "muzzle")])
print([e["id"] for e in CAT["ERGOS"]], [e["id"] for e in CAT["LIGHTS"]])
