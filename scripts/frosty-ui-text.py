"""Turn a raw UI metadata EBX into a table of its records and their resolved text.

  python scripts/frosty-ui-text.py <raw .ebx> [<raw .ebx> ...] [--strings <tsv>] [--descriptors <ebx>] [--catalog <json>] [--out <json>]

For each object in the asset, every field that points (directly or through a list) to a
text object (one holding a string id in Field_3d34898a) is resolved against the strings
table; plain string fields (internal names) are kept too. Objects with no text are skipped.
Output: one row per object with its class, GUID, plain strings, resolved text per field
and imports (with catalog paths when resolvable). Defaults are the 1.4.3.1 baseline; pass
--strings, --descriptors and --catalog together for another build.
"""
import argparse, json, os, subprocess, sys, tempfile
from pathlib import Path

CAPTURE = r"C:\Users\royal\Documents\BF6 Datamining\builds\1.4.3.0\capture"
STRINGS = CAPTURE + r"\pre-update-1.4.3.1-2026-09-29\fs_us_loc.strings.tsv"
DESCRIPTORS = CAPTURE + r"\toolchain\SharedTypeDescriptors-hotfix-2026-09-16.ebx"
CATALOG = CAPTURE + r"\pre-update-1.4.3.1-2026-09-29\collection\asset-catalog.json"
DECODER = Path(__file__).resolve().parent / "frosty-ebx-decode.py"
TEXT_FIELD = "Field_3d34898a"

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("ebx", nargs="+")
ap.add_argument("--strings", default=STRINGS)
ap.add_argument("--descriptors", default=DESCRIPTORS)
ap.add_argument("--catalog", default=CATALOG, help="asset-catalog.json used to name imports")
ap.add_argument("--out")
a = ap.parse_args()

strings = {}
for line in open(a.strings, encoding="utf-8"):
    k, _, v = line.rstrip("\n").partition("\t")
    strings[k.upper()] = v
guid_path = {}
if os.path.exists(a.catalog):
    guid_path = {x["guid"].lower(): x["path"] for x in json.load(open(a.catalog, encoding="utf-8-sig"))["assets"]}
else:
    print(f"Catalog not found, imports stay as GUIDs: {a.catalog}", file=sys.stderr)

def text_of(obj):
    v = obj.get(TEXT_FIELD) if isinstance(obj, dict) else None
    if isinstance(v, int) and not isinstance(v, bool):
        key = f"{v & 0xFFFFFFFF:08X}"
        return strings.get(key, f"<missing {key}>")
    return None

rows = []
with tempfile.TemporaryDirectory(prefix="frosty-ui-text-") as tmpdir:
    for n, ebx in enumerate(a.ebx):
        tmp = os.path.join(tmpdir, f"{n}.decoded.json")
        subprocess.run([sys.executable, str(DECODER), "--descriptors", a.descriptors, "--ebx", ebx, "--out", tmp],
                       check=True, capture_output=True)
        assets = json.load(open(tmp, encoding="utf-8"))["assets"]
        asset = assets[0] if isinstance(assets, list) else list(assets.values())[0]
        objs = asset["objects"]
        for i, o in enumerate(objs):
            texts, plain, imports = {}, {}, {}
            def walk(v, path):
                if isinstance(v, dict):
                    if "$ref" in v and isinstance(v["$ref"], int) and 0 <= v["$ref"] < len(objs):
                        t = text_of(objs[v["$ref"]])
                        if t is not None:
                            texts[path] = t
                        return
                    if "$import" in v:
                        g = v["$import"].get("fileGuid", "").lower()
                        imports[path] = guid_path.get(g, g)
                        return
                    for k, x in v.items():
                        if not k.startswith("$"):
                            walk(x, f"{path}/{k}")
                elif isinstance(v, list):
                    for j, x in enumerate(v):
                        walk(x, f"{path}[{j}]")
                elif isinstance(v, str) and path.count("/") == 1:
                    plain[path[1:]] = v
            for k, v in o.items():
                if not k.startswith("$") and k != TEXT_FIELD:
                    walk(v, f"/{k}")
            if texts:
                rows.append({"asset": os.path.basename(ebx), "object": i, "class": o.get("$class"), "guid": o.get("$guid"),
                             "plain": plain, "text": texts, "imports": imports})

print(f"{len(rows)} records with text")
for r in rows:
    name = next(iter(r["plain"].values()), "") if r["plain"] else ""
    parts = "; ".join(f"{k.split('/')[-1]}={v[:70]}" for k, v in r["text"].items())
    print(f"[{r['asset'][:28]} #{r['object']}] {name[:30]} | {parts[:230]}")
if a.out:
    json.dump(rows, open(a.out, "w", encoding="utf-8"), indent=1)
    print(f"Written: {a.out}")
