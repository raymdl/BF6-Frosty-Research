"""Validate derived.json (2.1.1.0 raw) against the site's current data for the 63 existing weapons, then build
proposed.json for the four new weapons with the same functions. Writes validation.json and proposed.json.

Site rules reproduced (sources: site scripts frosty-hit-zones.py / frosty-ballistics.py / frosty-collateral.py, docs):
  ammo id        Frosty attachment suffix after _AMO_ (AMMO_BY_SUFFIX of frosty-hit-zones.py; PolymerLinks added here)
  cost           attachment Field_6ee865a5
  default        ammunition attachment id listed in the Equipment preset flagged Field_b656da95
  ballistics     base = WB primary projectile; ammo = swap projectile if the ammo selects one, else base
  hit zones      head = grid(projectile material -> head material)[protection index + protection steps];
                 limb = grid(projectile material -> limb material)[0] (abdomen must be equal)
  collateral     table10[clamp(penetration index + sum of penetration steps, 0, 9)]
  dmg            projectile health curve (Field_2ad7e688 flat pairs; registry XYValues where a row exists)
  recoil tiers   site ads/hipRecoilTierMod = GS recoil amount steps of the ammo (catalogue value merged with effectOverrides)
  subsonic       velocity factor 0.8^tier -> subsonic-tier treatment
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import json, math, pathlib, collections
import common as c

HERE = settings.part("B")
d = json.load(open(HERE / "derived.json", encoding="utf-8"))
P = d["projectiles"]
S = lambda name: json.load(open(c.SITE / "data" / name, encoding="utf-8"))
site_ammo = S("ammo.json"); site_ball = S("ballistics.json"); site_hz = S("hit_zones.json")
site_bal = S("balance_tables.json"); site_weapons = {w["id"]: w for w in S("weapons.json")}
CATALOG = {a["id"]: a for a in site_ammo["AMMO"]}
TABLE10 = [0.0, 0.166667, 0.25, 0.333334, 0.500001, 0.571429, 0.666667, 0.750001, 0.833334, 1.0]
SUFFIX = {"FMJ": "standard", "Tungsten": "penetration", "Frangible": "frangible", "HollowPoint": "hollow_pt",
          "BallisticTip": "synthetic", "PolymerCase": "lightweight", "Polymer_Case": "lightweight",
          "Match": "long_range", "MatchTungsten": "range_pen", "Subsonic": "subsonic",
          "SubsonicHollowPoint": "subsonic_hp", "SubsonicTungsten": "subsonic_pen",
          "Buckshot": "buckshot", "No00Buckshot": "buckshot_00", "Flechette": "flechette", "Slugs": "slugs"}
NEW_SUFFIX = {"PolymerLinks": "lightweight"}   # judgement call, see REPORT.md
NEW = ["mk24", "elr40", "z84m", "rspr"]
NEW_CLS = {"mk24": "Assault Rifle", "elr40": "Sniper Rifle", "z84m": "LMG", "rspr": "SMG"}
ORDER = [a["id"] for a in site_ammo["AMMO"]]


def resolve(wid, w, suffix_map):
    """Everything the site stores, per ammo attachment that has exactly one ability branch."""
    issues = []
    base = w["baseProjectile"]; bp = P[base]
    prot, pen = w["protectionIndex"]["live"], w["penetrationIndex"]["live"]
    z = bp["zones"]
    out = {"base": base, "protectionIndex": prot, "projectileMaterial": bp["material"], "ammo": {}, "unmapped": [], "issues": issues}
    if "error" in z:
        issues.append("base zones: " + z["error"]); return out
    out["headshot"] = z["head"][prot] if 0 <= prot < len(z["head"]) else None
    out["limb"] = z["limb"][0]
    if len(z["limb"]) != 1 or z["abdomen"] != z["limb"]:
        issues.append("limb/abdomen records differ for material %d" % bp["material"])
    for a in w["ammo"]:
        aid = suffix_map.get(a["suffix"])
        if aid is None:
            out["unmapped"].append(a["suffix"]); continue
        if len(a["branches"]) != 1:
            issues.append("%s: %d ability branches" % (a["attachment"], len(a["branches"]))); continue
        b = a["branches"][0]
        swaps = sorted({s["projectile"] for s in b["swaps"]})
        if len(swaps) > 1:
            issues.append("%s: conflicting swaps %s" % (a["attachment"], swaps)); continue
        proj = swaps[0] if swaps else base
        zz = P[proj]["zones"]
        idx = prot + b["protectionSteps"]
        cidx = pen + sum(b["penetrationSteps"])
        vel = b["velocityFactors"]
        rec = {"attachment": a["attachment"], "cost": a["pointCost"], "default": a["inDefaultPreset"], "kill": b["killSwitchDefault"],
               "projectile": proj, "swapVia": sorted({s["via"] for s in b["swaps"]}), "protectionSteps": b["protectionSteps"],
               "headshot": zz["head"][idx] if "head" in zz and 0 <= idx < len(zz["head"]) else None,
               "limb": zz["limb"][0] if "limb" in zz else None,
               "penetrationSteps": b["penetrationSteps"], "collateralIndex": cidx, "collateral": TABLE10[max(0, min(9, cidx))],
               "adsRecoil": b["recoil"]["adsAmount"], "hipRecoil": b["recoil"]["hipAmount"],
               "adsRecoilVar": b["recoil"]["adsVariation"], "hipRecoilVar": b["recoil"]["hipVariation"],
               "recoilAssets": b.get("recoilAssets", []),
               "velocity": vel, "adsMoveSpeedSteps": b["adsMoveSpeedSteps"], "regenDelayAdd": b["regenDelayAdd"],
               "spot2D": b["spot2D"], "spot3D": b["spot3D"], "other": b["other"], "selectors": b["selectors"], "branchIssues": b["issues"]}
        out["ammo"].setdefault(aid, []).append(rec)
    return out


def num(x):
    return int(x) if float(x).is_integer() else x


def site_dmg(curve):
    """Site shape: whole numbers are written without a decimal point in weapons.json (0, 21, 80)."""
    return [{"r": num(r), "d": num(dd), "source": "Frosty"} for r, dd in curve]


def dmg_at(points, r):
    """Site contract: clamp outside, linear between distinct ranges, at a repeated range the earlier value wins."""
    if r <= points[0][0]:
        return points[0][1]
    for i in range(1, len(points)):
        (r0, d0), (r1, d1) = points[i - 1], points[i]
        if r <= r1:
            if r1 == r0:
                continue
            return d0 + (d1 - d0) * (r - r0) / (r1 - r0)
    return points[-1][1]


def same_function(a, b):
    xs = sorted({p[0] for p in a} | {p[0] for p in b})
    probe = set()
    for x in xs:
        probe.update((x, x + 0.5, max(0, x - 0.5)))
    probe.update((0, 500))
    return all(abs(dmg_at(a, r) - dmg_at(b, r)) < 1e-6 for r in probe)


def tier_of(factor):
    t = math.log(factor) / math.log(0.8)
    return round(t) if abs(t - round(t)) < 1e-3 else None


val = collections.OrderedDict((k, {"checked": 0, "match": 0, "mismatches": []}) for k in (
    "ammo roster (site choice has a raw attachment)", "ammo point cost", "default ammo", "kill switch stored false on site choices",
    "ballistics base projectile", "ballistics ammo projectile", "projectile gravity/drag/guid", "hit zones protectionIndex",
    "hit zones projectileMaterial", "hit zones base headshot/limb", "hit zones ammo headshot/limb", "collateral",
    "dmg curve (exact points)", "dmg curve (same function)", "ammo recoil tier (ads, hip)", "subsonic velocity treatment",
    "projectile override dmg (shotgun 00 buck / slugs)", "muzzle velocity vs site bulletVel", "catalogue effects (regen, spot, ADS move)"))


def chk(name, ok, detail):
    v = val[name]; v["checked"] += 1
    if ok: v["match"] += 1
    else: v["mismatches"].append(detail)


extras = collections.Counter(); extras_list = []
resolved = {}
for wid, w in d["weapons"].items():
    if w.get("isNew"):
        continue
    r = resolve(wid, w, {**SUFFIX, "PolymerLinks": "polymer_links(not on site)", "SubsonicFrangible": "subsonic_frangible(not on site)"})
    resolved[wid] = r
    sa = site_ammo["WEAPON_AMMO"][wid]; sb = site_ball["weapons"][wid]; sh = site_hz["weapons"][wid]
    sc = site_bal["COLLATERAL_MULT_OVERRIDE"][wid]; sw = site_weapons[wid]
    for iss in r["issues"]:
        print("ISSUE", wid, iss)
    # ---- roster / cost / default
    defaults = [aid for aid, recs in r["ammo"].items() if any(x["default"] for x in recs)]
    chk("default ammo", defaults == [sa["def"]], "%s: site %s raw %s" % (wid, sa["def"], defaults))
    for aid, cost in sa["ammo"].items():
        recs = r["ammo"].get(aid)
        chk("ammo roster (site choice has a raw attachment)", bool(recs), "%s/%s: no raw attachment" % (wid, aid))
        if not recs:
            continue
        # two attachments can map to one site id (M240L Polymer_Case and none other); all must agree
        keyf = lambda x: (x["cost"], x["projectile"], x["headshot"], x["limb"], x["collateral"], x["adsRecoil"], x["hipRecoil"])
        if len({keyf(x) for x in recs}) != 1:
            print("NOTE", wid, aid, "attachments disagree:", [(x["attachment"],) + keyf(x) for x in recs])
        x = recs[0]
        chk("ammo point cost", x["cost"] == cost, "%s/%s: site %s raw %s" % (wid, aid, cost, x["cost"]))
        chk("kill switch stored false on site choices", x["kill"] is False, "%s/%s: kill switch %s" % (wid, aid, x["kill"]))
        chk("ballistics ammo projectile", sb["ammo"].get(aid) == x["projectile"], "%s/%s: site %s raw %s" % (wid, aid, sb["ammo"].get(aid), x["projectile"]))
        sz = sh["ammo"].get(aid, {})
        chk("hit zones ammo headshot/limb", (sz.get("headshot"), sz.get("limb")) == (x["headshot"], x["limb"]),
            "%s/%s: site %s/%s raw %s/%s" % (wid, aid, sz.get("headshot"), sz.get("limb"), x["headshot"], x["limb"]))
        chk("collateral", sc.get(aid) == x["collateral"], "%s/%s: site %s raw %s (index %s + %s)" % (wid, aid, sc.get(aid), x["collateral"], w["penetrationIndex"]["live"], x["penetrationSteps"]))
        eff = dict(CATALOG[aid]); eff.update(sa.get("effectOverrides", {}).get(aid, {}))
        site_rec = (eff.get("adsRecoilTierMod", 0), eff.get("hipRecoilTierMod", 0))
        chk("ammo recoil tier (ads, hip)", site_rec == (x["adsRecoil"], x["hipRecoil"]),
            "%s/%s: site %s raw %s via %s" % (wid, aid, site_rec, (x["adsRecoil"], x["hipRecoil"]), x["recoilAssets"]))
        vt = sa.get("velocityTreatments", {}).get(aid)
        facs = [v["factor"] for v in x["velocity"] if v["factor"] != 1.0]   # the slug packages carry a 1.0 factor
        if vt or facs:
            mvv = w["muzzleVelocity"]; base_v = mvv["registry"] if mvv["registry"] is not None else mvv["file"]
            if vt and vt["kind"] == "subsonic-tier":
                ok = len(facs) == 1 and tier_of(facs[0]) == vt["subsonicVelocityTier"]
            elif vt and "subsonicVelocityMps" in vt:   # absolute: base muzzle velocity x factor (factor is not a power of 0.8)
                ok = len(facs) == 1 and tier_of(facs[0]) is None and abs(base_v * facs[0] - vt["subsonicVelocityMps"]) < 2e-3
            else:
                ok = False
            chk("subsonic velocity treatment", ok, "%s/%s: site %s raw %s" % (wid, aid, json.dumps(vt), json.dumps(x["velocity"])))
        cat_ok = (eff.get("healthRegenDelayAddS", 0) == sum(x["regenDelayAdd"])
                  and (eff.get("worldSpotMult") or 1) == (x["spot3D"][0] if x["spot3D"] else 1)
                  and abs((eff.get("minimapSpotMult") or 1) - (x["spot2D"][0] if x["spot2D"] else 1)) < 1e-6
                  and eff.get("adsMoveSpeedTierShift", 0) == -sum(x["adsMoveSpeedSteps"]))
        chk("catalogue effects (regen, spot, ADS move)", cat_ok, "%s/%s: site regen %s world %s minimap %s adsMove %s | raw regen %s 3D %s 2D %s adsMove %s" % (
            wid, aid, eff.get("healthRegenDelayAddS"), eff.get("worldSpotMult"), eff.get("minimapSpotMult"), eff.get("adsMoveSpeedTierShift"),
            x["regenDelayAdd"], x["spot3D"], x["spot2D"], x["adsMoveSpeedSteps"]))
        po = sa.get("projectileOverrides", {}).get(aid)
        if po:
            cur = P[x["projectile"]]["curve"]
            sp = [[p["r"], p["d"]] for p in po["dmg"]]
            chk("projectile override dmg (shotgun 00 buck / slugs)", bool(cur) and same_function(sp, cur), "%s/%s: site %s raw %s" % (wid, aid, sp, cur))
    for aid, recs in r["ammo"].items():
        if aid not in sa["ammo"]:
            for x in recs:
                extras[aid] += 1; extras_list.append("%s %s cost %s kill switch %s" % (wid, x["attachment"], x["cost"], x["kill"]))
    for u in r["unmapped"]:
        extras["unmapped:" + u] += 1; extras_list.append("%s unmapped suffix %s" % (wid, u))
    # ---- ballistics / hit zones / dmg
    chk("ballistics base projectile", sb["base"] == r["base"], "%s: site %s raw %s" % (wid, sb["base"], r["base"]))
    chk("hit zones protectionIndex", sh["protectionIndex"] == r["protectionIndex"], "%s: site %s raw %s (registry %s, file %s)" % (
        wid, sh["protectionIndex"], r["protectionIndex"], w["protectionIndex"]["registry"], w["protectionIndex"]["file"]))
    chk("hit zones projectileMaterial", sh["projectileMaterial"] == r["projectileMaterial"], "%s: site %s raw %s (%s)" % (wid, sh["projectileMaterial"], r["projectileMaterial"], r["base"].rsplit("/", 1)[-1]))
    chk("hit zones base headshot/limb", (sh["headshot"], sh["limb"]) == (r.get("headshot"), r.get("limb")), "%s: site %s/%s raw %s/%s" % (wid, sh["headshot"], sh["limb"], r.get("headshot"), r.get("limb")))
    cur = P[r["base"]]["curve"]
    sp = [[p["r"], p["d"]] for p in sw["dmg"]]
    chk("dmg curve (exact points)", sp == cur, "%s: site %s raw %s" % (wid, sp, cur))
    chk("dmg curve (same function)", bool(cur) and same_function(sp, cur), "%s: site %s raw %s" % (wid, sp, cur))
    mv = w["muzzleVelocity"]; live = mv["registry"] if mv["registry"] is not None else mv["file"]
    chk("muzzle velocity vs site bulletVel", abs(live - sw["bulletVel"]) < 1e-3, "%s: site %s raw registry %s file %s" % (wid, sw["bulletVel"], mv["registry"], mv["file"]))

for key, sp in site_ball["projectiles"].items():
    rp = P.get(key)
    ok = rp is not None and (rp["gravityMps2"], rp["dragPerMeter"], rp["guid"]) == (sp["gravityMps2"], sp["dragPerMeter"], sp["guid"])
    chk("projectile gravity/drag/guid", ok, "%s: site %s raw %s" % (key, sp, {k: rp[k] for k in ("gravityMps2", "dragPerMeter", "guid")} if rp else None))

# registry / file agreement, all 67
regfile = {"protection": [0, 0, []], "penetration": [0, 0, []], "velocity": [0, 0, []]}
for wid, w in d["weapons"].items():
    for nm, key in (("protection", "protectionIndex"), ("penetration", "penetrationIndex"), ("velocity", "muzzleVelocity")):
        v = w[key]
        if v["registry"] is None:
            regfile[nm][2].append("%s: no registry row, file %s" % (wid, v["file"])); continue
        regfile[nm][0] += 1
        if v["registry"] == v["file"]: regfile[nm][1] += 1
        else: regfile[nm][2].append("%s: registry %s file %s" % (wid, v["registry"], v["file"]))

# collateral table read from the grids for every projectile used
tables = collections.Counter()
for key, p in P.items():
    for zone, recs in (p["zones"].get("collateralTables") or {}).items():
        tables[json.dumps(recs)] += 1

# ---------------------------------------------------------------- proposals
prop = {"data/ammo.json": {}, "data/ballistics.json": {}, "data/hit_zones.json": {}, "data/balance_tables.json": {}, "data/weapons.json": {}}
detail = {}
new_proj = {}
for wid in NEW:
    w = d["weapons"][wid]
    r = resolve(wid, w, {**SUFFIX, **NEW_SUFFIX})
    detail[wid] = {"resolved": r, "indices": {k: w[k] for k in ("protectionIndex", "penetrationIndex", "muzzleVelocity")},
                   "wbRegistryRows": w["wbRegistryRows"], "unmapped": r["unmapped"]}
    ids = sorted(r["ammo"], key=ORDER.index)
    for aid in ids:
        if len(r["ammo"][aid]) != 1:
            raise ValueError("%s/%s: %d attachments" % (wid, aid, len(r["ammo"][aid])))
    A = {aid: r["ammo"][aid][0] for aid in ids}
    defaults = [aid for aid in ids if A[aid]["default"]]
    entry = {"def": defaults[0] if len(defaults) == 1 else None, "ammo": {aid: A[aid]["cost"] for aid in ids}}
    vt, eo = {}, {}
    for aid in ids:
        x = A[aid]
        facs = [v["factor"] for v in x["velocity"] if v["factor"] != 1.0]
        if facs:
            t = tier_of(facs[0]) if len(facs) == 1 else None
            if t is None:
                raise ValueError("%s/%s: velocity factor %s is not a 0.8 tier; needs the absolute treatment" % (wid, aid, facs))
            vt[aid] = {"kind": "subsonic-tier", "subsonicVelocityTier": t, "displayRounding": "floor"}
        cat = CATALOG[aid]
        if (cat.get("adsRecoilTierMod", 0), cat.get("hipRecoilTierMod", 0)) != (x["adsRecoil"], x["hipRecoil"]):
            eo[aid] = {"adsRecoilTierMod": x["adsRecoil"], "hipRecoilTierMod": x["hipRecoil"]}
    if vt: entry["velocityTreatments"] = vt
    if eo: entry["effectOverrides"] = eo
    prop["data/ammo.json"]["WEAPON_AMMO/" + wid] = entry
    prop["data/ballistics.json"]["weapons/" + wid] = {"base": r["base"], "ammo": {aid: A[aid]["projectile"] for aid in ids}}
    for key in [r["base"]] + [A[aid]["projectile"] for aid in ids]:
        if key not in site_ball["projectiles"]:
            new_proj[key] = {k: P[key][k] for k in ("gravityMps2", "dragPerMeter", "guid")}
    prop["data/hit_zones.json"]["weapons/" + wid] = {
        "protectionIndex": r["protectionIndex"], "projectileMaterial": r["projectileMaterial"], "headshot": r["headshot"], "limb": r["limb"],
        "ammo": {aid: {"headshot": A[aid]["headshot"], "limb": A[aid]["limb"]} for aid in ids}}
    prop["data/balance_tables.json"]["COLLATERAL_MULT_OVERRIDE/" + wid] = {aid: A[aid]["collateral"] for aid in ids}
    pd_name = r["base"].rsplit("/", 1)[-1]; wb_name = w["wb"].rsplit("/", 1)[-1]
    prop["data/weapons.json"]["[id=%s]" % wid] = {
        "dmg": site_dmg(P[r["base"]]["curve"]),
        "damageSource": "Frosty %s tweakable damage curve referenced by %s, raw capture %s." % (pd_name, wb_name, settings.BUILD_LABEL)}
    detail[wid]["curveOwn"] = P[r["base"]]["curveOwn"]; detail[wid]["curveRegistry"] = P[r["base"]]["curveRegistry"]
    detail[wid]["swapCurves"] = {k.rsplit("/", 1)[-1]: P[k]["curve"] for k in {A[a]["projectile"] for a in ids} if k != r["base"]}
    detail[wid]["catalogueCheck"] = {aid: {"regenDelayAdd": A[aid]["regenDelayAdd"], "spot3D": A[aid]["spot3D"], "spot2D": A[aid]["spot2D"],
                                           "adsMoveSpeedSteps": A[aid]["adsMoveSpeedSteps"], "other": A[aid]["other"], "selectors": A[aid]["selectors"],
                                           "kill": A[aid]["kill"], "collateralIndex": A[aid]["collateralIndex"], "protectionSteps": A[aid]["protectionSteps"],
                                           "recoilAssets": A[aid]["recoilAssets"], "attachment": A[aid]["attachment"], "swapVia": A[aid]["swapVia"],
                                           "siteCatalogueClassCollateral": CATALOG[aid].get("collateralMult", {}).get(NEW_CLS[wid])} for aid in ids}
prop["data/ballistics.json"]["projectiles (new entries)"] = new_proj
import hashlib
prop["data/ballistics.json"]["note: raw .ebx sha256 of the new projectile files (the file's source.projectileSha256 holds XML-export hashes, which a raw read cannot produce)"] = {
    k: {"file": "builds/%s/" % settings.BUILD_LABEL + P[k]["file"], "sha256": hashlib.sha256(open(c.BUILD / P[k]["file"], "rb").read()).hexdigest()} for k in new_proj}
prop["data/ammo.json"]["AMMO (catalogue)"] = {
    "required new entries": [],
    "note": "Every ammunition record of the four weapons maps to an existing catalogue id. PKM's 'PolymerLinks' record is mapped to 'lightweight' (same two effects as PolymerCase). See REPORT.md, judgement call 1.",
    "alternative if Polymer Links must be its own type (display name not found in held files)": {
        "id": "polymer_links", "name": None, "adsMoveSpeedTierShift": -1,
        "collateralMult": {"LMG": 0.75}}}
# own vs registry agreement on every projectile read
pr = {"curve": [0, 0, []], "gravity": [0, 0, []], "drag": [0, 0, []]}
for key, p in P.items():
    for nm, own, reg in (("curve", p["curveOwn"], p["curveRegistry"]), ("gravity", p["gravityOwn"], p["gravityRegistry"]), ("drag", p["dragOwn"], p["dragRegistry"])):
        if reg is None:
            pr[nm][2].append("%s: no registry row" % key.rsplit("/", 1)[-1]); continue
        pr[nm][0] += 1
        if own == reg: pr[nm][1] += 1
        else: pr[nm][2].append("%s: own %s registry %s" % (key.rsplit("/", 1)[-1], own, reg))

json.dump(prop, open(HERE / "proposed.json", "w", encoding="utf-8"), indent=2)
print("projectile own vs registry:", {k: (v[1], v[0], v[2]) for k, v in pr.items()})
print("raw ammo records not on site (list):", extras_list)
print("new weapon point cost lists:", {wid: {a["suffix"]: (a["pointCost"], a["pointCostList"]) for a in d["weapons"][wid]["ammo"]} for wid in NEW})
json.dump({"validation": val, "registryVsFile": regfile, "projectileOwnVsRegistry": pr, "rawAmmoRecordsNotOnSite": {"counts": extras, "list": extras_list},
           "collateralTablesInGrids": tables, "soldierMaterials": d["soldierMaterials"], "grids": d["grids"], "newWeaponDetail": detail},
          open(HERE / "validation.json", "w", encoding="utf-8"), indent=1)
for k, v in val.items():
    print("%-55s %4d / %4d" % (k, v["match"], v["checked"]))
    for m in v["mismatches"][:70]:
        print("      ", m[:330])
print("registry vs file:", {k: (v[1], v[0], v[2]) for k, v in regfile.items()})
print("raw ammo records not on site:", dict(extras))
print("collateral tables seen in grids:", [(k[:140], n) for k, n in tables.items()])
