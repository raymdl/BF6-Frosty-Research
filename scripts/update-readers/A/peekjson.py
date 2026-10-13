"""python peekjson.py <file> [dotted.path] [max chars] -> keys and truncated previews of a JSON file."""
import json, sys
j = json.load(open(sys.argv[1], encoding="utf-8"))
path = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != "." else ""
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 400
for p in [x for x in path.split(".") if x]:
    j = j[int(p)] if isinstance(j, list) else j[p]
if isinstance(j, dict):
    for k, v in j.items():
        print(k, "|", type(v).__name__, len(v) if hasattr(v, "__len__") else "", "|", json.dumps(v, ensure_ascii=False)[:mx])
elif isinstance(j, list):
    print("list", len(j))
    for v in j[:3] + j[-2:]:
        print(json.dumps(v, ensure_ascii=False)[:mx])
else:
    print(json.dumps(j, ensure_ascii=False)[:mx])
