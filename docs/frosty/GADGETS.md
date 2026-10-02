# Gadget source evidence

Gadgets are research for a possible future Analyzer section. Vehicles are a separate game category and have their own page, [Vehicles](VEHICLES.md). Cosmetics, skins and artwork are excluded. Sound is out of scope. Battle royale, Granite and Gauntlet mechanics are excluded, and shared objects stay candidates where standard multiplayer use is unproved. Site implementation is not authorized.

This page records what the saved game data says about each gadget: attributed UI text, dated EA statements, stored source values and the selection chains that reach them. It does not say what a gadget does in a match.

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

Open: the Squad file `d0a2de18-a7b2-4c3c-9e87-aff6ddc8a180` (two exact child GUIDs) and the FasterRecharge selector owner `aeb43f2c-3c7b-4056-a8f6-f965da671da3`. A Killshot export/import control reproduced; no owner was found in the historical index, and no global absence is claimed.

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
- AT Mine: historical chains at the older head; current catalog identities exist, but typed owner continuity is unproved.
- Drones: two separate chains; the Recon-to-TRV150 variant join is unproved.
- Proximity: an unknown-role Shot field reaches a SimEx detector dependency; the primary projectile object stays separate.
- T-UGS and Proximity share the declared query-result type; parameter comparison covers eleven current detector values and keeps MTN-55 timing as a comparison clue only.
- Airburst and L154: Equipment, Ability, CUST, WB and a separate PF root reach the lingering and FireRadius exports; no equipment-to-PF bridge.

## Method limits

- **No compiled utility operation reader** was found in the inspected inventory (L190 stays blocked). Repair, supply, revive and regeneration operations are therefore unnamed. The enum and curve readers (L1001, L1002) do not read the utility format. This is a limit of what was inspected, not proof that no reader exists.
- A name, equal scalar, wrapper identity or authored port is insufficient to name an operation.
- UI-to-source number matches (Hemostatic 12.5 and 2.5, MP-APS 3, MTN-55 1 s and 2 s, revive 2.2 s) are consistent with each other, which makes them good questions for a future capture, not controls.
