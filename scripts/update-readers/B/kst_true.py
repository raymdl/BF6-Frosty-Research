"""Rows stored true in KST_CH2_S1_Weapons (grouped by the part after the weapon name)."""
import collections, re
import common as c
objs, _ = c.load("Common/GameSetup/Tweakables/Killswitches/KST_CH2_S1_Weapons")
t = collections.Counter(); n = 0
for o in objs:
    name = o.get("Field_0c59fa06")
    if isinstance(name, str) and "Field_42c8b257" in o:
        n += 1
        if c.unbox(o["Field_42c8b257"]):
            m = re.match(r"U_PRG_([A-Za-z0-9]+)_(.*)", name)
            t[m.group(2) if m else name] += 1
print("rows", n, "true", dict(t))
