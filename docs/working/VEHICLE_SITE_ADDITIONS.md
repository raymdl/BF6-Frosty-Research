# Vehicle research and potential Analyzer additions

## Purpose

Prepare comparison stats for a possible vehicle section. Vehicles remain outside the current weapon and attachment section. Cosmetics, skins and artwork are excluded. This work does not authorize site data, simulation or UI changes.

## Review before resuming

Start with the comparison list below. The saved census and source profiles already cover all 46 exact blueprint roots. Do not repeat the census or launch general graph audits. A new lead must name an approved stat, named families, an exact selected route and a known-answer control.

The operator approved the stat list on 30 September and authorized ordered Stage 2 work overnight. Before each Frosty use, the parent must run the build guard and check that no other Frosty or raw collector process is active. If the guard fails or local time reaches 03:45, stop all Frosty use for the rest of the run and use saved evidence only. Evidence is 1.4.3.1 at Head 4892087. Its use after the update is not verified. The 1.4.3.5 update check in [GAME_UPDATE_GUIDE.md](../GAME_UPDATE_GUIDE.md), Stage 1, decides carry-forward. If a new data build was created, compare each cited raw asset SHA-256 against the new capture and list changed vehicle assets before reuse.

Keep actual owner keys, Head values and descriptor identities separate. Selected owner, entry and armament counts are not usable seats or default loadouts. MD slot/bone associations do not prove a whole owner is visual only. MM state/input graphs do not supply physical equations. MH47 polymorphic components do not prove absent weapons. A failed known-answer control invalidates its route and establishes no negative result.

## Active research

The `2026-09-30T2021-0400-vehicles` run is closed. All three workers stopped. Its [handoff](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-09-30T2021-0400-vehicles/HANDOFF.md) and review are in the run folder. Current evidence is 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. Reused receipts keep their original Head and carry forward by raw hash. Earlier Stage 2 notes below retain their historical build labels.

| Lead | Closed result | Research / site commit |
|---|---|---|
| L3031 | Guarded shared-lock capture resolves 42 external GUID pairs across 28 unique targets, zero failed. MBT source controls pass; image route does not complete a card/root chain. | e0f1ceb / 7c5326b |
| L3032 | Fifteen selected category targets and source control pass; no complete card/root edge. UI stops after two leads. | 228b242 / 63eee8c |
| L3033 | Current cannon control passes; four selected UI assets and two cannon candidates do not prove an exact APHEI owner. Projectile and carrier rule remain unresolved. Stop after one lead. | c6f8234 / 7982be4 |

All nine cards remain unlinked; no family seat counts, roles or tags are assigned. No working UI-to-asset method is claimed. The missing target capture gap is resolved; exact lookup/owner selection remains open. APHEI is current-only evidence, with no old/raw comparison or before/after claim. No additional recording proposal was made.

Parent review and records check pass: 549 valid records, zero errors and two existing warnings. Final committed JSON parses and every vehicle finding matches its receipt asset key. L3032 repairs the earlier L3031 partial-staging error. Unrelated concurrent changes and the prior L3024 generated diff remain preserved.

No health recording, in-game test, projectile damage/radius naming hunt, Drone weapon join, site implementation or push occurred. Reopen only with a new exact UI consumer/root edge or a current APHEI text-to-weapon owner link. Use the [standing rules](frosty-orchestrator-standing.txt) for any new guarded capture.

## Coverage and source status

The [coverage file](../../reference-data/frosty/vehicle-coverage.json) retains the original census identities and capture rows. It now includes the reviewed exact root profiles, branch evidence pointers, role dispositions and supplemental source stages from L3011. The 14 pinned coverage artifacts matched their saved hashes. All 46 exact root raw hashes also matched. A parent read confirmed CB90 `MaxHealth` 1000 at raw offset 440, bytes `00007a44`, raw SHA-256 `2d8e05398f8f3f2b79159a8db1ec5a87d3033ac7c2469d0cb5f3c6c3f6911ad3`.

