"""Is 'the weapon's AAM lists the record' the rule that decides whether a live record is a site choice?"""
import collections, re
from derive import *
own = collections.defaultdict(set)   # aam stem lower -> normalized record names
for r in ui.aam_records():
    own[r["aam"].rsplit("/", 1)[-1].lower()[4:]].add(ui.normalized(r["name"]))
tab = collections.Counter(); ex = collections.defaultdict(list)
for w in ROSTER:
    d = derive(w)
    names = own.get(w["stem"].lower(), set())
    for r in d["records"]:
        if r["slot"] in ("sight", "accessory"): continue
        name = r["attachment"][len("Attachment_"):]
        inaam = ui.normalized(name) in names or ui.normalized(ui.without_slot(name)) in names or ui.normalized(re.sub(r"_(RGT|LFT|TOP)_", "_", name)) in names
        onsite = bool(TRUTH.get((w["siteId"], r["attachment"].lower()))) if not w["new"] else "new"
        k = (onsite, inaam, r["stem"] if (onsite is not True or not inaam) else "")
        tab[k] += 1; ex[k].append(w["siteId"])
for k, v in sorted(tab.items(), key=str):
    print(v, k, ",".join(ex[k]) if k[2] else "")
