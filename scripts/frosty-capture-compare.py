"""Compare a new -Catalog capture with the pre-update baseline capture.

  python scripts/frosty-capture-compare.py <baseline collection dir> <new collection dir> <out comparison.json>
      [--baseline-catalog <dir>]

Each collection dir holds asset-catalog.json and raw-status.jsonl (frosty-collect-raw.ps1
output). Compares the catalogs (added, removed, GUID, size and Frosty record SHA-1 changes)
and the raw SHA-256 of every route captured successfully in both. Read-only except for the
output file. Paths are grouped by top-level area so gameplay changes stand out.

--baseline-catalog takes the baseline asset-catalog.json from another folder, for a baseline
whose raw files and catalog come from different runs (a loaded-cache raw capture plus a
rebuilt-cache catalog). Frosty lists more assets in a run that rebuilds its cache, so compare
a rebuilt-cache capture only with a rebuilt-cache catalog.

Every raw file compared is re-hashed from disk on both sides and checked against the SHA-256
in its raw-status.jsonl; a missing file or a mismatch is listed and makes the result
incomplete.

Coverage is explicit: baseline routes absent from the new status file (and the reverse) are
listed, and the script exits 1 when coverage is incomplete, so a partial capture cannot
support a hotfix decision.
"""
import argparse, collections, hashlib, json, os, sys

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("baseline")
ap.add_argument("new")
ap.add_argument("out")
ap.add_argument("--baseline-catalog", help="folder holding the baseline asset-catalog.json (default: the baseline dir)")
a = ap.parse_args()
base_dir, new_dir, out_path = a.baseline, a.new, a.out
base_cat_dir = a.baseline_catalog or base_dir

def catalog(d):
    c = json.load(open(os.path.join(d, "asset-catalog.json"), encoding="utf-8-sig"))
    return c, {x["path"].lower(): x for x in c["assets"]}

def raw(d):
    rows = {}
    for line in open(os.path.join(d, "raw-status.jsonl"), encoding="utf-8-sig"):
        r = json.loads(line)
        rows[r["path"].lower()] = r
    return rows

def area(path):
    p = path.lower()
    for key, label in (("/ui/", "ui"), ("/sound/", "sound"), ("/art/", "art"), ("animations/", "animation"),
                       ("/hardware/", "hardware"), ("systems/", "systems"), ("gamemodes", "gamemodes"), ("levels/", "levels")):
        if key in p or p.startswith(key.strip("/")):
            return label
    return "other"

def disk_mismatches(d, rows, keys):
    bad = []
    for k in keys:
        r = rows[k]
        try:
            with open(os.path.join(d, r["file"]), "rb") as f:
                ok = hashlib.sha256(f.read()).hexdigest() == r["sha256"].lower()
        except OSError:
            ok = False
        if not ok:
            bad.append(r["path"])
    return sorted(bad)

bc, bmap = catalog(base_cat_dir)
nc, nmap = catalog(new_dir)
added = sorted(nmap[k]["path"] for k in nmap.keys() - bmap.keys())
removed = sorted(bmap[k]["path"] for k in bmap.keys() - nmap.keys())
changed = {f: [] for f in ("guid", "originalBytes", "storedBytes", "sha1")}
for k in bmap.keys() & nmap.keys():
    for f in changed:
        if bmap[k].get(f) != nmap[k].get(f):
            changed[f].append(nmap[k]["path"])
for f in changed:
    changed[f].sort()

braw, nraw = raw(base_dir), raw(new_dir)
missing_new = sorted(braw[k]["path"] for k in braw.keys() - nraw.keys())
missing_base = sorted(nraw[k]["path"] for k in nraw.keys() - braw.keys())
both = [k for k in braw.keys() & nraw.keys() if braw[k]["status"] == nraw[k]["status"] == "success"]
raw_diff = sorted(nraw[k]["path"] for k in both if braw[k]["sha256"] != nraw[k]["sha256"])
new_fail = sorted(nraw[k]["path"] for k in nraw if nraw[k]["status"] != "success" and braw.get(k, {}).get("status") == "success")
new_ok = sorted(nraw[k]["path"] for k in nraw if nraw[k]["status"] == "success" and k in braw and braw[k]["status"] != "success")
still_fail = sorted(nraw[k]["path"] for k in nraw if nraw[k]["status"] != "success" and k in braw and braw[k]["status"] != "success")
disk_bad = {"baseline": disk_mismatches(base_dir, braw, both), "new": disk_mismatches(new_dir, nraw, both)}
complete = not missing_new and not missing_base and not new_fail and not disk_bad["baseline"] and not disk_bad["new"]

def by_area(paths):
    return dict(collections.Counter(area(p) for p in paths))

result = {
    "baseline": {"dir": base_dir, "catalogDir": base_cat_dir, "gameHead": bc.get("gameHead"), "sdkVersion": bc.get("sdkVersion"), "assets": len(bmap),
                 "routes": len(braw)},
    "new": {"dir": new_dir, "gameHead": nc.get("gameHead"), "sdkVersion": nc.get("sdkVersion"), "assets": len(nmap),
            "routes": len(nraw)},
    "catalog": {"added": added, "removed": removed, "changed": changed,
                "changedAnyByArea": by_area(set().union(*changed.values()))},
    "raw": {"coverageComplete": complete, "missingInNew": missing_new, "missingInBaseline": missing_base,
            "comparedRoutes": len(both), "sha256Changed": raw_diff, "sha256ChangedByArea": by_area(raw_diff),
            "newFailures": new_fail, "newSuccesses": new_ok, "failuresInBoth": still_fail,
            "diskHashMismatch": disk_bad},
}
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=1)

print(f"Head {result['baseline']['gameHead']} -> {result['new']['gameHead']}; SDK {result['baseline']['sdkVersion']} -> {result['new']['sdkVersion']}")
print(f"Catalog: {len(bmap)} -> {len(nmap)} assets; added {len(added)}, removed {len(removed)}; "
      + ", ".join(f"{f} changed {len(v)}" for f, v in changed.items()))
print(f"Catalog changes by area: {result['catalog']['changedAnyByArea']}")
print(f"Raw: {len(braw)} baseline routes, {len(nraw)} new; {len(both)} compared; SHA-256 changed {len(raw_diff)} "
      f"{result['raw']['sha256ChangedByArea']}; new failures {len(new_fail)}; new successes {len(new_ok)}; "
      f"failing in both {len(still_fail)}")
print(f"Coverage: missing in new {len(missing_new)}, missing in baseline {len(missing_base)}")
for p in raw_diff[:30]:
    print("  raw changed:", p)
print(f"Disk re-hash: {len(both)} files per side; mismatches baseline {len(disk_bad['baseline'])}, new {len(disk_bad['new'])}")
for label, paths in (("new failure", new_fail), ("missing in new", missing_new), ("missing in baseline", missing_base),
                     ("baseline file does not match its recorded hash", disk_bad["baseline"]),
                     ("new file does not match its recorded hash", disk_bad["new"])):
    for p in paths[:10]:
        print(f"  {label}:", p)
print(f"Written: {out_path}")
if not complete:
    sys.exit("INCOMPLETE: raw coverage differs from the baseline (missing routes or new failures), or files on disk "
             "do not match their recorded hashes. "
             "This comparison cannot support a hotfix decision until each is explained.")