| Coverage item | Reviewed result |
|---|---|
| Census | 6,847 catalog entries, 41 family/candidate rows, 38 blueprint families |
| Exact roots | 46 identities and 46 source profiles; every reviewed root is Head 4892087 |
| Separate role reviews | Five: C17, MD530, Cheetah, signal-decryption antenna and Abrams ULR prop |
| Cheetah | Functional Gepard customization alias; five selected equipment/passive routes reviewed in L3014; no additional chassis |
| Antenna | Separate vehicle-authored objective; configured MaxHealth 150 and RepairRateModifier 1; excluded from ordinary vehicle comparisons |
| TRV150 spectator | Separate typed support role outside the 46 chassis roots; no additional helicopter chassis |
| Compiled resources | Eight selected bodies pinned in the earlier run; graph operations and native execution unresolved |
| Global membership/config | Seven unread routes through 32 selected references; scoped out of this intrinsic comparison list |

The seven scoped-out routes are `CT_GLA_CH1_S3_VehicleUnlocks`, `GRX_DICEAI`, `KST_Vehicles`, `SoldierMutatorsPublicChannels`, `CommonPublicChannels`, `PlayerAbilityCategoriesAsset` and `SoldierOnlyPublicChannels`. Their full paths and evidence are in the coverage file and L3011. None is reclassified as a terminal native or schema limit. This list excludes unlock eligibility, mode admission, current multiplayer availability, default loadouts and global player/AI policy. If the operator adds one of those stats, first identify its exact dependency among these routes.

Functional evidence uses descriptor SHA-256 `99b49cfd8bdb5bb6f0181df8ac0d93a0396c1b7f07a1ba3ce8ca1cea45969640` at Head 4892087. Separate release controls use Head 4892017 and descriptor SHA-256 `91c9ea7c3dd830e34a78123c8bb7485e80eefdb18fc9c7ee41117971d23565c2`. Stage 1 made no new capture; Stage 2 captured only the three control assets stated above.

## Approved comparison stat list

Each family has an explicit stat map in the pinned `stage-1/comparison-stat-map.json` artifact linked by L3018. It includes all 38 families and links all 46 root profiles. The tables below are its review view. Role groups are provisional comparison groups; they do not establish multiplayer availability. AH6M variants can have different attack/transport roles. MQ9 remains in the drone group despite its Airplane source folder. Stationary AA remains in the stationary group.

Use these status terms:

- **Sourced:** A reviewed serialized value or selected source identity has a receipt. This does not establish native activation or gameplay units. The configured health names below use an exact own-wrapper join or an explicitly stated same-owner schema inference.
- **Sourceable:** An exact selected route and typed field path exist. Some WF words have candidate names only. A named stat requires a same-owner naming control before a trace is launched. The route alone does not authorize a lead that can only repeat a limit.
- **Needs in-game validation:** Native composition, compiled operations, units, activation or unresolved receiver semantics prevent a usable gameplay value. Saved identities and raw tuples are still retained as findings.

### Stats shared across roles

