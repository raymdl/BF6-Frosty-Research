# Open Frosty questions

[Frosty docs](README.md) · [Weapons](WEAPONS.md) · [Attachments](ATTACHMENTS.md) · [Attachment bugs](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/ATTACHMENT_BUGS.md)

The single list of open questions about the game data. Add new questions here, not in
separate files. When a question is answered, move the result to the topic page and
delete the row (git history keeps it).

Most questions need either a decoded native consumer (not available: the game code was
not examined) or a controlled in-game test. The suggested test is given where one is
known.

Active investigations with their own files:

- [Ranked in-game capture plan](../working/BF6_CAPTURE_PRIORITIES.md) (current priorities and test steps)
- [Recoil and spread recordings](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/working/BF6_RECOIL_SPREAD_RECORDING_HANDOFF.md)
- [Composite stats](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/archive/COMPOSITE_STATS_FINDINGS.md) (includes which native
  provider supplies Precision)

## 1.4.3.5 update limits (30 September 2026)

The [update receipt](../../reference-data/provenance/frosty-update-1.4.3.5-2026-09-30.json)
pins the current evidence and the exact missing routes.

| Question | Next step |
|---|---|
| Content changes in 751 patch-summary routes with no retained old raw, including 110 catalog-hash changes | A search of 70 other retained captures recovered 2 more (both drone gadget features, byte-identical; `supplemental-old-raw-search.json` in the 1.4.3.5 reports). Obtain a retained pre-update capture for the rest; do not substitute current bytes. |
| Before/after damage multipliers in the three current changed-record material grids | Obtain old raw for the exact maps, then use the bounded reader with each build's own descriptors. Current cross-map agreement is insufficient. |
| Asset/consumer implementing the announced APHEI/carrier damage restriction and shallow-water AI fix | Join exact consumers and compare old/current source; patch wording and current-only AI records are not proof. |
| Native significance of Class_d8dce156 enum member classRef changes | Resolve the descriptor metadata targets. Integer offsets, class size and alignment are unchanged; no instance-offset change is established. |
| Native effect of two purchase deeplinks moving from KST_Glacier_Meta to GRX_Online | Trace the store consumer. The serialized ownership move is established, not its runtime effect. |
| Three Blacklight selector inputs outside current/reference raw coverage | Capture exact inputs before a complete selector-graph claim. This does not block the listed unrelated attachment-bug retention. |

## Field meanings

