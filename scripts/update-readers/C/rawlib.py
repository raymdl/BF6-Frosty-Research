"""Shared raw-EBX loader for stage 9 part C (attachments). Read-only on every input."""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import importlib.util, pathlib, json, collections, functools
D = settings.D
RUN = settings.RUN
REPO = settings.REPO
SITE = settings.SITE
spec = importlib.util.spec_from_file_location("dec", REPO / "scripts/frosty-ebx-decode.py")
dec = importlib.util.module_from_spec(spec); spec.loader.exec_module(dec)
types = dec.type_descriptors(settings.DESCRIPTORS)
_cat = json.load(open(settings.CATALOG, encoding="utf-8"))
_rows = _cat if isinstance(_cat, list) else next(v for v in _cat.values() if isinstance(v, list))
byguid = {str(r["guid"]).lower(): r["path"] for r in _rows}
held = {}      # lower route -> file path
route_case = {}  # lower route -> route as stored
for _k, (_p, _r) in settings.held_routes().items():
    held[_k] = _p; route_case[_k] = _r
_cache = {}


def load(route):
    k = route.lower()
    if k not in _cache:
        a = dec.Ebx(pathlib.Path(held[k]), types).decode()
        _cache[k] = (a["objects"], {(o.get("$guid") or "").lower(): o for o in a["objects"]})
    return _cache[k]


def imp(x):
    """(route, classGuid) of an import, or None."""
    if isinstance(x, dict) and "$import" in x:
        i = x["$import"]
        return byguid.get(i["fileGuid"].lower()), i["classGuid"].lower()
    return None


def deref(x, objs):
    """(route or None, object or None) behind a $ref or $import."""
    if isinstance(x, dict) and "$ref" in x:
        return None, objs[x["$ref"]]
    i = imp(x)
    if i and i[0] and i[0].lower() in held:
        return i[0], load(i[0])[1].get(i[1])
    return (i[0] if i else None), None


_S = None
def strings():
    global _S
    if _S is None:
        _S = {}
        for l in open(settings.STRINGS, encoding="utf-8"):
            if "\t" in l:
                k, v = l.rstrip("\n").split("\t", 1); _S[k.upper()] = v
    return _S


def sid(i):
    return "%08X" % (i & 0xFFFFFFFF) if isinstance(i, int) else None


def unbox(v):
    while isinstance(v, dict) and "$boxedValue" in v:
        v = v["$boxedValue"]
    return v


_REG = None
def registry():
    """name -> live value from GRX_Weapons."""
    global _REG
    if _REG is None:
        _REG = {}
        for o in load("common/gamesetup/tweakables/gameremixer/grx_weapons")[0]:
            n = o.get("Field_0c59fa06")
            if isinstance(n, str) and "Field_42c8b257" in o:
                _REG[n] = unbox(o["Field_42c8b257"])
    return _REG


def identities():
    j = json.load(open(REPO / "reference-data/provenance/frosty-weapon-identities.json", encoding="utf-8"))["weapons"]
    return j
