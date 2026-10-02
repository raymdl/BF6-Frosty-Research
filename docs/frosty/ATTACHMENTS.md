# Attachment and optic data in Frosty

[Frosty docs](README.md) · [Field map](FIELD_MAP.md) · [Data graph](DATA_GRAPH.md) · [Attachment bugs](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/ATTACHMENT_BUGS.md) · [Open questions](OPEN_QUESTIONS.md)

What the game data says about attachments and optics, and which site values are
generated from it. The site model is in the [attachment model](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/ATTACHMENT_MODEL.md);
game data errors are in [attachment bugs](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/ATTACHMENT_BUGS.md). The link path from a
site choice to its modifiers is in the [data graph](DATA_GRAPH.md).

<!-- gunfight-ranked-equipment:start -->
## Attachment weight and functional package source boundary

[L743-L744](../../reference-data/provenance/frosty-2026-10-01-gunfight-ranked-equipment-qualification.json) checks attachment-weight candidates, base UI package imports, SVDM/P90 package bodies and the exact Season 2 metadata owner. No semantic weight field or receiver qualified. Point costs and animation pose weights are separate concepts.

Season 2 text resolves `7BFF8D02` to Professional's Headtaker and `B2FEF564` to Side Effects. Four pointer/StringId reads and two independent parent StringId re-reads passed against the current strings table. The package metadata and token bodies inspected do not establish fitted choices. Their resolved image references and similarly named token objects are not a functional identity chain. EA's remaining 50/45 points are validation predictions until the exact choice/budget consumer is joined. No weight, handling or package value change is proposed.

The initial SVCh/SVDM import nomination was corrected before interpretation. Current SVDM file/exported GUIDs are `05ca9d8b-e332-4c53-9088-6673203a37ac` / `fe832261-9f01-415b-a7dc-f530a519af9a`. The failed nomination is retained in the run; no finding uses it.
<!-- gunfight-ranked-equipment:end -->

## Supplemental source owner atlas (1.4.3.5, L792)

[L792](../../reference-data/provenance/frosty-2026-10-01-L792-supplemental-owner-field-atlas.json) adds 256 current owner files, 30,392 typed occurrences, 2,558 descriptor/path families and 1,019 outward imports in 14 bounded batches. The M433 same-owner control passed before conclusions. Parent native review and sampled raw re-reads passed. Reconciliation covers 50,482 original graph edges and 20,620 exact target identities.

Current captures close every qualified missing body in this pass, including pistol optic records, Blacklight selectors and affectors, PiP, breath/zeroing UI and reticle draw/property bodies. Exact current file and exported-object GUIDs retain their source pointer proofs. Historical wrapper bytes remain qualification context. Broad registry reachability does not select a weapon effect.

Global configuration, presentation/resource and native-consumer limits remain explicit. They do not establish no effect. Fifty-one compact rows in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) retain investigated routes, fields, attempts and reopen conditions. Newly typed scalar roles remain frontier work; zero capture gaps does not mean all field roles are known.

## Selection wrapper field atlas (1.4.3.5, L791)

[L791](../../reference-data/provenance/frosty-2026-10-01-L791-selection-wrapper-field-atlas.json) accounts for 9,679 candidate wrappers: 7,728 current owners decoded and 1,951 current raw gaps. The exact AK-205 branch/action/exported selector and same-owner internal-token control passed first. Current extraction contains 39,545 typed records, 7,793 local objects and seven descriptor-qualified field families. All current inventory hashes match. The worker verified 420 outward object joins and 3,508 pointer operands; parent review and sampled raw re-reads passed.

All 1,951 gap routes exist in the current catalog with the expected file GUIDs. Historical captures pin 63 to Head 4892017 and 1,888 to Head 4892087; their bytes are qualification context and are not current values. The gap evidence retains 2,823 exact imports from 66 current parents. Typed progression/action references, broad registry reachability and native selected effects remain separate. Wrapper names and configuration references do not establish gameplay effects. L792 reconciles the relevant selected targets before capture and supplemental coverage.

## Attachment modifier field atlas (1.4.3.5, L790)

[L790](../../reference-data/provenance/frosty-2026-10-01-L790-attachment-modifier-field-atlas.json) covers 128 initial packages and 102 exact linked supplemental owners, with 2,157 families qualified by both declaring descriptor and concrete owner. The M39 EMR iron-sight selector/exported sway-input control passed first: 0.6666666865348816 matches the current site factor and consumer. The recovered registered Blacklight capture adds 561 typed fields. The worker completed 3,978 independent raw checks; parent review and sampled raw re-reads passed.

One relative weapon-sway context has an exact site input/consumer join. Other effect contexts retain their own inference limits or unexplained roles. The 1,968 graph edges include 15 occurrences to nine exact missing current target files, checked against current report captures. A broad configuration import does not imply every contained rule affects a selected weapon. Arrays and field hashes retain their declaring type; no percentage, unit or runtime modifier order follows from numeric resemblance.

## Attachment record field atlas (1.4.3.5, L789)

[L789](../../reference-data/provenance/frosty-2026-10-01-L789-attachment-record-field-atlas.json) accounts for 5,546 attachment candidates: 5,542 decoded current owners, 18 typed field families and four raw gaps. The same-owner M433 brake point-cost and exact progression control passed first. The atlas reproduces 4,554 current point-cost proofs and 4,522 complete serialized progression/Ability/action/selector/WPM associations. The worker raw-checked 32,716 consequential operands plus four control reads; parent review and sampled re-reads passed.

Point-cost fields retain exact site consumers and per-weapon override contexts. Other fields remain known limits or unexplained identifiers, categories and alternate-record references. The four gaps are M145MGO and QMK171A attachment records for RagingHunter and TRR8, absent from the searched current capture/report folders. All 11,084 import edges retain exact identities; candidate records without a selected choice chain remain separate. No attachment effect follows from a route name, category number or missing raw file.

## Ability field atlas (1.4.3.5, L788)

[L788](../../reference-data/provenance/frosty-2026-10-01-L788-ability-field-atlas.json) covers all 63 weapon Ability owners, 150 typed field families and 260,587 occurrences. The AK-205 magazine branch/action/exact selector control passed before extraction. All 63 offered-branch arrays target the current local branch class. The worker reproduced 182 source magazine associations, with 542 selection reads and 63 offered-list reads; parent raw re-reads and review passed.

These are source selection structures, not the site effect consumers. The atlas retains 33,883 outward import edges, six missing current targets and 23 additional owner candidates for reconciliation. The 135 exact SRU-linked underbarrel branches have explicit excluded-profile dispositions; their external profile bodies were not examined. IDs, flags and repeated array positions do not supply gameplay meanings. Missing raw targets do not support effect-absence claims.

## Ammo package field atlas (1.4.3.5, L786)

[L786](../../reference-data/provenance/frosty-2026-10-01-L786-ammo-field-atlas.json) covers 260 current source files and 55 typed families: 132 selector/token owners, 125 ammo-value owners and three effect-only packages. The exact AK-205 Ability branch/action/selector control gives source capacity 37 for the 36-round menu choice. The actual package capacity owner is `Class_e7d2410a`; the WB `Struct_598cc52c` context is separate. All hashes match, and parent raw re-reads pass.

The current exact serialized chains link 182 site choices to 113 WPM owners. Source capacity minus menu capacity is +1 for 171 choices and 0 for 11; this does not assign loaded/chambered-round behavior. The unexplained `Field_bd024e1d` has four integer values across the 125 ammo owners, from -1 to 99. Six local reload objects retain exact phase-array leaves from 0.5 to 7.984000205993652; no phase-duration formula follows. The atlas separates modeled capacity, traced fields without a site reader, known limits and never-examined fields. Additional exact outgoing owner candidates remain part of Stage 1 coverage.

## Current site value audit (30 September–1 October 2026)

The [census](../../reference-data/provenance/frosty-site-audit-attachments-census-2026-09-30.json)
contains **113 numeric field families and 7,578 numeric leaves**. A01 applies:
the site baseline combines source versions and reviewed panel evidence. Owners
follow the site's `docs/data-flow/REGISTER.md` and "Attachment source generation".
The four named generator scopes and prior field comparisons exclude 7,248 leaves;
251 leaves retain prior no-source-field contracts or observations. Magazine points
(287 leaves), nominal capacity (287) and stored reload tiers (282) have prior field
records. Source loaded/chamber capacity remains separate from nominal menu capacity.

All **79 remaining candidate leaves in 12 families** now have a disposition in
the run's `census-reconciled.json`, with one receipt per family. **No new material
value mismatch or Analyzer change proposal was established.** The original census
and its earlier usage stop are retained as history; the operator removed that stop
condition on continuation.

L540 supplied the only new source extraction: six offered AG Coating Attachment
owners on 1.4.3.5 / Head 4909002 / descriptor `4c28ad65...`. The same-owner 185KSK
Canted Iron Sights control passed first (5 points). All six owner fields
`Class_a9b2eb87.Field_6ee865a5` read **10** at raw offset **128**, u32,
bytes `0a000000`, matching the site. Worker review passed; the parent independently
re-read M2010ESR. Serialized point cost does not prove every compatibility/runtime
condition. No capture was needed.

| Family | Candidate leaves | Result |
| --- | ---: | --- |
| [SIGHTS.adsMoveSpeedTierShift](../../reference-data/provenance/frosty-site-audit-attachments-sights-adsmovespeedtiershift-2026-10-01.json) | 2 | 275 prior optic selection rows: source -1 becomes site +1; matches. |
| [MUZZLES.worldSpotMult](../../reference-data/provenance/frosty-site-audit-attachments-muzzles-worldspotmult-2026-10-01.json) | 18 | Direct source factors match; neutral packages without a comparable operand stay class (d). |
| [MUZZLES.minimapSpotMult](../../reference-data/provenance/frosty-site-audit-attachments-muzzles-minimapspotmult-2026-10-01.json) | 11 | 3D-only spotting effects retain minimap 1; other neutral packages stay class (d). |
| [MUZZLES.hipSpreadTierMod](../../reference-data/provenance/frosty-site-audit-attachments-muzzles-hipspreadtiermod-2026-10-01.json) | 1 | 53 Standard Suppressor selections match current effective values; L115 keeps reviewed bug 12. |
| [BARRELS.movingAdsSpreadTierMod](../../reference-data/provenance/frosty-site-audit-attachments-barrels-movingadsspreadtiermod-2026-10-01.json) | 8 | Eight zero defaults: no comparable owner scalar in retained selector review; class (d), no lead. |
| [BARRELS.velMult](../../reference-data/provenance/frosty-site-audit-attachments-barrels-velmult-2026-10-01.json) | 6 | Six inactive fallback values; present velTierMod=0 controls displayed velocity. |
| [BARRELS.worldSpotMult](../../reference-data/provenance/frosty-site-audit-attachments-barrels-worldspotmult-2026-10-01.json) | 2 | Both VSSM choices match source world factor 0. |
| [GRIPS.movingAdsSpreadTierMod](../../reference-data/provenance/frosty-site-audit-attachments-grips-movingadsspreadtiermod-2026-10-01.json) | 12 | Twelve defaults: no comparable bound scalar in retained review; class (d), no lead. |
| [GRIPS.adsRecoilTierMod](../../reference-data/provenance/frosty-site-audit-attachments-grips-adsrecoiltiermod-2026-10-01.json) | 8 | Eight defaults: no comparable bound scalar in retained review; class (d), no lead. |
| [GRIPS.frostyModifiers.movingAdsSpreadTierMod](../../reference-data/provenance/frosty-site-audit-attachments-grips-frostymodifiers-movingadsspreadtiermod-2026-10-01.json) | 2 | KS18K Slim Angled zero is intentional (bug 1b); L115 QD Grip Pod has no comparable scalar, class (d). |
| [ACCESSORIES.pts](../../reference-data/provenance/frosty-site-audit-attachments-accessories-pts-2026-10-01.json) | 4 | AG Coating: all six current raw costs match 10; prior paid accessory costs match 5/10; None=0 is a site contract. |
| [WEAPON_MAG.tacRldOverrideMs](../../reference-data/provenance/frosty-site-audit-attachments-weapon-mag-tacrldoverridems-2026-10-01.json) | 5 | Five integer-ms rounding cases, class (b), under L107; no proposal. |

The 79-leaf disposition is: 18 prior field matches, one new current-raw match,
five precision-only reload values, one intentional grip override, six inactive
velocity fallbacks, one None cost contract and 47 bounded no-source-route leaves.
These are leaf counts, not weapon-attachment pair counts. The five reload aliases
are PP-19/53, M60/50, M240L/75 and /100, and RPK-74M/95; retained integer-ms
rounding follows [L107](../../reference-data/provenance/frosty-2026-09-28-L107-precision-audit.json).
No precision-only proposal was added.

Earlier source evidence keeps its original Head and carries forward by equal raw
hash; 90 reused raw bodies were rehashed against current capture. Reuse is not a
new field extraction. No-route defaults do not establish source zero or native
absence. Spotting operands remain conditional on native composition; the four
existing SP suppressor minimap candidates (.10 versus .14, L47/L49) remain unresolved
and do not become a new mismatch claim. Reviewed bugs 1b, 6 and 12 remain in force.
No site data, simulation or UI edits, source-generator runs, underbarrel profiles
or in-game tests were included.

## 1.4.3.5 recheck (30 September 2026)

The captured AD/Attachment set (6,546 records) and weapon-modifier folder (721
records) have unchanged raw content. The 17 attachment-bug rows retain their prior
source and description status; this is not new in-game confirmation. Current
metadata roles and localization were checked separately. All 1,004 AD metadata
assets have layout ambiguity, but their raw bytes and the complete English strings
table are unchanged.

The 34 GCR assets have no paired-value/flag mismatch, disabled nonzero residue or
value outside the recovered 14-value ladder. The retained multi-package scan returns
15 candidate actions, not confirmed bugs. Re-reading 629 current raw magazine
operands supports 287 relative-to-default selections without a value disagreement
or missing default. The five checked handling fields match between KTS100 50 Rnd
and default 60 Rnd; reload and sway were not newly measured. Three unrelated
Blacklight inputs lack current/reference raw in the retained selector graph.
See the [dated receipt](../../reference-data/provenance/frosty-update-1.4.3.5-2026-09-30.json)
and its per-entry recheck and consistency artifacts. Native activation and earlier
panel observations keep their original evidence limits.

## Exhaustive source census (1.4.3.0)

The [reviewed primary-root census summary](../../reference-data/provenance/frosty-audit-branches-summary-2026-09-23.json)
(full report in the external audit reports directory, pinned by hash)
covers all 64 candidate base weapon triples: 6,112 referenced branches, 6,111 referenced
action objects and 14,015 selector references. All branch/action references resolve within
this set. Its 358 WPM selector lists support 6,007 selector-to-WB joins. The GS pass
covers 8,367 binding structures across eight structure types, supporting 5,089
selector-to-GS joins. The [parent fresh-decode check](../../reference-data/provenance/frosty-audit-branches-validation-2026-09-23.json)
independently matches every root branch/action reference, selector identity and GS
binding tuple. Earlier one-structure-type results were incomplete and are superseded.
Eight references whose target XML was absent were resolved through the catalog and
hash-checked raw target objects. Layout warnings remain.

