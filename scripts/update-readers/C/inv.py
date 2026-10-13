"""Inventory of held routes for the new weapons and for attachment UI metadata."""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import pathlib, collections, sys
held = {r: (pathlib.Path(p).parents[0].name, p) for p, r in settings.held_routes().values()}
for w in ("AssaultRifle/MRGGA", "BoltAction/CDX40", "MG/PKM", "SMG/RSAR999", "Carbine/M4A1"):
    rs = [(r, v[0]) for r, v in held.items() if ("/weapons/" + w + "/").lower() in r.lower()]
    print("==", w, len(rs), collections.Counter(v for _, v in rs))
    print("  attachments", sum("/attachment_" in r.lower() for r, _ in rs), "prg", sum("/u_prg_" in r.lower() for r, _ in rs))
    print("  other:", sorted(r.rsplit("/", 1)[-1] + ("*" if v != "main" else "") for r, v in rs if "/attachment_" not in r.lower() and "/u_prg_" not in r.lower()))
c = collections.Counter()
for r in held:
    rl = r.lower()
    if "metadata/attachments" in rl:
        c[rl.split("/")[5] if len(rl.split("/")) > 6 else "(root)"] += 1
print(len(c), sum(c.values()), dict(c))
for r, v in held.items():
    rl = r.lower()
    if any(k in rl for k in sys.argv[1:]) and "/hardware/weapons/" not in rl:
        print(v[0][:12], r)
