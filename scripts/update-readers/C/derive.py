"""Derive the site's attachment data for one weapon from the 2.1.1.0 raw files.

Reproduces, from raw EBX, what these site generators write from XML:
  frosty-attachment-handling.py   grip/laser frostyModifiers, magazine handling fields
  frosty-barrel-ads.py            BARRELS[].adsTimeTierModByWeapon
  frosty-sniper-brakes.py         muzzle recoil-amount overrides
  frosty-assumption-review.py     recoil amount/variation steps
  frosty-attachment-compatibility.py   slots, dependencies, WEAPON_ACCESSORY
  frosty-attachment-tooltips.py   byWeapon description ids, optic categories
Identity (raw record -> site id) comes from identity.py (reviewed mapping of the 63 existing weapons).
"""
import json, re, collections, pathlib
from rawlib import *
import identity, graph, ui, weapons as W

CAT = json.load(open(SITE / "data/attachments.json", encoding="utf-8"))
TIPS = json.load(open(SITE / "data/attachment-tooltips.json", encoding="utf-8"))
AMMO = json.load(open(SITE / "data/ammo.json", encoding="utf-8"))
CATKEY = {"muzzle": "MUZZLES", "barrel": "BARRELS", "grip": "GRIPS", "laser": "LASERS", "light": "LIGHTS", "ergo": "ERGOS", "sight": "SIGHTS"}
BYID = {s: {e["id"]: e for e in CAT[k]} for s, k in CATKEY.items()}
CAT_SLOT = {"Muzzle": ["muzzle"], "Barrel": ["barrel"], "BottomRail": ["grip"], "Magazine": ["mag"], "Ammunition": ["ammo"], "MagazineWell": ["ergo"],
            "TopRail": ["laser", "light", "grip"], "RightRail": ["light", "laser", "grip"], "LeftRail": ["light", "laser", "grip"]}
ACCESSORY_FAMILIES = {"CantedIronSights": "canted_irons", "AGCoating": "ag_coating",
                      **{f: "secondary_optic" for f in ("CantedReflex", "CantedReflexSlanted", "OffsetRedDot", "G43Magnifier", "Variable2x", "Variable3x", "Variable4x")}}
ROWS = identity.load_choices()
ROSTER = W.roster()
BY_SITE = {w["siteId"]: w for w in ROSTER}
IDX = ui.Index()
# how many weapons use each site id (single-weapon ids are weapon-specific variants)
USERS = collections.defaultdict(set)
for r in ROWS:
    USERS[(r["slot"], r["id"])].add(r["weapon"])
TRUTH = collections.defaultdict(list)   # (weapon, attachment basename lower) -> [(slot, id)]
for r in ROWS:
    TRUTH[(r["weapon"], pathlib.PurePosixPath(r["source"].split("#")[0]).stem.lower())].append((r["slot"], r["id"]))

RELOAD_TIERS = [1, 1.13, 1.277]
SMOOTH = {"6b84de87/28df1cde/5695ee1c": "adsRecoilDecayMult", "7b609515/28df1cde/5695ee1c": "hipRecoilDecayMult",
          "6b84de87/5a02dd65/bbbfe9cc": "recoilDurationOverride", "6b84de87/1d04f0f6/4692836a": "recoilDecreaseTimeExponentAdd",
          "6b84de87/5a02dd65/4692836a": "recoilDurationAdd"}
