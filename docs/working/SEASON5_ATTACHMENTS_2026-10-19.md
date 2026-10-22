# Season 5 attachments on existing weapons (2.1.1.0, 19 October 2026)

Closes checklist row U44 of [2.1.1.0-checklist.md](../updates/2.1.1.0-checklist.md): the three
Season 5 attachments added to existing weapons that had not been traced (the Actuated Module was
traced on 18 October). Also records a side finding on the ELR-40 raised by the operator during the
run. Research only: no site data, simulation or UI change was made; nothing committed or pushed.

Build 2.1.1.0 hotfix capture, read from saved raw files only (no new Frosty run):
`BF6 Datamining\builds\2.1.1.0\reports\client-new-check-2026-10-15\collection\raw` with its
`asset-catalog.json`, descriptors `capture\toolchain\SharedTypeDescriptors.ebx` (SHA-256
`c477622c…`, layout-identical to the hotfix descriptors). Strings: `capture\fs_us_loc.strings.tsv`.
Baseline for "new": `builds\1.4.3.5\capture\collection\raw`.

Scripts and results: `BF6 Datamining\reports\weapon-analyzer-research\2026-10-19-season5-attachments\`
(`s5_bindings.py` and `s5_controls.py` reuse the site's `frosty-attachment-wiring-check.py` decoder
and binding walk; `bindings.json` has every weapon's selector, package and GS binding for the four
Season 5 attachments; `packages.json` the decoded packages; `uitext.json` the metadata text;
`s5_grm.py`, `s5_nondef.py`, `s5_imports.py` the package comparisons; `s5_rf.py`, `s5_cdx.py`,
`s5_zero.py`, `s5_zrows.py`, `s5_final.py` the ELR-40 zeroing trace).

## Method

1. List the `Attachment_<weapon>_<slot>_<name>` and `U_PRG_` records for each new attachment in
   every weapon folder (the weapon folders name the grip `DDVertical`, not `VerticalGrip02`).
2. For each record, follow the progression to its ability branch, the branch's actions to the
   `U_WPM_*` selectors, and each selector to (a) the WB modifier package that lists it and the
   `WME_*` effects that package imports, and (b) the `GS_` bindings keyed by that selector. This is
   the site's wiring-check walk, run on all 69 weapon folders.
3. Compare the bound packages field by field with the packages of the existing attachments of the
   same family, so that the site tier follows the established family mapping rather than a new
   reading.
4. Resolve the UI metadata (`AD_*`) text against the 2.1.1.0 strings table.

Optic packages are not reached by step 2 (their effects sit inside the `WPM_SCP_*` package the WB
lists directly), so the FML19 was compared by its import list with two rifle thermals and two
sidearm red dots instead.

## 1. DD Vertical (`Attachment_<weapon>_BTM_DDVertical`)

**Text.** `AD_DDVertical`: label "Vertical", description "Moderately reduces recoil."
(string `E4BDD91B`). No new "… Vertical" display name is in the 2.1.1.0 English strings table (the
only grip names are Folding, Alloy, Ribbed, 6H64, Classic and Canted Vertical), so the name the
loadout screen shows was not established from source. Point cost `Field_6ee865a5` = 30.

**Bindings, identical on every weapon that offers it.** Selector `U_WPM_BTM_Vertical02_W30` (new
in 2.1.1.0; `Vertical02_W20` is the Ribbed Vertical's selector).

| Route | Asset | Content |
|---|---|---|
| GS binding | `GRM_Recoil_BTM_P30` | `RecoilAmountMultiplierExponent` (`Field_22ce7cf3/Field_4692836a`) = 3 in both the Unzoomed (`Field_7b609515`) and Zoomed (`Field_6b84de87`) branches; every other field neutral. The package differs from `GRM_Recoil_BTM_P10/P20/P40/P50` in that one integer only (1/2/4/5). |
| WB package | `WPM_BTM_VerticalGrip02_W30` (new) → `WME_DynamicPivot_M10` | Dynamic pivot multiplier, the same effect every vertical grip except Alloy Vertical carries; not modelled on the site. |
| Not bound | `GDM_Array_ADSMoveDispersion_BTM_M10`, `WME_ADSMoveSpeed_M05` | Absent: no moving-ADS accuracy cost and no ADS movement-speed cost. |

**Family mapping (control weapons M4A1, M121 A2, DB-12; same on all).**

| Grip | Selector | GS recoil | GS moving-ADS dispersion | WB effects | Site today |
|---|---|---|---|---|---|
| Folding Vertical | `Vertical01_W10` | P20 | M10 | DynamicPivot_M10 | ADS 2 / hip 2 / moving −1 |
| Alloy Vertical | `Vertical01_W20` | P20 | – | – | 2 / 2 / 0 |
| Ribbed Vertical | `Vertical02_W20` | P30 | M10 | DynamicPivot_M10 | 3 / 3 / −1 |
| 6H64 Vertical | `Vertical03_W25` | P40 | M10 | ADSMoveSpeed_M05, DynamicPivot_M10 | 4 / 4 / −1, ADS move +1 |
| Classic Vertical | `Vertical04_W35` | P50 | M10 | ADSMoveSpeed_M05, DynamicPivot_M10 | 5 / 5 / −1, ADS move +1 |
| **DD Vertical (new)** | `Vertical02_W30` | **P30** | **–** | DynamicPivot_M10 | **3 / 3 / 0** |

So the new grip is the Ribbed Vertical's recoil reduction without its moving-ADS penalty, for 10
more points, which is what its description says against the Ribbed Vertical's ("Moderately reduces
recoil at the cost of aim down sights (ADS) accuracy while moving", `AD_Tango_Vertical`).

**Not live yet (operator, 19 October):** the DD Vertical is not offered in the game at 2.1.1.0;
its records sit behind the Season 5 kill switch (`KST_CH2_S1_Weapons`, default false) and are
expected to unlock in a later Season 5 phase. Hold the site entry until it appears in the loadout
screen.

**Proposed site entry (on release, needs operator approval):** `GRIPS` id for the new grip with
`adsRecoilTierMod` 3, `hipRecoilTierMod` 3, `movingAdsSpreadTierMod` 0, `pts` 30, no handling
shifts, added to the grip list of the 49 weapons below. The display name should be read from the
loadout screen first.

**Weapons offering it (attachment record present, kill switch `KST_CH2_S1_Weapons` default
false), 49:** KORD 6P67, NVO-228E, EF88, B36A4, AK4D, M433, L85A3, M16A4, SOR-556 Mk2, TR-7, VCR-2;
AK-205, BROD 3, M417 A2, M4A1, GRT-BC, QBZ-192, SOR-300SC, SG 553R, M277; LMR27, M39 EMR, SVK-8.6,
SVDM, VSSM; M240L, M250, DRS-IAR, M/60, M123K, M121 A2, L110, RPK-74M, RPKM, KTS100 MK8; 18.5KS-K,
M87A1, DB-12, M1014; SCW-10, SL9, PW5A3, PW7A2, SGX, PP-19, RSPR, CZ3A1, UMG-40, KV9.
Not offered: the six bolt-actions, ELR-40, vz. 61, Mk 24, Z84M, and GRT-CPS (progression record
`U_PRG_MSBSGROTCPS_BTM_DDVertical` exists but no attachment record). The 13 October count of "34
weapons" counted GS files that changed, not attachment records.

## 2. Polymer Links (`Attachment_<weapon>_AMO_PolymerLinks`)

**Text.** `AD_Ammo_PolymerLinks`: label "Lightweight", description "Standard-penetration
ammunition contained within lightweight belt links providing improved aim down sights (ADS)
movement speed." (`44E52C7D`). Display string "Polymer Links" (`8F96E2FF`). Cost 10.

**Bindings.** Selector `U_WPM_AMO_PolymerLinks_W10`; package `WPM_AMO_PolymerLinks_W10` imports
exactly the two effects of the rifle Polymer Case package (`WPM_AMO_PolymerCase_W10`):
`WME_ADSMoveSpeed_P05` (one ADS-move tier faster; site `adsMoveSpeedTierShift` −1) and
`WME_Penetration_P05` (the Standard penetration step; the 14 October M121 A2 panel shows 0.75).
No GS binding. Same cost as Polymer Case.

**Weapons, 7 belt-fed LMGs:** M240L, M250, M/60, M123K, M121 A2, L110, Z84M. New for six of them:
in 1.4.3.5 only the M240L had a Lightweight ammunition record (`Attachment_M240L_AMO_Polymer_Case`),
and that record is still present in 2.1.1.0 beside the new one, both with kill switch default
false and identical effects. Whether the M240L menu lists two Lightweight options is a one-glance
check for the operator. Magazine LMGs (RPK-74M, RPKM, DRS-IAR, KTS100 MK8) keep Polymer Case.

**Site.** Already consistent: site commit `016013a` (13 October) added `lightweight` at 10 points
to all seven, and `data/attachment-tooltips.json` carries the belt-links text. No change proposed.

## 3. FML 1.00x thermal sight (`Attachment_<weapon>_SCP_FML19`)

**Text.** Display string "FML 1.00x" (`1ABD5235`). Its metadata record
`Common/UI/Static/Metadata/Attachments/Shared/AD_FML19_Thermal` is in the 2.1.1.0 catalog but in no
saved capture (one route; label and description unread). Cost 25. Unlock tags `CT_GLA_CH1_S0` and
`CT_GLA_CH1_S2`.

**Weapons, 7 sidearms:** ES 5.7, GGH-22, P18, M45A1, M44, vz. 61, M357 Trait. Like every sidearm
optic other than iron sights, it binds nothing in the GS or WB modifier lists.

**Package `WPM_SCP_FML19` against controls.**

| Content | FML 1.00x | HISS HD (rifle thermal) | RMR, ACRO P2 (sidearm red dots) |
|---|---|---|---|
| Aiming controller import | `Aim_01x00_PiP` | `Aim_06x00_PiP` | `Aim_01x00_PiP` |
| Render FOV `Field_7768ebf2` / `Field_e5b5c7db` | 55 / 4 | 22 / 5 | 55 / 4 |
| Thermal mode list `Class_a11c1a03` (0.1, 0.01, 2 / 0.9, 2 / 0.1) | present | present | absent |
| Visual environment import | `VE_FML19_Thermal` | `VE_HISSHD_Thermal` | `VE_RMR` |
| `WME_ADSMoveSpeed_M05` import | **absent** | present | absent |
| Riser pair `Field_149939ab` / `Field_e9129d03` | 1.07 | 0.5 | 1.0 |
| `Class_bfd4f199.Field_3b707594`; `Class_87421347.Field_16562b71` | 1.1; 1.2 triplets | 1.0; 1.0 | 1.0; 1.0 |

The site's Thermal category carries `adsMoveSpeedTierShift` 1 because every rifle thermal and
variable-high optic imports `WME_ADSMoveSpeed_M05` (L62, confirmed on the M4A1 menu 25 September).
The FML 1.00x does not import it: it is a 1.00x thermal with the handling of a sidearm red dot.
The 13 October optic-category receipt lists the seven FML19 records as unresolved (category null),
so the optic generator has no rule for the label yet.

**Not live yet (operator, 19 October):** the FML 1.00x is not offered in the game at 2.1.1.0; like
the DD Vertical it waits behind the Season 5 kill switch for a later phase. Hold the site entry
until it appears.

**Proposed site entry (on release, needs operator approval):** offer a Thermal sight on the seven sidearms at
25 points with no ADS-move shift (a sidearm-only variant of the `thermal` entry, or `noEffect`),
and give `optic_category` a rule for "FML 1.00x". The two unnamed multipliers (1.07 pair, 1.1 and
1.2 triplets) have no site model; they are recorded here only.

## 4. ELR-40: custom zeroing enabled without the FN Elity (operator report, 19 October)

The operator reports the ELR-40 behaves as if it had a built-in rangefinder, unannounced and
undescribed. Source agrees that it is the only weapon with a zeroing flag set:

- Every weapon blueprint's zeroing block (`Class_35259f6b/Field_58d70acb/Field_7d5dc312`) was read
  on all 69 weapon folders. `Field_4449ee55` is true on `CDX40_WB` only; false on the other 68.
  `Field_4b636fc6` is false on all 69. `Field_4e34fabb` is true on the bolt-actions and DMRs as
  before. The ELR-40 block otherwise matches the other snipers: minimum 100, maximum 1000, delay
  0.4, list 100/200/300/400/500.
- The registry `GRX_Weapons` has a named row set for `CDX40_WB….Shot.Zeroing`, and its parent
  node's hash array (`Field_4471d2f1`) is paired with its child rows (`Field_080f1aaa`), which
  names the two hashes the field map had left open: **`Field_4449ee55` = CustomZeroing,
  `Field_4b636fc6` = RangeFinder** (the other pairs reproduce the known
  RangeFindingInAdsOnly, MinimumCustomZeroingDistance, MaximumCustomZeroingDistance and
  CustomZeroingDelay). The registry row `CDX40_WB….Zeroing.CustomZeroing` is true; it is the only
  CustomZeroing or RangeFinder row in `GRX_Weapons` that is true (PSR and L115 rows are false).
- The FN Elity attachment (`U_WPM_RGT_RangeFinder_W10` → `WPM_RGT_RangeFinder_W10`, effect
  `Class_4e0a8f72`) sets both RangeFinder and CustomZeroing true. The ELR-40 therefore has the
  CustomZeroing half of the FN Elity built in; its own FN Elity record (`Attachment_CDX40_LFT_FNElity`,
  left rail) is an ordinary branch with kill switch `KST_CH2_S1_Weapons` default false.

What CustomZeroing alone does in play (free zero distance between 100 and 1000 m after a 0.4 s
delay, with or without a displayed range) is the operator's observation to describe; the game's own
text does not mention it. Zeroing is not modelled on the site (L9 parked), so this is a candidate
entry for the site's game-bugs document, not a data change. The field map row is updated.

## Open items

- Display name of the DD Vertical as the loadout screen shows it (not in the strings table under
  any "… Vertical" name).
- `AD_FML19_Thermal` metadata: one uncaptured route if its text is wanted.
- M240L: whether both Lightweight records appear in the menu.
- Stat-screen check of the DD Vertical on one weapon (recoil bars equal to the Ribbed Vertical,
  Mobility unchanged) would confirm the tier reading; source and family mapping do not require it.
