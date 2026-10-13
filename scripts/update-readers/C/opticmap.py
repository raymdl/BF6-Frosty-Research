"""Site optic-category mapping vs raw 2.1.1.0 sights. python opticmap.py [weapon] -> label diffs; no arg -> totals."""
import sys, json, glob, collections
from derive import *
p = sorted(glob.glob(str(REPO / "reference-data/provenance/frosty-optic-category-mapping-*.json")))[-1]
J = json.load(open(p, encoding="utf-8"))
print(p.rsplit("\\", 1)[-1], {k: (len(v) if isinstance(v, list) else str(v)[:80]) for k, v in J.items()})
print(json.dumps(J["categories"][0])[:700])
site = {}
for c in J["categories"]:
    for m in c["members"]:
        site[(c["weapon"], m["source"].rsplit("/", 1)[-1].rsplit(".", 1)[0].lower())] = (c["attachment"], m["label"], m.get("sourcePointCost", c.get("sourcePointCost")))
C = collections.Counter(); ex = collections.defaultdict(list)
only = sys.argv[1:] or None
for w in ROSTER:
    if w["new"] or (only and w["siteId"] not in only): continue
    d = derive(w); seen = set()
    for r in d["records"]:
        if r["slot"] != "sight": continue
        k = (w["siteId"], r["attachment"].lower()); seen.add(k)
        s = site.get(k)
        if not s: C["raw sight not in site mapping"] += 1; ex["raw sight not in site mapping"].append("%s:%s:%s" % (w["siteId"], r["stem"], r["label"])); continue
        C["category " + ("ok" if s[0] == r["siteId"] else "MISMATCH")] += 1
        if s[0] != r["siteId"]: ex["category"].append("%s:%s raw %s site %s" % (w["siteId"], r["stem"], r["siteId"], s[0]))
        C["label " + ("ok" if s[1] == r["label"] else "MISMATCH")] += 1
        if s[1] != r["label"]: ex["label"].append("%s:%s raw %r site %r" % (w["siteId"], r["stem"], r["label"], s[1]))
    for k in site:
        if k[0] == w["siteId"] and k not in seen:
            C["site member not a live raw sight"] += 1; ex["site member not a live raw sight"].append("%s:%s:%s" % (k[0], k[1][-22:], site[k][1]))
for k, v in sorted(C.items()): print(v, k)
for k, v in ex.items(): print(k, len(v), "; ".join(v[:14])[:900])
