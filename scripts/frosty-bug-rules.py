#!/usr/bin/env python3
r"""Re-run the rules behind the game bug list on one build's raw capture, for every weapon.

  python scripts/frosty-bug-rules.py <build>\capture\collection\raw --out result.json [--only 2,4,29]

Each entry of the Analyzer's docs/ATTACHMENT_BUGS.md rests on a rule that can be read from the
game files (for example "the selector binds effect X on other weapons and not on this one").
This script applies the rule to ALL weapons of the capture and reports, per entry, the weapons
where the bug condition holds now, set against the weapons the entry lists today (LISTED below):
newly affected and no longer affected. Entries that cannot be decided from files are reported as
"manual" with the reason. The in-game half of an entry (panel display, firing, cycle order) is
never decided here; the "manual" field of a scripted entry says what is left.

It reuses scripts/update-readers (attachment graph, descriptors, raw loader) and
scripts/frosty-ebx-decode.py; the raw folder must be <data>\builds\<build>\capture\collection\raw
so that the readers find the build's other raw folders (multiplayer copies) and descriptors.
When the bug list changes, update LISTED, ALSO_IN_TEXT and BY_DESIGN here to match it.

Rules of evidence: values come from the game files only; a file or field the rule needs and the
capture lacks is reported as an error on that entry, never guessed. Registry (GRX_Weapons)
overrides are applied only where a rule says so (entries 20 and 24).
"""
import argparse
import collections
import datetime
import json
import os
import pathlib
import re
import shutil
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
READERS = HERE / "update-readers"

# ---------------------------------------------------------------- baseline: what the bug list says today
# Weapon names are the site names (frosty-weapon-identities.json). Pair entries use "Weapon / in-game name".
LISTED = {
    2: ["M45A1"],
    4: ["PP-19"],
    6: ["PP-19"],
    10: ["KTS100 MK8"],
    11: ["RPK-74M", "L115"],
    13: ["Mini Scout"],
    14: ["GRT-BC", "SL9", "KORD 6P67", "SG 553R", "PW5A3", "KV9", "CZ3A1", "UMG-40"],
    15: ["SOR-300SC", "GRT-CPS"],
    16: ["BROD 3", "NSW4"],
    17: ["M433", "SGX", "L110", "P18"],
    18: ["Mk 24"],
    20: ["ELR-40"],
    21: ["Mk 24 / Adjustable Angled", "Z84M / Adjustable Angled", "Mk 24 / Full Angled", "Z84M / Full Angled"]
        + ["%s / QD Grip Pod" % w for w in ("Mk 24", "Z84M", "EF88", "M16A4", "NSW4", "BROD 3", "RPK-74M", "VSSM")],
    22: ["Interdictor"],
    23: ["Interdictor / MGO 3.50x", "M16A4 / QMK 3.00x"],
    24: ["ELR-40"],
    25: ["%s / bipod" % w for w in ("Mk 24", "EF88", "VSSM", "Z84M")]
        + ["%s / grip pods" % w for w in ("Mk 24", "EF88", "Z84M", "VSSM", "BROD 3", "NSW4")],
    26: ["EF88", "BROD 3", "Mk 24", "NSW4"],
    27: ["ELR-40"],
    28: ["KORD 6P67", "SG 553R", "PW5A3", "UMG-40", "KV9", "CZ3A1"],
    29: ["M433"],
}
# Weapons the entry's own text already names as meeting the condition but not as listed weapons.
ALSO_IN_TEXT = {
    11: ["P18", "ES 5.7", "GGH-22", "M45A1"],   # "four semi-automatic pistols also use the base parts" (source finding)
}
# Folders whose weapons the entry text excludes as intended design.
BY_DESIGN = {
    16: ("BoltAction", "Operator: bolt-action rifles lack the iron-sight sway package by design (entry 16, 25 September)."),
}

# Effect classes (hash names from the decoder).
RELOAD_CLS = {"Class_9705264b", "Class_7d916d6b"}
CORE_HANDLING = {"Class_4aac041b": "draw", "Class_03db7a68": "sprint recovery", "Class_016623ac": "ADS time",
                 "Class_104c2294": "ADS time", "Class_bb7f4ea1": "ADS time", "Class_303a33cc": "ADS move speed"}
SWAY_CLS = {"Class_2fea847d", "Class_28d25398"}
PEN_CLS = "Class_d11a23a2"
PEN_TABLE_ROWS = 10   # collateral table rows 0..9 (2.1.2.0 checklist, S6-index-bounds-grid); not re-read here
MODE = {0: "single", 1: "bolt", 2: "auto", 3: "burst"}
SHOT = ".WeaponEntityData.WeaponFiring.PrimaryFire.Shot."
F = lambda h: "Field_" + h
CAT_SLOT = {"Muzzle": "muzzle", "Barrel": "barrel", "BottomRail": "grip", "Magazine": "mag", "Ammunition": "ammo",
            "MagazineWell": "ergo", "TopRail": "laser", "RightRail": "light", "LeftRail": "light", "Sight": "sight",
            "OpticAccessory": "accessory"}


def setup(raw):
    raw = pathlib.Path(raw).resolve()
    if raw.name.lower() != "raw" or raw.parent.name.lower() != "collection" or raw.parents[1].name.lower() != "capture":
        sys.exit("expected <data>\\builds\\<build>\\capture\\collection\\raw, got %s" % raw)
    build = raw.parents[2]
    os.environ["BF6_BUILD"] = build.name
    os.environ["BF6_DATAMINING"] = str(build.parents[1])
    work = tempfile.mkdtemp(prefix="bugrules-")   # the readers write their caches here; removed at the end
    os.environ["BF6_READER_WORK"] = work
    sys.path.insert(0, str(READERS / "C"))
    return build, work


def load_readers():
    global rawlib, graph, ui
    import rawlib as _r   # noqa: E402
    import graph as _g
    import ui as _u
    rawlib, graph, ui = _r, _g, _u

    def scalars(o, skip=("Field_0c59fa06", "Field_819acc98")):
        """graph.scalars without its dropping of 1 and -1 (penetration steps are often +-1)."""
        out = {}

        def walk(x, p):
            if isinstance(x, dict):
                if "$import" in x or "$ref" in x or "absoluteOffset" in x:
                    return
                for k, c in x.items():
                    if not k.startswith("$") and k not in skip:
                        walk(c, p + "/" + k[6:] if k.startswith("Field_") else p + "/" + k)
            elif isinstance(x, list):
                for i, c in enumerate(x):
                    walk(c, p + "[%d]" % i)
            elif x is not None and x != "" and x is not False and not (isinstance(x, (int, float)) and not isinstance(x, bool) and x == 0):
                out[p.lstrip("/")] = x
        walk(o, "")
        return out
    graph.scalars = scalars