FIELDS = {
    "grip": ("adsRecoilTierMod", "hipRecoilTierMod", "movingAdsSpreadTierMod", "hipSpreadTierMod", "adsTimeTierMod", "adsMoveSpeedTierShift",
             "sprintRecoveryTierShift", "deployTimeTierShift"),
    "laser": ("hipSpreadTierMod", "movingAdsSpreadTierMod", "sprintRecoveryTierShift", "deployTimeTierShift"),
    "light": ("sprintRecoveryTierShift", "deployTimeTierShift"),
    "muzzle": ("adsRecoilTierMod", "hipRecoilTierMod", "adsRecoilVariationTierMod", "hipRecoilVariationTierMod", "hipSpreadTierMod",
               "sprintRecoveryTierShift", "deployTimeTierShift", "weaponSwayMult", "adsRecoilDecayMult", "hipRecoilDecayMult",
               "recoilDurationOverride", "recoilDecreaseTimeExponentAdd"),
    "barrel": ("adsTimeTierMod", "movingAdsSpreadTierMod", "hipSpreadTierMod", "sprintRecoveryTierShift", "deployTimeTierShift"),
    "ergo": ("adsRecoilTierMod", "hipRecoilTierMod", "adsRecoilVariationTierMod", "hipRecoilVariationTierMod", "sprintRecoveryTierShift",
             "deployTimeTierShift", "reloadSpeedMult", "recoilDurationAdd"),
    "mag": ("adsTimeTierShift", "adsMoveSpeedTierShift", "sprintRecoveryTierShift", "deployTimeTierShift", "movingAdsSpreadTierMod",
            "reloadSpeedTier", "weaponSwayMult"),
}
DEFAULT = {"weaponSwayMult": 1, "adsRecoilDecayMult": 1, "hipRecoilDecayMult": 1, "recoilDurationOverride": None, "reloadSpeedMult": 1}


def live_branches(rec):
    return [b for b in rec["branches"] if not b["kill"]["default"]]


def id_selectors(rec):
    return tuple(sorted({s["unlock"] for b in live_branches(rec) for s in b["selectors"] if "/_weaponmodifiers/" in s["unlockRoute"].lower()}))


def sway7(v):
    for x in (2 / 3, 4 / 9, 1.5, 2.25):
        if abs(v - x) < 2e-6:
            return round(x, 7)
    return round(v, 7)


def raw_fields(rec):
    """Site-named effect fields read from the raw operands of one attachment record, plus notes."""
    out, notes = {}, []
    per_branch = []
    for b in live_branches(rec):
        acc = collections.defaultdict(list); seen = set()
        for s in b["selectors"]:
            for e in s["effects"]:
                op = e.get("operand") or {}
                key = (e["src"], e.get("holder"), e["asset"], json.dumps(op, sort_keys=True), json.dumps(e.get("values"), sort_keys=True))
                if key in seen and not e.get("local"):
                    continue
                seen.add(key)
                name = e["asset"].lower()
                cond = bool(op.get("conditional")) or "deployed" in name or "bipod" in name
                for k in ("adsAnimation", "adsFov", "adsMoveSpeed", "sprintRecovery", "deployTime"):
                    if k in op and op[k] is not None:
                        acc[k].append(op[k])
                if e.get("class") == "Class_743a3ce0":
                    for k, holder in (("hipSpread", "Field_b53510be"), ("movingAdsSpread", "Field_2ffeb6ac")):
                        if k in op:
                            if cond:
                                notes.append("conditional %s %s (%s) not applied" % (k, op[k], e["asset"]))
                            elif e.get("holder") != holder:
                                notes.append("%s %s bound in GS list %s, not %s; not applied (%s)" % (k, op[k], e.get("holder"), holder, e["asset"]))
                            else:
                                acc[k].append(op[k])
                if e.get("class") == "Class_bb838ff6":
                    for k in ("adsRecoil", "hipRecoil", "adsRecoilVariation", "hipRecoilVariation"):
                        if k in op:
                            if cond:
                                notes.append("conditional %s %s (%s) not applied" % (k, op[k], e["asset"]))
                            else:
                                acc[k].append((op[k], e["asset"]))
                    for path, f in SMOOTH.items():
                        if path in (op.get("scalars") or {}):
                            acc[f].append(op["scalars"][path])
                if "weaponSway" in op and not e.get("local"):
                    acc["weaponSway"].append(op["weaponSway"])
                if "weaponSway" in op and e.get("local"):
                    notes.append("weapon-local sway object %s (not a shared modifier; ignored as on the site)" % op["weaponSway"])
                if "reloadSpeed" in op:
                    acc["reloadSpeed"].append(op["reloadSpeed"])
                if "magCapacityRaw" in op:
                    acc["magCapacityRaw"].append(op["magCapacityRaw"])
        f = {}
        a, v = acc.get("adsAnimation", []), acc.get("adsFov", [])
        if len(a) > 1 or len(v) > 1:
            notes.append("multiple ADS animation/FOV effects %s/%s" % (a, v))
        a0, v0 = (a[0] if a else 0), (v[0] if v else 0)
        if a0 != v0:
            notes.append("ADS animation %s and FOV %s steps differ" % (a0, v0))
        f["adsStep"] = a0
        for k, site, sign in (("adsMoveSpeed", "adsMoveSpeedTierShift", -1), ("sprintRecovery", "sprintRecoveryTierShift", -1),
                              ("deployTime", "deployTimeTierShift", -1), ("hipSpread", "hipSpreadTierMod", -1), ("movingAdsSpread", "movingAdsSpreadTierMod", 1)):
            vs = acc.get(k, [])
            if len(vs) > 1:
                notes.append("multiple %s operands %s summed" % (k, vs))
            f[site] = sign * sum(vs)
        for k, site in (("adsRecoil", "adsRecoilTierMod"), ("hipRecoil", "hipRecoilTierMod"), ("adsRecoilVariation", "adsRecoilVariationTierMod"),
                        ("hipRecoilVariation", "hipRecoilVariationTierMod")):
            vs = acc.get(k, [])
            if len(vs) > 1:
                notes.append("multiple %s operands %s summed" % (k, ["%s=%s" % (n, x) for x, n in vs]))
            f[site] = sum(x for x, _ in vs)
        for site in SMOOTH.values():
            vs = acc.get(site, [])
            if vs:
                if len(set(vs)) > 1:
                    notes.append("multiple %s operands %s" % (site, vs))
                f[site] = vs[0]
        ws = acc.get("weaponSway", [])
        if ws:
            p = 1.0
            for x in ws: p *= x
            f["weaponSwayMult"] = sway7(p)
        if acc.get("reloadSpeed"):
            f["reloadSpeed"] = acc["reloadSpeed"][0]
        if acc.get("magCapacityRaw"):
            f["magCapacityRaw"] = acc["magCapacityRaw"][0]
        per_branch.append(f)
    if not per_branch:
        return {}, ["no live ability branch"]
    if any(json.dumps(p, sort_keys=True) != json.dumps(per_branch[0], sort_keys=True) for p in per_branch[1:]):
        notes.append("ability branches disagree")
    return per_branch[0], sorted(set(notes))


