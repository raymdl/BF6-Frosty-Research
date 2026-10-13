"""Raw attachment graph for one weapon (2.1.1.0 raw EBX, no XML export).

Same joins as attachment_graph() in the site's scripts/frosty-configuration.py and as
<run>/uncaptured/attgraph.py, with more kept per effect:
  ability root branches (Field_d7605aab) keyed by progression (Field_f86e0433)
  branch actions (Field_ffba60f0, Class_4ed159fb) unlock selectors (Field_7e54e22c) under /_WeaponModifiers/
  a selector GUID enables WB modifiers (Field_0cd9f20f members whose Field_819acc98 lists it; effects
  in Field_9690d604) and GS bindings (Field_2f0e5b83 modifier, Field_6d011165 selector)
Each GS binding keeps the name of the GS list that holds it (the site treats lists differently).
Results are cached as JSON under cache/.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import json, pathlib, collections, functools
from rawlib import *

HERE = settings.part("C")
CACHE = HERE / "cache"; CACHE.mkdir(exist_ok=True)
FLAGS743 = ("Field_b0057325", "Field_93dd77b9", "Field_b574fa40", "Field_15cae63e", "Field_897a3f2c", "Field_92cdfefc", "Field_9ca063e9")


def scalars(o, skip=("Field_0c59fa06", "Field_819acc98")):
    out = {}
    def walk(x, p):
        if isinstance(x, dict):
            if "$import" in x or "$ref" in x or "absoluteOffset" in x:
                return
            for k, c in x.items():
                if not k.startswith("$") and k not in skip:
                    walk(c, p + "/" + k[6:] if k.startswith("Field_") else p + "/" + k)
        elif isinstance(x, list):
            for i, c in enumerate(x):
                walk(c, p + "[%d]" % i)
        elif x not in (None, "", 0, 0.0, False, 1.0, -1):
            out[p.lstrip("/")] = x
    walk(o, "")
    return out


def g(o, *ks):
    for k in ks:
        o = o.get(k) if isinstance(o, dict) else None
    return o


def operand(route, o):
    c = o["$class"]; name = (route or "").lower(); d = {}
    if c == "Class_016623ac": d["adsAnimation"] = g(o, "Field_9540bd8e")
    elif c == "Class_104c2294": d["adsFov"] = g(o, "Field_9540bd8e")
    elif c == "Class_303a33cc": d["adsMoveSpeed"] = g(o, "Field_c427eabf")
    elif c == "Class_03db7a68": d["sprintRecovery"] = g(o, "Field_9540bd8e")
    elif c == "Class_4aac041b": d["deployTime"] = g(o, "Field_9540bd8e")
    elif c == "Class_743a3ce0":
        kind = "hipSpread" if "/hipdispersion/" in name else "movingAdsSpread" if "/adsmovedispersion/" in name else "spreadOther"
        d[kind] = g(o, "Field_9540bd8e", "Field_4692836a"); d["target"] = o.get("Field_94752c29")
        d["flags"] = "".join("T" if o.get(f) else "." for f in FLAGS743)
        if "bipod" in name or "grippod" in name or name.endswith("gdm_array_hipdispersion_btm_p20"):
            d["conditional"] = True
    elif c == "Class_bb838ff6":
        for aim, f in (("ads", "Field_6b84de87"), ("hip", "Field_7b609515")):
            for nm, m in (("Recoil", "Field_22ce7cf3"), ("RecoilVariation", "Field_02433593")):
                v = g(o, f, m, "Field_4692836a")
                if v: d[aim + nm] = v
        d["scalars"] = scalars(o)
    elif c == "Class_2fea847d": d["weaponSway"] = o.get("Field_90fd0310")
    elif c == "Class_28d25398": d["cameraSway"] = o.get("Field_90fd0310")
    elif c == "Class_9705264b": d["reloadSpeed"] = o.get("Field_348b8cd1")
    elif c == "Class_e7d2410a": d["magCapacityRaw"] = o.get("Field_7f22bfb4"); d["magOther"] = o.get("Field_4614adfe")
    return d


def weapon_graph(label, folder, stem, refresh=False):
    cp = CACHE / (label + ".json")
    if cp.exists() and not refresh:
        return json.load(open(cp, encoding="utf-8"))
    base = "common/hardware/weapons/" + folder.lower() + "/"
    ab_objs, _ = load(base + stem.lower() + "_ability")
    wb_objs, _ = load(base + stem.lower() + "_wb")
    gs_objs, _ = load(base + "gs_" + stem.lower())
    by_prog = collections.defaultdict(list)
    for m in ab_objs[0].get("Field_d7605aab", []):
        _, br = deref(m, ab_objs)
        if br is not None and imp(br.get("Field_f86e0433")):
            by_prog[imp(br["Field_f86e0433"])].append(br)
    mod_by_sel = collections.defaultdict(list); missing_mod = []
    def find_lists(x):
        if isinstance(x, dict):
            for k, c in x.items():
                if k == "Field_0cd9f20f" and isinstance(c, list):
                    for m in c:
                        r, mo = deref(m, wb_objs)
                        if mo is None:
                            if r: missing_mod.append(r)
                            continue
                        for s in mo.get("Field_819acc98", []) or []:
                            mod_by_sel[str(s).lower()].append((r, mo))
                else:
                    find_lists(c)
        elif isinstance(x, list):
            for c in x:
                find_lists(c)
    find_lists(wb_objs)
    bind_by_sel = collections.defaultdict(list)
    def find_bind(x, holder):
        if isinstance(x, dict):
            if "Field_2f0e5b83" in x and "Field_6d011165" in x:
                bind_by_sel[str(x["Field_6d011165"]).lower()].append((holder, x))
            for k, c in x.items():
                find_bind(c, k)
        elif isinstance(x, list):
            for c in x:
                find_bind(c, holder)
    find_bind(gs_objs, "")
    atts = []
    for route in sorted(k for k in held if k.startswith(base + "attachment_")):
        a = load(route)[0][0]
        cat_r = imp(a.get("Field_fe77e9a9")); prog = imp(a.get("Field_157a7d74"))
        full = a["Field_0c59fa06"].rsplit("/", 1)[-1]
        rec = {"attachment": full, "stem": full.split("_", 2)[2] if full.count("_") >= 2 else full, "route": route_case[route],
               "category": (cat_r[0] or "?").rsplit("/", 1)[-1].replace("AttachmentCategory_", "") if cat_r else None,
               "progression": (prog[0] or "?").rsplit("/", 1)[-1] if prog else None, "cost": a.get("Field_6ee865a5"),
               "idHash": a.get("Field_de6f63b3"), "branches": []}
        for br in by_prog.get(prog, []) if prog else []:
            slot = imp(br.get("Field_64ef48eb"))
            b = {"slot": (slot[0] or "?").rsplit("/", 1)[-1] if slot else None, "selectors": [], "issues": []}
            ks = br.get("Field_def7f8dd") or {}
            kr, ko = deref((ks.get("Field_e0b43a29") or {}).get("Field_6b28f68f"), ab_objs)
            b["kill"] = {"registry": (kr or "").rsplit("/", 1)[-1], "row": ko.get("Field_0c59fa06") if ko else None,
                         "default": bool(unbox(ko.get("Field_42c8b257"))) if ko else None, "localFallback": ks.get("Field_043d7a08")}
            for am in br.get("Field_ffba60f0", []):
                _, act = deref(am, ab_objs)
                if act is None:
                    continue
                if act["$class"] != "Class_4ed159fb":
                    b["issues"].append("action type " + act["$class"])
                for u in act.get("Field_7e54e22c", []) or []:
                    sel = imp(u)
                    if not sel or not sel[0]:
                        continue
                    low = sel[0].lower()
                    known = sel[1] in mod_by_sel or sel[1] in bind_by_sel
                    if "/_weaponmodifiers/" not in low and not known:
                        continue
                    s = {"unlock": sel[0].rsplit("/", 1)[-1], "unlockRoute": sel[0], "guid": sel[1], "effects": []}
                    seen = set()
                    for mr, mo in mod_by_sel.get(sel[1], []):
                        for e in mo.get("Field_9690d604", []) or []:
                            er, eo = deref(e, wb_objs if mr is None else load(mr)[0])
                            er = er or mr
                            if er and "/muzzlevfx/" in er.lower():
                                continue
                            if eo is None:
                                s["effects"].append({"src": "WB", "asset": (er or "?").rsplit("/", 1)[-1], "missing": True}); continue
                            key = (er, eo.get("$guid") or id(eo))
                            if key in seen:
                                continue
                            seen.add(key)
                            op = operand(er, eo)
                            s["effects"].append({"src": "WB", "asset": (er or "WB").rsplit("/", 1)[-1], "local": er is None, "class": eo["$class"],
                                                 "operand": op, "values": {} if (op and "scalars" not in op) else scalars(eo)})
                    for holder, bd in bind_by_sel.get(sel[1], []):
                        gr, go = deref(bd["Field_2f0e5b83"], gs_objs)
                        op = operand(gr, go) if go else {}
                        s["effects"].append({"src": "GS", "holder": holder, "asset": (gr or "GS").rsplit("/", 1)[-1], "local": gr is None,
                                             "class": go["$class"] if go else None, "operand": op, "bindIndex": bd.get("Field_3f680d24"),
                                             "values": {} if (not go or (op and "scalars" not in op)) else scalars(go)})
                    if not s["effects"]:
                        b["issues"].append("selector with no WB/GS match: " + s["unlock"])
                    b["selectors"].append(s)
            rec["branches"].append(b)
        atts.append(rec)
    # base indices and equipment dependencies
    wbname = wb_objs[0]["Field_0c59fa06"].rsplit("/", 1)[-1]
    reg = registry()
    basei = {}
    for o in wb_objs:
        if o["$class"] == "Class_542ac52c":
            for k, nm in (("Field_db03e8a9", "WeaponZoomTransitionIndex"), ("Field_5198399a", "SprintSettingsIndex"),
                          ("Field_dcb8bf9e", "WeaponZoomedMoveSpeedMultiplierIndex")):
                if isinstance(o.get(k), dict):
                    basei.setdefault(nm, {})["file"] = o[k].get("Field_2b6f2936")
    for nm in ("AnimationZoomSettingsIndex", "WeaponZoomTransitionIndex", "SprintSettingsIndex", "WeaponZoomedMoveSpeedMultiplierIndex"):
        v = reg.get("%s.%s.Index" % (wbname, nm))
        if v is not None:
            basei.setdefault(nm, {})["registry"] = v
    dep = []
    for o in wb_objs:
        if o["$class"] == "Class_01419c76":
            i = imp(o.get("Field_5b9b2235"))
            dep.append({"array": (i[0] or "?").rsplit("/", 1)[-1] if i else None, "index": g(o, "Field_2c3e0fbf", "Field_2b6f2936")})
    equip = []
    er = base + "equipment_" + stem.lower()
    if er in held:
        eo = load(er)[0]
        for ent in eo[0].get("Field_e70ce6be", []) or []:
            src = imp(g(ent, "Field_399fae20", "Field_d28dfb00"))
            equip.append({"source": src[0].rsplit("/", 1)[-1] if src and src[0] else None, "requires": [x & 0xFFFFFFFF for x in ent.get("Field_f4142987", []) or []]})
    out = {"label": label, "folder": folder, "stem": stem, "wb": wbname, "attachments": atts, "missingWbModifiers": sorted(set(missing_mod)),
           "baseIndices": basei, "deploy": dep, "equipment": equip, "hasEquipment": er in held}
    json.dump(out, open(cp, "w", encoding="utf-8"))
    return out


if __name__ == "__main__":
    import sys
    gph = weapon_graph(sys.argv[1], sys.argv[2], sys.argv[3], refresh=True)
    print(len(gph["attachments"]), "attachments", gph["baseIndices"], gph["deploy"], len(gph["equipment"]), "equipment entries", len(gph["missingWbModifiers"]), "missing WB modifier assets")
    for a in gph["attachments"]:
        if len(sys.argv) > 4 and sys.argv[4].lower() in a["attachment"].lower():
            print(json.dumps(a, indent=1))