| Question | Next step |
|---|---|
| The `Field_`/`Class_` hash algorithm | None known; see the [field map](FIELD_MAP.md). Use exact registry child/hash associations where available, then other stated name evidence. |
| `Field_0ef83ce9`, `Field_6eb133f8`, `Field_c39698a3` | Find a registry value or a consumer. |
| `Field_149939ab` / `Field_e9129d03` (non-unit Riser samples include 1.2 and 1.3) | Compare an optic with and without the pair in game. |
| `Field_440ed7fa` (frame-quantized WB duration) | Compare with fire-mode or animation timings. |
| WB firing `Field_c5d1c8fe/{Field_91121984,Field_0d926433}` | [All 63 weapon comparisons](WEAPONS.md#anonymous-wb-recoil-candidates) reject a direct substitution for named GS recoil bounds. Need a consumer or independent activation control; ordinary gameplay motion cannot name the anonymous source field. |
| Native ZDA/HDA state selection and H1 meaning | Ordered source rows and exact selectors reproduce all nine named Sym minima for 63/63 weapons ([receipt](../../reference-data/provenance/frosty-site-constants-2026-09-23.json)). This supports the ZDA stance columns and H2–H5 associations. H1 has no named Sym minimum. Use jump/sprint and stance captures or a native consumer to settle H1 and activation. |

## Source coverage

| Question | Next step |
|---|---|
| Complete source review of Analyzer inputs | Every input is classified in the final ledger, but about 1,176 rows remain blocked. Work the [active source leads](../working/FROSTY_RESEARCH_QUEUE.md#active-source-leads). All 63 site weapons are in scope; KSG is a source-only reference with proven campaign roots. Follow non-site branches only when they can affect a displayed or proposed value. Capture coverage is not semantic review. |
| Five imported object GUIDs absent from captured target files | [Verified caller report](../../reference-data/provenance/frosty-audit-object-targets-reviewed-2026-09-23.json): 15 raw pointer callers reach absent objects in PB_AT4, KST_Vehicles and SPC_RenderLayers. Need target definitions or resolution evidence; do not infer runtime failure. Keep shader caller mode scope unresolved. |
| Serialized expression resource format | [22 core-weapon resource bodies are captured](../../reference-data/provenance/frosty-audit-core-resources-2026-09-23.json). The [four-sample review](../../reference-data/provenance/frosty-audit-expression-resources-validation-2026-09-23.json) found no body reader in the inspected SDK source. Establish boundaries, fields and EBX metadata relationships before naming operations or treating embedded asset strings as runtime imports. |

## Weapons

| Question | Suggested test |
|---|---|
| Controller recoil: activation and composition of 0.95 (0.8836 before 2.1.1.0); six sniper rifles have no binding; `GRM_Recoil_Controller_03` is the only modifier with header integer `Field_94752c29` = 2 ([L4038](../../reference-data/provenance/frosty-2026-10-14-L4038-gun-sway-modifier-header-flags.json)), enumeration undecoded | Mouse and controller on the same PC and build, ADS and hip, identical M4A1 builds, plus a sniper. Separate amount, variation, growth and recovery. |
| Spotting: product or minimum composition (bases found per weapon in WB `Field_5ebda408`; [review](WEAPONS.md#spot-on-fire-base-ranges-1430-23-september-2026)); M45A1/Skorpion built-in 27/64.29 base; the source 0.1 versus site 0.14 CQB/Lightened candidates (M39 EMR, M417 A2, DRS-IAR, M2010 ESR; [exact M39 chain](../../reference-data/provenance/frosty-2026-09-24-L47-selected-spotting-chain.json)). Do not infer their product without composition evidence | Native activation/composition remains unresolved. The former observer recording request was removed as unnecessary ([operator removal decision, 28 September 2026](../working/BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)); retain the exact source-consumer question. |
| Regeneration: native addition and reset of the 5 s base plus ammo delay | Native addition/reset remains unresolved. The former regeneration recording request was removed as unnecessary ([operator removal decision, 28 September 2026](../working/BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)); retain the exact source-consumer question. |
| Recoil recovery: the native arithmetic behind the 0.8 factor scale, the 100 ms tail on the AK-205 and TR-7, the missing Lightened advantage in the LMR27 tail, and the camera layer above the bullets | Bullet-hole and camera captures on four profiles ([L4040](../../reference-data/provenance/frosty-2026-10-14-L4040-ak205-recoil-recovery-capture.json) to [L4049](../../reference-data/provenance/frosty-2026-10-17-L4049-stretched-time-fit.json); [summary](WEAPONS.md#recovery-captures-14-to-17-october-2026-l4040-to-l4049)): x0.8 applied on the site; no structural variant beats it on every weapon. Reopen on a readable implementation of the law or a season that changes the operands; a capture placing bullets against the camera on one shot would separate a stretched aim from a camera offset. |
| Spread: the switch rule between firing, not-firing and idle recovery; the site has no idle state | Firing to not-firing answered on the M433 ADS indicator ([L4050](../../reference-data/provenance/frosty-2026-10-15-L4050-m433-spread-indicator-law.json)): firing recovery 2.7 + 1.2 x delta^2.5 deg/s between shots and for one shot interval after the last shot, then not-firing 7.2 deg/s, each within 5% at 120 fps, as the site computes it. The idle state after 0.4 s is never reached in the 0.2 s tail and remains open (recording scenario 4 in the recoil handoff). |
| `IdleDecreaseTargetDuration`: native use, and the VSSM/Interdictor index exceptions | [Source table link resolved](WEAPONS.md#idle-duration-table-1430-23-september-2026): the first eight values match the ADS-time ladder minus one 60 Hz frame within 0.001 ms when interpreted as seconds, and the index equals the ADS animation index in 62 of 64 weapons. Spread settling on entering ADS is a supported hypothesis; the native consumer is unresolved. Test with VSSM ADS timing; do not equate its floats to measured recovery times. |
| Unused recoil bounds (`VerticalRecoilMin/Max/Increase`, `HorizontalRecoilLeft/Right`) | Compare with recordings before modeling. [L33](../../reference-data/provenance/frosty-2026-09-24-L33-polar-recoil-build-separated.json) withdrew the non-polar outlier; native use of these bounds remains open. [L111](../../reference-data/provenance/frosty-2026-09-28-L106-L111-orchestrator-trial.json) records all 882 current values; the 20 degree `MaxVerticalRecoil` cap is never reached by the site's recoil path (peak 8.6 degrees). |
| `ReloadThreshold`, `ReloadDelay`, `PostReloadDelay`; phase list `Field_dc244b57` (threshold × time lands nearest its second-to-last entry on 47 of 57 weapons) | Reload captures that mark ammo commit. The effective empty time is settled ([capture](WEAPONS.md#reload-values-and-empty-reload-capture-23-september-2026)). |
| Class traits: native activation | Compare a trait weapon with and without the class. |
| DLC Bolt (`ads_bolt`): effective sniper fire rate while scoped | The site keeps base RPM and marks the attachment unmodeled. Trace the exact ADS-bolt effect against ordinary/zoomed completion fields for all six snipers, retain the scoped/unscoped readiness and overlap question while holding Recon trait fixed. The former bolt-cadence recording request was removed ([operator removal decision, 28 September 2026](../working/BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)). A true capability operand alone does not quantify the cadence change. |
| General soldier/class settings: FasterHealing, Flak/StanceFlak, DamageSpot, LowProfile and movement defaults | Exact source operands and links are retained in the topic notes. Need a standard MP class/loadout selection path and the compiled/native consumer before assigning effective bonuses. Record class/specialization and mode settings in captures. |
| Mode/map application of shared health, damage, regeneration and spotting settings | [Registry, Conquest/Breakthrough and two-map source checks](WEAPONS.md#mode-and-map-context) are complete within the bounded pass. Need compiled/inherited application or live server values; registry membership, tags and stored defaults do not establish effective rules. Keep mode and round state fixed in captures; avoid Breakthrough retreat phases for baseline spotting. |
| Bipod and mounted states (recoil, no per-shot spread increase) | Not modeled; decide whether to model. |
| Collateral: native lookup code (the clamp rule is confirmed) | None needed for the site. |

## Attachments

| Question | Suggested test |
|---|---|
| Lights: idle recovery (on/off activation is answered: the twelve light modifiers alone set the header flag `Field_897a3f2c`, the dump's `OnlyOnWeaponLightEnabled`, [L4038](../../reference-data/provenance/frosty-2026-10-14-L4038-gun-sway-modifier-header-flags.json)) | Same 6P67 build, light on, stationary and moving hip growth and recovery; ADS as a control. A light-off trial would now test the flag, not the site. |
| SGX CQB/Long and Mini Scout Short sway: source gates the site values on canted iron sights ([L94](../../reference-data/provenance/frosty-2026-09-26-L94-optic-accessory-and-local-sight-sway.json)); removed 26 September | Optional: SGX CQB versus no muzzle with an optic, ADS sway pair. |
| Sway and ADS: camera versus aim motion; VSSM regular barrel has a GS +1 ADS binding but no WB effect (site 250 ms on both barrels) | [23 September source review](ATTACHMENTS.md#vssm-barrel-ads-follow-up-1430-23-september-2026) keeps the two paths separate. Measure regular/ASM barrel ADS with factory optic and fixed magazine, or decode the native GS consumer. |
| Sniper Tungsten: intended balance across weapons remains unknown; source-specific −6/−1/−7 steps are now implemented and panel-checked | Further gameplay captures can test shot behavior; they cannot establish design intent. |
| Slim Angled on L115, Mini Scout, Interdictor: does the second `GID_ADSTime_BTM_P10` binding stack? | Panels show one ADS tier ([bug 1](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/ATTACHMENT_BUGS.md#1-slim-angled-applies-an-unstated-moving-ads-penalty)). |
| Order of several modifiers on one field | No record combines two operations, so it cannot be seen in the data. |
| BROD 3 `TreatedBarrel` (label **Cryo**): offered in game? The site has no Cryogenic option | [Source identity/default confirmed](ATTACHMENTS.md#unmatched-branch-follow-up-1430-23-september-2026); check the BROD 3 barrel menu or active availability consumer. |
| M4A1 plain `ERG_Magwell`: player-facing purpose | Source branch selects an empty default part and is distinct from FlaredMagwell; [review](ATTACHMENTS.md#unmatched-branch-follow-up-1430-23-september-2026). A direct menu or consumer trace is still needed. |
| `AMO_SubsonicFrangible` on 15 weapons: no site selection (kill-switch default True) | All 15 branch defaults rechecked in1.4.3.0; live availability and overrides remain unresolved. Check the ammo menus after updates. |
| PP-19 25 Rnd and GRT-CPS burst fire: source-only branches | Recheck if a build offers them. |

The full list of Frosty records without a site match is the
[13 September inventory](../archive/FROSTY_UNMATCHED_WEAPONS_ATTACHMENTS.md).

## Optics

| Question | Suggested test |
|---|---|
| L115 optics at render FOV 55 (same as RPK-74M bug 11) | Compare R-MR, ROX or Mini Flex on the L115 and another sniper. Historical comparison suggestion only; optic-framing recordings were removed as unnecessary ([operator removal decision, 28 September 2026](../working/BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)). Source/model precedence remains unresolved. |
| ES 5.7, GGH-22, P18, M45A1 optics at 55, while other pistols use 40 | Compare an optic on the P18 and the M44. Historical comparison suggestion only; optic-framing recordings were removed as unnecessary ([operator removal decision, 28 September 2026](../working/BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)). Source/model precedence remains unresolved. |
| M2010 ESR inline model parts: SDO 55 and LERT 59 beside the shared parts (34, 20) | Exact raw paths and GRX structure reviewed; native precedence remains unknown. Compare scope size with another sniper at the same PiP/FOV settings. Historical comparison suggestion only; optic-framing recordings were removed as unnecessary ([operator removal decision, 28 September 2026](../working/BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)). Source/model precedence remains unresolved. |
| SL9 iron sights at the default 55 | Checked 16 September: no visible effect found; the value may still be unset. |

| Breath control: duration, sway effect and standard multiplayer activation | [Source expression/channel link](ATTACHMENTS.md#sway) is resolved. Need a caller/compiled consumer trace or controlled measurements. |

| Zeroing: effective list selection, units, attachment activation and ballistic correction | [63 raw WB blocks](WEAPONS.md#zeroing-source-configuration-1430-23-september-2026) are recorded; 12 have named min/max/delay. Effective selection, units, activation and correction remain unresolved. The former zeroing recording request was removed as unnecessary ([operator removal decision, 28 September 2026](../working/BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)); this does not authorize ballistic correction. |
| Glint: final selector application and visibility thresholds | M2010 iron-sight and decoy no-flare source chains are resolved. Need native composition or controlled observer tests for gameplay visibility. |

## Game updates and collection

| Question | Next step |
|---|---|
| 1.4.3.0 `Aim_*_PiP` comparisons retain provisional field semantics | [Bounded layout review](TOOLS.md#sdk-and-decoding) reproduces one pair through exact type keys and nested class references. Shared decoded values match; one import was added. Keep warnings until affected fields have independent layout/consumer evidence. |
| 1.4.3.0 patch note "incorrect impact visual effects": no matching asset change in the captured set | Widen the capture to impact effects. |
| Collections for 1.4.2.5 and 1.4.3.0 are partial | See [Tools](TOOLS.md#per-build-collection-rules). |

### Unresolved soldier file GUIDs

Confirmed references in `Class_25c12137/Field_a2734e52/member/Field_8cf424e7`. All
file/object pairs were already `BadRef` in 1.4.2.5 XML. Neither build catalog contains
the target files, and the 16,426 captured raw bodies have no matching objects. Caller
names do not identify the targets or prove runtime use.

| File GUID | Caller context | Caller assets | Pointer uses |
|---|---|---:|---:|
| `2631e8f8-a115-413d-a696-5ec194081d73` | Ladder, traversal, revive, melee, fire | 15 | 33 |
| `8f992c03-80cb-4ed5-8a6e-0274a57f659c` | In-air and parachute | 3 | 11 |
| `b4765624-c221-4138-b446-3b3aa155cf3b` | Overlay, melee, in-air | 3 | 3 |
| `d0a2de18-a7b2-4c3c-9e87-aff6ddc8a180` | Mandown, revive, rope, zipline | 8 | 16 |

Reopen only if a target body becomes available, a catalog resolves a GUID, the caller
pointers change, or a consumer can answer a specific question. Evidence:
[GUID trace](../../reference-data/provenance/frosty-1.4.3.0-unresolved-guid-trace-2026-09-16.json);
the 16 caller assets are indexed in `asset-findings.json`.

## Weapon Attributes follow-up

- `Field_b30a73ed` / `Struct_a92e7ee4`: exact runtime target remains unknown.
  KS18K Slim Angled moving-ADS penalty is no longer pending: source collection,
  menu score and twelve indicator captures support zero. Trace the native consumer
  to name the alternate field; do not infer it from the modifier asset name.
- Hipfire `IncreasePerShotFraction`: confirm the native comparison behind the
  inferred conditional factor. Confirm the native Control sine operation and
  zero-variation behavior. Precision native provider and all fallback rules remain
  incompletely decoded.
- Mobility uses ADS animation index, not necessarily the zoom-transition index.
  L115 bases are 2 and 1 respectively. The runtime score now preserves this distinction.

Current scope and evidence: [Weapon Attributes model](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/WEAPON_ATTRIBUTES_MODEL.md).

### Burst recoil activation (21 September 2026)

GRT-BC and SL9 captures show the same recoil values in the hover and equipped
states. KORD also has an equipped capture with unchanged recoil. SG 553R and
PW5A3 currently have hover evidence only. These observations do not establish
recoil behavior during firing.

The GRT-BC source chain resolves through `MSBSGROTB_WB.xml` objects
`...0028` (unlock binding), `...001e` (behavior operation), `...0033`
(behavior list), and `...0022` (fire-mode selector). The selector mask is
`0x8`, equal to `1 << 3`; SDK enum `Enum_16e6fa59.Field_c57b586e` is 3,
and the separate `WPM_ERG_BurstFireReplace_W10` operation selects that enum.
The selector GUID `588728fd-2ae7-4424-aa22-45d9b3c82ba0` matches all three
GS bindings: recoil conversion, recoil P20, and AutoIdentifier. No broken
reference or mask mismatch was found in this chain.

The shared `CMU_SemiAuto` uses the same selector class (`Class_9dfbb158`)
with mask `0x1`. This supports interpreting the burst selector as a fire-mode
condition. Linear Comp has direct attachment bindings instead. A menu provider
that does not evaluate this condition could therefore show the changed mode
list without applying burst recoil. This remains an explanation, not a confirmed
native execution trace. XML and SDK field types do not show which mode state the
menu provider evaluates or whether it evaluates these behavior lists at all.

Next evidence needed: native menu-provider/selector execution, or a controlled
firing comparison that separates actual recoil behavior from menu display.
Do not classify this as a gameplay attachment failure from panel captures alone.

## L4006 - Parked questions screened against the registry and EA-note methods (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4006-parked-weapon-questions-against-new-methods.json). The methods of 9 and 10 October were applied to each parked row of the research queue. Weapon registry rows hold the same numbers as the files (L4000, L4004), add no field names (L4002), and attachment effect files (`WME_`, `WPM_`, `GDM_`, `GID_`, `AAM_`) have no registry rows at all.

| ID | Question | What the new methods give | Reopen condition |
|---|---|---|---|
| W1 | Bipod and mounted modifiers, idle table | GS registry rows equal own values (L4000) and add no name; no EA figure | not met |
| W2 | VSSM GS ADS +1 against WB timing | no registry row for the GS binding; no EA figure | not met |
| W3 | M4A1 Magwell, BROD3 Cryo, SubsonicFrangible | no registry row; EA notes do not mention them | not met |
| W4 | Reload threshold and delays, Field_440ed7fa | reload rows equal own values (L4000); Field_440ed7fa has no registry row (L4002) | not met |
| W6 | Burst recoil, controller activation, lights, modifier order, class traits, Slim Angled | no registry row beyond package Priority values; no EA figure | not met |
| W7 | Weapon Attributes provider, Field_b30a73ed | no registry row (L4002) | not met |
| W8 | Grid surface and velocity candidates | outside the three methods; no new field association | not met |
| W9 | Jump and landing inventory | no weapon registry row; soldier rows were recorded in L3350 | not met |
| O1 | Ambiguous PiP layouts | no registry row; no EA figure | not met |
| O2 | Riser fields, model precedence, render FOV | no registry row; no EA figure | not met |
| O3 | Optic glint and breath control | no registry row; no EA figure | not met |
| M1 | Regeneration and spotting activation and base values | EA 1.3.3.0 states M45A1 and vz. 61 are subsonic by default, matching their stored 27 / 64.29 ranges (L4001); soldier rows RegenerationDelay 5, RegenerationRate 10, SpotOnFireDuration 0.4 and DefaultSpotDuration 5 were already recorded | partly: official statement added, activation still open |
| M2 | Soldier settings, abilities, suppression, movement | soldier registry rows recorded in L3350; no new consumer | not met |
| M3 | Four soldier file GUIDs | outside the three methods | not met |
| G1 | Mode and map overrides | outside the three methods | not met |

4 raw-offset checks matched.

## L4009 - Audit of earlier negative closures (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4009-audit-negative-closures-evidence-reread.json). - **Byte re-read.** 109 receipts of 116 leads; 65 carry byte-level evidence; 16432 recorded checks over 553 files; 0 differ, 0 files changed, 0 missing.
- **Leads without byte checks.** 45, mostly of 23 to 26 September. Evidence kind as extracted: raw-offsets 23, decoded-values 12, counts-only 7, decision 3.
- **Re-tests by a second route:**

| Lead | Earlier claim | Independent re-test | Result |
|---|---|---|---|
| L34 | SpawnDelay is 0 on all 63 primary weapon files | registry row Shot.SpawnDelay (equal to own value by L4000): 0.0 on 63 of 63 | reproduced |
| L23 | InitialSpeedVariation (Field_661b879d) is 0 on every weapon | registry row present on 8 weapons, all 0.0; own Field_661b879d {0.0: 83, -1.0: 1} over 83 owners | reproduced (one owner outside the 63 holds -1.0 on a path ending in the same hash) |
| L36 | Only the DRS-IAR has a nonzero HeatPerBullet | registry row OverHeat.HeatPerBullet exists on ['drsiar'] only, value 0.0025 | reproduced |
| L21 | Field_54ba3947 and Field_834a710f are 1.0 in both aim branches | own values: {1.0: 152} and {1.0: 152} | reproduced |
| L1 | Field_c2b88435 is a 0/1 flag that differs on a few weapons | own values {0.0: 77, 1.0: 6} | reproduced |
| L48 | Field_bd024e1d stores -1, 2 or 99 | own values {-1.0: 93, 2.0: 1, 99.0: 2} | reproduced |
| L72 | Field_db0fcea2 holds 16 on DB-12 shells | own values {1.0: 79, 16.0: 4} | reproduced (1 elsewhere, 16 on four owners) |
| L116 | Field_8d6d2bc1 is not set on weapon files | own values {0.0: 83} | consistent |
| L7 | Per-weapon spot ranges are stored but no reader was found | L4001 and L4008: stored 27 / 64.29 on two sidearms; the stat screen shows them | claim stands; its consequence (leave the site at 54 / 150) was wrong and is corrected by L4008 |
| L17, L24 | Match Trigger binds recoil and recovery effects; the site shows none | screenshot audit: all 24 Match Trigger panels show recoil amount, recoil variation, Control and Precision equal to the weapon's other panels | site equals the stat screen; a single-fire effect is not displayed there, so the panels neither confirm nor refute it |

- **Lesson.** The earlier closures are accurate about file contents. The weak pattern is 'stored but no consumer found, so the site is left alone' (L7): check such values against the screenshot audit or EA notes before accepting the closure.
- Not re-tested: 35 leads whose claims concern names, routes or counts.

72 raw-offset checks matched.

## L4012 - UI metadata paths (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4012-ui-metadata-paths-review.json). Eleven UI metadata files not read before (seven under `Common/UI/Static/Metadata`, four `CAT_*` tutorial cards) hold display text, icons and references only. Dead end, closed by the operator.

- Hints, without numbers: the two knife descriptions and the Knife Sprint card say sprint speed is higher with a knife out (not on the Sledgehammer); the bipod card says accuracy improves when deployed.
- Reviews: Datamining `reports\metadata-review-2026-10-10`.

11 raw-offset checks matched.