The [complete action-field check](../../reference-data/provenance/frosty-audit-action-fields-2026-09-23.json)
freshly enumerates all 6,115 action objects in those raw bodies. Four are outside
the branch census: one in M27IAR and three in MP7A2. They have no internal caller
in their decoded source files; global/native use remains unresolved. All eight
action fields are retained. In addition to the main selector list, 191 imports
occur in `Field_f1f008ba`, 135 in `Field_2717f5c2` and 139 in `Field_072fe4eb`.
These fields include underbarrel and bipod references and require separate joins.
The earlier selector-to-GS/WB totals cover `Field_7e54e22c` only.
The [linked Ability ID check](../../reference-data/provenance/frosty-audit-action-ability-ids-2026-09-23.json)
matches all 139 action IDs to the exact linked Ability's ID. This confirms the
serialized association for 135 underbarrel and four bipod actions; it does not
establish when the game executes them.

The [underbarrel secondary-selector trace](../../reference-data/provenance/frosty-audit-underbarrel-parts-2026-09-23.json)
joins all 135 underbarrel actions across 27 weapons to their parent WB parts.
Its 190 secondary-selector references yield 393 single-selector matches across
14 shared parts and three inline parts. These are structural matches, not fully
evaluated activations. The four M320 families each have base, Plus and Reload
parts; M26DB has base and Reload parts. Plus parts list the Grenadier trait as a
second selector. Reload parts list Assault Gadget Reload and contain the same
`1.1` reload operand. Native selector evaluation and timing remain unresolved.

The shared M320 parts reference `PrimaryFire_M320` and `GS_M320HE`; smoke, AT and
thermobaric parts also carry distinct projectile references. M26DB contains a
buckshot firing reference and a separate Dragon's Breath projectile effect with
priority `9000`. That composition needs native application proof. HK417A2, M4A1
and XM7 also have inline Generic parts with a draw-step operand of `1`.
All 40 unmatched secondary references are `U_WPM_UBL_Any` in the checked parent
WB part lists; they are not evidence of global non-use. The earlier draft's zero
WPM counts checked only the main action list and cannot describe these paths.

The [SRU membership check](../../reference-data/provenance/frosty-audit-sru-validation-2026-09-23.json)
freshly validates all five SRU roots and their 186 distinct member targets. The four
M320 lists share 186 unique entries; M26DB has 183. The three M320-only entries are
the 1P86, QMK171A and M145MGO optic selectors. Every list repeats ANPAS35_Base at
indices 68 and 69. None of the SRU member targets overlaps the same action's
secondary selectors in the 135 checked actions. This confirms membership, not
whether the game adds, removes or resets these selectors. The repeated entry is
not a proven gameplay defect.

This is structural coverage, not native activation or multiplayer availability.
The progression-to-metadata join leaves 537 branches without a matching metadata
record and one with two matches. A [600-body raw check](../../reference-data/provenance/frosty-audit-branch-metadata-gaps-validation-2026-09-23.json)
confirms all 537 progression links and targets. None has a reference from the
scanned `Class_a9b2eb87` metadata class in the captured index. This is a metadata
join gap, not a missing raw target or proof that the attachment is unavailable.
A [follow-up grouping](../../reference-data/provenance/frosty-audit-phase1-checkpoint-2026-09-23.json)
reconciles the 537 branches into 135 known underbarrel choices, 51 default-like
selector paths, 350 further attachment action candidates and one VSSM branch.
The 51 paths include 46 `_Empty`-named records and five named optics: one Steiner
CQT and four ZT410 records. Their exact structural joins are checked; neither
names nor paths prove default selection or no-op behavior. VSSM branch 93 links to
`U_ATT_VSSM_Stock`, but has no exact identity join to the separate Folding Stock
ADS spread receipt. Availability and native activation remain unresolved.
The [Ultimax follow-up](../../reference-data/provenance/frosty-audit-ultimax-metadata-2026-09-23.json)
finds that `Short` and `ShortBarrel` share a progression entry, while the captured
Equipment lists select `ShortBarrel` by exact GUID. This resolves that source
association without proving that the other record is globally unused.

The [additional Ability census](../../reference-data/provenance/frosty-audit-additional-abilities-validation-2026-09-23.json)
checks another 142 roots: 135 UBL-labelled and seven melee-labelled records, not
bipod variants. Their branch arrays are empty, but each has an exact captured caller:
135 attachment action objects and seven equipment objects. Fresh raw decoding checks
all 142 roots and all 34 caller files, including both file and object GUIDs. These
records remain in scope. Empty branch arrays do not mean unused abilities. Their
other fields and the caller selectors still need review; source links alone do not
prove runtime activation.

## Composition rules

- A package's `WME_*` effects apply to a weapon only when that weapon's WB lists the
  package's part. M2010 ESR lists `WPM_BTM_FastBOLT02_W15`; L115, Mini Scout and
  Interdictor select that package but do not list its part.
- GS bindings are per weapon. `Vertical03_W20` has a recoil binding in `GS_BREN3` and
  none in `GS_M27IAR`.
- One action can select several packages; `scripts/frosty-multi-package-scan.py` lists
  them. Two such cases are game errors (Slim Angled, M121 A2/M45A1 ammo).
- `_W##` suffixes on `U_WPM_*` names are not costs; `Field_6ee865a5` is the only cost.
- WB animation and FOV ADS effects are parallel. When they agree they count once; a
  conflict stops generation. The GS ADS route is separate and not added.
- Magazine shifts on the site are relative to the default magazine. Regular packages
  (`U_WPM_MAG_Std_W05`) add draw +1 (site −1), so other magazines draw slower than the
  default even without a draw operand.

## Availability

- 5,542 attachment records; 11 have no branch in the ability root list. Of 5,531 linked
  branches, 5,388 have kill-switch default False and 143 True. These are exported
  defaults, not a live roster.
- A True default is good exclusion evidence (all 15 unmapped SubsonicFrangible assets
  are True). An unset switch does not prove availability.
- Source presence is not availability: SVK-8.6 Adjustable Angled and AK-205 Underslung
  Mount exist in the data but are not offered in game, and were removed.

## Unmatched branch follow-up (1.4.3.0, 23 September 2026)

The [reviewed branch evidence](../../reference-data/provenance/frosty-attachment-branches-reviewed-2026-09-23.json)
keeps source identities separate from live availability:

- M4A1 `ERG_Magwell` has a zero-cost MagazineWell category entry in the Ergonomic
  slot and selects `U_DPF_MagWell_Empty`. It is distinct from `ERG_FlaredMagwell`,
  which selects magwell-flare art and its shared modifier selector. Do not create
  a second player-facing Magwell Flare from the plain record; its purpose remains
  unresolved. Both inspected registry defaults are false.
- `AD_M4A1_ERG_Flare` directly resolves to **Mag Flare** (`ECC4BCCE`) and
  **Enables reloading while aiming down sights.** (`ECC670D6`) in the current US
  strings export. This corrects a transcription error in the worker draft that
  made the strings appear absent. UI wording is not native effect activation proof.
  The [exact package trace](../../reference-data/provenance/frosty-mag-flare-capability-2026-09-23.json)
  links the selected FlaredMagwell package to `WME_ADSReload_P10`, which contains
  boolean settings and no established reload-speed multiplier. A future utility
  indicator could distinguish this from a numerical stat change; active behavior
  and weapon eligibility still need validation.
- BROD 3 is source `BREN3`, as established by the weapon identity mapping.
  Its treated-barrel metadata directly names **Cryo**. The associated registry
  default is true; the current live offer is unverified.
- All 15 Subsonic Frangible attachment/progression/ability branches have individual
  registry references with true defaults. File hashes and all 15 registry values
  were checked, with three branch samples independently decoded. Current menu
  offers and server overrides remain unverified; true defaults are not proof of
  active exclusion or gameplay behavior.

The current-build strings file is under `builds/1.4.3.0/xml/Common/Localization/`;
the XML overlay holds a different strings snapshot. The reviewed report records
the exact current file hash. Stale metadata XML was replaced by raw decoding for
this review; conservative descriptor-layout warnings remain.

## Generated site values