def signature(rec):
    """Weapon-independent effect signature of a record (which modifiers, with which operands)."""
    sig = set()
    for b in live_branches(rec):
        for s in b["selectors"]:
            for e in s["effects"]:
                op = {k: v for k, v in (e.get("operand") or {}).items()}
                sig.add((e["src"], e.get("holder") or "", "local:" + str(e.get("class")) if e.get("local") else e["asset"],
                         json.dumps(op or e.get("values") or {}, sort_keys=True)))
    return frozenset(sig)


def site_effective(wid, slot, aid):
    """The site's effective record for one selection (catalogue entry merged with its per-weapon maps)."""
    if slot == "mag":
        return dict(CAT["WEAPON_MAG"][wid]["mags"][aid])
    e = BYID[slot][aid]
    r = {k: v for k, v in e.items() if not isinstance(v, dict) or k in ("utilities",)}
    r.update((e.get("weaponOverrides") or {}).get(wid, {}))
    r.update((e.get("frostyModifiers") or {}).get(wid, {}))
    if slot == "barrel":
        r["adsTimeTierMod"] = (e.get("adsTimeTierModByWeapon") or {}).get(wid)
    return r


def raw_site_fields(slot, f):
    """Raw fields in the site's field names for this slot."""
    r = {k: f.get(k, 0) for k in FIELDS[slot]}
    if slot in ("grip", "barrel"):
        r["adsTimeTierMod"] = f.get("adsStep", 0)
    if slot == "mag":
        r["adsTimeTierShift"] = -f.get("adsStep", 0)
        rs = f.get("reloadSpeed", 1)
        r["reloadSpeedTier"] = next((i for i, x in enumerate(RELOAD_TIERS) if abs(x - rs) < 1e-6), "unmapped %s" % rs)
        r["weaponSwayMult"] = f.get("weaponSwayMult", 1)
    if slot == "muzzle":
        for k in ("weaponSwayMult", "adsRecoilDecayMult", "hipRecoilDecayMult"):
            r[k] = f.get(k, 1)
        r["recoilDurationOverride"] = f.get("recoilDurationOverride")
    if slot == "ergo":
        r["reloadSpeedMult"] = f.get("reloadSpeed", 1)
    return r