# ---------------------------------------------------------------- weapons
class Weapon:
    def __init__(self, folder, stem, name, onsite):
        self.folder, self.stem, self.name, self.onsite = folder, stem, name, onsite
        self.cls = folder.split("/")[0]
        self.base = "common/hardware/weapons/" + folder.lower() + "/"
        self.graph = graph.weapon_graph(stem.lower(), folder, stem, refresh=True)
        self._wb = self._gs = self._ab = None

    def route(self, kind):
        return self.base + (self.stem.lower() + "_" + kind if kind != "gs" else "gs_" + self.stem.lower())

    @property
    def wb(self):
        if self._wb is None:
            self._wb = rawlib.load(self.route("wb"))[0]
        return self._wb

    @property
    def gs(self):
        if self._gs is None:
            self._gs = rawlib.load(self.route("gs"))[0]
        return self._gs

    def fire(self):
        return [o for o in self.wb if o["$class"] == "Class_35259f6b"][0]

    def gs_bindings(self):
        """[(selector key lower, modifier asset name)] for every GS effect binding."""
        out = []

        def walk(x):
            if isinstance(x, dict):
                if "Field_2f0e5b83" in x and "Field_6d011165" in x:
                    r, o = rawlib.deref(x["Field_2f0e5b83"], self.gs)
                    out.append((str(x["Field_6d011165"]).lower(), (r or "local").rsplit("/", 1)[-1]))
                for c in x.values():
                    walk(c)
            elif isinstance(x, list):
                for c in x:
                    walk(c)
        for o in self.gs:
            walk(o)
        return out

    def files(self):
        return {"wb": self.stem + "_WB.ebx", "gs": "GS_" + self.stem + ".ebx", "ability": self.stem + "_Ability.ebx"}

    def branches(self, cats=None, live=True):
        for a in self.graph["attachments"]:
            if cats and a["category"] not in cats:
                continue
            for b in a["branches"]:
                if live and b["kill"]["default"]:
                    continue
                yield a, b


def roster():
    ident = {w["internalId"].lower(): w["siteName"] for w in rawlib.identities()}
    j = json.load(open(rawlib.REPO / "reference-data/provenance/frosty-weapon-identities.json", encoding="utf-8"))
    ident.update({w["internalId"].lower(): w["sourceName"] for w in j.get("identifiedOutsideSite", [])})
    site = set()
    wp = rawlib.SITE / "data/weapons.json"
    if wp.is_file():
        site = {w["name"] for w in json.load(open(wp, encoding="utf-8"))}
    out = []
    for k in sorted(rawlib.held):
        if "/hardware/weapons/" in k and k.rsplit("/", 1)[-1].startswith("gs_"):
            r = rawlib.route_case[k]
            folder = re.split(r"/weapons/", r, flags=re.I)[1].rsplit("/", 1)[0]
            stem = r.rsplit("/", 1)[-1][3:]
            base = "common/hardware/weapons/" + folder.lower() + "/" + stem.lower()
            if base + "_wb" not in rawlib.held or base + "_ability" not in rawlib.held:
                continue
            nm = ident.get(stem.lower(), stem)
            out.append((folder, stem, nm, (nm in site) if site else True))
    return out


class Ctx:
    def __init__(self):
        self.W = [Weapon(f, s, n, o) for f, s, n, o in roster()]
        self.by_name = {w.name: w for w in self.W}
        self._ui = None
        self._pkg = {}
        self._routes = None

    def disp(self, w):
        return w.name if w.onsite else w.name + " (not on site)"

    # package files by asset name
    def package_route(self, asset):
        if self._routes is None:
            self._routes = collections.defaultdict(list)
            for k in rawlib.held:
                b = k.rsplit("/", 1)[-1]
                if b.startswith(("wpm_", "u_wpm_", "wme_")):
                    self._routes[b].append(k)
        r = self._routes.get(asset.lower(), [])
        return r[0] if r else None

    def find_key(self, asset, key):
        out = []
        r = self.package_route(asset)
        if r:
            def walk(o):
                if isinstance(o, dict):
                    for k, v in o.items():
                        if k == key:
                            out.append(v)
                        else:
                            walk(v)
                elif isinstance(o, list):
                    for v in o:
                        walk(v)
            walk(rawlib.load(r)[0])
        return out

    # UI text for a weapon attachment (in-game name, description)
    def ui(self, w, a):
        if self._ui is None:
            self._idx = ui.Index()
            self._sbn = collections.defaultdict(set)
            for x in self.W:
                for aa in x.graph["attachments"]:
                    n = aa["attachment"][len("Attachment_"):]
                    self._sbn[ui.normalized(ui.without_slot(n))].add(CAT_SLOT.get(aa["category"], "?"))
            self._ui = {}
        k = (w.stem, a["attachment"])
        if k not in self._ui:
            name = a["attachment"][len("Attachment_"):]
            link = self._idx.weapon_ui(name, CAT_SLOT.get(a["category"], "?"), self._sbn)
            res = {"name": None, "desc": None}
            if link:
                for r in link.get("aamRecords", []):
                    res["name"] = ((r.get("inGameName") or {}).get("text") or res["name"] or "").strip() or None
                c = self._idx.consensus(link["assets"])
                res["desc"] = c[1] if c else None
            self._ui[k] = res
        return self._ui[k]


def names(sel):
    return [e["asset"] for e in sel["effects"]]


def classes(sel):
    return {e["class"] for e in sel["effects"]}


def base_pairs(base_modes):
    return [base_modes[0]] + [m for m in base_modes[1] if m != base_modes[0]]


def base_modes(w):
    fl = w.fire()[F("f8822efa")]
    return fl[F("16e6fa59")], list(fl[F("9b956c3d")])


# ---------------------------------------------------------------- rules: each returns dict(now={item: [evidence]}, notes=[...], extra...)
def r1(c):
    now = {}
    for w in c.W:
        if w.cls != "BoltAction":
            continue
        for a, b in w.branches({"BottomRail"}):
            if len(b["selectors"]) > 1:
                now.setdefault(c.disp(w), []).append("%s: ability branch lists %s" % (w.files()["ability"], [s["unlock"] for s in b["selectors"]]))
    return {"now": now, "baseline": []}


def r2(c):
    now = {}
    for w in c.W:
        for a, b in w.branches({"Ammunition"}):
            if a["stem"] == "AMO_FMJ":
                continue
            fmj = [s["unlock"] for s in b["selectors"] if s["unlock"].startswith("U_WPM_AMO_FMJ")]
            if fmj:
                now.setdefault(c.disp(w), []).append("%s: ability branch (Field_7e54e22c) of %s lists %s" % (w.files()["ability"], a["attachment"], [s["unlock"] for s in b["selectors"]]))
    return {"now": now}


def _claims_reload(c):
    """Magazines whose description promises faster reloads but whose selector carries no reload effect."""
    now, skipped = {}, []
    for w in c.W:
        for a, b in w.branches({"Magazine"}):
            t = c.ui(w, a)
            if not t["desc"] or not re.search(r"faster reload", t["desc"], re.I):
                continue
            if not b["selectors"]:
                skipped.append(c.disp(w) + " " + a["attachment"])
                continue
            if not any(classes(s) & RELOAD_CLS for s in b["selectors"]):
                now.setdefault(c.disp(w), []).append("%s (%s): description \"%s\"; selectors %s carry no reload-speed effect (Class_9705264b) or reload-phase package (Class_7d916d6b); effects %s"
                                                     % (a["attachment"], t["name"], t["desc"], [s["unlock"] for s in b["selectors"]], sorted({n for s in b["selectors"] for n in names(s)})))
    return now, skipped


