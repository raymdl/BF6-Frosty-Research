"""Print full attgraph.json records. python recshow.py <label> <substring> [file]"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import sys, json, pathlib
U = settings.RUN / "uncaptured"
g = json.load(open(U / ((sys.argv[3] if len(sys.argv) > 3 else "attgraph") + ".json"), encoding="utf-8"))
for a in g[sys.argv[1]]["attachments"]:
    if sys.argv[2].lower() in a["attachment"].lower():
        print(json.dumps(a, indent=1)[:6000])