def eq(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and not isinstance(a, bool) and not isinstance(b, bool):
        return abs(a - b) <= 1e-5 * max(1, abs(a), abs(b))
    return a == b


VARIANT_SUFFIX = re.compile(r"_(sr|svk86|ks18k|db12|vssm|sl9|lmr27|interdictor|smg)$")


def resolve(maps, slot, rec, w, in_game_name=None):
    """Site id for a raw record on weapon w. Returns (id or None, method, candidates)."""
    sels, stem, cost = id_selectors(rec), rec["stem"], rec["cost"]
    cands = dict(maps["selector"].get((slot, sels), {}))
    if not cands or not sels:
        st = dict(maps["stem"].get((slot, stem.lower()), {}))
        if st and not sels:
            cands = st
        if not cands:
            return None, "new (no existing weapon has this selector set)", {}
    method = "selector"
    def narrow(pred, label):
        nonlocal cands, method
        c2 = {k: v for k, v in cands.items() if pred(k)}
        if c2 and len(c2) < len(cands):
            cands = c2; method += "+" + label
    if len(cands) > 1 and slot == "mag":
        return None, "magazine (id from capacity)", cands
    if len(cands) > 1:   # stored cost must equal the catalogue cost
        def cost_ok(k):
            e = BYID.get(slot, {}).get(k)
            if e is None: return False
            return any(c == cost for c in [e.get("pts")] + [o.get("pts") for o in (e.get("weaponOverrides") or {}).values() if "pts" in o])
        narrow(cost_ok, "cost")
    if len(cands) > 1:   # sniper-rifle variants
        sr = w["cls"] == "Sniper Rifle"
        if any(k.endswith("_sr") for k in cands):
            narrow(lambda k: k.endswith("_sr") == sr, "class")
    if len(cands) > 1:   # ids that exist for one weapon only are that weapon's own variants
        narrow(lambda k: len(USERS[(slot, k)]) > 1 or USERS[(slot, k)] == {w["siteId"]}, "shared-id")
    if len(cands) > 1:
        st = maps["stemsel"].get((slot, stem.lower(), sels), {})
        narrow(lambda k: k in st, "stem")
    if len(cands) > 1 and in_game_name:
        narrow(lambda k: (BYID.get(slot, {}).get(k) or {}).get("name", "").lower() == in_game_name.lower(), "in-game name")
    if len(cands) == 1:
        return next(iter(cands)), method, cands
    return None, "ambiguous", cands


def optic_category(label):
    label = (label or "").strip()
    if label == "Basic Sight": return "iron"
    if label == "Thermal Hybrid": return "therm_hyb"
    if label.startswith("Thermal "): return "thermal"
    if label.startswith(("Sight ", "Scope ")): return "std_optic"
    return {"Variable 1-4x": "var_low", "Variable 1.5-4.5x": "var_low", "Variable 1-5x": "var_high", "Variable 1-6x": "var_high",
            "Variable 2-8x": "var_high", "Variable 3-10x": "var_high"}.get(label)


_GLOBAL = {}
def global_tables():
    """Tables that need every existing weapon: slots_by_name, shared model anchors, optic peers."""
    if _GLOBAL:
        return _GLOBAL
    slots_by_name = collections.defaultdict(set)
    for r in ROWS:
        internal = BY_SITE[r["weapon"]]["stem"]
        name = pathlib.PurePosixPath(r["source"].split("#")[0]).stem
        name = re.sub(r"^(Attachment_|U_PRG_)", "", name, flags=re.I)
        slots_by_name[ui.normalized(ui.without_slot(name))].add(r["slot"])
    shared = collections.defaultdict(set)   # (slot, model, selectors) -> AD assets
    peers = collections.defaultdict(set)    # optic (model, selectors) -> AD assets
    for w in ROSTER:
        if w["new"]:
            continue
        gph = graph.weapon_graph(w["siteId"], w["folder"], w["stem"])
        for rec in gph["attachments"]:
            name = rec["attachment"][len("Attachment_"):]
            if rec["category"] == "Sight":
                link = IDX.weapon_ui(name, "sight", {ui.normalized(ui.without_slot(name)): {"sight"}})
                sels = tuple(sorted({s["unlock"] for b in rec["branches"] for s in b["selectors"]}))
                if link and sels:
                    peers[(ui.normalized(name.split("_SCP_", 1)[-1]), sels)].update(link["assets"])
                continue
            for slot, _ in TRUTH.get((w["siteId"], rec["attachment"].lower()), []):
                link = IDX.weapon_ui(name, slot, slots_by_name)
                parts = re.split(r"_(?:MZL|BTM|RGT|LFT|TOP|ERG|AMO)_", name, maxsplit=1, flags=re.I)
                sels = id_selectors(rec)
                if link and len(parts) == 2 and sels and slot in ("muzzle", "grip", "laser", "light", "ergo", "ammo"):
                    shared[(slot, ui.normalized(parts[1]), sels)].update(link["assets"])
    _GLOBAL.update(slots_by_name=slots_by_name, shared=shared, peers=peers)
    return _GLOBAL


def ui_link(name, slot, sels):
    gt = global_tables()
    sbn = gt["slots_by_name"]
    key = ui.normalized(ui.without_slot(name))
    if slot not in sbn.get(key, set()):
        sbn = dict(sbn); sbn[key] = set(gt["slots_by_name"].get(key, set())) | {slot}
    link = IDX.weapon_ui(name, slot, sbn)
    if not link:
        parts = re.split(r"_(?:MZL|BTM|RGT|LFT|TOP|ERG|AMO)_", name, maxsplit=1, flags=re.I)
        if len(parts) == 2 and sels:
            assets = sorted(gt["shared"].get((slot, ui.normalized(parts[1]), sels), set()))
            if assets and IDX.consensus(assets):
                link = {"method": "shared-model-and-selector-consensus", "assets": assets}
    return link


_OWN = {}
def own_name(w, name):
    """In-game model name of a record from the weapon's own AAM (unique text or None)."""
    if not _OWN:
        for r in ui.aam_records():
            _OWN.setdefault(r["aam"].rsplit("/", 1)[-1].lower()[4:], {}).setdefault(ui.normalized(r["name"]), set()).add(r["inGameName"].get("text"))
    t = _OWN.get(w["stem"].lower(), {})
    for key in (ui.normalized(name), ui.normalized(ui.without_slot(name)), ui.normalized(re.sub(r"_(RGT|LFT|TOP)_", "_", name, flags=re.I))):
        names = t.get(key)
        if names:
            return next(iter(names)) if len(names) == 1 and None not in names else None
    return None


def derive(w, maps=None):
    """Full attachment data for weapon w (roster row). maps: identity maps (leave-one-out for existing weapons)."""
    wid = w["siteId"]
    maps = maps or identity.build(ROWS, exclude_weapon=None if w["new"] else wid)
    gph = graph.weapon_graph(wid, w["folder"], w["stem"])
    out = {"weapon": wid, "records": [], "skipped": [], "new": [], "notes": []}
    choices = collections.defaultdict(dict)   # slot -> id -> info
    by_hash = {}
    optics = []
    accessories = []
    for rec in gph["attachments"]:
        by_hash[rec["idHash"] & 0xFFFFFFFF] = rec
    for rec in gph["attachments"]:
        name = rec["attachment"][len("Attachment_"):]
        lb = live_branches(rec)
        base = {"stem": rec["stem"], "attachment": rec["attachment"], "category": rec["category"], "cost": rec["cost"],
                "physicalSlots": sorted({b["slot"] for b in lb}), "selectors": list(id_selectors(rec)),
                "killRows": sorted({b["kill"]["row"] or "" for b in rec["branches"]})}
        if not rec["branches"]:
            out["skipped"].append({**base, "reason": "no ability branch"}); continue
        if not lb:
            out["skipped"].append({**base, "reason": "kill switch on by default"}); continue
        if rec["cost"] == 0 and not any(b["selectors"] for b in lb):
            out["skipped"].append({**base, "reason": "empty-slot placeholder (cost 0, no selector)"}); continue
        f, notes = raw_fields(rec)
        base.update(raw=f, notes=notes)
        if rec["category"] == "Sight":
            link = IDX.weapon_ui(name, "sight", {ui.normalized(ui.without_slot(name)): {"sight"}})
            model = ui.normalized(name.split("_SCP_", 1)[-1])
            allsels = tuple(sorted({s["unlock"] for b in rec["branches"] for s in b["selectors"]}))
            if not link and model == "ironsights":
                a = "common/ui/static/metadata/attachments/%s/ad_%s_sight" % (w["stem"].lower(), w["stem"].lower())
                if a in IDX.desc:
                    link = {"method": "same-weapon-iron-sight-descriptor", "assets": [a]}
            if link and not all(a in IDX.desc for a in link["assets"]):
                base["uiAssetsNotHeld"] = [a for a in link["assets"] if a not in IDX.desc]
            if (not link or base.get("uiAssetsNotHeld")) and global_tables()["peers"].get((model, allsels)):
                link = {"method": "same-optic-model-and-selector", "assets": sorted(global_tables()["peers"][(model, allsels)])}
                base.pop("uiAssetsNotHeld", None)
            labels = set(IDX.labels(link["assets"])) if link else set()
            label = next(iter(labels)) if len(labels) == 1 and "" not in labels else None
            cat = optic_category(label) if label else None
            if not cat and model == "ironsights" and any(s["unlock"] == "U_WPM_IronSights" for b in lb for s in b["selectors"]):
                cat = "iron"
            base.update(slot="sight", siteId=cat, label=label, uiMethod=link and link["method"], uiAssets=link and link["assets"])
            optics.append(base); out["records"].append(base); continue
        if rec["category"] == "OpticAccessory":
            fam = rec["stem"].split("_", 1)[1] if "_" in rec["stem"] else rec["stem"]
            base.update(slot="accessory", siteId=ACCESSORY_FAMILIES.get(fam), family=fam)
            accessories.append(base); out["records"].append(base); continue
        res = None
        link0 = IDX.weapon_ui(name, CAT_SLOT.get(rec["category"], ["?"])[0], global_tables()["slots_by_name"])
        ign = own_name(w, name)
        for slot in CAT_SLOT.get(rec["category"], []):
            sid_, method, cands = resolve(maps, slot, rec, w, ign)
            if sid_ or method.startswith(("ambiguous", "magazine")):
                res = (slot, sid_, method, cands); break
        if res is None:
            res = (CAT_SLOT.get(rec["category"], ["?"])[0], None, "new (no existing weapon has this selector set)", {})
        slot, sid_, method, cands = res
        if slot == "mag":
            capraw = f.get("magCapacityRaw")
            base["magCapacityRaw"] = capraw
        link = ui_link(name, slot, id_selectors(rec))
        desc = IDX.consensus(link["assets"]) if link else None
        base.update(slot=slot, siteId=sid_, identity=method, candidates=cands, inGameName=ign,
                    uiMethod=link and link["method"], uiAssets=link and link["assets"],
                    uiAssetsNotHeld=[a for a in (link["assets"] if link else []) if a not in IDX.desc],
                    descriptionIds=desc and desc[0], description=desc and desc[1])
        out["records"].append(base)
    out["baseIndices"], out["deploy"], out["equipment"] = gph["baseIndices"], gph["deploy"], gph["equipment"]
    out["byHash"] = {h: r["attachment"] for h, r in by_hash.items()}
    return out


if __name__ == "__main__":
    import sys
    w = BY_SITE[sys.argv[1]]
    d = derive(w)
    for r in d["records"]:
        if r.get("slot") in ("sight", "accessory") and len(sys.argv) < 3:
            continue
        print("%-10s %-30s %3s -> %-22s %-34s ui=%-32s desc=%s %s" % (r.get("slot"), r["stem"], r["cost"], r.get("siteId"), r.get("identity", ""),
              r.get("uiMethod"), r.get("descriptionIds"), "; ".join(r.get("notes", []))))
    for s in d["skipped"]:
        print("skipped", s["stem"], s["cost"], s["reason"])