def r4(c):
    now, skipped = _claims_reload(c)
    return {"now": now, "notes": ["Skipped, no selector resolved from the ability branch (cannot be decided): %s" % skipped] if skipped else []}


def r6(c):
    """A muzzle selector that most weapons bind to GRM_SmoothRecoil* but this weapon's GS file does not."""
    per = collections.defaultdict(dict)
    for w in c.W:
        for a, b in w.branches({"Muzzle"}):
            for s in b["selectors"]:
                per[s["unlock"]][w.stem] = (a, any(n.startswith("GRM_SmoothRecoil") for n in names(s)), s["guid"])
    now = {}
    notes = []
    for u, d in per.items():
        have = sum(1 for v in d.values() if v[1])
        if len(d) >= 5 and have / len(d) >= 0.8 and have < len(d):
            notes.append("%s: smoothing bound on %d of %d weapons" % (u, have, len(d)))
            for stem, (a, ok, guid) in d.items():
                if not ok:
                    w = next(x for x in c.W if x.stem == stem)
                    now.setdefault(c.disp(w), []).append("%s: no binding (Field_2f0e5b83/Field_6d011165) to selector %s of %s (%s) for GRM_SmoothRecoil*" % (w.files()["gs"], guid[:8], u, a["attachment"]))
    return {"now": now, "notes": notes}


def r10(c):
    """Magazines described as improved handling that gain none of draw, sprint recovery, ADS time or ADS move speed against the weapon's default (Std) magazine."""
    now, broad = {}, {}
    for w in c.W:
        default = None
        for a, b in w.branches({"Magazine"}):
            if any(s["unlock"].startswith("U_WPM_MAG_Std") for s in b["selectors"]):
                default = (a, b)
        if not default:
            continue

        def vec(b):
            v = collections.Counter()
            for s in b["selectors"]:
                for e in s["effects"]:
                    m = re.search(r"_([PM])(\d\d)$", e["asset"])
                    if not m:
                        continue
                    asp = CORE_HANDLING.get(e["class"]) or ("sway" if e["class"] in SWAY_CLS else "reload" if e["class"] in RELOAD_CLS else None)
                    if e["asset"].startswith("GDM_Array_ADSMoveDispersion"):
                        asp = "moving-ADS accuracy"
                    if asp:
                        v[asp] += (1 if m.group(1) == "P" else -1) * int(m.group(2)) // 5
            return v
        dv = vec(default[1])
        for a, b in w.branches({"Magazine"}):
            if a["attachment"] == default[0]["attachment"]:
                continue
            t = c.ui(w, a)
            if not t["desc"] or "improved handling" not in t["desc"].lower() or not b["selectors"]:
                continue
            mv = vec(b)
            delta = {k: mv[k] - dv[k] for k in set(mv) | set(dv) if mv[k] != dv[k]}
            core = {k: v for k, v in delta.items() if k in set(CORE_HANDLING.values()) and v > 0}
            line = "%s (%s) vs default %s: %s" % (a["attachment"], t["name"], default[0]["attachment"], delta or "no handling difference")
            if not core:
                now.setdefault(c.disp(w), []).append(line)
                if not any(v > 0 for v in delta.values()):
                    broad.setdefault(c.disp(w), []).append(line)
    return {"now": now, "notes": ["Under the broader reading of the method doc (any of sprint, draw, ADS, ADS move, sway, moving-ADS accuracy, reload improved) only these remain: %s" % sorted(broad)],
            "manual": "Whether 'improved handling' is wrong needs the in-game panel (2.1.2.0 recheck: entry 10 'Re-judge in game')."}


def r11(c):
    """Optic packages whose render FOV (Field_7768ebf2) differs from the one most weapons use for the same optic selector."""
    per = collections.defaultdict(dict)
    for w in c.W:
        for a, b in w.branches({"Sight"}):
            for s in b["selectors"]:
                for e in s["effects"]:
                    if e["asset"].startswith("WPM_SCP_"):
                        fov = c.find_key(e["asset"], "Field_7768ebf2")
                        if fov:
                            per[s["unlock"]].setdefault(w.stem, (e["asset"], fov[0], a["attachment"]))
    now = {}
    for u, d in per.items():
        mode, n = collections.Counter(v[1] for v in d.values()).most_common(1)[0]
        if len(d) >= 10 and n / len(d) >= 0.5:
            for stem, (asset, fov, att) in d.items():
                if fov != mode:
                    w = next(x for x in c.W if x.stem == stem)
                    now.setdefault(c.disp(w), []).append("%s: %s (%s) uses package %s, render FOV Field_7768ebf2 = %g; %d of %d weapons use %g" % (w.files()["wb"], att, u, asset, fov, n, len(d), mode))
    return {"now": now, "manual": "The visual effect (stretched arm, small optic) is in game only."}


def r13(c):
    """Bolt-action Tungsten Core recoil binding is not exactly one GRM_Recoil_AMO_Bolt_* effect."""
    now, info = {}, {}
    for w in c.W:
        for a, b in w.branches({"Ammunition"}):
            if "Tungsten" not in a["stem"] or "Match" in a["stem"] or "Subsonic" in a["stem"]:
                continue
            gr = sorted({n for s in b["selectors"] for n in names(s) if n.startswith("GRM_Recoil_AMO")})
            info.setdefault(w.cls, collections.Counter())[tuple(gr)] += 1
            if w.cls == "BoltAction" and gr != ["GRM_Recoil_AMO_Bolt_M10"]:
                now.setdefault(c.disp(w), []).append("GS_%s.ebx: Tungsten selector U_WPM_AMO_TungstenCore_W05 binds %s (bolt-action rule: one GRM_Recoil_AMO_Bolt_M10)" % (w.stem, gr))
    return {"now": now, "notes": ["Tungsten recoil bindings by class: %s" % {k: {",".join(g): n for g, n in v.items()} for k, v in info.items()}]}


def r14(c):
    """Burst Mode/Training weapons whose burst recoil effects are bound to the BurstFireActive token, not to the attachment's selector."""
    r = c.package_route("U_WPM_ERG_BurstFireActive") or next((k for k in rawlib.held if k.endswith("/u_wpm_erg_burstfireactive")), None)
    if not r:
        return {"error": "U_WPM_ERG_BurstFireActive not in the capture"}
    token = str(rawlib.load(r)[0][0]["$guid"]).lower()
    now = {}
    for w in c.W:
        sel = [s for a, b in w.branches({"MagazineWell"}) for s in b["selectors"] if re.match(r"U_WPM_ERG_BurstFire(Enabled|Replace)", s["unlock"])]
        if not sel:
            continue
        under = sorted({n for k, n in w.gs_bindings() if k == token and n.startswith("GRM_")})
        if under and not any(s["guid"].lower() == token for s in sel):
            now.setdefault(c.disp(w), []).append("%s binds %s under key %s (U_WPM_ERG_BurstFireActive); the attachment selector %s does not carry that key" % (w.files()["gs"], under, token[:8], sel[0]["unlock"]))
    return {"now": now, "manual": "14b (whether the burst modifiers apply while firing) is an open in-game question; this rule decides only the menu-side binding (14a)."}


