"""Write REPORT.md from validate.json, structure.txt, propose-notes.json and proposed.json."""
import json, collections
V = json.load(open("validate.json", encoding="utf-8")); N = json.load(open("propose-notes.json", encoding="utf-8"))
P = json.load(open("proposed.json", encoding="utf-8")); A = P["data/attachments.json"]; T = P["data/attachment-tooltips.json"]
ST = [l.rstrip("\n") for l in open("structure.txt", encoding="utf-8-sig", errors="replace")]
tot = V["totals"]; L = []
def w(*a): L.append(" ".join(str(x) for x in a))
w("# Stage 9 part C: attachments\n")
w("Everything below is read from raw 2.1.1.0 EBX files and the `GRX_Weapons` registry. No site or research-repo file was changed.\n")
w("## Files in this folder\n")
w("- `proposed.json`: fragments keyed by target file, then by JSON path. `X[id=foo]/frostyModifiers/mk24` means the `mk24` key inside that catalogue entry; `GRIPS[+]` is a new catalogue entry; `WEAPON_ATTS/<w>/grip[+]` appends one id to that list.")
w("- `propose-notes.json`: evidence per proposed value (raw record, stored cost, in-game name, identity basis, raw effect fields, flags), the Actuated Module rows, and the optic members.")
w("- `rawlib.py`, `graph.py`, `weapons.py`, `identity.py`, `ui.py`, `derive.py`, `structure.py`: the derivation. `validate.py` and `structure.py` are the two comparisons against the site; `propose.py` writes the proposal; `report.py` writes this file.")
w("- `validate.json`, `validate.txt`, `structure.txt`, `propose.txt`: full outputs. `cache/`: decoded graph of each of the 67 weapons. Other small `.py` files are inspection helpers.\n")
w("## Validation against the 63 existing weapons\n")
w("Identity was tested leave-one-out: each weapon's records were identified using only the other 62 weapons' reviewed mapping (`frosty-site-attachment-mapping-2026-09-15.json`, 3,015 non-sight source rows).\n")
w("| Check | Match | Mismatch | Note |\n|---|---|---|---|")
w("| Stored point cost equals site points | %d | %d | Convention confirmed: the file value is the site `pts`. The `_Wnn` suffix on a selector name is not the cost. |" % (tot["cost ok"], tot.get("cost MISMATCH", 0)))
w("| Effect fields (per selection, all modelled handling, recoil, spread, sway and reload fields) | %d | %d | See below. |" % (tot["field ok"], tot["field MISMATCH"]))
w("| Identity, leave-one-out | %d | %d wrong, %d not resolved | Plus %d magazines, whose id comes from capacity, not from other weapons. |" % (tot["identity ok"], tot["identity MISMATCH"], tot["identity unresolved"], tot["identity mag (by capacity)"]))
w("| Availability lists (muzzle, barrel, grip, laser, light, ergo, magazine; 7 per weapon) | %d | %d | See below. |" % (tot["list ok"], tot["list MISMATCH"]))
w("| Tooltip description id | %d (+%d with no description on either side) | %d | See below. |" % (tot["tooltip ok"], tot["tooltip absent both"], tot["tooltip MISMATCH"]))
w("| Live raw records with no site choice | | %d | See below. |" % tot["record not on site MISMATCH"])
import re
sc = collections.OrderedDict()
for l in ST:
    m = re.match(r"\s*(\d+) (.+) (ok|MISMATCH|raw-1|raw|OTHER)$", l)
    if m: sc.setdefault(m.group(2), {})[m.group(3)] = int(m.group(1))
for k, v in sc.items():
    if k in ("mag id", "mag name"): continue
    w("| Structure: %s | %d | %d | |" % (k, v.get("ok", 0), v.get("MISMATCH", 0)))
