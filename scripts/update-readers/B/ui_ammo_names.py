"""UI metadata records for ammunition of the four new weapons (and any record whose label holds an argument substring).
Prints every string-id field resolved against fs_us_loc. Read-only."""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import sys, json, re
import common as c
strings = {}
for l in open(c.BUILD / "capture/fs_us_loc.strings.tsv", encoding="utf-8", errors="replace"):
    p = l.rstrip("\n").split("\t", 1)
    if len(p) == 2:
        strings[p[0].upper()] = p[1]
subs = [s.lower() for s in sys.argv[1:]]
if not subs:   # default: the attachment ids (Field_de6f63b3) of the new weapons' ammunition records, signed and unsigned
    import pathlib
    d = json.load(open(settings.part("B") / "derived.json", encoding="utf-8"))
    label = {}
    for wid in ("mk24", "elr40", "z84m", "rspr"):
        for a in d["weapons"][wid]["ammo"]:
            for v in (a["id"], a["id"] - (1 << 32)):
                label[str(v)] = a["attachment"]
    subs = list(label)
    print("searching for", len(subs) // 2, "attachment ids")
for k in sorted(c.held):
    if "/ui/" in k and "attachmentmetadata" in k:
        objs, _ = c.load(k)
        for o in objs:
            blob = json.dumps(o)
            low = blob.lower()
            if any(s in low for s in subs):
                ids = {}
                def walk(x, path):
                    if isinstance(x, dict):
                        for kk, v in x.items():
                            walk(v, path + "/" + kk[-8:])
                    elif isinstance(x, list):
                        for i, v in enumerate(x):
                            walk(v, path + "[%d]" % i)
                    elif isinstance(x, int) and not isinstance(x, bool):
                        h = "%08X" % (x & 0xFFFFFFFF)
                        if h in strings:
                            ids[path] = (h, strings[h][:110])
                    elif isinstance(x, str) and len(x) < 120 and not path.endswith("$guid") and not path.endswith("$class"):
                        ids[path] = x
                walk(o, "")
                print(c.proper[k].rsplit("/", 1)[-1], json.dumps(ids)[:700])