def r15(c):
    """Base reload entry whose ReloadTime (Field_85ff24a0) differs from ReloadTimeBulletsLeft (Field_fc66e75e) and the end of its phase list (Field_dc244b57), which agree."""
    now, near = {}, []
    for w in c.W:
        fl = w.fire()[F("f8822efa")]
        for i, e in enumerate(fl[F("d15a0c1c")]):
            t, bl, ph = e[F("85ff24a0")], e[F("fc66e75e")], e[F("dc244b57")]
            end = ph[-1] if ph else None
            if t and end is not None and abs(bl - end) <= 0.002 and abs(t - bl) > 0.002:
                now.setdefault(c.disp(w), []).append("%s ReloadInfoArray[%d]: ReloadTime %.3f, ReloadTimeBulletsLeft %.3f, last phase time %s" % (w.files()["wb"], i, t, bl, "%.3f" % end if end is not None else "none"))
            elif t and end is not None and abs(t - end) > 0.002:
                near.append("%s ReloadInfoArray[%d]: ReloadTime = BulletsLeft = %.3f but last phase time %.3f (not the entry's pattern)" % (c.disp(w), i, t, end))
    return {"now": now, "notes": near, "manual": "Which value the game uses is decided by timed captures, not by the files."}


def r16(c):
    """Iron sights (selector U_WPM_IronSights) that do not import the shared sway effect WME_WSway_P05."""
    now, design = {}, {}
    for w in c.W:
        for a, b in w.branches({"Sight"}):
            for s in b["selectors"]:
                if s["unlock"] == "U_WPM_IronSights" and not any(e["asset"] == "WME_WSway_P05" for e in s["effects"]):
                    line = "%s: iron-sight selector %s (%s) lists no WME_WSway_P05 / WME_CSway_P05 (effects: %s)" % (w.files()["wb"], s["unlock"], a["attachment"], sorted(set(names(s))))
                    (design if w.cls == BY_DESIGN[16][0] else now).setdefault(c.disp(w), []).append(line)
    return {"now": now, "byDesign": design, "byDesignReason": BY_DESIGN[16][1]}


def r17(c):
    """In-world spot-on-fire base (WB root Class_542ac52c Field_5ebda408/Field_9918e670) other than the usual 54."""
    vals = {}
    for w in c.W:
        root = [o for o in w.wb if o["$class"] == "Class_542ac52c"][0].get(F("5ebda408"), {})
        vals[w] = (root.get(F("9918e670")), root.get(F("31022dc5")))
    mode = collections.Counter(v[0] for v in vals.values()).most_common(1)[0][0]
    now, other = {}, {}
    for w, (world, mini) in vals.items():
        line = "%s: Class_542ac52c Field_5ebda408/Field_9918e670 = %g (minimap Field_31022dc5 = %g); %g on most weapons" % (w.files()["wb"], world, mini, mode)
        if world == 75:
            now[c.disp(w)] = [line]
        elif world != mode:
            other[c.disp(w)] = line
    return {"now": now, "alsoDiffers": other, "notes": ["Most common value: %g m. Weapons at other values than 75 are listed in alsoDiffers; they do not match the entry's 75 m pattern." % mode],
            "manual": "The in-game panel reading (75 m) is manual. Registry (GRX_Weapons) overrides of the field were not read."}


def r18(c):
    """Hollow Point that costs no more than the same weapon's FMJ (Standard) ammunition."""
    now = {}
    for w in c.W:
        by = {a["stem"]: a["cost"] for a in w.graph["attachments"]}
        hp, fmj = by.get("AMO_HollowPoint"), by.get("AMO_FMJ")
        if hp is not None and fmj is not None and hp <= fmj:
            others = sorted({a["cost"] for x in c.W if x is not w for a in x.graph["attachments"] if a["stem"] == "AMO_HollowPoint"})
            now[c.disp(w)] = ["Attachment_%s_AMO_HollowPoint.ebx: point cost Field_6ee865a5 = %s, AMO_FMJ = %s; other weapons' Hollow Point costs %s" % (w.stem, hp, fmj, others)]
    return {"now": now}


def r20(c):
    """Live ammunition x magazine combinations whose penetration row (base index + ammo steps + magazine steps) passes the collateral table."""
    reg = rawlib.registry()
    now = {}
    for w in c.W:
        wbname = w.wb[0]["Field_0c59fa06"].rsplit("/", 1)[-1]
        shot = w.fire()[F("58d70acb")]
        rv = reg.get(wbname + SHOT + "DamagePenetrationMultiplierIndex")
        base = rv if isinstance(rv, int) else shot[F("7e2be65f")]
        base = base - (1 << 32) if isinstance(base, int) and base >= 1 << 31 else base

        def steps(b):
            seen, tot = set(), 0
            for s in b["selectors"]:
                for e in s["effects"]:
                    if e["class"] == PEN_CLS and e["src"] == "WB":
                        key = (e["asset"], json.dumps(e["values"], sort_keys=True))
                        v = e["values"].get("fbfacac9", 0)
                        tot += v if v < 1 << 31 else v - (1 << 32)
            return tot
        ammo = [(a, steps(b)) for a, b in w.branches({"Ammunition"})]
        mags = [(a, steps(b)) for a, b in w.branches({"Magazine"})] or [(None, 0)]
        for a, sa in ammo:
            for m, sm in mags:
                row = base + sa + sm
                if row > PEN_TABLE_ROWS - 1 or row < 0:
                    now.setdefault(c.disp(w), []).append("%s + %s: base index %d (%s) + ammo steps %d + magazine steps %d = row %d, table rows 0..%d"
                                                         % (a["stem"], m["stem"] if m else "-", base, "registry" if isinstance(rv, int) else "%s Field_7e2be65f" % w.files()["wb"], sa, sm, row, PEN_TABLE_ROWS - 1))
    return {"now": now, "notes": ["Collateral table size (10 rows) is taken from the 2.1.2.0 material-grid check (checklist Stage 6), not re-read by this script."],
            "manual": "The x0.00 panel display and the firing-range damage are in game only."}


def r21(c):
    """Grip selectors whose GRM_Recoil_BTM_* step differs from the one most weapons bind to the same selector."""
    per = collections.defaultdict(dict)
    for w in c.W:
        for a, b in w.branches({"BottomRail"}):
            for s in b["selectors"]:
                g = tuple(sorted(n for n in names(s) if n.startswith("GRM_Recoil_BTM")))
                if g:
                    per[s["unlock"]].setdefault(w.stem, (g, a))
    now = {}
    for u, d in per.items():
        mode, n = collections.Counter(v[0] for v in d.values()).most_common(1)[0]
        if len(d) < 10 or n / len(d) < 0.6:
            continue
        for stem, (g, a) in d.items():
            if g != mode:
                w = next(x for x in c.W if x.stem == stem)
                nm = c.ui(w, a)["name"] or a["stem"]
                now.setdefault("%s / %s" % (c.disp(w), nm), []).append("GS_%s.ebx binds %s to selector %s (%s); %d of %d weapons bind %s" % (w.stem, list(g), u, a["attachment"], n, len(d), list(mode)))
    return {"now": now, "pairs": True}