w("| Magazine id from capacity and in-game name | %d | %d | %d ids use stored capacity minus one, %d use it unchanged. |" % (sc["mag id"].get("raw-1", 0) + sc["mag id"].get("raw", 0), sc["mag id"].get("OTHER", 0), sc["mag id"].get("raw-1", 0), sc["mag id"].get("raw", 0)))
w("| Sight category of each raw sight vs the site optic mapping | 1,930 | 1 | `grtcps` NX8-4: its descriptor is not in the capture. Labels match on 1,929 of 1,931. |")
w("| Sight tooltip = lowest description id among category members | %d | %d | |" % (N["validation"]["sightTooltipRule"].get("sight tooltip == min id of category members", 0), N["validation"]["sightTooltipRule"].get("sight tooltip differs", 0)))
w("")
w("The four classes asked for are all inside the 63: for example `m4a1` (AR), `m2010esr` and `l115` (sniper), `m240l` (LMG), `kv9` and `sgx` (SMG). Per-weapon counts are in `validate.json` under `perWeapon`.\n")
w("### Every mismatch and its cause\n")
mm = V["mismatches"]; g = collections.defaultdict(list)
for x in mm: g[x[1]].append(x)
w("**Effect fields (%d).**" % len(g["field"]))
fc = collections.defaultdict(list)
for x in g["field"]: fc[(x[2], x[3] if x[2] != "mag" else "(magazine)", x[4], x[5], x[6])].append(x[0])
for k, ws in sorted(fc.items()): w("- %s `%s` `%s`: %s, %s. Weapons: %s." % (k[0], k[1], k[2], k[3], k[4], ", ".join(ws)))
w("\nCauses: the burst-mode and burst-training values (variation +3, duration -0.0006, GRT-BC amount +1) are not attachment modifiers in the raw graph; the site takes them from the fire-mode data, so this script cannot see them. `canted_vertical` hip spread -2 is the `GDM_Array_HipDispersion_BTM_P20_NoBipod` binding, which this script treats as conditional; the site applies it for this one grip. The `m121a2` magazine reload tier is the site's value for `50_fast`, where the raw record has no reload-speed operand. None of these affect a value proposed below except `canted_vertical` on `z84m`, which keeps the catalogue value.\n")
w("**Identity (%d wrong, %d not resolved).** All are ids used by one weapon only, which leave-one-out cannot learn by construction: the `_ks18k`, `_svk86`, `_db12`, `_sl9`, `_lmr27`, `_interdictor` grip variants, `bipod`/`bipod_sr` on the two DMR-class users, the SL9/GRT-BC burst-mode pair, `subsonic_pen`, sidearm bottom-rail lasers and lights (this script only tries the grip slot for bottom-rail records, which is right for primaries), single-weapon barrels and ammo, and three sniper brakes where the same selector carries three site names. None of the four new weapons hits an unlearnable case: 161 of 161 identified non-magazine records have package effects identical to an existing weapon's record with the same id.\n")
w("**Availability lists (%d).**" % len(g["list"]))
for x in g["list"]: w("- `%s` %s: %s; %s. Cause: these records have their kill switch on by default in 2.1.1.0, so this script leaves them out; the site still lists them." % (x[0], x[2], x[3], x[4]))
w("\n**Live raw records with no site choice (%d).**" % len(g["record not on site"]))
rc = collections.defaultdict(list)
for x in g["record not on site"]: rc[x[2]].append(x[0])
for k, ws in sorted(rc.items(), key=lambda kv: -len(kv[1])): w("- `%s` (%d): %s" % (k, len(ws), ", ".join(ws)))
w("\nCauses: `BTM_ACEModule` is deliverable C2. `AMO_PolymerLinks` and `AMO_BallisticTip` are ammo records not on the site (ammo is outside part C; flagged for the main session). The two `LA-23IRSP` records are the reviewed exclusions in `frosty-handling-mapping-followup.json`. The rest are records that are live in 2.1.1.0 on existing weapons and that the site does not offer; I did not determine whether they are new in 2.1.1.0 or deliberately left out. They are existing-weapon issues and are not fixed here.\n")
w("**Tooltips (%d).**" % len(g["tooltip"]))
tc = collections.Counter()
for x in g["tooltip"]:
    tc["site uses an approved screenshot text" if x[5].startswith("site screenshot") else "raw link found no single description (descriptor not in the capture, or linked descriptors disagree)" if x[4] == "raw None" else "different id"] += 1
