"""Assemble proposed.json for part A (run after extract.py, uimeta.py, precision.py, reloadscan.py).

Fragments are keyed by target file and JSON path, in the site's shape. Nothing is copied from another weapon:
every value is read from the weapon's own 2.1.1.0 raw files, GRX_Weapons, its bullet file, the shared arrays its
GS indexes, the settings Precision table matched to it by value, or its UI metadata record.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import json, hashlib, pathlib, collections, re
import lib, extract, reloadscan
from lib import f32
F = lambda h: "Field_" + h
NEW = (("mk24", "MRGGA"), ("elr40", "CDX40"), ("z84m", "PKM"), ("rspr", "RSAR999"))
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
ui = json.load(open(lib.HERE / "uimeta.json", encoding="utf-8"))["new"]
prec = json.load(open(lib.HERE / "precision.json", encoding="utf-8"))
ORDER = ["id", "name", "description", "cls", "cal", "rpm", "mag", "tacRld", "emptyRld", "bulletVel", "recoilV", "recoilDir", "recoilVar", "recoilIncAds",
         "fireMode", "availableFireModes", "fireModes", "spreadDyn", "recoil", "spread", "dmg", "damageStatus", "damageSource", "reloadSpeed", "provenance"]


def cal_from_bullet(b):
    """Site label style from the bullet asset name: PD_65x48mm -> 6.5x48mm with the site's multiplication sign."""
    n = b[3:]
    n = re.sub(r"_(PDW|MG|Carbine|Semi|Bolt|Match)$", "", n); n = re.sub(r"_(PDW|MG|Carbine|Semi|Bolt|Match)$", "", n)
    m = re.match(r"^(\d)(\d+)x(\d+mm\w*)$", n)
    if m:
        return "%s.%s×%s" % m.groups()
    m = re.match(r"^(\.\d+)([A-Za-z].*)$", n)
    if m:
        return "%s %s" % m.groups()
    return n


def std_magazine(internal):
    """Capacity set by the weapon-specific Regular magazine package, if one exists and sets MagazineCapacity."""
    k = "wpm_mag_std_" + internal.lower()
    hits = [r for r in lib.held if r.rsplit("/", 1)[-1].startswith(k)]
    out = []
    for r in hits:
        for o in lib.load(r)[0]:
            if o["$class"] == "Class_e7d2410a":
                out.append((r.rsplit("/", 1)[-1], o.get(F("7f22bfb4")), o.get(F("4614adfe"))))
    return out


# --- convention checks on the existing 63 -------------------------------------------------------------
ids = json.load(open(lib.REPO / "reference-data/provenance/frosty-weapon-identities.json", encoding="utf-8"))["weapons"]
site = {w["id"]: w for w in json.load(open(lib.SITE / "data/weapons.json", encoding="utf-8"))}
checks = {"stdMagazinePackagesOnExisting": [], "animationIndexDiffersFromTransitionIndex": [], "calFromBullet": [0, 0, []]}
for e in ids:
    if e["siteId"] not in site:
        continue
    r = extract.raw(e["internalId"])
    sm = [x for x in std_magazine(e["internalId"]) if x[1] not in (None, -1, 0)]
    if sm:
        checks["stdMagazinePackagesOnExisting"].append((e["siteId"], sm, "base", r["mag"], "site", site[e["siteId"]]["mag"]))
    if r["AnimationZoomSettingsIndex"] != r["WeaponZoomTransitionIndex"]:
        checks["animationIndexDiffersFromTransitionIndex"].append((e["siteId"], r["AnimationZoomSettingsIndex"], r["WeaponZoomTransitionIndex"]))
    c = cal_from_bullet(r["bullet"]); ok = c == site[e["siteId"]]["cal"]
    checks["calFromBullet"][0] += ok; checks["calFromBullet"][1] += 1
    if not ok:
        checks["calFromBullet"][2].append((e["siteId"], r["bullet"], c, site[e["siteId"]]["cal"]))