| Stat | Status and existing evidence | Route or remaining boundary |
|---|---|---|
| Configured MaxHealth | Sourced for 35 base families; see family table. AAV7A1, TheBeast and JetSki need validation of meaning. | Exact VB root ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ actual Class_f2a56983 owner. L3001 maps Field_9040392c on key e39565c4c24306f97c377628d6d9a47e. Different keys cannot inherit the name. |
| Effective health, zone damage and disable thresholds | Needs in-game validation. L3007ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œL3010 and L3017 retain zone/connection owners. L3010 has configured DisabledDamageThreshold/ClearDisabledDamageThreshold 200 on 11 base roots and 300 on DirtBike01/02. | Named thresholds do not supply damage equations, disabled-state direction or effective HP. |
| Configured repair multiplier | Sourced RepairRateModifier 1 on the same 35 base families. | VB health owner ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Field_8fc892f2 on the exact named schema. This is not HP per second. |
| Effective repair rate and delay | Needs in-game validation. L3017 includes repair interaction and ModBuilder consumers. | Base rate, delay, tool composition and native activation remain unresolved. |
| Armament alternatives | Sourced selected WF/Ability identities and labels from L3002ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œL3010; MH47 remains a polymorphic armament limit. | Exact root weapon component ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ selected WF and Ability/U. Per-family routes are in the map. No default or active loadout follows. |
| Direct damage, blast damage and radius | Needs in-game validation. L3013 sources 13 PD profiles, six selected curve pairs on four curve-bearing assets and seven exact null pairs; selected InnerRadius25/50 point arrays are retained. L3007/L3009 retain other projectile/warhead consumers. | Selected WF ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ PD/PB ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ local warhead and curve owners. Names, point order and values do not prove units, interpolation or composed damage. |
| Configured firing operand | Sourced for exact matched selections in the completed Stage 2 receipts below. Unmatched or untraced owners remain sourceable. | Same-Head M4A1 own-wrapper control names RateOfFire through exact owner and nested/member schema identity. Values are configured fields, not measured RPM. |
| Observed fire rate and sustained fire | Needs in-game validation. | Shot scheduling, heat, burst behavior and activation are not established by candidate rate words. |
| Reload, cooldown, heat recovery and resupply | Needs in-game validation. Exact selected WF/Ability routes exist, but the reviewed evidence has no named effective timing formula. | Do not launch an unnamed float scan or repeat the compiled-reader audit. |
| Configured ammo words | Sourced MagazineCapacity, NumberOfMagazines, InitialAmmo and AutoReplenishDelay for matched selections in the completed Stage 2 receipts below. | Source values do not establish loaded/reserve rounds, infinite ammo or displayed cooldown. Unmatched owners remain explicit. |
| Loaded rounds, reserve rounds and ammo recovery | Needs in-game validation. | Source selections and configured words do not establish the displayed or active ammunition state. |
| Countermeasure/passive alternatives | Sourced selected Ability/U/WMD/tag identities where present, including L3014 AA/MBT and L3015 IFV/AAV/APC consumers. | Root selections ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ exact Ability/U ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ modifier/tag/graph owner. A selected identity is not default availability. |
| Countermeasure charges, duration, cooldown and lock break | Needs in-game validation. | Thermal-smoke/passive compiled operations, tag dispatch and native effects remain unresolved. |
| Entry and station definitions | Sourced selected entry/slot indices and associations in L3007ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œL3010/L3016/L3017. | Root ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ exact entry/slot owner; MD links retain slot/bone/default associations only. |
| Usable seats, switching and weapon access | Nine archetype seat counts are sourced in-game statements in L3023. Exact family links remain unresolved; family values stay unset. Switching and weapon access need in-game validation. | Count every enterable seat on a vehicle with an exact card join; prediction: the count equals its card number. No recording or test was run. |
| Projectile speed, drop, lock range and guidance | Full configured Shot.InitialSpeed vectors are sourced for matched Stage 2 selections below. Effective velocity, drop and guidance need in-game validation. | Preserve all three vector components. Source vectors do not establish runtime equations or units. |
| Speed, acceleration, braking, turning and stability | Needs in-game validation. L3007ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œL3010/L3016 retain local flight/input/configuration/MM owners. | MM state labels, MD names and typed tuples do not supply physical equations or units. For stationary weapons compare traverse and aiming response instead. |

Completed Stage 2 configured source updates are listed below. Exact matched profiles move from sourceable to sourced; families with unmatched alternatives remain partial. A new lead must name its exact same-owner control before launch. Effective velocity, direct damage and blast radius remain unresolved.

Concrete example routes are `Common/Hardware/Vehicles/_VehiclesCommon/WeaponData/MBT/WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG`, `.../MBT/WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` and `Common/Hardware/Vehicles/_VehiclesCommon/WeaponData/RWS/WF_Vehicles_RWS_AGL`. The full paths, exact owner keys, typed field paths, offsets, bytes and raw hashes for each candidate are in the stat-map artifact. Existing raw values are reused; no new firing interpretation is claimed.

