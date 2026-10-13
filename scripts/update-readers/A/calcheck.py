"""Site `cal` labels by base bullet asset (existing 63), and the bullet assets of the four new weapons."""
import json, collections
import lib, extract
ids = json.load(open(lib.REPO / "reference-data/provenance/frosty-weapon-identities.json", encoding="utf-8"))["weapons"]
site = {w["id"]: w for w in json.load(open(lib.SITE / "data/weapons.json", encoding="utf-8"))}
m = collections.defaultdict(lambda: collections.defaultdict(list))
for e in ids:
    if e["siteId"] in site:
        r = extract.raw(e["internalId"])
        m[r["bullet"]][site[e["siteId"]]["cal"]].append(e["siteId"])
for b in sorted(m):
    print(b, "->", json.dumps({k: v for k, v in m[b].items()}, ensure_ascii=True))
for internal in ("MRGGA", "CDX40", "PKM", "RSAR999"):
    r = extract.raw(internal)
    print("NEW", internal, r["bullet"], "| same bullet asset on site:", json.dumps(dict(m.get(r["bullet"], {})), ensure_ascii=True))