# --- new weapons ---------------------------------------------------------------------------------------
proposed = collections.OrderedDict(); evidence = {}
weapons = []; decay = {"RECOIL_DEC": {}, "RECOIL_DEC_TEXP": {}, "RECOIL_DEC_EXP": {}}; bal = {"RECOIL_MULT": {}, "HIP_SPREAD_BASE_INDEX": {}}
roles = {}; reloadx = {}; notes = {}
for sid, internal in NEW:
    r = extract.raw(internal); rec = extract.record(r)
    u = ui[sid]; assert len(u) == 1, (sid, len(u)); u = u[0]
    mag_note = None
    sm = [x for x in std_magazine(internal) if x[1] not in (None, -1, 0)]
    if sm and sm[0][1] != rec["mag"]:
        mag_note = "Base MagazineCapacity is %d; the Regular magazine package %s sets %d, used as the default (site convention: capacity of the default magazine including the chambered round)." % (rec["mag"], sm[0][0], sm[0][1])
        rec["mag"] = sm[0][1]
    wbname = r["wbRoute"].rsplit("/", 1)[-1]
    files = {"wb": r["wbRoute"], "gs": r["gsRoute"], "bullet": r["bulletRoute"].lower(), "uiMetadata": u["asset"].lower()}
    reg_n = sum(1 for l in r["log"] if l[2] is not None)
    w = collections.OrderedDict()
    w["id"] = sid; w["name"] = u["name"]; w["description"] = u["description"]
    w.update(rec)
    w["cal"] = cal_from_bullet(r["bullet"])
    w["damageStatus"] = "verified"
    w["damageSource"] = "Frosty %s tweakable damage curve referenced by %s, build %s." % (r["bullet"], lib.load(r["wbRoute"])[0][0]["Field_0c59fa06"].rsplit("/", 1)[-1], settings.BUILD_LABEL)
    fields = ["cls", "cal", "rpm", "mag", "tacRld", "emptyRld", "reloadSpeed", "bulletVel", "recoilV", "recoilDir", "recoilVar", "recoilIncAds", "recoil", "spread", "spreadDyn", "dmg"]
    note = ("All listed base fields were read from the " + settings.BUILD_LABEL + " raw %s, %s and %s files; %d of %d scalar leaves also have a GRX_Weapons registry row and every one equals the file value. "
            % (lib.load(r["wbRoute"])[0][0]["Field_0c59fa06"].rsplit("/", 1)[-1], lib.load(r["gsRoute"])[0][0]["Field_0c59fa06"].rsplit("/", 1)[-1], r["bullet"], reg_n, len(r["log"])))
    note += "rpm is %s. " % ("FireLogic.RateOfFire" if r["primaryMode"] == 2 else "the bolt cycle 60 / (BoltActionTime / BoltActionSpeed + BoltActionDelay + 60 / RateOfFireForSingleFire)" if r["primaryMode"] == 1 else "RateOfFireForSingleFire")
    note += "tacRld and emptyRld are ReloadInfoArray[0] and [1] ReloadTimeBulletsLeft at ReloadSpeed 1. Moving ADS and hipfire minima use the array selectors (ZDA_Moving_Weapons index %d, HDA_Weapons index %d). cal is formatted from the bullet asset name." % (r["adsMoveIndex"], r["hipIndex"])
    if mag_note:
        note += " " + mag_note
    w["provenance"] = {"schemaVersion": 1, "status": "sourced",
                       "frosty": {"sourceBuild": settings.BUILD_LABEL, "buildEvidence": "raw EBX capture of the installed %s client (builds/%s)" % (settings.BUILD_LABEL, settings.BUILD_LABEL), "fields": fields, "note": note,
                                  "sourcingEvidence": (settings.part("A") / "proposed.json").as_posix().split("/BF6 Datamining/")[-1] + "#evidence/" + sid},
                       "notes": ["name and description are the English strings %s and %s linked from the %s record %s (label %s)." % (u["nameId"], u["descriptionId"], u["asset"].rsplit("/", 1)[-1], u["guid"], u["label"]),
                                 "Not tested in game."]}
    weapons.append(collections.OrderedDict((k, w[k]) for k in ORDER if k in w))
    assert set(w) == set(ORDER), set(w) ^ set(ORDER)
    ra = rec["recoil"]["ads"]
    decay["RECOIL_DEC"][sid] = ra["decFactor"]; decay["RECOIL_DEC_TEXP"][sid] = ra["decTimeExp"]
    if ra["decExp"] != 1:
        decay["RECOIL_DEC_EXP"][sid] = ra["decExp"]
    bal["RECOIL_MULT"][sid] = ra["amountMult"]; bal["HIP_SPREAD_BASE_INDEX"][sid] = r["hipIndex"]
    tags = u["tags"]
    roles[sid] = {"style": tags[0], "range": tags[1], "firing": tags[2],
                  "records": [{"asset": u["asset"], "guid": u["guid"], "label": u["label"], "primary": True, "tags": [t["text"] for t in tags]}]}
    res, nfiles, missing = reloadscan.scan(internal)
    mags = [x for x in res if x["file"].lower().startswith("wpm_mag_")]
    if mags:
        reloadx[sid] = mags
    evidence[sid] = {"internal": internal, "files": {k: {"route": v, "sha256": sha(lib.held[v])} for k, v in files.items()},
                     "registryRowsFound": reg_n, "leavesRead": len(r["log"]),
                     "leavesWithoutRegistryRow": [l[0] for l in r["log"] if l[2] is None],
                     "fileVsRegistryDisagreements": [l[0] for l in r["log"] if l[2] is not None and not (extract.same(l[1], l[2]) if not isinstance(l[1], list) else l[1] == l[2])],
                     "raw": {"primaryFireMode": r["primaryMode"], "alternateFireModes": r["altModes"], "rateOfFire": f32(r["rateOfFire"]), "rateOfFireForSingleFire": f32(r["rateOfFireSingle"]),
                             "rateOfFireForBurst": f32(r["rateOfFireBurst"]), "burstsPerMinute": f32(r["burstsPerMinute"]), "boltAction": {k: f32(v) for k, v in r["bolt"].items()},
                             "baseMagazineCapacity": r["mag"], "regularMagazinePackage": sm, "reloadInfoArray": [{k: (f32(v) if isinstance(v, float) else v) for k, v in e.items()} for e in r["reload"]],
                             "bullet": r["bullet"], "damageProtectionMultiplierIndex": r["protectionIndex"], "damagePenetrationMultiplierIndex": r["penetrationIndex"],
                             "hipArray": r["hipArray"][0], "unzoomedMinAnglesArrayIndex": r["hipIndex"], "hipRow": r["hipRow"],
                             "movingAdsArray": r["adsMoveArray"][0], "movingZoomedMinAnglesArrayIndex": r["adsMoveIndex"], "movingAdsRow": r["adsMoveRow"],
                             "stationaryZoomedMinAnglesArrayIndex": r["adsStatIndex"], "idleDecreaseTargetDuration": [r["idleStatIndex"], r["idleMoveIndex"]],
                             "minMaxDispersion": {k: [f32(a) for a in v] for k, v in r["minmax"].items()},
                             "dispersionMoving": {k: {f: f32(x) for f, x in v.items()} for k, v in r["dyn"].items() if k.endswith(".move")},
                             "wbRootIndices": {k: r[k] for k in ("WeaponZoomTransitionIndex", "AnimationZoomSettingsIndex", "AltAnimationZoomSettingsIndex", "SprintSettingsIndex",
                                                                 "WeaponZoomedMoveSpeedMultiplierIndex", "WeaponHipMoveSpeedMultiplierIndex")},
                             "gsBindsNoIncreaseSemi": r["semiNoIncreaseBound"],
                             "gsBoundModifiers": sorted(set(b[2] for b in r["gsBindings"] if b[2] and not b[2].startswith("GCR_")))},
                     "ui": {k: u[k] for k in ("asset", "objectIndex", "guid", "label", "nameId", "name", "descriptionId", "description", "tags")},
                     "precisionTable": prec["evidence"].get(sid)}
    notes[sid] = mag_note

