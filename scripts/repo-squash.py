"""Plan and apply the push-time squash for the BF6 repos without touching the working tree.

  python scripts/repo-squash.py plan <repo> [--gap-minutes 90 | --by-day] [--out plan.json]
  python scripts/repo-squash.py apply <plan.json>
  python scripts/repo-squash.py citations <plan.json> <repo> [<repo> ...]

plan: lists unpushed commits (origin/<branch>..<branch>, oldest first), classifies each as
  site (touches a site path) or research, and groups consecutive research commits into
  sessions (a gap longer than --gap-minutes starts a new session; --by-day starts one per
  calendar day instead, for parallel sessions whose commits interleave). Site commits stay single.
  Writes plan.json with a proposed message per research group; edit groups or messages there.
  A group's message ends with the union of its commits' Co-Authored-By trailers, so work
  from different agents keeps each agent's attribution.
apply: first re-checks the plan: origin/<branch> must still be the plan's base and an ancestor
  of the branch, the groups must list exactly the unpushed commits in order, each site group
  must be one site commit and no research group may contain a site commit. Then it rebuilds the unpushed history with git commit-tree from each group's final tree, so the
  new tip has exactly the old tip's tree and the working tree is never touched. Creates
  refs/backup/pre-squash-<timestamp> at the old tip, then moves the branch with a
  compare-and-swap update-ref (fails if anything was committed meanwhile). Records the
  old->new hash map in the plan file.
citations: after apply, searches tracked files of the given repos for any old squashed hash
  (7+ characters) and prints file:line with the replacement hash. It does not edit files.
"""
import datetime, json, os, re, subprocess, sys

SITE_PREFIXES = ("data/", "sim/", "ui/", "assets/", "schemas/", "vendor/")
SITE_FILES = ("index.html", "sitemap.xml", "ship-surface.json")
SITE_RE = re.compile(r"^v\d+\.\d+\.\d+\.\d+/")  # published archives
TRAILER_RE = re.compile(r"^co-authored-by:\s*(.+?)\s*$", re.I | re.M)

