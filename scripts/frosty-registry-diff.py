"""Diff the tweakable registries of two raw collections by row name.

Covers every captured file under a Tweakables folder plus every GRX_*, MUT_* and
MutatorDatabase* file elsewhere (per-mode and per-level mutators). A row is an object with
a name in Field_0c59fa06; rows are matched by name, never by position. Values are compared
from the decoder output: boxed values by their resolved value, in-file references by the
referenced row's name, so layout-only changes (offsets, type-table indices, row ids) do not
show. Rows of the same name in one file are numbered in file order (name#2, ...).

Writes a TSV (asset, change, row, field, old, new, redsec) and prints one line per asset
with a change. Nothing is filtered: REDSEC rows (Granite assets or Granite_/BR_/RR_ names)
are flagged, not dropped, so the caller decides what is in scope.
"""
import argparse, importlib.util, json, os, sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location("frosty_ebx_decode", Path(__file__).with_name("frosty-ebx-decode.py"))
decode = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(decode)

NAME = "Field_0c59fa06"
# Row id, two name hashes and the parent link: identity, not value.
IGNORED = {"Field_8cf424e7", "Field_c124c7d8", "Field_e73c7944", "Field_96e1b4f3", "$guid"}
REDSEC_PREFIXES = ("Granite_", "BR_", "RR_")


def in_scope(relative):
    low = relative.lower()
    name = low.rsplit("/", 1)[-1]
    return "/tweakables/" in low or name.startswith(("grx_", "mut_", "mutatordatabase"))


def registry_files(collection, extra):
    """Relative lower-case route -> raw file; later folders override earlier ones."""
    files = {}
    for raw in [Path(collection) / "raw"] + [Path(e) / "raw" for e in extra]:
        for parent, _, names in os.walk(raw):
            for n in names:
                if n.lower().endswith(".ebx"):
                    rel = Path(parent, n).relative_to(raw).with_suffix("").as_posix()
                    if in_scope(rel):
                        files[rel.lower()] = (rel, Path(parent, n))
    return files


def rows(path, types):
    objects = decode.Ebx(path, types).decode()["objects"]
    label = [o.get(NAME) if isinstance(o.get(NAME), str) else o.get("$class") for o in objects]

    def norm(v):
        if isinstance(v, dict):
            if "$boxedValue" in v:
                return norm(v.get("value"))
            if set(v) == {"$ref"}:
                return f"->{label[v['$ref']]}" if isinstance(v["$ref"], int) and v["$ref"] < len(label) else "->?"
            return {k: norm(x) for k, x in v.items() if k not in IGNORED}
        if isinstance(v, list):
            return [norm(x) for x in v]
        return v

    found = {}
    for o in objects:
        name = o.get(NAME)
        if not isinstance(name, str) or not name or "/" in name:   # the file's own container
            continue
        key, i = name, 2
        while key in found:
            key, i = f"{name}#{i}", i + 1
        found[key] = {k: norm(v) for k, v in o.items() if k not in IGNORED and k != NAME}
    return found


def text(v):
    return "" if v is None else json.dumps(v, ensure_ascii=False, separators=(",", ":"))


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

    old_types, new_types = decode.type_descriptors(args.old_descriptors), decode.type_descriptors(args.new_descriptors)
    old, new = registry_files(args.old, args.old_extra), registry_files(args.new, args.new_extra)
    with open(args.out, "w", encoding="utf-8", newline="") as out:
        out.write("asset\tchange\trow\tfield\told\tnew\tredsec\n")
        for key in sorted(old.keys() | new.keys()):
            asset = (new.get(key) or old.get(key))[0]
            a = rows(old[key][1], old_types) if key in old else None
            b = rows(new[key][1], new_types) if key in new else None
            if a is None or b is None:
                out.write(f"{asset}\t{'file added' if a is None else 'file removed'}\t\t\t\t\t{int('granite' in key)}\n")
                print(f"{asset}: file {'added' if a is None else 'removed'} ({len(b if a is None else a)} rows)")
                if a is None:
                    a = {}
                else:
                    continue
            counts = {"added": 0, "removed": 0, "changed": 0}
            for row in sorted(a.keys() | b.keys()):
                redsec = int("granite" in key or row.startswith(REDSEC_PREFIXES))
                if row not in a:
                    counts["added"] += 1
                    out.write(f"{asset}\tadded\t{row}\t\t\t{text(b[row])}\t{redsec}\n")
                elif row not in b:
                    counts["removed"] += 1
                    out.write(f"{asset}\tremoved\t{row}\t\t{text(a[row])}\t\t{redsec}\n")
                elif a[row] != b[row]:
                    counts["changed"] += 1
                    for f in sorted(a[row].keys() | b[row].keys()):
                        if a[row].get(f) != b[row].get(f):
                            out.write(f"{asset}\tchanged\t{row}\t{f}\t{text(a[row].get(f))}\t{text(b[row].get(f))}\t{redsec}\n")
            if any(counts.values()):
                print(f"{asset}: {len(a)} -> {len(b)} rows, +{counts['added']} -{counts['removed']} ~{counts['changed']}")


if __name__ == "__main__":
    main()