### Role-specific comparison priorities

Every role includes the applicable shared stats above. These extra gameplay stats all need in-game validation with the current receipts.

| Role | Families | Extra stats a player would compare | Existing evidence |
|---|---|---|---|
| MBT | Abrams, Leopard | Front/side/rear damage; turret traverse/elevation; main/coax weapon access; disable recovery | L3010, L3013, L3014, L3017 |
| IFV/APC | Bradley, CV90, AAV7A1 | Passenger access; turret traverse/elevation; autocannon/missile access; amphibious behavior where supported | L3010, L3013, L3015, L3017; AAV health names remain unresolved |
| AA | Gepard, with Cheetah customization alias | Air-target damage; lock range/acquisition time; gun overheat; anti-spotting and smoke effects | L3006, L3010, L3013, L3014 |
| Light/transport ground | Couch, Flyer60, JLTV, Marauder, PTV, QuadBike, TheBeast, Vector, DirtBike01/02 | Hill acceleration; turn/brake response; rollover; passenger exposure; station weapon access | L3010, L3016, L3017; TheBeast health names remain unresolved |
| Attack helicopter | AH64E, AH6M, Eurocopter | Climb rate; yaw/pitch/roll response; pilot/gunner access; missile lock time; flare/other selected countermeasure timing | L3002, L3003, L3007, L3008; role varies by exact variant |
| Transport helicopter | UH60, MH47 | Usable passenger/gunner stations; climb rate; flight response; spawn behavior; countermeasure timing | L3008; MH47 armament remains an exact polymorphic schema limit |
| Jet | F14, F16, F22, FA18F, JAS39, SU57 | Top/boost speed; boost duration/recovery; turn/climb response; stall behavior; lock and countermeasure timing | L3002, L3003, L3007, L3008 |
| Boat | CB90, JetSki, RHIB | Forward/reverse speed; water turning; shore transition; passenger exposure; station access | L3005, L3009; JetSki health names remain unresolved |
| Stationary | BGM71TOW, CWS/CROWS, GDF009, M2MG, Phalanx, SSMBattery | Traverse/elevation limits; firing/cooldown; guidance/lock; operator exposure | L3005, L3009; selected definitions do not prove player access or multiplayer admission |
| Drone | MQ9, TRV150 | Control range; view/targeting; deployment/recovery; flight response; loss-of-link behavior; selected payload access | L3003, L3008, L3009; spectator support role stays separate |

### Configured values by family

These are base-root source values. The stat map links every exact variant profile. Do not copy a base value onto a different SP/Cine owner. Most names are inferred from exact same-owner class/key/member schema identity with L3001, rather than each root's own remixer wrapper. CB90 has its own exact name joins. Effective health and repair behavior remain unresolved for every row.