for k, v in tc.items(): w("- %d: %s." % (v, k))
w("\n**Structure.**")
w("- `accessory` (50 of 63): `avail` matches everywhere; only `excludedSights` differs. The raw 2.1.1.0 `Equipment_<W>` lists now permit sights the site still excludes (on `m4a1` the Canted Iron Sights list ends with `SCP_M145MGO` and `SCP_QMK171A`, which are the site's excluded 3.50x and 3.00x labels). Likely cause: the site lists predate these additions. I could not check an older build. Dependencies at category level match 63 of 63.")
w("- `barrelDef`: rule used is `basic` if offered, else `heavy`. One miss: `vssm` (`vssm_suppressed`).")
w("- `iron sway`: `pp19` raw product 0.5481276, site 0.6666667 (its iron sight record carries a second sway object).")
w("- `defAds anim==fov`: `l115` registry animation index 2, zoom-transition index 1; the site uses 1.")
w("- Magazine id misses: `m87a1`, `m1014`, `svdm` (site fast/rnd naming does not follow the in-game name), `db12` (two tubes), `m121a2`, `kts100` (belt weapons whose magazine package stores the capacity without the extra round).\n")
w("## C1: the four new weapons\n")
w("Counts of proposed choices:\n\n| Weapon | Muzzle | Barrel | Grip | Laser | Light | Ergo | Magazine | Sights (records) | Left out |\n|---|---|---|---|---|---|---|---|---|---|")
for wid, n in N["weapons"].items():
    c = n["counts"]
    w("| `%s` | %d | %d | %d | %d | %d | %d | %d | %d | %s |" % (wid, c["muzzle"], c["barrel"], c["grip"], c["laser"], c["light"], c["ergo"], c["mag"], c["sights"],
      "; ".join("`%s` (%s, cost %s)" % (s["stem"], s["reason"], s["cost"]) for s in n["skipped"] if s["cost"] or "kill" in s["reason"]) or "none"))
w("\nGrip counts include the Actuated Module where the weapon has it. RSPR underbarrel matches the in-game list: Vertical 10, 20, 20, 25, 35; Stubby 20, 30, 30, 35, 45; Handstop 10; Angled 20; Actuated 10; `BTM_DDVertical` (30) is left out because its kill switch is on by default. Stored cost equals catalogue `pts` for every identified record on all four weapons (no cost flag was raised).\n")
w("Identity came from selector sets shared with existing weapons. There are no new catalogue stems on these weapons other than the Actuated Module: HUXFH762, KX5, Rotor43, Titan, CDX64, the M84 flash hider and the weapon-specific barrels use selector sets that existing site ids already use, and their package effects are identical to an existing weapon's record with that id (161 of 161).\n")
for wid, n in N["weapons"].items():
    w("### `%s`\n" % wid)
    b = n["structure"]["baseIndexSources"]
    w("- Base indices: " + "; ".join("%s file %s, registry %s" % (k, v.get("file", "not found"), v.get("registry", "no row")) for k, v in b.items()) + ".")
    m = A["WEAPON_MAG/" + wid]
    w("- `WEAPON_MAG`: defAds %s, defAms %s, sprintRecoveryBaseIndex %s, deployBaseIndex %s, deployTimeTable %s, def `%s`." % (m["defAds"], m["defAms"], m["sprintRecoveryBaseIndex"], m["deployBaseIndex"], m["deployTimeTable"], m["def"]))
    for i, info in n["mags"].items():
        e = m["mags"][i]
        w("  - `%s`: `%s`, cost %s, in-game name %r, stored capacity %s from the %s, reload tier %s." % (i, info["stem"], info["cost"], info["inGameName"], info["capacityRaw"], info["capacitySource"], e["reloadSpeedTier"]))
    w("- Sight costs by category: %s. Iron-sight sway: %s." % (json.dumps(n["structure"]["sightCosts"]), n["structure"]["ironSway"]))
    ov = {k: v for k, v in A.items() if k.endswith("/weaponOverrides/" + wid)}
    if ov: w("- Per-weapon muzzle or ergo overrides: " + "; ".join("`%s` %s" % (k.split("/")[0], json.dumps(v)) for k, v in ov.items()) + ".")
    fl = [f for f in n["flags"] if "Hybrid Suppressor" not in f and "Taclight - Hip" not in f and "Adjustable Angled '" not in f]
    for f in fl: w("- Flag: " + f)
    for u in n["unresolved"]: w("- Not identified: %s `%s`, cost %s, in-game name %r. Raw fields: %s." % (u["slot"], u["stem"], u["cost"], u["inGameName"], json.dumps({k: v for k, v in u["raw"].items() if v not in (0, 1, None)})))
    w("- Description not found (descriptor asset not in the capture, or no single text): " + ("; ".join(n["tooltipMissing"]) or "none") + ".")
    w("")
