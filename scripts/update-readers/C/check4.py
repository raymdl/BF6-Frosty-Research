import json
P = json.load(open("proposed.json", encoding="utf-8")); A = P["data/attachments.json"]; T = P["data/attachment-tooltips.json"]
N = json.load(open("propose-notes.json", encoding="utf-8"))
for w in ("mk24", "elr40", "z84m", "rspr"):
    print(w, json.dumps(A["WEAPON_ATTS/" + w])[:1500])
    print(w, json.dumps(A.get("WEAPON_ERGO/" + w)), json.dumps(A.get("WEAPON_ACCESSORY/" + w))[:700])
    print(w, "sightCosts", N["weapons"][w]["structure"]["sightCosts"], "uncat", N["weapons"][w]["structure"]["sightUncategorised"], "base", json.dumps(N["weapons"][w]["structure"]["baseIndexSources"]))
    print(w, "tips", {k: len(v) for k, v in T["byWeapon/" + w].items()}, "sight", T["byWeapon/" + w].get("sight"))
print("new descriptions:", [k for k in T if k.startswith("descriptions/")])
print(len(P), {k: len(v) for k, v in P.items()})
rows = N["ace"]["rows"]
print("ACE", json.dumps(N["ace"]["signature"])[:900], N["ace"]["strings"])
print([(r["weapon"], r["storedCost"], r["killSwitch"][0][-40:], bool(r["inOwnAam"]), r["physicalSlots"]) for r in rows][:6])
print("in own AAM:", [r["weapon"] for r in rows if r["inOwnAam"]])
print(json.dumps(A["GRIPS[+]"])[:400])