def r22(c):
    """Bolt-action Precision table (settings Class_0fd27406): fallback (no matching flag) row value other than 100."""
    S = "common/gamesetup/gameconfigurations/glaciergameconfiguration/settings"
    objs = rawlib.load(S)[0]
    par = [o for o in objs if o["$class"] == "Class_fe5894b1"][0]
    tabs = []
    for ref in par[F("d0874615")]:
        _, o = rawlib.deref(ref, objs)
        rows = [(r.get(F("aee62a28")), any(r.get(F(f)) is True for f in ("5d2f3411", "b2922d79", "dfde0349", "1c1c4149", "d55c6d70", "9aefcaf4")))
                for r in o[F("4da34085")][F("f028b424")][F("59491962")]]
        tabs.append((o.get(F("e5bb1946")), o.get(F("85ff24a0")), o.get(F("7f22bfb4")), rows))
    now, notes = {}, []
    for w in c.W:
        if w.cls != "BoltAction":
            continue
        fl, shot, ammo = w.fire()[F("f8822efa")], w.fire()[F("58d70acb")], w.fire()[F("4cc9e2ed")]
        e0 = fl[F("d15a0c1c")][0]
        vel, tac, mag = shot[F("0bf4f62b")][F("32a99b9c")], e0[F("fc66e75e")] / (e0[F("1c533b56")] or 1), ammo[F("7f22bfb4")]
        hit = [t for t in tabs if t[0] and abs(t[0] - vel) < 1e-2 and t[2] == mag and abs(t[1] - tac) < 2e-3]
        if len(hit) != 1:
            notes.append("%s: %d Precision tables match velocity %g, reload %.3f, magazine %d" % (c.disp(w), len(hit), vel, tac, mag))
            continue
        fb = [v for v, keyed in hit[0][3] if not keyed]
        if any(abs(v - 100) > 1e-3 for v in fb):
            now[c.disp(w)] = ["settings.ebx Class_fe5894b1 Field_d0874615 table matched by muzzle velocity %g, tactical reload %.3f, magazine %d: fallback row Field_aee62a28 = %s (keyed rows %s)" % (vel, tac, mag, fb, [v for v, keyed in hit[0][3] if keyed][:3])]
    return {"now": now, "notes": notes, "manual": "The panel reading of 1 (the 0.5 fallback shown as 1) is in game only; the keyed-row-ignored explanation is an inference."}


def r23(c):
    """A scope that no optic accessory lists on this weapon although most weapons list it (so the Optic Accessory slot disappears)."""
    listed_by = collections.defaultdict(lambda: [0, 0])
    per = {}
    for w in c.W:
        ids = set()
        for e in w.graph["equipment"]:
            ids |= set(e["requires"])
        per[w.stem] = {}
        for a, b in w.branches({"Sight"}):
            if a["stem"].startswith("SCP_") and "Iron" not in a["stem"]:
                ok = (a["idHash"] & 0xFFFFFFFF) in ids
                per[w.stem][a["stem"]] = (ok, a)
                listed_by[a["stem"]][0 if ok else 1] += 1
    now = {}
    for w in c.W:
        peers = {s: v for s, v in per[w.stem].items() if listed_by[s][0] / (sum(listed_by[s]) or 1) >= 0.8 and sum(listed_by[s]) >= 10}
        if not peers or sum(1 for v in peers.values() if v[0]) / len(peers) < 0.5:
            continue   # a weapon whose accessories list few of the common scopes (revolvers, pistols) has no slot to lose
        for s, (ok, a) in peers.items():
            if not ok:
                nm = c.ui(w, a)["name"] or s
                now.setdefault("%s / %s" % (c.disp(w), nm), []).append("Equipment_%s.ebx: no optic-accessory entry (Field_f4142987) lists %s (id %d); listed on %d of %d weapons"
                                                                        % (w.stem, a["attachment"], a["idHash"] & 0xFFFFFFFF, listed_by[s][0], sum(listed_by[s])))
    return {"now": now, "pairs": True, "manual": "The missing slot in the menu is in game only."}


def curve(c, asset):
    """Damage curve of the bullet that a magazine/ammo package swaps in (registry row overrides the file, as the site does)."""
    for ref in c.find_key(asset, "Field_808dd66c"):
        i = rawlib.imp(ref)
        if i and i[0] and "/_bullets/" in i[0].lower() and i[0].lower() in rawlib.held:
            objs, by = rawlib.load(i[0])
            b = by[i[1]]
            _, cv = rawlib.deref(b[F("2ad7e688")], objs)
            flat = [v for v in cv.get(F("5279388d"), [])]
            pts = [[p[F("3901db14")], p[F("42fc0f5e")]] for p in cv.get(F("edfc6df6"), [])] or [[flat[k], flat[k + 1]] for k in range(0, len(flat), 2)]
            real = objs[0].get("Field_0c59fa06", "").rsplit("/", 1)[-1] or i[0].rsplit("/", 1)[-1]
            rv = rawlib.registry().get(real + ".BulletEntityData.TweakableDamageCurve.XYValues")
            if isinstance(rv, dict) and rv.get("Field_ffba60f0"):
                a = rv["Field_ffba60f0"]
                pts = [[a[k], a[k + 1]] for k in range(0, len(a), 2)]
            return real, pts
    return None, None


def span(pts, level=100.0):
    xs = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        for lo, hi, cond in ((y0, y1, True),):
            if (y0 - level) * (y1 - level) < 0:
                xs.append(x0 + (level - y0) * (x1 - x0) / (y1 - y0))
        if y0 >= level:
            xs.append(x0)
        if y1 >= level:
            xs.append(x1)
    return (min(xs), max(xs)) if xs else None


def r24(c):
    """Magazine/ammo description naming a range ('between Xm and Ym') whose swapped-in bullet one-shots (curve >= 100) over a different span."""
    now, ok = {}, []
    for w in c.W:
        for a, b in w.branches({"Magazine", "Ammunition"}):
            t = c.ui(w, a)
            m = re.search(r"between (\d+)\s*m and (\d+)\s*m", t["desc"] or "")
            if not m:
                continue
            for s in b["selectors"]:
                for e in s["effects"]:
                    real, pts = curve(c, e["asset"]) if e["src"] == "WB" and e["asset"].startswith("WPM_") else (None, None)
                    if not pts:
                        continue
                    sp = span(pts)
                    lo, hi = int(m.group(1)), int(m.group(2))
                    line = "%s (%s) text \"between %dm and %dm\"; bullet %s curve %s gives damage >= 100 from %s m" % (a["attachment"], t["name"], lo, hi, real, pts, "%.1f to %.1f" % sp if sp else "never")
                    if not sp or abs(sp[0] - lo) > 1.5 or abs(sp[1] - hi) > 1.5:
                        now.setdefault(c.disp(w), []).append(line)
                    else:
                        ok.append(c.disp(w) + ": " + line)
    return {"now": now, "notes": ["Text matches curve: " + "; ".join(ok)] if ok else [],
            "manual": "In-game one-shot range tests; the base weapon's 'Most effective between' text (weapon UI metadata) is not compared."}