w("Name-only differences that are already present on existing weapons and were not treated as problems: \"Hybrid Suppressor (L/K/S)\", \"Taclight - Hip\", \"Adjustable Angled \" with a trailing space.\n")
w("### Judgement calls in C1\n")
w("1. `rspr` Single-Port Brake: `GS_RSAR999` binds selector `U_WPM_MZL_Brake1_W05` to both `GRM_Recoil_MZL_P10` (+1) and `GRM_Recoil_MZL_Bolt_P10` (+6). I summed them (7), following the site's precedent of summing combined steps. No existing weapon has this double binding. Needs an in-game check.")
w("2. `mk24` and `z84m` bind stronger recoil modifiers than other weapons for three grips: Adjustable Angled `GRM_Recoil_BTM_P20` (others P10), Full Angled and QD Grip Pod `GRM_Recoil_BTM_P30` (others P20). Written as `adsRecoilTierMod`/`hipRecoilTierMod` inside `frostyModifiers`, the shape the site already uses for `qd_grip_pod` on `brod3`, `ef88`, `m16a4`. There is no existing precedent for the two angled grips. Worth one in-game look.")
w("3. `elr40` `MZL_CDX40MB` (\"Multi-port Brake\", cost 10) is mapped to `dp_brake`, as the site does for the same selector, name and cost on `interdictor`. The site will show \"Double-Port Brake\".")
w("4. `elr40` `MZL_CDX-40CDX64Suppressor` (in-game \"CQB Suppressor\", cost 30) uses selector `U_WPM_MZL_ImprvdSuppressor02_W30`, which is `light_supp` on the site (`sv98` is the precedent; sniper `cqb_supp` uses `ImprvdSuppressor01`). I kept `light_supp` with the raw values as a per-weapon override. The site name will read \"Lightened Suppressor\"; the main session should decide whether that is acceptable.")
w("5. `z84m` has three 100-round magazines. Ids `100_rnd` (Metal Box, the default), `100_fast` (Polymer Box, reload multiplier 1.13) and `100_pouch` (Canvas Pouch) are my naming; the site has no precedent for a third same-capacity magazine.")
w("6. `elr40` \"Single Shot\" stores capacity 1. I wrote `mag: 1` (`1_rnd`), not 0. The other magazines follow stored capacity minus one, which their in-game names confirm (8 -> \"7rnd\", 6 -> \"5rnd\").")
w("7. `barrelDef` is `basic`, or `heavy` on `z84m`, by the rule that matches 62 of 63 existing weapons. It is not the in-game \"Factory\" barrel (that rule matched only 31).")
w("8. Magazine `name` uses the site's \"N Rnd\" / \"N Fast\" form, not the in-game model name.")
w("9. Order inside each availability list follows catalogue order; the site's own order is not derivable.\n")
w("### Not found\n")
w("- `tacRldOverrideMs` for magazines (animation data; the site has it on belt magazines such as `m240l`). Not derived for `z84m`.")
w("- Descriptions listed per weapon above. Captures needed: `Shared/AD_ACEModule`, `Shared/AD_DDVertical`, the weapon-specific `Attachments/{MRGGA,CDX40,PKM,RSAR999}/AD_*` assets (barrels, magazines, iron sights, PKM muzzle and bipod, RSAR999 `ERG_Flare`), `AD_Shared_ERG_RailCover_3SlotMlok` and `_4SlotMlok`, `AD_Shared_MAG_PMAG20rnd762N`, `AD_CDX64Suppressor`, `AD_Rotor43`, `AD_Titan762_Supp1`.")
w("- Iron-sight tooltip for `mk24`, `elr40`, `z84m` (same cause). `rspr` has it (`0BB6AC0B`).")
w("- `rspr` has no `GRX_Weapons` rows for its base indices and no `AnimationZoomSettingsIndex` value; the file values are used.")
w("- `z84m` `AMO_PolymerLinks` (\"Polymer Links\", cost 10) is an ammo record with no site id. It is also live on six existing LMGs. Ammo belongs to the other parts.")
w("- Catalogue fields that are not per-weapon (velocity, suppression, spotting, utilities) were not re-derived; the package-signature check stands in for them.\n")
w("### Provenance the site tests will ask for\n")
w("- `scripts/optic-costs.test.mjs` reads the latest `reference-data/provenance/frosty-optic-category-mapping-*.json` and needs every site weapon in it. `proposed.json` carries the members (source route, label, stored cost) for the four weapons under the third top-level key; the labels for sights whose descriptor is weapon-specific were taken from the same optic model and selector on other weapons (`labelBasis`).")
w("- `scripts/draw-time.test.mjs` compares base indices with `frosty-draw-time-2026-09-09.json` and needs one row per weapon.\n")
w("## C2: Actuated Module\n")
ace = N["ace"]; rows = [r for r in ace["rows"] if r["live"]]
w("Raw package `WPM_BTM_Actuated_W10` (selector `U_WPM_BTM_Actuated_W10`), identical on all %d weapons that have the record: weapon sway x0.666667 (all seven fields), camera sway x0.666667 (all seven fields), dynamic pivot 0.75 on both vectors. No GS binding, so no recoil, spread, ADS, sprint or deploy effect; stored cost 10 everywhere; physical slot `SC_BottomRail`; no `Equipment` rule mentions it.\n" % len(rows))
w("Strings: `FCC2C91E` \"%s\" (the AAM in-game name), `6FBF09F4` \"%s\", `6FC0BDFC` \"%s\". The description id is a unique text match in the string table; `AD_ACEModule` is not in the capture, so the pointer from the attachment to that string is not proven.\n" % (ace["strings"]["FCC2C91E"], ace["strings"]["6FBF09F4"], ace["strings"]["6FC0BDFC"]))
w("Proposed: `GRIPS[+]` `{id: actuated_module, name: Actuated Module, pts: 10, weaponSwayMult: 0.6666667, frostyModifiers: {<weapon>: all four zero}}`; `WEAPON_ATTS/<w>/grip[+]` for each weapon below; tooltip `byWeapon/<w>/grip/actuated_module = 6FC0BDFC` and `descriptions/6FC0BDFC`.\n")
w("What the site model can represent: only the weapon-sway multiplier, and only after a code change. `sim/applyAttachments.js` multiplies sway from the muzzle, magazine, barrel and sight; a grip `weaponSwayMult` is currently ignored. Camera sway and the dynamic pivot (the \"changing stances\" part of the description) are not modelled at all (`docs/ATTACHMENT_MODEL.md`).\n")
w("Weapons: %d existing site weapons and three new ones (`mk24`, `elr40`, `rspr`) have a live record. `z84m` has no `Attachment_PKM_BTM_ACEModule` record. The brief expected 54 kill-switch rows; rows for weapons outside the site roster were not counted here.\n" % sum(not r["new"] for r in rows))
w("Uncertain: the weapon's own AAM (the UI list) names the Actuated Module on only 7 of the 36 existing weapons, and on five site weapons the AAM names it with no attachment record (`cz3a1`, `l115`, `pp19`, `vcr2`, `z84m`). RSPR, confirmed in game, has both. I have not established whether a record without an AAM entry is offered in game. One in-game look at `m4a1` (record, no AAM entry) and one at `l115` (AAM entry, no record) would settle it. The table marks which is which.\n")
w("| Site id | Raw record | Stored cost | Kill-switch row (default) | In the weapon's AAM |\n|---|---|---|---|---|")
for r in sorted(rows, key=lambda r: (r["new"], r["weapon"])):
    w("| `%s`%s | `%s` | %s | %s | %s |" % (r["weapon"], " (new)" if r["new"] else "", r["record"], r["storedCost"], "; ".join(k.split("/", 1)[-1] for k in r["killSwitch"]), "yes" if r["inOwnAam"] else "no"))
