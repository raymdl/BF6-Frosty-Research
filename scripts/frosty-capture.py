"""Capture raw EBX routes from the installed game into the open build, one Frosty process at a time.

  python scripts/frosty-capture.py <name> <route> [<route> ...] [--catalog] [--build 1.4.3.0]
  python scripts/frosty-capture.py <name> --routes-file <file> [--catalog] [--build 1.4.3.0]
  python scripts/frosty-capture.py <name> --into capture/pre-update-<client>-<date>/collection --catalog --routes-file <file>
  python scripts/frosty-capture.py <name> --into reports/<client>-check-<date>/collection --catalog --routes-file <file> --update-check

Steps: take an exclusive lock (<datamining>/.frosty-capture.lock, released by the OS when this
process exits) so two captures started through this script cannot overlap; refuse if a FrostyCmd
or frosty-collect-raw.ps1 process is already running (catches captures started by hand); run
frosty-build.py guard; run frosty-collect-raw.ps1 into builds/<build>/reports/<name>/ (or
builds/<build>/<--into>), a new folder that is never reused; print the per-route status; run
frosty-build.py record. Exits non-zero if the lock, process check, guard, collector or record fails.

--catalog writes the full 110 MB catalog (build and hotfix captures only).
--update-check is for the Stage 1 capture after a game update: guard is expected to fail on the
new client, so it is skipped, and record is left to the update procedure after its decision.
"""
import argparse, json, msvcrt, os, subprocess, sys
from pathlib import Path

RESEARCH = Path(__file__).resolve().parent.parent
DM = r"C:\Users\royal\Documents\BF6 Datamining"
GAME = r"C:\Program Files\EA Games\Battlefield 6"
RUNTIME = r"FrostyToolsuite-battlefield6\FrostyEditor\bin\Release\Final"
COLLECTOR = RESEARCH.parent / "BF6 Weapon Analyzer" / "scripts" / "frosty-collect-raw.ps1"

BUSY_PS = ("$p = @(Get-Process FrostyCmd -ErrorAction SilentlyContinue) + @(Get-CimInstance Win32_Process "
           "-Filter \"Name='powershell.exe'\" | Where-Object { $_.ProcessId -ne $PID -and "
           "$_.CommandLine -match '-File\\s+\"?[^\"]*frosty-collect-raw\\.ps1' }); $p.Count")

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("name", help="capture name, <topic>-<yyyy-mm-dd>; the folder under reports/ unless --into is given")
ap.add_argument("routes", nargs="*")
ap.add_argument("--routes-file")
ap.add_argument("--catalog", action="store_true")
ap.add_argument("--build", default="1.4.3.0")
ap.add_argument("--into", help="output folder relative to builds/<build>/ (default reports/<name>)")
ap.add_argument("--update-check", action="store_true", help="Stage 1 capture: skip guard and record")
ap.add_argument("--datamining", default=DM)
ap.add_argument("--game", default=GAME)
ap.add_argument("--collector", default=str(COLLECTOR))
a = ap.parse_args()

routes = list(a.routes)
if a.routes_file:
    routes = [l.strip() for l in open(a.routes_file, encoding="utf-8-sig") if l.strip()] + routes
if not routes and not a.catalog:
    sys.exit("Nothing to capture: give routes or --catalog.")
if a.update_check and not a.catalog:
    sys.exit("--update-check needs --catalog: the update comparison reads the catalog.")

build_dir = Path(a.datamining) / "builds" / a.build
out = (build_dir / (a.into or Path("reports") / a.name)).resolve()
if build_dir.resolve() not in out.parents:
    sys.exit(f"STOP: {out} is not inside {build_dir}.")
if out.exists():
    sys.exit(f"STOP: {out} exists. Use a new capture name.")

lock = open(Path(a.datamining) / ".frosty-capture.lock", "a+")
try:
    msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
except OSError:
    sys.exit("STOP: another frosty-capture.py is running. Only one Frosty process at a time.")

busy = subprocess.run(["powershell", "-NoProfile", "-Command", BUSY_PS], capture_output=True, text=True)
if busy.returncode or not busy.stdout.strip().isdigit():
    sys.exit(f"STOP: the process check failed: {busy.stderr.strip()[:500]}")
if busy.stdout.strip() != "0":
    sys.exit(f"STOP: {busy.stdout.strip()} Frosty process(es) already running. Only one Frosty process at a time.")

def build_tool(*args):
    return subprocess.run([sys.executable, "scripts/frosty-build.py", "--datamining", a.datamining, *args],
                          cwd=RESEARCH, capture_output=True, text=True)

if not a.update_check:
    guard = build_tool("guard", a.build, "--game", a.game)
    print(guard.stdout.strip() or guard.stderr.strip())
    if guard.returncode:
        sys.exit("STOP: guard failed. The game may have updated: run the game update check first.")

out.mkdir(parents=True)
cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", a.collector,
       "-FrostyDirectory", str(Path(a.datamining) / RUNTIME), "-GamePath", a.game, "-OutputDirectory", str(out)]
if routes:
    routes_txt = out / "routes.txt"
    routes_txt.write_text("\n".join(routes) + "\n", encoding="ascii")
    cmd += ["-RoutesFile", str(routes_txt)]
if a.catalog:
    cmd.append("-Catalog")
run = subprocess.run(cmd, capture_output=True, text=True)
if run.returncode:
    print(run.stdout[-2000:], run.stderr[-2000:])
    sys.exit("Collector failed; see output above. Check for a stuck FrostyCmd/powershell process.")

status = out / "raw-status.jsonl"
ok = bad = 0
if status.exists():
    for line in open(status, encoding="utf-8-sig"):
        r = json.loads(line)
        if r["status"] == "success":
            ok += 1
        else:
            bad += 1; print(f"  FAILED {r['path']}: {r['reason']}")
print(f"Captured {ok} routes, {bad} failed -> {out}")
ident = out / "capture-identity.json"
if ident.exists():
    print("Identity:", ident.read_text(encoding="utf-8-sig").strip())

if a.update_check:
    print("Update check: record skipped; record after the hotfix/new-build decision.")
    sys.exit(0)
rec = build_tool("record", a.build)
print(rec.stdout.strip().splitlines()[-1] if rec.stdout.strip() else rec.stderr.strip())
if rec.returncode:
    sys.exit("STOP: record failed; the capture is on disk but not in the manifest. Run verify and investigate.")
