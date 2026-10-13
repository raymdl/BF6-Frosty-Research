"""Stage 9 part A extractor: per-weapon base record fields from 2.1.1.0 raw EBX + GRX_Weapons registry.

raw(internal) -> dict of source values (file value, overridden by a registry row where one exists).
record(internal, ...) -> site-shaped weapons.json fields.
Run directly: validates the 63 existing site weapons and writes validation.json / validation.txt.
"""
import json, sys, struct, collections
import lib
from lib import f32

F = lambda h: "Field_" + h
ZOOM, UNZOOM = F("6b84de87"), F("7b609515")
STAT, MOVE, JUMP, MJS = F("0a160c57"), F("e2ae7c09"), F("a059dd20"), F("447d6d51")
STAND, CROUCH, PRONE = F("8c7ee85a"), F("956304be"), F("97ff0ca4")
REG_AIM = {ZOOM: "Zoomed", UNZOOM: "Unzoomed"}
REG_STANCE = {STAND: "Standing", CROUCH: "Crouching", PRONE: "Prone"}
REG_MOVE = {STAT: "Stationary", MOVE: "Moving", JUMP: "JumpingSprinting", MJS: "MovingJumpingSprinting"}
RECOIL = {"dir": "RecoilDirection", "amount": "RecoilAmount", "amountMult": "RecoilAmountMultiplier",
          "amountExp": "RecoilAmountMultiplierExponent", "dirVar": "RecoilDirectionVariation",
          "dirVarMult": "RecoilDirectionVariationMultiplier", "dirVarExp": "RecoilDirectionVariationMultiplierExponent",
          "decNorm": "RecoilDecreaseNorm", "decExp": "RecoilDecreaseExponent", "decTimeExp": "RecoilDecreaseTimeExponent",
          "decOffset": "RecoilDecreaseOffset", "duration": "RecoilDuration", "decFactor": "RecoilDecreaseFactor",
          "shootingDecScale": "ShootingRecoilDecreaseScale"}
DYN = {"inc": "IncreasePerShot", "idleTime": "IdleTime", "idleCoef": "IdleDecreaseCoefficient", "idleExp": "IdleDecreaseExponent",
       "idleOffset": "IdleDecreaseOffset", "firingCoef": "FiringDecreaseCoefficient", "firingExp": "FiringDecreaseExponent",
       "firingOffset": "FiringDecreaseOffset", "notFiringCoef": "NotFiringDecreaseCoefficient",
       "notFiringExp": "NotFiringDecreaseExponent", "notFiringOffset": "NotFiringDecreaseOffset",
       "firstShotMul": "FirstShotIncreaseMultiplier", "distExp": "DistributionExponent"}
HASH = {v: k for k, v in lib.NAMES.items()}
HASH.update({"RecoilDuration": "5a02dd65", "FirstShotIncreaseMultiplier": "bf650805", "RateOfFire": "14c4a054"})
CLS = {"assaultrifle": "Assault Rifle", "carbine": "Carbine", "smg": "SMG", "mg": "LMG", "dmr": "DMR",
       "boltaction": "Sniper Rifle", "shotgun": "Shotgun", "pistol": "Sidearm", "sidearm": "Sidearm", "secondary": "Sidearm"}
MODE = {0: "single", 1: "single", 2: "auto", 3: "burst"}
SEMI_NOINC = "gbm_noincrease_semi_p00"

_routes = None


def routes(internal):
    """(wb route, gs route) for an internal weapon name."""
    global _routes
    if _routes is None:
        _routes = {}
        for r in lib.held:
            if r.startswith("common/hardware/weapons/"):
                _routes.setdefault(r.rsplit("/", 1)[-1], []).append(r)
    k = internal.lower()
    wb = [r for r in _routes.get(k + "_wb", []) if "/" + k + "/" in r]
    gs = [r for r in _routes.get("gs_" + k, []) if "/" + k + "/" in r]
    assert len(wb) == 1 and len(gs) == 1, (internal, wb, gs)
    return wb[0], gs[0]


