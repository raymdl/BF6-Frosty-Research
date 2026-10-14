# Gadget source evidence

Gadgets are research for a possible future Analyzer section. Vehicles are a separate game category and have their own page, [Vehicles](VEHICLES.md). Cosmetics, skins and artwork are excluded. Sound is out of scope. Battle royale, Granite and Gauntlet mechanics are excluded, and shared objects stay candidates where standard multiplayer use is unproved. Site implementation is not authorized.

This page records what the saved game data says about each gadget: attributed UI text, dated EA statements, stored source values and the selection chains that reach them. It does not say what a gadget does in a match.

**Season 5 (2.1.1.0).** Most values below were read at 1.4.3.5. Where a stated value changed in 2.1.1.0, the new value follows it as `(2.1.1.0: x)`; `registry` means the registry row changed and the file value did not. Derived columns (products, hit counts, EA comparisons) are not recomputed. Source: `builds\2.1.1.0\reports\registry-diff-2026-10-14\` and the 13 October update trace (`2026-10-13-update-2110-post\STAGE6-8-TRACE-RESULTS.md`).

## Evidence classes

Every statement below belongs to one class. A source value can be quoted next to a UI or EA statement, but the page never converts one into the other.

| Class | Meaning | What it cannot prove |
|---|---|---|
| Stored source value | A value in a selected export, read by exact owner, member, offset and hash. | Units, role, activation, default loadout, effective stat. |
| Inherited default | A value on a base-class field the selected export inherits. | That it drives the gadget's behaviour. |
| Attributed UI statement | Exact card or ability text, with its string id and client build. | A join to a gameplay export, or current availability. |
| Dated EA statement | A line from a pinned EA article snapshot, with its version. | That the saved build still behaves that way. |
| Hypothesis | An interpretation with named alternatives and a discriminating test. | Anything. |
| Effective runtime behaviour | Observed or proved operation. | Nothing on this page reaches it. |

**Registry defaults are not selected values.** A selected export's own value must never be replaced by, or averaged with, the registry or leaf default, and the same rule holds when only one of them is known.

A UI number that equals a stored value is recorded as a correspondence. It is not an execution control. Where this page puts them side by side it says so.

Receipts for everything below are in `reference-data/provenance/`, found through [`lead-index.json`](../../reference-data/frosty/lead-index.json). Raw run folders are under `BF6 Datamining/reports/weapon-analyzer-research/`.

## Where earlier gadget findings live

- [Data graph: gadget routes](DATA_GRAPH.md#gadget-routes-hotfix-head-4892087) holds the selection chains traced up to L215 (hotfix Head 4892087), including Spawn Beacon, Ladder, Supply Crate, Decoy, drones, mines and the call-in, launcher, explosive, tools and utility censuses.
- [UI text](UI_TEXT.md) holds the 78 gadget UI records (63 substantive, 12 label or stub texts, 3 missing ids) and the tooltip mapping. [`gadget-ui-metadata.json`](../../reference-data/frosty/gadget-ui-metadata.json) holds their exact text and ids.
- [Gadget research and potential additions](../working/GADGET_SITE_ADDITIONS.md) holds the working proposals and the validation checks that have not been run.

## Transfer census, gadget side (L640, L645, L648)

Moved from the vehicle page, which keeps the vehicle side ([Vehicles](VEHICLES.md#vehicle-semantic-transfer-census-l640)).

[L640](../../reference-data/provenance/frosty-2026-09-30-L640-transfer-census.json) inventories 39 gadget comparison rows, 17 shared vehicle comparison rows and the per-family vehicle stat map. Exact class, descriptor key and field identity permit transfer of configured RateOfFire, MagazineCapacity, reload source fields and Shot.InitialSpeed components. Replenishment and reserve-count semantics are unconfirmed on infantry and do not transfer. Gravity and drag transfer only for the exact infantry projectile schema consumed by `frosty-ballistics.py`; other projectile owners keep their own field identities. M4A1 and L115 extraction controls pass the IEEE float32 contract.

[L645](../../reference-data/provenance/frosty-2026-10-01-L645-weapon-shape-profiles.json) extracted 11 weapon-like gadget firing owners with full source precision. Effective reload totals stay null because the selector and composition are unconfirmed. L648 adds 15 selected gadget, underbarrel or source-only throwable owners, including Breaching Dart, M26 and M320 HE; unsupported AT, TB and Smoke selections stay explicit, and C4, Claymore and M4 SLAM remain included. Durability and named Season 5 validation exclusions stay separate from extraction.

## Displayable gadget stats (L224-L228)

These are the gadget half of the 1 October display-stat run. They keep configured fields, attributed UI or EA statements and unresolved effective stats apart.

| Lead | Result |
|---|---|
| L224 | All 39 comparison rows, 28 current proposals and 78 metadata records classified with separate configured and effective support. |
| L225 | Twelve high-impact mechanic groups keep source or dated EA meanings without an effective numeric consumer mapping (exhausted). |
| L226 | The proposed gadget stat schema maps all 39 candidate rows; site use needs separate authorization. |
| L227 | All 28 proposal rows audited at named-field level, repeated fields mapped to L224. |
| L228 | 130 exact named configured heat operands on 26 selected gadget and underbarrel owners; effective heat and cooldown unresolved. |

## Repair Tool, Defibrillator and Squad Revive (L232)

[L232](../../reference-data/provenance/frosty-2026-10-02-L232-repair-defibrillator-squad-revive.json). Saved utility sources are Head 4892087; matching Head 4909002 copies are byte carry-forward, not new measurements.

| Item | Class | Statement |
|---|---|---|
| Repair Tool range | Stored source value | Named RepairTool_Range stores 2 / 0 / 10, selected by SimEx binding 0. Slot roles, units and query geometry unproved; no effective 2 m range. |
| Repair Tool interval | Stored source value | Apply Damage / Repair Interval stores 0.10000000149011612 / 0.009999999776482582 / 1 (binding 1), vehicle-damage rank 3 / 0 / 6. Shared interval candidate; cadence unproved. |
| Repair amount | Stored source value | Named Repair Amount Per Second stores 40 / 0 / 250 (`Field_42c8b257`, offset 39572 of GRX_Gadgets_Glacier, f32 40.0, re-read 2 October). **40 is not verified health per second.** |
| Repair Tool heat | Stored source value | HeatPerBullet 0.0142000000923872, HeatDropPerSecond 0.4000000059604645, OverHeatDropDelay 0.10000000149011612, OverHeatThreshold 0.15000000596046448, OverHeatPenaltyTime 0.5, named through the M27IAR own-wrapper control. Configured heat is separate from repair rate and cooldown. |
| Repair Tool projectile | Stored source value | Class_23637dce StartDamage and EndDamage 13 / 13, falloff 100 / 200. Hit cadence unknown. DestroyGadget is a selected affector; its IsDisarmingGadget invocation is unproved. |
| Defibrillator | Stored source value | 13-row curve candidate, two six-entry revive affectors, a separate damage affector (ordinary CT Defib_Damage, address 2792). Supercharge selects TraitSprintSpeedMultiplier without a proved setter. Selected true channels: FastSprintRequired, Defibrillator_ManuallyEquipped, CanReviveTeam_WithGadget; unselected IsReviving stores false. |
| Defibrillator charge | Dated EA statement | EA 1.2.3.0: 0.35 s minimum charge before revival, 1 s full charge (charge duration, not total interaction time). Not measured at Head 4909002. |
| Squad revive | Stored source value | Named total time 4.71999979019165 s and Support 2.200000047683716 s (`GRX_Glacier_Soldier`, offsets 24244 and 22900, re-read 2 October), buffer 0.4000000059604645. Provisional HealthRestored affector stores eleven values 100, 90, 80, 75, 70, 60, 50, 40, 30, 25, 20; class rank 6 / 0 is not equated with list slots. Regen selects named rate 10, delay 0, amount 0. |
| Recipient query | Stored source value | Exposes RootTransform, TeamId, SquadId and ReviverPlayerId; no proved predicate, list operation or reach. |

Open: the Squad file `d0a2de18-a7b2-4c3c-9e87-aff6ddc8a180` (two exact child GUIDs) and the FasterRecharge selector owner `aeb43f2c-3c7b-4056-a8f6-f965da671da3`. A Killshot export/import control reproduced; no owner was found in the historical index, and no global absence is claimed. On 4 October 2026 none of the six retained catalogs (Heads 4420709 to 4909067) listed the Squad file GUID or the three other unresolved caller-table GUIDs, while two controls resolved in every catalog ([lookup receipt](../../reference-data/provenance/frosty-2026-10-04-squad-revive-file-guid-catalog-lookup.json)). With no catalog route a guarded capture cannot be requested; that is a lookup limit, not evidence the file is absent from the game.

Operator description of revives (4 October 2026; not measured): Support can drag and revive any teammate to half health and has a buff that speeds up revives; Support's defibrillators revive to half health on a tap and to full health when fully charged; any class can drag and revive squadmates to half health.

## Regeneration and healing schemas (L229)

[L229](../../reference-data/provenance/frosty-2026-10-02-L229-gadget-regen-healing-effect-schemas.json), Head 4909002 with historical comparison.

| Item | Class | Statement |
|---|---|---|
| Regeneration affectors | Stored source value | Three affectors share root key `12c2e0050200181dda3acd681d713afb` and entry key `4c0e9affce5b0ddafd22b9f84a957a3e`. FasterRegen 30 / 2.5 / 0 (enum 0, Boolean false); Hemostatic 12.5 / 2.5 / 0 (enum 2, Boolean false); post-revive inline 0 / 0 / 0 (enum 0, Boolean true) importing named rate 10, delay 0, amount 0; baseline named declarations 10 / 5 / 0. The Boolean and enum operations are unnamed. |
| Pouch and Crate healing | Stored source value | Share root key `3ee7f406b86151f14a9e86c1c739f345` and entry key `1c1c478ebbf923a9ac8ef7ae4b6e26c2`; both store 0 / 20 / 2.5 candidates. `Field_33d6811e` is true for Pouch and false for Crate. The healing entry differs from regeneration, and a shared wrapper identity does not transfer field or Boolean meaning. |
| Enum key census | Stored source value | The exact regeneration enum-key reverse field-reference check finds one typed field user in each of the current and historical descriptors (the regeneration entry). A descriptor census, not an instance census or operation control. |
| Cover and CB90 health | Stored source value | Each declares its own `Field_9040392c` under a different key; their shared base does not. MaxHealth transfer between them is invalid. |

No operation control (add, replace or multiply) exists for any of these. Equal numbers and common wrappers do not name one.

## Supply, medic and ActiveMedic (L233)

[L233](../../reference-data/provenance/frosty-2026-10-02-L233-healing-resupply-functional-dossiers.json). UI text is from client 1.4.3.1, Head 4892087; source is current Head 4909002 where stated. Granite and BR material is excluded; Standalone Medic Crate and Ammo Bag are identity candidates, not confirmed multiplayer items; Supply Drop has no relevant multiplayer caller.

| Item | Class | Statement |
|---|---|---|
| Supply Pouch | Attributed UI statement | UI `CF806780`: single-use pouch that replenishes ammo and medical supplies for the owner or teammates; fully restocks primary and secondary ammo capacity and restores a portion of health. |
| Supply Pouch | Stored source value | Provider selects five effect entries (auto-replenish, GasMask and NVG resupply, three ammo rows to PrimaryWeapon and Sidearm). Unnamed lifetime candidate 60 and UI-only 30 / 15 classified. Resource and mode applicability of the GasMask and NVG effects is unproved. |
| Supply Crate / Supply Bag | Stored source value | Pickup reaches enable and callback graphs (RIDs `4416c7136c35d68f`, `0ec7446691fdd4a3`); the callback binds the self-speedup affector. AmmoCrate selects PrimaryWeapon and Sidearm. Crate parents select the MedicCrate healing affector: two null-reference f32 wrappers with literals 0 and 20, a direct 2.5, three false flags; its selector selects the Ignore_Damage token, a configuration token and not damage immunity. |
| ActiveMedic (Restock Allies) | Attributed UI statement | UI `B29284A3`: "Resupply and heal nearby friendly forces for 10 seconds. Reviving teammates takes only 1.7 seconds." Both Support paths select ActiveMedic (slot 3); Support path 2 selects CrateResupplyPlus (slot 0). KST children store Boolean false with unknown polarity. |
| Pouch and crate rules | Dated EA statement | EA 1.0.1.0: deployed pouches cannot be picked up, vehicle healing removed, pouches grant one extra C4 as overstock and use repair-station-style over-time healing. |

**Open question: the 1.7 s revive.** No source value for 1.7 was found. The squad-revive source stores 4.72 s and Support 2.2 s (L232). Whether the ActiveMedic state shortens the revive, and where 1.7 comes from, is unresolved.

Ready prediction (not dispatched: revive time is not a site number today): a squad drag revive takes 4.72 s for a non-Support, 2.2 s for Support, and 1.7 s for Support with ActiveMedic active (1.7 from the UI text only). The check is frame counting on existing footage from the trusted creators, with no new recording request. Whether 4.72 s includes the 0.4 s buffer is unknown, so a footage check should report both readings.

The Vehicle Supply Crate side of this run is on the [vehicle page](VEHICLES.md#from-the-gadget-runs-vehicle-supply-crate-and-cover-health-channels).

## Protection and concealment (L234)

[L234](../../reference-data/provenance/frosty-2026-10-02-L234-protection-concealment-functional-report.json), from `CURRENT_REPORT.md` and `current-handoff.json`. The run's earlier `blockers.json` is stale and not used.

| Item | Class | Statement |
|---|---|---|
| MP-APS and EIDOS | Stored source value | `VEH_Gadget_MPAPS` object 38 and `VEH_Gadget_EIDOS` object 40 select feature exports; each feature selects the logic SimEx. Named AliveTimer 5.0 / 0.0 / 50.0, MaxIntercepts 3 / 1 / 10 (tuple `Field_42c8b257 / Field_c06d0cbb / Field_3ff76ddb`, default, minimum and maximum roles unassigned), EIDOS Max Intercept Range 5.0 / 0.0 / 20.0 and a Previous Targets state. **Only the serialized association is closed.** Compiled feature boundaries (RIDs `3ca94ebf63445fbd`, `ff4984bf5104a851`), projectile predicates and recharge stay opaque, and neither "3 effective intercepts" nor 5 s or 5 m is claimed. |
| MP-APS and EIDOS | Attributed UI statement | UI `3F62B7B5`: larger projectiles including missiles, mortars and tank shells, up to 3 per activation window after initial detection. UI `67725988` (EIDOS, card-labelled GPDIS): thrown and launched grenades, up to 3 per detection-started window. The UI 3 and stored MaxIntercepts 3 are a correspondence, not a control. |
| Hemostatic | Stored source value | Affector_AutoRegen_HemostaticSmoke RegenerationRate 12.5, RegenerationDelay 2.5, RegenerationAmount 0.0 (re-read 2 October); enum member 2 qualified but unnamed. |
| Hemostatic | Attributed UI statement | UI `41BB4EBC`: revival 2.2 s, regeneration 12.5 hp/s after 2.5 s, slower bleedout. The 12.5 and 2.5 match the stored values and 2.2 matches the Support squad-revive time (L232). Units and activation are unproved. |
| Deployable Cover | Stored source value | Four named part associations (all Front); four f32 200.0 operands (DamageZones offsets 340, 548, 756, 1028, re-read; no HP or total claimed); selected suppression -100 and explosive 0.5 candidates. Zone health operation unproved. |
| Smoke, M320 Smoke, Flashbang, Concussion, mask | Attributed UI statement | UI `61638249` (Smoke Grenade: concealment, clears infantry markers within the radius), `3A7EE575` (M320 Smoke), `7D174130` (Flashbang: blindness scaled by proximity and line of sight), `B8B7884E` (Concussion: disorientation, temporary ADS and sprint prevention), `71DC2D9B` (protective mask against VL-7 disorientation). Source selections and parameters are in the run report. M320 Flash has no established standard multiplayer projectile selection. No standard multiplayer armor mechanic was established. |
| Fixes | Dated EA statement | EA 1.1.2.0 (2025-11-18): Deployable Cover persistence after vehicle destruction fixed; MP-APS smoke propagation between friendlies fixed; GPDIS placement-preview interference fixed. |

## Deployment and lifecycle (L235)

[L235](../../reference-data/provenance/frosty-2026-10-02-L235-deployment-lifecycle-functional-handoff.json). Historical Head 4892087 and current Head 4909002, each stated; current byte equality is checked per asset.

| Item | Class | Statement |
|---|---|---|
| Spawn Beacon | Attributed UI statement | UI `3A5A0145`: single-use deploy point for the operator and each squad member; constant sound audible to hostiles; inactive after the owner deploys; squad-member deployment disabled in Small Scale Battles. Inactive is not necessarily destroyed. |
| Spawn Beacon | Stored source value | Ability, CUST, WB, Shot to the base VEH export. Ammo 1 / 1 / -1, AutoReplenishMagazine true, rounds -1 (a resource tuple, not an active count or unlimited uses). Killswitch Boolean false has unproved polarity. |
| Ladder | Stored source value | Separate deployed mesh, physics and LadderConfig; one plain interaction branch against three Assault branches including LadderTop (not three active ladders); vector (0.5, 3.84, 0.249939) without units; persistence exports 30 and 6 are not proved cooldowns. UI: higher vantage points; placement angle can enable bridge or ramp use. |
| Recon and common drone | Stored source value | Selected TimeToLive and OutOfBounds branches; three attached-projectile battery-drain multipliers, Drone_MaxLifetime, NormalizedRemainingLifetime, detonation on lifetime elapsed or destroyed and nearby-explosive range. Nine current parameter exports carry operands but no proved capacity or lifetime. Payload-drone and SP rows (operands 2.0 and 0.35) are SP routes, not multiplayer evidence. |
| EOD Bot | Attributed UI statement | Remote robot for repair, objective arming and disarming, gadget disruption and deployment; self-destructs after remote M-COM arming completes. Aim tuple -180 / 180 / -22 / 45 and a durability-like 75 are unnamed configured values without units. |
| NVG | Stored source value | WB and client imports reach a captured relay and Subsurface lighting (two captures at Head 4909002). Mutator triplets MaxDuration 51 / 1 / 99, Degradation_Start% 0.25 / 0 / 1, MaxExposureOffset -2 / -10 / 0 (`MutatorDatabase_CH1_S02`, re-read 2 October). UI for both NVG records is only "NVGs". |

## Detection, jamming and designation (L236)

[L236](../../reference-data/provenance/frosty-2026-10-02-L236-detection-designation-functional-result.json). UI is historical Head 4892087 card text; EA statements are dated and snapshot-pinned. Audio findings in the run are excluded.

| Item | Class | Statement |
|---|---|---|
| T-UGS | Attributed UI statement | UI `37A814D7`: spots moving enemies, vehicles and gadgets; crouching or prone infantry can evade; team world and minimap marks. |
| T-UGS | Stored source value | Vehicle and gadget flags true; SpottingRadius payload 15, duration 2, pulse delay 1.5, Intel radius multiplier 1.5, ShadowSpeedThreshold 4; Ammo 1 / 1 / -1. Seven subsets of three query ids are unmapped filter clues; anonymous 75 / -1 / -1 operands are kept apart from named parameters. |
| T-UGS | Dated EA statement | The owner's death no longer destroys the device; spotting persistence after the owner respawns improved. |
| MTN-55 / proximity | Attributed UI statement | UI `EE72583F`: spots enemies within visible range; one scan per second; two-second mark; world and minimap marks. EA 1.3.1.5 describes enemy-soldier spotting reliability. |
| MTN-55 / proximity | Stored source value | Vehicles true, gadgets false, LOS true; radius payload 7; pulse 1 and duration 2. **The UI timing and the stored pulse and duration correspond; that is not an execution control.** Primary owner selection is a candidate. |
| Mobile Jammer | Stored source value | Radius default 10, Ammo 1 / 1 / -1, AutoReplenishDelay 45 (source only); NumJams is not a cap. UI `2C7891A8`: carried or tossed, temporary effect on enemy equipment. |
| Drone gadget disruption | Dated EA statement | EA 1.3.2.0: close targets through walls, distant targets need line of sight, no threshold stated. Source candidates: max-distance 80, max-angle 2.5, thresholds 12 / 18 / 25; DestroyGadget has unmapped 1000 fields; no damage amount proved. UI `34F9718C`. |
| PLD / Laser Designator | Stored source value | Zoom distance candidates 80 / 180 / 360 / 540, angles 10 / 3.75 / 1.875 / 1.25; duration candidates 5 / 30 / 20, MarkTarget 15, laser progress 0.5. Dated EA: 20% lock-range benefit (1.3.1.0), designation 20 to 9 seconds. The EA 9 s, source 5 / 30 / 20 and MarkTarget 15 stay distinct. UI `8DE53FB4`, card association ambiguous. |
| Tracer Dart affector | Stored source value | EnableLocalLocking, TemporarilyDisabled, RemoveProjectile, Destroy, Stop, Valid and TTL carry **null defaults** (no zero or false claim). UI `5F6B5F0A`; EA 1.4.2.0: marked targets can lock via launchers. Do not compare with the projectile's TimeToLive 20 below. |
| HSS / Lancet | Attributed UI statement | UI `72DE420D` (internal name Lancet, display DGMK4; no UI-to-gameplay join). Selected chain and ammo configuration at Head 4892087; the current chain is in the selection-chain section. |

## Gadget projectiles and explosions (L230)

[L230](../../reference-data/provenance/frosty-2026-10-02-L230-gadget-projectile-explosion-values.json), Head 4909002. Names come from the exact current IGLA declaring-schema control where the gadget's own wrapper names nothing.

| Gadget | Class | Values |
|---|---|---|
| IGLA | Stored source value | Own Damage 100, Drag 0, MaxSpeed 640, InitialSpeed 500, TimeToLive 40. The MaxSpeed registry leaf is 480 and separate. The declaring key differs from the older L152 key; no historical transfer. |
| Stinger (gadget) | Stored source value | Own wrappers zero. Controlled-schema Damage 100, Drag 0, MaxSpeed 400, with inherited InitialSpeed 350 and TimeToLive 18. |
| TracerDart projectile | Inherited default | InitialSpeed 350, TimeToLive 20 (owner-01, offsets 336 and 340, re-read 2 October). Inherited declared default; not shown to be the effective launch speed or lifetime. **This is the projectile, not the Tracer Dart affector** whose TTL is a null default. |
| Airburst | Stored source value | Primary InitialSpeed 250, TimeToLive 0.25; lingering object InitialSpeed 0, TimeToLive 5 (not an own Airburst wrapper and not the effective fire duration). Lingering damage affector holds four unnamed tuples. |
| Incendiary | Stored source value | Primary InitialSpeed 300, TimeToLive 10, own DamageMultiplier 1; MinimumBlastDamage hash absent in the seven-slot array. |

The Airburst and Incendiary primary explosion roots are the same nonexported class (key `a57116aedf259bd743cedc6f7d0622f5`); no member or value transfers between them.

## Selection chains (L231)

[L231](../../reference-data/provenance/frosty-2026-10-02-L231-gadget-selection-chains.json). Exact source edges only; no UI join, activation owner or runtime behaviour.

- Lancet / HSS Equipment, Ability, Feature, TrackAndDestroy: three exact current pointer checks pass at Head 4909002 (two-owner safe capture, no failures). This closes the missing-current-owner gap the detection run left.
- Claymore projectile to `SimEx_ClaymoreFrag`: exact source pointer, import pair and target export; no fragment behaviour.
- AT Mine ([L237](../../reference-data/provenance/frosty-2026-10-04-L237-atmine-current-continuity.json)): ten historical selected owner, member, import, local and channel relationships retain source continuity. Five owners captured at Head 4909067 are byte-identical to their Head 4892087 inputs. The channel targets remain retained Head 4909002 collection inputs; the independent review also found them byte-identical to raw inputs pinned at Head 4892087. No fresh Head 4909067 channel capture is claimed. Activation, arming, recipients, damage, mine count and lifecycle behaviour remain unproved.
- Deployable Mortar ([mapping receipt](../../reference-data/provenance/frosty-2026-10-04-deployable-mortar-continuity.json)): seven known selection checks retain continuity from WB through VB local objects 1, 48 and 50 to the exact FeatureEx export and its child ResourceRef `20827a2678e50d17`. WB and VB are saved Head 4909002 inputs; FeatureEx was captured at Head 4909067; each equals its own Head 4892087 historical raw input. The ResourceRef stays opaque; no standard-MP admission, placement, ownership, arming, removal, lifecycle operation or runtime behaviour is established.
- Drones: two separate chains; the Recon-to-TRV150 variant join is unproved.
- Proximity: an unknown-role Shot field reaches a SimEx detector dependency; the primary projectile object stays separate.
- T-UGS and Proximity share the declared query-result type; parameter comparison covers eleven current detector values and keeps MTN-55 timing as a comparison clue only.
- Airburst and L154: Equipment, Ability, CUST, WB and a separate PF root reach the lingering and FireRadius exports; no equipment-to-PF bridge.

## Method limits

- **No compiled utility operation reader** was found in the inspected inventory (L190 stays blocked). Repair, supply, revive and regeneration operations are therefore unnamed. The enum and curve readers (L1001, L1002) do not read the utility format. This is a limit of what was inspected, not proof that no reader exists.
- A name, equal scalar, wrapper identity or authored port is insufficient to name an operation.
- UI-to-source number matches (Hemostatic 12.5 and 2.5, MP-APS 3, MTN-55 1 s and 2 s, revive 2.2 s) are consistent with each other, which makes them good questions for a future capture, not controls.

## L3307 - Stored values for every gadget stat entry (9 October 2026)

`Categorization_Gadgets` holds 68 entries. `scripts/frosty-roster-values.py` traced each from its GUID list to its defining object, its carrier files and the damage, blast and projectile fields those files reach, and joined named `GRX_Gadgets_Glacier` rows. 63 entries have a defining object, 60 have own values, 44 have registry rows and 53 have a UI name. Five have no value of any kind: the two underbarrel shotgun entries (`gad_ubsg_buck`, `gad_ubsg_slug`: no saved file contains their GUIDs) and the three underbarrel launcher entries (`gad_ubl_gl_he`, `gad_ubl_gl_smoke`, `gad_ubl_gl_tb`: carried by rifle ability files in the weapon tree, not decoded in this pass).

Evidence class: stored source values with raw-offset checks (11,854 checks over 470 files, all matched, shared with the vehicle rosters). Registry rows are joined by owner name or by a hand-reviewed name table; UI names are a hand name table. None of this shows units or runtime use, and registry defaults are recorded separately from own values.

Per-entry tables, the unresolved list with what was searched, and the open questions with an in-game test for each are in `docs/working/ROSTER_VALUES.md`. Data: `reference-data/frosty/roster-values.json`, `roster-registry-vs-own.json`, `roster-registry-name-joins.json`, `roster-display-names.json`. Receipt: `reference-data/provenance/frosty-2026-10-09-L3307-roster-values.json`.
## L3308 - Lock-on values (9 October 2026)

Every lock-on weapon points at one or more locking controller objects (`Class_9a3efaa2`); 106 such objects sit in 62 saved gadget and vehicle files. Six of their fields are named by equality with registry rows of the same controller: lock time, unlock time, release time, release-on-new-target time, minimum range and ray length. All values are in `reference-data/frosty/locking-controllers.json`; 636 raw-offset checks matched.

| Weapon file | Own objects: lock time / unlock / release / release on new target / ray length / minimum range |
| --- | --- |
| `WB_Stinger` | 1.5 / 0.5 / 1.5 / 1 / 650 / 0 and 1 / 0.5 / 1.5 / 1 / 750 / 0 |
| `WB_IGLA` | 1.8 / 0.5 / 1.5 / 0.1 / 600 / 39 and 1.2 / 0.5 / 1.5 / 0.1 / 800 / 39 |
| `WB_Javelin` | 1.8 / 0.5 / 1.5 / 0.1 / 650 / 39 and 1 / 0.5 / 1.5 / 0.1 / 750 / 39 |
| `WB_MBTLAW` | 3 / -1 / 5 / 0.5 / 650 / 0 |
| `WB_PLD` (laser designator) | 1.2 / -1 / 1 / 1.5 / 750 / 0 and 1.2 / -1 / 1 / 1.5 / 650 / 0; registry primary 1.5 and secondary 1.2 lock time with ray length 750 |
| Fighter air-to-air (`F22`, `SU57`) | 1 / -1 / 0.5 / 1.5 / 800 / 0 and 0.625 / -1 / 0.5 / 1.5 / 800 / 0; registry 665 default and 800 painted, lock time 1 for both |
| Attack helicopter air-to-air | 1.25 / -1 / 0.5 / 1.5 / 800 / 0; registry 650 default and 780 painted |
| Mobile AA missile (`Gepard`) | 1 / -1 / 0.5 / 1 / 800 / 0 and 0.625 / -1 / 0.5 / 1 / 800 / 0; registry 650 default and 780 painted |
| Air-to-ground (`F16`, `JAS39`, `AH64E` gunner) | 0.75 / -1 / 0.5 / 1.5 / 800 / 0; registry equal |
| IFV homing missile (`Bradley`, `CV90`) | 0.75 / -1 / 1.5 / 1 / 800 / 0; registry equal |

The registry also stores `Vehicle_HUD_Locking_PainterPainterMaxDuration` 9, `PLD_World Lock On Time`, `PLD_World Locking Cooldown` and `LockingTimeMultiplier` rows. EA's 1.3.1.0 note of a 20% lock-range bonus on painted targets corresponds to the registry's 650 to 780 pair, and its 20 to 9 second designation change to the stored 9; both are correspondences, not controls.

Open: which object of a pair applies to a painted target; whether a match uses the registry rows or the own objects (they differ only in the ray length of air-to-air default controllers); units; the gadget that owns the registry's `PrimaryLockingController` (1.5, ray length 687.5) and `SecondaryLockingController` (1.4, 550). In-game test: with a Stinger, time the lock tone on a hovering helicopter at a fixed range, unpainted and then laser-painted, and find the longest range at which each locks; 1.5 s against 1 s and a range ratio near 650 to 750 would identify the pair. Receipt: `reference-data/provenance/frosty-2026-10-09-L3308-locking-controllers.json`.

## L3309 - Recon drone, laser designator and sensor spotting values (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3309-spotting-detection.json). Dataset: `reference-data/frosty/registry-spotting-detection.json`. Registry defaults from `GRX_Gadgets_Glacier` (Lancet rows from `GRX_Gadgets_Glacier_CH1_S02`), each read back at its raw offset; meaning is read from the row name, and units and use in a match are unconfirmed. Soldier spotting rows are in [SOLDIER.md](SOLDIER.md).

| Gadget | Rows | Stored defaults |
|---|---|---|
| Recon drone | `Drone_Controlled_Max Spotting Distance_ZoomLevel 0 / 1` | 60 / 160 (uncontrolled rows equal) |
| Recon drone | `Drone_Controlled_Max Spotting Angle_ZoomLevel 0 / 1` | 10 / 5 |
| Recon drone | `Drone_GadgetSpotting_Spotting Radius`, `_Time Intreval` | 40, 1.5 |
| Recon drone | `Drone_Lock On Gadgets Max Distance`, `Max Angle` | 80, 2.5 |
| Recon drone | `Drone_Destroy Gadget Cooldown`, `Lock On Time` | 5, 0 |
| Recon drone | `Drone_MaxLifetime`, `_Granite` | 80, 45 |
| EOD bot | `EODBot_GadgetSpotting_Spotting Radius`, `_Time Intreval`, `EODBot_Max Detection Distance` | 40, 1.5, 40 |
| Laser designator | `PLD_Controlled_Max Spotting Distance_ZoomLevel 0..3` | 80 / 180 / 360 / 540 |
| Laser designator | `PLD_Controlled_Max Spotting Angle_ZoomLevel 0..3` | 10 / 3.75 / 1.875 / 1.25 |
| Laser designator | `PLD_Handheld Spotting Max Distance`, `Angle` | 500, 10 |
| Laser designator | `PLD_*_Soldier / Gadget / Vehicle_SpottingDuration` | 5 / 20 / 30 (handheld and deployed equal) |
| Laser designator | `PLD_SpotVehicleOnLaserPaintProgress` | 0.5 |
| Lancet | `Lancet_HipFire / ZoomLevel1 / ZoomLevel2_Max Detection Distance` | 30 / 60 / 80 |
| Lancet | `Lancet_MaxDetectionRange_UAV`, `Lancet_Spot Duration Of Driver` | 450, 5 |
| T-UGS | `TUGS_Spotting Radius`, `Delay Between Spotting Pulses`, `Spotting Duration` | 15, 1.5, 2 (as recorded earlier) |
| Proximity grenade | `ProximityGrenade_Spotting Radius`, `Delay Between Spotting Pulses`, `Spotting Duration` | 7, 1, 2 |

The laser designator spot durations (5 / 20 / 30) equal the soldier registry's default, gadget and vehicle spot durations.

Open, with the test that would settle each:

- Recon drone range: fly at a stationary enemy and note the distance at which they are marked without zoom (stored 60) and with zoom (stored 160); check whether deployed gadgets are marked within 40 m.
- Laser designator range by zoom level: mark a vehicle at 150 m, 300 m and 500 m at each zoom step.
- Whether the recon drone also uses the `GRX_Characters` cylinder rows: hover above an enemy without aiming at them and note whether they are marked.

## L3310 - Gadget counts, replenish, cooldown and effect rules (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3310-gadget-rules.json). Dataset: `reference-data/frosty/registry-gadget-rules.json` (517 rows, each default read back at its raw offset). Registry defaults from `GRX_Gadgets_Glacier` and `GRX_Gadgets_Glacier_CH1_S02`; own asset values are in L3307. Meaning is read from row names; units and use in a match are unconfirmed.

Ammunition and replenish rows by registry owner (`-1` is stored as written; its meaning is not established):

| Owner | Magazine capacity | Magazines | Initial ammo | Auto replenish magazine | Auto replenish rounds | Auto replenish delay |
|---|---|---|---|---|---|---|
| `AT4_Weapon Blueprint` | 1 | 2 | -1 | true | -1 | 30 |
| `AirburstIncendiary_Weapon Blueprint` | 1 | 3 | -1 | true | -1 | 30 |
| `AntiTankGrenade_WB` | 1 | 2 | -1 | true | -1 | 30 |
| `ConcussionGrenade_WB` | 1 | 1 | -1 | true | -1 | 30 |
| `Defibrillators_Equipped_WB` | 1 | 3 | 3 | true | -1 | 4 |
| `DeployableCover_WB` | 1 | 1 | -1 | true | -1 | 30 |
| `DeployableMortar_WB` | 1 | 1 | -1 | true | -1 | 90 |
| `Drone_Weapon Blueprint` | 1 | 1 | -1 | true | -1 | 30 |
| `Flashbang_WB` | 1 | 1 | -1 | true | -1 | 30 |
| `Gadget_ATMine_WB` | 1 | 3 | -1 | true | -1 | 10 |
| `Gadget_SupplyCrate_WB` | 1 | 1 | -1 | true | -1 | 15 |
| `IncendiaryGrenade_WB` | 1 | 1 | -1 | true | -1 | 30 |
| `Javelin_Weapon Blueprint` | 1 | 3 | -1 | true | -1 | 30 |
| `M18Claymore_WB` | 1 | 1 | -1 | true | -1 | 30 |
| `M4SLAM_WB` | 1 | 3 | -1 | true | -1 | 15 |
| `MBTLAW_Weapon Blueprint` | 1 | 3 | -1 | true | -1 | 18 |
| `MPAPS_WB` | 1 | 1 | -1 | true | -1 | 18 |
| `MiniV40_WB` | 1 | 2 | -1 | true | -1 | 30 |
| `PLD_Controlled_VehicleWeaponComponentData` | 1 | 0 | 0 | false | -1 | 5 |
| `PLD_Handheld_Weapon Blueprint` | 1 | 1 | 1 | true | -1 | 15 |
| `PTKM1R_WB` | 1 | 1 | -1 | true | -1 | 21 |
| `RPG7V2_Weapon Blueprint` | 1 | 3 | -1 | true | -1 | 18 |
| `RepairTool_Weapon Blueprint` | -1 | -1 | -1 | false | -1 | 5 |
| `SmokeGrenade_WB` | 1 | 2 | -1 | true | -1 | 18 |
| `SniperDecoy_WB` | 1 | 3 | -1 | true | -1 | 12 |
| `SpawnBeacon_Weapon Blueprint` | 1 | 1 | -1 | true | -1 | 30 |
| `Stinger_Weapon Blueprint` | 1 | 3 | -1 | true | -1 | 18 |
| `SupplyPouch_WB` | 1 (2.1.1.0: 3) | 3 (2.1.1.0: 1) | -1 | true (2.1.1.0: false) | -1 (2.1.1.0: 1) | 39 |
| `TUGS_Weapon Blueprint` | 1 | 1 | -1 | true | -1 | 30 |
| `ThrowingKnife_WB` | 1 | 5 | -1 | true | -1 | 15 |
| `TracerDart_Weapon Blueprint` | 1 | 3 | -1 | true | -1 | 9 |
| `VB_VEH_DeployableMortar_HE Shell` | 1 | -1 | -1 | false | -1 | 8 |
| `VB_VEH_DeployableMortar_Smoke Shell` | 1 | 3 | 0 | true | -1 | 45 |
| `WB_AdrenalineShot` | 1 | 1 | -1 | true | -1 | 45 |
| `WB_C4` | 1 | 4 | -1 | true | -1 | 30 |
| `WB_M26Mass` | 5 | 2 | -1 | true | -1 | 60 |
| `WB_VehicleSupplyCrate` | 1 | 1 | -1 | true | -1 | 120 |
| `X95BRE_BreachingDart` | 1 | 3 | -1 | true | -1 | 15 |

Ability rows: `Ability_AdrenalineShot` active 1, recharge 0; `DeployableCover_Ability` active 1, recharge 0; `DeployableMortar_Ability` active 1, recharge 0; `Gadget_ATMine_Ability` active 1.8, recharge 0; `Gadget_SupplyCrate_Ability` active 1, recharge 0; `MPAPS_Ability` active 0, recharge 20.

Effect rules (flat rows):

| Topic | Stored defaults |
|---|---|
| Grenade fuse | Frag and default: minimum time before detonation 1.1, delay after bounce 1.4 (2.1.1.0, frag: 1.1). Concussion: 0.7 and 0.4. Flashbang: 1.1 and 1.4. |
| Flash and stun | Flashbang, M320 flash and stun drill store the same rows: duration in front 3.5 close / 2.5 far, sides 1.5 / 1.0, behind 0.6 / 0.2; close range 6, max range 12; angle in front 60, sides 90. |
| Concussion grenade | Duration 3.5 within 5, 2.5 within 7, 1.5 within 9. |
| Incendiary | Grenade radius 1.7, height 1.0; `Fire damage duration` 2.5; thermobaric fire damage duration 4.0. |
| Repair tool | Repair 40 per second (active 60), anti-repair 30 (active 45), interval 0.1, range 2. EOD bot: repair 40 (active 75), anti-repair 30 (active 45), range 3.2. |
| Defibrillator | Charge time minimum 0.3, time to full charge 1.0; max range friendly 2.0, enemy 1.5. |
| Supply | Supply pouch health regeneration 25 for 4; supply crate open 0.4; vehicle supply crate 15 supplies, resupply interval 5, construct 0.6. |
| Adrenaline | Duration 8, rank 5. |
| C-4 | Arm delay 0.5. |

Open, with the test that would settle each:

- Carried counts and which side is live: count a gadget's items on spawn and compare with the stored magazines and capacity.
- Replenish: use all of a gadget away from any supply source and time the return of each item (stored delay, for example 30 for the AT4 and 18 for the RPG-7V2).
- Flash duration by angle and range: time the white-out at 5 m and 10 m facing, side-on and facing away.
- Repair rate: time a repair of a tank from a known health to full.
- Grenade fuse: time a frag from release to detonation with and without a bounce.

## L3315 - Healing and ammunition supply effects (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3315-resistance-heal-ammo-effects.json). Dataset: `reference-data/frosty/effect-resistance-heal-ammo.json`. Every saved object of the healing effect class (`Class_1486fe7f`, seven objects) and the ammunition supply effect class (`Class_42da642c`, 17 objects) was read, each scalar checked at its raw offset. Flak effects from the same lead are in [SOLDIER.md](SOLDIER.md).

Healing. `Field_77f58095` and `Field_3202ac10` are named InitialHeal and HealOverTime by a stored link: the vehicle medbay effect fills them from the registry rows `Passives_Vehicles_Medbay_InitialHeal` and `Passives_Vehicles_Medbay_HealOverTime`. `Field_8bba458c` is unnamed.

| Effect file | InitialHeal | HealOverTime | `Field_8bba458c` |
|---|---|---|---|
| `Affector_Healing_SupplyPouch` | 0 | 20 | 2.5 |
| `Affector_Healing_MedicCrate` | 0 | 20 | 2.5 |
| `Affector_Healing_MedicalTriage` | 0 | 20 | 1.0 |
| `Affector_EmergencyDamageControl_ExtraHeal` | registry `EmergencyDamageControl_ExtraHealingAmount` (50) | 70 | 2.0 |
| `Affector_VEH_PassiveAbility_Medbay_Heal` | registry (5) | registry (20) | 2.5 |
| `Affector_SelfHeal_AdrenalineShot` | 0 | 5, 10, 12.5, 15, 17.5, 20 and further ranks | 0 |
| `Affector_RepairTool_HealVehicle` | 2.5, 5, 7.5, 10, 12.5, 15 and further ranks | 0 | 0 |

Ammunition supply. No field of this class is named. The stored values that differ between effects:

| Effect file | `Field_2e02f8ac` | `Field_5b881d59` | `Field_f502de34` | `Field_89e9d098` |
|---|---|---|---|---|
| `Affector_Ammunition_Rifle_AmmoCrate`, `_MG_`, `_PDWPistol_` | 0 | 1 | 20 | 1 |
| `Affector_Ammunition_BoltDMR_AmmoCrate`, `_Shotgun_` | 0 | 1 | 5 | 1 |
| `Affector_Ammunition_AmmoCrate` (entry 0) | 1 | 1 | 0 | 1 |
| `Affector_Ammunition_SupplyPouch` (entries 0, 1, 2) | 0 | 2, 3, 4 | 0 | 1 |
| `Affector_LethalGadgets_AmmoCrate` | 1 | 0 | 0 | 1 |
| `Affector_VehicleSupplyCrate_Ammo` | 1 | 0 | 0 | 0.8 |

Open, with the test that would settle each:

- The unnamed healing field (2.5 or 1.0): stand on a medic crate at 50 health and record health per second and any delay before it starts.
- The ammunition integer (5 or 20): stand on a supply crate with an empty rifle reserve and with an empty shotgun reserve and count rounds gained per supply tick.
- The supply pouch values 2, 3, 4: pick up a pouch with each weapon class empty and count magazines gained.

## L3332 - Blast radius fields, and radii for launchers, C-4 and mines (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3332-explosion-radius-fields.json). Dataset: `reference-data/frosty/explosion-radius-fields.json`. The soldier damage table of L3329 (`SOLDIER.md`) had no radius for weapons without a registry row. Three fields of the explosion object (`Class_9966532d`) are named here by comparing them with the registry rows of the 19 owners that have them:

| Field | Name | Agrees with the registry row |
|---|---|---|
| `Field_33f3a8ab` | BlastRadius | 14 of 19 owners |
| `Field_95e340fe` | InnerBlastRadius | 17 of 19 owners |
| `Field_524836d3` | ShockwaveRadius | 19 of 19 owners |

All 7 exceptions are pairs already recorded as disputed, where the registry was changed and the asset kept the older value (L3318, L3324). The naming rests on value agreement, not on a stored name link.

The asset's own values for the weapons with no registry radius row, in metres:

| Item | Owner | Blast radius | Inner blast radius | Shockwave radius |
|---|---|---|---|---|
| IFV MPLD round (no EA figure) | `PD_Vehicles_IFV_PrimaryWeapon_MPLD` | 5 | 1 | 10 |
| M136 AT | `PB_AT4` | 5 | 2 | 7.5 |
| MBT-LAW | `PB_MBTLAW` | 4 | 1 | 6.5 |
| 9K93 IGLA | `PB_NS_IGLA` | 5 | 1 | 7.5 |
| SLM-93A | `PB_NS_Stinger` | 5 | 1 | 7.5 |
| C-4 | `PNS_C4` | 3 | 1 | 5 |
| M4A1 SLAM (body) | `PB_M4SLAM` | 1 | 0.99 | 3.5 |
| EOD Bot mine | `PB_NS_EODBot_Mines` | 2 | 1.99 | 4.5 |
| PTKM-1R | `PB_PRJ_PTKM1R_EFP` | 4 | 3.99 | 8 |

The mines store an inner radius just below the radius, which reads as full damage across the whole radius (inference). No field was found for the minimum blast damage. 141 raw-offset checks matched.

Still open, with the test that would settle each:

- Radii in game. Detonate C-4 with a teammate at 2.5 m and at 3.5 m: damage at 2.5 m only confirms the radius 3.
- Minimum blast damage. A tank HE shell at 4.9 m from a soldier: 20 means the stored minimum applies at the edge.
- Shockwave radius. Stand 7 m from an RPG impact (between the radius 6 and the shockwave radius 8.5) and note any effect.

## L3333 - C-4: the registry row PB_C4 is bound to nothing (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3333-c4-registry-row-orphan.json). L3327 left open whether C-4 uses the asset's own BlastDamage 100 or the registry row `PB_C4...BlastDamage` 180. Stored data settles it:

- The build's asset catalog has no file named `PB_C4`. The C-4 folder holds `PNS_C4` and its presentation and logic files only.
- The C-4 weapon file `WB_C4` imports `PNS_C4` (by file GUID). `PNS_C4` imports no registry row.
- For comparison, `PB_NS_RPG` imports 7 registry rows and `PB_M4SLAM_EFP` 6, each under its own owner name; `PB_AT4`, `PB_MBTLAW` and `PB_M4SLAM` import none.

So the `PB_C4` rows are leftovers bound to no saved file, and C-4's stored damage is 100 (350 against tanks, L3327). The same check separates the two groups seen so far: projectiles that import their registry rows follow the registry, and projectiles that import none use their own values. 7 raw-offset checks matched.

Still open, with the test that would settle each:

- One C-4 pack on a full-health tank: 350 expected; 630 would mean the orphan row is used.
- Other orphan registry owners were not surveyed.

## L3340 - Stored blast falloff curves (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3340-blast-falloff-curves.json). Dataset: `reference-data/frosty/blast-falloff-curves.json`. Six curve files hold the shape of blast damage with distance. The explosion object points at one through `Field_0839b22b`. x is distance as a fraction of the blast radius; y is the fraction of blast damage.

| Curve file | Points (x, y) | Imported by |
|---|---|---|
| `Javelin_BlastDamageFallOffCurve` | (0, 1), (0.125, 1), (0.125, 0.67), (0.33, 0.67), (0.33, 0.33) | `PB_Javelin` |
| `BlastCurve_C4` | (0, 1), (0.599, 0.9958), (0.6, 0.8), (0.758, 0.8), (0.761, 0.4063), (0.9026, 0.4021), (0.9036, 0.2), (1, 0.2) | `PD_Railgun`, `VB_VEH_SP_Drone_Payload_Gameplay`, `VB_VEH_Drone_Payload`, `PNS_C4` |
| `FragGrenade_BlastDamageFalloff_Curve` | (0, 1), (0.2, 1), (0.6, 0.8), (0.601, 0.6), (0.799, 0.4), (0.8, 0.2), (1, 0.2) | `PB_NS_EODBot_ClusterCharge_Submunition`, `PBNS_FragGrenade`, `PBNS_SP_Player_FragGrenade` |
| `BlastCurve_Vehicles_InnerRadius25` | (0.25, 1), (0.9, 0.2) | `PB_Vehicle_AGL_Grenade`, `PD_Vehicles_IFV_PrimaryWeapon_HEAB`, `PD_Vehicles_IFV_SecondaryWeapon_LightRockets`, `PD_Vehicles_MBT_AmmoTypes_MPAT` |
| `BlastCurve_Vehicles_InnerRadius40` | (0.4, 1), (0.9, 0.2) | `PD_Vehicles_MBT_AmmoTypes_HE` |
| `BlastCurve_Vehicles_InnerRadius50` | (0.5, 1), (0.9, 0.2) | `PB_Missile_AGM84`, `PB_Missile_TOW2B`, `PB_Missile_TOW2B_AirVehicle`, `PB_Missile_TOW2B_SP`, `PB_NS_Missile_AA_Secondary_AimGuided`, `PB_NS_Missile_AA_Secondary_HighVelocity` |

How the axes were named: the frag grenade's own inner radius (1 m) is 0.2 of its radius (5 m) and its curve leaves full damage at x = 0.2; the vehicle curves are named InnerRadius25, 40 and 50 and start at 0.25, 0.4 and 0.5; all three end at 0.2 of damage, the 20% minimum EA announced in [1.3.1.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) (L3337).

In metres, with straight lines between points:

| Explosive | Blast damage | Radius | Damage by distance |
|---|---|---|---|
| Frag grenade | 100 | 5 m | 100 to 1 m; falls to 80 at 3 m; 60 at 3 m falling to 40 at 4 m; 20 from 4 m to 5 m |
| C-4 | 100 | 3 m | 100 to 1.8 m; 80 to 2.27 m; about 40 to 2.71 m; 20 to 3 m |
| MAS 148 Glaive | 155 (registry) | 4 m | full to 0.5 m; 67% to 1.32 m; 33% beyond |
| HEAT-MP-T shell | 100 | 5 m (registry) | full to 1.25 m; falls to 20 at 4.5 m; 20 to 5 m |
| HEMP-T shell | 100 (registry) | 5 m | full to 2 m by the curve (registry inner radius 2.25); falls to 20 at 4.5 m |

- **EA's HEAT-MP-T lethal radius comes from the curve.** 0.25 x 5 m = 1.25 m, the figure in [1.3.3.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-3-0); the `InnerBlastRadius` row holds 1.0 (L3337).
- 9 of the 10 owners with a non-zero `MinimumBlastDamage` row import a vehicle curve.
- No curve: `PBNS_ATMine`, `PBNS_AntiTankGrenade`, `PBNS_M720A1`, `PB_AT4`, `PB_ATGM_Homing_Spike`, `PB_Bomb_GBU39`, `PB_Bomb_Mk82AIR`, `PB_M4SLAM`, `PB_MBTLAW`, `PB_Missile_AGM114_Hellfire`, `PB_Missile_MBT_GuidedMunition`, `PB_NS_EODBot_Mines`, `PB_NS_IGLA`, `PB_NS_M320HE`, `PB_NS_M320Thermobaric`, `PB_NS_RPG`, `PB_NS_Stinger`, `PB_PRJ_PTKM1R_EFP`, `PD_M26Mass12Frag`, `PD_Vehicles_IFV_PrimaryWeapon_MPLD`, `PRJ_Missile_AGM65_Maverick`, `PRJ_Missile_APKWS-II`, `PRJ_Missile_Hydra70`, `PRJ_Missile_Zuni`, `WF_Vehicles_AttackHeli_Passenger_PrimaryWeapon_Chaingun`. Their falloff shape is not stored here.
- Each point also stores a mode and tangents that were not interpreted.

106 raw-offset checks matched.

Still open, with the test that would settle each:

- HEMP-T full-damage distance (2 m by curve, 2.25 m by inner radius). A shell landing 2.1 m from a full-health soldier without flak: a kill means 2.25.
- Frag grenade steps. A grenade exploding 3.5 m from a full-health soldier without flak should deal about 50; at 4.5 m, 20.

## L3342 - Grenades, 40 mm grenades and the mortar shell against soldiers and vehicles (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3342-grenade-and-mortar-damage.json). Dataset: `reference-data/frosty/grenade-and-mortar-damage.json`. Full blast damage = blast damage x grid value of the explosion's material against the target. The registry default is used where a row exists; the own value is shown when it differs. Names are joined to files by name only, and none of these has an EA figure.

| Item | File | Blast damage | Inner / blast radius (m) | Soldier body | Tanks, IFVs (119) | Helicopters (121) | Jets (120) | Flyer, Vector, RHIB (122) | Quad, bikes (187) |
|---|---|---|---|---|---|---|---|---|---|
| Frag grenade | `PBNS_FragGrenade` | 100 | 1 / 5 | 100 | 0 | 100 | 100 | 100 | 100 |
| 40 mm HE grenade (M320) | `PB_NS_M320HE` | 120 | 1 / 5 | 120 | 6 | 96 | 96 | 96 | 96 |
| 40 mm thermobaric grenade (M320) | `PB_NS_M320Thermobaric` | 50 (own 30) | 2 / 3 | 50 | 2.5 | 20 | 20 | 10 | 10 |
| Anti-tank grenade | `PBNS_AntiTankGrenade` | 50 | 0.75 / 1.5 | 42.5 | 150 | 325 | 500 | 350 | 350 |
| Mortar HE shell (M720A1) | `PBNS_M720A1` | 60 | 2.444 / 7.622 | 60 | 0 | 60 | 60 | 60 | 60 |

- The frag grenade and the mortar blast do nothing to armoured vehicles but full damage to aircraft and light vehicles.
- The anti-tank grenade's blast material has the same values against tanks, helicopters and jets as the Glaive's (L3339): 150 to a tank, of 1200.
- Mortar HE direct hit: material 167, registry Damage 100 (own 200), value 1 on armour, 7 on aircraft, 4.5 and 11 on light vehicles.
- The hand and 40 mm grenades' impact objects have a material but no damage field.
- Falloff with distance: the frag grenade has a stored curve (L3340); the others have none.

4346 raw-offset checks matched.

Tests that would check these:

- One anti-tank grenade on a full-health tank: 150 removed.
- One thermobaric grenade at a soldier's feet: 50 (registry) or 30 (own).
- One frag grenade under a landed helicopter: 100 removed.

## L3343 - Launcher missile speed, lock time and lock range against EA (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3343-launcher-speed-and-lock-values.json). Dataset: `reference-data/frosty/launcher-speed-and-lock-values.json`. EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) give speeds, accelerations, lock times and one lock range for the launchers. Names are joined to files by name only. A Haiku worker proposed candidate fields; each value here was re-read by script.

Missile object (`Class_6a25e89d`): `Field_1a2b6380` is MaxSpeed and `Field_0f6601e1` is EngineStrength, named by the files where a registry row of that name holds the same number.

| Item | File | Max speed own | Max speed registry | EA max speed | Equal to EA's new | Engine strength own | EA acceleration | Equal |
|---|---|---|---|---|---|---|---|---|
| MBT-LAW | `PB_MBTLAW` | 300 | none | 75 to 300 | yes | 100 | 50 to 100 | yes |
| MAS 148 Glaive | `PB_Javelin` | 60 | 70 | 60 to 70 | yes | 40 | not stated | - |
| Attack helicopter TOW | `PB_Missile_TOW2B_AirVehicle` | 90 | 120 | 90 to 120 | yes | 50 | not stated | - |
| Ground vehicle TOW | `PB_Missile_TOW2B` | 150 | 90 | remains 90 | yes | 50 | not stated | - |
| 9K93 IGLA | `PB_NS_IGLA` | 640 | none | 640 to 480 | no | 65 | 65 to 100 | no |
| SLM-93A | `PB_NS_Stinger` | 400 | none | 540 to 480 | no | 50 | not stated | - |
| SLM-93A (second file) | `PB_Stinger` | 350 | none | 540 to 480 | no | 200 | not stated | - |
| Stinger, vehicle file | `PBNS_Stinger_Vehicle` | 540 | 540 | 540 to 480 | no | 65 | not stated | - |

Weapon file: lock time is `Field_1351d684` in `Class_a4fe2c96`; lock range is `Field_f41246df` in `Class_6191fd53` (two objects, two ranges).

| Item | File | Lock time (s) | EA lock time | Lock ranges (m) | Ratio | EA base range |
|---|---|---|---|---|---|---|
| 9K93 IGLA | `WB_IGLA` | 1 | 1.2 to 1 | 840 and 700 | 1.2 | not stated |
| MAS 148 Glaive | `WB_Javelin` | 1.4 | 1.8 to 1.4 | 650 and 780 | 1.2 | not stated |
| SLM-93A | `WB_Stinger` | 1.5 | not stated | 550 and 687.5 | 1.25 | 650 to 550 |
| MBT-LAW | `WB_MBTLAW` | 3 | not stated | 650 | - | not stated |

- EA's "missile acceleration" is EngineStrength.
- **IGLA and SLM-93A speeds are not updated in these files.** The IGLA stores 640 and 65, EA's old values; no file stores 480.
- The two lock ranges differ by 1.2 for the IGLA and Glaive, EA's "consistent 20%" laser designator bonus, but by 1.25 for the SLM-93A.
- Tank active protection: `Ability_MBT_ActiveProtectionSystem` `Field_85c11a9b` = 0.55, the activation time in [1.3.3.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-3-0). The same object stores 32 (registry RechargeTime 32) and 4.0 (registry ActiveTime 5.0).

55 raw-offset checks matched.

Still open, with the test that would settle each:

- IGLA and SLM-93A missile speed: time a missile over a known distance.
- SLM-93A designated lock range: try to lock a designated helicopter at 675 m (possible if 687.5, not if 660).
- Active protection window: 4 s or 5 s.

## L3352 - Gadget registry rows not recorded before (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3352-gadget-registry-global-rows.json). Dataset: `reference-data/frosty/gadget-registry-global-rows.json`. `GRX_Gadgets_Glacier` has 276 rows without an owner prefix; 187 of them were not named anywhere in the docs. All are in the dataset with default, minimum and maximum. These are registry defaults: the row name is the only description, units are implied by the name, and nothing here shows which mode reads a row.

Rows matching `Damage / Radius / Health / Heal / Cooldown / Duration / Range / Resupply / Regen / Charges / MaxCount / Limit` (52 of 187):

| Row | Default | Min | Max |
|---|---|---|---|
| `BaseDamage` | 2 | 1 | 9 |
| `Defibrillators_PeepholeRadius` | 0 | 0 | 10 |
| `Defibrillators_SP_Max Range` | 4 | 0 | 10 |
| `Drone_NearbyProjectile_Explosive Trigger Range` | 0.5 | 0.5 | 5 |
| `Drone_RangeFinder Max Distance` | 1000 | 0 | 10000 |
| `DroneMovement_Initial Upward Momentum Duration` | 1.5 | 0 | 3 |
| `EIDOS_Max Intercept Range` | 5 | 0 | 20 |
| `EODBot_Apply Damage/ Repair Interval` | 0.1 | 0.01 | 1 |
| `EODBot_BR_Damage Vehicle Rank` | 5 | 0 | 6 |
| `EODBot_Damage Vehicle Rank` | 3 | 0 | 6 |
| `EODBot_Repair_Range` | 3.2 | 0 | 10 |
| `Fire Radius` | 2.2 | 0.1 | 5 |
| `FirePutOut_Duration` | 1 | 0 | 1.5 |
| `Flashbang_Duration_Sides_Close` | 1.5 | 0 | 10 |
| `Flashbang_Duration_Sides_Far` | 1 | 0 | 10 |
| `Flashbang_Max Range` | 12 | 0 | 30 |
| `FumigatorHealthGate` | 0.35 | 0 | 0 |
| `GasDealsDamage` | True | none | none |
| `M26Dragon_MaxDistanceAffectorsLowDamage` | 20 | 0 | 30 |
| `M320_AT_Thermite Affector Duration` | 3.5 | 0 | 5 |
| `M320_Flash_Close Range` | 6 | 0 | 30 |
| `M320_Flash_Duration_Behind_Close` | 0.6 | 0 | 10 |
| `M320_Flash_Duration_Behind_Far` | 0.2 | 0 | 10 |
| `M320_Flash_Duration_Infront_Close` | 3.5 | 0 | 10 |
| `M320_Flash_Duration_Infront_Far` | 2.5 | 0 | 10 |
| `M320_Flash_Duration_Sides_Close` | 1.5 | 0 | 10 |
| `M320_Flash_Duration_Sides_Far` | 1 | 0 | 10 |
| `M320_Flash_Max Range` | 12 | 0 | 30 |
| `M320_LVG_BlastRadius` | 3.5 | 2 | 5 |
| `M320_Thermobaric_Incendiary Radius` | 1 | 0 | 10 |
| `PelletLimit` | 25 | 4 | 700 |
| `PLD_Deployed_Controlled_Gadget_SpottingDuration` | 20 | 0 | 30 |
| `PLD_Deployed_Controlled_Soldier_SpottingDuration` | 5 | 0 | 30 |
| `PLD_Deployed_Controlled_Vehicle_SpottingDuration` | 30 | 0 | 30 |
| `PLD_Deployed_Uncontrolled_Gadget_SpottingDuration` | 20 | 0 | 30 |
| `PLD_Deployed_Uncontrolled_Soldier_SpottingDuration` | 5 | 0 | 30 |
| `PLD_Deployed_Uncontrolled_Vehicle_SpottingDuration` | 30 | 0 | 30 |
| `PLD_Handheld_Gadget_SpottingDuration` | 20 | 0 | 30 |
| `PLD_Handheld_Soldier_SpottingDuration` | 5 | 0 | 30 |
| `PLD_Handheld_Vehicle_SpottingDuration` | 30 | 0 | 30 |
| `ProximityGrenade_Spotting Duration` | 2 | 0.5 | 12 |
| `ProximityGrenade_Spotting Radius_GraniteMulti` | 2.14 | 0 | 10 |
| `StunDrill _Duration_Behind_Close` | 0.6 | 0 | 10 |
| `StunDrill _Duration_Behind_Far` | 0.2 | 0 | 10 |
| `StunDrill _Duration_Infront_Close` | 3.5 | 0 | 10 |
| `StunDrill _Duration_Infront_Far` | 2.5 | 0 | 10 |
| `StunDrill _Duration_Sides_Close` | 1.5 | 0 | 10 |
| `StunDrill _Duration_Sides_Far` | 1 | 0 | 10 |
| `StunDrill_Close Range` | 6 | 0 | 30 |
| `StunDrill_Max Range` | 12 | 0 | 30 |
| `SupplyCrate_OpenCrateDuration` | 0.4 | 0 | 2 |
| `VSC_Resupply Neutral Vehicles Max Time` | 15 | 0 | 30 |

187 raw-offset checks matched.

## L3353 - Repair Tool and EOD Bot repair rows (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3353-repair-rate-rows.json). Registry defaults, by exact row name:

| Tool | State | Repair amount per second | Anti-repair amount per second |
|---|---|---|---|
| Repair Tool | standard | 40 | 30 |
| Repair Tool | active repair | 60 | 45 |
| Repair Tool | battle royale | 30 | 15 |
| Repair Tool | battle royale, active repair | 60 | 30 |
| EOD Bot | standard | 40 | 30 |
| EOD Bot | active repair | 75 | 45 |
| EOD Bot | battle royale | 30 | 15 |
| EOD Bot | battle royale, active repair | 60 | 30 |

Related rows: tool range 2 m, bot range 3.2 m, apply interval 0.1 s for both, `Repair Exhaustion Recovery Rate` 6, `VehicleRepairedAmount_AccumulatorTime` 2.

If the amount is health per second on the vehicle's own scale (not verified; see the note in the repair table above on this page):

| Vehicle | Root health | Seconds from 0 to full at 40 | at 60 | Own regeneration per second (L3346) |
|---|---|---|---|---|
| Tank (Abrams, Leopard) | 1200 | 30 | 20 | 120 |
| IFV, anti-air, helicopters, jets | 1000 | 25 | 16.6667 | 100 |
| Armoured transport (JLTV, Marauder) | 800 | 20 | 13.3333 | 80 |

A standard repair at 40 would then be a third of a tank's own regeneration rate, which is a reason to doubt the plain reading. 23 raw-offset checks matched.

Test: repair a tank from a known health for exactly 10 s; 400 gained means 40 health per second.

## L3366 - Claymore fragmentation damage 50 (9 October 2026)

**Withdrawn in L3367 below: the value 50 is shared by other gadgets and is not the Claymore's damage.**

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3366-claymore-fragment-damage-50.json). EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0): Claymore fragmentation base close-range damage 65 to 50. The blast object holds BlastDamage 1 (L164), so the figure is elsewhere: `M18Claymore_Projectile` has a property list (`Class_1788e77e`) of name-hash and value pairs with three floats:

| Name hash | Value |
|---|---|
| `2b715869` | 30 |
| `2b71592f` | 50 |
| `2b7158ae` | 15 |

The 50 equals EA's figure. The names are hashes of one family; what 30 and 15 mean is not read. No registry row is named for Claymore damage. 3 raw-offset checks matched.

Test: health lost to an enemy Claymore at 1 m and at the edge of its range.

## L3367 - Correction: the Claymore's 50 is a shared value, not its damage (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3367-claymore-50-shared-default.json). L3366 above is withdrawn. The same three values under the same name hashes (30, 50, 15) are in 8 gadget projectile files, among them `PBNS_ATMine`, `PB_M4SLAM`, `PB_NS_EODBot_Mines`, `PBNS_MobileJammer` and `PBNS_ProximityGrenade`. A value shared by mines, a jammer and a sensor grenade is not a damage figure; the match with EA's Claymore figure was a coincidence.

The Claymore's fragmentation damage (EA: 50) is not located in stored data: blast object BlastDamage 1, no registry row, no file-specific value. 4 raw-offset checks matched.

Test: health lost to an enemy Claymore at 1 m.

## L3375 - Portable Mortar firing profile (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3375-portable-mortar-profile.json). Dataset: `reference-data/frosty/portable-mortar-profile.json`. Registry defaults (own values not read):

| Registry row | Default |
|---|---|
| `VB_VEH_DeployableMortar_HE Shell.WeaponFiring.PrimaryFire.Shot.InitialSpeed.y` | 48.3 |
| `VB_VEH_DeployableMortar_HE Shell.WeaponFiring.PrimaryFire.Shot.InitialSpeed.z` | 31.37 |
| `VB_VEH_DeployableMortar_HE Shell.WeaponFiring.PrimaryFire.FireLogic.ReloadInfoArray[0].ReloadTime` | 2.65 |
| `VB_VEH_DeployableMortar_HE Shell.WeaponFiring.PrimaryFire.OverHeat.HeatPerBullet` | 0.03 |
| `VB_VEH_DeployableMortar_HE Shell.WeaponFiring.PrimaryFire.OverHeat.HeatDropPerSecond` | 0.25 |
| `VB_VEH_DeployableMortar_HE Shell.WeaponFiring.PrimaryFire.Ammo.MagazineCapacity` | 1 |
| `VB_VEH_DeployableMortar_HE Shell.WeaponFiring.PrimaryFire.Ammo.NumberOfMagazines` | -1 |
| `VB_VEH_DeployableMortar_HE Shell.WeaponFiring.PrimaryFire.Ammo.AutoReplenishDelay` | 8 |
| `VB_VEH_DeployableMortar_HE Shell.WeaponFiring.PrimaryFire.Ammo.AutoReplenishMagazine` | 0 |
| `VB_VEH_DeployableMortar_Smoke Shell.WeaponFiring.PrimaryFire.Shot.InitialSpeed.y` | 48.3 |
| `VB_VEH_DeployableMortar_Smoke Shell.WeaponFiring.PrimaryFire.Shot.InitialSpeed.z` | 31.37 |
| `VB_VEH_DeployableMortar_Smoke Shell.WeaponFiring.PrimaryFire.FireLogic.ReloadInfoArray[0].ReloadTime` | 2.65 |
| `VB_VEH_DeployableMortar_Smoke Shell.WeaponFiring.PrimaryFire.OverHeat.HeatPerBullet` | 0.03 |
| `VB_VEH_DeployableMortar_Smoke Shell.WeaponFiring.PrimaryFire.OverHeat.HeatDropPerSecond` | 0.25 |
| `VB_VEH_DeployableMortar_Smoke Shell.WeaponFiring.PrimaryFire.Ammo.MagazineCapacity` | 1 |
| `VB_VEH_DeployableMortar_Smoke Shell.WeaponFiring.PrimaryFire.Ammo.NumberOfMagazines` | 3 |
| `VB_VEH_DeployableMortar_Smoke Shell.WeaponFiring.PrimaryFire.Ammo.AutoReplenishDelay` | 45 |
| `VB_VEH_DeployableMortar_Smoke Shell.WeaponFiring.PrimaryFire.Ammo.AutoReplenishMagazine` | 1 |
| `DeployableMortar_WB.WeaponEntityData.WeaponFiring.PrimaryFire.Ammo.AutoReplenishDelay` | 90 |
| `DeployableMortar_WB.WeaponEntityData.WeaponFiring.PrimaryFire.Ammo.MagazineCapacity` | 1 |
| `DeployableMortar_WB.WeaponEntityData.WeaponFiring.PrimaryFire.Ammo.NumberOfMagazines` | 1 |
| `VB_VEH_DeployableMortar.MaxHealth` | 50 |
| `VB_VEH_DeployableMortar.RegenerationRate` | 0 |
| `ArtilleryMasteryMortarReload` | 0.75 |
| `SupplyCratePlusMortarReload` | 0.835 |
| `Mortar_Supply Crate Reload` | 0.623 |

Arithmetic on these (inference):

- Launch speed 57.6 m/s at 57.0 degrees; about 309 m with no drag and gravity 9.81 (upper estimate).
- Reload 2.65 s; with the multipliers 1.99 s (0.75), 2.21 s (0.835) or 1.65 s (0.623). Which multiplier applies when is not read.
- Heat 0.03 per shell against 0.25 per second cooling: no practical overheat.

Shell damage is in L3342. 26 raw-offset checks matched.

Test: time the gap between two shells with and without a Supply Crate nearby.

## L3376 - Launcher and gadget reload times (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3376-gadget-launcher-reload-times.json). Dataset: `reference-data/frosty/gadget-reload-times.json`. Own reload entries of the gadget weapon files, with the registry default where a row exists (file and registry owner joined by name):

| Weapon file | Own reload time | Own reload time, rounds left | Registry default |
|---|---|---|---|
| `WB_RPG7V2` | 3.4 | -1 | 3.4 |
| `WB_Stinger` | 3.4 | 3.66 | 3.4 |
| `WB_MBTLAW` | 3.4 | -1 | 3.4 |
| `WB_AT4` | 3.66 | 3.66 | 3.66 |
| `WB_Javelin` | -1 | -1 | -1 |
| `WB_TracerDart` | 3.38 | 3.38 | 3.38 |
| `WB_RepairTool` | 3.59 | -1 | 3.59 |
| `WB_M26Mass` | 3.53 | 3 | 3.53 |
| `WB_AirburstIncendiary` | 2.53 | 2.53 | 2.53 |
| `WB_IGLA` | 3.4 | 2.33 | no row |
| `WB_Panzerfaust3` | 4.96 | 4.96 | no row |
| `DrillGL_WB` | 2.53 | 2.53 | no row |
| `Railgun_WB` | 4.266 | -1 | no row |
| `Minigun_WB` | 6.7 | 5.83 | no row |
| `Lancet_WB` | 3.233 | -1 | no row |
| `SupplyDrop_WB` | 3.6 | -1 | no row |
| `KineticStrike_WB` | 20 | 20 | no row |

- All nine with a registry row agree with it.
- Javelin: -1 in both, no timed reload stored.
- Rounds-left value differs for the Stinger, IGLA, M26 MASS and Minigun; which applies to a one-round launcher is not shown.
- EA's notes state no launcher reload time.

43 raw-offset checks matched.

Test: time one RPG-7V2 reload and one Stinger reload.

## L3377 - Railgun and Panzerfaust 3 under the damage rule (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3377-railgun-panzerfaust3-damage-rule.json). Dataset: `reference-data/frosty/railgun-panzerfaust3-damage.json`. Stored damage times the grid value for each target (before the hit factor of L3323 for aimed hits):

| File | Part | Material | Stored damage | tank / IFV | helicopter | jet | light vehicle | quad / bike | soldier chest | soldier stomach |
|---|---|---|---|---|---|---|---|---|---|---|
| `PD_Railgun` | blast | 679 | 0 | 0 (x0) | 0 (x0) | 0 (x0) | 0 (x0) | 0 (x0) | 0 (x0) | 0 (x0) |
| `PD_Railgun` | direct | 678 | 150 | 375 (x2.5) | 525 (x3.5) | 525 (x3.5) | 825 (x5.5) | 1350 (x9) | 150 (x1) | 150 (x1) |
| `PB_Panzerfaust3` | direct | 125 | 100 (file only) | 200 (x2) | 900 (x9) | 1000 (x10) | 550 (x5.5) | 500 (x5) | 100 (x1) | 100 (x1) |
| `PB_Panzerfaust3` | blast | 164 | 130 (file only) | 0 (x0) | 0 (x0) | 0 (x0) | 39 (x0.3) | 1105 (x8.5) | 130 (x1) | 130 (x1) |
| `PB_Panzerfaust3_DM32` | direct | 167 | 100 (file only) | 100 (x1) | 700 (x7) | 700 (x7) | 450 (x4.5) | 1100 (x11) | 100 (x1) | 100 (x1) |
| `PB_Panzerfaust3_DM32` | blast | 164 | 230 (file only) | 0 (x0) | 0 (x0) | 0 (x0) | 69 (x0.3) | 1955 (x8.5) | 230 (x1) | 230 (x1) |

- Railgun registry rows: speed 1029 m/s, magazine 1, magazines 11, reload 4.266 s, falloff 100 to 200 m with 150 at both ends.
- Panzerfaust 3 shares material 125 with the RPG (registry damage 125). Its 100 is a file-only value and may be stale.

2089 raw-offset checks matched.

Test: one Railgun hit on a tank's rear (750 expected) and one Panzerfaust 3 hit on a tank's side (300 expected).

## L3378 - Call-in strike munitions under the damage rule (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3378-call-in-strike-munitions-damage-rule.json). Dataset: `reference-data/frosty/call-in-strike-munitions.json`. File damage times the grid value for each target. None of these has a registry damage row, so the values may be stale (L3343):

| File | Part | Material | File damage | tank / IFV | helicopter | light vehicle | soldier chest |
|---|---|---|---|---|---|---|---|
| `PB_PRJ_Missile_AGM179_JAGM` | direct | 125 | 175 | 350 (x2) | 1575 (x9) | 962.5 (x5.5) | 175 (x1) |
| `PB_PRJ_Missile_AGM179_JAGM` | blast | 206 | 160 | 347.2 (x2.17) | 1067.2 (x6.67) | 1360 (x8.5) | 80 (x0.5) |
| `PB_Bomb_Mk82_AirStrike` | direct | 125 | 450 | 900 (x2) | 4050 (x9) | 2475 (x5.5) | 450 (x1) |
| `PB_Bomb_Mk82_AirStrike` | blast | 95 | 335 | 1172.5 (x3.5) | 1172.5 (x3.5) | 1507.5 (x4.5) | 335 (x1) |
| `PB_Bomb_Mk82_AirStrike_Delayed` | direct | 125 | 450 | 900 (x2) | 4050 (x9) | 2475 (x5.5) | 450 (x1) |
| `PB_Bomb_Mk82_AirStrike_Delayed` | blast | 95 | 335 | 1172.5 (x3.5) | 1172.5 (x3.5) | 1507.5 (x4.5) | 335 (x1) |
| `PB_PRJ_Artillery_155mmM795HE_SP_Beach` | direct | 125 | 330 | 660 (x2) | 2970 (x9) | 1815 (x5.5) | 330 (x1) |
| `PB_PRJ_Artillery_155mmM795HE_SP_Beach` | blast | 95 | 120 | 420 (x3.5) | 420 (x3.5) | 540 (x4.5) | 120 (x1) |
| `PB_PRJ_Missile_KineticStrike_TEMP` | direct | 20 | 1000 | 0 (x0) | 0 (x0) | 1000 (x1) | 1000 (x1) |
| `PB_PRJ_Missile_KineticStrike_TEMP` | blast | 130 | 1 | 0 (x0) | 1 (x1) | 3 (x3) | 1 (x1) |
| `PB_PRJ_Missile_AIM9X_CarrierStrike_SSMBattery` | direct | 743 | 1000 | 2000 (x2) | 9000 (x9) | 5500 (x5.5) | 1000 (x1) |
| `PB_PRJ_Missile_AIM9X_CarrierStrike_SSMBattery` | blast | 607 | 160 | 160 (x1) | 480 (x3) | 400 (x2.5) | 128 (x0.8) |
| `PB_40x46mmLVG_Drill` | blast | 429 | 40 | 16 (x0.4) | 100 (x2.5) | 120 (x3) | 40 (x1) |
| `PB_40x46mmLVG_Drill_Gas` | blast | 429 | 40 | 16 (x0.4) | 100 (x2.5) | 120 (x3) | 40 (x1) |

Pattern and warning rows (registry):

| Registry row | Default |
|---|---|
| `Artillery_ShellCountPerVolley` | 18 |
| `Artillery_VolleyCount` | 1 |
| `Artillery_TimeBetweenShells` | 0.5709 |
| `Artillery_TimeBetweenShellsVariation` | 0.175 |
| `Artillery_DispersionRadius` | 45 |
| `Artillery_FireDelay` | 4 |
| `Artillery_RangeingShotCount` | 2 |
| `Artillery_RangeingTimeBetweenShots` | 2 |
| `JAGMStrike_MapInnerBlastRadius` | 4 |
| `JAGMStrike_MapBlastRadius` | 10 |
| `JAGMStrike_MapShockwaveRadius` | 20 |
| `JAGMStrike_WarningRadius` | 200 |
| `AirStrike_WarningDelay` | 3 |

3877 raw-offset checks matched.

Test: health lost by a tank to one JAGM hit.

## L3379 - Fire damage affectors and their stages (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3379-fire-damage-affector-stages.json). Dataset: `reference-data/frosty/fire-damage-affectors.json`. Fire damage is not in a blast object. Six affector files (`Class_14965f9f`) each hold an interval and a list of stages (integer, float, material 169):

| Affector file | Interval (`ce8df685`) | `72380a66` | `093fdee2` | Stages: integer / float |
|---|---|---|---|---|
| `Affector_FireFizzleOut` | 0.2 | 0 | 100 | 2 / 2, 50 / 1 |
| `Affector_Damage_AirburstIncendiary` | 0.3 | 15 | 1 | 10 / 15 |
| `Affector_Damage_Thermobaric` | 0.4 | 5 | 1 | 8 / 2, 5 / 1.5 |
| `Affector_Damage_Exit_IncendiaryGrenade` | 0.2 | 0 | 1 | 3 / 1 |
| `Affector_Damage_InOpenVehicle_IncendiaryGrenade` | 0.1 | 1 | 1 | 8 / 2, 6 / 3.5, 4 / 5 |
| `Affector_Damage_IncendiaryGrenade` | 0.1 | 0 | 1 | 2 / 0, 15 / 2.5, 10 / 7, 5 / 10 |

- Candidate reading: integer = damage, float = time. For the incendiary grenade the integers fall as the floats rise (15 to 2.5 s, 10 to 7 s, 5 to 10 s), and the projectile lives 10 s. The thermobaric list does not fit the same reading of the float.
- Field names are hashes; units (per interval or per second) are not shown.
- Material 169 against the soldier: head scalar -; neck / chest scalar 1; stomach scalar 1; limb scalar -.

58 raw-offset checks matched.

Test: health lost in the first and in the eighth second inside an incendiary grenade fire.

## L3385 - Repair Tool and EOD Bot damage to vehicles (9 October 2026) - Replaced by L3386

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3385-repair-tool-vehicle-damage-affector.json). Dataset: `reference-data/frosty/repair-tool-vehicle-damage-affector.json`. `Affector_RepairToolDamageVehicle` and `Affector_EODBot_DamageVehicle` hold the same seven entries on material 479. Per application, times the grid value:

| Entry | InitialDamage | Tank / IFV (x1) | Helicopter (x1.25) | Light vehicle (x2) |
|---|---|---|---|---|
| 0 | 10 | 10 | 12.5 | 20 |
| 1 | 5 | 5 | 6.25 | 10 |
| 2 | 7.5 | 7.5 | 9.375 | 15 |
| 3 | 12.5 | 12.5 | 15.625 | 25 |
| 4 | 15 | 15 | 18.75 | 30 |
| 5 | 17.5 | 17.5 | 21.875 | 35 |
| 6 | 20 | 20 | 25 | 40 |

- Registry: `RepairTool_Damage Vehicle Rank` 3, `RepairTool_BR_Damage Vehicle Rank` 5, `RepairTool_Apply Damage/ Repair Interval` 0.1. If the rank is the entry index: 12.5 in multiplayer, 17.5 in Battle Royale (candidate, joined by name).
- 12.5 every 0.1 s would be 125 per second against a tank, about twice the repair rate; the tick rate is not confirmed.

36 raw-offset checks matched.

Test: health an enemy tank loses in 5 s of Repair Tool use.

## L3386 - Repair Tool affectors and the stacking table (9 October 2026, replaces L3385)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3386-repair-tool-affectors-and-stacking-table.json). Dataset: `reference-data/frosty/repair-tool-affectors-and-stacking-table.json`. Registry rows:

| Registry row | Default |
|---|---|
| `RepairTool_Damage Vehicle Rank` | 3 |
| `RepairTool_BR_Damage Vehicle Rank` | 5 |
| `RepairTool_Apply Damage/ Repair Interval` | 0.1 |
| `RepairTool_ActiveRepair_AntiRepair Amount Per Second` | 45 |
| `RepairTool_ActiveRepairBR_AntiRepair Amount Per Second` | 30 |
| `RepairTool_Default_Repair Amount Per Second` | 40 |
| `RepairTool_ActiveRepair_Repair Amount Per Second` | 60 |
| `RepairTool_DefaultBR_Repair Amount Per Second` | 30 |
| `RepairTool_ActiveRepairBR_Repair Amount Per Second` | 60 |
| `RepairTool_Default_AntiRepair Amount Per Second` | 30 |
| `RepairTool_DefaultBR_AntiRepair Amount Per Second` | 15 |
| `RepairTool_Range` | 2 |

Stacking table in `Affector_VehicleRepair` (eight of 16 entries, all identical):

| Count (`621f70fb`) | Multiplier (`6be2817d`) | Count x multiplier |
|---|---|---|
| 2 | 0.75 | 1.5 |
| 3 | 0.58 | 1.74 |
| 4 | 0.5 | 2 |
| 5 | 0.4 | 2 |
| 6 | 0.33 | 1.98 |
| 7 | 0.28 | 1.96 |
| 8 | 0.25 | 2 |

- Fits: with several repairers each one is scaled, and the total caps at about twice one repairer (candidate; hashes only).
- Heal entries in `Affector_RepairTool_HealVehicle`: 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20.

Damage entries (both damage affectors, material 479), per application, times the grid value:

| Entry | InitialDamage | Tank / IFV (x1) | Helicopter (x1.25) | Light vehicle (x2) |
|---|---|---|---|---|
| 0 | 10 | 10 | 12.5 | 20 |
| 1 | 5 | 5 | 6.25 | 10 |
| 2 | 7.5 | 7.5 | 9.375 | 15 |
| 3 | 12.5 | 12.5 | 15.625 | 25 |
| 4 | 15 | 15 | 18.75 | 30 |
| 5 | 17.5 | 17.5 | 21.875 | 35 |
| 6 | 20 | 20 | 25 | 40 |

- `Damage Vehicle Rank` 3 and 5 point at 12.5 and 17.5 if the rank is the entry index (candidate, joined by name).
- Whether the damage to enemy vehicles is the `AntiRepair` per-second row (30) or a damage entry per 0.1 s is not settled; L3385 wrongly ruled the first out.

81 raw-offset checks matched.

Tests: repair time of a damaged tank with one and with two repairers; health an enemy tank loses in 5 s of Repair Tool use.

## L4021 - Explosive, throwable and supply gadget graphs (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4021-explosive-and-supply-gadget-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/gadgets-explosives-supply.md`).

