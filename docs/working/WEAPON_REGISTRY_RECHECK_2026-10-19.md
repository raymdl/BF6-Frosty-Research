# Weapon registry recheck on build 2.1.1.0 (19 October 2026)

Research only. Re-run of the 10 October weapons registry checks (L4000, L4002, L4003, L4004 on build 1.4.3.5) and of the 30 September fire-mode extraction (L604) on the open build, to see which stored, registry and site values moved. Nothing here is an in-game reading, and no site data, simulation or UI change is authorized. Nothing was captured, committed or pushed.

## Method

All commands run from the run folder `C:\Users\royal\Documents\BF6 Datamining\builds\2.1.1.0\reports\weapon-registry-recheck-2026-10-19` (`common.py` points the repo decoder at `builds/2.1.1.0` and `capture/toolchain/SharedTypeDescriptors.ebx`; every route was already in `capture/collection/raw`, so no capture). Scripts are copies of the 10 October ones from `reports/weapon-analyzer-research/2026-10-10-weapons-registry` with the build changed.

1. `python allrows.py` reads every named value row of every `GRX_*` registry (34,340 rows; 32,512 on 1.4.3.5, the file `2026-10-09-registry-rows/allrows.json`).
2. `python owncmp.py` groups rows by owner and suffix and picks, for each suffix, the decoded leaf path that equals the registry default on the most owners. Control: restricted to the 63 site weapons' `_WB` and `GS_` files and the site's bullet files, the pairing gives 2,771 / 11,500 / 567 values over 60 / 206 / 13 row names, exactly the 10 October counts (L4000), and the same paths.
3. `python recheck.py` (reads the old side from `builds/1.4.3.5` raw only: that folder also holds a 2.1.1.0 capture under `reports/client-2110-check-2026-10-13`, which the repo's `raw_files()` would prefer by file time; `recheck.py` excludes it) writes `registry-diff-site.json` (registry rows of the site owners, old against new), `own-diff-site.json` (every numeric leaf of 190 site owner files, old against new, 198,748 leaves compared), `pair-status.json` (registry default against own value per row, both builds). `python own-summary.py` classifies the leaf differences.
4. `python curves.py` then `python curve-compare.py`: own and registry-default damage curves of all 94 bullet files (88 on 1.4.3.5, `curves-all.json` of the 10 October run), and the site's `dmg` lists against the 2.1.1.0 own health curve.
5. `python site-compare.py` (the 10 October `w1/build.py`: site `bulletVel`, `rpm`, `mag`, `tacRld`, `emptyRld` against registry rows, 441 records on the 63 weapons) and `python site-values.py` (adds `fireModes` rates, recoil direction and decrease-time exponent, drag, gravity, for the 67 weapons now in `weapons.json`, and diffs the 441 records against the 10 October `w1/compare.json`).
6. `python names.py` (L4002 value-match naming; same threshold as 10 October: leaf equals the row default on at least 90 percent of owners, at least two distinct defaults) against `FIELD_MAP.md`, `OPEN_QUESTIONS.md` and the 116 negative closures (`negative-leads-116.json`, the 10 October list).
7. `python firemodes.py`, `python firemodes2.py`, `python mt3.py`, `python guid-search.py`: the six `FireLogic` fields and the alternate-mode list of each `_WB` file (same field paths as `join.py` of the 30 September run), the 12 mode-changing modifier files, and the Match Trigger / `CMU_SemiAuto` imports.
8. `python rawcheck-manifests.py` runs `scripts/frosty-raw-check.py --manifest` on three manifests (`raw-check-manifest-*.json`, output `raw-checks-*.json`): 1,500 registry/own pairs, 259 curve points, 402 fire-mode fields. All 2,161 match. The GUID searches for the Match Trigger result are in `guid-search.json`.

## Source assets

Registries: `Common/GameSetup/Tweakables/GameRemixer/GRX_Weapons` (and the other `GRX_*`). Weapon files `Common/Hardware/Weapons/<class>/<name>/<name>_WB`, firing data `GS_<name>`, bullets `Common/Hardware/Weapons/_Bullets/PD_*`, mode modifiers `_WeaponModifiers/_Ergo/FireMode/*`, `_Ergo/CMU_SemiAuto`. Crosswalk of the 63 site weapons: `crosswalk-1.4.3.0.json` (copy of the 10 October file); the four Season 5 weapons added to the site are `MRGGA` (Mk 24), `CDX40` (ELR-40), `PKM` (Z84M), `RSAR999` (RSPR). Site files: `BF6 Weapon Analyzer/data/weapons.json` (67 weapons), `ballistics.json`, `attachments.json`. Old side: `builds/1.4.3.5/reports/client-60769-check-2026-10-03/collection/raw`. New side: `builds/2.1.1.0/reports/client-new-check-2026-10-15/collection/raw` (hotfix capture; the 15 October hotfix changed no weapon file).

## Result

- **Registry against own value (L4000 repeated).** 14,838 values over 279 row names on the 63 weapons' `_WB`, `GS_` and bullet files compared on both builds: **0 differing on 1.4.3.5, 0 differing now.** The only 6 values on these rows whose default moved are M39 EMR and SVDM recoil rows (`GS_M39EMR`, `GS_SVDM`); the own value moved with them (rows equal). No pair started or stopped differing. New rows reach 1,054 more equal pairs on the 4 Season 5 weapons and 89 on existing files (see "Added rows").
- **All-owner count.** The same pass over every owner: 74 registry-against-own differences on 1.4.3.5, 98 now (25 new, 1 resolved, 7 moved on the registry side). All are vehicle, gadget and launcher owners (`PD_Vehicles_*`, `SupplyPouch_WB`), the pairs the roster refresh of the same day already lists; none is a site weapon.
- **Own values.** 2,006 numeric leaf differences over 74 of the 190 site owner files; every one falls in six classes (table below). Value changes on stats: spot-on-fire base 54 to 75 on four weapons, the two GS recoil rows, the `Field_f2d603de` class profile on two weapons, and 13 armor damage curves.
- **Bullet damage curves (L4004 repeated).** Health curves: no change on the 69 bullet files that have both an own and a registry curve; registry equals own on all of them (3 files have an own curve and no registry curve, as before). Armor curves: 13 bullet files changed, own and registry together, equal on both builds (table). Site `dmg` lists against the own health curve: on the 63 existing weapons 59 equal, 3 equal with an added 0 m point (M250, M277, Mini Scout) and 1 differing (M45A1, the reviewed 54 to 75 m step), the same split as on 10 October with no own curve moved; the four new weapons' lists equal their curves.
- **Site against source.** Nothing on the 63 existing weapons moved: all 441 records of the L4003 comparison have the same registry value, site value and equality as on 10 October (velocity 63 of 63, magazine 63 of 63, rate of fire 55 of 63 with the same eight manually cycled or single-fire weapons). Fire-mode rates, recoil direction, decrease-time exponent, drag and gravity equal the 2.1.1.0 source on every weapon that has a row (709 comparisons: 686 equal, 13 with no registry row to compare (RSPR `_WB`, BROD 3 firing data `GS_BREN3`, the RPK-74M and VSSM bullet files; the RSPR velocity, magazine and rates, the BROD 3 recoil and the RPK-74M and VSSM drag read from the own file equal the site), 10 unequal: nine rates (the VSSM single-fire rate, seven manually cycled weapons as on 10 October, and the new bolt-action ELR-40) and the ELR-40 magazine below). The 13 October site edits (SVDM direction 20 and exponent 1.1, M39 EMR exponent 1.0) equal the source. One value does not match: the ELR-40 (see open items).
- **Registry rows added (L4002).** See below. No new field name.
- **Fire modes (L604).** Base mode list and the five rates are unchanged on all 63 weapons; the 12 mode-changing modifier files are byte-identical. The SGX (`MPX_WB`) and L110 (`Minimi_WB`) lost the `_Ergo/CMU_SemiAuto` import (details below).

## Registry defaults that changed on site owners (6 rows)

| Owner | Row | Old | New | Own value (same offset in the owner file) |
| --- | --- | --- | --- | --- |
| `GS_M39EMR` (M39 EMR) | `Recoil.Unzoomed.RecoilDecreaseTimeExponent` | 0.75 | 1.0 | 1.0 |
| `GS_M39EMR` (M39 EMR) | `Recoil.Zoomed.RecoilDecreaseTimeExponent` | 0.75 | 1.0 | 1.0 |
| `GS_SVDM` (SVDM) | `Recoil.Unzoomed.RecoilDecreaseTimeExponent` | 0.75 | 1.1 | 1.1 |
| `GS_SVDM` (SVDM) | `Recoil.Zoomed.RecoilDecreaseTimeExponent` | 0.75 | 1.1 | 1.1 |
| `GS_SVDM` (SVDM) | `Recoil.Unzoomed.RecoilDirection` | 4 | 20 | 20 |
| `GS_SVDM` (SVDM) | `Recoil.Zoomed.RecoilDirection` | 4 | 20 | 20 |

The site already holds these (13 October edit). Offsets in `pair-status.json`, raw-checked in `raw-checks-registry-own.json`.

## Own-value differences by class (2,006 leaves, site owner files)

| Class | Changed | Added | Removed | Owners | Reading |
| --- | --- | --- | --- | --- | --- |
| GS modifier-list priority index (`Field_2296f84f[n]`, `Field_a2bef75b[n]` / `Field_3f680d24`) | 260 | 56 | 0 | 56 `GS_` | Index shifts: two foregrip entries (`WPM_BTM_Actuated_W10`, `WPM_BTM_VerticalGrip02_W30`) inserted into the lists (checklist U44); not stat changes |
| GS recoil rows | 6 | 0 | 0 | 2 | The table above |
| WB spot-on-fire base `Field_5ebda408/Field_9918e670` | 4 | 0 | 0 | 4 | 54 to 75 on `HK433_WB` (M433), `MPX_WB` (SGX), `Minimi_WB` (L110), `M18_WB` (P18); checklist U24, already in FIELD_MAP.md |
| WB class profile `Field_f2d603de` (`Field_3f5f0ea4` x, y, z; `Field_e1d8c5f8`) | 7 | 0 | 0 | 2 | `HK433_WB` 9 / 2.5 / 0.2 to 14.5 / 3.0 / 0.24 (first and third entries) and `M2010ESR_WB` to 11 / 2.6 / 0.3 and 16.5 / 3.0 / 0.3; `Field_e1d8c5f8` 0.82 to 0.7 on one `M2010ESR_WB` entry; already in `STAGE6-8-TRACE-RESULTS.md` as class-profile retargets, no registry rows |
| WB modifier-array structure (`MPX_WB`, `Minimi_WB`, `HK433_WB`, `M2010ESR_WB`, `M18_WB`) | 765 | 806 | 8 | 5 | Entries added to and removed from arrays (new foregrip and ammunition entries, the `CMU_SemiAuto` removal); values shifted by index, not interpreted |
| PD armor damage curve points (`Field_5279388d`) | 70 | 24 | 0 | 13 | The table below; checklist U23 |

## Armor damage curves that changed (13 bullet files)

Own armor curve (`TweakableArmorDamageCurve`), points as range:damage. The registry default curve changed identically in each file and equals the own curve on 2.1.1.0.

| Bullet file | 1.4.3.5 | 2.1.1.0 |
| --- | --- | --- |
| `PD_.300BLK_Carbine` | 0:26.05 19:26.05 31:26.05 31:20.67 46:20.67 46:17.13 85:17.13 85:14.62 | 0:20.67 19:20.67 31:20.67 46:20.67 46:17.13 85:17.13 85:14.62 |
| `PD_762x39mm` | 0:27.48 31:27.48 31:21.56 46:21.56 46:20.67 85:20.67 85:17.13 | 0:20.67 46:20.67 85:20.67 85:17.13 |
| `PD_762x39mm_Carbine` | 0:26.05 31:26.05 31:20.67 46:20.67 46:17.13 85:17.13 85:14.62 | 0:20.67 46:20.67 46:17.13 85:17.13 85:14.62 |
| `PD_762x51mmNATO_Semi`, `_Semi_Match`, `PD_762x54mmR_Semi`, `_Semi_Match` | 0:41.5 31:41.5 31:37.6 85:37.6 85:34.4 | 0:27.5 85:27.5 (flat) |
| `PD_545x39mm`, `PD_545x39mm_MG` | 0:17.74 31:17.74 31:17.13 85:17.13 85:14.62 | breakpoint 46 added: 31:17.74 31:17.13 46:17.13 46:14.62 85:14.62 85:12.76 |
| `PD_556x45mmNATO`, `PD_556x45mmNATO_MG` | 0:21.56 31:21.56 31:20.67 85:20.67 85:17.13 | 31:21.56 31:20.67 46:20.67 46:17.13 85:17.13 85:14.62 |
| `PD_10x25mm_PDW` | 0:26.05 19:26.05 31:26.05 31:20.67 46:20.67 85:17.13 85:14.62 | 0:26.05 9:26.05 9:20.67 19:20.67 19:17.13 31:17.13 31:14.62 46:14.62 85:14.62 |
| `PD_9x19mm_PDW` | 0:20.67 19:20.67 31:20.67 31:17.13 46:17.13 46:14.62 85:14.62 85:12.76 | 0:20.67 9:20.67 9:17.13 19:17.13 19:14.62 31:14.62 31:12.76 46:12.76 85:12.76 |

Full point lists are in `curve-diff.json`. The site holds no armor curve (its `dmg` lists are the health curves); the change is checklist U23 ("probably REDSEC armour plates").

## Added registry rows (L4002)

- **Count.** `registry-diff-2026-10-14/registry-diff.tsv` lists 4,970 added rows over all registries, 2,150 of them in `GRX_Weapons` (1,669 with a default value) and 563 in the new `KST_CH2_S1_Weapons`. The 1,846 figure was not reproduced: the value-row reader (`allrows.py`) finds **1,836** value rows added (1,672 in `GRX_Weapons`, 75 `GRX_Gadgets_Glacier`, 34 `GRX_Persistence_Glacier`, 24 `GRX_Vehicles`, 19 `GRX_Vehicles_CH2`, 7 `GRX_Online`, 3 `GRX_UI`, 1 `GRX_Glacier_Soldier`) and 8 removed; the tsv has 1,833 value-bearing added rows in the `GRX_*` files. 1,846 is neither.
- **On site-weapon owners (1,086 rows).** 840 `GS_` rows (210 each for `GS_MRGGA`, `GS_CDX40`, `GS_PKM`, `GS_RSAR999`) and 147 `_WB` rows for the four Season 5 weapons (`CDX40_WB` 57, `MRGGA_WB` 45, `PKM_WB` 45; `RSAR999_WB` has no registry row), 24 `StanceChangePenalties` rows on `GS_M240L`, 75 rows on the five new bullet files (`PD_.375EnABELR_API`, `PD_.375EnABELR_Match`, `PD_65x48mm`, `PD_762x39mm_PDW`, `PD_762x54mmR_MG`; 15 each). Every one equals its own value; none is on an existing weapon's stat row.
- **Row names.** The set of row suffixes on weapon, firing-data and bullet owners is the same 332 as on 1.4.3.5 (none new, none removed). Value-matching names 106 leaf hashes, 102 of the 10 October run plus four (`Field_db4fa3c2` `AutoReplenishRounds`, `Field_4449ee55` `CustomZeroing`, `Field_7ce404e6` `MinAngleOffset`, `Field_ed10e827` `Duration` of the stance penalties) that gained their second distinct value or their second owner set on the new weapons. All 106 are already in `FIELD_MAP.md`. None of the 24 hashes in `OPEN_QUESTIONS.md` is named. 29 of the 399 `Field_` hashes cited by the 116 negative closures are named by a registry row, all already in the map; none gains a new name, so none of those closures is reopened. `Field_440ed7fa` still has no row. **No row was added to `FIELD_MAP.md`.**
- **Odd names.** 46 rows named `M16A3_WB - PrimaryFire…` (M16A4), `M16A3_WB - InitialSpeed…` and the like (and `PD_Railgun - TweakableArmorDamageCurve`) are added; they use the standard field names with a different owner label. They copy the `M16A3_WB` defaults except `M16A3_WB - InitialSpeed.z` = 720 against `M16A3_WB…Shot.InitialSpeed.z` = 680 (own 680, site 680). The row set was not used by the pairing; see open items.
- **Other registries.** `KST_CH2_S1_Weapons` (563 kill-switch rows) and the mutator rows name attachments and loot, not weapon field hashes.

## Fire modes (L604)

Same fields as the 30 September run (`Field_f8822efa`: primary mode `Field_16e6fa59`, `RateOfFire`, `RateOfFireForBurst`, `RateOfFireForSingleFire`, `BurstsPerMinute`; `Field_58d70acb/Field_ca2ec42a` rounds per burst; alternate list `Field_9b956c3d`), read from the 63 weapons' `_WB` files and compared with `fire-modes.json` (110 rows, 12 branches):

- **Mode lists and rates.** 0 changes on 63 of 63: primary mode, alternate list, the four rate fields and rounds per burst all equal. SGX: auto 830.769, single 449.999 (list auto + single). L110: auto 719.999 (list auto only; single-fire field 399.999 as before, unused).
- **Branches.** The 12 mode-changing modifier files (`WPM_ERG_BurstFireEnabled_W10`, `_BurstFireReplace_W10`, `_FullAutoReplace_W30`, `_FullAutoReplaceVSSM_W50`) are byte-identical by SHA-256; the set of `_Ergo/FireMode` routes is the same 11 before and after, so the 10 site choices and the two source-only branches stand.
- **Match Trigger on the SGX and L110.** EA's note removes the Match Trigger from both. In the source: `MPX_WB` (SGX) and `Minimi_WB` (L110) each lost one import, the condition asset `_Ergo/CMU_SemiAuto` (GUID `443b41bc-f4b5-45e9-8d7c-3e4208121496`; byte search: one hit in each 1.4.3.5 file, none in 2.1.1.0). Of the 63 existing weapons these are the only two that lost it; 41 of the other 61 `_WB` files import it (43 of 63 did on 1.4.3.5). `CMU_SemiAuto` is a two-object condition asset (one field, value 1) and is not specific to the Match Trigger (it is imported by weapons that do not offer one), so the loss shows that the semi-auto conditional modifiers no longer apply on these two, not by itself that a Match Trigger attachment was removed. Neither weapon has a Match Trigger attachment record in the catalog on either build (no `Attachment_` or `U_PRG_` Match Trigger asset for `MPX` or `Minimi`), and the site already offers none (SGX: buffer only; L110: none). The checklist row U45 calls the removed entry `CMU_MatchTrigger`; no asset of that name exists, the import is `CMU_SemiAuto`. Mode lists and rates of both weapons did not change.
- **Other weapons.** No other mode list or rate moved. `HK433_WB` (M433) is the one weapon that gained a Match Trigger import (`_Ergo/MatchTrigger/WPM_ERG_MatchTrigger_W15`, GUID `36d9d2e2-d5e9-4075-9e9d-9f4c9d148cad`, one hit at offset 26360 in the 2.1.1.0 file, none before); it keeps its `CMU_SemiAuto` import. Its mode list is unchanged (auto + single; the site offers the Match Trigger on it).
- **New weapons (read, not diffed).** Mk 24 auto 635.294, single 359.999; RSPR auto 719.999, single 399.999; Z84M auto 719.999 only; ELR-40 bolt (mode 1) 299.999. All equal the site's `fireModes`.

## Open items

1. **ELR-40 magazine.** `weapons.json` `mag` is 8; `CDX40_WB` registry and own `MagazineCapacity` is 1 (`NumberOfMagazines` 50); `WEAPON_MAG.elr40` defaults to the 7 Rnd magazine. Not resolved here (the 7 Rnd package was not read); the ELR-40's site rate 36.26 is, like the other manually cycled weapons, a cycle-derived value against a placeholder 300 in `RateOfFire`. Report to the operator before any site change.
2. **M433 Match Trigger import.** `HK433_WB` newly imports the Match Trigger package W15 directly; what that changes in the M433 is not traced (the M433 already offers the attachment).
3. **`M16A3_WB - InitialSpeed.z` = 720.** A stray added row group with the M16A3 defaults except velocity 720 (the real row, the own value and the site say 680). Not consumed by any pairing; check whether the game reads the odd-named rows.
4. **MPX, Minimi, HK433, M2010 ESR, M18 `_WB` array entries.** 1,579 leaf differences are entries added to modifier arrays (Actuated Module, Polymer Links, FML 1.00x per the 19 October attachment note); not mapped one to one here.
5. **Armor curves of 13 bullets** (U23) are listed, not analysed.
6. **Queue ids.** The task asked for rows from L4020. L4020 to L4050 are already closed leads with receipts (gadget graphs and recoil work), so the new queue rows use L4051 onward.

## Not examined

Attachment package values (`WPM_*`, `GRM_*`, `WME_*` files); rows under `WeaponModifierDataAssets`; limb multipliers and the bolt-action sweet-spot datasets of L4003 (the weapon files holding them were compared as raw leaves only: no limb leaf is in the differing classes above); reload sums beyond the 441-record comparison (identical to 10 October: 42 of 58 empty-reload sums equal, 3 tactical); ammunition-type bullet files of `data/ammo.json` (L580 to L582); gadget, launcher and vehicle owners (the roster refresh covers them); EA's 2.1.1.0 notes were not re-read for weapon lines beyond the Match Trigger statement in the task; in-game behaviour of any changed value; BROD 3 firing data (`GS_BREN3`), `PD_545x39mm_MG`, `PD_9x39mm_Match`, `PD_9x39mm_Semi` still have no registry rows to pair with (as on 10 October).
