#!/usr/bin/env python3
r"""Run Stage 0 or Stage 1 of the game update procedure as one command.

  python scripts/frosty-update-run.py stage0 [--dry-run] [--force] [--sights] [--client <id>]
  python scripts/frosty-update-run.py stage1 [--dry-run] [--name client-new] [--previous-label <label>]
      [--old-extra <capture folder>]... [--new-extra <capture folder>]...

Common arguments (before or after the subcommand):
  --datamining DIR   default C:\Users\royal\Documents\BF6 Datamining
  --game DIR         default C:\Program Files\EA Games\Battlefield 6
  --runtime DIR      default <datamining>\FrostyToolsuite-battlefield6\FrostyEditor\bin\Release\Final
  --date yyyy-mm-dd  default today
  --build BUILD      default: the build frosty-build.py status reports as open
  --dry-run          print every command, copy, rename and written file in order, with full
                     paths, and change nothing (the read-only checks still run)

The procedure is docs/GAME_UPDATE_GUIDE.md in the Analyzer repo (Stage 0, Stage 1, and Stage 2
step 5 for the multiplayer copies). This script only chains the scripts that guide names.

stage0 (while the old build is still installed):
  Need check: guard passes, the baseline exists and no game file (other than EAAntiCheat* and
  preloader*) is newer than the baseline's asset-catalog.json -> "Stage 0 not needed", exit 0
  (--force runs it anyway). Guard failing -> stop: Stage 1 applies.
  Otherwise, in order: baseline capture (frosty-capture.py --catalog, newest route list);
  graph bodies; sight files (only when the build has no sight-files folder or a client was added
  since the newest one; --sights forces it); toolchain copies and the strings export; multiplayer
  copies; record; verify. The baseline capture stopping is a stop; a later step failing is
  recorded and the run continues (exit 1 at the end). The cache rename for the routes that fail
  as "not in current catalog" is printed, not done.

stage1 (guard fails on a new bf6.exe; the game must be closed):
  Guide steps 1 to 5: executable identity; cache rename; capture with --update-check into
  reports\<name>-check-<date>\collection; client-check; frosty-capture-compare.py (and a second
  comparison against collection-fresh-cache when the baseline has one); frosty-mutator-values.py;
  frosty-hotfix-check.py. Exit codes that are results (compare 1, client-check 1, hotfix-check 1
  or 2) do not stop the run; a capture failure does. Ends with a summary table and the decision
  inputs, also written to <check folder>\stage1-summary.md. The hotfix or new-build decision
  (step 6) is never made here.

Baseline (both subcommands): the open build's newest capture\pre-update-*\collection, else
capture\collection; its descriptors are the descriptorsFile of the BUILD.json client whose
frostyArchiveHead is the baseline's gameHead.

Nothing is ever deleted or overwritten: a target that exists stops the step.
"""
import argparse
import datetime
import hashlib
import json
import msvcrt
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

RESEARCH = Path(__file__).resolve().parent.parent
SCRIPTS = RESEARCH / "scripts"
COLLECTOR = RESEARCH.parent / "BF6 Weapon Analyzer" / "scripts" / "frosty-collect-raw.ps1"
DM = r"C:\Users\royal\Documents\BF6 Datamining"
GAME = r"C:\Program Files\EA Games\Battlefield 6"
RUNTIME = r"FrostyToolsuite-battlefield6\FrostyEditor\bin\Release\Final"
STRINGS_ASSET = "Common/Localization/Languages/fs_us_loc"
TOOLCHAIN = ("Profiles/BF6SDK.dll", "FrostySdk.dll", "SharedTypeDescriptors.ebx", "FrostyCmd.exe")
IGNORED_GAME_FILES = ("eaanticheat", "preloader")
DATE = re.compile(r"(\d{4}-\d{2}-\d{2})([a-z]?)")

DRY = False
STEPS = []  # (step, exit code or None, output file or "", note)


# ---------- small helpers ----------

def say(text=""):
    print(text, flush=True)


def py(script, *args, isolated=False):
    return [sys.executable, *(["-I"] if isolated else []), str(SCRIPTS / script), *[str(a) for a in args]]


def build_tool(a, *args):
    return py("frosty-build.py", "--datamining", a.datamining, *args)


