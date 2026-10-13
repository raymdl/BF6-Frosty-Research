"""Side finding: the Interdictor Precision table in 2.1.1.0 against the site's stored table."""
import json
import lib, precision
a = json.load(open(lib.SITE / "data/weapon_attributes.json", encoding="utf-8"))["tables"]
for k in ("interdictor", "l115", "m2010esr"):
    print("site", k, json.dumps(a[k])[:600])
for t in precision.tables():
    if abs(t["source"]["bulletVelocity"] - 732.7392) < 0.01 or abs(t["source"]["bulletVelocity"] - 742) < 0.01 and t["source"]["magazine"] == 6:
        print("2.1.1.0 object", t["objectIndex"], t["guid"], json.dumps(t["source"]), "base", json.dumps(t["base"]), "rows", json.dumps(t["rows"]))
