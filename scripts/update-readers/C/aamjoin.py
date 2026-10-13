"""Test for a hard join between Attachment records and AAM records: does the attachment's id
(Field_de6f63b3) occur among the AAM record's lookup keys (Field_1636b8bd)?
python aamjoin.py <folder under weapons> <stem>   e.g. SMG/RSAR999 RSAR999"""
import sys, re
from rawlib import *
folder, stem = sys.argv[1], sys.argv[2]
base = "common/hardware/weapons/" + folder.lower() + "/"
aam = load(base + "aam_" + stem.lower())[0]
recs = [o for o in aam if o["$class"] == "Class_ccf7da47"]
bykey = collections.defaultdict(list)
for o in recs:
    for i, k in enumerate(o.get("Field_1636b8bd") or []):
        bykey[k & 0xFFFFFFFF].append((i, o))
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
hit = miss = 0
pos = collections.Counter()
for r in sorted(k for k in held if k.startswith(base + "attachment_")):
    a = load(r)[0][0]
    k = a["Field_de6f63b3"] & 0xFFFFFFFF
    m = bykey.get(k, [])
    if m:
        hit += 1
        for i, o in m: pos[i] += 1
    else:
        miss += 1
    if len(sys.argv) > 3 or not m:
        print("%-40s %-10s -> %s" % (r.rsplit("/", 1)[-1][len("attachment_" + stem) + 1:], k, [(i, o["Field_55aded8d"]) for i, o in m]))
print("attachments", hit + miss, "joined", hit, "unjoined", miss, "key positions", dict(pos), "AAM records", len(recs))
