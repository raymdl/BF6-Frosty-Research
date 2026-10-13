"""Weapon UI metadata: name, description and the three role tags per weapon record (Class_593f6146).

Reads every UIWeaponAbilityMetaData* file held in the 2.1.1.0 captures, validates names, descriptions and
role tags against the site for existing weapons, then prints the four new weapons. Writes uimeta.json.
"""
import json, re, hashlib, pathlib
import lib
F = lambda h: "Field_" + h


def sid(objs, ref):
    """(string id hex upper, text) behind a pointer to a Class_fbe1d3bc object."""
    if not isinstance(ref, dict):
        return None, None
    _, o = lib.deref(ref, objs)
    if o is None:
        return None, None
    v = o.get(F("3d34898a"))
    if v is None:
        return None, None
    h = "%08X" % (v & 0xffffffff) if isinstance(v, int) else str(v).upper()
    return h, lib.string(h)


def internal_of(o, objs):
    for f in ("ebe3976f", "53078b86"):
        x = o.get(F(f))
        for cand in (x if isinstance(x, list) else [x]):
            i = lib.imp(cand) if isinstance(cand, dict) else None
            if i and i[0]:
                m = re.search(r"T_UI_(.+?)_PKG", i[0])
                if m:
                    return m.group(1), i[0]
    return None, None


def records():
    out = []
    for route in sorted(r for r in lib.held if "uiweaponabilitymetadata" in r):
        objs, _, a = lib.load(route)
        name = objs[0].get(F("0c59fa06"), route)
        for i, o in enumerate(objs):
            if o["$class"] != "Class_593f6146":
                continue
            nm = sid(objs, o.get(F("fd698f51"))); ds = sid(objs, o.get(F("490f0dd0")))
            tags = [sid(objs, t) for t in (o.get(F("8c7f991f")) or [])]
            internal, img = internal_of(o, objs)
            cat = None
            cr = o.get(F("f8c63ce7"))
            if isinstance(cr, dict):
                r2, co = lib.deref(cr, objs)
                if co is not None:
                    cat = (r2 or "") + "|" + str(co.get(F("55aded8d")) or co.get(F("0c59fa06")) or co.get("$class"))
            out.append({"asset": name, "file": lib.held[route], "objectIndex": i, "guid": o.get("$guid"), "label": o.get(F("55aded8d")),
                        "internal": internal, "image": img, "nameId": nm[0], "name": nm[1], "descriptionId": ds[0], "description": ds[1],
                        "tags": [{"id": t[0], "text": t[1]} for t in tags], "category": cat})
    return out


if __name__ == "__main__":
    recs = records()
    ids = json.load(open(lib.REPO / "reference-data/provenance/frosty-weapon-identities.json", encoding="utf-8"))["weapons"]
    site = {w["id"]: w for w in json.load(open(lib.SITE / "data/weapons.json", encoding="utf-8"))}
    roles = json.load(open(lib.SITE / "data/weapon-role-tags.json", encoding="utf-8"))["weapons"]
    norm = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower())
    byint = {}
    for r in recs:
        byint.setdefault(norm(r["internal"] or r["label"]), []).append(r)
    print("metadata files:", sorted(set(r["asset"] for r in recs)), "records:", len(recs))
    cnt = {"name": [0, 0], "description": [0, 0], "roleTags": [0, 0], "roleRecordGuid": [0, 0]}
    notes = []
    for e in ids:
        s = e["siteId"]
        if s not in site:
            continue
        rs = byint.get(norm(e["internalId"]), [])
        if not rs:
            # label fallback (GRT-CPS 'GrotC'): match by resolved name
            rs = [r for r in recs if r["name"] == site[s]["name"]]
        prim = [r for r in rs if r["image"]] or rs
        ok_name = any(r["name"] == site[s]["name"] for r in rs)
        ok_desc = any(r["description"] == site[s]["description"] for r in rs)
        want = [roles[s][g] for g in ("style", "range", "firing")]
        ok_tags = any([(t["id"], t["text"]) for t in r["tags"]] == [((w or {}).get("id"), (w or {}).get("text")) for w in want] for r in rs)
        guids = {x["guid"] for x in roles[s].get("records", [])}
        ok_guid = guids <= {r["guid"] for r in rs} and bool(guids)
        for k, ok in (("name", ok_name), ("description", ok_desc), ("roleTags", ok_tags), ("roleRecordGuid", ok_guid)):
            cnt[k][0] += ok; cnt[k][1] += 1
            if not ok:
                notes.append((s, k, [(r["asset"].rsplit("/", 1)[-1], r["label"], r["name"], r["descriptionId"], [t["text"] for t in r["tags"]]) for r in rs],
                              site[s]["name"] if k == "name" else site[s]["description"][:60] if k == "description" else [w and w["text"] for w in want]))
    print("validation (matches of 63):", {k: "%d/%d" % tuple(v) for k, v in cnt.items()})
    for n in notes:
        print("  MISMATCH", json.dumps(n, ensure_ascii=False)[:700])
    new = {}
    for s, internal in (("mk24", "MRGGA"), ("elr40", "CDX40"), ("z84m", "PKM"), ("rspr", "RSAR999")):
        rs = byint.get(norm(internal), [])
        new[s] = rs
        print("==", s, internal, len(rs))
        for r in rs:
            print(json.dumps({k: v for k, v in r.items() if k != "file"}, ensure_ascii=False, indent=1))
            print("   file sha256", hashlib.sha256(pathlib.Path(r["file"]).read_bytes()).hexdigest())
    json.dump({"validation": cnt, "new": new}, open(lib.HERE / "uimeta.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