| Area | Generator | Result |
|---|---|---|
| Barrel ADS | `scripts/frosty-barrel-ads.py` | 233 unique weapon/barrel selections (234 records). Basic, Short, Light, Cryogenic, Extended Light, Short Light +1; Extended, Heavy, Heavy Extended and both VSSM barrels 0. M4A1 Basic 200 ms; both VSSM barrels 250 ms. |
| Grip, laser, magazine handling | `scripts/frosty-attachment-handling.py` | 1,487 selections, 5,489 fields. Grips and lasers store per-weapon `frostyModifiers`; magazines use their existing per-weapon fields. |
| Sniper brakes | `scripts/frosty-sniper-brakes.py` | 16 weapon/brake pairs, +6 amount tiers (`GRM_Recoil_MZL_Bolt_P10`). |
| Linear Comp and burst | `scripts/frosty-assumption-review.py` | 45 Linear Comp and 8 burst selections (below). |
| Slots and prerequisites | `scripts/frosty-attachment-compatibility.py` | See [data graph](DATA_GRAPH.md#slots-and-prerequisites). |
| Collateral, ballistics | `scripts/frosty-collateral.py`, `scripts/frosty-ballistics.py` | See [Weapons](WEAPONS.md). |
| Tooltips, optic categories | `scripts/frosty-attachment-tooltips.py` | See [UI text](UI_TEXT.md#current-site-mapping). |

All generators accept `--root <Frosty export root>`; most accept `--check` for a
read-only comparison. They stop when a generated field loses its source mapping or the
input hashes change. Commands: [maintenance](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/MAINTENANCE.md#regenerate-attachment-modifiers).

### Handling details

- **Coordinates, not effects.** M60 and PW7A2 base indices come from `GRX_Weapons`
  (M60 ADS 2 → 1, M60 ADS movement 6 → 4, PW7A2 ADS movement 10 → 8). Bases and magazine
  modifiers changed together, so results are unchanged
  ([proof](../../reference-data/provenance/frosty-handling-coordinate-proof.json)).
- **Unbound selectors.** DRS-IAR Alloy Vertical and both RPK-74M 30-round magazines
  generate from matched sibling modifiers; three extra selectors have no binding and are
  recorded, not assigned values
  ([evidence](../../reference-data/provenance/frosty-handling-unbound-selector-review.json)).
- **Green laser.** The earlier handling trace finds the hip step on normal LA-23,
  but not on the `_IR_SP` variant. The current DRS-IAR mapping retains normal
  LA23PEQ and LA-23 IR SP alternatives. Their runtime selection and the latter's
  mode exclusivity are not established; the suffix alone does not exclude it.
  The [visibility review](../../reference-data/provenance/frosty-site-laser-visible-2026-09-23.json)
  preserves both source records.
- **Shotgun tube variants.** M1014 4 Rnd / 4 Fast are `MAG_Compact1` / `Compact2`; M87A1
  5 Rnd / 5 Fast are `590A1 MAG_Compact1` / `Compact3`. Variant values (99 tube; 4 and 5
  speedloader) identify the variants; they are not reload multipliers.
- **VZ.61 "lasers".** Canted, Folding, Ribbed and Stippled Stubby and Compact Handstop
  are grips on a shared rail.
- **Belt boxes.** M240L 75 Rnd binds `GDM_Array_ADSMoveDispersion_MAG_P10` (+1: 0.32 →
  0.22°). The L110/M123K 200-round selector has no spread binding; the site uses 0
  (bug entry 7).
- **Suppressor identities.** `ImprvdSuppressor01` is CQB, `ImprvdSuppressor02` is
  Lightened.

### Magazine capacities and reload operands (23 September 2026)

The [current magazine review](../../reference-data/provenance/frosty-site-magazines-2026-09-23.json)
traces all 287 selections through their exact ability actions, selectors and WB
effect lists. It checks 569 site leaves against descriptor-derived raw values.
The site reports nominal magazine rounds: 263 selected capacities are one below
the raw configured count, DB-12 is two below, and 23 match directly. This is a
representation and loaded-state question, not an automatic correction. The
current `Mag Size` tooltip says rounds in the selected magazine; `sim/core.js`
does not use that number for cadence. A future loaded-capacity value should state
whether chambers are included and distinguish spawn, empty and tactical reloads.

Of 282 reload-tier leaves, 101 select the raw 1.13 multiplier, one selects 1.277,
and 179 are neutral with no reload-speed effect in their selected graph. M121 A2
50 Fast is the exception: its selected package replaces `ReloadInfoArray`, with
`5.6 / 1.009009 ≈ 5.550` seconds. The site's generic tier gives
`6.267 / 1.13 ≈ 5.546018` seconds. A selection-specific animation override is a
source-backed proposal; native activation is still unverified. Ordinary 60 fps
shot timing cannot reliably distinguish this roughly four-millisecond difference.

The five existing magazine animation overrides are also source-backed after
time/speed division and millisecond rounding: M240L 75/100 Rnd 7100 ms, M60
50 Rnd 4534 ms, PP19 53 Rnd 2667 ms and RPK-74M 95 Rnd 2950 ms.
The [exception review](../../reference-data/provenance/frosty-reload-exceptions-leaves-2026-09-23.json)
retains the separate PP19 bug and composed-observation evidence.

### Ammunition effect operands (23 September 2026)

The [current ammo review](../../reference-data/provenance/frosty-site-ammo-effects-2026-09-23.json)
checks 83 effect leaves against exact attachment selectors and descriptor-offset
raw fields. All 337 applicable weapon/ammo comparisons agree. These include
subsonic recoil shifts of +1, penetration shifts of -6 on M2010/SV-98/PSR and -7
on Mini Scout, and the -9 hip-spread tier shifts on the four site shotguns.
The seven shared recoil/movement tier values agree for every applicable current
selection after per-weapon overrides are accounted for.

The same review checks the six shared spotting factors and the frangible/flechette
regeneration additions. Selected source operands support the site's index sums,
reversed spread/movement ladder signs, spot factors and delay additions. Native
activation and composition order remain separate questions.

All 77 class-based collateral fallback values are inactive for current choices:
all 328 selectable weapon/ammo pairs have a per-weapon collateral override. Their
retained values are software fallback data, not verified effective mechanics.

The [subsonic velocity review](../../reference-data/provenance/frosty-site-ammo-velocity-2026-09-23.json)
sources all 26 tier inputs from selected velocity factors and checks the slug ADS
spread increment (0.05 in both source movement branches for four shotguns).
Five prior screenshot-based absolute velocity inputs discarded source precision:

| Weapon / ammo | Prior site input | Base source velocity × selected factor |
|---|---:|---:|
| M417 A2 Subsonic / Subsonic HP | 273 m/s | 560 × 0.488570005 = 273.599203 m/s |
| PW7A2 Subsonic Tungsten | 341 m/s | 576 × 0.592999995 = 341.567997 m/s |
| USG-90 Subsonic / Subsonic HP | 265 m/s | 543 × 0.488570005 = 265.293513 m/s |

Every integer equals the floor of the source-derived candidate. This can explain
the original menu transcription; it is not evidence that the menu is wrong.
The site now retains these source-derived values. Ammo/barrel composition remains
an explicit native-consumer limit.

### Recoil operands

| Attachment | ADS amount / variation steps | Hip amount / variation steps |
|---|---|---|
| Linear Comp | −1 / +3 | −1 / +3 |
| Burst Training; SL9 Burst Mode | 0 / +3 | 0 / +3 |
| GRT-BC Burst Training | +1 / +3 | +1 / +3 |

Burst attachments select a fire-mode modifier and a behavior node (mode mask 8 = enum
value 3) whose selector the GS recoil bindings use. The +1/−1 amount operands cancel on
ordinary burst attachments; GRT-BC has +2/−1.

Applied follow-ups:

- Smooth Bolt: −0.5 time-exponent addition on 17 muzzles.
- `GRM_AutoIdentifier_P00`: −0.0006 s duration addition on five weapons, after any muzzle
  duration override.
- Mini Scout Tungsten: −7 amount steps (combined −1/−6 links).
- Slim Angled: moving-ADS index −1 on PSR, SV-98, L115, Mini Scout and
  Interdictor (bug entry 1a). KS18K is excluded; see the trace below.

The [current muzzle operand audit](../../reference-data/provenance/frosty-site-muzzle-operands-2026-09-23.json)
checks 172 recoil/spread/handling leaves: 151 match selected source operands and
17 are neutral or inactive software fallbacks. The audit recorded four source questions.
PP-19 Flash Comp has no GS selector binding in the captured body, and its WB package
contains a spotting effect without a recoil modifier. The site now uses neutral
ADS/hip recovery factors and no duration override for that choice. L115 Standard
Suppressor also lacks the GS hip-spread index binding; the site now uses zero tier
shift. These changes follow the recorded bug observations; the bounded graphs alone
do not prove native absence. See the attachment-bug records for those observations.

A raw byte search confirms the PP-19 result: `GS_PP19` does not contain the
`U_WPM_MZL_FlashCompensator_W15` selector GUID, while the `GS_UMP40` control does.
It is bound on 39 of the 40 Flash Comp weapons. This is the same kind of binding
omission as the L115 suppressor; see [attachment bugs](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/ATTACHMENT_BUGS.md) #6, which also has the operator report.

### Current grip and barrel field review (1.4.3.0, 23 September 2026)

The [grip/sight leaf review](../../reference-data/provenance/frosty-site-grips-sights-effect-review-2026-09-23.json)
covers 167 site entries. Its current selected GDM trace contains 535 moving-ADS
bindings in `Field_2ffeb6ac`, nine distinct-target KS18K bindings in `Field_b30a73ed`,
and 151 hip bindings in `Field_b53510be`. Compare effective per-weapon overrides,
not just shared catalog values. The QD Grip Pod and sniper Slim Angled outliers
match their mapped source operands. A missing direct selector operand is retained
as a bounded source gap, not proof of zero effect. The nine `noEffect` flags are
Analyzer UI flags; they are not native boolean findings.

The [heavy-family barrel review](../../reference-data/provenance/frosty-site-barrel-ads-spread-2026-09-23.json)
checks 61 selected weapon/barrel choices. Heavy, Heavy Extended and Cryogenic
match the site's four ADS spread factors: increment `0.666667`, firing decrease
coefficient `1.837117`, firing offset `0.666667`, and not-firing offset `0.666667`.
All 488 operand checks agree across both source branches, decoded values and raw
bytes. The [barrel velocity review](../../reference-data/provenance/frosty-site-barrel-velocity-2026-09-23.json)
sources `0.8/1.25` factors; the site's `-1/+1` tiers encode those values through
`0.8^(-tier)`. This does not claim that the native source stores those tier integers.
Native activation, priority and composition remain unresolved.

### Ergonomic attachment field review

The [ERGOS receipt](../../reference-data/provenance/frosty-site-ergos-2026-09-23.json)
records 51 effect leaves with exact selected attachment routes and raw bytes.
Draw timing uses the selected WME's `Field_9540bd8e=+1`; the site's `-1` shift is
its inverse representation because the resolver subtracts the shift. Mag Catch's
`1.063` maps to `Class_9705264b/Field_348b8cd1` in `WME_ReloadSpeedSmall_P05`.
VSSM automatic RPM maps to the WB's `799.999` RateOfFire, distinct from its single
shot rate and the Folding Stock's separate single-fire modifier.
The [L68D receipt](../../reference-data/provenance/frosty-2026-09-26-L68D-vssm-full-auto-replace-naming-limit.json)
records `Field_503c0ef4=true` and `Field_1180f1ee=1`; neither hash pairs with a
child name in the scoped pinned `GRX_Weapons` scan after the `StartDamage=25` control. This does not establish the enum domain, damage meaning, or runtime activation.

Buffer's `visualRecoil=-1` only selects the site's "Decreased" badge. Do not read
it as a measured magnitude or a native `-1` operand. The selected package contains
an opaque `Field_c4814c93` with `-1/0` variants and a separate three-component
`0.75` vector at `Field_3b707594`; their consumers and relation to this badge remain
unresolved. A recording can test visible motion but cannot identify that anonymous
field by itself. Other unmapped recoil tier and duration leaves retain their exact
source routes as semantic blockers; equal numbers are not accepted as mappings.

### ADS Bolt and sniper cadence

The [ADS Bolt source receipt](../../reference-data/provenance/frosty-site-ads-bolt-cadence-2026-09-23.json)
checks the site ID `ads_bolt` (DLC Bolt), available for M2010ESR, SV98M, MRAD and
L115A3. Its exact selector binds `WPM_ERG_DLCBolt_W25`, which imports
`WME_ADSBoltRechamber_P25`. The latter stores `Field_68c40b57=true` (one byte
`01` at offset 144). The package supplies a capability flag, not a demonstrated
25% speed bonus. Mini Scout and Interdictor are not in this attachment's current
four-weapon choice set; their base behavior needs separate comparison.

The Analyzer shows a Rechamber in ADS utility and does not apply an ADS Bolt cadence branch.
The proposed output must distinguish the next accepted shot from the next shot
with ADS fully restored. Without the attachment, ADS exit, rechambering and ADS
entry may affect the latter. Their overlap and the meaning of the zoom completion
fraction are unresolved, so adding three full durations is not yet justified.
Keep Recon's separate bolt-speed modifier fixed during the attachment comparison.
See [weapon timing](WEAPONS.md#timing-fields) and
the former capture rank 6 ([removed 28 September](../working/BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)).

## Lights

All twelve `GBM_Increase_Hip_{S1..S5,A30..A60}_RGT_P10` assets hold the same ten entries:
two hip branches (`Field_447d6d51`, `Field_0a160c57`), each with

| Target | Name | Operand |
|---|---|---|
| `Field_0084b1d1` | `IncreasePerShot` | ×0.666667 |
| `Field_2ca8533e` | `FiringDecreaseCoefficient` | ×1.837117 (= 0.666667^−1.5) |
| `Field_1b9eef5d` | `FiringDecreaseOffset` | ×0.666667 |
| `Field_4d3f0635` | `NotFiringDecreaseOffset` | ×0.666667 |
| `Field_aa558d2b` | `IdleDecreaseOffset` | ×0.666667 |

Links cover 62 weapons. The site applies these factors to 137 supported light
selections, treats a selected light as on, and does not model idle recovery. Native
activation is not decoded.

### Laser visibility remains a semantic blocker

The [visibility review](../../reference-data/provenance/frosty-site-laser-visible-2026-09-23.json)
traces the site's `laserVisible` flag to its enemy-visibility tooltip. The inspected
candidate `Class_bc0062dc/Field_32cf19f5` is true for every laser type, including
5 mW Red, 50 mW Violet and the Red combination device, whose site flags are false.
This rules out a direct use of that flag as the site's classification; it does
not prove that those site values are wrong. The candidate's meaning and native
visibility consumer are unknown. Keep source alternatives and their scope limits
in the receipt. The rank-11 paired beam/dot test checks the displayed claim without
expanding FX or material graphs.

## Sway

206 weapon-sway and 3 camera-sway objects. Shared P05/M05/P10 factors are
0.6666667/1.5/0.4444444. The site shows muzzle and magazine amount changes as a
percentage against the bare weapon (magazine strengths include −33.3% and −55.6%;
adverse muzzle factor 1.5 gives +50%). Iron-sight weapon sway (L62) is shown; camera
sway is not. `WME_DynamicPivot` uses
`Field_f235e44f`/`Field_a4f104cc` multipliers; canted iron sights set only
`Field_f235e44f` (2.5 or 3).

[L129](../../reference-data/provenance/frosty-2026-09-29-L129-absolute-sway.json)
screened the WB/GS roots of six sniper rifles and six DMRs for an absolute sway
baseline. The direct WB candidates are selector-owned `Class_2fea847d` records:
one `Field_90fd0310` operand and an iron selector were raw-checked per weapon.
The six sniper operands range from 1.008332 to 1.072083. Cached parent references
establish the candidate ownership; their pointer bytes were not independently
checked. L115 and SV-98 have two selector tokens beside one child reference, so
their ordering and activation are unresolved.

These candidates extend the sight-state context already recorded by L94 below;
they do not establish an absolute amplitude, an operation, or missing sniper
iron-sight factors. The site multiplies relative attachment factors, and the
existing L94 captures do not support applying local sight values as general ADS
multipliers. This bounded pass omitted external imports and broader target walks;
the provisional GS screen is not an absence claim. Reopen for a concrete absolute
baseline/consumer route rather than repeating these operands.

The [23 September optic discovery](../../reference-data/provenance/frosty-optic-discovery-2026-09-23.json)
captured `Affector_HoldBreath` and `PresEx_HoldBreath` from the registered hotfix
(Head 4892087). The expression's external pointer resolves to the existing
`SoldierOnlyPublicChannels.IsSniperHoldingBreath` object; the collection also
contains `InputBreathControl`. The expression references compiled resource
`08a1a89d496bbf73`. These records do not establish hold duration, sway reduction,
or standard multiplayer activation. A bounded search of 230 older soldier raw
captures found no caller of the expression. Keep breath-control modeling blocked
on an activation/consumer trace or controlled measurements.

The later [multiplayer ability review](../../reference-data/provenance/frosty-multiplayer-ability-candidates-reviewed-2026-09-23.json)
found a direct `Ability_StanceFlak/Field_a21a7b29[0]` import of that same
`Affector_HoldBreath`. Its separate StanceFlak expression imports `CurrentStance`,
`IsBenefittingFromBipod` and the left/right/up mounted channels. This supplies an
authored ability caller for the affector. It does not decode the condition, identify
an active standard MP class, or establish a breath-control/protection bonus.

## VSSM barrel ADS follow-up (1.4.3.0, 23 September 2026)

The [reviewed source trace](../../reference-data/provenance/frosty-vssm-ads-reviewed-2026-09-23.json)
confirms two separate paths. `GS_VSSM/Field_4d248d91[11]` binds
`GID_ADSTime_BRL_P10` to the regular-barrel selector
`2d77eab2-17a5-48bb-b917-3a35913e0dd4`. Both integer modifier operands are 1.
The WB package list is `Class_542ac52c/Field_0cd9f20f[72:74]`: its regular and
no-port packages contain four silenced/audio/spotting effects each, with no ADS
animation or FOV timing effect in either package.

Six raw assets passed independent hash and file-GUID checks. The GS/WB containing
layouts retain decoder warnings. The raw enum value 0 is labeled `Field_84e57075`
in XML; that label alone does not identify a native calculation.

Keep the separate GS tier visible in research. It is not evidence to add another
delay to the current 250 ms WB-derived value. A controlled regular/ASM barrel
comparison with the factory optic and a fixed magazine, or the native GS consumer,
is still needed to determine its effect on completed ADS.

The [63-weapon ADS comparison](../../reference-data/provenance/frosty-site-ads-2026-09-23.json)
also identifies an Interdictor exception. Full Angled selector `8ad0e9cd…` maps to
GS binding 1; Slim Angled has that selector and `8cf80d8c…`, mapping to bindings
1 and 2. Both bind the +1/+1 ADS operand package. The site gives one tier to each
grip. Whether the native bindings add, deduplicate or use priority is unresolved.
The ranked capture plan gives 300 versus 366.667 ms predictions for Slim Angled
with Basic barrel, Standard ammo and 5 Rnd held fixed.

## Spotting candidates

The [exact-choice audit](../../reference-data/provenance/frosty-site-spotting-2026-09-23.json)
checks 653 muzzle, 233 barrel and 328 ammo choices. Four selections bind an
SP-prefixed suppressor package carrying 0.1 at priority 9001: M39 EMR/M417 A2
CQB and DRS-IAR/M2010 ESR Lightened. The site uses 0.14 (21 m); a controlling
0.1 package would give 15 m. Do not multiply the linked packages into 0.014
without native composition evidence. A prefix alone does not exclude these
multiplayer-bound packages.

[L47](../../reference-data/provenance/frosty-2026-09-24-L47-selected-spotting-chain.json)
checks the exact M39 EMR WB import through the selector-matching SP wrapper to
its recorded WME target. Three raw-backed assertions pass. This strengthens one
existing association; Attachment/AAM identity comes from the prior mapping.
Native activation and composition remain open, so the existing rank-1 capture
and site factor stay unchanged.

[L49](../../reference-data/provenance/frosty-2026-09-24-L49-spotting-package-context.json)
also verifies the ordinary wrapper at WB index 81 with the same selector. Both
are listed; this does not prove eligibility or a winner. SP metadata priority
9001 and two opaque false flags supply no verified mode rule. Keep the existing
spotting test; neither package naming nor priority establishes composition.

VSSM's actual default selects `vssm_suppressed`, whose package imports P35
(world 0, minimap 0.06); the site gives 0/9 m. PP-19 Flash Hider and Flash Comp
both bind `WME_SpotRange_3D_P10` (world 0, minimap 1), matching site factors.
These checks resolve exact associations; activation and priority remain open.

## Optic categories and costs

- The site keeps six sight categories: Iron Sights (5), Standard Optic (10), Variable
  Low (20), Variable High (25), Thermal (25), Thermal Hybrid (35).
  `WEAPON_ATTS[id].sight` restricts categories; `sightPoints` overrides cost (iron 15 on
  six bolt-actions, including the Interdictor since 1.4.3.0).
- `optic_category` in `scripts/frosty-attachment-tooltips.py` classifies each Frosty
  optic by its UI label only ("Basic Sight" = iron; variable ranges listed explicitly).
  It stops on an unknown label or two costs for one category on one weapon.
- `scripts/optic-costs.test.mjs` compares the newest
  `frosty-optic-category-mapping-*.json` with `data/attachments.json` (category set,
  `sightPoints`, default costs).
- 350 site optic choices map to 1,927 Frosty sight records. Optic names:
  [UI text](UI_TEXT.md#attachment-and-optic-names-aam-records).

## Optic render FOV and zoom

Evidence: [frosty-optic-render-fov-2026-09-16.json](../../reference-data/provenance/frosty-optic-render-fov-2026-09-16.json).
Field meanings come from values and in-game screenshots.

### Optic field atlas (1.4.3.5, L784)

[L784](../../reference-data/provenance/frosty-2026-10-01-L784-optic-field-atlas.json) covers 158 initial optic candidates and 114 additional exact linked owners: 731 typed field families and 1,735 import edges. Supplemental owners include input options, aiming controllers, render/zoom curves, lens-flare settings and aim-assist settings. Zoom, PiP, world/render FOV, glint-related sources and zeroing-related fields remain separate. Numeric optical settings were inventoried beyond the initial route-prefix scope; texture/bone/registry context retains explicit descriptor dispositions.

The render-FOV controls passed before extraction: base RMR 55 degrees and RMR Riser 40, both from the same exact `Class_3a930efc` descriptor. Three zoom-definition owners also reproduce the L133 type, raw-hash and input-reference controls. The worker raw-checked 4,507 consequential operands; the parent review separately checks the controls and sampled operands. Array positions, legacy labels, equal values and asset names do not establish a field role. Optical sensitivity, magnification, render scale, relative sway and glint strength are not interchangeable. Source settings without a confirmed consumer stay known limits or unexplained frontier fields; this pass does not turn O1-O3 into numeric gameplay claims.

### Glint, zeroing and breath frontier (1.4.3.5, L795)

[L795](../../reference-data/provenance/frosty-2026-10-01-L795-optic-glint-zeroing-frontier.json) records 348 current owner and consumer dispositions. The M2010 iron-sight selector, NoScopeGlint and NoFlare control passed nine raw reads before findings. The worker checked 56,591 operands; parent review and sampled raw re-reads passed. The semantic pass covers 98 glint/zeroing families, 20 modifier-control families and exact rangefinder/breath schemas.

Exact current registry links name six fields in 12 WB zeroing blocks. Two enum fields retain their raw signed values and hashed members. Current SoldierInfoPromptZeroing pointers join the exact HUDLoadout_WeaponZeroingDBD export and its ZeroingDistance binding. They provide no selectable numeric UI array or native zeroing equation. Anti-Glare UI text supports the existing qualitative glint wording; source differences do not establish a cone angle or strength percentage.

The breath presentation expression joins an exact public channel and compiled resource RID `08a1a89d496bbf73`. Four qualified resource inventories contained no matching body. [L818](../../reference-data/provenance/frosty-2026-10-01-L818-compiled-breath-resource-frontier.json) later captured and verified the exact current body; its compiled grammar remains unresolved. No native expression grammar, breath duration or recovery stat was established. Eleven compact routes in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) record the attempted sources and reopen conditions. New exact source-owner candidates remain frontier work; no new numeric comparison is proposed.

### Optic source frontier (1.4.3.5, L794)

[L794](../../reference-data/provenance/frosty-2026-10-01-L794-optic-fov-pip-frontier.json) traces 125 current FOV/controller/zoom/input owners plus three exact PiP/reset supplements: 2,155 scalar occurrences and 99 concrete families. The RMR 55 and Riser 40 controls passed first. All 4,182 consequential raw reads passed; parent native review and sampled re-reads passed.

Sixteen current zoom bodies reproduce the existing three-field source relationship. Thirty-one current options resolve 75 localized records. Exact descriptor, SDK, prior-receipt, registry, UI and available consumer searches retain the unknown numeric roles. Selected-part and inline/shared precedence remain unresolved. No new effective numeric stat is proposed; the existing optic identity/PiP-FOV proposal is retained. Exact visual composition targets remain separate frontier work.

The batch's compact family limits are in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json). Field names, array order and matching scalar values do not establish native optical meaning.

### Optic visual composition frontier (1.4.3.5, L797)

[L797](../../reference-data/provenance/frosty-2026-10-01-L797-optic-composition-frontier.json) covers 41 optical composition roots and two exact linked resource-backed owners: 11,251 typed occurrences, 383 full field families and 292 numeric families. The RMR incoming pointer, exported root/type key and same-owner enum control passed first. All 10,594 consequential reads passed; parent native review and sampled raw re-reads passed.

The exact graph contains 171 local edges and four external imports; all four reach the two included thermal owners. RMR contains the text tokens Zoom, Distortion, IsRound, Attenuation and BackgroundBlur. The descriptor, 27 SDK type records and available independent consumer/schema sources do not bind those tokens to numeric array members. Array order supplies no confirmed view or reticle statistic. The atlas retains 84 lens/glint operands with their separate role limits.

Each of the 292 numeric family routes has a compact tried/stop/reopen row in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json). Exact typed source coverage does not establish optical units or native composition. No new numeric stat is proposed.

### Optical consumer residuals (1.4.3.5, L802)

[L802](../../reference-data/provenance/frosty-2026-10-01-L802-optic-consumer-residual-frontier.json) reconciles 3,289 source candidates from the optic and linked-owner inventories, plus all 224 initially ranked identities. All 100 optical ranked identities retain exact prior dispositions. RMR and zoom controls passed first. The pass adds 309 raw reads and qualifies 24 exact imported target objects; parent review and an independent new-owner operand read passed.

The 22 CrosshairPropertyInterface entries identify case-sensitive property-name hashes through the confirmed hash algorithm. They supply structural identifiers, without a numeric reticle size, opacity or zoom meaning. Current option UI states behavior; the remaining shader, aiming-input and NoAssist fields do not establish native optical equations. The exact sight-to-canted blend owner adds [13 typed source contexts](../../reference-data/frosty/weapon-frontier/field-atlas-addendum-L802.json), including 11 scalars and 12 identities absent from the Stage 1 baseline; its float at offset 152 is zero, with role and units unresolved.

Every candidate maps to its immutable source context. This mapping records the available field evidence and limits; generic ability, handling and configuration meanings remain open. The batch has 171 compact source groups in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json). No missing qualified owner request or new numeric comparison stat is established. Remaining source contexts continue in later batches.

### Modifier residual fields (1.4.3.5, L804)

[L804](../../reference-data/provenance/frosty-2026-10-01-L804-modifier-residual-frontier.json) traces 42 assigned modifier identities across ten current representative bodies. The same-owner control passed six raw reads first. Fifty new operand/import-export reads, 15 local-owner pointer reads and two qualified rangefinder proof reuses retain the actual declaring descriptors and container parents. Parent review and independent samples passed. Ten direct current edges have no missing target body.

Twenty-one prior receipt matches have equal source hashes, offsets and bytes. Existing fire-mode source/model context remains prior evidence; unknown flags and enum members gain no native operation from those matches. No new comparison stat or capture target is established. Forty new compact limits in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) retain exact modifier context. Shared WB, optic, projectile and ammo contexts remain separate.

### Laser and light source fields (1.4.3.5, L807)

[L807](../../reference-data/provenance/frosty-2026-10-01-L807-laser-light-source-frontier.json) traces 150 identities and 158 previously unexamined contexts on ten exact laser/flashlight FX source routes. Three qualified controls and 157 new representative raw reads passed. Parent review and an independent sample passed. The pass preserves 13 prior outgoing graph contexts and repeats no L802 context.

Ten current declaring schemas retain hashed field names. Exact source/registry and independent consumer checks establish no new numeric role or player comparison stat. Serialized FX fields are source context; their values do not establish a laser or light gameplay effect. Compact source groups in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) record the attempted sources and reopen conditions. Roles, units and native operation remain explicit limits.

