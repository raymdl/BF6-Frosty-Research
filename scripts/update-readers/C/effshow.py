"""Compact effect listing per record. python effshow.py <label> <substring> [file]"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import sys, json, pathlib
U = settings.RUN / "uncaptured"
g = json.load(open(U / ((sys.argv[3] if len(sys.argv) > 3 else "attgraph") + ".json"), encoding="utf-8"))
for a in g[sys.argv[1]]["attachments"]:
    if sys.argv[2].lower() in a["attachment"].lower():
        print("##", a["attachment"], a["pointCost"])
        for b in a["branches"]:
            for s in b["selectors"]:
                print("   sel", s["unlock"])
                for e in s["effects"]:
                    print("      WB", e.get("asset"), e.get("class"), json.dumps(e.get("operand") or e.get("values"))[:200])
                for e in s["gs"]:
                    print("      GS", e.get("asset"), e.get("class"), json.dumps(e.get("operand") or e.get("values"))[:200])
