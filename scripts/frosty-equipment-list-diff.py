"""Diff every weapon's Equipment_* list between two raw collections: which attachment files it offers.

An Equipment_<weapon> file imports the attachment files the weapon offers. An attachment can
be removed from the game by dropping it from this list while its Attachment_* file, ability
binding and kill-switch row all stay: the DRS-IAR Synthetic Tip in 2.1.2.0. The availability
census (update guide Stage 7) reads this list as well as the kill switches.

For each Equipment_* file under Common/Hardware/Weapons in either collection, the offered set is
every Attachment_* file of the same weapon folder (folder case ignored) whose file GUID the list
imports. Each side is decoded with its own descriptors. Writes a TSV (equipment, change,
attachment) with rows "removed", "added", "list added" and "list removed", and prints the
removals.

  python -I scripts/frosty-equipment-list-diff.py <old collection> <new collection>
      --old-descriptors <file> --new-descriptors <file>
      [--old-extra <capture folder>]... [--new-extra <capture folder>]... --out <tsv>
"""
import argparse, importlib.util, os
from pathlib import Path

_spec = importlib.util.spec_from_file_location("frosty_ebx_decode", Path(__file__).with_name("frosty-ebx-decode.py"))
decode = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(decode)

ROOT = "common/hardware/weapons/"


def weapon_files(collection, extra):
    """Lower-case route -> (route, raw file) for Equipment_* and Attachment_* files; later folders win."""
    files = {}
    for raw in [Path(collection) / "raw"] + [Path(e) / "raw" for e in extra]:
        for parent, _, names in os.walk(raw):
            for n in names:
                low = n.lower()
                if low.endswith(".ebx") and low.startswith(("equipment_", "attachment_")):
                    rel = Path(parent, n).relative_to(raw).with_suffix("").as_posix()
                    if rel.lower().startswith(ROOT):
                        files[rel.lower()] = (rel, Path(parent, n))
    return files


def imports(value, found):
    if isinstance(value, dict):
        if "$import" in value and isinstance(value["$import"], dict):
            found.add(str(value["$import"].get("fileGuid", "")).lower())
        for v in value.values():
            imports(v, found)
    elif isinstance(value, list):
        for v in value:
            imports(v, found)
    return found


def offered(files, types):
    """Equipment route -> set of attachment names it imports from its own folder."""
    guid_name, lists = {}, {}
    for key, (route, path) in files.items():
        asset = decode.Ebx(path, types).decode()
        folder = key.rsplit("/", 1)[0]
        name = route.rsplit("/", 1)[1]
        if name.lower().startswith("attachment_"):
            guid_name[(folder, str(asset.get("fileGuid", "")).lower())] = name
        else:
            lists[key] = (route, folder, imports(asset["objects"], set()))
    return {key: (route, {guid_name[(folder, g)] for g in guids if (folder, g) in guid_name})
            for key, (route, folder, guids) in lists.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("old", help="Old collection folder (with raw\\)")
    parser.add_argument("new", help="New collection folder (with raw\\)")
    parser.add_argument("--old-descriptors", required=True)
    parser.add_argument("--new-descriptors", required=True)
    parser.add_argument("--old-extra", action="append", default=[], help="Further old capture folder (with raw\\); repeatable, later wins")
    parser.add_argument("--new-extra", action="append", default=[], help="Further new capture folder (with raw\\); repeatable, later wins")
    parser.add_argument("--out", required=True, help="TSV to write")
    args = parser.parse_args()

    old = offered(weapon_files(args.old, args.old_extra), decode.type_descriptors(args.old_descriptors))
    new = offered(weapon_files(args.new, args.new_extra), decode.type_descriptors(args.new_descriptors))
    rows = []
    for key in sorted(old.keys() | new.keys()):
        name = (new.get(key) or old.get(key))[0].rsplit("/", 1)[1]
        if key not in old:
            rows.append((name, "list added", ""))
        elif key not in new:
            rows.append((name, "list removed", ""))
        a, b = (old.get(key) or ("", set()))[1], (new.get(key) or ("", set()))[1]
        rows += [(name, "removed", x) for x in sorted(a - b)] + [(name, "added", x) for x in sorted(b - a)]
    with open(args.out, "w", encoding="utf-8", newline="\n") as out:
        out.write("equipment\tchange\tattachment\n")
        out.writelines("\t".join(r) + "\n" for r in rows)
    count = lambda c: sum(r[1] == c for r in rows)
    print(f"{len(old)} old and {len(new)} new lists; {count('removed')} removed, {count('added')} added, "
          f"{count('list added')} lists added, {count('list removed')} lists removed")
    for r in rows:
        if r[1] in ("removed", "list removed"):
            print("\t".join(r))


if __name__ == "__main__":
    main()