| Family | Role group | Configured MaxHealth | Configured RepairRateModifier | Receipt |
|---|---|---|---|---|
| airplane/f14 | Jet | `1000` | `1` | L3008 |
| airplane/f16 | Jet | `1000` | `1` | L3007 |
| airplane/f22 | Jet | `1000` | `1` | L3008 |
| airplane/fa18f | Jet | `1000` | `1` | L3008 |
| airplane/jas39 | Jet | `1000` | `1` | L3008 |
| airplane/mq9 | Drone | `1000` | `1` | L3008 |
| airplane/su57 | Jet | `1000` | `1` | L3008 |
| boat/cb90 | Boat | `1000` | `1` | L3009 |
| boat/jetski | Boat | Needs validation; different owner key | Needs validation; different owner key | L3009 |
| boat/rhib | Boat | `1000` | `1` | L3009 |
| car/couch | Light/transport ground | `1000` | `1` | L3010 |
| car/flyer60 | Light/transport ground | `1000` | `1` | L3010 |
| car/jltv | Light/transport ground | `800` | `1` | L3010 |
| car/marauder | Light/transport ground | `800` | `1` | L3010 |
| car/ptv | Light/transport ground | `1000` | `1` | L3010 |
| car/quadbike | Light/transport ground | `1000` | `1` | L3010 |
| car/thebeast | Light/transport ground | Needs validation; different owner key | Needs validation; different owner key | L3010 |
| car/vector | Light/transport ground | `1000` | `1` | L3010 |
| drone/trv150 | Drone | `100` | `1` | L3009 |
| helicopter/ah64e | Attack helicopter | `1000` | `1` | L3007 |
| helicopter/ah6m | Attack helicopter | `700` | `1` | L3008 |
| helicopter/eurocopter | Attack helicopter | `1000` | `1` | L3008 |
| helicopter/mh47 | Transport helicopter | `1000` | `1` | L3008 |
| helicopter/uh60 | Transport helicopter | `1500` | `1` | L3008 |
| motorcycle/dirtbike01 | Light/transport ground | `1000` | `1` | L3010 |
| motorcycle/dirtbike02 | Light/transport ground | `1000` | `1` | L3010 |
| stationary/bgm71tow | Stationary | `150` | `1` | L3009 |
| stationary/cws | Stationary | `300` | `1` | L3009 |
| stationary/gdf009 | Stationary | `1000` | `1` | L3009 |
| stationary/m2mg | Stationary | `150` | `1` | L3009 |
| stationary/phalanx | Stationary | `1000` | `1` | L3009 |
| stationary/ssmbattery | Stationary | `1000` | `1` | L3009 |
| tank/aav7a1 | IFV/APC | Needs validation; different owner key | Needs validation; different owner key | L3010 |
| tank/abrams | MBT | `1200` | `1` | L3010 |
| tank/bradley | IFV/APC | `1000` | `1` | L3010 |
| tank/cv90 | IFV/APC | `1000` | `1` | L3010 |
| tank/gepard | AA | `1000` | `1` | L3010 |
| tank/leopard | MBT | `1200` | `1` | L3010 |

## Proposals awaiting the operator

These proposals have a sourced value and a concrete test. They remain conditional until the 1.4.3.5 update check and operator approval. No in-game recording was requested or started.

| Proposed stat | Sourced value | Validation step and prediction |
|---|---|---|
| Configured CB90 health | MaxHealth 1000; L3001/L3009 | First use a vehicle stat screen if it exposes an absolute health value. Prediction: its base value is 1000. If no absolute display exists, approve a controlled damage test before presenting this as gameplay HP. |
| MBT configured health comparison | Abrams/Leopard 1200; Bradley/CV90 1000; L3010 | Use identical single-hit damage on matched tested zones, without repair or changing equipment. If damage composition is equal, the MBT health-fraction loss is 5/6 of the IFV loss. A failed prediction leaves zone/native composition unresolved; it does not invalidate the source values. |
| Helicopter configured health comparison | AH6M 700; UH60 1500; L3008 | Use matched controlled single hits on the exact base variants, without repair. If effective damage is equal, UH60 health-fraction loss is 7/15 of AH6M loss. Confirm variants and zone behavior before treating this as a durability ranking. |

Other items remain findings or validation questions because they do not yet have a named effective value and a defensible prediction. Any recording plan must follow the four-part rule in [BF6_CAPTURE_PRIORITIES.md](BF6_CAPTURE_PRIORITIES.md) and receive operator approval first.

## Recommended next stage

Follow the approved item order in the active table. Prefer reuse of existing configured-value receipts. Launch only a sourceable stat with a concrete same-owner control; keep a worker below about 300 raw reads. Do not spend another lead on reader grammar, unnamed float inventory or a known native limit. If two consecutive leads in one role produce no sourced stat, move to another role. The update check still decides whether Head 4892087 evidence carries forward after 1.4.3.5.

The selected source coverage is merged and the stat list is approved. Native vehicle mechanics and multiplayer availability remain unresolved. No site implementation, health-test recording or push is authorized by this run.

## Stage 2 configured source updates

