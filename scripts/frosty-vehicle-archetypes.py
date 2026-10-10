#!/usr/bin/env python3
"""Vehicle stat ids with their archetype and hardware-tree parents (L3306).

  python scripts/frosty-vehicle-archetypes.py --capture-dir <capture folder> --descriptors <SharedTypeDescriptors.ebx> --out <json> [--compare <earlier json>]

Reads four raw assets under <capture folder>/raw/Persistence/StatCategories:
StatCategorization/Categorization_Vehicles and StatCategoryTrees/Category_VehicleArchetypes,
Category_Hardware and Category_HardwareGroups. Each Categorization_Vehicles entry imports
nodes of those trees; this writes one row per entry with the node names and their parents.

`id` is the hardware-tree leaf name (the id GameTools reports); `statName` is the entry's
own name, which differs for the two dirt bikes. `archetype` and `domain` are null when the
entry imports no archetype node or has no veh_sur / veh_air / veh_nav / stationary parent.
--compare prints ids added, removed or changed against an earlier output and exits 1 when
there is any difference. Output has no dates; --out must not exist.
This reads serialized links only; it makes no claim about runtime use.
"""
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = "Persistence/StatCategories/"
ROUTES = {
    "vehicles": BASE + "StatCategorization/Categorization_Vehicles",
    "archetypes": BASE + "StatCategoryTrees/Category_VehicleArchetypes",
    "hardware": BASE + "StatCategoryTrees/Category_Hardware",
    "groups": BASE + "StatCategoryTrees/Category_HardwareGroups",
}
NAME = "Field_97a3169c"
CHILDREN = "Field_8a7dfc78"
DOMAINS = ("veh_sur", "veh_air", "veh_nav", "stationary")


def decode(capture_dir, descriptors):
    raw = capture_dir / "raw"
    files = [raw / (route + ".ebx") for route in ROUTES.values()]
    missing = [str(f) for f in files if not f.is_file()]
    if missing:
        sys.exit("missing raw asset(s): " + ", ".join(missing))
    with tempfile.TemporaryDirectory() as tmp:
        listing = Path(tmp) / "list.txt"
        listing.write_text("\n".join(str(f) for f in files) + "\n", encoding="ascii")
        out = Path(tmp) / "decoded.json"
        subprocess.run(
            [sys.executable, str(Path(__file__).with_name("frosty-ebx-decode.py")),
             "--descriptors", str(descriptors), "--ebx-list", str(listing),
             "--root", str(raw), "--out", str(out)],
            check=True, stdout=subprocess.DEVNULL)
        decoded = json.loads(out.read_text(encoding="utf-8"))
    if decoded["failures"]:
        sys.exit("decode failures: " + json.dumps(decoded["failures"]))
    return decoded, files


def tree(asset):
    """guid -> list of node names from the node up to (not including) the unnamed root."""
    objects = asset["objects"]
    parent = {}
    for index, obj in enumerate(objects):
        for child in obj.get(CHILDREN) or []:
            if "$ref" in child:
                parent[child["$ref"]] = index
    chains = {}
    for index, obj in enumerate(objects):
        if NAME not in obj:
            continue
        chain, at = [], index
        while at is not None and NAME in objects[at]:
            chain.append(objects[at][NAME])
            at = parent.get(at)
        chains[obj["$guid"]] = chain
    return chains


def build(decoded):
    assets = decoded["assets"]
    trees = {key: tree(assets[ROUTES[key]]) for key in ("archetypes", "hardware", "groups")}
    by_file = {assets[ROUTES[key]]["fileGuid"]: key for key in trees}
    rows = []
    for entry in assets[ROUTES["vehicles"]]["objects"]:
        if NAME not in entry:
            continue
        found = {"archetypes": [], "hardware": [], "groups": []}
        for pointer in entry.get(CHILDREN) or []:
            target = pointer.get("$import")
            key = by_file.get(target["fileGuid"]) if target else None
            if key:
                found[key].append(trees[key][target["classGuid"]])
        if len(found["hardware"]) != 1 or len(found["archetypes"]) > 1:
            sys.exit(f"{entry[NAME]}: expected one hardware node and at most one archetype node")
        hardware = found["hardware"][0]
        archetype = found["archetypes"][0] if found["archetypes"] else None
        rows.append({
            "id": hardware[0],
            "statName": entry[NAME],
            "archetype": archetype[0] if archetype else None,
            "archetypeParents": archetype[1:] if archetype else [],
            "domain": next((name for name in hardware[1:] if name in DOMAINS), None),
            "hardwareParents": hardware[1:],
            "groups": sorted(chain[0] for chain in found["groups"]),
        })
    rows.sort(key=lambda row: row["id"].upper())
    archetypes = sorted(
        ({"id": chain[0], "parent": chain[1] if len(chain) > 1 else None}
         for chain in trees["archetypes"].values()), key=lambda node: node["id"])
    return rows, archetypes


def compare(new, old_path):
    old = json.loads(Path(old_path).read_text(encoding="utf-8"))
    before = {row["id"]: row for row in old["vehicles"]}
    after = {row["id"]: row for row in new["vehicles"]}
    lines = [f"added {i}: archetype {after[i]['archetype']}, domain {after[i]['domain']}"
             for i in sorted(set(after) - set(before))]
    lines += [f"removed {i}" for i in sorted(set(before) - set(after))]
    lines += [f"changed {i}: {json.dumps(before[i])} -> {json.dumps(after[i])}"
              for i in sorted(set(before) & set(after)) if before[i] != after[i]]
    if old["archetypes"] != new["archetypes"]:
        lines.append("archetype tree changed")
    print("\n".join(lines) if lines else f"no vehicle or archetype changes against {old_path}")
    return bool(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--capture-dir", required=True, type=Path)
    parser.add_argument("--descriptors", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    if args.out.exists():
        sys.exit(f"{args.out} exists")
    decoded, files = decode(args.capture_dir, args.descriptors)
    rows, archetypes = build(decoded)
    identity = args.capture_dir / "capture-identity.json"
    result = {
        "schemaVersion": 1,
        "lead": "L3306",
        "source": {
            "gameHead": json.loads(identity.read_text(encoding="utf-8-sig")).get("gameHead") if identity.is_file() else None,
            "descriptorsSha256": decoded["descriptorsSha256"],
            "assets": {route: hashlib.sha256(f.read_bytes()).hexdigest() for route, f in zip(ROUTES.values(), files)},
        },
        "archetypes": archetypes,
        "vehicles": rows,
    }
    args.out.write_text(json.dumps(result, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(rows)} vehicles, {sum(1 for row in rows if row['archetype'])} with an archetype -> {args.out}")
    if args.compare and compare(result, args.compare):
        sys.exit(1)


if __name__ == "__main__":
    main()