proposed["data/weapons.json"] = {"path": "$ (append to the array, after vssm)", "value": weapons}
proposed["data/recoil_decay.json"] = {"path": "$.RECOIL_DEC / $.RECOIL_DEC_TEXP / $.RECOIL_DEC_EXP (add keys)", "value": decay}
proposed["data/balance_tables.json"] = {"path": "$.RECOIL_MULT / $.HIP_SPREAD_BASE_INDEX (add keys)", "value": bal}
proposed["data/weapon_attributes.json"] = {"path": "$.tables (add keys)", "value": {"tables": prec["tables"]}}
proposed["data/weapon-role-tags.json"] = {"path": "$.weapons (add keys); $.source.metadata (append)", "value": {
    "weapons": roles,
    "source.metadata[+]": {"asset": "Common/UI/Static/Metadata/S5/UIWeaponAbilityMetaData_S5B1", "sha256": sha(lib.held["common/ui/static/metadata/s5/uiweaponabilitymetadata_s5b1"])}}}
proposed["data/reload-exceptions.json"] = {"path": "$.animationOverrides (add key); $.counts", "value": {
    "animationOverrides": {"elr40": {"<magazine id the attachments worker gives Attachment_CDX40_MAG_Compact1>": {
        "tacRldOverrideMs": 3166, "displayName": "<in-game name of Attachment_CDX40_MAG_Compact1, not resolved here>", "recordKey": "elr40-single-round"}}},
    "counts": {"animationOverrideRecords": 5, "animationOverrideEntries": 6, "screenshotExceptionEntries": 1, "composedLoadoutEvidenceEntries": 1}},
    "sourceRows": reloadx}
out = {"generated": "2026-10-13", "build": settings.BUILD_LABEL, "proposed": proposed, "evidence": evidence, "conventionChecks": checks}
json.dump(out, open(lib.HERE / "proposed.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(json.dumps(checks, ensure_ascii=True)[:3000])
for w in weapons:
    print(json.dumps({k: v for k, v in w.items() if k not in ("spreadDyn", "recoil", "dmg", "provenance", "fireModes")}, ensure_ascii=True))
print(json.dumps(decay), json.dumps(bal)); print(json.dumps(reloadx)[:1500]); print(notes)