### Mixed optical owner fields (1.4.3.5, L809)

[L809](../../reference-data/provenance/frosty-2026-10-01-L809-mixed-optic-source-frontier.json) traces 150 identities in 362 remaining WB, modifier, projectile, registry and ammo source contexts. The RMR control passed first. All 420 consequential checks and 92 declared parent-container proofs passed; parent review and an independent sample passed. The batch repeats no L802 or L807 source context.

Nineteen current declaring schemas retain hashed names. Eighteen exact same-source prior contexts preserve role limits. Consumer mentions are qualified against their actual property and owner; a shared hash supplies no alias or operation. No new unit, operator or comparison stat is established. Compact groups in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) retain tried sources and reopen evidence. Mixed owner context does not establish an optical role.

### Optical container source contexts (L812)

[L812](../../reference-data/provenance/frosty-2026-10-01-L812-mixed-optic-container-frontier.json) maps 200 identities in 847 remaining mixed-owner contexts. Controls passed first. The pass adds 917 raw operand checks and 372 declared parent proofs; parent review and an independent container read passed. Exact underbarrel source memberships remain excluded from semantic processing: 135 external profile routes and 270 source memberships. No representative operand uses an excluded route.

Sixteen declaring schemas retain hashed names. Thirty-six exact prior context joins retain their limits; 21 consumer-mention files are qualified by actual property and owner. There is no new same-source registry role or numeric comparison stat. Compact source groups in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) retain tried routes and reopen evidence. Serialization, field names and native operation remain separate.

### Optical sway source contexts (L814)

[L814](../../reference-data/provenance/frosty-2026-10-01-L814-optic-sway-source-frontier.json) maps the next 111 optical/mixed identities in 491 remaining source contexts. Controls passed first. All 625 consequential raw reads and 351 declared parent proofs passed; parent review and an independent sample passed. No previously reviewed optical context is repeated.

Three exact inherited Class_2fea847d/Field_90fd0310 source contexts retain typed sway candidates. They do not establish a selected WB/WM receiver, operator, unit or native composition. The batch establishes no new numeric stat. Compact source groups in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) retain available evidence limits and reopen conditions. A typed candidate is distinct from a confirmed player comparison effect.

### Remaining linked optical and FX fields (L815)

[L815](../../reference-data/provenance/frosty-2026-10-01-L815-remaining-extra-owner-frontier.json) The pass covers 242 identities in 268 remaining linked-owner contexts. Five controls passed first. There are 287 new operand reads and 112 declared parent proofs; parent review and an independent sample passed. Exact contexts do not repeat earlier optical or FX batches.

Nineteen declaring schemas retain hashed names. Three qualified prior zoom contexts retain their limits. Consumer mentions are checked against their actual properties and owners. No new numeric role, comparison stat or missing selected consumer is established. Compact source groups retain the available evidence and reopen conditions. The compact limits are in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json).

### Current compiled breath resource (L818)

[L818](../../reference-data/provenance/frosty-2026-10-01-L818-compiled-breath-resource-frontier.json) follows the exact current PresEx_HoldBreath RID `08a1a89d496bbf73` through the installed SDK lookup and raw export route. The source/channel controls passed first. The shared helper captured a known resource control and the 224-byte target on Head 4909002. Current source identity, resource status and both body hashes passed independent checks. This supersedes the earlier scoped inventory gap with a current body proof.

The target type is SerializedExpressionNodeGraph. The inspected current SDK, collector and 273 C# source files supply raw access and type identity, without a validated graph grammar or known-answer node/operator control. No typed graph fields, breath duration, recovery equation or new comparison stat were decoded. The resource owner and source edge are retained; the compact limit in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) names the parser or native-consumer evidence needed to reopen it. Installed handler metadata continues in L824.

### Installed compiled resource handlers (L824)

[L824](../../reference-data/provenance/frosty-2026-10-01-L824-compiled-resource-handler-frontier.json) inspects 19 current installed root, plugin and BF6 assemblies, covering 29,626 types with zero loader failures. Texture resource inheritance and its declared Read contract pass a positive metadata/source control; the exact current breath RID operand is independently re-read. Parent review passed. Assembly identities, references and hashes qualify the bounded inventory.

Texture is the sole Resource subclass in that inventory. The localization plugin handler registration names UITextDatabase and is distinct from expression graph decoding. The inspected metadata establishes no validated SerializedExpressionNodeGraph grammar, typed graph fields or new stat. Native and unnamed mechanisms remain unknown. The grouped limit in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) reopens with a validated graph parser and current semantic control, or an exact native-consumer contract.

### Emitter and atlas resource types (L825)

[L825](../../reference-data/provenance/frosty-2026-10-01-L825-emitter-atlas-resource-frontier.json) qualifies two current EmitterGraphResource bodies and one AtlasTexture body from exact source RID operands. Known source/resource and Texture contract controls passed first. Current resource identities, body hashes and consequential source operands passed independent checks. Parent review passed. The bounded grammar search covers 287 source files and 19 current installed assemblies.

The local AtlasTexturePlugin source declares a dedicated Read and SaveBytes layout. Its version-three length agrees with the current 92-byte body. This is a parser candidate; length agreement and an unloaded plugin source do not provide an independent current semantic control. Texture's Read contract is not transferred to AtlasTexture. The emitter type remains opaque under the inspected source and handler routes. No typed resource field or new comparison stat is promoted. Compact boundaries in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) name the required controls and consumer contracts. The atlas-control route continues in L826.

### Current atlas resource control (L826)

[L826](../../reference-data/provenance/frosty-2026-10-01-L826-atlas-resource-control-frontier.json) The pass checks 688 receipt, document and index files, three current resource inventories, the current manifest and six plugin source files. Known controls passed first; parent review and an independent source operand read passed. The sole qualified current AtlasTexture body is the captured 92-byte target. Earlier atlas bodies are on Head 4892087 with Read False and supply no current semantic control.

The source DDS export contract consumes Width, Height and MipCount. The checked evidence contains no independently known current dimensions, mip count, chunk or DDS fixture to validate that candidate reader. The route stays open at a precise control gap; no payload field or comparison stat is promoted. The compact boundary in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) records the required validation evidence.

### Current mesh resource control (L827)

[L827](../../reference-data/provenance/frosty-2026-10-01-L827-mesh-resource-control-frontier.json) The pass checks the exact current 1,344-byte MeshSet body, 19 current assemblies, 676 prior receipts, four current resource inventories, 23 plugin source files and the current manifest. Known controls passed first; parent review and an independent RID operand read passed. Historical metadata-only bodies are retained as context.

The dedicated MeshSet source reader has an explicit Battlefield6 branch. It is a positive parser candidate, without an independent current bounds, LOD, vertex or chunk control in the checked scope. Older game field positions do not qualify the current body. The route stays open at that control gap; no payload field or comparison stat is promoted. The compact boundary in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) records the required validation evidence.

### Further linked optical and FX owners (L822)

[L822](../../reference-data/provenance/frosty-2026-10-01-L822-linked-optical-fx-owner-frontier.json) types seven further current metadata owners reached by exact source pointers: the NVG expression and query data, volume-light emitter, mesh, shader, texture metadata and World LOD group. The same-current expression/channel/RID control passed first. The owners contain 673 typed occurrences in 465 families: 321 new full descriptor/path identities and 144 existing identities with new contexts. Field/export, string and selected-channel reads passed; parent review and an independent operand sample passed.

All 14 actual EBX pointers resolve to exact current exported objects. Five nonzero resource edges retain their actual body/type proofs and the parser/control limits in L824-L827. Five DQD labels have same-struct and local exported bindings; import-array position supplies no channel meaning. Shared rendering owners are qualified graph context, without a selected weapon value or native comparison equation. No new displayed stat is established. Fifty-nine compact class/route groups in [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) retain source attempts and reopen conditions. The current atlas adds every qualified typed field while preserving the baseline.

### Current optic field atlas (L819)

[L819](../../reference-data/provenance/frosty-2026-10-01-L819-current-weapon-field-atlas.json) includes optic, attachment/modifier and linked presentation owners in the [current field atlas](../../reference-data/frosty/weapon-frontier/field-atlas.json). The declared optic group has 749 distinct identities in 1,574 source contexts. Mixed modifier, camera, shader, UI and FX owners retain their own qualified graph contexts. Group counts overlap; registry reachability does not select an optic effect.

