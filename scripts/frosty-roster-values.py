#!/usr/bin/env python3
"""Stat-category roster of vehicles, gadgets and vehicle equipment with their stored values.

  python scripts/frosty-roster-values.py --build-dir <BF6 Datamining/builds/X> --descriptors <SharedTypeDescriptors.ebx> --out-dir <new folder> [--name-joins <json>] [--names <json>]

Reads every saved raw file under <build-dir> (any .../raw/<route>.ebx; the newest copy of a
route wins). For each entry of Categorization_Vehicles, Categorization_Gadgets and
Categorization_Vehicles_Equipment it writes:
  category  hardware-tree chain, group tags, effect tags, archetype, misc tags (import pointers)
  defined   objects whose instance GUID is one of the entry's listed GUIDs
  usedBy    other files that contain one of those GUIDs; `carriers` are the ones that name
            no other roster entry, `mountObjects` the objects of the others that import it
  own       explosion and projectile values in objects reached from `defined`, from every
            object of a carrier and from the mount objects, through local and import
            pointers, each with file, byte offset and type
  registry  named GRX_Gadgets_Glacier / GRX_Vehicles rows whose owner name equals the base
            name of a reached file (joinRule "ownerName"), plus rows listed for the entry
            in --name-joins (joinRule "nameTable", a match on names alone)
  carrierUnnamed  other plain numbers in carrier files, by field hash
A vehicle also gets `equipment` (entries its blueprint mounts) and `customization` (entries
within two imports of each VehicleCustomizationContext_* file that imports its blueprint).
Writes roster.json, roster-compact.json (with display names from --names), file-imports.json,
raw-check-manifest.json (for frosty-raw-check.py --manifest) and summary.json into --out-dir,
which must not exist. Values are stored source values; nothing here says which value a match
uses.
"""
import argparse
import collections
import hashlib
import importlib.util
import json
import re
import sys
import uuid
from pathlib import Path

CAT = "Persistence/StatCategories/StatCategorization/"
TREES = "Persistence/StatCategories/StatCategoryTrees/"
ROSTERS = {"vehicle": CAT + "Categorization_Vehicles", "gadget": CAT + "Categorization_Gadgets",
           "vehicleEquipment": CAT + "Categorization_Vehicles_Equipment"}
REGISTRIES = ("Common/Hardware/Gadgets/GRX_Gadgets_Glacier", "Common/GameSetup/Tweakables/GameRemixer/GRX_Vehicles")
DECODE = re.compile(r"^(Common/Hardware/(Gadgets|Vehicles)/|Common/Gameplay/(Loadouts/Vehicles|Abilities)/|"
                    r"Persistence/StatCategories/|Common/GameSetup/Tweakables/GameRemixer/GRX_Vehicles$)", re.I)
NAME, CHILDREN, GUIDS, INDEX = "Field_97a3169c", "Field_8a7dfc78", "Field_1e6bcd75", "Field_2b6f2936"
ROWNAME, ROWVALS = "Field_0c59fa06", ("Field_42c8b257", "Field_c06d0cbb", "Field_3ff76ddb")
EXPLOSION = "Class_9966532d"
FIELDS = {"Field_19861d8c": "BlastDamage", "Field_33f3a8ab": "BlastRadius", "Field_95e340fe": "InnerBlastRadius",
          "Field_3ef01f58": "ShockwaveDamage", "Field_524836d3": "ShockwaveRadius", "Field_91bb7b5f": "Damage",
          "Field_94869d67": "StartDamage", "Field_bc7acc94": "EndDamage", "Field_e5b11905": "DamageFalloffStartDistance",
          "Field_68be3481": "DamageFalloffEndDistance", "Field_0bf4f62b": "InitialSpeed", "Field_5ef7b9a1": "TimeToLive",
          "Field_30c37c24": "Drag"}
MAX_DEPTH = 8
MAX_UNNAMED = 80