def run(step, cmd, save=None, expected=(0,), marker=None, cwd=RESEARCH):
    """Run one command. Returns (exit code, output); (None, "") under --dry-run.

    The output is printed and, with save, written to that file (stdout then stderr).
    A code in expected with marker in the output is a result; anything else is noted UNEXPECTED.
    """
    say(f"\n[{step}]")
    say(("WOULD RUN: " if DRY else "RUN: ") + subprocess.list2cmdline([str(c) for c in cmd]))
    if save:
        say(("WOULD WRITE: " if DRY else "OUTPUT TO: ") + str(save))
    if DRY:
        STEPS.append((step, None, str(save or ""), "dry run"))
        return None, ""
    done = subprocess.run([str(c) for c in cmd], cwd=cwd, capture_output=True, text=True, errors="replace")
    text = done.stdout + (("\n" + done.stderr) if done.stderr.strip() else "")
    say(text.rstrip())
    say(f"exit code {done.returncode}")
    if save:
        if Path(save).exists():
            say(f"NOT WRITTEN: {save} exists; the output above is the only copy.")
        elif Path(save).parent.is_dir():
            Path(save).write_text(text, encoding="utf-8")
        else:
            say(f"NOT WRITTEN: folder {Path(save).parent} does not exist.")
    ok = done.returncode in expected and (marker is None or done.returncode == 0 or marker in text)
    STEPS.append((step, done.returncode, str(save or ""), "" if ok else "UNEXPECTED"))
    return done.returncode, text


def quiet(cmd):
    """Run a read-only command (also under --dry-run) and return (exit code, output)."""
    done = subprocess.run([str(c) for c in cmd], cwd=RESEARCH, capture_output=True, text=True, errors="replace")
    return done.returncode, (done.stdout.strip() or done.stderr.strip())


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def stamp(seconds):
    return datetime.datetime.fromtimestamp(seconds).strftime("%Y-%m-%d %H:%M:%S")


def ps_quote(text):
    return "'" + str(text).replace("'", "''") + "'"


def running(*names):
    """Names of running processes among names (PowerShell Get-Process); None if the check failed."""
    command = "@(Get-Process -Name " + ",".join(names) + " -ErrorAction SilentlyContinue | ForEach-Object { $_.ProcessName }) -join ','"
    done = subprocess.run(["powershell", "-NoProfile", "-Command", command], capture_output=True, text=True)
    if done.returncode:
        return None
    return [n for n in done.stdout.strip().split(",") if n]


def file_version(exe):
    done = subprocess.run(["powershell", "-NoProfile", "-Command",
                           f"(Get-Item -LiteralPath {ps_quote(exe)}).VersionInfo.FileVersion"],
                          capture_output=True, text=True)
    return done.stdout.strip() or f"(not read: {done.stderr.strip()[:200]})"


def summary_table():
    rows = ["| Step | Exit code | Output file | Note |", "|---|---|---|---|"]
    for step, code, out, note in STEPS:
        rows.append(f"| {step} | {'-' if code is None else code} | {out or '-'} | {note or '-'} |")
    return rows


# ---------- build facts ----------

def open_build(a):
    code, text = quiet(build_tool(a, "status"))
    if code:
        sys.exit(f"STOP: frosty-build.py status failed: {text}")
    opened = [line.split()[0] for line in text.splitlines() if len(line.split()) > 1 and line.split()[1] == "open"]
    if len(opened) != 1:
        sys.exit(f"STOP: status lists {len(opened)} open builds {opened}; give --build.")
    return opened[0]


def guard(a):
    cmd = build_tool(a, "guard", a.build, "--game", a.game)
    code, text = quiet(cmd)
    say("RAN (read-only): " + subprocess.list2cmdline(cmd))
    say(f"  {text}\n  exit code {code}")
    return code == 0


def route_list(capture):
    """Newest capture\\raw-routes*.txt by the date in its name; plain raw-routes.txt is oldest."""
    def key(path):
        found = DATE.search(path.name)
        return (found.group(1), found.group(2), path.name) if found else ("", "", path.name)
    lists = [p for p in capture.glob("raw-routes*.txt") if "fresh-cache-only" not in p.name]
    if not lists:
        sys.exit(f"STOP: no raw-routes*.txt in {capture}")
    newest = max(lists, key=key)
    grids = sum(1 for line in open(newest, encoding="utf-8-sig") if line.strip().lower().endswith("materialgrid_win32"))
    if grids:
        sys.exit(f"STOP: {newest} holds {grids} level materialgrid_win32 routes (guide, Ground rules: never export them).")
    return newest


def baseline(bdir):
    """(collection, fresh-cache collection or None) of the build's current baseline."""
    def key(path):
        found = DATE.search(path.name)
        return (found.group(1), found.group(2), path.name) if found else ("", "", path.name)
    folders = [p for p in (bdir / "capture").glob("pre-update-*") if (p / "collection").is_dir()]
    parent = max(folders, key=key) if folders else bdir / "capture"
    fresh = parent / "collection-fresh-cache"
    return parent / "collection", (fresh if (fresh / "asset-catalog.json").is_file() else None)