def _auto_reachable(w):
    pm, alt = base_modes(w)
    if 2 in [pm] + alt:
        return True
    return any("FullAutoReplace" in s["unlock"] for a, b in w.branches() for s in b["selectors"])


def r25(c):
    now = {}
    for w in c.W:
        auto = _auto_reachable(w)
        for a, b in w.branches({"BottomRail"}):
            for s in b["selectors"]:
                n = set(names(s))
                has_hip = any(x.startswith("GDM_Array_HipDispersion_BTM") for x in n)
                has_ads = any(re.match(r"GBM_Increase_ADS_\d+_BTM_Bipod", x) for x in n)
                if s["unlock"] == "U_WPM_BTM_Bipod01_W10" and not has_hip and not has_ads:
                    now.setdefault("%s / bipod" % c.disp(w), []).append("GS_%s.ebx under selector %s (%s) binds %s only: no GDM_Array_HipDispersion_BTM_* and no GBM_Increase_ADS_*_BTM_Bipod" % (w.stem, s["unlock"], a["attachment"], sorted(x for x in n if x.startswith("GRM"))))
                if re.match(r"U_WPM_BTM_GripPod0\d_", s["unlock"]) and has_hip and not has_ads and auto:
                    now.setdefault("%s / grip pods" % c.disp(w), []).append("GS_%s.ebx under selector %s (%s) binds the hip array and recoil package but no GBM_Increase_ADS_*_BTM_Bipod (weapon reaches automatic fire)" % (w.stem, s["unlock"], a["attachment"]))
    return {"now": now, "pairs": True, "manual": "The deployed-spread recordings and the Z84M in-game check are manual."}


def r26(c):
    """Weapons offering single plus auto or burst whose GS file binds no GBM_NoIncrease_Semi_P00."""
    now, ctrl = {}, 0
    for w in c.W:
        pm, alt = base_modes(w)
        modes = [pm] + alt
        if 0 in modes and (2 in modes or 3 in modes):
            if any(n == "GBM_NoIncrease_Semi_P00" for k, n in w.gs_bindings()):
                ctrl += 1
            else:
                now[c.disp(w)] = ["%s: no binding (Field_2f0e5b83) to GBM_NoIncrease_Semi_P00; %s Field_16e6fa59/Field_9b956c3d modes %s" % (w.files()["gs"], w.files()["wb"], [MODE[m] for m in modes])]
    return {"now": now, "notes": ["%d weapons offering single and auto/burst bind it." % ctrl], "manual": "The per-shot bloom in semi is an in-game recording."}


def _modes_of(c, asset):
    out = []
    for o in (rawlib.load(c.package_route(asset))[0] if c.package_route(asset) else []):
        if "Field_7313f5d3" in o:
            out.append([o["Field_7313f5d3"]] + list(o.get("Field_2a5a28ee", [])))
    return out[0] if out else None


def r28(c):
    """A fire-mode replacement attachment with the same mode set as the base weapon in a different cycle order (Burst Training)."""
    now = {}
    for w in c.W:
        pm, alt = base_modes(w)
        base = base_pairs((pm, alt))
        for a, b in w.branches({"MagazineWell"}):
            for s in b["selectors"]:
                for e in s["effects"]:
                    if e["class"] == "Class_032c7d25":
                        repl = _modes_of(c, e["asset"])
                        if repl and set(repl) == set(base) and repl != base:
                            now.setdefault(c.disp(w), []).append("%s replaces base modes %s (%s Field_16e6fa59/Field_9b956c3d) with %s (Field_7313f5d3/Field_2a5a28ee): same modes, other order"
                                                                 % (e["asset"], [MODE[m] for m in base], w.files()["wb"], [MODE[m] for m in repl]))
    return {"now": now, "manual": "The in-game cycle direction was confirmed by the operator; the files give only the stored order."}


def r29(c):
    now = {}
    for w in c.W:
        for a, b in w.branches({"MagazineWell"}):
            for s in b["selectors"]:
                if s["unlock"] == "U_WPM_ERG_MatchTrigger_W15" and not s["effects"]:
                    now[c.disp(w)] = ["%s: Match Trigger selector U_WPM_ERG_MatchTrigger_W15 resolves to no WB effect and no GS binding (the other weapons hold a local effect chain)" % w.files()["wb"]]
    return {"now": now, "manual": "The recordings (kick ratio, 80% recovery) are manual."}


def r27(c):
    """Suppressors with the same in-game name that use a different selector on this weapon than on most weapons."""
    per = collections.defaultdict(dict)
    for w in c.W:
        for a, b in w.branches({"Muzzle"}):
            nm = c.ui(w, a)["name"]
            if nm and "Suppressor" in nm:
                sel = tuple(sorted(s["unlock"] for s in b["selectors"] if s["unlock"].startswith("U_WPM_MZL_")))
                if sel:
                    per[nm].setdefault(w.stem, (sel, a))
    now = {}
    for nm, d in per.items():
        mode, n = collections.Counter(v[0] for v in d.values()).most_common(1)[0]
        if len(d) < 5 or n / len(d) < 0.6:
            continue
        for stem, (sel, a) in d.items():
            if sel != mode:
                w = next(x for x in c.W if x.stem == stem)
                now.setdefault(c.disp(w), []).append("%s is named \"%s\" but selects %s; %d of %d weapons with that name select %s" % (a["attachment"], nm, list(sel), n, len(d), list(mode)))
    return {"now": now, "manual": "That the in-game name and text are the CQB Suppressor's is a UI fact; the recoil package effect is in game only."}


# ---------------------------------------------------------------- offer checks (not a bug entry)
def newest(folder, pattern):
    found = sorted(pathlib.Path(folder).glob(pattern))
    if not found:
        sys.exit("no file matching %s in %s" % (pattern, folder))
    return found[-1]