def load_decoder():
    spec = importlib.util.spec_from_file_location("ebxdecode", Path(__file__).with_name("frosty-ebx-decode.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    RAW_TYPES = {mod.BOOLEAN: "bool", mod.INT8: "i8", mod.UINT8: "u8", mod.INT16: "i16", mod.UINT16: "u16",
                 mod.INT32: "i32", mod.UINT32: "u32", mod.INT64: "i64", mod.UINT64: "u64",
                 mod.FLOAT32: "f32", mod.FLOAT64: "f64"}

    class EbxAt(mod.Ebx):
        """Adds $at (object start) and $fo (field name -> absolute file offset) to every class body."""
        def _read_class(self, class_type, start_offset):
            out = super()._read_class(class_type, start_offset)
            offsets, kinds = out.setdefault("$fo", {}), out.setdefault("$ft", {})
            for field in class_type["fields"]:
                kind = mod.debug_type(field["flags"])
                if kind != mod.INHERITED:
                    offsets[f"Field_{field['hash']}"] = start_offset + field["offset"]
                if kind in RAW_TYPES:
                    kinds[f"Field_{field['hash']}"] = RAW_TYPES[kind]
            out["$at"] = start_offset
            return out
    return mod, EbxAt


def raw_files(build_dir):
    newest = {}
    for path in build_dir.rglob("*.ebx"):
        parts = path.parts
        if "raw" not in parts or "materialgrid" in str(path).lower():
            continue
        at = len(parts) - 1 - parts[::-1].index("raw")
        route = "/".join(parts[at + 1:])[:-4]
        key = route.lower()
        if key not in newest or path.stat().st_mtime > newest[key][1].stat().st_mtime:
            newest[key] = (route, path)
    return newest


def scalar_type(value):
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, float):
        return "f32"
    return "i32" if -2**31 <= value < 2**31 else "u32"


def summarize(obj):
    """Imports, local refs and named scalar fields (with offsets) in one object subtree."""
    imports, refs, values, others = [], [], [], []

    def walk(node):
        if isinstance(node, dict):
            if "$import" in node:
                imports.append((node["$import"]["fileGuid"], node["$import"]["classGuid"]))
                return
            if "$ref" in node and len(node) == 1:
                refs.append(node["$ref"])
                return
            offsets, kinds = node.get("$fo", {}), node.get("$ft", {})
            for key, value in node.items():
                if key in FIELDS and isinstance(value, (int, float)) and key in kinds:
                    values.append({"field": key, "name": FIELDS[key], "value": value,
                                   "offset": offsets[key], "type": kinds[key]})
                elif (key in kinds and kinds[key] != "bool" and isinstance(value, (int, float)) and value
                      and (isinstance(value, float) or abs(value) < 100000)):
                    others.append({"field": key, "value": value, "offset": offsets[key], "type": kinds[key]})
                elif isinstance(value, (dict, list)) and key not in ("$fo", "$ft"):
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)
    walk(obj)
    return imports, refs, values, others