The source passes cover zoom, PiP, FOV, glint, zeroing, aiming input, sway, reticle/lens composition and exact linked resource edges. Sixteen current zoom bodies reproduce the existing three-field source relationship. Thirty-one optic options resolve 75 localized records. Exact zeroing HUD and public-channel bindings are traced. Anti-Glare text supports the existing qualitative glint wording. Field names and array positions supply no native units or numeric effect.

The current breath and NVG expression bodies, emitter resources, AtlasTexture and MeshSet bodies are captured and hashed. Their grammar or same-current semantic control remains a precise limit. O1-O3 are retained as known gaps. The field atlas and [compact route limits](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) show what was tried and what would reopen each route. No new effective zoom, glint percentage, zeroing distance or breath timer is promoted.

### Finding the part an attachment uses

Take the attachment's selector GUIDs (the `selectors` in
`frosty-optic-category-mapping-*.json`). In the WB, the part in `Field_0cd9f20f` whose
`Field_819acc98` lists the GUID is the part (an external `WPM_*` file or an inline
`Class_897c99a7`). Follow its local pointers to `Field_7768ebf2` (render FOV) and to any
`Class_fe7cd16a` (aim override). Ignore inline `U_ATT_*` model parts that list the same
selector without an aim; they caused about 35 false aim mismatches.

### Render FOV

`Field_7768ebf2` is the weapon render FOV in degrees; 55 is the default. It changes how
large the weapon, optic and arms are drawn, not the world zoom.

- **RPK-74M and L115 (bug entry 11).** They link the base
  `WPM_SCP_{RMR,RomeoX,EotechEFLX,AcroP2,TrijiconSRO,ShieldCQS}` parts (55). Other long
  guns use `_Riser` or `_LowRiser` parts at 40 (CQ RDS 44). Confirmed in game on the
  RPK-74M: the optic looks small and the arm stretched.
- **Consistency.** 57 of 63 optics have one value on every weapon. Riser, low-riser and
  mounted versions give the same value everywhere; only the six base parts differ.
- **Pistols.** ES 5.7, GGH-22, P18 and M45A1 use the base parts; M44, vz. 61 and M357
  Trait use `_LowRiser` (40). 55 on the four may be unintended; not checked in game.
- **Mounted parts.** `RMR_Mounted` (38), `AcroP2_Mounted` (42), `TrijiconSRO_Mounted`
  (42) and `EotechELFX_Mounted` (55) are not linked by any WB. `ShieldCQS_Short_Mounted`
  (44) is linked by one weapon.
- **M2010 ESR.** Inline model parts hold SDO 55 (shared part 34) and LERT 59 (shared 20).
  Which value applies is not known.
- **No formula.** Render FOV does not follow magnification (correlation about −0.6 with
  log magnification). 6× to 10× scopes use 16–28; red dots and low-power optics mostly
  28–44; at 3.50× the SDO has 34 and the MGO 48. Read the value per part.
- **Rejected causes.** Riser model height (same model and aim), the
  `Field_149939ab`/`Field_e9129d03` pair (1.25–1.3 on some riser parts; the reviewed
  MRO blocks have the pair at 1.0, without that non-unit value) and the zoom levels.

The [23 September raw review](../../reference-data/provenance/frosty-optic-parts-2026-09-23.json)
confirms the distinct M2010 paths: WB part entry 15 selects local object 34, which
leads through object 41 to model/render object 6 (55); LERT's local object 30 leads
through 42 to object 5 (59). Shared parts at entries 11 and 48 hold 34 and 20.
The local render objects retain layout warnings. Named GRX anchors identify the
modifier structure, but do not establish native precedence. Do not treat array
order as priority or these render records as aiming-controller overrides.
The same review reads the Riser field pair as 1.3 on RMR and 1.2 on Acro P2;
sampled RMR base and MRO values are 1.0. The pair's physical meaning remains unknown.

### Iron sights

- No iron-sight part overrides the aim, so every weapon uses `Aim_1x50` → `1_5xZoom`:
  **1.50×**. 1.00× optics (`Aim_01x00_PiP`) zoom less. The operator confirmed this in
  game; the site shows "Iron Sights (1.50x)".
- Iron render FOV is weapon specific: 18 (KTS100 MK8) to 50, except SL9 and four
  pistols at 55. The SL9 was checked in game with no visible effect found; the value may
  still be unset by mistake. Screenshots with very different values (SL9 55, KTS100 MK8
  18, PW7A2 50) show the same world zoom; only the weapon size differs.

### Zoom levels

| Asset | Camera FOV (°) | Zoom | PiP factor |
|---|---|---|---|
| `DefaultBase`, `1_0xZoom`, `Zoom_01x00_PiP` | 55 | 1.00 | 1 |
| `1_25xZoom` | 45.21893 | 1.25 | 1 |
| `1_5xZoom` | 38.27812 | 1.50 | 1 |
| `Zoom_01x50_PiP` | 39.2611 | 1.50 | 1.027778 |
| `Zoom_04x00_PiP` | 18.47956 | 4.00 | 1.25 |
| `Zoom_10x00_PiP` | 8.929769 | 10.00 | 1.5 |

Camera FOV = 2·atan(tan 27.5° × factor / zoom). All 36 levels are in the report
(`zoomLevels`). `Aim_Default_IronSight` (`1_25xZoom_IronSights`) exists, but no weapon
blueprint links it. The G36 built-in sights use `Aim_Fast_1x25` and
`Aim_300_6_1x00_8x00`.

### Recheck after an update

