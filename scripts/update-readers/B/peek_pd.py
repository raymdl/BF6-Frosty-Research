"""python peek_pd.py <PD name> : print the bullet object's reference fields and scalar fields compactly."""
import sys, json
import common as c
route = "Common/Hardware/Weapons/_Bullets/" + sys.argv[1]
print(c.held[route.lower()])
objs, _ = c.load(route)
root = objs[0]
print("root", root["$class"], {k: v for k, v in root.items() if k.startswith("Field_")})
for i, o in enumerate(objs):
    if o["$class"] == "Class_23637dce":
        print("bullet object", i, o["$guid"], "layoutAmbiguous", o.get("$layoutAmbiguous"))
        for k, v in o.items():
            if isinstance(v, dict) and ("$ref" in v or "$import" in v):
                r, t = c.deref(v, objs)
                print("  ", k, "->", ("ref %d" % v["$ref"]) if "$ref" in v else r, t["$class"] if t else None,
                      json.dumps({kk: vv for kk, vv in (t or {}).items() if kk in ("Field_5279388d", "Field_0c59fa06")})[:400])
            elif k in ("Field_d9d33d20", "Field_30c37c24", "Field_c7584f55", "Field_f52e0562", "Field_2ad7e688", "Field_6008eb31", "Field_0bdc38c4", "Field_7e05a1ae"):
                print("  ", k, json.dumps(v)[:300])
            elif isinstance(v, dict) and "Field_6b28f68f" in v:
                r, t = c.deref(v["Field_6b28f68f"], objs)
                print("  ", k, "tweak ->", r, (t or {}).get("Field_0c59fa06"), json.dumps(c.unbox((t or {}).get("Field_42c8b257")))[:200])
        if len(sys.argv) > 2:
            print(json.dumps({k: v for k, v in o.items() if not isinstance(v, (dict, list))}))
    elif o["$class"] == "Class_6a0d9448":
        r, t = c.deref(o["Field_84a4ac26"]["Field_6b28f68f"], objs)
        print("curve object", i, o["$guid"], "flat", o["Field_5279388d"], "points", len(o["Field_edfc6df6"]), "| registry row:", r, (t or {}).get("Field_0c59fa06"),
              json.dumps(c.unbox((t or {}).get("Field_42c8b257")))[:300])
    else:
        print("other object", i, o["$class"], json.dumps(o)[:160])