class Src:
    """File value with registry override; remembers both and counts disagreements."""
    def __init__(self):
        self.log = []          # (label, file value, registry value or None)

    def get(self, label, filev, regname):
        rv = lib.reg(regname) if regname else None
        if isinstance(rv, dict):
            rv = None
        self.log.append((label, filev, rv, regname))
        return rv if rv is not None else filev


def curve(pd_route, classguid, src, tag):
    objs, by, _ = lib.load(pd_route)
    b = by[classguid]
    name = pd_route.rsplit("/", 1)[-1]
    real = objs[0].get("Field_0c59fa06", "").rsplit("/", 1)[-1] or name
    _, c = lib.deref(b[F("2ad7e688")], objs)
    flat = [f32(v) for v in c.get(F("5279388d"), [])]
    pts = [[f32(p[F("3901db14")]), f32(p[F("42fc0f5e")])] for p in c.get(F("edfc6df6"), [])] or [[flat[i], flat[i + 1]] for i in range(0, len(flat), 2)]
    rv = lib.reg(real + ".BulletEntityData.TweakableDamageCurve.XYValues")
    regpts = None
    if isinstance(rv, dict):
        a = [f32(v) for v in rv.get("Field_ffba60f0", [])]
        regpts = [[a[i], a[i + 1]] for i in range(0, len(a), 2)]
    src.log.append((tag + "dmg", pts, regpts, real + "...XYValues"))
    return real, (regpts if regpts else pts), pts, flat, b