- Claymore (`SimEx_ClaymoreFrag`): damage = BaseDamage x pellets x sprint modifier x range term x (0.67 if the target's armour is above 0), rounded to steps of 5. Pellets come from PelletCount, a stance factor and distance, with constants 2.3 and 25, clamped to PelletLimit. A -3 offset enters the range term. The tunable values themselves are not in the graph.
- Supply crate (`SimEx_SupplyCrate_Granite`): tick period 5 s (floor 0.01); each tick applies a per-weapon-class ammunition affector with parameter 4.95; the target must have health above 0.
- Flashbang, Stun Drill and Stun Drill trigger flash share one rule: effect class from view angle (in front, sides, behind) and close or far range, six duration tunables, plus 0.2 s, through `Affector_Flashbang`.
- Concussion grenade: three rings (close, mid, max radius tunables), each with its own duration tunable and its own entry of `Affector_ConcussionGrenade`.
- PTKM1R: only vehicles faster than `VehicleMovingThreshold` and between MinimumRange and MaximumRange trigger it; scan period 0.1 s; an owner-state branch uses a 180 half-angle and 1.5 x MaximumRange.
- Incendiary, thermobaric, proximity grenade and others are described in the findings file; those rows are a delegated reading and are not individually raw-checked.

14 raw-offset checks matched.

## L4026 - Tool and miscellaneous gadget graphs (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4026-tool-and-misc-gadget-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/gadgets-tools-misc.md`).

- Defibrillator (`SimEx_Defib`): charge time = clamp(`TimeToFullCharge` - `ActiveReviveTimeReduction`, `ChargeTimeMinimum`, `TimeToFullCharge`). Effects: `Affector_Damage_Defibrillator` parameter 0.5, `AffectorRevive_Defibrillator_Ranked` parameter 2.0 (entry 6 when the action enum is 24), `Affector_Supercharge` parameter 5.0 when an upgrade test passes. Search radius is the larger of the friendly and enemy range tunables.
- EIDOS (`SimEx_EIDOS_Logic_GameVolume`): alive time = `EIDOS_Alive Timer` + `PerimeterDefenseTimerExtension` (upgrade only); ends when the timer completes or intercepts reach `EIDOS_Max Intercepts` + `PerimeterDefenseProjectileAddition` (upgrade only); intercept search every 0.1 s within `EIDOS_Max Intercept Range`. MPAPS has the same structure with its own tunables.
- Mobile jammer: radius x `ImprovedJammerRadiusMulti` with the upgrade; jam, lock-jam and projectile-jam effects applied with parameter 0.2; self-jam uses `JammingDuration_Self`.
- Drone out-of-bounds timer: rises at 1 x and decays at 2 x frame time, capped at `Drone_Max Time Out Of Bounds`, checked every 0.25 s.
- Adrenaline shot: three self effects (flak, suppression, debuff removal) all take `AdrenalineShot_Duration`.
- Gas mask, TUGS, laser designator, repair tool, deployable cover, Lancet and tracer dart are described in the findings file; those rows are a delegated reading and not individually raw-checked.

10 raw-offset checks matched.

## L4029 - Game-mode graphs (battle royale, Gauntlet, shared modes, single player) (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4029-game-mode-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/gamemodes.md`).

- Sabotage gadget: arming 30 s (needs on ground), interact fill 0.45 s, search range = `Sabotage_Distance` + 1 (+ `ImprovisorDistanceAdd` with the upgrade), applies the disable-all-vehicle-weapons effect for 29 s; blocked during the insertion sequence.
- Sabotage projectile: the vehicle-sabotaged effect lasts 26 s; state steps at 28.7 s and at 6.5 s and 10.5 s after attach; immobilise duration = 26 - state 1 duration.
- Capture rate (`TeamInsideVolume`): `CaptureSpeedMultipliers`[clamp(players, 0, 4)], x `fAssaultClassCaptureModifier` when the assault-class kill switch is on.
- Battle royale loadout crate points: radius = zone radius x random^0.66, 20 tries per crate.
- Battle royale airdrop placement: small-ring mode when ring radius < `BR_Airdrop_Small_Ring_Radius`; slope accepted below 0.1; a buffer ratio pulls the point toward the centre; reward-drop search constant 0.35.
- Night Raid (single player) speed modifier: (0.715 + 0.285 x clamp((d - 2) / 13, 0, 1)) x 0.85, otherwise 0.87.
- Contract counters (damage, headshot, kill, vehicle, capture, loot) are squad accumulators with thresholds passed in.
- MCOM interaction graphs hold 60 and 4 constants (read as seconds; role inferred).

13 raw-offset checks matched.

## L4030 - In-round progression, remaining gadget and AI graphs (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4030-in-round-progression-and-remaining-gadget-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/gadgets-perks-ai.md`).

- Passive upgrades (period / effect duration): low profile 1.0 / 1.1 s, stance flak 1.0 / 1.1 s, mechanized infantry 2.0 / 2.1 s, vehicle health plus 2.0 / 2.0 s, enhanced filtering every 0.333 s.
- Active Medic: 7 m radius, crate-healing and ammo effects of 1.1 s, plus a 10 s self buff. Active Attack: 10 m squad radius, ends after 4.9 s. Active Repair and Anti-Repair: 10 s.
- Combat High: kills within 5 s of each other raise a stack from 0 to 5; each stack applies `Healing_CombatHigh` with parameter 0.1. Repeatable Reward stacks to 4.
- Mortar fire support: a ranging shot, then volleys; shells spawn 300 above the target with vertical velocity -100, landing in a random disc of `Mortar_DispersionRadius`; `FireSupportActive` multiplies shell count by `Artillery_IncreaseShellCountPerVolley`.
- Sniper decoy: every 2 s applies an anti-glint effect (2.1 s) within 5 m; fires a fake effect every 1.5 to 6 s at random.
- AI health ping: starts below 95 health and clears at 100; a squad leader counts as recently damaged for 2.0 s.
- Sabotage timings repeat L4029 (29 s weapon disable, 26 s sabotaged).

11 raw-offset checks matched.

## L4035 - Values in the effect assets that graphs apply (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4035-effect-asset-values-for-graph-effects.json). Decoded from the effect (affector) assets named by the expression graphs; table in the run folder (`expression-graphs/affectors-table.tsv`).

- The table `expression-graphs/affectors-table.tsv` lists the 208 effect assets named by simulation graphs with their class and non-default stored fields.
- Defibrillator: both revive effects (`AffectorRevive_Defibrillator_Revive`, `_Ranked`) hold six entries of 50, 60, 70, 80, 90, 100 (read as health restored, chosen by entry index); the damage effect holds entries rising from 50 in steps of 10. `AffectorRevive_HealthRestored` holds 100, 90, 80, 75, 70, 60, 50, 40, 30, 25, 20.
- Explosive damage multipliers: `Affector_Flak` 0.67 (the same 0.67 the Claymore graph uses, L4021), adrenaline shot flak 0.8, giga shield 0.5.
- Combat High healing entries 5, 6, 7, 8, 9, 10 (one per stack). Medical triage healing 20 with 1.0; emergency damage control extra heal 70 with 2.0. Auto-regeneration: resilient 30 and 2.5; hemostatic smoke 12.5 and 2.5.
- Spotting: low profile spot duration x 0.667 and spot delay 1.2; improved jammer target spot duration x 0.5 and time until spot 1.5; anti-air anti-spotting spot time x 0.75.
- Lock-on: mark target 1.34; anti-air and attack helicopter passive lock-on time 0.8; tracer dart locking signature multiplier 11; smoke discharger locking jammer 25, 15 and 0.2.
- Mechanic overheat: stationaries 0.5, vehicles 0.9. Gadget over-repair 20. Ceramic armour entries 121 and 242 (and 40, 80) with 0.5. Race-mode catch-up boost entries are 1.02^n, from 1.0 to 1.148685.
- Defibrillator charge against EA: stored full charge 1.0 s matches the 1.2.3.0 note; the stored minimum is 0.3 s where the note says 0.35 s (L232). The graph rule gives 1.0 - 0.7 = 0.3 s when the active-revive reduction applies.

52 raw-offset checks matched.
