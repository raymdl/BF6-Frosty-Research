import json, collections
from rawlib import REPO
j = json.load(open(REPO / "reference-data/provenance/frosty-handling-mapping-followup.json", encoding="utf-8"))
print({k: (len(v) if isinstance(v, (list, dict)) else str(v)[:200]) for k, v in j.items()})
ex = j["excludedSourceAttachments"]
print(json.dumps(ex[0])[:600])
c = collections.Counter()
for r in ex:
    c[(r["attachmentXml"].rsplit("/", 1)[-1].split("_", 2)[-1][:28], str(r.get("reason", r.get("status", "")))[:110])] += 1
for k, v in sorted(c.items()): print(v, k)
