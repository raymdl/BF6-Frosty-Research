"""Per-weapon Precision tables (data/weapon_attributes.json tables/<id>) from the raw 2.1.1.0 settings file.

Raw port of the research repo's scripts/frosty-precision-tables.py (which reads the XML export):
container Class_fe5894b1.Field_d0874615 -> Class_0fd27406 objects; rows at
Field_4da34085/Field_f028b424/Field_59491962. Tables are matched to weapons by value (rpm, recoil amount,
multiplier, decrease, min angle, duration, velocity, reload, damage, magazine), as the original script does.
Validates against the site's 63 tables, then writes the tables of the four new weapons to precision.json.
"""
import json, collections
import lib, extract
from lib import f32
F = lambda h: "Field_" + h
SETTINGS = "common/gamesetup/gameconfigurations/glaciergameconfiguration/settings"
OBJ = {"rpm": "5bd8006c", "adsRecoilAmount": "22810b21", "adsRecoilAmountMult": "50b8fd5b", "adsRecoilDecrease": "28df1cde",
       "adsMinAngle": "ac3cfd53", "recoilDuration": "5a02dd65", "bulletVelocity": "e5bb1946", "tacticalReload": "85ff24a0", "damage": "91bb7b5f"}
ROW = {"amountSum": "b521b248", "variationSum": "303e9335", "rpm": "14c4a054", "minAngle": "ac3cfd53", "duration": "5a02dd65", "decrease": "28df1cde", "panel": "aee62a28"}
FLAGS = ("5d2f3411", "b2922d79", "dfde0349", "1c1c4149", "d55c6d70", "9aefcaf4")


def i32(v):
    if isinstance(v, float) and v == int(v):
        v = int(v)
    return v - (1 << 32) if isinstance(v, int) and v >= 1 << 31 else v


def site_fields(w):
    ads = (w.get("recoil") or {}).get("ads") or {}
    return {"rpm": w.get("rpm"), "adsRecoilAmount": ads.get("amount"), "adsRecoilAmountMult": ads.get("amountMult"), "adsRecoilDecrease": ads.get("decFactor"),
            "adsMinAngle": w.get("recoilIncAds"), "recoilDuration": ads.get("duration"), "bulletVelocity": w.get("bulletVel"),
            "tacticalReload": w.get("tacRld"), "damage": (w.get("dmg") or [{}])[0].get("d"), "magazine": w.get("mag")}


def matches(src, site):
    return [k for k, v in src.items() if site.get(k) is not None and abs(v - site[k]) <= max(1e-3, abs(v) * 2e-3)]


def tables():
    objs, _, _ = lib.load(SETTINGS)
    parents = [o for o in objs if o["$class"] == "Class_fe5894b1"]
    assert len(parents) == 1, len(parents)
    out = []
    for idx, ref in enumerate(parents[0][F("d0874615")]):
        _, o = lib.deref(ref, objs)
        src = {k: o[F(h)] for k, h in OBJ.items()}; src["magazine"] = i32(o[F("7f22bfb4")])
        rows = []
        for r in o[F("4da34085")][F("f028b424")][F("59491962")]:
            v = {k: f32(r[F(h)]) for k, h in ROW.items()}
            v["amountSum"] = i32(r[F(ROW["amountSum"])]); v["variationSum"] = i32(r[F(ROW["variationSum"])])
            v["valid"] = any(r[F(f)] is True for f in FLAGS)
            rows.append(v)
        base = {"amountSum": i32(o[F("22ce7cf3")]), "variationSum": i32(o[F("303e9335")]), "rpm": f32(o[F(OBJ["rpm"])]),
                "minAngle": f32(o[F(OBJ["adsMinAngle"])]), "duration": f32(o[F(OBJ["recoilDuration"])]), "decrease": f32(o[F(OBJ["adsRecoilDecrease"])])}
        extra = {"primaryMode": o.get(F("16e6fa59")), "altModes": o.get(F("9b956c3d")), "rateOfFire": f32(o.get(F("14c4a054"))),
                 "rateOfFireSingle": f32(o.get(F("be31b12d"))), "longRangeDamage": f32(o.get(F("6f62f682"))),
                 "animationZoomSettingsIndex": o.get(F("ae4adc54")), "sprintSettingsIndex": o.get(F("5198399a")),
                 "spotMinimap": f32(o.get(F("c9493eaf"))), "spotWorld": f32(o.get(F("9918e670")))}
        out.append({"objectIndex": idx, "guid": o.get("$guid"), "source": {k: f32(v) for k, v in src.items()}, "base": base, "rows": rows, "extra": extra})
    return out