[L3020](../../reference-data/provenance/frosty-2026-09-30-L3020-vehicle-configured-stats.json): Bradley and CV90 select ten deduplicated controlled firing profiles with eight configured fields each. AAV7A1 selects only two unmatched SP firing owners and has no sourced firing profile; its configured firing fields remain sourceable. Exact boundaries are in the receipt and [value tables](../frosty/VEHICLES.md). Native cadence, ammunition state and projectile damage remain validation questions. The pinned comparison map preserves this distinction.

[L3021](../../reference-data/provenance/frosty-2026-09-30-L3021-vehicle-configured-stats.json): Tank/Gepard have 6 deduplicated controlled firing profiles with eight configured fields each. Families with unmatched alternatives remain partial; exact boundaries are in the receipt and [value tables](../frosty/VEHICLES.md). Native cadence, ammunition state and projectile damage remain validation questions. The latest pinned comparison map is in this receipt.

[L3022](../../reference-data/provenance/frosty-2026-09-30-L3022-vehicle-configured-stats.json): Car/Flyer60, Car/JLTV, Car/Marauder, Car/Vector have 4 deduplicated controlled firing profiles with eight configured fields each. Families with unmatched alternatives remain partial; exact boundaries are in the receipt and [value tables](../frosty/VEHICLES.md). Native cadence, ammunition state and projectile damage remain validation questions. The latest pinned comparison map is in this receipt.


## Sourced vehicle UI statements (L3023)

The [receipt](../../reference-data/provenance/frosty-2026-09-30-L3023-vehicle-ui-metadata.json) and [UI text procedure](../frosty/UI_TEXT.md) retain all cards, text ids and links. Role names, descriptions, seat text and tags are sourced on their cards. Exact family/root links remain open; every card is explicitly unlinked.

| Card / role name | Description | Seat text | Tags | Exact family/root link |
|---|---|---|---|---|
| MAIN BATTLE TANK (MBT) | Built for engaging enemy land vehicles but can also effectively combat enemy infantry. | 2 Seats | 2 Seats, Anti-Vehicle, Hard Target | Unlinked |
| INFANTRY FIGHTING VEHICLE (IFV) | Effectively counters hostile infantry but has limited capability against heavy enemy armor. | 6 Seats | 6 Seats, Anti-Soldier | Unlinked |
| LIGHT GROUND TRANSPORT (LIGHT TRANSPORT) | Designed for rapid battlefield traversal. Equipped with firepower to combat hostiles.  | 5 Seats | 5 Seats, Open Seats, Transport | Unlinked |
| ARMORED TRANSPORT (ATP) | Primarily for use in urban areas. Mine blast protection ensures optimal navigation through hostile territory. | 4 Seats | 4 Seats, Shielded Seats | Unlinked |
| MOBILE ANTI-AIR (ANTI-AIR) | Capable of using dual autocannons and homing missiles to combat enemy aircraft. | 1 Seat | 1 Seat, Shielded Seats | Unlinked |
| Attack Helicopter (ATTACK HELI) | Highly effective at engaging all ground targets, especially when both crew positions are manned. | 2 Seats | 2 Seats, Anti-Vehicle, Anti-Soldier | Unlinked |
| TRANSPORT HELICOPTER (TRANSPORT HELI) | This transport helicopter serves as a vital component in air assaults. Two side-mounted miniguns aid in self-defense. | 5 Seats | 5 Seats, Transport | Unlinked |
| ATTACK JET (ATTACK JET) | A fast multirole attack aircraft specialized in engaging all ground targets, including vehicles and infantry. | 1 Seat | 1 Seat, Anti-Vehicle, Anti-Soldier, Soft Target | Unlinked |
| FIGHTER JET (FIGHTER JET) | A stealth fighter that specializes in combating other air vehicles, with limited air-to-ground combat capabilities. | 1 Seat | 1 Seat, Anti-Vehicle, Soft Target | Unlinked |

Numeric seat counts have the enterable-seat test and prediction stated above. These statements do not establish multiplayer availability or default loadouts. The coverage file and updated comparison map retain all nine unlinked cards and unset family values.