def raw(internal):
    wbr, gsr = routes(internal)
    s = Src(); out = {"internal": internal, "wbRoute": wbr, "gsRoute": gsr, "folder": wbr.split("/")[3]}
    wobjs, _, _ = lib.load(wbr); gobjs, _, _ = lib.load(gsr)
    wbname = wobjs[0]["Field_0c59fa06"].rsplit("/", 1)[-1]; gsname = gobjs[0]["Field_0c59fa06"].rsplit("/", 1)[-1]
    fires = [o for o in wobjs if o["$class"] == "Class_35259f6b"]
    out["firingObjects"] = len(fires)
    fire = fires[0]
    gs = [o for o in gobjs if o["$class"] == "Class_539cff9b"][0]
    P = wbname + ".WeaponEntityData.WeaponFiring.PrimaryFire."
    fl, shot, ammo = fire[F("f8822efa")], fire[F("58d70acb")], fire[F("4cc9e2ed")]
    g = lambda lab, v, rn: s.get(lab, v, rn)
    out["rateOfFire"] = g("rof", fl[F("14c4a054")], P + "FireLogic.RateOfFire")
    out["rateOfFireSingle"] = g("rofSingle", fl[F("be31b12d")], P + "FireLogic.RateOfFireForSingleFire")
    out["rateOfFireBurst"] = g("rofBurst", fl[F("5bd8006c")], P + "FireLogic.RateOfFireForBurst")
    out["burstsPerMinute"] = g("bpm", fl[F("2320e742")], P + "FireLogic.BurstsPerMinute")
    out["primaryMode"] = fl[F("16e6fa59")]; out["altModes"] = list(fl[F("9b956c3d")])
    out["burstRoundsField"] = shot[F("ca2ec42a")]
    ba = fl[F("eebe0fd8")]; BP = P + "FireLogic.BoltAction."
    out["bolt"] = {k: g("bolt." + k, ba[F(h)], BP + n) for k, h, n in (
        ("delay", "caf2ace0", "BoltActionDelay"), ("time", "a1abbce8", "BoltActionTime"), ("speed", "1c57216a", "BoltActionSpeed"),
        ("frac", "2084d4bf", "BoltActionTimeCompletedFraction"), ("fracZoom", "21f2d4ee", "BoltActionTimeCompletedFractionZoom"))}
    out["reload"] = []
    for i, e in enumerate(fl[F("d15a0c1c")]):
        RP = P + "FireLogic.ReloadInfoArray[%d]." % i
        out["reload"].append({k: g("reload%d.%s" % (i, k), e[F(h)], RP + n) for k, h, n in (
            ("time", "85ff24a0", "ReloadTime"), ("timeBulletsLeft", "fc66e75e", "ReloadTimeBulletsLeft"), ("speed", "1c533b56", "ReloadSpeed"),
            ("delay", "c0c7c72f", "ReloadDelay"), ("postDelay", "b480c17a", "PostReloadDelay"), ("bridgeDelay", "27b15985", "BridgeDelay"),
            ("maxAmmo", "c59cc6a8", "MaxAmmoCountInWeapon"), ("minAmmo", "82265a82", "MinAmmoCountInWeapon"))})
        out["reload"][-1]["type"] = e[F("6e081af4")]
        out["reload"][-1]["phases"] = [f32(v) for v in e[F("dc244b57")]]
    out["mag"] = g("mag", ammo[F("7f22bfb4")], P + "Ammo.MagazineCapacity")
    out["bulletVel"] = g("vel", shot[F("0bf4f62b")][F("32a99b9c")], P + "Shot.InitialSpeed.z")
    out["protectionIndex"] = g("prot", shot[F("9ba8b76b")], P + "Shot.DamageProtectionMultiplierIndex")
    out["penetrationIndex"] = g("pen", shot[F("7e2be65f")], P + "Shot.DamagePenetrationMultiplierIndex")
    out["pelletsField"] = {h: shot[F(h)] for h in ("db0fcea2", "085057c2", "2fd1661f")}
    pr, pg = lib.imp(shot[F("808dd66c")])
    out["bulletRoute"] = pr
    out["bullet"], out["dmg"], out["dmgFilePoints"], out["dmgFileFlat"], _ = curve(pr, pg, s, "")
    # WB root indices (registry only names; file values live on the weapon root object)
    root = [o for o in wobjs if o["$class"] == "Class_542ac52c"][0]
    for nm, h in (("WeaponZoomTransitionIndex", "db03e8a9"), ("AnimationZoomSettingsIndex", "ae4adc54"), ("AltAnimationZoomSettingsIndex", "e7f4ce7c"),
                  ("SprintSettingsIndex", "5198399a"), ("WeaponZoomedMoveSpeedMultiplierIndex", "dcb8bf9e"), ("WeaponHipMoveSpeedMultiplierIndex", "8c46f71b")):
        out[nm] = g(nm, root[F(h)][F("2b6f2936")], wbname + "." + nm + ".Index")
    # GS
    G = gsname + "."
    out["recoil"] = {}
    for aim, key in ((ZOOM, "ads"), (UNZOOM, "hip")):
        blk = gs[F("c5d1c8fe")][aim]
        out["recoil"][key] = {k: g("recoil.%s.%s" % (key, k), blk[F(HASH[n])], G + "Recoil.%s.%s" % (REG_AIM[aim], n)) for k, n in RECOIL.items()}
        out["recoil"][key]["usePolar"] = blk[F("8bd6dcdd")]
    out["dyn"] = {}
    for aim, key in ((ZOOM, "ads"), (UNZOOM, "hip")):
        for mv, mk in ((STAT, "stat"), (MJS, "move")):
            blk = gs[F("0a5922e0")][aim][mv]
            out["dyn"][key + "." + mk] = {k: g("dyn.%s.%s.%s" % (key, mk, k), blk[F(HASH[n])], G + "DispersionBehavior.%s.%s.%s" % (REG_AIM[aim], REG_MOVE[mv], n)) for k, n in DYN.items()}
    out["minmax"] = {}
    for aim in (ZOOM, UNZOOM):
        for st in (STAND, CROUCH, PRONE):
            for mv in (STAT, MOVE, JUMP):
                blk = gs[F("3ed1c995")][aim][st].get(mv)
                if blk is None:
                    continue
                rn = G + "MinMaxDispersion.%s.%s.%s." % (REG_AIM[aim], REG_STANCE[st], REG_MOVE[mv])
                key = "%s.%s.%s" % (REG_AIM[aim], REG_STANCE[st], REG_MOVE[mv])
                out["minmax"][key] = [g("minmax." + key + ".min", blk[F("7baf4297")], rn + "MinAngle"), g("minmax." + key + ".max", blk[F("60e4e484")], rn + "MaxAngle")]
    out["hipIndex"] = g("hipIndex", gs[F("fe708077")], G + "UnzoomedMinAnglesArrayIndex")
    out["adsStatIndex"] = g("adsStatIndex", gs[F("cee5ebfe")], G + "StationaryZoomedMinAnglesArrayIndex")
    out["adsMoveIndex"] = g("adsMoveIndex", gs[F("d94fe6ad")], G + "MovingZoomedMinAnglesArrayIndex")
    idle = gs[F("5b6caeda")]
    out["idleStatIndex"] = g("idleStat", idle[F("6138f58f")], G + "IdleDecreaseTargetDuration.StationaryIndex")
    out["idleMoveIndex"] = g("idleMove", idle[F("54a69c98")], G + "IdleDecreaseTargetDuration.MovingIndex")
    # arrays
    out["hipArray"] = lib.imp(gs[F("ad14dd81")]); out["adsMoveArray"] = lib.imp(gs[F("b5e19f3d")]); out["adsStatArray"] = lib.imp(gs[F("ba183dd4")])
    hr = arr(gs[F("ad14dd81")], gobjs)
    out["hipRow"] = None
    if hr is not None and 0 <= out["hipIndex"] < len(hr):
        row = hr[out["hipIndex"]]
        out["hipRow"] = {"hipStand": f32(row[F("1867639b")]), "hipMove": f32(row[F("c5401fc2")])}
    mr = arr(gs[F("b5e19f3d")], gobjs)
    out["adsMoveRow"] = None
    if mr is not None and 0 <= out["adsMoveIndex"] < len(mr):
        row = mr[out["adsMoveIndex"]]
        out["adsMoveRow"] = {k[6:]: f32(v) for k, v in row.items() if k.startswith("Field_") and isinstance(v, float)}
    # GS bindings: all imported modifier names with selector
    binds = []
    for coll, lst in gs.items():
        if not isinstance(lst, list):
            continue
        for b in lst:
            if isinstance(b, dict) and F("2f0e5b83") in b:
                i = lib.imp(b[F("2f0e5b83")])
                binds.append((coll[6:], b.get(F("6d011165")), (i[0] or "?").rsplit("/", 1)[-1] if i else None, b.get(F("3f680d24"))))
    out["gsBindings"] = binds
    allb = json.dumps(gs)
    out["semiNoIncreaseBound"] = any((b[2] or "").lower() == SEMI_NOINC for b in binds)
    out["_gsHasSemiImport"] = None
    out["log"] = s.log
    return out