if __name__ == "__main__":
    site = json.load(open(lib.SITE / "data/weapons.json", encoding="utf-8"))
    attrs = json.load(open(lib.SITE / "data/weapon_attributes.json", encoding="utf-8"))
    new = []
    NEW = (("mk24", "MRGGA"), ("elr40", "CDX40"), ("z84m", "PKM"), ("rspr", "RSAR999"))
    for sid, internal in NEW:
        r = extract.raw(internal); rec = extract.record(r); rec["id"] = sid
        new.append(rec)
    weapons = site + new
    tabs = tables(); assigned = {}; problems = []
    for t in tabs:
        ranked = sorted(((len(matches(t["source"], site_fields(w))), w["id"]) for w in weapons), reverse=True)
        (score, wid), (runner, rid) = ranked[0], ranked[1]
        t["match"] = {"id": wid, "score": score, "runnerUp": [rid, runner], "matchedFields": matches(t["source"], site_fields(next(w for w in weapons if w["id"] == wid)))}
        if score - runner < 2 or wid in assigned:
            problems.append((t["objectIndex"], t["guid"], ranked[:3], t["source"]))
            continue
        assigned[wid] = t
    print("tables in settings:", len(tabs), "| assigned:", len(assigned), "| problems:", len(problems))
    for p in problems:
        print("  PROBLEM", json.dumps(p)[:600])
    same = lambda a, b: extract.same(a, b)
    ok = collections.Counter(); bad = []
    for wid, st in attrs["tables"].items():
        t = assigned.get(wid)
        if t is None:
            bad.append((wid, "no table matched")); continue
        b_ok = set(st["base"]) == set(t["base"]) and all(same(st["base"][k], t["base"][k]) for k in st["base"])
        r_ok = len(st["rows"]) == len(t["rows"]) and all(set(a) == set(b) and all(same(a[k], b[k]) for k in a) for a, b in zip(st["rows"], t["rows"]))
        ok["base"] += b_ok; ok["rows"] += r_ok; ok["rowCount"] += len(st["rows"]) == len(t["rows"])
        if not b_ok:
            bad.append((wid, "base", st["base"], t["base"]))
        if not r_ok:
            diff = [(i, a, b) for i, (a, b) in enumerate(zip(st["rows"], t["rows"])) if not (set(a) == set(b) and all(same(a[k], b[k]) for k in a))]
            bad.append((wid, "rows", len(st["rows"]), len(t["rows"]), diff[:2]))
    print("site tables:", len(attrs["tables"]), "| base equal:", ok["base"], "| all rows equal:", ok["rows"], "| row count equal:", ok["rowCount"])
    for b in bad:
        print("  MISMATCH", json.dumps(b)[:900])
    out = {}
    for sid, _ in NEW:
        t = assigned.get(sid)
        print("==", sid, "matched" if t else "NOT MATCHED", json.dumps({k: t[k] for k in ("objectIndex", "guid", "match", "source", "base", "extra")} if t else None)[:1200])
        if t:
            print("   rows:", len(t["rows"]), json.dumps(t["rows"][:3])[:500])
            out[sid] = t
    json.dump({"validation": {"siteTables": len(attrs["tables"]), "baseEqual": ok["base"], "rowsEqual": ok["rows"], "mismatches": bad},
               "tables": {k: {"base": v["base"], "rows": v["rows"]} for k, v in out.items()},
               "evidence": {k: {x: v[x] for x in ("objectIndex", "guid", "match", "source", "extra")} for k, v in out.items()}},
              open(lib.HERE / "precision.json", "w", encoding="utf-8"), indent=1)
