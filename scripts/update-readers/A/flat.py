"""python flat.py <route> <object index> [path filter substr] -> flattened leaves path = value (named where known)."""
import sys, json
import lib
objs, _, a = lib.load(sys.argv[1])
idx = int(sys.argv[2]); flt = sys.argv[3].lower() if len(sys.argv) > 3 else ""


def nm(k):
    return (k[6:] + ":" + lib.NAMES[k[6:]]) if k.startswith("Field_") and k[6:] in lib.NAMES else (k[6:] if k.startswith("Field_") else k)


def walk(x, p):
    if isinstance(x, dict):
        if "$import" in x:
            r = lib.imp(x); out(p, "IMPORT " + str(r[0]) + " #" + r[1][:8]); return
        if "$ref" in x:
            out(p, "REF %d %s" % (x["$ref"], objs[x["$ref"]]["$class"])); return
        for k, v in x.items():
            walk(v, p + "/" + nm(k))
    elif isinstance(x, list):
        if x and all(not isinstance(v, (dict, list)) for v in x):
            out(p, [lib.f32(v) for v in x]); return
        if not x:
            out(p, []); return
        for i, v in enumerate(x):
            walk(v, p + "[%d]" % i)
    else:
        out(p, lib.f32(x))


def out(p, v):
    if flt in p.lower():
        print(p, "=", v)


walk(objs[idx], "")
