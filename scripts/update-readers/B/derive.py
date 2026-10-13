"""Stage 9 part B: projectile and ammunition side, derived from 2.1.1.0 raw EBX + GRX_Weapons registry.

For the 63 site weapons (identity map) and the four new ones, writes derived.json with, per weapon:
  wb/gs/ability/equipment routes; base projectile (WB Class_35259f6b Field_58d70acb Field_808dd66c);
  protection index (registry ...Shot.DamageProtectionMultiplierIndex, else WB Field_9ba8b76b);
  penetration index (registry ...Shot.DamagePenetrationMultiplierIndex, else WB Field_7e2be65f);
  muzzle velocity (registry ...Shot.InitialSpeed.z, else WB Field_0bf4f62b/Field_32a99b9c);
  default-preset attachment ids (Equipment root Field_6780584d entry with Field_b656da95 true);
  every ammunition attachment (Attachment_*_AMO_*): point cost, id, ability branches, kill switch,
  and the effects reached through its selectors (same joins as <run>/uncaptured/attgraph.py):
     Class_e85fff64 Field_fbfacac9  protection step        Class_d11a23a2 Field_fbfacac9  penetration step
     any effect Field_808dd66c -> /_Bullets/  projectile swap
     Class_3e93759b Field_6a5c4efd  muzzle velocity factor  Class_303a33cc Field_c427eabf  ADS move speed step
     Class_5830cb87 Field_8359723e  health regen delay add  Class_0045e7fa d98b0371 / 6f8d5f40  2D / 3D spot factor
     GS Class_bb838ff6  recoil amount / variation steps (ads Field_6b84de87, hip Field_7b609515)
  and per projectile: gravity, drag, material, health damage curve (Field_2ad7e688 flat array, registry
  TweakableDamageCurve.XYValues where a row exists).
Hit zones use the bounded MaterialGrid reader from the research repo's frosty-hit-zones.py only.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import importlib.util, json, pathlib, struct, collections, re, sys
import common as c

HERE = settings.part("B")
NEW = {"mk24": "MRGGA", "elr40": "CDX40", "z84m": "PKM", "rspr": "RSAR999"}
NEW_CLS = {"mk24": "Assault Rifle", "elr40": "Sniper Rifle", "z84m": "LMG", "rspr": "SMG"}
SHOT = ".WeaponEntityData.WeaponFiring.PrimaryFire.Shot."
BULLETS = "/_bullets/"

spec = importlib.util.spec_from_file_location("hz", c.REPO / "scripts/frosty-hit-zones.py")
hz = importlib.util.module_from_spec(spec); spec.loader.exec_module(hz)


def f32(x):
    """Shortest decimal that is the same float32."""
    if x is None:
        return None
    t = struct.unpack("<f", struct.pack("<f", x))[0]
    for nd in range(0, 10):
        s = round(x, nd)
        if struct.unpack("<f", struct.pack("<f", s))[0] == t:
            return s
    return x


def signed(v):
    return v - (1 << 32) if isinstance(v, int) and v >= 1 << 31 else v


# ---------------------------------------------------------------- material grids (bounded reader only)
class Grid:
    def __init__(self, level):
        types_by_guid, _ = hz.type_descriptors(c.BUILD / "capture/toolchain/SharedTypeDescriptors.ebx")
        path = c.BUILD / ("capture/collection/raw/Game/GlacierMP/levels/%s/%s/materialgrid_win32.ebx" % (level, level))
        self.level = level
        self.g = hz.MaterialGrid(path, types_by_guid)

    def head_limb(self, s, t):
        return self.g.protection(s, t)

    def collateral(self, s, t):
        """Class_6aa794ef float array at +24 in the (s, t) cell; same cell walk as MaterialGrid.protection."""
        g = self.g
        row_offset, row_count, _ = g.array(g.rows_offset + 8 * g.index_map[s])
        cell = row_offset + 16 * g.index_map[t]
        out = []
        for side in (0, 8):
            groups, gn, _ = g.array(cell + side)
            for gi in range(gn):
                items, m, _ = g.array(groups + 8 * gi)
                for it in range(m):
                    off, typ = g.pointer(items + 16 * it)
                    if typ is not None and typ["hash"] == "6aa794ef":
                        vals, count, flags = g.array(off + 24)
                        if flags != hz.FLOAT32_ARRAY_FLAGS or not 0 < count <= 32:
                            raise ValueError("unexpected collateral array")
                        out.append([round(struct.unpack_from("<f", g.data, g.data_start + vals + 4 * k)[0], 6) for k in range(count)])
        return out


# ---------------------------------------------------------------- weapon files
def find_weapon(internal):
    gs = [k for k in c.held if k.endswith("/gs_" + internal.lower()) and "/hardware/weapons/" in k]
    if len(gs) != 1:
        raise ValueError("%s: GS files %s" % (internal, gs))
    folder = gs[0].rsplit("/", 1)[0] + "/"
    inf = [k for k in c.held if k.startswith(folder) and "/" not in k[len(folder):]]
    wb = [k for k in inf if k.endswith("_wb")]
    ab = [k for k in inf if k.endswith("_ability")]
    if len(ab) > 1:   # under-barrel and bipod abilities sit beside the weapon ability
        ab = [k for k in ab if k == folder + internal.lower() + "_ability"]
    eq = [k for k in inf if k[len(folder):].startswith("equipment_")]
    if len(wb) != 1 or len(ab) != 1:
        raise ValueError("%s: WB %s ability %s" % (internal, wb, ab))
    amo = sorted(k for k in inf if k[len(folder):].startswith("attachment_") and "_amo_" in k)
    return {"folder": folder, "gs": gs[0], "wb": wb[0], "ability": ab[0], "equipment": eq, "ammoAttachments": amo}


_proj = {}


def projectile(route, guid):
    key = c.proper[route.lower()]
    if key not in _proj:
        objs, by = c.load(route)
        o = by[guid]
        name = key.rsplit("/", 1)[-1]
        packed = o["Field_c7584f55"]["Field_48288193"]
        _, curve = c.deref(o.get("Field_2ad7e688"), objs)
        own = curve.get("Field_5279388d") if curve else None
        own_points = len(curve.get("Field_edfc6df6") or []) if curve else None
        regrow = c.reg_value(name + ".BulletEntityData.TweakableDamageCurve.XYValues")
        reg = regrow.get("Field_ffba60f0") if isinstance(regrow, dict) else regrow
        live = reg if reg is not None else own
        grav_reg, drag_reg = c.reg_value(name + ".BulletEntityData.Gravity"), c.reg_value(name + ".BulletEntityData.Drag")
        _proj[key] = {
            "guid": guid, "file": c.held[route.lower()].replace("\\", "/").split("/builds/%s/" % settings.BUILD_LABEL)[-1],
            "packedMaterial": "0x%08x" % packed, "material": packed >> 20,
            "gravityOwn": f32(o.get("Field_d9d33d20")), "dragOwn": f32(o.get("Field_30c37c24")),
            "gravityRegistry": f32(grav_reg) if grav_reg is not None else None,
            "dragRegistry": f32(drag_reg) if drag_reg is not None else None,
            "gravityMps2": f32(grav_reg if grav_reg is not None else o.get("Field_d9d33d20")),
            "dragPerMeter": f32(drag_reg if drag_reg is not None else o.get("Field_30c37c24")),
            "curveOwn": [f32(v) for v in own] if own else None, "curveOwnPointListLength": own_points,
            "curveRegistry": [f32(v) for v in reg] if reg else None,
            "curve": [[f32(live[i]), f32(live[i + 1])] for i in range(0, len(live), 2)] if live else None,
            "registryRows": sum(1 for k in c.registry() if k.startswith(name + ".")),
        }
    return key


def shot_block(wb_objs):
    blocks = [o["Field_58d70acb"] for o in wb_objs if o["$class"] == "Class_35259f6b" and isinstance(o.get("Field_58d70acb"), dict)]
    if not blocks:
        raise ValueError("no primary shot block")
    return blocks[0], len(blocks)


def graph(w):
    """Ammo attachments -> effects. Same joins as uncaptured/attgraph.py."""
    ab_objs, _ = c.load(w["ability"]); wb_objs, _ = c.load(w["wb"]); gs_objs, _ = c.load(w["gs"])
    by_prog = collections.defaultdict(list)
    for m in ab_objs[0].get("Field_d7605aab", []):
        _, br = c.deref(m, ab_objs)
        if br is not None and c.imp(br.get("Field_f86e0433")):
            by_prog[c.imp(br["Field_f86e0433"])].append(br)
    mod_by_sel = collections.defaultdict(list); missing = []

    def find_lists(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "Field_0cd9f20f" and isinstance(v, list):
                    for m in v:
                        r, mo = c.deref(m, wb_objs)
                        if mo is None:
                            if r: missing.append(r)
                            continue
                        for s in mo.get("Field_819acc98", []) or []:
                            mod_by_sel[str(s).lower()].append((r, mo))
                else:
                    find_lists(v)
        elif isinstance(x, list):
            for v in x:
                find_lists(v)
    find_lists(wb_objs)
    bind_by_sel = collections.defaultdict(list)

    def find_bind(x):
        if isinstance(x, dict):
            if "Field_2f0e5b83" in x and "Field_6d011165" in x:
                bind_by_sel[str(x["Field_6d011165"]).lower()].append(x)
            for v in x.values():
                find_bind(v)
        elif isinstance(x, list):
            for v in x:
                find_bind(v)
    find_bind(gs_objs)

    out = []
    for route in w["ammoAttachments"]:
        a = c.load(route)[0][0]
        name = a["Field_0c59fa06"].rsplit("/", 1)[-1]
        prog = c.imp(a.get("Field_157a7d74")); cat = c.imp(a.get("Field_fe77e9a9"))
        rec = {"attachment": name, "suffix": re.split("_AMO_", name, flags=re.I)[1], "id": a.get("Field_de6f63b3"),
               "category": (cat[0] or "?").rsplit("/", 1)[-1] if cat else None, "pointCost": a.get("Field_6ee865a5"),
               "pointCostList": [x.get("Field_6ee865a5") for x in a.get("Field_f6a09c90") or []],
               "progression": (prog[0] or "?").rsplit("/", 1)[-1] if prog else None, "branches": []}
        for br in by_prog.get(prog, []) if prog else []:
            slot = c.imp(br.get("Field_64ef48eb"))
            ks = br.get("Field_def7f8dd") or {}
            kr, ko = c.deref((ks.get("Field_e0b43a29") or {}).get("Field_6b28f68f"), ab_objs)
            b = {"slot": (slot[0] or "?").rsplit("/", 1)[-1] if slot else None,
                 "killSwitchRow": ko.get("Field_0c59fa06") if ko else None,
                 "killSwitchDefault": bool(c.unbox(ko.get("Field_42c8b257"))) if ko else None,
                 "killLocalFallback": ks.get("Field_043d7a08"),
                 "selectors": [], "protectionSteps": 0, "penetrationSteps": [], "swaps": [], "velocityFactors": [],
                 "adsMoveSpeedSteps": [], "regenDelayAdd": [], "spot2D": [], "spot3D": [],
                 "recoil": {"adsAmount": 0, "hipAmount": 0, "adsVariation": 0, "hipVariation": 0}, "other": [], "issues": []}
            seen = set()
            for am in br.get("Field_ffba60f0", []):
                _, act = c.deref(am, ab_objs)
                if act is None:
                    continue
                if act["$class"] != "Class_4ed159fb":
                    b["issues"].append("action type " + act["$class"])
                for u in act.get("Field_7e54e22c", []) or []:
                    sel = c.imp(u)
                    if not sel or not sel[0] or "/_weaponmodifiers/" not in sel[0].lower():
                        continue
                    b["selectors"].append(sel[0].rsplit("/", 1)[-1])
                    hits = 0
                    for mr, mo in mod_by_sel.get(sel[1], []):
                        for e in mo.get("Field_9690d604", []) or []:
                            er, eo = c.deref(e, wb_objs if mr is None else c.load(mr)[0])
                            er = er or mr
                            hits += 1
                            if eo is None:
                                b["issues"].append("missing effect asset " + str(er)); continue
                            ident = (er, eo.get("$guid"))
                            if ident in seen:
                                continue
                            seen.add(ident)
                            cls = eo["$class"]; asset = (er or "WB").rsplit("/", 1)[-1]
                            if er and "/muzzlevfx/" in er.lower():
                                continue
                            if cls == "Class_e85fff64":
                                b["protectionSteps"] += signed(eo.get("Field_fbfacac9"))
                            elif cls == "Class_d11a23a2":
                                b["penetrationSteps"].append(signed(eo.get("Field_fbfacac9")))
                            elif cls == "Class_3e93759b":
                                b["velocityFactors"].append({"asset": asset, "factor": f32(eo.get("Field_6a5c4efd")),
                                                             "fields": {k[6:]: v for k, v in eo.items() if k.startswith("Field_") and not isinstance(v, (dict, list)) and k not in ("Field_0c59fa06",)}})
                            elif cls == "Class_303a33cc":
                                b["adsMoveSpeedSteps"].append(signed(eo.get("Field_c427eabf")))
                            elif cls == "Class_5830cb87":
                                b["regenDelayAdd"].append(f32(eo.get("Field_8359723e")))
                            elif cls == "Class_0045e7fa":
                                if "2d" in asset.lower(): b["spot2D"].append(f32(eo.get("Field_d98b0371")))
                                else: b["spot3D"].append(f32(eo.get("Field_6f8d5f40")))
                            else:
                                b["other"].append({"asset": asset, "class": cls})
                            ref = c.imp(eo.get("Field_808dd66c"))
                            if ref and ref[0] and BULLETS in ref[0].lower():
                                if ref[0].lower() not in c.held:
                                    b["issues"].append("swap projectile not captured: " + ref[0])
                                else:
                                    b["swaps"].append({"via": asset, "projectile": projectile(ref[0], ref[1])})
                    for bd in bind_by_sel.get(sel[1], []):
                        gr, go = c.deref(bd["Field_2f0e5b83"], gs_objs)
                        hits += 1
                        if go is None:
                            b["issues"].append("missing GS modifier " + str(gr)); continue
                        asset = (gr or "GS").rsplit("/", 1)[-1]
                        if go["$class"] == "Class_bb838ff6":
                            for aim, f in (("ads", "Field_6b84de87"), ("hip", "Field_7b609515")):
                                for nm, m in (("Amount", "Field_22ce7cf3"), ("Variation", "Field_02433593")):
                                    v = ((go.get(f) or {}).get(m) or {}).get("Field_4692836a")
                                    if v:
                                        b["recoil"][aim + nm] += signed(v)
                            b.setdefault("recoilAssets", []).append(asset)
                        else:
                            b["other"].append({"asset": asset, "class": go["$class"], "gs": True})
                    if not hits:
                        b["issues"].append("selector with no WB/GS match: " + sel[0].rsplit("/", 1)[-1])
            rec["branches"].append(b)
        out.append(rec)
    return out, sorted(set(missing))


def main():
    ids = json.load(open(c.REPO / "reference-data/provenance/frosty-weapon-identities.json", encoding="utf-8"))["weapons"]
    weapons = [(r["siteId"], r["internalId"], False) for r in ids] + [(k, v, True) for k, v in NEW.items()]
    grids = []
    for level in ("mp_abbasid", "mp_badlands"):
        try:
            grids.append(Grid(level))
        except FileNotFoundError:
            print("grid not held:", level)
    bones_objs, _ = c.load("Common/Gameplay/Soldier/GlacierSoldierBoneCollision")
    bone_mat = {}

    def find_bones(x):
        if isinstance(x, dict):
            if "Field_c6156e75" in x and isinstance(x.get("Field_c7584f55"), dict):
                bone_mat[x["Field_c6156e75"]] = x["Field_c7584f55"]["Field_48288193"] >> 20
            for v in x.values():
                find_bones(v)
        elif isinstance(x, list):
            for v in x:
                find_bones(v)
    find_bones(bones_objs)
    limb = {bone_mat[n] for n in hz.LIMB_BONES}
    assert len(limb) == 1, limb
    head_m, abd_m, limb_m = bone_mat[hz.HEAD_BONE], bone_mat[hz.ABDOMEN_BONE], limb.pop()

    def lookup(fn, s, t):
        vals = [getattr(g, fn)(s, t) for g in grids]
        if any(v != vals[0] for v in vals[1:]):
            raise ValueError("grids disagree %s %d->%d: %s" % (fn, s, t, vals))
        return vals[0]

    zone_cache = {}

    def zones(material):
        if material not in zone_cache:
            try:
                head, lim, abd = lookup("head_limb", material, head_m), lookup("head_limb", material, limb_m), lookup("head_limb", material, abd_m)
                coll = {name: lookup("collateral", material, t) for name, t in (("head", head_m), ("limb", limb_m), ("abdomen", abd_m))}
                zone_cache[material] = {"head": head, "limb": lim, "abdomen": abd, "collateralTables": coll}
            except Exception as e:
                zone_cache[material] = {"error": str(e)}
        return zone_cache[material]

    out = {"build": settings.BUILD_LABEL, "soldierMaterials": {"head": head_m, "abdomen": abd_m, "limb": limb_m, "all": bone_mat},
           "grids": [{"level": g.level, "sha256": g.g.sha256, "bytes": len(g.g.data), "indexMap": len(g.g.index_map), "rows": g.g.row_count} for g in grids],
           "weapons": {}}
    for site_id, internal, is_new in weapons:
        try:
            w = find_weapon(internal)
        except ValueError as e:
            out["weapons"][site_id] = {"error": str(e)}; print("ERROR", site_id, e); continue
        wb_objs, _ = c.load(w["wb"])
        wb_name = c.proper[w["wb"]].rsplit("/", 1)[-1]
        shot, nblocks = shot_block(wb_objs)
        ref = c.imp(shot.get("Field_808dd66c"))
        base = projectile(ref[0], ref[1])
        reg_prot = c.reg_value(wb_name + SHOT + "DamageProtectionMultiplierIndex")
        reg_pen = c.reg_value(wb_name + SHOT + "DamagePenetrationMultiplierIndex")
        reg_vel = c.reg_value(wb_name + SHOT + "InitialSpeed.z")
        file_prot, file_pen = signed(shot.get("Field_9ba8b76b")), signed(shot.get("Field_7e2be65f"))
        file_vel = f32((shot.get("Field_0bf4f62b") or {}).get("Field_32a99b9c"))
        default_ids, all_eq_ids = [], set()
        for eq in w["equipment"]:
            eobjs, _ = c.load(eq)
            for p in eobjs[0].get("Field_6780584d") or []:
                ids_ = [x.get("Field_c1ad37da") for x in p.get("Field_6bf3cb97") or []]
                all_eq_ids.update(ids_)
                if p.get("Field_b656da95"):
                    default_ids.append(ids_)
        atts, missing = graph(w)
        for a in atts:
            a["inDefaultPreset"] = any(a["id"] in d for d in default_ids)
            a["inAnyPreset"] = a["id"] in all_eq_ids
        out["weapons"][site_id] = {
            "internalId": internal, "isNew": is_new, "wb": c.proper[w["wb"]], "gs": c.proper[w["gs"]], "ability": c.proper[w["ability"]],
            "equipment": [c.proper[e] for e in w["equipment"]], "wbRegistryRows": sum(1 for k in c.registry() if k.startswith(wb_name + ".")),
            "shotBlocks": nblocks, "baseProjectile": base,
            "protectionIndex": {"registry": signed(reg_prot) if reg_prot is not None else None, "file": file_prot,
                                "live": signed(reg_prot) if reg_prot is not None else file_prot},
            "penetrationIndex": {"registry": signed(reg_pen) if reg_pen is not None else None, "file": file_pen,
                                 "live": signed(reg_pen) if reg_pen is not None else file_pen},
            "muzzleVelocity": {"registry": f32(reg_vel) if reg_vel is not None else None, "file": file_vel},
            "defaultPresetCount": len(default_ids), "ammo": atts, "missingWbModifiers": missing,
        }
    for key, p in _proj.items():
        p["zones"] = zones(p["material"])
    out["projectiles"] = _proj
    json.dump(out, open(HERE / "derived.json", "w", encoding="utf-8"), indent=1)
    print("weapons", len(out["weapons"]), "projectiles", len(_proj), "grids", [g.level for g in grids],
          "soldier materials head/abdomen/limb", head_m, abd_m, limb_m)


if __name__ == "__main__":
    main()
