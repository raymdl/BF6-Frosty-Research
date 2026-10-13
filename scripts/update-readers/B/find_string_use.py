"""python find_string_use.py <8-hex string id> [route filter]: objects in held UI metadata files that hold this string id;
prints all string ids of the object resolved."""
import sys, json
import common as c
strings = {}
for l in open(c.BUILD / "capture/fs_us_loc.strings.tsv", encoding="utf-8", errors="replace"):
    p = l.rstrip("\n").split("\t", 1)
    if len(p) == 2:
        strings[p[0].upper()] = p[1]
target = int(sys.argv[1], 16); flt = (sys.argv[2] if len(sys.argv) > 2 else "metadata").lower()
needles = (str(target), str(target - (1 << 32)))
for k in sorted(c.held):
    if flt in k:
        try:
            objs, _ = c.load(k)
        except Exception as e:
            continue
        for i, o in enumerate(objs):
            blob = json.dumps(o)
            if any(n in blob for n in needles):
                found = []
                def walk(x, path):
                    if isinstance(x, dict):
                        for kk, v in x.items():
                            walk(v, path + "/" + kk[-8:])
                    elif isinstance(x, list):
                        for j, v in enumerate(x[:12]):
                            walk(v, path + "[%d]" % j)
                    elif isinstance(x, int) and not isinstance(x, bool):
                        h = "%08X" % (x & 0xFFFFFFFF)
                        if h in strings:
                            found.append((path, h, strings[h][:100]))
                    elif isinstance(x, str) and len(x) < 100 and "$" not in path[-7:]:
                        found.append((path, x))
                walk(o, "")
                print(c.proper[k].rsplit("/", 1)[-1], "obj", i, o["$class"], json.dumps(found)[:900])