def installed_client(info, exe_hash):
    return next((c for c in info.get("clients", []) if c.get("exeSha256") == exe_hash), None)


def baseline_descriptors(bdir, info, collection):
    """The descriptors file BUILD.json names for the client the baseline was captured on."""
    clients = info.get("clients", [])
    head = None
    identity = collection / "capture-identity.json"
    if identity.is_file():
        head = load_json(identity).get("gameHead")
    match = [c for c in clients if head is not None and c.get("frostyArchiveHead") == head]
    client = match[-1] if match else clients[-1]
    why = (f"client '{client.get('label')}' has frostyArchiveHead {head}, the baseline's gameHead" if match
           else f"no client has the baseline's gameHead {head}; used the last client '{client.get('label')}'")
    return bdir / client["descriptorsFile"], why


# ---------- stage 0 ----------

def need_check(a, bdir, collection):
    """(needed, lines) for the Stage 0 need check. Guard must already have passed."""
    catalog = collection / "asset-catalog.json"
    if not catalog.is_file():
        return True, [f"no baseline catalog at {catalog}"]
    cut = catalog.stat().st_mtime
    newer, newest, count = [], None, 0
    for folder, _, files in os.walk(a.game):
        for name in files:
            if name.lower().startswith(IGNORED_GAME_FILES):
                continue
            count += 1
            full = os.path.join(folder, name)
            try:
                mtime = os.stat(full).st_mtime
            except OSError:
                continue
            if newest is None or mtime > newest[0]:
                newest = (mtime, full)
            if mtime > cut:
                newer.append((mtime, full))
    lines = [f"baseline catalog: {catalog} (written {stamp(cut)})",
             f"game files checked: {count} under {a.game} (EAAntiCheat* and preloader* names left out); "
             f"newest is {newest[1]} ({stamp(newest[0])})" if newest else f"no files found under {a.game}",
             f"game files newer than the baseline catalog: {len(newer)}"]
    lines += [f"  newer: {path} ({stamp(mtime)})" for mtime, path in sorted(newer, reverse=True)[:10]]
    return bool(newer) or newest is None, lines


def sights_condition(bdir, info):
    """(run it, reason, mesh list or None) for the guide's Stage 0 step 3 condition."""
    def key(path):
        found = DATE.search(path.name)
        return found.group(1) if found else ""
    folders = [p for p in (bdir / "reports").glob("sight-files-*")
               if re.fullmatch(r"sight-files-\d{4}-\d{2}-\d{2}[a-z]?", p.name) and (p / "mesh-list.txt").is_file()]
    if not folders:
        previous = info.get("previousBuild")
        old = []
        if previous:
            old = [p for p in (bdir.parent / previous / "reports").glob("sight-files-*") if (p / "mesh-list.txt").is_file()]
        meshes = max(old, key=key) / "mesh-list.txt" if old else None
        return True, f"{bdir.name} has no reports\\sight-files-<date> folder", meshes
    newest = max(folders, key=key)
    meshes = newest / "mesh-list.txt"
    later = [c for c in info.get("clients", []) if c.get("checkedUtc", "")[:10] > key(newest)]
    if later:
        return True, (f"client '{later[-1].get('label')}' (checked {later[-1]['checkedUtc'][:10]}) was added after "
                      f"{newest.name}"), meshes
    return False, (f"{newest} is the baseline: no client was added after it. Sights drawn since then cannot be "
                   "detected here; if any were, add their meshes to a new list and pass --sights"), meshes


def copy_file(source, target):
    say(("WOULD COPY: " if DRY else "COPY: ") + f"{source} -> {target}")
    if not Path(source).is_file():
        say("  MISSING SOURCE")
        return False
    if Path(target).exists():
        say("  NOT COPIED: target exists")
        return False
    if not DRY:
        Path(target).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return True


