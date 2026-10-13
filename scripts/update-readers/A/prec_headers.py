"""2.1.1.0 Precision tables: does each table's header (the weapon values stored with it) still equal the
weapon's current values? Lists every header field that differs from the matched site weapon."""
import json
import lib, precision as P
site = json.load(open(lib.SITE / "data/weapons.json", encoding="utf-8"))
tabs = P.tables()
rows = []
for t in tabs:
    ranked = sorted(((len(P.matches(t["source"], P.site_fields(w))), w["id"]) for w in site), reverse=True)
    score, wid = ranked[0]
    w = next(x for x in site if x["id"] == wid); sf = P.site_fields(w)
    ok = set(P.matches(t["source"], sf))
    diff = {k: (t["source"][k], sf.get(k)) for k in t["source"] if k not in ok}
    rows.append((wid, score, ranked[1], diff, t))
print("tables", len(tabs))
for wid, score, runner, diff, t in sorted(rows, key=lambda r: -len(r[3])):
    keyed = [r for r in t["rows"] if r["valid"]]
    if diff or wid in ("interdictor", "ef88", "brod3", "mk24", "elr40", "z84m", "rspr", "l115"):
        print(wid, "score", score, "runner-up", runner, "| header vs weapon differs:", diff, "| keyed rows", len(keyed),
              "panel range", (min(r["panel"] for r in keyed), max(r["panel"] for r in keyed)) if keyed else None,
              "| fallback", [r["panel"] for r in t["rows"] if not r["valid"]])
