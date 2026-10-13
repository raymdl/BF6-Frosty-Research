"""Find magazine/part packages that replace ReloadInfoArray (the source of data/reload-exceptions.json animationOverrides).

For a weapon: every object in the WB, and in every WPM part file the WB part list imports, that holds reload-info
entries (Field_fc66e75e ReloadTimeBulletsLeft) other than the base firing object. Reports time, speed and time/speed
in ms, the owning part file and the part's selector GUIDs (Field_819acc98).
Controls: M240L (7100 ms), M60E6 (4534), PP19 (2667), RPK74M (2950), MG5 (5.6/1.009009).
"""
import sys, json
import lib, extract
from lib import f32
F = lambda h: "Field_" + h


def reload_entries(o, path=""):
    """Yield (path, entry dict) for every struct holding Field_fc66e75e inside object o."""
    if isinstance(o, dict):
        if F("fc66e75e") in o:
            yield path, o
        for k, v in o.items():
            if k.startswith("$"):
                continue
            yield from reload_entries(v, path + "/" + k[6:])
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from reload_entries(v, path + "[%d]" % i)


def part_files(wobjs):
    out = set()
    def walk(x):
        if isinstance(x, dict):
            if "$import" in x:
                i = lib.imp(x)
                if i and i[0] and "/wpm_" in i[0].lower() or (i and i[0] and "/_weaponmodifiers/" in i[0].lower()):
                    out.add(i[0])
                return
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(wobjs)
    return sorted(out)


def scan(internal):
    wbr, _ = extract.routes(internal)
    wobjs = lib.load(wbr)[0]
    res = []
    files = [(wbr, wobjs)]
    missing = []
    for r in part_files(wobjs):
        if r.lower() in lib.held:
            files.append((r, lib.load(r)[0]))
        else:
            missing.append(r)
    for route, objs in files:
        sels = []
        for o in objs:
            if o["$class"] == "Class_897c99a7":
                sels += [s for s in (o.get(F("819acc98")) or []) if isinstance(s, str)]
        for i, o in enumerate(objs):
            if route == wbr and o["$class"] == "Class_35259f6b":
                continue
            for p, e in reload_entries(o):
                t, s = e.get(F("fc66e75e")), e.get(F("1c533b56"))
                if not isinstance(t, (int, float)):
                    continue
                res.append({"file": route.rsplit("/", 1)[-1], "object": i, "class": o["$class"], "path": p, "timeBulletsLeft": f32(t), "reloadTime": f32(e.get(F("85ff24a0"))),
                            "speed": f32(s), "ms": round(1000 * t / s) if s else None, "maxAmmo": e.get(F("c59cc6a8")), "minAmmo": e.get(F("82265a82")),
                            "partSelectors": len(sels) if route != wbr else None})
    return res, len(files), missing


if __name__ == "__main__":
    for internal in sys.argv[1:] or ["M240L", "M60E6", "PP19", "RPK74M", "MG5", "MRGGA", "CDX40", "PKM", "RSAR999"]:
        res, n, missing = scan(internal)
        print("==", internal, "| files scanned:", n, "| part files not held:", len(missing), missing[:4])
        for r in res:
            print("  ", json.dumps(r))
