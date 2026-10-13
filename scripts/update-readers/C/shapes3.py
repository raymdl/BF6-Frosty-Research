import json, collections
from derive import *
c = collections.defaultdict(list)
for w, a in CAT["WEAPON_ATTS"].items():
    c["slots " + json.dumps(a.get("slots"))].append(w)
    c["deps " + json.dumps(a.get("dependencies"))[:700]].append(w)
    c["extra keys " + json.dumps(sorted(set(a) - {"muzzle", "barrel", "barrelDef", "grip", "laser", "light", "slots", "dependencies"}))].append(w)
    if "sightPoints" in a: c["sightPoints " + json.dumps(a["sightPoints"])].append(w)
    if "sight" in a: c["sight " + json.dumps(a["sight"])].append(w)
    m = CAT["WEAPON_MAG"][w]
    c["mag keys " + json.dumps(sorted(set(m) - {"mags"}))].append(w)
    c["deployTimeTable " + str(m.get("deployTimeTable"))].append(w)
for w, a in CAT["WEAPON_ACCESSORY"].items():
    c["acc " + json.dumps(a)[:600]].append(w)
for k, v in sorted(c.items()):
    print(len(v), k, "<-", ",".join(v[:5]))
