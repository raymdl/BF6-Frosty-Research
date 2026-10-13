"""Sights of one weapon: label, category, cost, kill, and which accessory families permit them."""
import sys, json, collections
from derive import *
wid = sys.argv[1]; w = BY_SITE[wid]; d = derive(w)
perm = collections.defaultdict(set)
for e in d["equipment"]:
    fam = e["source"].split("_SCA_")[-1] if "_SCA_" in e["source"] else e["source"][-18:]
    for h in e["requires"]:
        perm[d["byHash"].get(h)].add(fam[:9])
for r in d["records"]:
    if r["slot"] == "sight":
        print("%-30s %-3s %-9s %-18r %-34s %s" % (r["stem"][:30], r["cost"], r["siteId"], r["label"], r["uiMethod"], ",".join(sorted(perm.get(r["attachment"], [])))))
for s in d["skipped"]:
    if s["category"] in ("Sight", "OpticAccessory"): print("skipped", s["stem"], s["reason"], ",".join(sorted(perm.get(s["attachment"], []))))
print("equipment sources:", [e["source"].split("_", 2)[-1] for e in d["equipment"]])
print("site:", json.dumps(CAT["WEAPON_ACCESSORY"].get(wid))[:500])