[L3024](../../reference-data/provenance/frosty-2026-09-30-L3024-health-own-wrapper-check.json) closes the three requested own-wrapper attempts: AAV7A1, TheBeast and JetSki each select a serialized null wrapper. Their MaxHealth/RepairRateModifier labels remain unresolved. The parent confirmed the AAV7A1 null; no cross-key naming transfer or health recording was made.
[L3025](../../reference-data/provenance/frosty-2026-09-30-L3025-vehicle-configured-stats.json): airplane/f14, airplane/f16, airplane/f22, airplane/fa18f, airplane/jas39, airplane/su57 have 14 deduplicated controlled firing profiles with eight configured fields each. Families with unmatched alternatives remain partial; exact boundaries are in the receipt and [value tables](../frosty/VEHICLES.md). Native cadence, ammunition state and projectile damage remain validation questions. The latest pinned comparison map is in this receipt.

[L3026](../../reference-data/provenance/frosty-2026-09-30-L3026-vehicle-configured-stats.json): helicopter/ah64e, helicopter/ah6m, helicopter/eurocopter have 17 deduplicated controlled firing profiles with eight configured fields each. Families with unmatched alternatives remain partial; exact boundaries are in the receipt and [value tables](../frosty/VEHICLES.md). Native cadence, ammunition state and projectile damage remain validation questions. The latest pinned comparison map is in this receipt.

[L3027](../../reference-data/provenance/frosty-2026-09-30-L3027-vehicle-configured-stats.json): boat/cb90, boat/jetski, boat/rhib have 13 deduplicated controlled firing profiles with eight configured fields each. Families with unmatched alternatives remain partial; exact boundaries are in the receipt and [value tables](../frosty/VEHICLES.md). Native cadence, ammunition state and projectile damage remain validation questions. The latest pinned comparison map is in this receipt.

[L3028](../../reference-data/provenance/frosty-2026-09-30-L3028-vehicle-configured-stats.json): stationary/bgm71tow, stationary/cws, stationary/gdf009, stationary/m2mg, stationary/phalanx, stationary/ssmbattery have 8 deduplicated controlled firing profiles with eight configured fields each. Families with unmatched alternatives remain partial; exact boundaries are in the receipt and [value tables](../frosty/VEHICLES.md). Native cadence, ammunition state and projectile damage remain validation questions. The latest pinned comparison map is in this receipt.

[L3029](../../reference-data/provenance/frosty-2026-09-30-L3029-vehicle-configured-stats.json): helicopter/mh47, helicopter/uh60 have 1 deduplicated controlled firing profiles with eight configured fields each. Families with unmatched alternatives remain partial; exact boundaries are in the receipt and [value tables](../frosty/VEHICLES.md). Native cadence, ammunition state and projectile damage remain validation questions. The latest pinned comparison map is in this receipt.


## Completed Stage 2 run

[L3030](../../reference-data/provenance/frosty-2026-09-30-L3030-vehicle-stage2-closeout.json) pins the final comparison map and merged coverage: 69 configured firing profiles, 552 scalar operands, 27 families and 34 exact root profiles. The other 12 root profiles remain in the 46-root census. Nine UI cards and fifteen presets are sourced; all nine cards remain unlinked, so no family seat values are filled. The three own-health-wrapper attempts added no names.

MQ9 selects a deploy-time wrapper (Class_5b9b2235/key8bbd8fbf139b81bc58b352065eda425e); TRV150 selects its blueprint root (Class_b057bb60/key1d85d88a8e017d438f60302e5e3bad4b). Neither selected root matches the controlled ground WF root schema. No selected exact controlled ground weapon-owner join is proved on this route; no fields transferred and no follow-up tonight. This does not establish absent weapons.

The ordered overnight work is closed. All workers stopped. HANDOFF.md and cleanup.json are in the active run folder. No source tracing, in-game recording or site implementation remains active. Before reuse after 1.4.3.5, complete the update check and compare the cited raw assets if a new data build exists.