w("")
w("## Hard-coded counts the attachment additions would change\n")
w("Found by pattern search in `scripts/` and `docs/`; the search is not exhaustive.\n")
for l in [
 "`scripts/attachment-effects.test.mjs:694` `assert.equal(count, 17)`: muzzle overrides with `recoilDurationOverride 0.066667`. The `elr40` `long_supp` and `light_supp` overrides make it 19.",
 "`scripts/fire-modes.test.mjs:24,26`: \"all 63 implicit defaults\", `fixture.cases.length, 73` (`scripts/fixtures/fire-mode-defaults.json`).",
 "`scripts/draw-time.test.mjs:22`: \"all 63 base selectors\"; it also requires `evidence.weaponIndices.length == weapons.length`.",
 "`scripts/optic-costs.test.mjs`: no literal count, but fails unless the optic mapping covers every site weapon.",
 "`scripts/frosty-projectile-site-functions.mjs:70` and `scripts/frosty-projectile-lifetime.py:111,169,182,248`: 328 ammo selections, 64 projectile routes (ammo side, listed for completeness).",
 "`data/attachment-tooltips.json` `coverage`: `aamAssets 64`, `nonSightChoices 3011`, `mappedSelections 2966`, the `descriptionStatuses` and `matchMethods` counts, `ironSightTooltips 63`.",
 "`README.md:57`: \"Iron Sights on all 63 weapons\".",
 "`docs/ATTACHMENT_MODEL.md:84`: \"234 source records\" (barrels; +13).",
 "`docs/DATA_REFERENCE.md:79`: \"233 unique selections (234 source records)\"; lines 29, 33, 143: 63 weapons, 328 ammo choices.",
 "`docs/DATA_SOURCES.md:39`: \"233 unique barrel selections, 1,487 handling selections, 16 sniper brake ...\"; line 214: \"all 63 weapons ... 17 weapon-muzzle exceptions\"; line 6: 328 ammo choices.",
 "`docs/RECOIL_SPREAD_MODEL.md:172`: \"these 17 mapped selections\" (the list that follows needs the two `elr40` rows).",
 "`docs/TESTS.md:42`, `docs/STAT_LADDERS.md:66`, `docs/DAMAGE_BALLISTICS.md:50,116`, `docs/MODEL_LIMITATIONS.md:63,150`, `docs/WEAPON_ATTRIBUTES_MODEL.md:303`: \"63 weapons\" and \"328 ammo\" statements.",
 "`scripts/validate-data.mjs` has no literal weapon or selection count; lines 288-292 check `barrelDef` against the barrel list."]:
    w("- " + l)
w("")
w("## Needs an in-game check\n")
for l in ["RSPR Single-Port Brake recoil (+7 combined, or +1).", "Mk 24 and Z84M: Adjustable Angled, Full Angled and QD Grip Pod recoil one step stronger than on other weapons.",
          "ELR-40: \"CQB Suppressor\" behaviour and name; \"Single Shot\" capacity; whether the Canted Iron Sights and Secondary Optic exclusions match.",
          "Z84M: reload times of the three belt boxes (no `tacRldOverrideMs` derived).",
          "Actuated Module on a weapon with a record but no AAM entry (`m4a1`), and on one with an AAM entry but no record (`l115`).",
          "Existing weapons: `sv98` Hybrid Suppressor K/S and `interdictor` Lightened Suppressor are kill-switched in 2.1.1.0 but still listed on the site."]:
    w("- " + l)
open("REPORT.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("written", len(L), "lines")
