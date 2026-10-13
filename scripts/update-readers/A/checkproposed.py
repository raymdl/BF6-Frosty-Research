"""Shape check of proposed.json against the site's existing records."""
import json
import lib
p = json.load(open(lib.HERE / "proposed.json", encoding="utf-8"))
site = {w["id"]: w for w in json.load(open(lib.SITE / "data/weapons.json", encoding="utf-8"))}
roles = json.load(open(lib.SITE / "data/weapon-role-tags.json", encoding="utf-8"))
ws = p["proposed"]["data/weapons.json"]["value"]


def shape(v):
    if isinstance(v, dict):
        return {k: shape(x) for k, x in v.items()}
    if isinstance(v, list):
        return [shape(v[0])] if v else []
    return type(v).__name__ if not isinstance(v, (int, float)) or isinstance(v, bool) else "num"


for w in ws:
    for ref in ("brod3", "ef88", "vssm"):
        if ref in site:
            a = set(w) - set(site[ref]); b = set(site[ref]) - set(w)
            print(w["id"], "vs", ref, "extra", sorted(a), "missing", sorted(b), "| key order same:", [k for k in w if k in site[ref]] == [k for k in site[ref] if k in w])
    print("  fireModes", json.dumps(w["fireModes"]), "| dmg points", len(w["dmg"]), w["dmg"][0])
    for k in ("spreadDyn", "recoil", "spread"):
        ref = site["brod3"] if "brod3" in site else next(iter(site.values()))
        print("  ", k, "shape equal to brod3:", shape(w[k]) == shape(ref[k]))
print("brod3 provenance:", json.dumps(site.get("brod3", {}).get("provenance"), ensure_ascii=True)[:900])
print("new provenance:", json.dumps(ws[1]["provenance"], ensure_ascii=True)[:1400])
print("tables rows:", {k: len(v["rows"]) for k, v in p["proposed"]["data/weapon_attributes.json"]["value"]["tables"].items()})
rw = roles["weapons"]; first = next(iter(rw))
print("site role sample:", json.dumps(rw[first], ensure_ascii=True)[:700])
print("new role:", json.dumps(p["proposed"]["data/weapon-role-tags.json"]["value"]["weapons"]["rspr"], ensure_ascii=True)[:700])
print("site role source keys:", json.dumps(roles.get("source"), ensure_ascii=True)[:600])
c = p["conventionChecks"]
print("anim!=transition:", c["animationIndexDiffersFromTransitionIndex"], "| cal formatter:", c["calFromBullet"][:2], "| std mag pkgs on existing:", c["stdMagazinePackagesOnExisting"])
for k, v in p["evidence"].items():
    print(k, "leaves", v["leavesRead"], "reg rows", v["registryRowsFound"], "disagree", v["fileVsRegistryDisagreements"], "no-row sample", v["leavesWithoutRegistryRow"][:4])
att = json.load(open(lib.SITE / "data/weapon_attributes.json", encoding="utf-8"))
print("site attributes top keys:", list(att)[:12], "| l115 mobilityInputs:", json.dumps({k: v.get("l115") for k, v in att.items() if isinstance(v, dict) and "l115" in v and k != "tables"})[:400])
