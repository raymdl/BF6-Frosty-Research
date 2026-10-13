"""Resolve BF6 attachment UI labels and descriptions from Frosty XML and fs_us strings."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve(root, reference, strings):
    value = root.findtext(f"Class_535682be/{reference}")
    if not value or not value.startswith("[Class_fbe1d3bc] "):
        return {"error": f"missing reference: {value}"}
    guid = value.split(" ", 1)[1]
    target = root.find(f"Class_fbe1d3bc[@Guid='{guid}']")
    if target is None:
        return {"error": f"missing target: {guid}"}
    raw_id = target.findtext("Field_3d34898a")
    if not raw_id or not raw_id.startswith("0x"):
        return {"error": f"missing string id: {raw_id}"}
    string_id = raw_id[2:].upper()
    result = {"id": string_id}
    if string_id in strings:
        result["text"] = strings[string_id]
    else:
        result["error"] = "id absent from English string table"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    spec = importlib.util.spec_from_file_location("frosty_raw_tree", Path(__file__).resolve().parent / "frosty-raw-tree.py")
    raw_tree = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(raw_tree)
    parser.add_argument("xml_root", type=Path,
                        help="Folder holding the AD_* XML files; with --raw, a folder inside the raw export")
    parser.add_argument("strings_tsv", type=Path)
    parser.add_argument("output_json", type=Path)
    raw_tree.add_raw_arguments(parser)
    args = parser.parse_args()
    export = raw_tree.open_input(parser, args, None if args.raw else args.xml_root)
    if args.raw:
        args.xml_root = export.root / args.xml_root

    strings = {}
    duplicates = []
    with args.strings_tsv.open(encoding="utf-8-sig") as source:
        for line in source:
            string_id, text = line.rstrip("\r\n").split("\t", 1)
            if string_id in strings:
                duplicates.append(string_id)
            strings[string_id] = text

    records = []
    for path in sorted(args.xml_root.rglob("AD_*.xml")):
        root, digest = export.load(path.relative_to(export.root).as_posix())
        main_asset = root.find("Class_535682be")
        asset = main_asset.findtext("Field_0c59fa06") if main_asset is not None else None
        records.append({
            "asset": asset,
            "xmlSha256": digest,
            "label": resolve(root, "Field_33a358a7", strings),
            "description": resolve(root, "Field_490f0dd0", strings),
        })

    for record in records:
        if record["description"].get("error") == "id absent from English string table":
            record["reviewStatus"] = "description-review-required"
            record["reviewReason"] = "Verify the description against an in-game capture or a later English string export; retain the resolved label and leave description text unset."

    result = {
        "scope": "BF6 English attachment UI text from Frosty EBX metadata; descriptions are not mechanics proof",
        "sourceStrings": "Common/Localization/Languages/fs_us_loc",
        "sourceStringsSha256": sha256(args.strings_tsv),
        "stringIdDuplicates": sorted(set(duplicates)),
        "count": len(records),
        "attachments": records,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(export.mark(result), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    errors = [(item["asset"], key, item[key]["error"])
              for item in records for key in ("label", "description") if "error" in item[key]]
    print(f"{len(records)} records, {len(errors)} resolution errors, {len(duplicates)} duplicate string ids")
    for error in errors[:20]:
        print(*error, sep="\t")
    if len(errors) > 20:
        print(f"... {len(errors) - 20} more errors in output")


if __name__ == "__main__":
    main()
