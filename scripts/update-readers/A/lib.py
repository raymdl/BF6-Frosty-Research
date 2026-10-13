"""Shared loader for stage 9 part A: raw EBX by route, import resolution, registry rows, strings."""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import importlib.util, pathlib, json, struct, re
HERE = settings.part("A")
RUN = settings.RUN
REPO = settings.REPO
SITE = settings.SITE
D = settings.D
B = settings.BUILD
spec = importlib.util.spec_from_file_location("dec", REPO / "scripts/frosty-ebx-decode.py")
dec = importlib.util.module_from_spec(spec); spec.loader.exec_module(dec)
types = dec.type_descriptors(B / "capture/toolchain/SharedTypeDescriptors.ebx")
_cat = json.load(open(B / "capture/collection/asset-catalog.json", encoding="utf-8"))
_rows = _cat if isinstance(_cat, list) else next(v for v in _cat.values() if isinstance(v, list))
byguid = {str(r["guid"]).lower(): r["path"] for r in _rows}
held = {}
for _k, (_p, _r) in settings.held_routes().items():
    held[_k] = _p
_cache = {}
NAMES = {}
for l in open(settings.regnames(), encoding="utf-8").read().splitlines()[1:]:
    c = l.split("\t"); NAMES[c[0]] = c[1]


def load(route):
    k = route.lower()
    if k not in _cache:
        a = dec.Ebx(pathlib.Path(held[k]), types).decode()
        _cache[k] = (a["objects"], {(o.get("$guid") or "").lower(): o for o in a["objects"]}, a)
    return _cache[k]


def imp(x):
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


def unbox(v):
    if isinstance(v, dict) and "$boxedValue" in v:
        bv = v["$boxedValue"]
        return bv.get("value", bv) if isinstance(bv, dict) else bv
    return v


_reg = None


def registry():
    """name -> list of (value, min, max) from GRX_Weapons."""
    global _reg
    if _reg is None:
        _reg = {}
        objs = load("common/gamesetup/tweakables/gameremixer/grx_weapons")[0]
        for o in objs:
            n = o.get("Field_0c59fa06")
            if isinstance(n, str):
                _reg.setdefault(n, []).append(tuple(unbox(o.get(f)) for f in ("Field_42c8b257", "Field_c06d0cbb", "Field_3ff76ddb")))
    return _reg


def reg(name):
    r = registry().get(name)
    return r[0][0] if r else None


_str = None


def string(sid):
    global _str
    if _str is None:
        _str = {}
        for l in open(B / "capture/fs_us_loc.strings.tsv", encoding="utf-8"):
            p = l.rstrip("\n").split("\t", 1)
            if len(p) == 2:
                _str[p[0].lower()] = p[1]
    if isinstance(sid, int):
        sid = "%08x" % (sid & 0xffffffff)
    return _str.get(str(sid).lower())


def f32(x):
    """Shortest decimal that round-trips the float32 nearest to x."""
    if isinstance(x, bool) or not isinstance(x, float):
        return x
    f = struct.unpack("<f", struct.pack("<f", x))[0]
    for n in range(1, 10):
        s = float("%.*g" % (n, f))
        if struct.unpack("<f", struct.pack("<f", s))[0] == f:
            return int(s) if s == int(s) and abs(s) < 1e15 else s
    return f


def named(o):
    """Recursively rename Field_<hash> keys with known registry names (for reading dumps)."""
    if isinstance(o, dict):
        return {(k + ":" + NAMES[k[6:]] if k.startswith("Field_") and k[6:] in NAMES else k): named(v) for k, v in o.items()}
    if isinstance(o, list):
        return [named(v) for v in o]
    return f32(o) if isinstance(o, float) else o
