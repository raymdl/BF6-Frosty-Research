import json, collections, sys
P = "C:/Users/royal/Documents/BF6 Frosty Research/reference-data/provenance/frosty-site-attachment-mapping-2026-09-15.json"
j = json.load(open(P, encoding="utf-8"))
ch = j["choices"]
print(collections.Counter((c["slot"], c.get("mount")) for c in ch))
seen = set()
for c in ch:
    if c["weapon"] == (sys.argv[1] if len(sys.argv) > 1 else "m4a1"):
        k = c["slot"]
        if k in seen and len(sys.argv) < 3: continue
        seen.add(k)
        print(json.dumps(c)[:1800]); print()
print([k for k in j if k not in ("choices",)])