def git(repo, *args, env=None, input=None):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, encoding="utf-8",
                       env=env, input=input)
    if r.returncode:
        sys.exit(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout

def compress(leads):
    """L121, L122, L123, L125 -> L121-L123, L125 (suffixed ids stay single)."""
    out, run = [], []
    for lead in leads:
        n = int(lead[1:]) if lead[1:].isdigit() else None
        if n is not None and run and n == run[-1] + 1:
            run.append(n); continue
        if run: out.append(f"L{run[0]}" if len(run) == 1 else f"L{run[0]}-L{run[-1]}")
        run = [n] if n is not None else []
        if n is None: out.append(lead)
    if run: out.append(f"L{run[0]}" if len(run) == 1 else f"L{run[0]}-L{run[-1]}")
    return ", ".join(out)

def is_site(path):
    return path.startswith(SITE_PREFIXES) or path in SITE_FILES or bool(SITE_RE.match(path))

def is_site_commit(repo, sha):
    return any(is_site(f) for f in git(repo, "show", "--name-only", "--format=", sha).splitlines() if f)

def co_authors(repo, shas):
    """Co-Authored-By trailers of the given commits, deduplicated in first-seen order."""
    seen = {}
    for sha in shas:
        for m in TRAILER_RE.findall(git(repo, "show", "-s", "--format=%B", sha)):
            seen.setdefault(m.lower(), m)
    return [f"Co-Authored-By: {v}" for v in seen.values()]

def plan(repo, gap, out, by_day=False):
    branch = git(repo, "rev-parse", "--abbrev-ref", "HEAD").strip()
    upstream = f"origin/{branch}"
    git(repo, "fetch", "--quiet", "origin")
    merges = git(repo, "rev-list", "--merges", f"{upstream}..{branch}").split()
    if merges:
        sys.exit(f"Merge commits in the unpushed range ({len(merges)}); squash by hand.")
    shas = git(repo, "rev-list", "--reverse", f"{upstream}..{branch}").split()
    commits = []
    for sha in shas:
        meta = git(repo, "show", "-s", "--format=%H%x00%an%x00%ae%x00%aI%x00%s", sha).rstrip("\n").split("\x00")
        files = [f for f in git(repo, "show", "--name-only", "--format=", sha).splitlines() if f]
        commits.append({"sha": meta[0], "author": meta[1], "email": meta[2], "date": meta[3], "subject": meta[4],
                        "site": any(is_site(f) for f in files), "files": len(files)})
    groups, current = [], None
    for c in commits:
        when = datetime.datetime.fromisoformat(c["date"])
        if c["site"]:
            groups.append({"kind": "site", "commits": [c["sha"]], "subjects": [c["subject"]]}); current = None; continue
        same = (when.date() == current["_last"].date()) if (current and by_day) else             bool(current and (when - current["_last"]).total_seconds() <= gap * 60)
        if same:
            current["commits"].append(c["sha"]); current["subjects"].append(c["subject"]); current["_last"] = when
        else:
            current = {"kind": "research", "commits": [c["sha"]], "subjects": [c["subject"]], "_last": when,
                       "_first": when}
            groups.append(current)
    for g in groups:
        if g["kind"] == "research":
            leads = sorted({m for s in g["subjects"] for m in re.findall(r"\bL\d+[A-Z]?\b", s)},
                           key=lambda x: (int(re.sub(r"\D", "", x)), x))
            span = f"{g['_first']:%d %b %H:%M} to {g['_last']:%d %b %H:%M}"
            lead_text = f"leads {compress(leads)}" if leads else "research docs and tooling"
            trailers = co_authors(repo, g["commits"])
            g["message"] = (f"Research session {span}: {lead_text}\n\n"
                            + "\n".join(f"- {s}" for s in g["subjects"]) + "\n"
                            + ("\n" + "\n".join(trailers) + "\n" if trailers else ""))
            del g["_last"], g["_first"]
    data = {"repo": os.path.abspath(repo), "branch": branch, "upstream": upstream,
            "base": git(repo, "rev-parse", upstream).strip(), "oldTip": shas[-1] if shas else None,
            "groups": groups}
    json.dump(data, open(out, "w", encoding="utf-8"), indent=1)
    n_site = sum(g["kind"] == "site" for g in groups)
    print(f"{repo}: {len(commits)} unpushed commits -> {len(groups)} commits ({n_site} site kept, "
          f"{len(groups) - n_site} research sessions). Plan: {out}")
    for i, g in enumerate(groups, 1):
        first = g["message"].splitlines()[0] if g["kind"] == "research" else g["subjects"][0]
        print(f"{i:3}. {g['kind']:8} {len(g['commits']):3} commits  {first[:110]}")

def apply(plan_path):
    p = json.load(open(plan_path, encoding="utf-8"))
    repo = p["repo"]
    tip = git(repo, "rev-parse", p["branch"]).strip()
    if tip != p["oldTip"]:
        sys.exit("Branch moved since the plan was made; re-run plan.")
    git(repo, "fetch", "--quiet", "origin")
    if git(repo, "rev-parse", p["upstream"]).strip() != p["base"]:
        sys.exit(f"{p['upstream']} moved since the plan was made; re-run plan.")
    if subprocess.run(["git", "-C", repo, "merge-base", "--is-ancestor", p["base"], tip]).returncode:
        sys.exit(f"{p['upstream']} is not an ancestor of {p['branch']}; squashing would rewrite pushed commits.")
    unpushed = git(repo, "rev-list", "--reverse", f"{p['base']}..{tip}").split()
    if git(repo, "rev-list", "--merges", f"{p['base']}..{tip}").split():
        sys.exit("Merge commits in the unpushed range; squash by hand.")
    if [c for g in p["groups"] for c in g["commits"]] != unpushed:
        sys.exit("The plan's groups do not list exactly the unpushed commits, in order; fix the plan or re-run it.")
    for i, g in enumerate(p["groups"], 1):
        site = [c for c in g["commits"] if is_site_commit(repo, c)]
        if g["kind"] == "site" and (len(g["commits"]) != 1 or not site):
            sys.exit(f"Group {i}: a site group must be exactly one site commit.")
        if g["kind"] == "research" and site:
            sys.exit(f"Group {i}: research group contains site commit {site[0][:10]}; site commits stay single.")
        if g["kind"] not in ("site", "research"):
            sys.exit(f"Group {i}: unknown kind {g['kind']!r}.")
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    git(repo, "update-ref", f"refs/backup/pre-squash-{stamp}", tip)
    parent, mapping = p["base"], {}
    for g in p["groups"]:
        last = g["commits"][-1]
        meta = git(repo, "show", "-s", "--format=%an%x00%ae%x00%aI%x00%cn%x00%ce%x00%cI%x00%B", last).split("\x00")
        env = dict(os.environ, GIT_AUTHOR_NAME=meta[0], GIT_AUTHOR_EMAIL=meta[1], GIT_AUTHOR_DATE=meta[2],
                   GIT_COMMITTER_NAME=meta[3], GIT_COMMITTER_EMAIL=meta[4], GIT_COMMITTER_DATE=meta[5])
        message = meta[6] if g["kind"] == "site" else g["message"]
        tree = git(repo, "rev-parse", f"{last}^{{tree}}").strip()
        new = git(repo, "commit-tree", tree, "-p", parent, env=env, input=message).strip()
        for old in g["commits"]:
            mapping[old] = new
        parent = new
    if git(repo, "rev-parse", f"{parent}^{{tree}}").strip() != git(repo, "rev-parse", f"{tip}^{{tree}}").strip():
        sys.exit("New tip tree differs from the old tip; branch not moved.")
    git(repo, "update-ref", f"refs/heads/{p['branch']}", parent, tip)
    p["backupRef"], p["newTip"], p["hashMap"] = f"refs/backup/pre-squash-{stamp}", parent, mapping
    json.dump(p, open(plan_path, "w", encoding="utf-8"), indent=1)
    print(f"Rebuilt {len(mapping)} commits as {len(p['groups'])}; tree identical. New tip {parent[:10]}; "
          f"backup {p['backupRef']}.")
    print(git(repo, "log", "--oneline", f"{p['upstream']}..{p['branch']}"))

def citations(plan_path, repos):
    p = json.load(open(plan_path, encoding="utf-8"))
    mapping = {old: new for old, new in p.get("hashMap", {}).items() if old != new}
    if not mapping:
        sys.exit("No hash map; run apply first.")
    found = 0
    for repo in repos:
        for old, new in mapping.items():
            r = subprocess.run(["git", "-C", repo, "grep", "-n", "-I", "-E", rf"\b{old[:7]}[0-9a-f]{{0,33}}\b"],
                               capture_output=True, text=True, encoding="utf-8")
            for line in r.stdout.splitlines():
                found += 1
                print(f"{repo}: {line[:160]}\n    {old[:10]} -> {new[:10]}")
    print(f"{found} citation lines to update." if found else "No citations of squashed hashes found.")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "plan":
        a = sys.argv[2:]; gap, out = 90, "plan.json"
        by_day = "--by-day" in a
        if by_day: a.remove("--by-day")
        if "--gap-minutes" in a: i = a.index("--gap-minutes"); gap = int(a[i + 1]); del a[i:i + 2]
        if "--out" in a: i = a.index("--out"); out = a[i + 1]; del a[i:i + 2]
        plan(a[0], gap, out, by_day)
    elif cmd == "apply":
        apply(sys.argv[2])
    elif cmd == "citations":
        citations(sys.argv[2], sys.argv[3:])
    else:
        sys.exit(__doc__)