def offer_checks(c, mapping_path, optics_path):
    """What the game menu offers is what Equipment_<Weapon> lists AND whose ability branch is live (kill switch default off).
    (a) site choices with no source record listed; (b) no source both listed and live; (c) records listed, live, not a
    zero-point placeholder, that the site does not offer. Campaign-only routes are not held, so they show as unlisted.
    Sights: site ids (attachments.json WEAPON_ATTS) joined to records by the individual-optics file; iron-sight records
    are not joined (their names vary per weapon) and are left out."""
    held = rawlib.held
    eqkey = {}
    for k in held:
        d, _, n = k.rpartition("/")
        if n.startswith("equipment_"):
            eqkey[d] = k
    listed_cache = {}

    def listed(folder):
        if folder not in listed_cache:
            out = set()
            if folder in eqkey:
                def walk(x):
                    if isinstance(x, dict):
                        if "Field_d28dfb00" in x:
                            i = rawlib.imp(x["Field_d28dfb00"])
                            if i and i[0]:
                                out.add(i[0].lower())
                        for v in x.values():
                            walk(v)
                    elif isinstance(x, list):
                        for v in x:
                            i = rawlib.imp(v) if isinstance(v, dict) else None
                            if i and i[0] and "/attachment_" in i[0].lower():
                                out.add(i[0].lower())
                            else:
                                walk(v)
                walk(rawlib.load(eqkey[folder])[0][0])
            listed_cache[folder] = (out, folder in eqkey)
        return listed_cache[folder]

    wbase = {w.base.rstrip("/"): w for w in c.W}
    rec = {}

    def record(folder, route):
        if folder not in rec:
            rec[folder] = {a["route"].lower(): a for a in wbase[folder].graph["attachments"]} if folder in wbase else {}
        return rec[folder].get(route)

    def live(a):
        return a is not None and any(not b["kill"]["default"] for b in a["branches"])

    def is_placeholder(a):
        return (a["cost"] or 0) == 0 and not any(s["effects"] for b in a["branches"] if not b["kill"]["default"] for s in b["selectors"])

    mp = json.load(open(mapping_path, encoding="utf-8"))
    op = json.load(open(optics_path, encoding="utf-8"))
    att = json.load(open(rawlib.SITE / "data/attachments.json", encoding="utf-8"))
    route = lambda src: (src[:-4] if src.endswith(".xml") else src).lower()
    wfolder, offered = {}, collections.defaultdict(set)
    votes = collections.defaultdict(collections.Counter)
    for ch in mp["choices"]:
        for s in ch["sources"]:
            votes[ch["weapon"]][route(s["source"]).rpartition("/")[0]] += 1
            offered[ch["weapon"]].add(route(s["source"]))
    for w, v in votes.items():
        wfolder[w] = v.most_common(1)[0][0]

    def section():
        return {"choices": 0, "a_noListedSource": [], "b_noListedAndLiveSource": [], "c_listedLiveNotOffered": [], "explained": []}
    res = {"mapping": pathlib.Path(mapping_path).name, "opticsFile": pathlib.Path(optics_path).name,
           "rule": "Offered in game = listed in the weapon's Equipment_<W> lists and live (ability branch kill switch default off). Campaign-only routes are not held and so are unlisted.",
           "nonSight": section(), "sights": dict(section(), notJoined=[]), "noEquipmentFile": []}

    def judge(w, sec, label, srcs):
        folder = wfolder[w]
        lst, has = listed(folder)
        if not has and w not in res["noEquipmentFile"]:
            res["noEquipmentFile"].append(w)
        sec["choices"] += 1
        flags = [(r in lst, live(record(folder, r))) for r in srcs]
        if not any(l for l, _ in flags):
            sec["a_noListedSource"].append({"weapon": w, "choice": label, "sources": srcs, "held": [r in held for r in srcs]})
        elif not any(l and v for l, v in flags):
            sec["b_noListedAndLiveSource"].append({"weapon": w, "choice": label, "sources": srcs, "listedLive": flags})
        elif not all(l and v for l, v in flags):
            sec["explained"].append({"weapon": w, "choice": label, "why": "merged choice: one source record is unlisted or not live, another is listed and live",
                                     "unlisted": [r for r, (l, v) in zip(srcs, flags) if not (l and v)]})

    for ch in mp["choices"]:
        if ch["slot"] != "sight":
            judge(ch["weapon"], res["nonSight"], "%s/%s" % (ch["slot"], ch["attachment"]), [route(s["source"]) for s in ch["sources"]])
    optsrc = {w: {e["id"]: route(e["source"]) for e in lst} for w, lst in op["weapons"].items()}
    iron = {route(e["source"]) for v in op.get("ironSightVariants", {}).values() for e in v.values() if isinstance(e, dict) and e.get("source")}
    notoff = {route(x["source"]) for x in op.get("notOffered", [])}
    sight_offered = collections.defaultdict(set)
    for w, wa in att["WEAPON_ATTS"].items():
        if w not in wfolder:
            continue
        for sid in wa.get("sight", []):
            r = optsrc.get(w, {}).get(sid)
            if r is None:
                res["sights"]["notJoined"].append("%s/%s" % (w, sid))
                continue
            sight_offered[w].add(r)
            judge(w, res["sights"], sid, [r])
    for w, folder in wfolder.items():
        if folder not in wbase:
            continue
        lst, _ = listed(folder)
        for a in wbase[folder].graph["attachments"]:
            r = a["route"].lower()
            sight = a["category"] == "Sight"
            if r not in lst or not live(a) or a["category"] not in CAT_SLOT or a["category"] == "OpticAccessory":
                continue
            if r in offered[w] or r in sight_offered[w]:
                continue
            if sight and ("iron" in a["attachment"].lower() or r in iron):
                continue
            item = {"weapon": w, "record": a["attachment"], "category": a["category"], "points": a["cost"]}
            sec = res["sights"] if sight else res["nonSight"]
            if sight and r in notoff:
                sec["explained"].append(dict(item, why="optics file notOffered: listed and live, the site leaves it out"))
            elif is_placeholder(a):
                sec["explained"].append(dict(item, why="zero-point placeholder with no effect: listed and live, no site choice"))
            else:
                sec["c_listedLiveNotOffered"].append(item)
    res["counts"] = {k: {x: (len(v) if isinstance(v, list) else v) for x, v in res[k].items()} for k in ("nonSight", "sights")}
    return res


