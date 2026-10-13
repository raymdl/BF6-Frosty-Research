r"""Paths for the update readers: which build they read and where they keep their working files.

Edit settings.json to point at a new build, or set BF6_BUILD and BF6_READER_WORK for one run.
  build       build label under <datamining>\builds
  work        working folder; each part reads and writes its files in <work>\A, \B, \C
Every raw capture of the build is read: capture\collection\raw first, then each reports\*\raw
folder in date order (the date in the folder name), so a later capture overrides an earlier one.
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
DESCRIPTORS = BUILD / "capture/toolchain/SharedTypeDescriptors.ebx"
CATALOG = BUILD / "capture/collection/asset-catalog.json"
STRINGS = BUILD / "capture/fs_us_loc.strings.tsv"


def part(name):
    folder = WORK / name
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def raw_folders():
    def date(p):
        m = re.search(r"\d{4}-\d{2}-\d{2}", p.parent.name)
        return (m[0] if m else "", p.parent.name)
    later = sorted((p for p in (BUILD / "reports").glob("*/raw") if p.is_dir()), key=date)
    return [BUILD / "capture/collection/raw"] + later


def held_routes():
    """lower-case route -> (file path, route as stored), over every raw folder of the build."""
    held = {}
    for folder in raw_folders():
        for p in folder.rglob("*.ebx"):
            route = p.relative_to(folder).as_posix()[:-4]
            held[route.lower()] = (str(p), route)
    return held


def regnames():
    """The registry field-name table written by regnames.py (older runs kept it under trace/)."""
    for p in (WORK / "regnames.tsv", RUN / "trace/regnames.tsv"):
        if p.is_file():
            return p
    raise FileNotFoundError("regnames.tsv not found; run regnames.py first")