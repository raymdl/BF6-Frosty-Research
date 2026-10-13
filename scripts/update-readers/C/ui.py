"""Attachment UI metadata from raw 2.1.1.0 files: AD_* descriptors (label, description) and AAM_* maps
(attachment display record -> AD asset, in-game model name). Port of ui_indexes()/weapon_ui() in the
site's scripts/frosty-attachment-tooltips.py, reading raw EBX instead of XML.

AD root (Class_535682be): Field_33a358a7 -> label text object, Field_490f0dd0 -> description text object;
text object (Class_fbe1d3bc) Field_3d34898a = string id.
AAM record (Class_ccf7da47): Field_55aded8d internal label, Field_fd698f51 -> in-game name text object,
Field_85b318a1 -> AD asset.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent)); import settings
import json, re, pathlib, collections
from rawlib import *

HERE = settings.part("C")
SLOT_CODE = r"(SCP|MZL|BRL|BTM|TOP|RGT|LFT|ERG|MAG|AMO)"


def normalized(v):
    return re.sub(r"[^a-z0-9]", "", v.lower())


def without_slot(v):
    return re.sub("_" + SLOT_CODE + "_", "_", v, flags=re.I)


def descriptor_name(v):
    v = re.sub(r"^(Attachment_|AD_)", "", v, flags=re.I)
    v = re.sub(r"_MZL_FlashComp_", "_MZL_", v, flags=re.I)
    if "_brl_" in v.lower():
        v = re.sub(r"Barrel$", "", v, flags=re.I)
    return normalized(v)


def _text(ptr, objs):
    _, o = deref(ptr, objs)
    if not o:
        return {}
    i = sid(o.get("Field_3d34898a"))
    t = strings().get(i)
    return {"id": i, **({"text": t} if t is not None else {})}


def descriptors(refresh=False):
    cp = HERE / "cache" / "_descriptors.json"
    if cp.exists() and not refresh:
        return json.load(open(cp, encoding="utf-8"))
    out = {}
    for k in sorted(held):
        base = k.rsplit("/", 1)[-1]
        if not base.startswith("ad_"):
            continue
        if "/ui/static/metadata/attachments/" not in k and "/hardware/weapons/" not in k:
            continue
        try:
            objs = load(k)[0]
        except Exception as e:
            out[k] = {"asset": route_case[k], "error": repr(e)}; continue
        root = objs[0]
        if root["$class"] != "Class_535682be":
            continue
        out[k] = {"asset": route_case[k], "label": _text(root.get("Field_33a358a7"), objs), "description": _text(root.get("Field_490f0dd0"), objs)}
    json.dump(out, open(cp, "w", encoding="utf-8"))
    return out


def aam_records(refresh=False):
    """All AAM records held: list of {aam, name, adRoute, adHeld, inGameName{id,text}}."""
    cp = HERE / "cache" / "_aam.json"
    if cp.exists() and not refresh:
        return json.load(open(cp, encoding="utf-8"))
    out = []
    for k in sorted(held):
        if not k.rsplit("/", 1)[-1].startswith("aam_"):
            continue
        objs = load(k)[0]
        for o in objs:
            if o["$class"] != "Class_ccf7da47":
                continue
            r = imp(o.get("Field_85b318a1"))
            if not r:
                continue
            out.append({"aam": route_case[k], "name": o.get("Field_55aded8d") or "", "adRoute": r[0], "adHeld": bool(r[0] and r[0].lower() in held),
                        "adFileGuid": o["Field_85b318a1"]["$import"]["fileGuid"], "inGameName": _text(o.get("Field_fd698f51"), objs)})
    json.dump(out, open(cp, "w", encoding="utf-8"))
    return out


class Index:
    def __init__(self):
        self.desc = descriptors()
        self.names, self.rails, self.assets_by_name = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        self.records = collections.defaultdict(list)
        for r in aam_records():
            if not r["adRoute"]:
                continue
            a = r["adRoute"].lower()
            self.names[normalized(r["name"])].add(a)
            self.rails[normalized(re.sub(r" - (RGT|LFT|TOP) - ", " - ", r["name"]))].add(a)
            self.records[normalized(r["name"])].append(r)
        for a, rec in self.desc.items():
            if "asset" not in rec:
                continue
            base = rec["asset"].rsplit("/", 1)[-1]
            self.assets_by_name[descriptor_name(base)].add(a)
            if "/shared/" in a:
                model = re.sub(r"_(LeftRail|RightRail|TopRail)$", "", base, flags=re.I)
                model = re.sub(r"^AD_Shared_MZL_FlashComp_", "AD_", model, flags=re.I)
                model = re.sub(r"^AD_Shared_ERG_Quickdraw(Pistol|Revolver)$", r"AD_\1Quickdraw", model, flags=re.I)
                self.assets_by_name["shared:" + descriptor_name(model)].add(a)

    def weapon_ui(self, name, slot, slots_by_name):
        """name = '<Weapon>_<SLOT>_<Model>' (attachment stem with the weapon prefix)."""
        key = normalized(name)
        if self.names.get(key):
            return {"method": "aam-full-name", "assets": sorted(self.names[key]), "aamRecords": self.records[key]}
        short = normalized(without_slot(name))
        if len(slots_by_name.get(short, set())) == 1 and self.names.get(short):
            return {"method": "aam-without-slot", "assets": sorted(self.names[short]), "aamRecords": self.records[short]}
        rail = normalized(re.sub(r"_(RGT|LFT|TOP)_", "_", name, flags=re.I))
        if slot in ("laser", "light") and len(slots_by_name.get(rail, set())) == 1 and self.rails.get(rail):
            return {"method": "aam-without-rail-side", "assets": sorted(self.rails[rail])}
        direct = self.assets_by_name.get(descriptor_name(name), set())
        if direct:
            return {"method": "weapon-descriptor-asset-name", "assets": sorted(direct)}
        if slot in ("muzzle", "grip", "laser", "light", "ergo"):
            parts = re.split(r"_(?:MZL|BTM|RGT|LFT|TOP|ERG)_", name, maxsplit=1, flags=re.I)
            if len(parts) == 1 and slot == "grip":
                parts = name.split("_", 1)
            shared = self.assets_by_name.get("shared:" + normalized(parts[-1]), set()) if len(parts) == 2 else set()
            if shared:
                return {"method": "shared-hardware-descriptor-name", "assets": sorted(shared)}
        return None

    def consensus(self, assets):
        """(sorted description ids, text) when every asset is held and all texts agree; else None."""
        if not assets:
            return None
        ents = [self.desc.get(a, {}).get("description", {}) for a in assets]
        texts = {e.get("text") for e in ents}
        if len(texts) != 1 or None in texts or "" in texts:
            return None
        return sorted({e["id"] for e in ents}), next(iter(texts))

    def labels(self, assets):
        return sorted({(self.desc.get(a, {}).get("label", {}) or {}).get("text") or "" for a in assets})


if __name__ == "__main__":
    d = descriptors(refresh=True); a = aam_records(refresh=True)
    print(len(d), "AD descriptors;", sum("text" in (v.get("label") or {}) for v in d.values()), "labels,", sum("text" in (v.get("description") or {}) for v in d.values()), "descriptions,", sum("error" in v for v in d.values()), "errors")
    print(len(a), "AAM records;", sum(not r["adHeld"] for r in a), "point to AD assets not held")
    miss = collections.Counter((r["adRoute"] or "guid:" + r["adFileGuid"]) for r in a if not r["adHeld"])
    for k, v in miss.most_common(80):
        print("   not held:", v, k)
