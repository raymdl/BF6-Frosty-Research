"""Magazine attachments of the four new weapons from <run>/uncaptured/attgraph.json: in-game name, cost, capacity set by the package."""
import json
import lib
j = json.load(open(lib.RUN / "uncaptured/attgraph.json", encoding="utf-8"))
for w in ("MRGGA", "CDX40", "PKM", "RSAR999"):
    for a in j[w]["attachments"]:
        if "_MAG_" not in a["attachment"]:
            continue
        cap = []; rel = []
        for b in a["branches"]:
            for s in b["selectors"]:
                for e in s["effects"]:
                    if e["class"] == "Class_e7d2410a":
                        cap.append((s["unlock"], e["values"].get("7f22bfb4"), e["values"].get("4614adfe")))
                    if e["class"] == "Class_9705264b":
                        rel.append(e["values"].get("348b8cd1"))
        print(w, a["attachment"], "| cost", a["pointCost"], "| name", "%08X" % a["nameStringId"], repr(lib.string(a["nameStringId"])),
              "| capacity,magazines", cap, "| reload mult", rel, "| unlocks", [s["unlock"] for b in a["branches"] for s in b["selectors"]])