**PiP setting (1.4.3.0).** EA documents a new switch: disabled uses full-screen
FOV zoom; enabled combines that with extra zoom inside the optic. EA states that
total magnification stays unchanged. [Official update notes](https://forums.ea.com/blog/battlefield-game-info-hub-en/battlefield-6-update-1-4-3-0/13707600).
The raw `Aim_03x50_PiP` comparison adds an exact reference to
`Common/GameSetup/Options/Graphics/OptionEnablePiPZoom`; all shared decoded values
match the older capture. The option record contains `EnablePiPZoom` and `true`,
which does not establish the player's effective setting. Record PiP on/off with
camera FOV and ADS FOV settings in future optic comparisons. The documented
behavior does not clear nested decoder warnings or prove a native formula.
[Source review](../../reference-data/provenance/frosty-pip-review-2026-09-23.json)
and [setting context](../../reference-data/provenance/frosty-pip-setting-context-2026-09-23.json).

Compare `opticRenderFovByPart`, `riserFamilyLinksByWeapon` and `ironSights` in a new
dated report with this one. All 1,810 optic parts with their own aim zoom to the
magnification in their UI label.

### Optic input option references (1.4.3.0)

The [L133 source receipt](../../reference-data/provenance/frosty-2026-09-29-L133-optic-input.json)
traces six aiming controllers and the joystick-sensitivity camera root. The six
controllers share five references: SoldierZoomSensitivity, UniformSoldierAiming,
its coefficient, SmoothZoomInputSensitivity, and the separate Render option
FieldOfViewScaleADS. Four PiP zoom definitions (1×, 2×, 4× and 10×) reference
distinct per-tier sensitivity options through `Class_86ce0d70/Field_58cc4905`.
That field belongs to the zoom definition, not the controller. DefaultBase has
a raw null pointer there; this does not establish final no-zoom input behavior.

The four exactly referenced option bodies each have one `Class_921071e8` object
and the same numeric block: `Field_8ee32a15` 0.1, `Field_e2253f2b` 2,
`Field_8cf424e7` 1 and `Field_4276044b` 0.01. The first option's third field is
independently raw-verified. Default, range and step roles remain unresolved, as
do the effective sensitivity equation and activation. No attachment-to-controller
join is established here. These input references do not supply an optic sway,
movement or magnification multiplier, or support a numeric comparison proposal.

### Visibility and zeroing research

The [bounded glint trace](../../reference-data/provenance/frosty-optic-glint-reviewed-2026-09-23.json)
resolves the M2010 ESR iron-sight attachment through its ability action to
`U_WPM_IronSights`, which matches the selector of `WPM_NoScopeGlint` in the
weapon part list. Its modifier references
`WeaponLensFlareData_NoFlare`; the target's `Field_3062d390` array is empty.
The decoy anti-glint affector selects a separate unlock/package that references
the same target. The checked 6P67 part list lacks `WPM_NoScopeGlint`; this does
not establish whether the 6P67 can produce glint through another path. Active
multiplayer selection and a gameplay distance threshold are not established.

The narrow discovery pass found no zeroing name under gameplay/hardware/setup
folders. A wider catalog check found standard-MP zeroing HUD routes and a
RangeFinder weapon package. This is why a name-search miss is not proof that a
mechanic is absent. The [reviewed UI/package trace](../../reference-data/provenance/frosty-zeroing-reviewed-2026-09-23.json)
links the multiplayer widget to `ZeroingDistance`, and separately links the
rangefinder package to `Has Rangefinder`. The package has two true booleans;
their individual names and native application are not established. The
[weapon zeroing blocks](WEAPONS.md#zeroing-source-configuration-1430-23-september-2026)
provide named scalar limits and raw integer lists, with separate runtime limits.

### Anti Glare coating flare fields (1.4.3.0, 26 September 2026)

The [L95 source receipt](../../reference-data/provenance/frosty-2026-09-26-L95-anti-glare-coating.json)
records six selected sniper routes. Four same-weapon pairs and the actual
L115A3 baseline → MRAD_AG route change only per-record INT64
`Field_2e15621f` and a two-FLOAT32 `Field_c998527d` structure. The INT64 is not
an EBX resource reference. Both fields lack verified semantic names; the tuple's
components are `Field_3901db14` and `Field_42fc0f5e`.

| Record | Component 1: base → coating | Stored reduction | Component 2: base → coating | Stored reduction |
|---:|---:|---:|---:|---:|
| 0 | 0.015 → 0.007 | 53.3% | 0.015 → 0.007 | 53.3% |
| 1 | 0.03 → 0.015 | 50.0% | 0.015 → 0.01 | 33.3% |
| 2 | 0.06 → 0.03 | 50.0% | 0.015 → 0.01 | 33.3% |
| 3 | 0.06 → 0.03 | 50.0% | 0.06 → 0.03 | 50.0% |

MiniFix has three records; the other numeric comparisons have four. These are
stored component ratios only, not intensity, size, distance, angle, or
rendered-glint percentages. The Interdictor WB and coating WPM resolve to the
same serialized `WeaponLensFlareData_DesertTechHTI_AG` file/object; this source
equality does not establish runtime effect. Runtime activation and composition
remain unknown. No numeric site change is supported. The
[L96–L98 follow-up receipt](../../reference-data/provenance/frosty-2026-09-26-L96-L98-optic-accessories.json)
raw-verifies the shared description's StringId `3E3CC230`: “Reduces visible cone
of scope glint with an anti-reflective coating.” This supports a descriptive
utility label. It does not identify the tuple's units or establish a cone-angle
percentage. Reopen the numeric question for a typed field name/consumer or a
measurement of a defined glint quantity.

### SGX suppressor sway identity (1.4.3.0, 23 September 2026)

The [current SGX lineage review](../../reference-data/provenance/frosty-site-sgx-sway-lineage-2026-09-23.json)
traces exact attachment actions and selectors to MPX WB local object 20,
`Class_2fea847d/Field_90fd0310`. Its raw value is `0.9752820134` (offset 5156,
`15ac793f`). The wrapper lists the ConditionalExtended selector used by Long
Suppressor (SRD9) and CQB Suppressor (Compact Streamer). Light Suppressor
(SAI Cobra) selects a different package and does not share that selector.

The site's SGX Light Suppressor override `0.975282` therefore has a likely stale
attachment identity. The proposal is to move it to CQB Suppressor: Light's displayed
sway delta would change from -2.5% to neutral, and CQB from neutral to -2.5%.
Long's `1.462923` equals the local factor times its selected `WME_WSway_M05`
factor `1.5`; keep it as a source-compatible composition candidate. Current raw
hashes and exact attachment XML identities were checked separately from the older
13 September provenance. Native selector activation and multiplication remain
unproved. The local wrapper also lists a second selector; a shared selector alone
does not establish whether either or both are required. The override was moved
from Light to CQB Suppressor on 23 September; Long is unchanged. The paired capture
was [removed 28 September](../working/BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026).

**Same pattern on barrels.** Local WB sway overrides bound to the shared
`U_WPM_ANY_ConditionalShort`/`ConditionalExtended` selectors exist on three more
weapons, all on barrels:

| Weapon | Barrel choices | Local sway factor |
|---|---|---|
| GGH22 | Short and Extended | 0.850746 |
| Mini Scout | Short | 1.033862 |
| BROD3 | Short | Two parts: 1.016938 and 1.024638 |

No shared barrel package imports a sway effect, and the site models
barrel sway only through these per-weapon values (`weaponSwayMultByWeapon` on the barrel).
The site applies Mini Scout Short ×1.033862 since 23 September. GGH22's Short and
Extended barrels are not offered in game. BROD3 is deferred: how its two parts combine
is not known.
[Receipt](../../reference-data/provenance/frosty-source-leads-2026-09-23.json).

**Superseded by L94 (26 September): these locals are sight-gated.** The second
selector on the SGX wrapper is `U_WPM_SCA_CantedIronSights`, and the object's
`Field_e77336c8` is 2. That value appears only on the 60 canted-iron locals;
optic parts use 1 and unconditional sway effects use −1. Mini Scout Short 1.033862
and BROD 3 1.016938 have the same canted + ConditionalShort pairing. GGH-22's
0.850746 and BROD 3's 1.024638 pair with `U_WPM_IronSights`. Every weapon also has
an unconditional iron-sight local (1.05–1.22), which the 25 September recordings
do not show as a general ADS multiplier. The M4A1 iron/ROX ratios of 0.642 and
0.684 fit the shared ×0.667 package, not ×0.729, and BROD 3's 0.978 and 0.987 fit
1.0, not 1.076. The site's SGX CQB/Long and Mini Scout Short values therefore
likely apply only while aiming through canted irons. They were removed from the
site on 26 September (operator approval); the menu descriptions for CQB and the
Mini Scout 12" SBR mention no sway, while Long keeps its shared ×1.5.
[L94 receipt](../../reference-data/provenance/frosty-2026-09-26-L94-optic-accessory-and-local-sight-sway.json).

### Optic Accessory effects (L94, L96–L98, 26 September 2026)

Of the 355 SCA ability entries, the only GS bindings are `GCR_*` camera recoil,
which is unmodeled. The shared `WPM_SCA_*` parts import visuals, PiP zoom, lens
flare (AGCoating) and `WME_HighZoom_Magnifier_P00`. Inline `Class_104c2294` stores
16 on canted irons and the variable magnifiers, 0 on canted/offset red dots and 24
on the G43. Ordinary optics store 8–72 in the same field, so here it is an
unresolved optic setting, not an ADS tier step. The L94 WB inline optic sway
records (`e77336c8`=1) store 1. The separate shared Piggyback Reflex package
stores `Field_90fd0310=0.9990040064` with `e77336c8=-1`; this is not a verified
general sway reduction. Canted-iron sway locals (0.84–1.21 per weapon, `e77336c8`=2) are
associated with the canted-iron selector. This supports a sight-state
interpretation; native activation and selector composition remain unproved.
`Class_bfd4f199` stores three 1.1 values in 10 canted-red-dot records across five weapon bodies.
Its operation is unknown; the values do not establish a recoil multiplier.
This source pass establishes no additional numeric correction to the site's
primary-sight statistics.

The [L96–L98 receipt](../../reference-data/provenance/frosty-2026-09-26-L96-L98-optic-accessories.json)
closes the scoped non-AG source pass against Head 4892017. All 301 captured
attachment identities and costs match the 25 September L65-catalog-a/b rows
(`2026-09-25T1100-0400/1.4.3.0`). These are source
records, not proof that each choice is available in the current game.

| Source accessory family | Captured records | Point cost |
|---|---:|---:|
| Canted Iron Sights | 56 | 5 |
| Canted Reflex, including one separate MG5 slanted record | 56 | 10 |
| Piggyback Reflex (`OffsetRedDot`) | 56 | 10 |
| G43 Magnifier | 53 | 10 |
| Adjustable Magnification 2x / 3x / 4x | 12 each | 10 |
| SecondarySight empty choice | 44 | 0 |

The XML set adds KSG canted irons and Piggyback Reflex without captured raw
attachment files. Keep these two entries unverified. Some G43/variable labels
lack exact AAM joins; retain their source IDs without guessing names. The 257
compatibility rules use exact weapon and primary-optic identities. With the six
AGCoating rules they make up the 263 optic-accessory entries among the 285 in
`frosty-attachment-compatibility.json` ([DATA_GRAPH](DATA_GRAPH.md)). The site's
broad sight categories cannot express all these requirements.

Of the 44 SecondarySight entries, 43 have a resolved route to
`U_DPF_SecondarySight_Empty`. Ultimax's current ability branch confirms its
progression and secondary-sight choice, but not this empty-selector edge.
M27IAR has a separate missing join in the reused branch index. These gaps do
not establish an absent gameplay effect or an unavailable choice.

L97 covers 31 non-AG `WPM_SCA`/`U_WPM_SCA` packages plus G43. Five common
magnifier packages each contain a PiP effect and a separate
`WME_HighZoom_Magnifier_P00` import. Selector and effect arrays are preserved;
index correspondence alone does not prove pairing or simultaneous activation.
The HighZoom field stores −1, with its operation unresolved. No direct
`WME_DynamicPivot` reference occurs in this fixed package scope. The 25
September queue entry listing `WME_DynamicPivot` on canted irons recorded no
source route; the canted-sight WB sway locals carry Pivot components but are a
different class. Treat that earlier entry as unsupported; indirect WB/GS routes
are not disproved.

L98 records the four unnamed `Variable_Any` classes in five optic packages.
`Class_daaa7328.Field_1261cdf1` stores a 1.1 triplet in each. The selected GCR
targets use the named camera-recoil fields in the
[existing ladder](WEAPONS.md#camera-recoil-ladder); their values are not recoil
percentages. The canted-red-dot author label places its triplet in a secondary
optic firing-animation context, but does not name the operation. No numeric
site effect is established for these unnamed fields. An accessory model would
need exact optic compatibility and active sight state before these routes could
be applied. Research is paused after this source pass; native activation,
composition and unresolved field meanings remain open.

## Evidence

- [frosty-attachment-handling-generated.json](../../reference-data/provenance/frosty-attachment-handling-generated.json),
  [frosty-barrel-ads-generated.json](../../reference-data/provenance/frosty-barrel-ads-generated.json),
  [frosty-sniper-brakes-generated.json](../../reference-data/provenance/frosty-sniper-brakes-generated.json),
  [frosty-assumption-review.json](../../reference-data/provenance/frosty-assumption-review.json)
- [frosty-barrel-ads-2026-09-13.json](../../reference-data/provenance/frosty-barrel-ads-2026-09-13.json):
  WB and GS ADS routes (24 selections differ; the site follows WB)
- [frosty-handling-mapping-followup.json](../../reference-data/provenance/frosty-handling-mapping-followup.json),
  [frosty-other-attachment-review-2026-09-13.json](../../reference-data/provenance/frosty-other-attachment-review-2026-09-13.json)
- [belt-box-moving-ads-2026-09-13.json](../../reference-data/provenance/belt-box-moving-ads-2026-09-13.json)
- [frosty-light-field-names-2026-09-13.json](../../reference-data/provenance/frosty-light-field-names-2026-09-13.json)
- History: [attachment generation review](../archive/FROSTY_ATTACHMENT_GENERATION_2026-09-13.md),
  [optic source plan](../archive/OPTIC_FROSTY_SOURCE_PLAN.md)

## Weapon Attributes attachment tracing (21 September 2026)

The source review covers saved builds 1.4.2.5 and 1.4.3.0. See the
[Weapon Attributes model](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/WEAPON_ATTRIBUTES_MODEL.md) for calculations and limits.

- **Tungsten Core:** M2010 ESR, PSR and SV-98 select
  `GRM_Recoil_AMO_Bolt_M10` (−6 ADS/hip recoil amount steps). L115 and Interdictor
  select normal `GRM_Recoil_AMO_M10` (−1). Mini Scout binds both (−7).
  Variation does not change. Production follows these bindings; six steps as the
  intended rule for all snipers remains a hypothesis.
- **L115 Standard Suppressor:** the normal suppressor selector is active, but its
  GS has no corresponding hip-dispersion penalty binding. EF88 and M2010 ESR have
  that binding. The research Hipfire checker excludes the penalty; the generic
  production muzzle penalty remains a separate open correction (bug 12).
- **L115 QD Grip Pod:** no moving-ADS penalty binding. Production uses zero.
  Light + Violet reads Mobility 54; adding the pod reads 58.
- **18.5KS-K Slim Angled:** selects normal `U_WPM_BTM_Fast02_W25`, unlike the
  affected sniper grips that select Full Angled. Its extra
  `GDM_Array_ADSMoveDispersion_BTM_M10` binding is under `Field_b30a73ed`, not
  moving-ADS collection `Field_2ffeb6ac`. A modifier filename alone does not identify
  the runtime target. Twelve ADS indicator captures show Slim Angled matching no
  grip within one pixel, with and without Violet; Folding Stubby widens the moving
  indicator. Production now uses zero moving-ADS penalty. The other field's exact
  effect remains unknown; indicator widths do not establish pellet distribution.
- **VSSM:** both 200 mm Factory (30 points) and 200 mm ASM (20 points) have integrated
  suppression. The paired Folding Stock captures use ASM, with no separate suppressor.

Evidence: [Tungsten trace](../../reference-data/provenance/sniper-tungsten-recoil-2026-09-21.json),
[Mobility trace](../../reference-data/provenance/composite-mobility-source-trace-2026-09-21.json),
[ADS indicator measurements](../../reference-data/provenance/ks18k-ads-indicator-2026-09-21.json),
[paired panels](../../reference-data/provenance/composite-combination-results-2026-09-21.json).
Dated trace files preserve the status at collection time; the indicator follow-up
supersedes the earlier pending KS18K production status.

## Burst recoil duration overrides (L13, 24 September 2026)

The current file has five `ERGOS.weaponOverrides` recoil leaves, not the earlier
19-row starting count. All five store `recoilDurationAdd: -0.0006`: Burst Training
on SG553R, PW5A3 and CZ3A1; Burst Mode on SL9 and GRT-BC. Their GS records bind
`GRM_AutoIdentifier_P00` to `U_WPM_ERG_BurstFireActive`
(`588728fd-2ae7-4424-aa22-45d9b3c82ba0`). The shared modifier adds -0.0006 to
registry-named `RecoilDuration` for both aim states; all five bases are 0.025.

This supports the existing operands. The source model predicts 0.0244 when the
condition applies, before other modifiers. MP5 raw checks locate base floats at
1024/1176 and modifier additive floats at 1100/572. The GS selector and effect
pointer were also checked against raw bytes; the other four GS bindings were
independently decoded. [Receipt and reproduction](../../reference-data/provenance/frosty-2026-09-24-L13-burst-duration-bindings.json).

The Ability action selects `BurstFireEnabled`; the GS condition is the separate
`BurstFireActive` token. Native production of that token, firing activation and
composition remain unresolved. Keep the existing rank-9 capture requirement;
the 0.0006 duration delta alone is too small to identify reliably in normal video.
No numeric site change is proposed.

## Local non-sway parts (L6, 24 September 2026)

The `Class_45930daa` local-part family uses optic/iron-sight selectors. Its
three small floats must not be treated as recoil or spread multipliers. A direct
RPK74M trace resolves the registry author path `Tango Weapon Offset` /
`Weapon Offset for Optics`; this supports a weapon/optic placement role.
For Tango6T, the raw values at bytes 5216/5220/5224 are 0, -0.0175 and 0.02.
Individual component names, units and runtime behavior remain unknown.

EF88's instance has null registry references, but that did not exhaust the
family: RPK74M's non-null references supply this independent purpose clue.
No combat-stat change is proposed. [Reviewed trace](../../reference-data/provenance/frosty-2026-09-24-L6-local-optic-offset-scope.json).

The broader local-part inventory remains a source of bounded leads. Bipod flags
alone do not establish a recoil effect. M18's local MagazineCapacity 22 versus
the site's nominal 21-round magazine repeats the known chamber/nominal question.
The separate M250 numeric bipod part is recorded below as L16.

### M250 local bipod scalars (L16, 24 September 2026)

The [reviewed local part](../../reference-data/provenance/frosty-2026-09-24-L16-local-bipod-unmapped.json)
selects `Class_8b80c794` under `U_M250_Bipod`. Fields `e11a863e` and
`f9477ebd` are 1.0375; `6a647926` is 1.0. Their targets and operations remain
unknown. Two hotfix vehicle instances have the same checked class/inherited
descriptor layout and neutral operands. Their Stinger owner context does not
identify the effect. Keep release and hotfix records separate. No recoil, sway
or other numeric site change is supported; reopen with a typed consumer or
independently named target. Decoder layout ambiguity and runtime limits remain.

### Buffer animation-context limit (L18, 24 September 2026)

The [same-class registry trace](../../reference-data/provenance/frosty-2026-09-24-L18-buffer-animation-context.json)
finds author paths for secondary-optic proc-firing animation settings. The HTI
canted-optic example stores a 1.1 vector where Buffer stores 0.75. However, the
exact registry member arrays name only Priority. They do not name this vector
or its operation. Buffer has null anchors in both relevant objects. This is a
purpose clue, not proof of a 25% recoil reduction. Retain the qualitative site
badge; no numeric change is supported without a typed field or consumer.

### Match Trigger indirect effects (L17, 24 September 2026)

The [raw HK433 trace](../../reference-data/provenance/frosty-2026-09-24-L17-match-trigger-indirect-effects.json)
follows the attachment selector through a local WB target to embedded identifier
`15cff9ff-aab0-4230-9a53-5a2bb1606587`. The same identifier selects two GS effects:
`GBM_NoIncrease_ERG_P00` multiplies IncreasePerShot by zero in all four aim/stance
branches; `GRM_MatchTrigger_ERG_P15` adds 3 to RecoilAmountMultiplierExponent and
stores a 1.728 second-multiply operand on RecoilDecreaseFactor in both aim states.
Exact GRX child/hash pairs name all three targets.

This provides a source path beyond the site noEffect marker. It does not prove
native activation or composition. The description specifies semi-auto, but that
text is not a consumer. The three sibling WB identifiers relate to bipod/mounted
contexts and do not prove a fire-mode condition. Capture M433 with and without
Match Trigger in manually selected semi-auto and automatic control. A candidate
model gives recoil ratio 0.945^3 = 0.843908625, recovery factor 72*1.728 = 124.416
and no added per-shot bloom; minimum spread remains. These are conditional model
predictions, not runtime measurements. No cadence change or game bug is established.

The 25 September capture shows no hip bloom on M433 in semi with or without Match
Trigger. The bare semi baseline already lacks bloom (the L63 semi condition), so the
zero-increase operand cannot be isolated; recoil and recovery remain untested
([capture receipt](../../reference-data/provenance/frosty-2026-09-25-L63-L17-semi-bloom-captures.json)).

The 26 September existing-clip pilot verifies the paired video hashes and near-60 Hz
post-stall timing. The Trigger clip has three post-stall shots, but only two valid
steady event/baseline pairs because the first baseline crosses the recorder stall.
Static-background tracking measures camera/view motion, not isolated weapon recoil.
Without an input trace, established cross-clip framing, known FOV, and evidence for
the live capture build, these clips cannot test the conditional L17 recoil ratio.
This is a capture-sufficiency limit, not a negative finding about Match Trigger;
the L17 prediction remains open. The reticle-gap control differs by one pixel
between direct empty-pixel and prior inner-edge conventions; it is not recoil. See
the [L70 capture-limit receipt](../../reference-data/provenance/frosty-2026-09-26-L70-match-trigger-capture-limit.json).
Source release evidence and the unverified live capture build remain separate.

The [L24 family check](../../reference-data/provenance/frosty-2026-09-24-L24-match-trigger-family.json)
confirms the same exact GBM and GRM targets for all 24 current Match Trigger
selections. The parent fresh-decoded each WB and GS and checked the selector
array, local references, embedded identifier and both GS imports. Source priority
values differ between weapons. Shared targets extend source coverage; they do
not establish universal activation, stacking or a single final multiplier.
Keep the L17 capture requirement and each weapon's base values.

### Compact Handstop utility candidate (L27, 24 September 2026)

The [current CZ3A1 trace](../../reference-data/provenance/frosty-2026-09-24-L27-handstop-boolean-scope.json)
follows the exact progression, Ability action and selector into the shared
Handstop WPM imported by the WB. Its `Class_a00773e3/Field_18774676` is true at
raw offset 216; the same field is false in the base WB at offset 4676. No typed
name or native consumer is established. A different local Burst Mode selector
in the same WB must not be attributed to Handstop.

The mapped description says the attachment permits firing while sprinting.
That is a capture hypothesis, not proof of this field's name. Keep numeric tiers
unchanged. If a controlled capture confirms the utility, consider a utility
indication instead of interpreting the site's noEffect flag as no gameplay effect.

The [L30 owner-registry follow-up](../../reference-data/provenance/frosty-2026-09-24-L30-handstop-registry-scope.json)
checked both non-null registry anchors on that WB owner and their direct linked
groups. They provide no child/hash pair for `18774676`. The boolean remains
unnamed; this negative result does not show that it is unused.

### Indirect fire-mode condition candidate (L31, 24 September 2026)

The [bounded source check](../../reference-data/provenance/frosty-2026-09-24-L31-fire-mode-mask-candidate.json)
confirms Match Trigger value 1 and Burst value 8 in `Class_9dfbb158.Field_1c85cbb1`.
The class adds one uint32 above a GUID-only base. SDK member lists for
`FireModeSpecificModifierUnlock.FireLogicTypesMask` and
`ContextSpecificModifierUnlock.UnlockAssetGuid` fit that structure. Values 1 and 8
also fit bit masks for the SDK single-fire and burst enum positions. These are
independent structural clues, not an exact field-name mapping or native bit test.

The selected VSSM Full Auto WB and WPM contain no instance of this class. Its GS
instead binds the Full Auto selector directly. This control provides no value 4;
it rules out a universal record layout across these three selected paths, not the
candidate mask meaning. Keep the L17 semi/auto capture and existing Burst runtime
limits. No new numeric site change follows from this result.

### A3 Receiver and burst recoil tiers (L59, 24 September 2026)

All 34 site recoil tier values for A3 Receiver and the three burst choices now
have exact source operands ([receipt](../../reference-data/provenance/frosty-2026-09-24-L59-ergo-recoil-tiers.json)).
A site tier value equals an additive operand on `RecoilAmountMultiplierExponent`
or `RecoilDirectionVariationMultiplierExponent`, same sign.

- **A3 Receiver (M16A4):** `GRM_Recoil_ERG_M10` adds −1 to the amount exponent in
  both aim states, matching the site's −1.
- **Burst Training, Burst Mode and GRT-BC Burst Mode:** the effects are bound in
  each GS under the `BurstFireActive` condition token, not the attachment selector
  (as for L13's duration add). `GRM_RecoilConversion_ERG_P10` adds +3 to the
  variation exponent (site +3 on all eight weapons) and −1 to the amount exponent.
  A second effect adds +1 (`GRM_Recoil_ERG_P10`, seven weapons) or +2
  (`GRM_Recoil_ERG_P20`, GRT-BC) to the amount exponent. The sums, 0 and +1,
  equal the site amount tiers.

The site values match only if the game adds these operands; activation and
composition remain unresolved. No numeric change.

### Reverse coverage of recoil and spread effects (L60–L61, 24 September 2026)

L60 listed every recoil, bloom and dispersion effect that a site choice selects
in source and checked whether the site models it
([receipt](../../reference-data/provenance/frosty-2026-09-24-L60-reverse-coverage.json)).
In ERGOS, GRIPS, MUZZLES, LASERS and magazines, every effect is modeled or
already known (Match Trigger, the PP-19 and L115 bugs), except one. Site laser
and grip spread steps sit in per-weapon `frostyModifiers` with the source sign
negated.

The 25 September sweep of sights, barrels, lights and ammo found no new effect
([receipt](../../reference-data/provenance/frosty-2026-09-25-L60-reverse-coverage-remaining.json)).
Sights bind only `GCR_*` camera recoil. Barrel, light and ammo operands all match
the site, apart from ADS idle-recovery offsets (idle state is not modeled). The
Mini Scout penetration −7 is the sum of `GRM_Recoil_AMO_M10` −1 and
`GRM_Recoil_AMO_Bolt_M10` −6. `GS_MiniFix` binds each light selector to two
identical hip modifiers (`GBM_Increase_Hip_S1` and `_A40`). A screen of all GS
files finds same-family double bindings only there. The penetration pair stacks
in game ([bug 13](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/ATTACHMENT_BUGS.md#13-sniper-tungsten-core-recoil-penalties-are-inconsistent)),
so the light pair probably does too, giving 0.444 rather than 0.667. No displayed
value changes: the bloom recovers in about 0.07 s against a 1.27 s shot interval,
and the panel Hipfire factor does not depend on the size of the change.

The exception is the +2 hip dispersion step bound by bipods and grip pods
(`GDM_Array_HipDispersion_BTM_P20`, 142 weapon/choice pairs), which the site
omits. L61 ([receipt](../../reference-data/provenance/frosty-2026-09-24-L61-bipod-hip-dispersion.json))
found it identical to the `_NoBipod` copy that Canted Vertical binds, except one
boolean, `Field_b574fa40` (true on P20). Current EF88 panels show lasers raising
Hipfire from 40 to 47/54/62, while bipod and all grip pods stay at 40. The flagged
step therefore does not apply when the attachment is fitted; it most likely
requires a bipod or deployed state. The site omission matches the panel. Deployed
behavior stays with parked question W1.

### Reverse coverage of handling, velocity and sway (L62, 25 September 2026)

L62 repeated L60 for WME imports and `GID_*` bindings: ADS time, draw/deploy,
sprint recovery, ADS move speed, reload, sway and muzzle velocity
([receipt](../../reference-data/provenance/frosty-2026-09-25-L62-reverse-coverage-handling.json)).
Grips, muzzles, barrels, ergos, magazines and ammo agree with the site throughout.
ADS time keeps the source sign on grips and barrels and is negated on magazines;
draw, sprint and ADS-move shifts are negated everywhere. The only barrel exceptions
are GS-only `GID_ADSTime_BRL` +1 bindings on EF88 Extended, BROD3 Extended and the
VSSM barrels, where the site follows the WB (0). EF88 panels read Mobility 52 for
Basic and 48 for Extended, matching the WB-only index, which supports W2.

Sights carry category-wide effects the site omits. Every var_high and thermal optic
on all 56 weapons imports `WME_ADSMoveSpeed_M05` (one ADS-move tier slower; AK205
0.67 → 0.60, Mobility −2). Every iron sight except BROD3 and the six bolt-action
rifles imports `WPM_Sway_IronSights_P05` (weapon and camera sway ×0.666667). Iron
is the site's default sight, so any optic would show +50% weapon sway. The site's
reason for leaving out optic effects, that a category cannot identify one optic,
does not apply to these uniform effects. Both were applied on 25 September and
confirmed in game the same day: M4A1 menu captures show ADS move 0.82 → 0.75 with
Variable High/Thermal, and M4A1 recordings show reduced iron-sight sway (ratio 0.67)
([captures](../../reference-data/provenance/sight-sway-ads-move-captures-2026-09-25.json)).
BROD 3's missing iron-sight package is bug 16.
The BREN3 `AAM_BREN3` lists one primary `Iron Sights` attachment and a separate
`CantedIronSights` optic accessory. The WSE0231 skin has regular and folded iron-sight
art assets alongside a handguard variant, but no second primary iron-sight attachment
or handguard-specific sway selector appears in the 1.4.3.0 source trace. These model
variants do not change the site's BROD 3 sight effect.

### Selected barrel damage-family check (L68C, 26 September 2026)

The [L68C receipt](../../reference-data/provenance/frosty-2026-09-26-L68C-selected-barrel-damage-families.json)
checks selected Interdictor basic, extended and light barrels, and VSSM regular
and ASM barrels. Nine reused controls pass. The selected-chain check covers 30
captures and 14 selected WPM effect references; all 124 assertions pass. Neither
the tested `Class_b1afeb65/Field_808dd66c` projectile-replacement family nor
`Class_e85fff64/Field_fbfacac9` protection-index family appears in those checked
paths. This is bounded to two families and five choices; it does not rule out
other damage mechanisms or establish runtime activation. Broader L68A/B route
reviews remain partial. Existing barrel handling, recoil and sway were not
re-audited, and no site change is proposed.

### Non-ammo damage, fire-rate and velocity effects (L93, 26 September 2026)

The [L93 receipt](../../reference-data/provenance/frosty-2026-09-26-L93-non-ammo-damage-effect-screen.json)
screens the whole weapon catalog rather than L68's four weapons. The shared
`HeadShotDamage` (protection), `Penetration` and subsonic `MuzzleVelocity`
effects are selected only by `_Ammo` parts. Barrel `WME_MuzzleVelocity_P05`/`M05`
(1.25/0.8) match the site's barrel `velMult`. The 33 inline projectile-replacement
and protection-index objects in 20 weapon bodies all sit on single-player owner
selectors (`7672760d` Player, `6d45cd64` Enemy, `e67ab0f5` Squad) that swap in
`PD_SP_*` bullets, so they are out of scope.

The one non-ammo, non-velocity hit is the P90 Heavy Recoil Spring
(`WME_Firerate900_M10`: RateOfFire 800, single 400). It does have an ability
branch: `P90_Ability` SC_Ergonomic entry → `U_PRG_P90_Improved_Recoil_Spring_Base_900`
→ `U_WPM_ERG_HeavyRecoilSpring900_W10`. That corrects the 13 September note,
which said it had none. No `Attachment_P90_ERG_*` asset or English string
references it, and the 7 September menu shows 900 RPM for every USG-90 ergo
choice (None, Improved Mag Catch, Aftermarket Buffer). Keep the site's 899.999
RPM and ergo list. The operator treats it as a probable in-development
attachment whose values may change before any release; do not pursue it
unless it appears in a live menu. No non-ammo attachment selects an unmodeled multiplayer
damage, penetration, fire-rate or velocity effect.

### M4A1 M320 HE/AT serialized source profile (L71, 26 September 2026)

The [L71 receipt](../../reference-data/provenance/frosty-2026-09-26-L71-m320-he-at-source-profile.json)
records ordinary M4A1 HE and AT selector paths. The HE projectile stores
`InitialSpeed=250` and `TimeToLive=15`. L71B joins projectile object 1 to its
serialized Explosion object 7 (`Class_9966532d`), with `BlastDamage=120` and
`DamageMultiplier=1`; its layout remains ambiguous. L71C finds seven common
effect-class signatures and two AT-only classes, including a sound reference
and unnamed fields. This is source structure only: it does not establish
effective launch speed, HE/AT damage equivalence, native precedence or runtime
behavior. The separate [L75 receipt](../../reference-data/provenance/frosty-2026-09-26-L75-m320-explosion-naming-limit.json)
records the bounded field-naming result below.

### M320 HE Explosion field-naming limit (L75, 26 September 2026)

The `BlastDamage` hash/value control reproduces on the actual M320 owner. In
the pinned `GRX_Gadgets_Glacier` capture, two other hashes have 24 exact name
pairs each (`BlastRadius` and `ShockwaveRadius`), all on non-M320 anchors. No
paired owner body matches the pinned Head and descriptor, so L75 does not
independently transfer either name to M320. Those two mappings already appear in
`FIELD_MAP.md`; L75 did not discover them. The third tested hash has no pair in
this registry and remains unnamed. No units, falloff relationship, runtime
effect or site value is established.

### M4A1 M320 HE firing inputs and capture feasibility (L76/L76B, 26 September 2026)

The [L76 receipt](../../reference-data/provenance/frosty-2026-09-26-L76-m320-he-firing-inputs.json)
records the selected ordinary M4A1 firing record's `Shot.InitialSpeed` as
`[0, 0, 63]`; its object and FireLogic layouts remain ambiguous. The primary
M4A1 control names `Shot.InitialSpeed.z` at 590, matching the current site
bullet velocity. The stored projectile value 250 and TTL 15 are separate. The
FireLogic value 0 is labelled single only by `FIELD_MAP`; stored rates are
100/550/-1. One reload row and three phase values are recorded, but reload
activation, cadence, launch precedence and phase composition remain unresolved.

The [L76B receipt](../../reference-data/provenance/frosty-2026-09-26-L76B-m320-he-capture-feasibility.json)
contains arithmetic only. If 63 and 250 are treated as m/s under its explicit
stationary, no-drag, 60 fps and ±2-frame transit-duration assumptions, the 20 m
intervals do not overlap; the minimum gap is 10.229 frames with the 0–5°
launch-angle sensitivity included. Capture endpoint errors must be measured and
bounded to support that duration uncertainty. This does not identify the active
native speed, establish units, or promise that the launch and collision events
are observable in a live capture.

### M4A1 M320 thermobaric Explosion fields (L78, 26 September 2026)

The [L78 receipt](../../reference-data/provenance/frosty-2026-09-26-L78-m320tb-explosion-profile.json)
records the ordinary M4A1 selector-to-`WPM_UBL_M320TB` route and its selected
projectile's `Class_9966532d` Explosion owner. Direct registry associations name
local `BlastDamage=30` (registry value 50) and `DamageMultiplier=1` (registry
value 1). The M4A1 HE control reproduces at 120/1. The part-to-effect hop is a
decoded-path assertion without raw pointer bytes in the reused receipt. These
serialized values do not establish precedence, runtime activation, total damage,
or blast/burn behavior; no site value change is proposed.
The [L79 receipt](../../reference-data/provenance/frosty-2026-09-26-L79-m320-explosion-name-limits.json)
records the passing HE `BlastDamage=120` control and zero pairs for
`Field_0df20cb3` and `Field_920ff0be` in one pinned `GRX_Gadgets` scan (1,618
anchors, 5,726 entries). The ambiguous TB Explosion owner has raw pointers to
`Class_afbfd124` and `Class_920ff0be`; names, curve units, equations and runtime behavior remain unresolved.

### M320 HE/TB ShockwaveDamage local fields (L85, 26 September 2026)

The [L85 receipt](../../reference-data/provenance/frosty-2026-09-26-L85-m320-shockwave-input.json) records existing FIELD_MAP.md member `Field_3ef01f58` as FLOAT32 `1.0` on the selected HE and TB Explosion owners, raw-checked at offsets 1776 and 1824 as `0000803f`. The name already maps to `ShockwaveDamage` on `Class_9966532d`; it is not a new same-owner name association. Each exact GRX_Gadgets owner anchor has seven child/hash pairs and no pair for this hash. Both layouts remain ambiguous. This bounded local result supplies no global name-absence claim, directly paired registry value, extra-damage/addition equation, precedence, activation, composition, or native behavior; the prior TB part/effect hop has no independent raw-pointer check. No current primary defect, numeric site change, or capture is proposed.

### M4A1 M26/M320 HE secondary spread roots and Shot inputs (L86/L87, 26 September 2026)

The [L86/L87 receipt](../../reference-data/provenance/frosty-2026-09-26-L86-L87-secondary-spread-protection.json) records exact direct-index links from M4A1 GS to the pinned HDA_Weapons and ZDA_Moving_Weapons roots. The captured index contains 63 caller files and 126 direct sites; caller bodies were not expanded. Raw checks show both selected secondary GS owners have null words at both root fields, and the exact incoming index has no direct rows for either owner. This does not establish native nonuse, fallback, effective association or precedence.

The same receipt records the named DP12 Shot index control and matching root/Shot descriptor identities for the selected M26DB and M320 HE owners. Their signed INT32 values are 0 and -1 at offsets 1168 and 592. The inspected direct Shot registry references are null; no target-local Shot name anchor was established. The control name transfers by exact descriptor identity, but no target-local name, table mapping, numeric meaning or runtime behavior is claimed. No site change follows.

### Ordinary M26DB and M320 HE configured ammunition counts (L88, 26 September 2026)

The [L88 receipt](../../reference-data/provenance/frosty-2026-09-26-L88-m26-m320-configured-ammo-counts.json) records the DP12_WB known-answer control and matching root/Ammo descriptor identities for the ordinary selected M26DB and M320 HE owners. The configured counts are M26DB capacity 5 and magazines 2; M320 HE capacity 1 and magazines 2. Names use the accepted L37 control/field basis; cached decodes agree with the raw words, while both nested Ammo layouts remain ambiguous.

These serialized values are possible inputs for an optional secondary display profile only. The Analyzer has no secondary selector. Runtime activation, composition, native magazine behavior, loaded/chamber/reserve totals, and primary-count behavior remain unestablished. No site change follows.

### M4A1 ordinary M26DB secondary source profile (L73, 26 September 2026)

The [L73 receipt](../../reference-data/provenance/frosty-2026-09-26-L73-m26db-source-profile.json)
records the ordinary M4A1 `WPM_UBL_M26DB` internal M26 buckshot base and
Dragon's Breath replacement-projectile paths. These are profiles inside the
package, not necessarily separate menu choices. Both exact projectile owners
have four matching FLOAT32 hashes. The M4A1 owner control associates them with
`StartDamage`, `EndDamage`, `DamageFalloffStartDistance` and
`DamageFalloffEndDistance`. Their stored values, in that order, are 8.4, 2, 6
and 25 on the base profile, and 5, 2.5, 5 and 15 on Dragon's Breath. Both
curve pointers are raw-null.

The previous null child GUIDs on the M4A1 registry control were a reporting
omission. The [L73 child GUID correction](../../reference-data/provenance/frosty-2026-09-26-L73-registry-child-guid-reporting-correction.json)
records the four exported GUIDs; the supported names and values are unchanged.

These source names and values do not establish native scalar fallback or curve
precedence. No distance units are established. The [L73D receipt](../../reference-data/provenance/frosty-2026-09-26-L73D-ecr-m26-incendiary-naming-limit.json)
bounds three ECR_M26Incendiary hashes to one pinned `GRX_Gadgets` route; none has
a pair there after the positive `BlastDamage=120` control. This does not establish
global name absence or field meaning. No direct hit operation, burn behavior,
duration, tick rate or site change is established. Keep the M26 profiles separate
from M4A1 rifle-primary damage.

The [L77/L77B timing receipt](../../reference-data/provenance/frosty-2026-09-26-L77-m26db-secondary-timing.json) records two prior-name-basis fire-logic rate fields at 1799.999 RPM and a conditional 88.078 RPM result from applying the existing full-cycle formula to the exact matched nested bolt descriptor. Its one reload-info row has prior-name-basis `ReloadSpeed=1` and `ReloadTimeBulletsLeft=3`; this bounded result assigns no names to the other row members and does not establish native mode, completion, ADS overlap, reload selection, or a separate runtime profile.

### M4A1 M26DB secondary trajectory inputs (L80, 26 September 2026)

The [L80 receipt](../../reference-data/provenance/frosty-2026-09-26-L80-m26db-trajectory-inputs.json) records the selected inline `WPM_UBL_M26DB` `Shot.InitialSpeed=[0,0,400]` vector and two internal projectile profiles, each with `InitialSpeed=350`, `Gravity=-9.8100004196167` and `Drag=0`. Their `TimeToLive` values are 0.5 for M26Mass and 0.10000000149011612 for Dragonbreath. The inline firing vector and projectile speeds are separate serialized inputs; the two profiles are not asserted to be separate menu choices. Both projectile layouts and the firing-object layout remain ambiguous. Native activation, effective launch-speed composition, units, trajectory, range and expiry remain unresolved. This is optional secondary trajectory evidence only; no primary correction, numeric implementation or capture is proposed.

### M4A1 M26/M320 HE selected secondary recoil inputs (L81, 26 September 2026)

The [L81 receipt](../../reference-data/provenance/frosty-2026-09-26-L81-secondary-recoil-inputs.json) records raw-checked hip/ADS recoil inputs for the ordinary selected M26DB and M320 HE GunSway owners. Their exact root and nested descriptors match the M4A1 control; the seven field names follow prior `FIELD_MAP/source-recoil` evidence. M26 amount/direction/variation are 3/-10/12 for both aims. M320 HE stores amount 5 hip and 2 ADS, with direction and variation zero; multipliers are 1 and exponents are 0. Both target decoder `layoutAmbiguous` flags remain. Saved WPM imports resolve to the exact object GUIDs, but their pointer bytes were not checked. These are possible optional secondary inputs only: units, native activation/composition and final recoil remain unresolved. The rifle-primary model is not shown wrong; no numeric implementation or capture is proposed.

### M4A1 M26/M320 HE selected secondary spread inputs (L82/L84, 26 September 2026)

The [L82/L84 receipt](../../reference-data/provenance/frosty-2026-09-26-L82-L84-secondary-spread-inputs.json) records UINT32 zero in both selected GS HDA and moving-ZDA selectors. The common-table candidate association gives HDA row 0 candidates 7.400000095 (hip standing) and 9.25 (hip moving), and moving-ZDA row 0 candidate 0.680000007 (ADS moving). Stationary hip/ADS IncreasePerShot is 1.0/1.0 for M26DB and 0.5/0.5 for M320 HE. Local MinAngle/MaxAngle pairs in rows 0/1/9/10 are M26DB 1.5/1.5, 2/2, 0.5/0.5, 1.2/1.2; M320 HE 1/7, 1.5/7, 0.1/0.3, 0.3/0.7. The common-table candidates and local arrays are separate optional secondary inputs. The common HDA hip-minimum candidate 7.400000095 exceeds the local hip MaxAngle 1.5 for M26DB and 7 for M320 HE. This conflict does not establish precedence or effective spread. No direct GS-to-table import, native consumer, activation, composition or effective range is established. The selected WPM imports retain rawPointerByteCheck=false and both target layouts remain ambiguous. The optional-feature classification comes from the Astra code review; no primary-weapon defect or numeric site change is proposed.

The [L83 receipt](../../reference-data/provenance/frosty-2026-09-26-L83-secondary-recoil-recovery.json) records zero `RecoilDuration` in both aims for the selected M26 and M320 HE owners. M26 factor/exponent/time-exponent/offset are 70/0.6/3/0.001; M320 HE values are 3.6/0.8/2/0.001. Names use the prior `FIELD_MAP`/L13 basis and exact L81 descriptor match. Zero duration does not establish an instantaneous impulse, disablement, inheritance, fallback, or native timing; these remain optional secondary source inputs only.

### Legacy parts in KORD 6P67 and M250 blueprints (L64, 25 September 2026)

The WB part lists of these two weapons, and no others, import
`Game/KingstonLegacy/Mica` attachment parts
([receipt](../../reference-data/provenance/frosty-2026-09-25-L64-legacy-wb-parts.json)).
`WM_Foregrip` is keyed to the current Classic Vertical selector and holds 0.85/0.85
and 1.15/1.15 in `Class_d209d775` and `Class_be3e57cd`. `WM_Bipod` holds 0.75/1.25
under a key no current choice uses; the other legacy parts are empty. Neither class
occurs in any current asset, and the registry names none of their fields. No effect
or site change follows; reopen only with a consumer for either class.


The [L41 raw check](../../reference-data/provenance/frosty-2026-09-24-L41-vssm-selected-operands.json)
resolves the Full Auto selector to its GBM/GRM objects and matches ten dispersion,
two recoil-variation and four recovery operands to the existing Folding Stock
values. Recovery factor 76 and exponent 1.24 are enabled in both aim states.
Native evaluation and timing remain unresolved, so the existing assumption note
stays valid; the GRM layout warning is retained. No new capture is proposed.

## Current ammo modifier and point audit (1 October 2026)

This audit uses **1.4.3.5 / Head 4909002**, descriptor `4c28ad65...`, and
register assumption A01. Earlier identities retain their original Head and carry
forward by equal raw hashes. L589-L590 completed current typed raw selection
joins for all 328 choices: Attachment/progression, root-listed Ability branch and
action, exact selector GUID, WB modifier/effect lists, and GS condition/binding.
The controls passed before extraction. One missing M45A1 Blacklight import was
captured by the shared safe-capture script; the build manifest verification passed.

- [Recoil/spread, L589-L590](../../reference-data/provenance/frosty-2026-10-01-site-audit-ammo-recoil-spread.json): 186 selected operand comparisons match. 74 stored leaves were compared. Complete bounded graph checks also compare absent named owners with site consumer defaults. Source shotgun hip step +9 maps to site -9. Recoil amount and direction-variation exponent fields remain distinct. Slugs ADS spread increment 0.05 has no qualified source receiver/control; no lead.
- [Type modifiers](../../reference-data/provenance/frosty-2026-10-01-site-audit-ammo-type-modifiers.json): 120 selected operand comparisons are exact and 31 are float32 precision only, counted under L107 without a proposal. All offered Frangible and Flechette regeneration additions, Lightweight movement shifts, and Subsonic spotting factors now have complete selected joins. World and minimap factors are compared as products of separate selected operands.
- [Points and identities, L586-L587](../../reference-data/provenance/frosty-2026-09-30-site-audit-ammo-points-availability.json): all 328 point costs match exact current uint32 reads. The descriptor decoder's `layoutAmbiguous` flag is retained. Game menu availability and default selection have no qualified source route/control; no lead.
- [Per-class collateral tables](../../reference-data/provenance/frosty-2026-09-30-site-audit-ammo-class-tables.json): all 77 fallback leaves are inactive for the 328 current selections, which use per-weapon overrides. Native fallback origin is not established; no lead.

All 328 choices have complete bounded selected graphs. 137 choices contain
no named recoil/spread, ADS movement, regeneration-delay or spotting owner in
that graph. This establishes configured absence only. It does not establish
native runtime zero, activation, global default conditions or composition.
Sniper Tungsten exceptions and sidearm Subsonic omission retain
ATTACHMENT_BUGS.md entries 13 and 5. The older 30 September receipts remain frozen;
the two new family receipts supersede their partial modifier coverage.
No new non-precision value mismatch was found. No Analyzer change is proposed.

## Patch-note coverage questions (1 October 2026)

[Coverage receipt](../../reference-data/provenance/frosty-2026-10-01-patch-notes-coverage.json). L743 separates attachment weight from cost, sway and ADS handling. EA announces a weight exchange/corrected descriptions without numeric operands; existing L115 choice identities and 25/30-point costs do not establish weight. L744 asks for exact functional-package fitted selections and remaining budget; predict 100 minus summed selected costs when the exact package chain is joined. Both remain source questions, not applied Analyzer changes.

All 153 official sources were read; the final coverage files preserve item-level mappings and release state. Only current released questions were ranked. No new recording, native execution claim or site edit.

<!-- L901-attachment-ui:start -->
## Player-facing attachment, ammo and optic text (L901)

[L901](../../reference-data/provenance/frosty-2026-10-01-L901-attachment-ui-census.json) retains current text and exact local pointer/import evidence for all 1,003 UI AD assets. Fifty-seven missing IDs remain visible. The 233 nonempty metadata arrays are retained with target objects and raw checks, but their effect/pro-con roles are not inferred from field names. A metadata statement or image link does not establish the selected gameplay modifier. Exact selection joins continue in L903; existing reviewed bug behavior remains unchanged.
<!-- L901-attachment-ui:end -->

<!-- L903-selection-edges:start -->
## UI selection identity limit (L903)

[L903](../../reference-data/provenance/frosty-2026-10-01-L903-ui-selection-edges.json) verifies 5,303 AAM-to-AD edges across path-corresponding candidates for 63 weapons. It does not prove the native scalar-key/property receiver from the selected attachment to those records. Exact text pointers and imports establish description storage, while old name-based joins remain candidate context. No negative native-effect conclusion follows from the direct-root check.
<!-- L903-selection-edges:end -->

<!-- native-semantics:L1003:start -->
## Current resource reader controls (L1003)

Two current Emitter bodies, one AtlasTexture body and one MeshSet body pass identity, size and Head controls. Eight fresh reads cover body prefixes and exact derived copies of captured metadata. The metadata files are not resource body headers. Emitter size minus metadata first word is 28 in both samples; the sole MeshSet sample gives 64. Atlas metadata version 3 and body size 92 agree with the retained source path. These are structural controls and correlations. No independently confirmed current semantic input/output control or held-out body validates these grammars. No resource reader or atlas meaning is promoted.

Evidence: [receipt](../../reference-data/provenance/frosty-2026-10-01-L1003-resource-grammar-qualification.json). Known-answer source controls and parent raw re-reads pass. Native semantics remain separate from serialized facts.
<!-- native-semantics:L1003:end -->

<!-- L906-statement-comparisons:start -->
## Player-facing quantities and intended effects (L906)

[L906](../../reference-data/provenance/frosty-2026-10-01-L906-attachment-ui-statements.json) changes method from graph expansion to exact localization-ID references and established source domains. It retains all 2,317 AD text occurrences and classifies 415 numerical tokens across 396 occurrences and 107 IDs. Thirteen tokens match exact site tooltip text references; 402 remain unmapped to a qualified source/site quantity. No source conflict or source-only scalar match is inferred from equal names, values or field hashes.

The tokens are 232 nominal capacities, 111 nominal zoom values, 61 angles, four burst counts, three lengths, two model identifiers and two shot-size identifiers. The census finds no displayed percentage or timing effect quantity in those strings. A nominal magazine title remains separate from chamber-inclusive source capacity; a nominal optic title remains separate from selected optical FOV/PiP precedence. Angle and length labels are not assigned recoil or dispersion units.

The qualitative index covers recoil, spread, handling, ADS, sprint recovery, reload, zoom, sway, velocity, spotting and capacity. It retains all 17 reviewed attachment-bug overview rows with their original confirmed, suspected, source-inconsistency or corrected-interpretation boundaries. Intended text does not override recorded actual bindings or observations. Existing bug models remain applicable; this pass supplies no new scalar implementation proposal. Its controls, occurrence/token coverage and parent raw reread pass. Selected UI/gameplay receiver limits remain explicit in L903.
<!-- L906-statement-comparisons:end -->

<!-- native-semantics:L1007:start -->
### Emitter input-schema reader boundary (L1007)

The two retained current volume-light emitter prefixes were tested against exact authored owner identifier arrays. Source/resource identities and consequential raw bytes pass the structural control. Apparent record counts at offset 4 and hash/packed-word pairs from offset 8 remain a candidate grammar. Three authored candidate IDs do not occur in those candidate tables, but no complete authored input count/type contract is established. This comparison does not establish a semantic negative or a complete resource reader. Input-table roles, offsets and emitter operation meanings stay unresolved. No further capture or widening was used. See the [receipt](../../reference-data/provenance/frosty-2026-10-01-L1007-emitter-input-schema-control.json).
<!-- native-semantics:L1007:end -->

<!-- native-semantics:L1008:start -->
### UI choice/value enum boundary (L1008)

The final enum method tests exact retained UI choice/value bindings. Current widget-to-zeroing DBD pointers, exported GUIDs and local keys pass the source identity control. The selected enum 536 UI array is empty, and its retained UI text list has zero records. Five selected spotting reset entries store exact INT32 values 0, 0 and 31; they are not established named enum choices. No complete named UI choice/value mapping exists in the inspected selected artifacts. This scoped limit does not establish absence elsewhere. Missing contracts and exact reopen conditions are in the two result rows. No zeroing or spotting enum meaning is promoted. See the [receipt](../../reference-data/provenance/frosty-2026-10-01-L1008-ui-enum-binding-control.json).
<!-- native-semantics:L1008:end -->

<!-- L907-source-boundaries:start -->
## UI frontier completion and remaining source limits (L907)

[L907](../../reference-data/provenance/frosty-2026-10-01-L907-weapons-ui-frontier-census.json) completes the available metadata/statement frontier. All 1,003 AD owners, their 2,317 text occurrences, 233 nonempty candidate effect/pro-con arrays and the exact extra MG5 iron-sight metadata target have dispositions. The current seven bar delegate resource bodies are verified, but no selected native UI/gameplay receiver or new operand-role control is established.

Intended recoil, spread, handling, ADS, sprint recovery, reload and optic statements stay separate from actual bindings and the existing reviewed bug models. The statement index preserves all 17 prior bug overview rows and their confirmed/suspected/source-inconsistency/corrected-interpretation scopes. No new scalar site proposal is qualified. Reopen exact effects only when the named dead-end condition supplies a same-owner receiver, arithmetic or operand-role control. No underbarrel, gadget, vehicle or soldier perk-display finding is added.
<!-- L907-source-boundaries:end -->