def arr(ref, objs):
    """Rows of an array asset referenced from the GS (HDA_Weapons / ZDA_Moving_Weapons)."""
    r, o = lib.deref(ref, objs)
    if o is None:
        return None
    aobjs = lib.load(r)[0] if r else objs
    for k, v in o.items():
        if isinstance(v, list) and v and isinstance(v[0], dict):
            return [lib.deref(e, aobjs)[1] if ("$ref" in e or "$import" in e) else e for e in v]
    return None


def div32(a, b):
    """float32 quotient as the shortest round-trip decimal (site stored-precision rule)."""
    if b == 1:
        return f32(a)
    q = struct.unpack("<f", struct.pack("<f", struct.unpack("<f", struct.pack("<f", a))[0] / struct.unpack("<f", struct.pack("<f", b))[0]))[0]
    return f32(q)


def d32(x):
    """float32 value widened to double (site stores fireModes rpm this way)."""
    return struct.unpack("<f", struct.pack("<f", x))[0]


def record(r):
    """Site-shaped fields from raw()."""
    w = collections.OrderedDict()
    w["cls"] = CLS.get(r["folder"], r["folder"])
    pm = r["primaryMode"]; modes = [pm] + [m for m in r["altModes"] if m != pm]
    bolt = pm == 1
    mech = None
    if pm == 2:
        w["rpm"] = f32(r["rateOfFire"]); w["fireMode"] = "auto"
    elif pm == 3:
        w["rpm"] = f32(r["rateOfFireBurst"]); w["fireMode"] = "burst"
    elif pm == 0:
        w["rpm"] = f32(r["rateOfFireSingle"]); w["fireMode"] = "semi"
    else:
        b = r["bolt"]
        # site arithmetic: shortest-decimal operands in double precision (reproduces sv98, l115, interdictor, m87a1 exactly)
        w["rpm"] = 60.0 / (f32(b["time"]) / f32(b["speed"]) + f32(b["delay"]) + 60.0 / f32(r["rateOfFireSingle"]))
        w["fireMode"] = "pump" if r["folder"] == "shotgun" else "bolt"
    w["mag"] = r["mag"]
    r0 = r["reload"][0]; r1 = r["reload"][1] if len(r["reload"]) > 1 else r["reload"][0]
    w["tacRld"] = div32(r0["timeBulletsLeft"], r0["speed"])
    w["emptyRld"] = div32(r1["timeBulletsLeft"], r1["speed"])
    w["reloadSpeed"] = f32(r0["speed"])
    w["bulletVel"] = f32(r["bulletVel"])
    ra = r["recoil"]["ads"]
    w["recoilV"] = f32(ra["amount"]) * f32(ra["amountMult"]) ** f32(ra["amountExp"])
    w["recoilDir"] = f32(ra["dir"]); w["recoilVar"] = f32(ra["dirVar"])
    w["recoilIncAds"] = f32(r["dyn"]["ads.stat"]["inc"])
    names = []
    for m in modes:
        n = MODE[m]
        if n not in names and (m != 3 or pm == 3):   # an alternate burst mode is attachment-gated on the site
            names.append(n)
    w["availableFireModes"] = names
    fm = collections.OrderedDict()
    if 0 in modes or 1 in modes:
        fm["single"] = {"mechanism": ("pump" if r["folder"] == "shotgun" else "bolt") if 1 in modes else "semi", "rpm": d32(r["rateOfFireSingle"]),
                        "hipNoBloomOnSwitch": bool(r["semiNoIncreaseBound"])}
    if 2 in modes:
        fm["auto"] = {"mechanism": "auto", "rpm": d32(r["rateOfFire"])}
    if 3 in modes:
        fm["burst"] = {"mechanism": "burst", "rpm": d32(r["rateOfFireBurst"]), "burstRounds": r["burstRoundsField"], "burstBurstsPerMinute": d32(r["burstsPerMinute"])}
    w["fireModes"] = fm
    w["spreadDyn"] = {k: {f: f32(v) for f, v in r["dyn"][k + ".stat"].items()} for k in ("ads", "hip")}
    for k in ("ads", "hip"):
        if f32(r["dyn"][k + ".move"]["distExp"]) != f32(r["dyn"][k + ".stat"]["distExp"]):
            w["spreadDyn"][k]["distExpMove"] = f32(r["dyn"][k + ".move"]["distExp"])
    w["recoil"] = {k: {f: f32(v) for f, v in r["recoil"][k].items() if f != "usePolar"} for k in ("ads", "hip")}
    mm = r["minmax"]
    w["spread"] = {
        "adsStand": [f32(mm["Zoomed.Standing.Stationary"][0]), f32(mm["Zoomed.Standing.Stationary"][1])],
        "adsMove": [(r["adsMoveRow"] or {}).get("6c73f45b"), f32(mm["Zoomed.Standing.Moving"][1])],
        "hipStand": [(r["hipRow"] or {}).get("hipStand"), f32(mm["Unzoomed.Standing.Stationary"][1])],
        "hipMove": [(r["hipRow"] or {}).get("hipMove"), f32(mm["Unzoomed.Standing.Moving"][1])]}
    w["dmg"] = [{"r": p[0], "d": p[1], "source": "Frosty"} for p in r["dmg"]]
    return w


