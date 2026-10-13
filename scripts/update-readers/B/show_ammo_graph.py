"""Print the ammunition records of the new weapons from <run>/uncaptured/attgraph.json."""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import json, pathlib
RUN = settings.RUN
g = json.load(open(RUN / "uncaptured/attgraph.json", encoding="utf-8"))
for w in ["MRGGA", "CDX40", "PKM", "RSAR999"]:
    print("==", w, g[w]["missingWbModifiers"])
    for a in g[w]["attachments"]:
        if a["category"] == "AttachmentCategory_Ammunition":
            if not a["branches"]:
                print(" ", a["attachment"], a["pointCost"], "NO BRANCH")
            for b in a["branches"]:
                print(" ", a["attachment"], a["pointCost"], b["slot"], "kill", b["killSwitch"]["default"], b["issues"])
                for s in b["selectors"]:
                    print("     ", s["unlock"], [(e["asset"], e.get("class"), e.get("values")) for e in s["effects"]],
                          "GS", [(e["asset"], e.get("class"), e.get("values")) for e in s["gs"]])
