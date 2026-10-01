"""Re-read the raw bytes cited by research receipts and report mismatches.

Usage:
  python .claude/skills/review-frosty-research/review-rawcheck.py <receipt glob> [<receipt glob> ...] [--per-receipt 60]

Example:
  python .claude/skills/review-frosty-research/review-rawcheck.py "C:/Users/royal/Documents/BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3*.json"

Every object in a receipt that has path, offset and bytesHex is a raw check. The script
re-reads those bytes from the cited file (sampling at most --per-receipt per receipt),
compares them, and also compares the recorded f32 value with the bytes. Read-only.
"""
import glob, json, os, random, struct, sys

args = sys.argv[1:]
per = 60
if "--per-receipt" in args:
    i = args.index("--per-receipt"); per = int(args[i + 1]); del args[i:i + 2]
files = sorted({f for pattern in args for f in glob.glob(pattern)})
if not files:
    sys.exit("No receipts matched.")

random.seed(1)
total = byte_bad = value_bad = missing = 0
problems = []
for fn in files:
    found = set()
    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get("offset"), int) and isinstance(o.get("bytesHex"), str) and isinstance(o.get("path"), str):
                found.add((o["path"], o["offset"], o["bytesHex"].lower(), o.get("type"),
                           o.get("value") if isinstance(o.get("value"), (int, float)) else None))
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(json.load(open(fn, encoding="utf-8")))
    checks = sorted(found, key=str)
    sample = checks if len(checks) <= per else random.sample(checks, per)
    for path, off, hx, typ, val in sample:
        if not os.path.exists(path):
            missing += 1; problems.append((os.path.basename(fn), "missing file", path)); continue
        with open(path, "rb") as f:
            f.seek(off); got = f.read(len(hx) // 2).hex()
        total += 1
        if got != hx:
            byte_bad += 1; problems.append((os.path.basename(fn), "bytes differ", f"{os.path.basename(path)} @{off}: {hx} vs {got}"))
        elif typ == "f32" and val is not None and len(hx) == 8:
            v = struct.unpack("<f", bytes.fromhex(hx))[0]
            if abs(v - val) > 1e-4 * max(1.0, abs(val)):
                value_bad += 1; problems.append((os.path.basename(fn), "value differs", f"{os.path.basename(path)} @{off}: recorded {val}, bytes {v}"))
    print(f"{os.path.basename(fn)}: {len(checks)} raw checks, {len(sample)} sampled")

print(f"\nReceipts {len(files)}; re-read {total}; byte mismatches {byte_bad}; f32 value mismatches {value_bad}; missing files {missing}")
for p in problems[:25]:
    print("  ", *p)