def export_strings(a, target):
    """FrostyCmd export-strings under the capture lock (one Frosty process at a time)."""
    exe = Path(a.runtime) / "FrostyCmd.exe"
    cmd = [exe, "export-strings", "bf6", a.game, STRINGS_ASSET, target]
    if DRY:
        say(f"WOULD TAKE the capture lock {Path(a.datamining) / '.frosty-capture.lock'} and check that no FrostyCmd is running")
        return run("strings export", cmd, cwd=exe.parent)
    if Path(target).exists():
        say(f"\n[strings export]\nNOT RUN: {target} exists")
        STEPS.append(("strings export", None, str(target), "UNEXPECTED: target exists"))
        return None, ""
    lock = open(Path(a.datamining) / ".frosty-capture.lock", "a+")
    try:
        msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
    except OSError:
        say("\n[strings export]\nNOT RUN: the capture lock is held")
        STEPS.append(("strings export", None, str(target), "UNEXPECTED: capture lock held"))
        return None, ""
    try:
        busy = running("FrostyCmd")
        if busy is None or busy:
            say(f"\n[strings export]\nNOT RUN: FrostyCmd process check gave {busy}")
            STEPS.append(("strings export", None, str(target), "UNEXPECTED: FrostyCmd running or check failed"))
            return None, ""
        Path(target).parent.mkdir(parents=True, exist_ok=True)
        result = run("strings export", cmd, cwd=exe.parent)
        if result[0] == 0 and not Path(target).is_file():
            STEPS[-1] = ("strings export", 0, str(target), "UNEXPECTED: no file written")
        elif result[0] == 0:
            STEPS[-1] = ("strings export", 0, str(target), "")
        return result
    finally:
        lock.close()


