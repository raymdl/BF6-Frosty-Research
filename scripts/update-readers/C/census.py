"""Census over all cached weapon graphs: categories, slots, effect assets with their operands."""
import json, collections, sys
import weapons, graph
R = weapons.roster()
cats = collections.Counter(); eff = collections.defaultdict(collections.Counter); kills = collections.Counter(); holders = collections.Counter()
for w in R:
    gph = graph.weapon_graph(w["siteId"], w["folder"], w["stem"])
    for a in gph["attachments"]:
        cats[(a["category"], tuple(sorted({b["slot"] for b in a["branches"]})))] += 1
        for b in a["branches"]:
            if b["kill"]["default"]:
                kills[a["stem"]] += 1
            for s in b["selectors"]:
                for e in s["effects"]:
                    op = {k: v for k, v in (e.get("operand") or {}).items() if k != "scalars"}
                    key = (e["src"], e.get("holder", ""), e.get("class"), "local" if e.get("local") else e["asset"])
                    eff[key][json.dumps(op or e.get("values"), sort_keys=True)[:230]] += 1
for k, v in sorted(cats.items(), key=str): print(v, k)
print("killed by default:", dict(kills))
for k, v in sorted(eff.items(), key=str):
    if len(sys.argv) > 1 and not any(s.lower() in str(k).lower() for s in sys.argv[1:]):
        continue
    print(k, sum(v.values()))
    for vv, n in v.most_common(3):
        print("      ", n, vv)
