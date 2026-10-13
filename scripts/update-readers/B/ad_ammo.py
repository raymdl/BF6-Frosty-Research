"""Shared UI ammunition descriptors (Common/UI/Static/Metadata/Attachments/Shared/AD_Ammo_*): resolved name and
description strings. Lists catalog routes that are not held."""
import common as c
S = {}
for l in open(c.BUILD / "capture/fs_us_loc.strings.tsv", encoding="utf-8", errors="replace"):
    p = l.rstrip("\n").split("\t", 1)
    if len(p) == 2:
        S[p[0].upper()] = p[1]
ps = sorted(p for g, p in c.byguid.items() if "/ad_ammo" in p.lower() or "/ad_amo" in p.lower())
for p in ps:
    if p.lower() not in c.held:
        print(p, "NOT HELD"); continue
    o, _ = c.load(p)
    out = []

    def w(x):
        if isinstance(x, dict):
            for v in x.values(): w(v)
        elif isinstance(x, list):
            for v in x: w(v)
        elif isinstance(x, int) and not isinstance(x, bool) and ("%08X" % (x & 0xFFFFFFFF)) in S:
            out.append(("%08X" % (x & 0xFFFFFFFF), S["%08X" % (x & 0xFFFFFFFF)][:110]))
    w(o)
    print(p.rsplit("/", 1)[-1], out)