def stage0(a):
    bdir = Path(a.datamining) / "builds" / a.build
    info = load_json(bdir / "BUILD.json")
    say(f"Stage 0 for open build {a.build} ({bdir}), date {a.date}" + (" [DRY RUN: nothing is changed]" if DRY else ""))

    say("\n== Need check ==")
    if not guard(a):
        sys.exit(f"STOP: guard fails, so the installed bf6.exe is not a recorded client of {a.build}. The game has "
                 "already updated: Stage 0 can no longer be run, Stage 1 applies "
                 "(python scripts/frosty-update-run.py stage1).")
    collection, fresh = baseline(bdir)
    needed, facts = need_check(a, bdir, collection)
    say("  guard passes: the installed client is a recorded client of the open build")
    for line in facts:
        say("  " + line)
    if not needed:
        say(f"\nStage 0 not needed: {collection} is the pre-update baseline")
        say(f"  (rebuilt-cache part: {fresh})" if fresh else "  (it has no collection-fresh-cache)")
        if not a.force:
            return 0
        say("--force given: running Stage 0 anyway.")
    else:
        say("\nStage 0 is needed: the baseline is missing or the game files are newer than it.")

    exe_hash = sha256(Path(a.game) / "bf6.exe")
    client = installed_client(info, exe_hash) or {}
    client_id = a.client or str(client.get("frostyArchiveHead") or "")
    if not client_id:
        sys.exit("STOP: the installed client's BUILD.json entry has no frostyArchiveHead; give --client <id>.")
    say(f"\nInstalled client: '{client.get('label')}', bf6.exe SHA-256 {exe_hash}, file version "
        f"{client.get('exeFileVersion')}, Frosty archive Head {client.get('frostyArchiveHead')}, "
        f"SDK {client.get('sdkVersion')}")
    name = f"pre-update-{client_id}-{a.date}"
    folder = bdir / "capture" / name
    rel = f"capture/{name}"
    if folder.exists():
        message = f"{folder} exists. Captures never reuse a folder: use another --date or --client."
        if not DRY:
            sys.exit("STOP: " + message)
        say("WOULD STOP: " + message)
    routes = route_list(bdir / "capture")
    notes = info.get("notes", "")
    say(f"Route list: {routes}")
    say("  BUILD.json notes " + ("name this file." if routes.name in notes else
                                 "do NOT name this file; check it is the list for the next update."))
    if Path(a.runtime) != Path(a.datamining) / RUNTIME:
        say(f"NOTE: --runtime {a.runtime} is used for the toolchain copies and the strings export only; "
            f"frosty-capture.py and frosty-sight-diff.py always use {Path(a.datamining) / RUNTIME}.")

    say("\n== 1. Baseline capture ==")
    code, _ = run("baseline capture", py("frosty-capture.py", name, "--build", a.build, "--into", f"{rel}/collection",
                                         "--catalog", "--routes-file", routes, "--datamining", a.datamining,
                                         "--game", a.game))
    if code:
        say("\nSTOP: the baseline capture failed. Nothing else was run. Check for a stuck FrostyCmd or powershell process.")
        return 1
    status = folder / "collection" / "raw-status.jsonl"
    fresh_routes = folder / "raw-routes-fresh-cache-only.txt"
    cache = Path(a.runtime) / "Caches" / "bf6.cache"
    cache_aside = cache.with_name(f"bf6-{client_id}-{a.date}.cache")
    follow_up = py("frosty-capture.py", f"{name}-fresh-cache", "--build", a.build, "--into",
                   f"{rel}/collection-fresh-cache", "--catalog", "--routes-file", fresh_routes,
                   "--datamining", a.datamining, "--game", a.game)
    absent = []
    if DRY:
        say(f"WOULD READ: {status} and count the failures whose reason is 'not in current catalog'")
        say(f"WOULD WRITE (only if there are any): {fresh_routes}")
    else:
        other = []
        for line in open(status, encoding="utf-8-sig"):
            row = json.loads(line)
            if row["status"] != "success":
                (absent if "not in current catalog" in (row.get("reason") or "").lower() else other).append(row)
        say(f"Baseline failures: {len(absent)} 'not in current catalog', {len(other)} other")
        for row in other[:20]:
            say(f"  OTHER FAILURE {row['path']}: {row.get('reason')}")
        if absent and not fresh_routes.exists():
            fresh_routes.write_text("\n".join(row["path"] for row in absent) + "\n", encoding="ascii")
            say(f"WROTE: {fresh_routes} ({len(absent)} routes)")
    if DRY or absent:
        say("Follow-up for the 'not in current catalog' routes (guide, Stage 0 step 1; NOT done by this script):")
        say("  a loaded cache does not list them. Routes also absent from a rebuilt cache are simply not in the game;")
        say("  compare with the last capture's failures. With the game and Frosty closed:")
        say(f"  1. rename {cache} to {cache_aside}")
        say("  2. " + subprocess.list2cmdline([str(c) for c in follow_up]))
        say("     (it runs record itself; Stage 1 then uses collection-fresh-cache as --baseline-catalog)")

    say("\n== 2. Graph bodies ==")
    ids = bdir / "capture" / "expression-graph-resource-ids.txt"
    if ids.is_file():
        run("graph bodies", py("frosty-capture.py", f"{name}-graph-bodies", "--build", a.build, "--into",
                               f"{rel}/graph-bodies", "--resource-ids-file", ids, "--datamining", a.datamining,
                               "--game", a.game))
    else:
        say(f"NOT RUN: {ids} is missing; derive it from the build's graph sources (guide, Stage 0 step 2).")
        STEPS.append(("graph bodies", None, "", "UNEXPECTED: IDs file missing"))

    say("\n== 3. Sight files ==")
    wanted, reason, meshes = sights_condition(bdir, info)
    say("Condition (guide, Stage 0 step 3): run when the open build has no sight-files folder, or a hotfix client")
    say("was added or sights were drawn since the newest one; otherwise the existing folder is the baseline.")
    say(f"  {'RUN' if wanted else 'SKIP'}: {reason}" + ("; --sights forces it" if a.sights and not wanted else ""))
    if wanted or a.sights:
        if meshes is None:
            say("NOT RUN: no mesh-list.txt found in this build or the previous one.")
            STEPS.append(("sight files", None, "", "UNEXPECTED: no mesh list"))
        else:
            run("sight files", py("frosty-sight-diff.py", "export", f"sight-files-{a.date}", "--build", a.build,
                                  "--meshes", meshes, "--datamining", a.datamining, "--game", a.game, isolated=True))
    else:
        STEPS.append(("sight files", None, "", "skipped: the existing folder is the baseline"))

    say("\n== 4. Toolchain and strings ==")
    copied = [copy_file(Path(a.runtime) / part, folder / "toolchain" / part) for part in TOOLCHAIN]
    copied.append(copy_file(COLLECTOR, folder / "toolchain" / COLLECTOR.name))
    STEPS.append(("toolchain copies", None, str(folder / "toolchain"),
                  "dry run" if DRY else ("" if all(copied) else "UNEXPECTED: a file was not copied")))
    export_strings(a, folder / "fs_us_loc.strings.tsv")

    say("\n== 5. Multiplayer copies (guide, Stage 2 step 5: run again in Stage 0) ==")
    code, text = run("multiplayer copies", py("frosty-mp-copies.py", f"mp-copies-{a.date}", "--build", a.build,
                                              "--datamining", a.datamining, "--game", a.game))
    if code and "Nothing to write" in text:
        STEPS[-1] = (STEPS[-1][0], code, "", "result: the capture already holds every multiplayer copy")

    say("\n== 6. Record and verify ==")
    run("record", build_tool(a, "record", a.build))
    run("verify", build_tool(a, "verify", a.build))

    say("\n== Summary ==")
    for row in summary_table():
        say(row)
    say("\nLeft for the session to do by hand:")
    say(f"  - BUILD.json ({bdir / 'BUILD.json'}): add preUpdateCapture to the client '{client.get('label')}' entry")
    say(f"    (folder {rel}, routesFile, catalogFile, loadedCacheCatalogFile, graphBodiesFolder, stringsFile, note;")
    say("    the 2.1.1.0 BUILD.json has a worked entry), then record again.")
    say("  - The follow-up capture on a rebuilt cache printed under step 1, if any route failed as not in catalog.")
    say("  - Gate: failures are only routes absent from the catalog (compare with the last capture's); re-hash a")
    say("    sample of raw files against raw-status.jsonl; verify is clean.")
    say("  - If sights were drawn since the newest sight-files folder: extend the mesh list and run with --sights.")
    say(f"  - Checklist: docs/updates/<version>-checklist.md in {RESEARCH} and its README index (guide, step 6).")
    say("  - Read KNOWN_SITE_DIFFERENCES.md and list the differences the patch notes touch (guide, step 7).")
    bad = [s for s in STEPS if s[3].startswith("UNEXPECTED")]
    if bad:
        say(f"\n{len(bad)} step(s) did not finish as expected: " + ", ".join(s[0] for s in bad))
    return 1 if bad else 0


