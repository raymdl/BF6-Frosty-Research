r"""Paths for the update readers: which build they read and where they keep their working files.

Edit settings.json to point at a new build, or set BF6_BUILD and BF6_READER_WORK for one run.
  build       build label under <datamining>\builds
  work        working folder; each part reads and writes its files in <work>\A, \B, \C
  newWeapons  the update's new weapons: siteId, name, class, internal name, weapon folder
Every raw capture of the build is read: capture\collection\raw first, then
capture\collection-fresh-cache\raw, then each reports\*\raw folder in date order (the date in the
folder name), so a later capture overrides an earlier one. The reports\mp-copies-*\raw folders
(multiplayer copies, frosty-mp-copies.py) are read last, so no campaign copy overrides them.
File GUIDs resolve through byguid(): the capture catalog, with the renamed-asset catalogs
(reports\mp-*\asset-catalog.json) deciding the GUIDs they list. Routes in a
reports\*\campaign-only.txt (held by no multiplayer bundle) are left out of held_routes().
None of the three applies when BF6_RAWINDEX or BF6_CATALOG names another capture.
To read another capture (for example the pre-update baseline of a sealed build), set for one run:
  BF6_RAWINDEX     run raw index, <route><TAB><absolute .ebx path>[<TAB>sha256]; replaces the folder walk
  BF6_DESCRIPTORS  that capture's SharedTypeDescriptors.ebx
  BF6_CATALOG      its asset-catalog.json
  BF6_STRINGS      its fs_us_loc.strings.tsv
"""
import json, os, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
_cfg = json.loads((HERE / "settings.json").read_text(encoding="utf-8"))
D = pathlib.Path(os.environ.get("BF6_DATAMINING") or _cfg["datamining"])
SITE = pathlib.Path(_cfg["site"])
BUILD_LABEL = os.environ.get("BF6_BUILD") or _cfg["build"]
BUILD = D / "builds" / BUILD_LABEL
WORK = pathlib.Path(os.environ.get("BF6_READER_WORK") or _cfg["work"])
RUN = WORK.parent    # the run folder; one-off scripts read earlier trace outputs from it
DESCRIPTORS = pathlib.Path(os.environ.get("BF6_DESCRIPTORS") or BUILD / "capture/toolchain/SharedTypeDescriptors.ebx")
CATALOG = pathlib.Path(os.environ.get("BF6_CATALOG") or BUILD / "capture/collection/asset-catalog.json")
STRINGS = pathlib.Path(os.environ.get("BF6_STRINGS") or BUILD / "capture/fs_us_loc.strings.tsv")
NEW_WEAPONS = _cfg.get("newWeapons", [])


def part(name):
    folder = WORK / name
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def raw_folders():
    def date(p):
        m = re.search(r"\d{4}-\d{2}-\d{2}", p.parent.name)
        return (m[0] if m else "", p.parent.name)
    def mp(p):
        return p.parent.name.startswith("mp-copies-")
    later = sorted((p for p in (BUILD / "reports").glob("*/raw") if p.is_dir()), key=lambda p: (mp(p), date(p)))
    fresh = [p for p in [BUILD / "capture/collection-fresh-cache/raw"] if p.is_dir()]
    return [BUILD / "capture/collection/raw"] + fresh + later


def held_routes():
    """lower-case route -> (file path, route as stored), over every raw folder of the build."""
    held = {}
    index = os.environ.get("BF6_RAWINDEX")
    if index:
        for line in open(index, encoding="utf-8"):
            p = line.rstrip("\n").split("\t")
            if len(p) >= 2 and p[0]:
                held[p[0].lower()] = (p[1], p[0])
        return held
    for folder in raw_folders():
        for p in folder.rglob("*.ebx"):
            route = p.relative_to(folder).as_posix()[:-4]
            held[route.lower()] = (str(p), route)
    for listing in sorted((BUILD / "reports").glob("*/campaign-only.txt")):
        for line in listing.read_text(encoding="utf-8").splitlines():
            held.pop(line.strip().lower(), None)
    return held


def byguid():
    """lower-case file GUID -> route. A renamed-asset catalog decides the GUIDs it lists: the capture
    catalog gives those to a campaign-only leftover (AD_SF300 for AD_SF300_RightRail's GUID)."""
    cat = json.load(open(CATALOG, encoding="utf-8"))
    rows = cat if isinstance(cat, list) else next(v for v in cat.values() if isinstance(v, list))
    index = {str(r["guid"]).lower(): r["path"] for r in rows}
    if not os.environ.get("BF6_CATALOG"):
        for renamed in sorted((BUILD / "reports").glob("mp-*/asset-catalog.json")):
            for r in json.loads(renamed.read_text(encoding="utf-8"))["assets"]:
                index[r["guid"].lower()] = r["path"]
    return index


def regnames():
    """The registry field-name table written by regnames.py (older runs kept it under trace/)."""
    for p in (WORK / "regnames.tsv", RUN / "trace/regnames.tsv"):
        if p.is_file():
            return p
    raise FileNotFoundError("regnames.tsv not found; run regnames.py first")