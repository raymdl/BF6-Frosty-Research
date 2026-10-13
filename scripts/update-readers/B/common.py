"""Shared raw-EBX loader for stage 9 part B (2.1.1.0). Read-only on everything outside this folder.

load(route) -> (objects, by_guid); imp(x) -> (route, classGuid); deref(x, objs) -> (route, object).
registry() -> {row name: value} for GRX_Weapons.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import importlib.util, pathlib, json

RUN = settings.RUN
REPO = settings.REPO
SITE = settings.SITE
D = settings.D
BUILD = settings.BUILD
spec = importlib.util.spec_from_file_location("dec", REPO / "scripts/frosty-ebx-decode.py")
dec = importlib.util.module_from_spec(spec); spec.loader.exec_module(dec)
types = dec.type_descriptors(BUILD / "capture/toolchain/SharedTypeDescriptors.ebx")
_cat = json.load(open(BUILD / "capture/collection/asset-catalog.json", encoding="utf-8"))
_rows = _cat if isinstance(_cat, list) else next(v for v in _cat.values() if isinstance(v, list))
byguid = {str(r["guid"]).lower(): r["path"] for r in _rows}
held = {}      # lower route -> file path
proper = {}    # lower route -> route with original case
for _k, (_p, _r) in settings.held_routes().items():
    held[_k] = _p; proper[_k] = _r
_cache = {}


def load(route):
    k = route.lower()
    if k not in _cache:
        a = dec.Ebx(pathlib.Path(held[k]), types).decode()
        _cache[k] = (a["objects"], {(o.get("$guid") or "").lower(): o for o in a["objects"]})
    return _cache[k]


def imp(x):
    if isinstance(x, dict) and "$import" in x:
        i = x["$import"]
        return byguid.get(i["fileGuid"].lower()), i["classGuid"].lower()
    return None


def deref(x, objs):
    if isinstance(x, dict) and "$ref" in x:
        return None, objs[x["$ref"]]
    i = imp(x)
    if i and i[0] and i[0].lower() in held:
        return i[0], load(i[0])[1].get(i[1])
    return (i[0] if i else None), None


def unbox(v):
    if isinstance(v, dict) and "$boxedValue" in v:
        bv = v["$boxedValue"]
        return bv.get("value", bv) if isinstance(bv, dict) else bv
    return v


_reg = None


def registry():
    """GRX_Weapons rows: name -> list of row objects (a name can repeat)."""
    global _reg
    if _reg is None:
        _reg = {}
        for o in load("Common/GameSetup/Tweakables/GameRemixer/GRX_Weapons")[0]:
            n = o.get("Field_0c59fa06")
            if isinstance(n, str):
                _reg.setdefault(n, []).append(o)
    return _reg


def reg_value(name):
    rows = registry().get(name)
    if not rows:
        return None
    vals = [unbox(r.get("Field_42c8b257")) for r in rows]
    if any(json.dumps(v, sort_keys=True) != json.dumps(vals[0], sort_keys=True) for v in vals[1:]):
        raise ValueError("registry rows disagree: " + name)
    return vals[0]
