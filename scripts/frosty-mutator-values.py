"""Print watched mutator settings from raw captures, one column per collection.

A mutator entry stores max, default and min in three hashed fields; the slot roles come
from entries with known ranges (Gauntlet_LobbyMaxPlayers 100/32/0, MinRespawnTime
100/1.5/0). A max of 0 appears to mean no upper limit. "-" means the entry is absent.
These are shipped defaults; servers can override tweakables at runtime.
"""
import argparse, importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("frosty_raw_tree", Path(__file__).with_name("frosty-raw-tree.py"))
rt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rt)

ASSET = "Common/GameSetup/Tweakables/Mutators/MutatorDatabase_CH1.xml"
# Added in 2.1.1.0 (absent in 1.4.2.5 to 1.4.3.5): the 300 XP per 60 s caps.
WATCHED = ["WeaponXpCap", "VehicleXpCap", "ClassXpCap", "CareerXpCap", "BattlepassXpCap",
           "Xp Cap Interval In Seconds"]
NAME, MAX, DEFAULT, MIN = "Field_0c59fa06", "Field_3ff76ddb", "Field_42c8b257", "Field_c06d0cbb"


def value(text):
    return str(int(text, 16)) if text and text.lower().startswith("0x") else (text or "?")


def read(collection, descriptors):
    collection = Path(collection)
    export = rt.RawExport([collection / "raw/Common/GameSetup/Tweakables/Mutators"], descriptors,
                          collection / "asset-catalog.json")
    tree, _ = export.read("MutatorDatabase_CH1.xml")
    root = tree.getroot() if hasattr(tree, "getroot") else tree
    found = {}
    for element in root.iter():
        name = element.find(NAME)
        if name is not None and name.text in WATCHED:
            found[name.text] = " / ".join(value(element.findtext(k)) for k in (DEFAULT, MIN, MAX))
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("collections", nargs="+", help="Collection folders (with raw\\ and asset-catalog.json)")
    parser.add_argument("--descriptors", nargs="+", required=True,
                        help="SharedTypeDescriptors.ebx per collection, in the same order (or one for all)")
    args = parser.parse_args()
    descriptors = args.descriptors * len(args.collections) if len(args.descriptors) == 1 else args.descriptors
    if len(descriptors) != len(args.collections):
        parser.error("give one descriptors file, or one per collection")
    columns = [read(c, d) for c, d in zip(args.collections, descriptors)]
    print("| Setting | " + " | ".join("/".join(Path(c).parts[-3:-1]) for c in args.collections) + " |")
    print("|---" * (len(columns) + 1) + "|")
    for name in WATCHED:
        print(f"| `{name}` | " + " | ".join(col.get(name, "-") for col in columns) + " |")
    print("\nValues are default / min / max.")


if __name__ == "__main__":
    main()