RULES = {
    1: ("resolved", r1, "Regression check of a resolved entry: a bolt-action bottom-rail action selects more than one package."),
    2: ("scripted", r2, "An ammunition attachment's ability branch selects U_WPM_AMO_FMJ* in addition to its own ammo package."),
    4: ("scripted", r4, "A live magazine whose description says 'faster reloads' has no reload-speed effect (Class_9705264b) or reload-phase package (Class_7d916d6b) behind its selector."),
    6: ("scripted", r6, "For a muzzle selector that at least 80% of weapons bind to GRM_SmoothRecoil*, the weapon's GS file has no such binding."),
    10: ("scripted", r10, "A live magazine described as 'improved handling' gains none of draw, sprint recovery, ADS time or ADS move speed against the weapon's default (Std) magazine, from the WME_*_P/M tier in the effect names."),
    11: ("scripted", r11, "An optic's WB package has a render FOV (Field_7768ebf2) different from the one most weapons use for the same optic selector."),
    13: ("scripted", r13, "On a bolt-action weapon the Tungsten Core selector does not bind exactly one GRM_Recoil_AMO_Bolt_M10."),
    14: ("scripted", r14, "A weapon with a Burst Mode/Training selector has GRM_* recoil effects bound in its GS file under the U_WPM_ERG_BurstFireActive key, which the attachment selector lacks."),
    15: ("scripted", r15, "A base ReloadInfoArray entry has ReloadTime (Field_85ff24a0) different from ReloadTimeBulletsLeft (Field_fc66e75e) while that value and the end of the phase list (Field_dc244b57) agree."),
    16: ("scripted", r16, "The iron-sight selector (U_WPM_IronSights) lists no WME_WSway_P05; bolt-action rifles are reported separately as by design (entry text)."),
    17: ("scripted", r17, "The in-world spot-on-fire base in the WB root (Field_5ebda408/Field_9918e670) is 75 (the usual value is 54)."),
    18: ("scripted", r18, "The Hollow Point attachment costs no more than the weapon's FMJ ammunition."),
    20: ("scripted", r20, "For a live ammunition x magazine pair, base penetration index + ammo steps + magazine steps passes the 10-row collateral table."),
    21: ("scripted", r21, "A grip selector's GRM_Recoil_BTM_* step differs from the one that at least 60% of weapons bind to the same selector."),
    22: ("scripted", r22, "A bolt-action weapon's Precision table (settings, matched by velocity, tactical reload and magazine) has a fallback row other than 100."),
    23: ("scripted", r23, "A scope that most weapons list in an optic accessory's compatible list (Equipment_*, Field_f4142987) is listed in none on this weapon, which otherwise lists most scopes."),
    24: ("scripted", r24, "A magazine/ammo description 'between Xm and Ym' differs from the span where the swapped-in bullet's damage curve is at least 100 (registry curve applied)."),
    25: ("scripted", r25, "Bipod: the selector binds neither GDM_Array_HipDispersion_BTM_* nor GBM_Increase_ADS_*_BTM_Bipod. Grip pods: an automatic-capable weapon binds no GBM_Increase_ADS_*_BTM_Bipod under the pod selector."),
    26: ("scripted", r26, "A weapon offering single and auto/burst has no GS binding to GBM_NoIncrease_Semi_P00."),
    27: ("scripted", r27, "Suppressors with the same in-game name use different U_WPM_MZL_* selectors across weapons; the weapon differs from the majority."),
    28: ("scripted", r28, "A fire-mode replacement attachment keeps the base weapon's mode set but changes the cycle order (Field_7313f5d3/Field_2a5a28ee)."),
    29: ("scripted", r29, "A weapon's Match Trigger selector U_WPM_ERG_MatchTrigger_W15 resolves to no effect."),
}
MANUAL = {
    3: "resolved (description corrected, 10 Nov 2026); description-only entry, not re-run.",
    5: "removed 14 Oct 2026 (not a bug); nothing to run.",
    7: "resolved (belt-box text corrected, 10 Nov 2026); description-only entry, not re-run.",
    8: "resolved (description corrected, 10 Nov 2026); covered by entry 4's check if the 'faster reloads' claim returns without a reload effect.",
    9: "resolved (SGX Extended Barrel text corrected, 10 Nov 2026); description-only entry, not re-run.",
    12: "resolved (L115 binds hip dispersion for the Standard Suppressor, 10 Nov 2026); not re-run.",
    19: "resolved (RSPR brake has one recoil step, 10 Nov 2026); not re-run.",
}
TITLES = {1: "Slim Angled unstated moving-ADS penalty", 2: "Special ammo keeps the FMJ package", 4: "Fast magazine without reload bonus",
          6: "Flash Comp without recoil smoothing", 10: "50 Rnd 'improved handling' text", 11: "Optics use the default render FOV",
          13: "Tungsten Core recoil penalties inconsistent", 14: "Burst attachments bound to the runtime token", 15: "Empty reload ReloadTime mismatch",
          16: "Iron sights without sway reduction", 17: "Spot-on-fire range 75 m", 18: "Hollow Point costs as much as Standard",
          20: "Collateral row passes the table", 21: "Grips reduce recoil one step more", 22: "Bolt-action Precision fallback row",
          23: "Scope removes the Optic Accessory slot", 24: "Single Shot sweet spot wider than text", 25: "Deployed bipod/pods without spread binding",
          26: "No semi-auto bloom removal", 27: "Suppressor bound to another selector", 28: "Burst Training reverses the fire-mode cycle",
          29: "Match Trigger has no effect"}


def run(c, only):
    result = {}
    for n in sorted(set(RULES) | set(MANUAL)):
        if only and n not in only:
            continue
        if n in MANUAL:
            result[n] = {"entry": n, "status": "manual", "why": MANUAL[n]}
            continue
        kind, fn, rule = RULES[n]
        try:
            r = fn(c)
        except Exception as e:   # a missing file or field: report it, never guess
            import traceback
            result[n] = {"entry": n, "title": TITLES[n], "status": "error", "rule": rule, "error": repr(e), "trace": traceback.format_exc()[-600:]}
            continue
        if "error" in r:
            result[n] = {"entry": n, "title": TITLES[n], "status": "error", "rule": rule, "error": r["error"]}
            continue
        now = r["now"]
        listed = LISTED.get(n, [])
        text = ALSO_IN_TEXT.get(n, [])
        newly = sorted(k for k in now if k not in listed and k.split(" (not on site)")[0] not in listed and k.split(" (not on site)")[0] not in text)
        in_text = sorted(k for k in now if k not in listed and k.split(" (not on site)")[0] in text)
        gone = sorted(k for k in listed if k not in now and k + " (not on site)" not in now)
        result[n] = {"entry": n, "title": TITLES[n], "status": "resolved-regression" if kind == "resolved" else "scripted", "rule": rule,
                     "listed": listed, "now": sorted(now), "newlyAffected": newly, "noLongerAffected": gone,
                     "alsoNamedInEntryText": in_text, "evidence": {k: now[k] for k in sorted(now)}}
        for k in ("notes", "manual", "byDesign", "byDesignReason", "alsoDiffers"):
            if r.get(k):
                result[n][k] = r[k]
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("raw", help=r"<data>\builds\<build>\capture\collection\raw")
    ap.add_argument("--out", default="bug-rules.json")
    ap.add_argument("--only", help="comma-separated entry numbers")
    ap.add_argument("--mapping", help="site-to-game mapping for the offer checks (default: newest frosty-site-attachment-mapping-*.json)")
    ap.add_argument("--optics", help="individual-optics file for the sight offer checks (default: newest in the Analyzer reference-data/provenance)")
    a = ap.parse_args()
    build, work = setup(a.raw)
    load_readers()
    c = Ctx()
    only = {int(x) for x in a.only.split(",")} if a.only else None
    res = run(c, only)
    out = {"date": datetime.date.today().isoformat(), "build": build.name, "rawFolder": str(pathlib.Path(a.raw).resolve()),
           "weaponsRead": len(c.W), "weapons": [w.name for w in c.W], "entries": {str(k): v for k, v in res.items()}}
    mapping = a.mapping or newest(rawlib.REPO / "reference-data/provenance", "frosty-site-attachment-mapping-*.json")
    optics = a.optics or newest(rawlib.SITE / "reference-data/provenance", "frosty-individual-optics-*.json")
    out["offerChecks"] = offer_checks(c, mapping, optics)
    pathlib.Path(a.out).write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    oc = out["offerChecks"]
    for sec in ("nonSight", "sights"):
        print("offerChecks %-8s choices %d | a %d | b %d | c %d | explained %d" % (sec, oc[sec]["choices"], len(oc[sec]["a_noListedSource"]),
              len(oc[sec]["b_noListedAndLiveSource"]), len(oc[sec]["c_listedLiveNotOffered"]), len(oc[sec]["explained"])))
    for n, v in res.items():
        if v["status"] == "manual":
            print("%2d  manual     %s" % (n, v["why"]))
        elif v["status"] == "error":
            print("%2d  ERROR      %s" % (n, v["error"]))
        else:
            print("%2d  %-10s now %-2d new %s | gone %s | in text %s" % (n, v["status"][:10], len(v["now"]), v["newlyAffected"], v["noLongerAffected"], v["alsoNamedInEntryText"]))
    shutil.rmtree(work, ignore_errors=True)
    print("wrote", a.out)


if __name__ == "__main__":
    main()