def tree_chains(objects):
    parent = {}
    for index, obj in enumerate(objects):
        for child in obj.get(CHILDREN) or []:
            if isinstance(child, dict) and "$ref" in child:
                parent[child["$ref"]] = index
    chains = {}
    for index, obj in enumerate(objects):
        if isinstance(obj.get(NAME), str):
            chain, at = [], index
            while at is not None and isinstance(objects[at].get(NAME), str):
                chain.append(objects[at][NAME])
                at = parent.get(at)
            chains[obj["$guid"]] = chain
    return chains


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--build-dir", required=True, type=Path)
    parser.add_argument("--descriptors", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--names", type=Path, help="JSON of display names keyed by stat id (or statId@leaf) per kind")
    parser.add_argument("--name-joins", type=Path,
                        help="JSON {statId: [registry owner name, ...]}: joins made by name alone, marked joinRule nameTable")
    args = parser.parse_args()
    if args.out_dir.exists():
        sys.exit(f"{args.out_dir} exists")
    mod, EbxAt = load_decoder()
    types = mod.type_descriptors(args.descriptors)
    files = raw_files(args.build_dir)

    # Decode the gadget, vehicle, category and registry files into per-object summaries.
    objects = {}        # (route, index) -> summary
    by_guid = {}        # instance guid -> (route, index)
    file_route = {}     # file guid -> route
    used = {}           # route -> {"path", "sha256"}
    trees, rosters, registry, failures = {}, {}, collections.defaultdict(list), []
    for key, (route, path) in sorted(files.items()):
        if not DECODE.match(route) and route not in REGISTRIES:
            continue
        try:
            decoded = EbxAt(path, types).decode()
        except Exception as error:
            failures.append({"route": route, "error": f"{type(error).__name__}: {error}"})
            continue
        used[route] = {"path": str(path), "sha256": decoded["sha256"]}
        file_route[decoded["fileGuid"]] = route
        if route.startswith(TREES):
            trees[decoded["fileGuid"]] = (route.rsplit("Category_", 1)[-1], tree_chains(decoded["objects"]))
        if route in ROSTERS.values():
            rosters[route] = decoded["objects"]
        for index, obj in enumerate(decoded["objects"]):
            if "$unknownType" in obj:
                continue
            if route in REGISTRIES:
                name = obj.get(ROWNAME)
                value = obj.get(ROWVALS[0])
                boxed = isinstance(value, dict) and "value" in value
                if boxed:
                    value = value["value"]
                if index and isinstance(name, str) and isinstance(value, (int, float)):
                    offsets = {} if boxed else obj.get("$fo", {})
                    registry[name.split(".")[0]].append({
                        "file": route, "name": name, "default": value, "boxed": boxed,
                        "min": obj.get(ROWVALS[1]), "max": obj.get(ROWVALS[2]),
                        "offset": offsets.get(ROWVALS[0]), "type": scalar_type(value)})
                continue
            imports, refs, values, others = summarize(obj)
            objects[(route, index)] = {"class": obj.get("$class"), "guid": obj.get("$guid"), "at": obj.get("$at"),
                                       "imports": imports, "refs": refs, "values": values, "others": others}
            if obj.get("$guid"):
                by_guid[obj["$guid"]] = (route, index)

    # Byte scan every saved file for the roster GUIDs.
    entries = []
    for kind, route in ROSTERS.items():
        for obj in rosters.get(route, []):
            if isinstance(obj.get(NAME), str):
                entries.append((kind, route, obj))
    wanted = {uuid.UUID(g).bytes_le: g for _, _, obj in entries for g in obj.get(GUIDS) or []}
    pattern = re.compile(b"|".join(re.escape(raw) for raw in wanted))
    hits = collections.defaultdict(set)
    for key, (route, path) in files.items():
        if route.startswith(CAT):
            continue
        for match in pattern.finditer(path.read_bytes()):
            hits[wanted[match.group(0)]].add(route)

    owners_of = collections.defaultdict(set)    # route -> stat names whose GUIDs the file contains
    for _, _, obj in entries:
        for g in obj.get(GUIDS) or []:
            for route in hits.get(g, ()):
                owners_of[route].add(obj[NAME])

    name_joins = json.loads(args.name_joins.read_text(encoding="utf-8")) if args.name_joins else {}
    items, manifest, skipped_owners = [], [], []

    def check(route, offset, kind, expect):
        if offset is not None:
            manifest.append({"path": used[route]["path"], "offset": offset, "type": kind, "expect": expect})

    for kind, roster_route, entry in entries:
        category = collections.defaultdict(list)
        unresolved_imports = 0
        for pointer in entry.get(CHILDREN) or []:
            target = pointer.get("$import") if isinstance(pointer, dict) else None
            tree = trees.get(target["fileGuid"]) if target else None
            if tree and target["classGuid"] in tree[1]:
                category[tree[0]].append(tree[1][target["classGuid"]])
            else:
                unresolved_imports += 1
        guids = entry.get(GUIDS) or []
        defined = sorted({by_guid[g] for g in guids if g in by_guid})
        defined_routes = {route for route, _ in defined}
        used_by = sorted({route for g in guids for route in hits.get(g, ())} - defined_routes)
        # Follow local and import pointers from the defining objects, and from every object of a
        # carrier file that holds GUIDs of this roster entry only (an unlock object points nowhere;
        # the files that name it hold the weapon, ability or projectile links).
        carriers = [route for route in used_by if owners_of[route] == {entry[NAME]}]
        seeds = list(defined) + [node for node in objects if node[0] in set(carriers) and node not in defined]
        # In a file shared with other roster entries (a vehicle blueprint), start only from the
        # objects that import one of this entry's GUIDs.
        shared = set(used_by) - set(carriers)
        mounts = [node for node, summary in objects.items() if node[0] in shared
                  and any(class_guid in guids for _, class_guid in summary["imports"])]
        seeds += [node for node in mounts if node not in seeds]
        seen, queue, missing = dict.fromkeys(seeds, 0), collections.deque(seeds), 0
        while queue:
            node = queue.popleft()
            depth = seen[node]
            if depth >= MAX_DEPTH:
                continue
            summary = objects[node]
            targets = [(node[0], ref) for ref in summary["refs"]]
            for file_guid, class_guid in summary["imports"]:
                if class_guid in by_guid:
                    targets.append(by_guid[class_guid])
                elif file_guid not in file_route:
                    missing += 1
            for target in targets:
                if target in objects and target not in seen:
                    seen[target] = depth + 1
                    queue.append(target)
        own = []
        for (route, index), depth in sorted(seen.items()):
            summary = objects[(route, index)]
            for value in summary["values"]:
                own.append(dict(value, route=route, object=index, objectClass=summary["class"], depth=depth,
                                explosion=summary["class"] == EXPLOSION))
                check(route, value["offset"], value["type"], value["value"])
        # Every other plain number in the entry's own carrier files, by field hash (names unknown).
        unnamed = []
        for node in sorted(node for node in seen if node[0] in set(carriers)):
            for value in objects[node]["others"]:
                unnamed.append(dict(value, route=node[0], object=node[1], objectClass=objects[node]["class"]))
        unnamed = unnamed[:MAX_UNNAMED]
        for value in unnamed:
            check(value["route"], value["offset"], value["type"], value["value"])
        reached_routes = sorted({route for route, _ in seen})
        rows = []
        for route in reached_routes:
            base = route.rsplit("/", 1)[-1]
            for row in registry.get(base, []):
                rows.append(dict(row, owner=base, joinRule="ownerName"))
                check(row["file"], row["offset"], row["type"], row["default"])
        have = {row["owner"] for row in rows}
        for owner in name_joins.get(entry[NAME], []):
            # A row name without a dot is its own registry key, so take keys that extend the owner too.
            keys = [key for key in registry if (key == owner or key.startswith(owner + "_")) and key not in have]
            if not any(key == owner or key.startswith(owner + "_") for key in registry):   # no plain numeric row
                skipped_owners.append({"statId": entry[NAME], "owner": owner})
            for key in keys:
                have.add(key)
                for row in registry[key]:
                    rows.append(dict(row, owner=owner, joinRule="nameTable"))
                    check(row["file"], row["offset"], row["type"], row["default"])
        if entry.get("$guid"):
            check(roster_route, entry["$at"] - 16, "guid", entry["$guid"])
        hardware = category.get("Hardware", [[None]])[0]
        items.append({
            "kind": kind, "statId": entry[NAME], "statIndex": entry.get(INDEX), "entryGuid": entry.get("$guid"),
            "hardwareLeaf": hardware[0], "hardwareParents": hardware[1:],
            "groups": sorted(chain[0] for chain in category.get("HardwareGroups", [])),
            "effects": sorted(chain[0] for chain in category.get("Effects", [])),
            "archetype": (category.get("VehicleArchetypes") or [[None]])[0][0],
            "misc": sorted(chain[0] for chain in category.get("Misc", [])),
            "unresolvedCategoryImports": unresolved_imports,
            "guids": guids,
            "defined": [{"route": route, "object": index, "class": objects[(route, index)]["class"]}
                        for route, index in defined],
            "usedBy": used_by, "carriers": carriers,
            "mountObjects": [{"route": route, "object": index, "class": objects[(route, index)]["class"]}
                             for route, index in mounts],
            "reachedFiles": reached_routes, "importsToUnsavedFiles": missing,
            "own": own, "registry": rows, "carrierUnnamed": unnamed,
        })

    # Which roster items a vehicle blueprint uses.
    for vehicle in (item for item in items if item["kind"] == "vehicle"):
        blueprints = {d["route"] for d in vehicle["defined"]}
        vehicle["equipment"] = sorted(item["statId"] for item in items
                                      if item["kind"] == "vehicleEquipment" and blueprints & set(item["usedBy"]))

    args.out_dir.mkdir(parents=True)
    graph = collections.defaultdict(set)
    for (route, _), node in objects.items():
        for file_guid, _ in node["imports"]:
            graph[route].add(file_route.get(file_guid, file_guid))
    (args.out_dir / "file-imports.json").write_text(json.dumps(
        {route: sorted(targets) for route, targets in sorted(graph.items())}, indent=0), encoding="utf-8")
    # Customization contexts: files named VehicleCustomizationContext_* that import a vehicle's
    # blueprint; the roster entries are those with a defining or using file within two imports.
    routes_of = collections.defaultdict(set)
    for item in items:
        for route in [d["route"] for d in item["defined"]] + item["usedBy"]:
            routes_of[route].add(item["statId"])
    for vehicle in (item for item in items if item["kind"] == "vehicle"):
        blueprints = {d["route"] for d in vehicle["defined"]}
        vehicle["customization"] = []
        for route, targets in sorted(graph.items()):
            if route.rsplit("/", 1)[-1].startswith("VehicleCustomizationContext_") and blueprints & targets:
                near = set(targets) | {far for target in targets for far in graph.get(target, ())}
                found = sorted({stat for target in near - blueprints for stat in routes_of.get(target, ())}
                               - {vehicle["statId"]})
                vehicle["customization"].append({"context": route, "items": found})
    source = {"descriptorsSha256": types["sha256"], "filesDecoded": len(used), "decodeFailures": failures,
              "rosterAssets": {route: used[route] for route in ROSTERS.values() if route in used},
              "registryAssets": {route: used[route] for route in REGISTRIES if route in used}}
    files_used = sorted({item_route for item in items for item_route in item["reachedFiles"]})
    (args.out_dir / "roster.json").write_text(json.dumps(
        {"schemaVersion": 1, "source": source, "files": {route: used[route] for route in files_used}, "items": items},
        indent=1) + "\n", encoding="utf-8", newline="\n")
    # Compact form for the repository: one row per distinct value, file names without folders.
    names = json.loads(args.names.read_text(encoding="utf-8")) if args.names else {}
    base = lambda route: route.rsplit("/", 1)[-1]
    compact = []
    for item in items:
        named = names.get(item["kind"], {})
        row = {key: item[key] for key in ("kind", "statId", "statIndex", "entryGuid", "hardwareLeaf", "hardwareParents",
                                          "groups", "effects", "archetype", "misc", "guids")}
        row["display"] = named.get(f"{item['statId']}@{item['hardwareLeaf']}") or named.get(item["statId"])
        row["defined"] = [d["route"] for d in item["defined"]]
        row["carriers"] = item["carriers"]
        row["sharedUsers"] = sorted(set(item["usedBy"]) - set(item["carriers"]))
        row["mountObjects"] = len(item["mountObjects"])
        for key in ("equipment", "customization"):
            if key in item:
                row[key] = item[key]
        row["own"] = sorted({(v["name"], v["value"], base(v["route"]), v["objectClass"] or "", v["explosion"])
                             for v in item["own"]})
        row["registry"] = sorted({(r["owner"], r["name"], r["default"], r["min"], r["max"], r["joinRule"], r["boxed"])
                                  for r in item["registry"]}, key=str)
        row["carrierUnnamed"] = sorted({(v["field"], v["value"], base(v["route"]), v["objectClass"] or "")
                                        for v in item["carrierUnnamed"]}, key=str)
        row["importsToUnsavedFiles"] = item["importsToUnsavedFiles"]
        compact.append(row)
    (args.out_dir / "roster-compact.json").write_text(json.dumps({
        "schemaVersion": 1, "source": source,
        "columns": {"own": ["name", "value", "file", "objectClass", "isExplosionObject"],
                    "registry": ["owner", "rowName", "default", "min", "max", "joinRule", "boxedDefault"],
                    "carrierUnnamed": ["fieldHash", "value", "file", "objectClass"]},
        "items": compact}, separators=(",", ":"), ensure_ascii=False).replace('},{"kind"', '},\n{"kind"') + "\n",
        encoding="utf-8", newline="\n")
    unique = list({(c["path"], c["offset"], c["type"]): c for c in manifest}.values())
    (args.out_dir / "raw-check-manifest.json").write_text(json.dumps(unique, indent=0), encoding="utf-8")
    summary = {"items": collections.Counter(item["kind"] for item in items),
               "withDefinition": collections.Counter(item["kind"] for item in items if item["defined"]),
               "withOwnValues": collections.Counter(item["kind"] for item in items if item["own"]),
               "withRegistryRows": collections.Counter(item["kind"] for item in items if item["registry"]),
               "noDefinition": [item["statId"] for item in items if not item["defined"]],
               "noValues": [item["statId"] for item in items if not item["own"] and not item["registry"] and not item["carrierUnnamed"]],
               "nameJoinOwnersWithoutNumericRows": skipped_owners, "rawChecks": len(unique), "decodeFailures": len(failures), "registryOwners": len(registry)}
    (args.out_dir / "summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