# ---------- stage 1 ----------

def decision_inputs(check, identity, cache_note):
    """Lines for the guide's step 6 inputs, read from the files the steps wrote."""
    lines = ["## Decision inputs (guide, Stage 1 step 6)", "", f"- Executable: {identity}", f"- Cache: {cache_note}"]
    codes = {step: code for step, code, _, _ in STEPS}
    layout = {0: "identical (exit 0)", 1: "DIFFER (exit 1): a new build is needed"}.get(codes.get("client-check"), "not known")
    lines.append(f"- Type layouts (client-check): {layout}")
    for label, name in (("Comparison", "comparison.json"), ("Fresh-cache comparison", "comparison-fresh-cache.json")):
        path = check / name
        if not path.is_file():
            continue
        data = load_json(path)
        cat, raw = data["catalog"], data["raw"]
        lines.append(f"- {label} ({name}): Head {data['baseline']['gameHead']} -> {data['new']['gameHead']}; "
                     f"catalog {data['baseline']['assets']} -> {data['new']['assets']} assets, added {len(cat['added'])}, "
                     f"removed {len(cat['removed'])}, "
                     + ", ".join(f"{k} changed {len(v)}" for k, v in cat["changed"].items())
                     + f"; changed by area {cat['changedAnyByArea']}")
        lines.append(f"  raw: {raw['comparedRoutes']} compared, SHA-256 changed {len(raw['sha256Changed'])} "
                     f"{raw['sha256ChangedByArea']}; new failures {len(raw['newFailures'])}, new successes "
                     f"{len(raw['newSuccesses'])}, failing in both {len(raw['failuresInBoth'])}; missing in new "
                     f"{len(raw['missingInNew'])}, missing in baseline {len(raw['missingInBaseline'])}; disk mismatches "
                     f"{len(raw['diskHashMismatch']['baseline'])} / {len(raw['diskHashMismatch']['new'])}; "
                     f"coverage complete: {raw['coverageComplete']}")
    hot = check / "hotfix-check" / "summary.json"
    meaning = {0: "nothing gameplay changed", 1: "a registry row, watched mutator or gameplay path changed",
               2: "nothing changed but coverage is incomplete"}.get(codes.get("hotfix-check"), "not known")
    lines.append(f"- Hotfix check: exit {codes.get('hotfix-check')} ({meaning})")
    if hot.is_file():
        data = load_json(hot)
        lines.append(f"  changed: {data.get('changed')}; incomplete: {data.get('incomplete')}")
    watched = check / "watched-values.md"
    if watched.is_file():
        lines += ["- Watched mutator values (default / min / max):", ""]
        lines += [l for l in watched.read_text(encoding="utf-8-sig").splitlines() if l.startswith("|")]
    lines += ["", "The decision (hotfix, new build, or held) is not made by this script: guide, Stage 1 step 6.",
              "Explain every comparison exit 1 (missing routes, new failures) before deciding, and record",
              "catalogCheck, rawCheck and hotfixCheck in the client entry."]
    return lines


