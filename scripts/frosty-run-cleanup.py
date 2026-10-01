r"""Find and (optionally) clean up disk clutter in a closed research run folder.

  python scripts/frosty-run-cleanup.py <run folder>            report only; writes cleanup-plan.json
  python scripts/frosty-run-cleanup.py <run folder> --apply    apply the reviewed cleanup-plan.json; writes cleanup.json

Finds: junctions/symbolic links (removed as links, never following them); asset-catalog.json
copies (candidates unless cited); files over 50 MB (candidates unless cited). "Cited" means the
file's name with its parent folder, its full path, or its SHA-256 appears in tracked files of
either repo, or in any BUILD.json/MANIFEST.tsv. A failed citation search stops the script rather
than counting as "not cited". Refuses paths under builds\*\capture, builds\*\xml or toolchain
folders.

--apply does not re-plan: it acts only on the links and files in the reviewed cleanup-plan.json.
Before each action it re-checks that the link is still a link, and that the file has the planned
size and hash and is still uncited; any difference stops the script.
"""
import argparse, datetime, hashlib, json, os, subprocess, sys
from pathlib import Path

RESEARCH = Path(__file__).resolve().parent.parent
REPOS = [str(RESEARCH), str(RESEARCH.parent / "BF6 Weapon Analyzer")]
BUILDS = r"C:\Users\royal\Documents\BF6 Datamining\builds"
LIMIT = 50 * 1024 * 1024

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("run")
ap.add_argument("--apply", action="store_true")
ap.add_argument("--builds", default=BUILDS)
a = ap.parse_args()
run = os.path.abspath(a.run)
low = run.lower().replace("/", "\\")
if "\\builds\\" in low and ("\\capture" in low or "\\xml" in low) or "toolchain" in low:
    sys.exit("Refusing a protected folder.")
plan_path = os.path.join(run, "cleanup-plan.json")

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

def is_link(p):
    try:
        return os.path.islink(p) or bool(os.lstat(p).st_file_attributes & 0x400)  # reparse point
    except (AttributeError, OSError):
        return os.path.islink(p)

def cited(path, digest):
    rel = os.path.relpath(path, os.path.dirname(os.path.dirname(path)))  # parent\name
    terms = [path, path.replace("\\", "/"), path.replace("\\", "\\\\"), rel, rel.replace("\\", "/"), digest]
    for repo in REPOS:
        for t in terms:
            r = subprocess.run(["git", "-C", repo, "grep", "-l", "-I", "-F", t], capture_output=True, text=True)
            if r.returncode not in (0, 1):  # 1 = no match; anything else is a failed search
                sys.exit(f"STOP: citation search failed in {repo} ({r.returncode}): {r.stderr.strip()[:300]}")
            if r.returncode == 0:
                return f"{repo}: {r.stdout.splitlines()[0]}"
    for b in os.listdir(a.builds):
        for meta in ("BUILD.json", "MANIFEST.tsv"):
            mp = os.path.join(a.builds, b, meta)
            if os.path.exists(mp):
                text = open(mp, encoding="utf-8", errors="ignore").read()
                if digest in text:
                    return mp
    return None

if not a.apply:
    links, files = [], []
    for root, dirs, names in os.walk(run):
        for d in list(dirs):
            full = os.path.join(root, d)
            if is_link(full):
                links.append(full); dirs.remove(d)
        for n in names:
            full = os.path.join(root, n)
            if is_link(full):
                links.append(full); continue
            size = os.path.getsize(full)
            if n.lower() == "asset-catalog.json" or size > LIMIT:
                files.append((full, size))
    plan = {"run": run, "createdUtc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "links": links, "delete": [], "keep": []}
    for p, size in files:
        d = sha(p)
        c = cited(p, d)
        (plan["keep"] if c else plan["delete"]).append({"path": p, "bytes": size, "sha256": d, **({"citedBy": c} if c else {})})
    print(f"Links: {len(links)}")
    for l in links: print("  link:", l)
    print(f"Delete candidates: {len(plan['delete'])}, {sum(x['bytes'] for x in plan['delete'])/1e9:.2f} GB")
    for x in plan["delete"]: print(f"  {x['bytes']/1e6:9.1f} MB  {x['path']}")
    print(f"Kept (cited): {len(plan['keep'])}")
    for x in plan["keep"]: print(f"  {x['bytes']/1e6:9.1f} MB  {x['path']}  <- {x['citedBy']}")
    json.dump(plan, open(plan_path, "w", encoding="utf-8"), indent=1)
    print(f"Plan: {plan_path}. Re-run with --apply after the operator (or the run's cleanup rule) approves it.")
    sys.exit(0)

if not os.path.exists(plan_path):
    sys.exit("No cleanup-plan.json; run without --apply first and review it.")
plan = json.load(open(plan_path, encoding="utf-8"))
if os.path.normcase(plan["run"]) != os.path.normcase(run):
    sys.exit(f"STOP: the plan is for {plan['run']}, not {run}.")
for l in plan["links"]:
    if not is_link(l):
        sys.exit(f"STOP: no longer a link, not touching it: {l}")
for x in plan["delete"]:
    if not os.path.exists(x["path"]) or os.path.getsize(x["path"]) != x["bytes"] or sha(x["path"]) != x["sha256"]:
        sys.exit(f"STOP: changed since planning: {x['path']}")
    c = cited(x["path"], x["sha256"])
    if c:
        sys.exit(f"STOP: cited since planning: {x['path']} <- {c}")

done = {"run": run, "plan": plan_path, "planCreatedUtc": plan["createdUtc"],
        "appliedUtc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "linksRemoved": [], "deleted": [], "kept": plan["keep"]}
for l in plan["links"]:
    if os.path.isdir(l) and not os.path.islink(l):
        os.rmdir(l)            # removes a junction itself; the target is untouched
    else:
        os.unlink(l)
    done["linksRemoved"].append(l)
for x in plan["delete"]:
    if x["path"].lower().endswith("asset-catalog.json"):
        with open(os.path.join(os.path.dirname(x["path"]), "asset-catalog.removed.json"), "w", encoding="utf-8") as f:
            json.dump({"removedSha256": x["sha256"], "removedBytes": x["bytes"],
                       "reason": "Targeted-capture catalog copy not cited; removed at run cleanup",
                       "record": "cleanup.json in the run folder"}, f, indent=1)
    os.remove(x["path"])
    done["deleted"].append(x)
json.dump(done, open(os.path.join(run, "cleanup.json"), "w", encoding="utf-8"), indent=1)
print(f"Removed {len(done['linksRemoved'])} links and {len(done['deleted'])} files; recorded in cleanup.json.")
