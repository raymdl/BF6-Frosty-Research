"""Weapon roster: the 63 existing site weapons (identity map) plus the four new ones, with raw folder and file stem."""
import json
from rawlib import *

NEW = [("mk24", "Mk 24", "Assault Rifle", "MRGGA", "AssaultRifle/MRGGA"), ("elr40", "ELR-40", "Sniper Rifle", "CDX40", "BoltAction/CDX40"),
       ("z84m", "Z84M", "LMG", "PKM", "MG/PKM"), ("rspr", "RSPR", "SMG", "RSAR999", "SMG/RSAR999")]


def roster():
    site = {w["id"]: w for w in json.load(open(SITE / "data/weapons.json", encoding="utf-8"))}
    gs = {}
    for k in held:
        if "/hardware/weapons/" in k and k.rsplit("/", 1)[-1].startswith("gs_"):
            gs[k.rsplit("/", 1)[-1][3:]] = k
    out = []
    for w in identities():
        k = gs[w["internalId"].lower()]
        folder = route_case[k].split("/Weapons/", 1)[1].rsplit("/", 1)[0] if "/Weapons/" in route_case[k] else route_case[k].split("/weapons/", 1)[1].rsplit("/", 1)[0]
        stem = route_case[k].rsplit("/", 1)[-1][3:]
        out.append({"siteId": w["siteId"], "name": w["siteName"], "cls": site[w["siteId"]]["cls"], "internal": w["internalId"], "folder": folder, "stem": stem, "new": False})
    for sid_, name, cls, internal, folder in NEW:
        out.append({"siteId": sid_, "name": name, "cls": cls, "internal": internal, "folder": folder, "stem": internal, "new": True})
    return out


if __name__ == "__main__":
    import sys, graph
    for w in roster():
        if len(sys.argv) > 1 and w["siteId"] not in sys.argv[1:]:
            continue
        try:
            gph = graph.weapon_graph(w["siteId"], w["folder"], w["stem"], refresh=len(sys.argv) > 1)
            print("%-12s %-14s %-24s attachments %3d equipment %2d missingWB %d  %s" % (w["siteId"], w["cls"], w["folder"], len(gph["attachments"]),
                  len(gph["equipment"]), len(gph["missingWbModifiers"]), {k: v.get("registry", v.get("file")) for k, v in gph["baseIndices"].items()}), flush=True)
        except Exception as e:
            print("FAILED", w["siteId"], w["folder"], repr(e), flush=True)
