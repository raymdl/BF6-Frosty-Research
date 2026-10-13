"""Build raw-attachment -> site-id identity maps from the reviewed mapping of the 63 existing weapons
(research repo: frosty-site-attachment-mapping-2026-09-15.json, 3,361 choice rows with their raw sources).

Keys tried, from most to least specific. A key is usable when it maps to exactly one site id on
every existing weapon that has it.
  stem      slot + attachment stem after the weapon prefix (BTM_KACVerticalGrip)
  selector  slot + sorted selector unlock names (U_WPM_BTM_Vertical04_W35)
  sel+cost  slot + selectors + stored point cost
Run directly to print the ambiguity report.
"""
import json, collections, re, pathlib
REPO = pathlib.Path("C:/Users/royal/Documents/BF6 Frosty Research")
SITE = pathlib.Path("C:/Users/royal/Documents/BF6 Weapon Analyzer")
MAPPING = REPO / "reference-data/provenance/frosty-site-attachment-mapping-2026-09-15.json"


def stem_of(path, internal=None):
    s = pathlib.PurePosixPath(path.split("#")[0]).stem
    s = re.sub(r"^(Attachment_|U_PRG_)", "", s, flags=re.I)
    # weapon prefix = first token (weapon names have no underscore except none observed)
    return s.split("_", 1)[1] if "_" in s else s


def load_choices():
    j = json.load(open(MAPPING, encoding="utf-8"))
    rows = []
    for c in j["choices"]:
        if c["slot"] == "sight":
            continue
        for s in c["sources"]:
            if not s.get("abilityBranches"):
                continue
            sels = tuple(sorted(x["asset"].rsplit("/", 1)[-1] for x in s.get("selectors", [])))
            cost = int(s["rawPointCost"], 16) if s.get("rawPointCost") else None
            rows.append({"weapon": c["weapon"], "slot": c["slot"], "id": c["attachment"], "stem": stem_of(s["source"]),
                         "selectors": sels, "cost": cost, "sitePoints": c["sitePoints"], "source": s["source"],
                         "desc": c.get("descriptionIds"), "kind": s.get("kind")})
    return rows


def build(rows, exclude_weapon=None):
    maps = {k: collections.defaultdict(collections.Counter) for k in ("stem", "selector", "selcost", "stemsel")}
    for r in rows:
        if r["weapon"] == exclude_weapon:
            continue
        maps["stem"][(r["slot"], r["stem"].lower())][r["id"]] += 1
        maps["selector"][(r["slot"], r["selectors"])][r["id"]] += 1
        maps["selcost"][(r["slot"], r["selectors"], r["cost"])][r["id"]] += 1
        maps["stemsel"][(r["slot"], r["stem"].lower(), r["selectors"])][r["id"]] += 1
    return maps


SITE_SLOT = {"AttachmentCategory_Muzzle": "muzzle", "AttachmentCategory_Barrel": "barrel", "AttachmentCategory_BottomRail": "grip",
             "AttachmentCategory_Magazine": "mag", "AttachmentCategory_Ammunition": "ammo", "AttachmentCategory_MagazineWell": "ergo"}


def lookup(maps, slot, stem, selectors, cost):
    """Return (site id or None, method, candidates)."""
    sels = tuple(sorted(selectors))
    for name, key in (("stem+selector", ("stemsel", (slot, stem.lower(), sels))), ("selector+cost", ("selcost", (slot, sels, cost))),
                      ("selector", ("selector", (slot, sels))), ("stem", ("stem", (slot, stem.lower())))):
        c = maps[key[0]].get(key[1])
        if c and len(c) == 1:
            return next(iter(c)), name, dict(c)
        if c and name == "stem":
            return None, "ambiguous " + name, dict(c)
    amb = maps["selector"].get((slot, sels))
    return None, "new" if not amb else "ambiguous selector", dict(amb or {})


if __name__ == "__main__":
    rows = load_choices()
    print(len(rows), "source rows;", collections.Counter(r["slot"] for r in rows))
    maps = build(rows)
    for name in ("stem", "selector", "selcost", "stemsel"):
        m = maps[name]
        amb = {k: v for k, v in m.items() if len(v) > 1}
        print("== %s: %d keys, %d ambiguous" % (name, len(m), len(amb)), collections.Counter(k[0] for k in amb))
        for k, v in sorted(amb.items(), key=str)[:400 if name in ("selcost", "stemsel") else 0]:
            print("   ", k, dict(v))
    cc = collections.Counter((r["slot"], r["cost"] == r["sitePoints"]) for r in rows)
    print("stored cost == site points:", dict(cc))
    for r in rows:
        if r["cost"] != r["sitePoints"]:
            print("   cost differs", r["weapon"], r["slot"], r["id"], r["stem"], r["cost"], r["sitePoints"])