def leaves(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from leaves(v, p + "." + k if p else k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from leaves(v, p + "[%d]" % i)
    else:
        yield p, x


def same(a, b):
    if isinstance(a, bool) or isinstance(b, bool) or a is None or b is None or isinstance(a, str) or isinstance(b, str):
        return a == b
    if a == b:
        return True
    try:
        return struct.pack("<f", a) == struct.pack("<f", b)
    except Exception:
        return False


if __name__ == "__main__":
    ids = json.load(open(lib.REPO / "reference-data/provenance/frosty-weapon-identities.json", encoding="utf-8"))["weapons"]
    site = {w["id"]: w for w in json.load(open(lib.SITE / "data/weapons.json", encoding="utf-8"))}
    decay = json.load(open(lib.SITE / "data/recoil_decay.json", encoding="utf-8"))
    balance = json.load(open(lib.SITE / "data/balance_tables.json", encoding="utf-8"))
    mags = json.load(open(lib.SITE / "data/attachments.json", encoding="utf-8"))["WEAPON_MAG"]
    stats = collections.defaultdict(lambda: [0, 0]); mism = []; regdis = []; raws = {}
    for e in ids:
        sid, internal = e["siteId"], e["internalId"]
        if sid not in site:
            continue
        try:
            r = raw(internal)
        except Exception as ex:
            mism.append((sid, "EXTRACT", repr(ex), "")); continue
        raws[sid] = r
        for lab, fv, rv, rn in r["log"]:
            if rv is not None and not (same(fv, rv) if not isinstance(fv, list) else fv == rv):
                regdis.append((sid, lab, fv, rv))
        rec = record(r); sw = site[sid]
        # per-weapon maps in other data files
        ra = rec["recoil"]["ads"]
        for name, table, val in (("recoil_decay.RECOIL_DEC", decay["RECOIL_DEC"], ra["decFactor"]),
                                 ("recoil_decay.RECOIL_DEC_TEXP", decay["RECOIL_DEC_TEXP"], ra["decTimeExp"]),
                                 ("recoil_decay.RECOIL_DEC_EXP", decay["RECOIL_DEC_EXP"], ra["decExp"] if ra["decExp"] != 1 else None),
                                 ("balance.RECOIL_MULT", balance["RECOIL_MULT"], ra["amountMult"]),
                                 ("balance.HIP_SPREAD_BASE_INDEX", balance["HIP_SPREAD_BASE_INDEX"], r["hipIndex"]),
                                 ("balance.HIP_SPREAD_TABLE[index].hipStand", {sid: (balance["HIP_SPREAD_TABLE"][r["hipIndex"]] or {}).get("hipStand")}, (r["hipRow"] or {}).get("hipStand")),
                                 ("balance.MOVING_ACC_TIERS[adsMoveIndex]", {sid: balance["MOVING_ACC_TIERS"][r["adsMoveIndex"]]}, (r["adsMoveRow"] or {}).get("6c73f45b")),
                                 ("attachments.WEAPON_MAG.defAds", {sid: mags.get(sid, {}).get("defAds")}, r["WeaponZoomTransitionIndex"]),
                                 ("attachments.WEAPON_MAG.defAms", {sid: mags.get(sid, {}).get("defAms")}, r["WeaponZoomedMoveSpeedMultiplierIndex"]),
                                 ("attachments.WEAPON_MAG.sprintRecoveryBaseIndex", {sid: mags.get(sid, {}).get("sprintRecoveryBaseIndex")}, r["SprintSettingsIndex"])):
            ok = same(table.get(sid), val)
            stats[name][0] += ok; stats[name][1] += 1
            if not ok:
                mism.append((sid, name, table.get(sid, "<absent>"), val))
        for k, v in rec.items():
            if k not in sw:
                mism.append((sid, k, "site has no field", v)); continue
            sl = dict(leaves(sw[k], k)); el = dict(leaves(v, k))
            for p in sorted(set(sl) | set(el)):
                gen = p.split("[")[0] if p.startswith("dmg") else p
                gen = "dmg" if p.startswith("dmg") else p
                ok = p in sl and p in el and same(sl[p], el[p])
                stats[gen][0] += ok; stats[gen][1] += 1
                if not ok:
                    mism.append((sid, p, sl.get(p, "<absent>"), el.get(p, "<absent>")))
    with open(lib.HERE / "validation.txt", "w", encoding="utf-8") as f:
        f.write("weapons extracted: %d of %d\n\nfield\tmatch\ttotal\n" % (len(raws), len(site)))
        for k, (a, b) in stats.items():
            f.write("%s\t%d\t%d\n" % (k, a, b))
        f.write("\nMISMATCHES (site id, leaf, site, extractor)\n")
        for m in mism:
            f.write("\t".join(str(x) for x in m) + "\n")
        f.write("\nFILE VALUE != REGISTRY VALUE (site id, label, file, registry)\n")
        for m in regdis:
            f.write("\t".join(str(x) for x in m) + "\n")
    print(open(lib.HERE / "validation.txt", encoding="utf-8").read()[:12000])
