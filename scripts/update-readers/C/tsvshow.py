"""Show attgraph tsv rows for one weapon label, with names. python tsvshow.py RSAR999 [file]"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import sys, json, pathlib
U = settings.RUN / "uncaptured"
f = sys.argv[2] if len(sys.argv) > 2 else "attgraph"
g = json.load(open(U / (f + ".json"), encoding="utf-8"))
for a in g[sys.argv[1]]["attachments"]:
    for b in a["branches"] or [None]:
        print("%-34s %-14s %-16s %3s kill=%-5s %-22s %s | %s" % (
            a["attachment"].split("_", 2)[2], (a["category"] or "").replace("AttachmentCategory_", ""), b and b["slot"], a["pointCost"],
            b and b["killSwitch"]["default"], a.get("name"), json.dumps({k: v for k, v in (b["fields"] if b else {}).items() if v not in (0, None)}),
            ",".join(s["unlock"] for s in (b["selectors"] if b else []))))