def stage1(a):
    bdir = Path(a.datamining) / "builds" / a.build
    info = load_json(bdir / "BUILD.json")
    label = re.sub(r"[^A-Za-z0-9._-]+", "-", a.previous_label or a.build)
    check_name = f"{a.name}-check-{a.date}"
    check = bdir / "reports" / check_name
    say(f"Stage 1 for open build {a.build} ({bdir}), date {a.date}" + (" [DRY RUN: nothing is changed]" if DRY else ""))

    say("\n== Guard must fail ==")
    if guard(a):
        message = (f"guard passes: the installed bf6.exe is a recorded client of {a.build}. The client is unchanged; "
                   "Stage 1 does not apply.")
        if not DRY:
            say(message)
            return 0
        say("WOULD STOP HERE: " + message + " (dry run: the plan below is printed anyway)")

    say("\n== 1. Executable identity ==")
    exe = Path(a.game) / "bf6.exe"
    identity = f"{exe}: SHA-256 {sha256(exe)}, file version {file_version(exe)}"
    say(identity)
    say("  (do not order builds by the file version; use the hash for identity and the Frosty archive Head for order)")

    say("\n== Game and Frosty must be closed ==")
    busy = running("bf6", "FrostyCmd")
    message = "the process check failed" if busy is None else f"running: {', '.join(busy)}"
    if busy is None or busy:
        if not DRY:
            sys.exit(f"STOP: {message}. Close the game and any FrostyCmd, then run stage1 again.")
        say(f"WOULD STOP HERE: {message}")
    else:
        say("No bf6 or FrostyCmd process is running.")

    collection, fresh = baseline(bdir)
    descriptors, why = baseline_descriptors(bdir, info, collection)
    runtime_descriptors = Path(a.runtime) / "SharedTypeDescriptors.ebx"
    routes = route_list(bdir / "capture")
    new = check / "collection"
    say(f"\nBaseline: {collection}")
    say(f"Baseline rebuilt-cache collection: {fresh or 'none (the baseline catalog is used as it is)'}")
    say(f"Baseline descriptors: {descriptors} ({why})")
    say(f"Route list: {routes}")
    say(f"Check folder: {check}")
    for path in (collection / "asset-catalog.json", collection / "raw-status.jsonl", descriptors):
        if not path.is_file():
            sys.exit(f"STOP: {path} is missing.")
    if check.exists():
        if not DRY:
            sys.exit(f"STOP: {check} exists. Use another --name or --date.")
        say(f"WOULD STOP: {check} exists.")
    if Path(a.runtime) != Path(a.datamining) / RUNTIME:
        say(f"NOTE: frosty-capture.py always uses {Path(a.datamining) / RUNTIME}; --runtime {a.runtime} reaches "
            "only the cache rename, client-check and the descriptor arguments.")

    say("\n== 2. Fresh cache ==")
    cache = Path(a.runtime) / "Caches" / "bf6.cache"
    aside = cache.with_name(f"bf6-{label}-{a.date}.cache")
    say(("WOULD RENAME: " if DRY else "RENAME: ") + f"{cache} -> {aside}")
    if aside.exists():
        if not DRY:
            sys.exit(f"STOP: {aside} exists; nothing is overwritten. Use another --previous-label.")
        say("  WOULD STOP: the target exists.")
    if not cache.is_file():
        cache_note = f"{cache} was not there; Frosty builds a full cache anyway"
        say("  " + cache_note)
    else:
        if not DRY:
            cache.rename(aside)
        cache_note = f"renamed to {aside} (disposable: offer its deletion in the final report)"
    STEPS.append(("cache rename", None, str(aside), "dry run" if DRY else ""))

    say("\n== 3. Capture the new client ==")
    code, text = run("capture", py("frosty-capture.py", check_name, "--build", a.build, "--into",
                                   f"reports/{check_name}/collection", "--catalog", "--routes-file", routes,
                                   "--update-check", "--datamining", a.datamining, "--game", a.game))
    if code:
        say(f"\nSTOP: the capture failed. Nothing after it was run. The cache: {cache_note}.")
        return 1
    if not DRY:
        (check / "capture.txt").write_text(text, encoding="utf-8")
        STEPS[-1] = ("capture", code, str(check / "capture.txt"), "")

    say("\n== 4. Type layouts ==")
    run("client-check", build_tool(a, "client-check", a.build, "--game", a.game, "--runtime", a.runtime),
        save=check / "client-check.txt", expected=(0, 1), marker="Type layouts")

    say("\n== 5. Catalog and raw comparison ==")
    cmd = py("frosty-capture-compare.py", collection, new, check / "comparison.json")
    if fresh:
        cmd += ["--baseline-catalog", str(fresh)]
    run("compare", cmd, save=check / "comparison.txt", expected=(0, 1), marker="Written:")
    if fresh:
        say("\nThe baseline's rebuilt-cache-only routes are compared separately. Exit 1 is expected here: every")
        say("route outside collection-fresh-cache counts as 'missing in baseline'.")
        run("compare fresh-cache", py("frosty-capture-compare.py", fresh, new, check / "comparison-fresh-cache.json"),
            save=check / "comparison-fresh-cache.txt", expected=(0, 1), marker="Written:")

    say("\n== 5b. Watched mutator values ==")
    # The new collection's catalog comes from a rebuilt cache and can give one file GUID to two
    # assets; the baseline's loaded-cache catalog, read first, decides those (2.1.2.5: MUT_CHIITest
    # and MUT_PVE).
    run("watched values", py("frosty-mutator-values.py", collection, new, "--descriptors", descriptors,
                             runtime_descriptors, "--catalog", collection / "asset-catalog.json"),
        save=check / "watched-values.md")

    say("\n== 5c. Hotfix check ==")
    cmd = py("frosty-hotfix-check.py", collection, new, "--out-dir", check / "hotfix-check",
             "--old-descriptors", descriptors, "--new-descriptors", runtime_descriptors)
    for extra in ([str(fresh)] if fresh else []) + a.old_extra:
        cmd += ["--old-extra", extra]
    for extra in a.new_extra:
        cmd += ["--new-extra", extra]
    if fresh:
        cmd += ["--old-catalog", str(fresh)]
    run("hotfix-check", cmd, save=check / "hotfix-check.txt", expected=(0, 1, 2))
    if not DRY and not (check / "hotfix-check" / "summary.json").is_file():
        STEPS[-1] = (*STEPS[-1][:3], "UNEXPECTED: no hotfix-check\\summary.json")

    say("\n== Summary ==")
    lines = [f"# Stage 1 summary: {check_name} (open build {a.build})", "", *summary_table(), "",
             "Exit codes that are results, not failures: client-check 1 (layouts differ), compare 1 (coverage",
             "incomplete), hotfix-check 1 (gameplay changed) or 2 (coverage incomplete).", ""]
    if DRY:
        lines += ["## Decision inputs (guide, Stage 1 step 6)", "",
                  "(dry run: read after the run from client-check.txt, comparison.json, comparison-fresh-cache.json,",
                  "watched-values.md and hotfix-check\\summary.json)"]
    else:
        lines += decision_inputs(check, identity, cache_note)
    for line in lines:
        say(line)
    target = check / "stage1-summary.md"
    say(("\nWOULD WRITE: " if DRY else "\nWRITTEN: ") + str(target))
    if not DRY:
        target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    say("\nStopped before the decision. Next: guide Stage 1 step 6 (hotfix, new build, or held); record comes after it.")
    return 1 if any(s[3].startswith("UNEXPECTED") for s in STEPS) else 0


