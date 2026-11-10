"""Check an update checklist's Site column against the Analyzer site data.

python -I scripts/checklist-site-check.py docs/updates/<version>-checklist.md --site "<Analyzer repo>"
    [--checks docs/updates/<version>-site-checks.json]

The checklist is the one source for each row's site status: the last cell of every table whose
header ends in "Site". A row whose Site cell says "Not applicable" or "Not applied" is listed
with its reason. Every other row must have checks in the checks file (default: the checklist
name with "-site-checks.json" in place of "-checklist.md"), and every check must hold.

Checks file: {"<row id>": [check, ...]}. A check is {"file": "<data/... json>", "path": "...",
then one of:
  "eq": value           the value at the path (numbers within 1e-9, or 1e-6 relative)
  "absent": true        the path does not exist
  "includes": value     the list at the path contains the value (a list of values: all of them)
  "excludes": value     the list at the path does not contain the value
  "contains" / "lacks": text   the string at the path contains / does not contain the text
  "count": n with "includes" or "contains", and a "*" segment in the path: n of the matched
                        values hold it
Paths are dot-separated keys, or a JSON list of keys when a key holds a dot; "key[f=x]" picks
the object whose field f is x from a list ("[id=x]" at the root), a number indexes a list, and
"*" matches every key of an object. Availability is an "includes" or
"excludes" check on the weapon's list (attachments.json WEAPON_ATTS.<weapon>.<slot>,
WEAPON_MAG.<weapon>.mags, WEAPON_ERGO.<weapon>.avail, ammo.json WEAPON_AMMO.<weapon>.ammo).

Exit 0 when every applied row has checks and all hold; 1 otherwise.
"""
import argparse, json, re, sys
from pathlib import Path

ROW = re.compile(r"^\|\s*([A-Z]\d+)\s*\|")
SEG = re.compile(r"^([^\[\]]*)(?:\[(\w+)=([^\]]+)\])?$")
MISSING = object()


def site_rows(md):
    rows, site_table = {}, False
    for line in md.splitlines():
        if line.startswith("|") and not ROW.match(line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and not set("".join(cells)) <= set("-: "):
                site_table = cells[-1] == "Site"
            continue
        m = ROW.match(line)
        if m and site_table:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows[m.group(1)] = cells[-1]
        elif not line.startswith("|"):
            site_table = False
    return rows


def status(cell):
    low = cell.replace("**", "").strip().lower()
    if low.startswith(("not applicable", "not applied")):
        return "not"
    if "applied" in low:
        return "partly" if low.startswith("partly") or "not applied" in low else "applied"
    return "unknown"


def resolve(node, path):
    nodes = [node]
    parts = path if isinstance(path, list) else [p for p in re.split(r"\.(?![^\[]*\])", path) if p]
    for part in parts:
        m = SEG.match(part)
        if not m:
            raise ValueError(f"bad path segment {part!r}")
        key, field, ident = m.groups()
        out = []
        for n in nodes:
            if n is MISSING:
                out.append(MISSING); continue
            if key == "*":
                out.extend(n.values() if isinstance(n, dict) else [MISSING]); continue
            if key and isinstance(n, list) and key.isdigit():
                n = n[int(key)] if int(key) < len(n) else MISSING
            elif key:
                n = n.get(key, MISSING) if isinstance(n, dict) else MISSING
            if ident is not None:
                n = next((x for x in n if isinstance(x, dict) and str(x.get(field)) == ident), MISSING) \
                    if isinstance(n, list) else MISSING
            out.append(n)
        nodes = out
    return nodes


def same(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) <= max(1e-9, 1e-6 * abs(b))
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    return a == b


def run_check(site, c):
    data = site(c["file"])
    vals = resolve(data, c["path"])
    wild = "*" in c["path"]
    if "count" in c:
        if "contains" in c:
            n = sum(isinstance(v, str) and c["contains"] in v for v in vals)
        else:
            n = sum(isinstance(v, list) and c["includes"] in v for v in vals)
        return n == c["count"], f"{n} match"
    if c.get("absent"):
        return all(v is MISSING for v in vals), "present" if any(v is not MISSING for v in vals) else "absent"
    if any(v is MISSING for v in vals):
        return False, "path not found"
    if "eq" in c:
        ok = all(same(v, c["eq"]) for v in vals)
        return ok, json.dumps(vals if wild else vals[0])[:200]
    if "includes" in c:
        want = c["includes"] if isinstance(c["includes"], list) else [c["includes"]]
        miss = [w for v in vals for w in want if not (isinstance(v, (list, dict)) and w in v)]
        return not miss, f"missing {miss}" if miss else "included"
    if "contains" in c or "lacks" in c:
        ok = all(isinstance(v, str) and ("contains" not in c or c["contains"] in v)
                 and ("lacks" not in c or c["lacks"] not in v) for v in vals)
        return ok, json.dumps(vals[0])[:200]
    if "excludes" in c:
        return all(c["excludes"] not in v for v in vals), "excluded" if all(c["excludes"] not in v for v in vals) else "present"
    raise ValueError(f"check has no expectation: {c}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("checklist")
    ap.add_argument("--site", required=True, help="Analyzer repository root")
    ap.add_argument("--checks")
    a = ap.parse_args()
    md_path = Path(a.checklist)
    checks_path = Path(a.checks) if a.checks else md_path.with_name(md_path.name.replace("-checklist.md", "-site-checks.json"))
    rows = site_rows(md_path.read_text(encoding="utf-8"))
    checks = json.loads(checks_path.read_text(encoding="utf-8"))
    cache = {}

    def site(f):
        if f not in cache:
            cache[f] = json.loads((Path(a.site) / f).read_text(encoding="utf-8"))
        return cache[f]

    bad, ok_n, not_rows = [], 0, []
    for rid, cell in rows.items():
        st = status(cell)
        if st == "not":
            not_rows.append((rid, cell)); continue
        if st == "unknown":
            bad.append(f"{rid}: Site cell not recognised: {cell[:100]}"); continue
        if st == "partly":
            not_rows.append((rid, cell))
        if not checks.get(rid):
            bad.append(f"{rid}: applied but has no checks"); continue
        for c in checks[rid]:
            try:
                ok, got = run_check(site, c)
            except Exception as e:
                ok, got = False, f"{type(e).__name__}: {e}"
            if ok:
                ok_n += 1
            else:
                bad.append(f"{rid}: {c['file']} {c['path']}: {got} (check {json.dumps({k: v for k, v in c.items() if k not in ('file', 'path')})})")
    for rid in sorted(set(checks) - set(rows)):
        bad.append(f"{rid}: checks for a row the checklist does not have")

    print(f"{len(rows)} rows with a Site cell; {ok_n} checks passed; {len(bad)} problems.")
    for b in bad:
        print("FAIL", b)
    print("\nNot on the site (not applied, not applicable, or partly applied):")
    for rid, cell in not_rows:
        print(f"  {rid}: {cell}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
