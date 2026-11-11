#!/usr/bin/env python3
"""Census of the stored visual recoil values under Common/Hardware/Weapons.

  python scripts/frosty-visual-recoil-census.py --raw <capture>/collection/raw [--raw <capture>/collection-fresh-cache/raw] --descriptors <SharedTypeDescriptors.ebx> --out <json> [--compare <earlier json>]

The site models neither kind; this exists so an update shows when they change.

Records, per route and object:
  kickAnimation  every Class_bfd4f199 and Class_daaa7328 object (procedural firing animation
                 modifiers: the Aftermarket Buffer, mounted and bipod modifiers, optics, canted
                 sights and in-body copies). Field_149939ab and Field_e9129d03 are the push and
                 kick scales; the other fields are unnamed channels (2.1.2.0 checklist T1).
  cameraRecoil   weapons: the three camera recoil fields of each GS Class_539cff9b object
                 (Field_36c2f877 CameraRecoilAmount, Field_9532eb28 CameraRecoilWhenZoomedAmount,
                 Field_7f1bb9d4 IdleCameraRecoilWhenZoomedAmount; WEAPONS.md "Camera recoil ladder").
                 optics: every object of each GCR_* file.

Not covered: the base firing animation each weapon starts from (not identified).
--compare prints objects added or removed and fields changed against an earlier output and
exits 1 when there is any difference. Output has no dates; --out must not exist.
A later --raw folder replaces a route an earlier one holds (give reports/mp-copies-*/raw last).
This reads stored values only; it makes no claim about what the game does with them.
"""
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SCOPE = "Common/Hardware/Weapons"
KICK = {"Class_bfd4f199", "Class_daaa7328"}
GS_CLASS = "Class_539cff9b"
GS_FIELDS = ("Field_36c2f877", "Field_9532eb28", "Field_7f1bb9d4")
BATCH = 250


def routes(raws):
    found = {}
    for raw in raws:
        base = raw / SCOPE
        if not base.is_dir():
            sys.exit(f"missing: {base}")
        for path in base.rglob("*.ebx"):
            route = path.relative_to(raw).as_posix()[:-4]
            if "materialgrid" in route.lower():
                continue
            found[route] = path
    return found


def decode(paths, descriptors, tmp, number):
    listing = Path(tmp) / f"list{number}.txt"
    listing.write_text("\n".join(str(p) for p in paths) + "\n", encoding="utf-8")
    out = Path(tmp) / f"decoded{number}.json"
    subprocess.run(
        [sys.executable, str(Path(__file__).with_name("frosty-ebx-decode.py")),
         "--descriptors", str(descriptors), "--ebx-list", str(listing),
         "--out", str(out), "--exact-floats"],
        check=True, stdout=subprocess.DEVNULL)
    decoded = json.loads(out.read_text(encoding="utf-8"))
    out.unlink()
    if decoded["failures"]:
        sys.exit("decode failures: " + json.dumps(decoded["failures"])[:2000])
    return {Path(a["file"]): a for a in decoded["assets"].values()}


def values(obj, only=None):
    return {k: v for k, v in obj.items()
            if not k.startswith("$") and (only is None or k in only)}


def key(obj, index):
    """Object GUID, or #<index> for the in-file objects that have none (weapon-body copies)."""
    return obj.get("$guid") or f"#{index}"


def census(found, descriptors):
    items = sorted(found.items())
    batches = [items[i:i + BATCH] for i in range(0, len(items), BATCH)]
    kick, weapons, optics = {}, {}, {}
    with tempfile.TemporaryDirectory() as tmp:
        def job(number):
            batch = batches[number]
            assets = decode([p for _, p in batch], descriptors, tmp, number)
            return [(route, assets[path]) for route, path in batch]
        with ThreadPoolExecutor(4) as pool:
            for result in pool.map(job, range(len(batches))):
                for route, asset in result:
                    objects = asset["objects"]
                    hits = {key(o, i): {"class": o["$class"], **values(o)}
                            for i, o in enumerate(objects) if o.get("$class") in KICK}
                    if hits:
                        kick[route] = hits
                    name = route.rsplit("/", 1)[-1]
                    if name.startswith("GCR_"):
                        optics[route] = {key(o, i): {"class": o.get("$class"), **values(o)}
                                         for i, o in enumerate(objects)}
                    gs = {key(o, i): values(o, GS_FIELDS)
                          for i, o in enumerate(objects) if o.get("$class") == GS_CLASS}
                    if gs:
                        weapons[route] = gs
    return {"kickAnimation": kick, "cameraRecoil": {"weapons": weapons, "optics": optics}}


def flatten(node, prefix=""):
    if isinstance(node, dict):
        for key in node:
            yield from flatten(node[key], f"{prefix}/{key}" if prefix else key)
    else:
        yield prefix, json.dumps(node, sort_keys=True)


def objects_of(data):
    """(section, route, object key) -> {field path: value}."""
    out = {}
    for section, routes_ in (("kickAnimation", data["kickAnimation"]),
                             ("cameraRecoil/weapons", data["cameraRecoil"]["weapons"]),
                             ("cameraRecoil/optics", data["cameraRecoil"]["optics"])):
        for route, objs in routes_.items():
            for name, fields in objs.items():
                out[(section, route, name)] = dict(flatten(fields))
    return out


def compare(new, old):
    """Whole objects added or removed are one line each; changed fields are one line each.
    An object keyed #<index> shows as removed and added when its file's object order changes."""
    a, b = objects_of(old), objects_of(new)
    lines = [f"removed object {'/'.join(k)} ({len(a[k])} fields)" for k in sorted(a.keys() - b.keys())]
    lines += [f"added object {'/'.join(k)} ({len(b[k])} fields)" for k in sorted(b.keys() - a.keys())]
    for k in sorted(a.keys() & b.keys()):
        for field in sorted(a[k].keys() | b[k].keys()):
            before, after = a[k].get(field, "<absent>"), b[k].get(field, "<absent>")
            if before != after:
                lines.append(f"changed {'/'.join(k)}/{field}: {before} -> {after}")
    return lines


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", action="append", required=True, type=Path)
    ap.add_argument("--descriptors", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--compare", type=Path)
    args = ap.parse_args()
    if args.out.exists():
        sys.exit(f"refusing to overwrite {args.out}")
    found = routes(args.raw)
    data = census(found, args.descriptors)
    doc = {"schemaVersion": 1,
           "source": {"scope": SCOPE, "filesRead": len(found),
                      "descriptorsSha256": hashlib.sha256(args.descriptors.read_bytes()).hexdigest()},
           **data}
    args.out.write_text(json.dumps(doc, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    cam = data["cameraRecoil"]
    print(f"{len(found)} files read; kick animation {len(data['kickAnimation'])} routes, "
          f"{sum(len(v) for v in data['kickAnimation'].values())} objects; camera recoil "
          f"{len(cam['weapons'])} weapon routes, {len(cam['optics'])} GCR files -> {args.out}")
    if args.compare:
        earlier = json.loads(args.compare.read_text(encoding="utf-8"))
        lines = compare(data, earlier)
        for line in lines:
            print(line)
        if lines:
            sys.exit(1)
        print("no differences")


if __name__ == "__main__":
    main()