def main():
    global DRY
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--datamining", default=argparse.SUPPRESS)
    common.add_argument("--game", default=argparse.SUPPRESS)
    common.add_argument("--runtime", default=argparse.SUPPRESS)
    common.add_argument("--date", default=argparse.SUPPRESS, help="yyyy-mm-dd (default today)")
    common.add_argument("--build", default=argparse.SUPPRESS, help="default: the open build")
    common.add_argument("--dry-run", action="store_true", default=argparse.SUPPRESS)
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, parents=[common])
    sub = ap.add_subparsers(dest="command", required=True)
    s0 = sub.add_parser("stage0", parents=[common])
    s0.add_argument("--force", action="store_true", help="run even when the need check says Stage 0 is not needed")
    s0.add_argument("--sights", action="store_true", help="run the sight-files export whatever its condition says")
    s0.add_argument("--client", help="client id in the folder name pre-update-<client>-<date> "
                                     "(default: the installed client's frostyArchiveHead)")
    s1 = sub.add_parser("stage1", parents=[common])
    s1.add_argument("--name", default="client-new", help="check folder is reports\\<name>-check-<date>")
    s1.add_argument("--previous-label", help="label in the renamed cache file name (default: the open build name)")
    s1.add_argument("--old-extra", action="append", default=[], help="extra baseline capture folder for the hotfix check")
    s1.add_argument("--new-extra", action="append", default=[], help="extra new capture folder for the hotfix check")
    a = ap.parse_args()
    a.datamining = getattr(a, "datamining", DM)
    a.game = getattr(a, "game", GAME)
    a.runtime = getattr(a, "runtime", str(Path(a.datamining) / RUNTIME))
    a.date = getattr(a, "date", datetime.date.today().isoformat())
    DRY = getattr(a, "dry_run", False)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
        sys.exit("--date must be yyyy-mm-dd")
    a.build = getattr(a, "build", None) or open_build(a)
    if not (Path(a.datamining) / "builds" / a.build / "BUILD.json").is_file():
        sys.exit(f"STOP: no BUILD.json for build {a.build} under {a.datamining}")
    sys.exit(stage0(a) if a.command == "stage0" else stage1(a))


if __name__ == "__main__":
    main()
