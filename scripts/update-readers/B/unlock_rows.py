"""List WeaponUnlocks config rows (CT_GLA_*) for ammunition, grouped by weapon. Writes unlock_rows.json:
{internal weapon: {row label: [config, hash, value]}}. A row object has Field_0c59fa06 'U_<weapon> - <slot> - <label>'."""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import json, pathlib, collections, sys
import common as c
HERE = settings.part("B")
out = collections.defaultdict(dict); slots = collections.Counter()
for k in sorted(c.held):
    base = k.rsplit("/", 1)[-1]
    if "/gameconfigurations/ct_gla_" in k and not base.endswith("_valueregistry"):
        objs, _ = c.load(k)
        for o in objs:
            n = o.get("Field_0c59fa06")
            if isinstance(n, str) and n.startswith("U_") and " - " in n:
                parts = n[2:].split(" - ")
                slots[parts[1] if len(parts) > 1 else "?"] += 1
                if len(parts) >= 3 and parts[1] in ("AMO", "AMMO", "Ammo"):
                    v = {kk: vv for kk, vv in o.items() if kk not in ("Field_0c59fa06", "$class", "$guid")}
                    out[parts[0]][" - ".join(parts[2:])] = [c.proper[k].rsplit("/", 1)[-1], json.dumps(v)[:200]]
print(dict(slots))
json.dump(out, open(HERE / "unlock_rows.json", "w", encoding="utf-8"), indent=1)
for w in sorted(out):
    if len(sys.argv) < 2 or w in sys.argv[1:]:
        print(w, {k: v[0][7:] for k, v in out[w].items()})
