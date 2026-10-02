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
| Configured MaxHealth | source value with effect unconfirmed; durability validation excluded for Season 5. Sourced for 35 base families; see family table. AAV7A1, TheBeast and JetSki need validation of meaning. | Exact VB root → actual Class_f2a56983 owner. L3001 maps Field_9040392c on key e39565c4c24306f97c377628d6d9a47e. Different keys cannot inherit the name. unconfirmed; no recording planned. |
| Effective health, zone damage and disable thresholds | source value with effect unconfirmed; durability validation excluded for Season 5. Needs in-game validation. L3007–L3010 and L3017 retain zone/connection owners. L3010 has configured DisabledDamageThreshold/ClearDisabledDamageThreshold 200 on 11 base roots and 300 on DirtBike01/02. | Named thresholds do not supply damage equations, disabled-state direction or effective HP. unconfirmed; no recording planned. |
| Configured repair multiplier | source value with effect unconfirmed. Sourced RepairRateModifier 1 on the same 35 base families. | VB health owner → Field_8fc892f2 on the exact named schema. This is not HP per second. unconfirmed; no recording planned. |
| Effective repair rate and delay | source value with effect unconfirmed. Needs in-game validation. L3017 includes repair interaction and ModBuilder consumers. | Base rate, delay, tool composition and native activation remain unresolved. unconfirmed; no recording planned. |
| Armament alternatives | source value with effect unconfirmed. Sourced selected WF/Ability identities and labels from L3002–L3010; MH47 remains a polymorphic armament limit. | Exact root weapon component → selected WF and Ability/U. Per-family routes are in the map. No default or active loadout follows. unconfirmed; no recording planned. |
| Direct damage, blast damage and radius | source value with effect unconfirmed. Needs in-game validation. L3013 sources 13 PD profiles, six selected curve pairs on four curve-bearing assets and seven exact null pairs; selected InnerRadius25/50 point arrays are retained. L3007/L3009 retain other projectile/warhead consumers. | Selected WF → PD/PB → local warhead and curve owners. Names, point order and values do not prove units, interpolation or composed damage. unconfirmed; no recording planned. |
| Configured firing operand | confirmed via weapons (configured RateOfFire); source value with effect unconfirmed (remaining effects). Sourced for exact matched selections in the completed Stage 2 receipts below. Unmatched or untraced owners remain sourceable. | Same-Head M4A1 own-wrapper control names RateOfFire through exact owner and nested/member schema identity. Values are configured fields, not measured RPM. unconfirmed; no recording planned. |
| Observed fire rate and sustained fire | source value with effect unconfirmed. Needs in-game validation. | Shot scheduling, heat, burst behavior and activation are not established by candidate rate words. unconfirmed; no recording planned. |
| Reload, cooldown, heat recovery and resupply | source value with effect unconfirmed. Needs in-game validation. Exact selected WF/Ability routes exist, but the reviewed evidence has no named effective timing formula. | Do not launch an unnamed float scan or repeat the compiled-reader audit. unconfirmed; no recording planned. |
| Configured ammo words | confirmed via weapons (configured MagazineCapacity only); source value with effect unconfirmed (remaining effects). Sourced MagazineCapacity, NumberOfMagazines, InitialAmmo and AutoReplenishDelay for matched selections in the completed Stage 2 receipts below. | Source values do not establish loaded/reserve rounds, infinite ammo or displayed cooldown. Unmatched owners remain explicit. unconfirmed; no recording planned. |
| Loaded rounds, reserve rounds and ammo recovery | source value with effect unconfirmed. Needs in-game validation. | Source selections and configured words do not establish the displayed or active ammunition state. unconfirmed; no recording planned. |
| Countermeasure/passive alternatives | source value with effect unconfirmed. Sourced selected Ability/U/WMD/tag identities where present, including L3014 AA/MBT and L3015 IFV/AAV/APC consumers. | Root selections → exact Ability/U → modifier/tag/graph owner. A selected identity is not default availability. unconfirmed; no recording planned. |
| Countermeasure charges, duration, cooldown and lock break | source value with effect unconfirmed. Needs in-game validation. | Thermal-smoke/passive compiled operations, tag dispatch and native effects remain unresolved. unconfirmed; no recording planned. |
| Entry and station definitions | source value with effect unconfirmed. Sourced selected entry/slot indices and associations in L3007–L3010/L3016/L3017. | Root → exact entry/slot owner; MD links retain slot/bone/default associations only. unconfirmed; no recording planned. |
| Usable seats, switching and weapon access | source value with effect unconfirmed. Nine archetype seat counts are sourced in-game statements in L3023. Exact family links remain unresolved; family values stay unset. Switching and weapon access need in-game validation. | L3023/L649 retain stated archetype seat counts, with no exact family join. unconfirmed; no recording planned. |
| Projectile speed, drop, lock range and guidance | confirmed via weapons (configured launch vector and matched gravity/drag); source value with effect unconfirmed (remaining effects). Full configured Shot.InitialSpeed vectors are sourced for matched Stage 2 selections below. Effective velocity, drop and guidance need in-game validation. | Preserve all three vector components. Source vectors do not establish runtime equations or units. unconfirmed; no recording planned. |
| Speed, acceleration, braking, turning and stability | source value with effect unconfirmed. Needs in-game validation. L3007–L3010/L3016 retain local flight/input/configuration/MM owners. | MM state labels, MD names and typed tuples do not supply physical equations or units. For stationary weapons compare traverse and aiming response instead. unconfirmed; no recording planned. |

Completed Stage 2 configured source updates are listed below. Exact matched profiles move from sourceable to sourced; families with unmatched alternatives remain partial. A new lead must name its exact same-owner control before launch. Effective velocity, direct damage and blast radius remain unresolved.

Concrete example routes are `Common/Hardware/Vehicles/_VehiclesCommon/WeaponData/MBT/WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG`, `.../MBT/WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` and `Common/Hardware/Vehicles/_VehiclesCommon/WeaponData/RWS/WF_Vehicles_RWS_AGL`. The full paths, exact owner keys, typed field paths, offsets, bytes and raw hashes for each candidate are in the stat-map artifact. Existing raw values are reused; no new firing interpretation is claimed.

### Role-specific comparison priorities

Every role includes the applicable shared stats above. Each role row below is source value with effect unconfirmed; unconfirmed; no recording planned. Season 5 durability rows remain excluded from validation.

| Role | Families | Extra stats a player would compare | Existing evidence | Confidence |
|---|---|---|---|---|
| MBT | Abrams, Leopard | Front/side/rear damage; turret traverse/elevation; main/coax weapon access; disable recovery | L3010, L3013, L3014, L3017 | source value with effect unconfirmed; unconfirmed; no recording planned. |
| IFV/APC | Bradley, CV90, AAV7A1 | Passenger access; turret traverse/elevation; autocannon/missile access; amphibious behavior where supported | L3010, L3013, L3015, L3017; AAV health names remain unresolved | source value with effect unconfirmed; unconfirmed; no recording planned. |
| AA | Gepard, with Cheetah customization alias | Air-target damage; lock range/acquisition time; gun overheat; anti-spotting and smoke effects | L3006, L3010, L3013, L3014 | source value with effect unconfirmed; unconfirmed; no recording planned. |
| Light/transport ground | Flyer60, JLTV, Marauder, PTV, QuadBike, TheBeast, Vector, DirtBike01/02 (Couch excluded: REDSEC Easter egg) | Hill acceleration; turn/brake response; rollover; passenger exposure; station weapon access | L3010, L3016, L3017; TheBeast health names remain unresolved | source value with effect unconfirmed; unconfirmed; no recording planned. |
| Attack helicopter | AH64E, AH6M, Eurocopter | Climb rate; yaw/pitch/roll response; pilot/gunner access; missile lock time; flare/other selected countermeasure timing | L3002, L3003, L3007, L3008; role varies by exact variant | source value with effect unconfirmed; unconfirmed; no recording planned. |
| Transport helicopter | UH60 (MH47 excluded: round-start insertion animation only, not playable) | Usable passenger/gunner stations; climb rate; flight response; spawn behavior; countermeasure timing | L3008; MH47 armament remains an exact polymorphic schema limit | source value with effect unconfirmed; unconfirmed; no recording planned. |
| Jet | F14, F16, F22, FA18F, JAS39, SU57 | Top/boost speed; boost duration/recovery; turn/climb response; stall behavior; lock and countermeasure timing | L3002, L3003, L3007, L3008 | source value with effect unconfirmed; unconfirmed; no recording planned. |
| Boat | CB90, JetSki, RHIB | Forward/reverse speed; water turning; shore transition; passenger exposure; station access | L3005, L3009; JetSki health names remain unresolved | source value with effect unconfirmed; unconfirmed; no recording planned. |
| Stationary | BGM71TOW, CWS/CROWS, GDF009, M2MG, Phalanx, SSMBattery | Traverse/elevation limits; firing/cooldown; guidance/lock; operator exposure | L3005, L3009; selected definitions do not prove player access or multiplayer admission | source value with effect unconfirmed; unconfirmed; no recording planned. |
| Drone | MQ9, TRV150 | Control range; view/targeting; deployment/recovery; flight response; loss-of-link behavior; selected payload access | L3003, L3008, L3009; spectator support role stays separate | source value with effect unconfirmed; unconfirmed; no recording planned. |

### Configured values by family

These are base-root source values. The stat map links every exact variant profile. Do not copy a base value onto a different SP/Cine owner. Most names are inferred from exact same-owner class/key/member schema identity with L3001, rather than each root's own remixer wrapper. CB90 has its own exact name joins. Effective health and repair behavior remain unresolved for every row.

| Family | Role group | Configured MaxHealth | Configured RepairRateModifier | Receipt | Confidence |
|---|---|---|---|---|---|
| airplane/f14 | Jet | `1000` | `1` | L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| airplane/f16 | Jet | `1000` | `1` | L3007 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| airplane/f22 | Jet | `1000` | `1` | L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| airplane/fa18f | Jet | `1000` | `1` | L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| airplane/jas39 | Jet | `1000` | `1` | L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| airplane/mq9 | Drone | `1000` | `1` | L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| airplane/su57 | Jet | `1000` | `1` | L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| boat/cb90 | Boat | `1000` | `1` | L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| boat/jetski | Boat | Needs validation; different owner key | Needs validation; different owner key | L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| boat/rhib | Boat | `1000` | `1` | L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| car/couch | Light/transport ground | `1000` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| car/flyer60 | Light/transport ground | `1000` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| car/jltv | Light/transport ground | `800` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| car/marauder | Light/transport ground | `800` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| car/ptv | Light/transport ground | `1000` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| car/quadbike | Light/transport ground | `1000` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| car/thebeast | Light/transport ground | Needs validation; different owner key | Needs validation; different owner key | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| car/vector | Light/transport ground | `1000` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| drone/trv150 | Drone | `100` | `1` | L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| helicopter/ah64e | Attack helicopter | `1000` | `1` | L3007 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| helicopter/ah6m | Attack helicopter | `700` | `1` | L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| helicopter/eurocopter | Attack helicopter | `1000` | `1` | L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| helicopter/mh47 | Transport helicopter | `1000` | `1` | L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| helicopter/uh60 | Transport helicopter | `1500` | `1` | L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| motorcycle/dirtbike01 | Light/transport ground | `1000` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| motorcycle/dirtbike02 | Light/transport ground | `1000` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| stationary/bgm71tow | Stationary | `150` | `1` | L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| stationary/cws | Stationary | `300` | `1` | L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| stationary/gdf009 | Stationary | `1000` | `1` | L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| stationary/m2mg | Stationary | `150` | `1` | L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| stationary/phalanx | Stationary | `1000` | `1` | L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| stationary/ssmbattery | Stationary | `1000` | `1` | L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| tank/aav7a1 | IFV/APC | Needs validation; different owner key | Needs validation; different owner key | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| tank/abrams | MBT | `1200` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| tank/bradley | IFV/APC | `1000` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| tank/cv90 | IFV/APC | `1000` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| tank/gepard | AA | `1000` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| tank/leopard | MBT | `1200` | `1` | L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |

## Proposals awaiting the operator

These rows retain source values. Durability validation is excluded from this run. No recording is planned.

| Proposed stat | Sourced value | Validation step and prediction |
|---|---|---|
| Configured CB90 health | MaxHealth 1000; L3001/L3009 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| MBT configured health comparison | Abrams/Leopard 1200; Bradley/CV90 1000; L3010 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |
| Helicopter configured health comparison | AH6M 700; UH60 1500; L3008 | source value with effect unconfirmed; durability validation excluded for Season 5; unconfirmed; no recording planned. |

Other effects remain findings: unconfirmed; no recording planned.

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

## Gadget and vehicle semantics without recordings (L640-L650)

Run: `2026-09-30T234837-0400-gadget-vehicle-semantics`. This instruction supersedes the earlier recording and in-game test proposals in this document. Each stat uses one or more of these labels: **confirmed via weapons**, **confirmed via EA text**, **confirmed via a cited community in-game test**, or **source value with effect unconfirmed**. Confirmation applies only to the exact field and meaning stated; a mixed row does not promote every effect. No community test has been promoted. EA/UI statements require an exact version and source-owner match before they confirm a Frosty field.

The parent transfer census covers all 39 gadget rows, 17 vehicle shared rows and every saved family stat-map row. L641-L644 retain 57 vehicle firing owners. L650 adds the 12 AA/scout owners as a pre-update baseline labelled **changes in Season 5**. All 69 owners are retained; vehicle durability validation remains excluded. L645/L648 retain 26 gadget/underbarrel firing owners, including explicit source-only throwable rows. Four selected vehicle WF routes and unselected gadget variants keep their scope limits. No identity search was reopened.

M4A1 and L115 controls pass exact IEEE float32 source equivalence; literal float64 differences remain explicit. Configured capacity, rate, reload operands and launch vector transfer by exact class key and field identity. Matched infantry projectile owners also transfer gravity/drag and supported selected tweakable damage curves. Effective reload selector, guided flight, native activation and composed damage remain unconfirmed.

All 23 EA update snapshots are read and their summary fields are filled, preserving the inventory's `articles` list. L649 retains 17 UI mechanic quantities with unlinked gameplay owners. The statement ledger records missing version-matched operands and apparent cross-version differences without promoting a field from an item name. C4, Claymore and M4 SLAM remain in scope; the earlier broad Mines/charges exclusion in the L640 census is superseded. Named Season 5 AA/mine changes are retained as baselines and statements, with no durability or validation claim.

Current draft profiles, statements, community map, parent review and final commit receipts are in the run folder. No site data, simulation or UI changed. Any remaining effect: **unconfirmed; no recording planned**.

Local commits: L640 research `df51417`, site `d1b2361`; L641-L651 research `7ee81d8`, site index `baff78b`. Parent controls, raw reads and committed-content review pass. The records check has zero errors. Run-folder cleanup removed zero links and zero files. The run is closed; no further source lead or recording is queued.

## Patch-note candidate context (1 October 2026)

[Coverage receipt](../../reference-data/provenance/frosty-2026-10-01-patch-notes-coverage.json) cross-references 724 vehicle mentions, including 618 unmapped state/rule/fix mentions. The full candidate-stat grouping, source dates, update versions, URLs, affected items and stated numbers is in `2026-10-01T001542-0400-patch-notes-coverage/vehicle-patch-candidates.json` under the weapon-analyzer-research reports. This is additional official-article context for the existing candidate list, not a new semantic measurement or duplicate L640-L679 lead.

The cross-reference groups announced quantities and rules by their article mechanic. Existing configured firing/resource profiles remain separate from effective damage, blast, health, guidance, spotting and activation. Generic patch fixes are kept unmapped rather than credited to an unrelated scalar. Review those contexts when selecting an existing candidate route; require its exact owner and same-owner control. Season 5 and BR-only/SP-only items are excluded; historical and preview context stays labeled.

## Current vehicle baseline and field frontier (L3034 onward)

The `2026-10-01T011608-0400-vehicles-open-frontier` run is closed. The operator authorized an open source frontier at L3034 upward, including limits. Drift and usage stops do not apply to this run. UI identity searches remain parked. No site data, simulation, UI, push or recording is authorized.

Current raw is 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. All 46 exact roots are present. Guarded capture added 18 missing roots. Current source operands have exact owners, offsets, bytes and raw hashes. Every baseline value is **pre-Season 5 baseline; meaning unconfirmed**. Durability validation stays excluded.

[L3034](../../reference-data/provenance/frosty-2026-10-01-L3034-vehicle-baseline.json) retains all 46 health/regen/disable and selected damage-zone/armor source pictures: 183 local descriptor families and 27,473 checked raw reads across 85 files. The CB90 same-owner MaxHealth control is 1000 at offset 440, bytes `00007a44`; parent review and independent raw reread pass. Different schemas retain hash-only fields. No health, regeneration, armor or disable equation is asserted.

[Baseline](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T011608-0400-vehicles-open-frontier/L3034/baseline.json), [field inventory](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T011608-0400-vehicles-open-frontier/L3034/local-field-inventory.json) and [dead ends](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T011608-0400-vehicles-open-frontier/where-not-to-look.json) are saved. Each batch commits its compact dead ends inside one receipt. The scoped forward source frontier is exhausted. Native and exact-identity limits remain recorded with reopen conditions.

[L3035](../../reference-data/provenance/frosty-2026-10-01-L3035-vehicle-frontier.json): All 73 selected WF routes have current raw. They contain 72 firing owners: 69 have the exact infantry control key. The three new CRAM/RWS firing owners have a different key; the flare route is an array-only owner. All 83 non-null Shot projectile selections have exact current file/exported-object joins. The 27 selections with the controlled infantry projectile key retain gravity/drag and separate curve channels. Other owners stay hash-only. The 43 tested infantry selections do not supply a matching owner control for those other classes. Empty tweakable arrays remain empty; primary-health curves never substitute for them. Effective damage, reload, guidance and firing behavior remain unconfirmed. All 12 AA/scout selections retain full source replenishment/reload/heat fields as changes in Season 5. The parent independently reads the alternate CRAM Field_14c4a054 source operand as 1200 at offset 744, bytes `00009644`. This is hash-only source evidence, not an RPM claim for the alternate key. The M4A1 control and worker review pass; 32,293 unique raw reads pass.

[L3036](../../reference-data/provenance/frosty-2026-10-01-L3036-vehicle-frontier.json): All 46 roots have exact selected MM/MD coverage across 78 assets. The saved atlas retains 33,364 local owners, 7,195,338 raw operand reads and 64,863 source edges. Large raw payloads are compressed per asset; all payload hashes pass. All 218 selected descriptor schemas retain their exact keys and member types. There are no missing selected routes or traversal errors. 11,346 owners retain layoutAmbiguous markers; field-name transfer and absence claims are excluded for them. Speed units, acceleration/handling equations, turret rates and usable seats remain unconfirmed. Current same-owner CB90 MM and AAV7A1 MD hash-only pointer controls pass. The parent independently rereads the CB90 MM pointer at offset 66264 as -3536, bytes `30f2ffff`. Pointer/source labels do not establish an operation or physical unit.

[L3037](../../reference-data/provenance/frosty-2026-10-01-L3037-vehicle-frontier.json): All 46 current roots have selected VB issuing consumers and forward Ability/U/WF/WMD, lock/guidance and repair/resupply source fields retained. The atlas covers 3,271 selected owners, 118,985 raw reads, 6,824 target identity joins and 2,612 array-count reads. The selected pass has zero named raw gaps. Twelve exported-owner identities and two channel imports remain unresolved. The two channel file GUIDs have no match in the current 467,208-asset catalog; this is a source boundary, not an absent mechanic. Loadout artifacts record explicit source selections; default loadouts and availability remain null. The same-owner current smoke graph control passes. The parent independently reads a selected SP vehicle magazine modifier Float32 as 1 at offset 168, bytes `0000803f`; this does not establish an active modifier. Duration, charge/cooldown units, lock-break effects, repair/resupply composition and native receivers remain unconfirmed. Canonical full-precision numeric values are `rawChecks[].value`; the generic decoder `decodedValue` may be rounded display data.

[L3039](../../reference-data/provenance/frosty-2026-10-01-L3039-vehicle-frontier.json): All 22 vehicle community items are traced in rank order. Each item names current root candidates, exact issuing owners, reviewed controls and the selected firing/projectile, motion or Ability source proofs. Exact reachable graph owners remain separate from independent candidates. The source ledger does not establish active primary/secondary/gunner slots, equipment upgrades, team entry permission, Thermal Smoke duration/charges/cooldown/lock break, or vehicle supply composition. Dating and title/chapter ambiguity remain visible. No community value or validation claim is imported. The parent independently rereads the controlled MBT primary firing scalar as 900 at offset 1104, bytes `00006144`. This is a serialized source operand; active cadence and slot identity remain unconfirmed. Twenty-two compact dead-end rows identify the missing field-specific control or native receiver and the evidence that would reopen each item.

[L3038](../../reference-data/provenance/frosty-2026-10-01-L3038-vehicle-frontier.json): The frozen forward source frontier covers 1,607 current files, 983 schemas and 5,540 exact declaring-key/member families. Statuses are 9 in the stat map, 5,517 traced but not mapped and 14 known limits. All typed layouts were examined. The traced classification includes 2,915 families with layout inventory only; it does not mean that every family has a controlled value or native operation. Priority handling/boost/curves, countermeasure/lock/repair/resupply and turret/aiming source candidates have supplemental evidence across 171 files, 684 families and 46,399 raw reads. Dense MM/MD and reviewed Ability payloads are reused. No named eligible raw route remains missing. The parent independently rereads a WingData Float32 operand as 1.2000000476837158 at offset 184, bytes `9a99993f`; the generic display value is 1.2. Canonical numeric values are `rawChecks[].value`. Three unresolved object imports on two Marauder ownership file GUIDs have no match in the current catalog. They remain exact source limits, not absent-mechanic claims. The atlas keeps previous and current examination states, exact evidence pointers, ambiguous layouts and reopen conditions.

Close-out: all six batches are reviewed and committed with private indexes and atomic ref updates. The frozen scope is 46 roots, 1,607 files, 5,540 typed field families and 22 ranked community items. No named eligible current raw route remains missing. Native meaning remains unconfirmed. [Fresh handoff](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T011608-0400-vehicles-open-frontier/handoff.md) lists evidence, limits, exact local commits and operator video candidates. Final artifact hash and foreign generated-entry checks pass; the record check has zero errors and four existing warnings.

Research commits: L3034 `7ac780a`, L3035 `f4f51fd`, L3036 `d331b06`, L3037 `fa0c049`, L3038 `b1515b7`, L3039 `a40073e`. Generated site-index commits: L3034 `5dd0ca0`, L3035 `c858126`, L3036 `992ca1d`, L3037 `716737a`, L3038 `3f8ce9f`, L3039 `9d1da9a`. Cleanup retained both cited large files; zero links or files removed.

<!-- gadget-vehicle-display-2026-10-01-start -->
## Current run: displayable gadget and vehicle stats

Run: `2026-10-01T084100-0400-gadget-vehicle-display`. Closed: Stages 1, 2 and 3 are complete. All workers have stopped. The named source frontier is exhausted at the recorded receiver, unit, selection and composition boundaries. The vehicle source values retain the 1 October pre-Season 5 baseline. No vehicle value was re-extracted.

The proposed pages can show exact UI text and stated quantities, dated EA statements, and configured source profiles with their confidence, source version and scope. Curated item/card associations are labelled name-matched. UI-to-gameplay identity joins stay parked. Configured field meaning is separate from effective gameplay meaning. Effective damage, physical radius, duration, cooldown, charges, vehicle health/repair, countermeasure effects and lock behavior stay unresolved where a selected receiver contract is absent. Do not fill these fields with zero or convert source scalars to physical units without proof.

Coverage: L224 maps all 39 gadget comparison rows and 181 parts; L227 covers all 28 original gadget proposals and 227 named associations. The two sets overlap and are not unique-stat counts. L3040 maps all 77 original vehicle candidate rows and 355 components, including 173 unresolved effective components. L3042 transfers five exact configured OverHeat field names to 72 saved vehicle firing owners (360 unchanged operands). L228 verifies 26 current gadget firing owners (130 operands); two missing gadget captures were taken through the shared lock and match the original bytes. The original source Head and raw-hash carry-forward proof remain separate.

L226 and the L227/L228 supplements define the proposed gadget schema. L3043 defines the proposed vehicle schema. Both specify fields, units, source routes, confidence and validation basis. Their completed research records are findings; future page implementation remains a proposal that needs separate authorization. The run handoff and compact `where-not-to-look.json` preserve exact reopen conditions. No recording is proposed. No site or generated file was edited or committed, and nothing was pushed.

Method switch: after two batches produced mostly semantic limits, the run changed from graph expansion to exact infantry own-wrapper naming controls and separate source/text schemas. This produced the configured heat-field transfers without inventing effective heat formulas or percent units.

Validation: all nine lead receipts pass `frosty-records.py check-receipt`; consequential source operands were independently re-read. The EA inventory stayed read-only. Each local commit used a separate index seeded from HEAD and preserved other sessions' paths and hunks. One duplicate old hash citation in L227 is retired by the closing audit; the current audit artifact and findings are unchanged. The shared cleanup is complete: zero links and zero files removed, zero bytes freed. The report and cleanup.json are in the run folder. [Closing audit](../../reference-data/provenance/frosty-2026-10-01-gadget-vehicle-display-close-audit.json).

Lead commits: L224 `0bba62e1a80f5b7ef0c14fd696ac469e5f9f3c1c`; L225 `7bf1e839a3979be3b42efb28f8a38849cae72669`; L226 `a62a59c7ecbefb89902f48ce3f7352a0b8d951dc`; L227 `4ce71b55e379e2315d5aa20dcab969c4d185ff96`; L228 `0b5d23284bc1ee5028c7fe2f5acee691404949bf`; L3040 `2f6f01672c9fd74d7aac9c3b96f6b008fc26b302`; L3041 `4d0c5640015c7921734dc08a282d36be36d4c1e7`; L3042 `7268c03d3741ee65dee6c194fc5f980ad827452c`; L3043 `1ce5ada8d08393591cdaae55dca155ae8c5809db`

### L3041 reviewed

Ten high-impact vehicle questions have source facts and exact reopen conditions in [vehicle findings](../frosty/VEHICLES.md). Effective damage, health, repair, timing and locks remain unresolved. Reused values keep the pre-Season 5 label. The batch passes worker review, check-receipt and parent operand re-reads.

### L3040 reviewed

All 77 original candidate rows are covered by the reviewed support matrix and [vehicle findings](../frosty/VEHICLES.md). Configured, attributed statement and effective components have separate labels. The schema can use exact configured fields and dated/card statements; effective gameplay values remain unresolved. Nine card seat counts and two card armament counts stay attributed to their cards, without family identity joins.

### L3042 reviewed

Five configured OverHeat names now have exact infantry declaring-key/member support on 72 saved vehicle owners (360 unchanged values). See [vehicle heat findings](../frosty/VEHICLES.md). Units, percentage scale, active heat gate and effective heat/cooldown remain unresolved. The historical EA high-velocity statement and current source scalar stay separate.

### Proposed vehicle page stat schema (L3043)

The page can show exact vehicle/card text, attributed card quantities, dated EA statements and configured profiles for exact selected source owners. A curated card/family association is labelled name-matched. Keep the source baseline marked pre-Season 5. Effective gameplay values remain unset where native selection, units or composition are unresolved.

Each stat uses `field`, `valueKind`, `value`, `unit`, `sourceRoute`, `confidence`, `validationBasis`, `identityBasis`, `sourceVersion` and `scope`. Keep original source Head/descriptor/hash and separate carry-forward proof. Do not treat a card statement, patch change or selected alternative as a family gameplay value/default.

| Proposed fields | Units | Source route | Confidence | Validation basis and prediction |
|---|---|---|---|---|
| Card name, role/target/seat-exposure text; loadout/customization description | text | UIVehicleArchetypeMetadata, UIVehicleLoadoutPresetMetadata, UIVehicleMetadata and customization siblings, L3023/L3040 | source value with stated UI or EA support | Re-resolve the exact metadata pointer/string ID. Prediction: card text agrees; family identity stays name-matched. |
| Stated card seats and counted card armaments | stated seats/weapons | Nine L3023 cards plus dual AA autocannons/two transport miniguns, L3040 | source value with stated UI or EA support | Re-read the exact card quantity. Prediction: its statement agrees. Usable family seats, switching and active armaments remain unset. |
| Configured MaxHealth, RepairRateModifier, disable/clear thresholds | source health/modifier/threshold units; effective HP or HP/s unconfirmed | Exact VB root/local owner/key/member, L3001/L3010/L3034/L3041 | source value only; precise EA mechanic statements are separate supported fields | Reproduce exact own-wrapper/member control and raw read (CB90 1000; modifier 1). Prediction: configuration agrees; no effective health/repair/disable equation follows. |
| Selected armament, Ability/passive/countermeasure alternatives and station definitions | source identities/indices | VB selected components -> WF/Ability/U/WMD; entry/station definitions, L3035/L3037 | source value only | Re-read exact pointer/export identity. Prediction: source selection agrees. Active/default slot, availability and usable stations remain unresolved. |
| Configured MagazineCapacity, RateOfFire, ReloadTime, ReloadTimeBulletsLeft, ReloadSpeed | configured count, source rate/timing units or factor | Exact matched WF firing/Ammo/reload declaring keys/members, L640-L644/L3035/L3040 | confirmed meaning only for exact matched configured fields | Reproduce same-owner infantry naming control and source operands. Prediction: configuration agrees. Observed/sustained rate and effective selected reload remain unset. |
| NumberOfMagazines, InitialAmmo, replenishment flags/rounds/delay | source integer/boolean/scalar; sentinel meaning unresolved | Exact selected WF Ammo block, L3035/L3040 | source value only | Re-read exact member and retain -1. Prediction: operand agrees. Loaded/reserve rounds, refill amount/delay and unlimited-ammo claims remain unresolved. |
| Configured launch x/y/z and matched gravity/drag/curve operands | source vector/scalar units; effective physics/composed damage unconfirmed | Exact selected Shot -> matched PD/curve representation, L3035/L3040 | confirmed meaning for exact matched members; other owners source value only | Re-read full vector, projectile selection and exact key/member. Prediction: source operands agree. Guided path/drop/impact/material composition remain unset. |
| Configured OverHeat fields where L3042 proves an exact declaring-key/member match | source heat/timing units; effective model and percent scale unconfirmed | Selected WF Field_43a8d9ab -> exact OverHeat declaring key; L35 M27IAR own-wrapper control -> L3042 | confirmed meaning for the five configured field names only | Reproduce exact infantry key/member/name control and consequential vehicle raw reads. Prediction: each stored operand agrees. Do not infer an active heat gate, shots to overheat, cooldown or percentage from names alone. |
| Direct/blast/shockwave/curve source channels and damage-zone/armor inventories | source channel units where mapped; effective damage/physical coverage unknown | WF -> selected PD/PB/curve; VB -> selected zone/armor owners, L3034/L3035 | source value only; precise UI/EA text is a separate supported statement | Verify exact selected owner/member/channel. Prediction: serialized sources agree. Directional damage, weak spots, effective HP and total damage require the selected receiver equation. |
| Countermeasure charges/duration/cooldown/lock break; lock range/time/guidance | unknown for effective values | Exact selected issuing/Ability/U/WMD/tag/lock owners, L3037/L3041 | unresolved for effective stat; attributed EA descriptions/quantities supported separately | Obtain the named field-specific receiver and unit/dispatch contract. Prediction: the exact mechanic and active selection are established before any gameplay number is populated. |
| Speed/boost/climb, acceleration/braking/turning/stability, traverse/elevation, drone range/deployment/access | unknown for effective values | Selected MM/MD/wing/turret/control/entry owners, L3036/L3038/L3040 | unresolved for effective stat; source inventory stays context without invented physical names | Require a controlled receiving operation and unit/mode/state contract. Prediction: physical meaning and activation are established; state labels/tuples alone do not populate these values. |
| Dated EA mechanic statement | article's stated unit/text/version | Read-only inventory -> saved article URL/version/line/statement ID, L646/L647/L3040/L3041 | source value with stated UI or EA support as a dated statement | Recheck snapshot hash and named line. Prediction: article states that mechanic/quantity. Historical/preview changes stay separate from current baseline values. |

The exhaustive schema is `L3043/proposed-schema.json` in the run folder. It maps every final L3040 component to a source or statement route, confidence and validation basis. The L3042 heat supplement is separate so the older support matrix is not rewritten. Effective values remain null; null is not zero. No new vehicle value is extracted.

### Seat layer (operator, 1 October 2026)

Seats are a required level of the vehicle page. The MBT driver and gunner, for example, have different weapons and capabilities, so one combined loadout per vehicle would mislead. The page is organized as vehicle → seat → that seat's equipment. Each stat row above attaches to a vehicle when it is vehicle-wide (health, repair, mobility) and to a seat when it belongs to a station (armament, ammunition, heat, countermeasures, lock, gadgets, upgrades).

| Seat field | Meaning | Source route | Confidence until mapped |
|---|---|---|---|
| `seatIndex` | Station order in the vehicle's entry list | VB root → exact entry/station owner, L3007-L3017/L3036 | source value only |
| `role` | driver, gunner, pilot, passenger or other stated role | Entry owner plus card or EA role text | unresolved |
| `weapons`, `abilities`, `upgrades` | Equipment the station selects, with alternatives kept separate from defaults | Entry/station owner → exact WF/Ability/U/WMD selection, L3035/L3037 | unresolved |
| `canFire`, `exposed` | Whether the seat has a weapon and whether the occupant is exposed | Station definition plus card seat-exposure text | unresolved |
| `seatCountCheck` | Mapped stations agree with the card's stated seat count (MBT 2, IFV 6, light transport 5, armored transport 4, AA 1, attack helicopter 2, transport helicopter 5, attack jet 1, fighter jet 1) | L3023 cards | source value with stated UI support |

Seat-to-equipment mapping is the next vehicle research step (seat-mapping run, L3100 onward; MBT and IFV first). Weapon owner names that say Primary, Secondary, Coax or Gunner are hints only; a mapping needs an exact pointer chain from the root's station to the selected owner.

#### Operator-confirmed seat roles (1 October 2026)

The operator confirmed these roles from in-game knowledge (no recording). The equipment column is the L3101 source selection for that entry. Roles are labelled operator-confirmed, not source-established.

| Vehicle | Entry | Role | Equipment (L3101 source selection) |
|---|---|---|---|
| MBT (Abrams, Leopard) | 0 | Driver; fires the main gun and coax | 120 mm main gun; CoaxLMG or CoaxHMG alternatives |
| MBT (Abrams, Leopard) | 1 | Gunner; remote weapon station | RWS HMG, AGL or LMG alternatives |
| MBT (Abrams, Leopard) | 2-3 | Passengers | No configured weapon |
| IFV (Bradley, CV90) | 0 | Driver; fires the main gun and missiles | APFSDS-T, HEAB, Canister; Light Rockets, TOW or homing ATGM |
| IFV (Bradley, CV90) | 1 | Gunner; remote weapon station | RWS HMG, AGL, LMG or target designator |
| IFV (Bradley, CV90) | 2-5 | Passengers | No configured weapon |

The operator also confirmed the remaining multi-seat vehicles (1 October 2026). Equipment is the L3101-L3112 source selection for each entry.

| Vehicle | Entry | Role | Equipment (source selection) |
|---|---|---|---|
| AH-64E, Eurocopter | 0 | Pilot | Light, heavy or smart rockets; TOW or air-to-air missile |
| AH-64E, Eurocopter | 1 | Gunner | Chaingun; locking missile |
| AH-6M | 0 | Pilot | Minigun, GAU-19 or LR30; Hellfire, light or smart rockets, or air-to-air missile |
| AH-6M | 1 | Passenger with support tools | Thermal scanner, directional jammer, target designator |
| AH-6M | 2-3 | Passengers | No configured weapon |
| UH-60 | 0 | Pilot | No configured weapon |
| UH-60 | 1-2 | Door gunners | Minigun each |
| UH-60 | 3-4 | Passengers | No configured weapon |
| Gepard | 0 | Single crew seat | AAGP, AAAP or AAHV cannon; anti-air, high-velocity or aim-guided missile |
| AAV7A1 | 0 | Driver | No configured weapon |
| AAV7A1 | 1 | Gunner | RWS HMG or AGL |
| CB90 | 0 | Driver | M230LF or GAU-19; RBS70 or Mistral; coax LMG; torpedo or naval mines |
| CB90 | 1 | Gunner | 120 mm mortar: HE, smoke, guided, airburst or illumination |
| RHIB | 0 | Driver | No configured weapon |
| RHIB | 1 | Gunner | Open HMG |
| RHIB | 2-3 | Passengers | No configured weapon |
| JLTV, Marauder | 0 | Driver | No configured weapon |
| JLTV, Marauder | 1 | Gunner | RWS HMG, AGL or LMG |
| JLTV, Marauder | 2-3 | Passenger gunners | RWS LMG each |
| F-14 | 0 | Pilot | Cannon; air-to-air missile |
| F-14 | 1 | Second seat | AIM-54; semi-active radar missile |
| F/A-18F | 0 | Pilot | Cannon; air-to-air or anti-radiation missile; Zuni rockets; Rockeye bomb |
| F/A-18F | 1 | Second seat | Semi-active radar missile; bunker buster bomb; TV missile |

Single-seat jets and stationary weapons need no role mapping; their one entry is the operator seat.

The MH-47 is out of scope (operator, 1 October 2026). It appears only in the round-start insertion animation and is not a playable multiplayer vehicle. Do not map its seats or include it on the vehicle page.

Also out of scope: the Couch (Car_Couch), a REDSEC Easter egg rather than a multiplayer vehicle (operator, 1 October 2026), and the single-player or cinematic variants whose root names contain _SP, SP_, _Cine or _CarChase.

MBTs have 4 seats in multiplayer: 2 crew and 2 passengers. The archetype card's "2" counts crew seats, so the L3101 count check (4 entries against the card's 2) is explained rather than a conflict. The IFV card's 6 is the total (2 crew, 4 passengers). Entry-to-role assignment for these two families rests on the confirmed equipment split. Defaults among the alternatives are still unresolved; the next step is a loadout-preset pass.

| Proposal | Affected data/code | Evidence and remaining validation |
|---|---|---|
| L3043: vehicle page schema | Future vehicle page only; no implementation in this run | L3040/L3041 support and limits plus L3042 exact configured heat names. Display attributed text/configured profiles with source/confidence/scope labels; effective values require the named contracts. |
<!-- gadget-vehicle-display-2026-10-01-end -->

### Tank directional damage: known answers (operator, 1 October 2026)

These are the checks for the tank weak-spot research. Tank root health is 1200 for Abrams and Leopard and 1000 for Bradley, CV90 and AAV7A1 (L3010, L3203); the 1000 for an MBT is each damage part's own value (L3034 CB90 control, L3201). The hits-to-kill column below uses the operator premise of 1000. L3034 retains 8 damage-part owners per MBT (six at 1000, two at 100) and a per-part field Field_64b3e9cd of 0.7 on five parts and 0 on three; part names, directions and that field's meaning are unresolved.

| RPG-7V2 hit | Damage | Fraction of rear | Hits to kill (1000) | Basis |
|---|---|---|---|---|
| Front | 188 | 0.376 | 6 | EA 1.3.3.0 stated range minimum |
| Side | 375 | 0.75 | 3 | Creator in-game test (BO4KOGaming Short, 9 Jul 2026, after the Season 3 gunplay update); corroboration only |
| Rear | 500 | 1.00 | 2 | EA 1.3.3.0 stated range maximum; operator: two rear RPGs destroy a tank |

Operator answers from play, 1 October 2026 (no recording): one RPG to the side plus one to the rear does not kill a tank, by design; maximum damage needs a straight-on hit from behind. The Abrams angle-damage curves (side x1.9, rear x3.2 flat between 76 and 104 degrees) fit the pattern, but both answers are also predicted by the EA and creator numbers alone, and the curves do not reproduce the EA ratio of about 2.66 (see [angle-damage curves](../frosty/VEHICLES.md#angle-damage-curves-reviewed-addendum-1-october-2026)). Leopard, Bradley and AAV7A1 have no curve pointer in the selected owners. Source value with effect unconfirmed; no recording planned.

EA 1.3.1.0 and 1.3.3.0 state tank damage ranges for manually aimed weapons, all with the same maximum-to-minimum ratio (about 2.66): RPG-7V2 188-500, M136 AT 207-550, MBT 120 mm APFSDS and aim-guided shell 244-650, attack-helicopter heavy rockets 120-320, IFV light rockets 75-200. Lock-on and placed weapons state one value (IFV lock-guided missile 450, C-4 350, MBT-LAW 240), consistent with EA's note that lock-on damage does not depend on zone or angle. A vehicle page may show these as EA-stated values. No later patch note through 1.4.3.5 restates RPG-versus-tank damage.

## Vehicle seat mapping current run (L3100-L3149)

The source pass is closed at 1.4.3.5, Head 4909002. L3100-L3112 cover all 46 exact roots / 38 families in the prior census, including the MQ9 and TRV150 supplement. The 137 entries are source definitions. They do not establish usable player seats. 143 WF selections and 426 equipment configuration references retain their exact chains and raw checks. Role, capability kind, default, canFire, exposed and activation remain unresolved where the controlled source cannot name them.


### L3101 seat rows

Seat rows use the serialized source index. Equipment counts retain exact selected owner identities; they do not give active slots.

| Vehicle / root | seatIndex | role | weapons | capabilities | abilities / upgrades / countermeasures | canFire / exposed |
|---|---|---|---|---|---|---|
| tank/abrams / VB_VEH_Tank_Abrams | 0 | unresolved | 3 exact WF selections | 19 exact identities | unresolved split | unresolved |
| tank/abrams / VB_VEH_Tank_Abrams | 1 | unresolved | 3 exact WF selections | 11 exact identities | unresolved split | unresolved |
| tank/abrams / VB_VEH_Tank_Abrams | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/abrams / VB_VEH_Tank_Abrams | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/bradley / VB_VEH_Tank_Bradley | 0 | unresolved | 6 exact WF selections | 15 exact identities | unresolved split | unresolved |
| tank/bradley / VB_VEH_Tank_Bradley | 1 | unresolved | 4 exact WF selections | 12 exact identities | unresolved split | unresolved |
| tank/bradley / VB_VEH_Tank_Bradley | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/bradley / VB_VEH_Tank_Bradley | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/bradley / VB_VEH_Tank_Bradley | 4 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/bradley / VB_VEH_Tank_Bradley | 5 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/cv90 / VB_VEH_Tank_CV90 | 0 | unresolved | 6 exact WF selections | 15 exact identities | unresolved split | unresolved |
| tank/cv90 / VB_VEH_Tank_CV90 | 1 | unresolved | 4 exact WF selections | 12 exact identities | unresolved split | unresolved |
| tank/cv90 / VB_VEH_Tank_CV90 | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/cv90 / VB_VEH_Tank_CV90 | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/cv90 / VB_VEH_Tank_CV90 | 4 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/cv90 / VB_VEH_Tank_CV90 | 5 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/leopard / VB_VEH_Tank_Leopard | 0 | unresolved | 3 exact WF selections | 19 exact identities | unresolved split | unresolved |
| tank/leopard / VB_VEH_Tank_Leopard | 1 | unresolved | 3 exact WF selections | 11 exact identities | unresolved split | unresolved |
| tank/leopard / VB_VEH_Tank_Leopard | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/leopard / VB_VEH_Tank_Leopard | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |

Evidence: [L3101 receipt](../../reference-data/provenance/frosty-2026-10-01-L3101-vehicle-seat-map.json) and `L3101/seat-map.json` in the run folder. The source/card count comparison is in the topic-page lead section.

### L3102 seat rows

Seat rows use the serialized source index. Equipment counts retain exact selected owner identities; they do not give active slots.

| Vehicle / root | seatIndex | role | weapons | capabilities | abilities / upgrades / countermeasures | canFire / exposed |
|---|---|---|---|---|---|---|
| tank/aav7a1 / VB_VEH_Tank_AAV7A1 | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| tank/aav7a1 / VB_VEH_Tank_AAV7A1 | 0 | unresolved | 2 exact WF selections | 4 exact identities | unresolved split | unresolved |
| tank/gepard / VB_VEH_Tank_Gepard | 0 | unresolved | 6 exact WF selections | 24 exact identities | unresolved split | unresolved |

Evidence: [L3102 receipt](../../reference-data/provenance/frosty-2026-10-01-L3102-vehicle-seat-map.json) and `L3102/seat-map.json` in the run folder. The source/card count comparison is in the topic-page lead section.

### L3103 seat rows

Seat rows use the serialized source index. Equipment counts retain exact selected owner identities; they do not give active slots.

| Vehicle / root | seatIndex | role | weapons | capabilities | abilities / upgrades / countermeasures | canFire / exposed |
|---|---|---|---|---|---|---|
| helicopter/ah64e / VB_VEH_Helicopter_AH64E | 0 | unresolved | 5 exact WF selections | 13 exact identities | unresolved split | unresolved |
| helicopter/ah64e / VB_VEH_Helicopter_AH64E | 1 | unresolved | 2 exact WF selections | 4 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M | 0 | unresolved | 7 exact WF selections | 18 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M | 1 | unresolved | 3 exact WF selections | 6 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M_M05_SP_Cine | 0 | unresolved | 2 exact WF selections | 5 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M_M05_SP_Cine | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M_M05_SP_Cine | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M_M05_SP_Cine | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_SP_MH6M | 0 | unresolved | 2 exact WF selections | 5 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_SP_MH6M | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_SP_MH6M | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_SP_MH6M | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_SP_MH6M | 4 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/ah6m / VB_VEH_Helicopter_SP_MH6M | 5 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/eurocopter / VB_VEH_Helicopter_Eurocopter | 0 | unresolved | 5 exact WF selections | 12 exact identities | unresolved split | unresolved |
| helicopter/eurocopter / VB_VEH_Helicopter_Eurocopter | 1 | unresolved | 2 exact WF selections | 4 exact identities | unresolved split | unresolved |
| helicopter/eurocopter / VB_VEH_Helicopter_Eurocopter_SP | 0 | unresolved | 5 exact WF selections | 13 exact identities | unresolved split | unresolved |
| helicopter/eurocopter / VB_VEH_Helicopter_Eurocopter_SP | 1 | unresolved | 2 exact WF selections | 4 exact identities | unresolved split | unresolved |

Evidence: [L3103 receipt](../../reference-data/provenance/frosty-2026-10-01-L3103-vehicle-seat-map.json) and `L3103/seat-map.json` in the run folder. The source/card count comparison is in the topic-page lead section.

### L3104 seat rows

Seat rows use the serialized source index. Equipment counts retain exact selected owner identities; they do not give active slots.

| Vehicle / root | seatIndex | role | weapons | capabilities | abilities / upgrades / countermeasures | canFire / exposed |
|---|---|---|---|---|---|---|
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 1 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 2 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 3 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 4 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 5 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 6 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 7 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 8 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 9 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 10 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 11 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 12 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 13 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 14 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 15 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 16 | unresolved | 0 exact WF selections | shared context, unassigned | unresolved split | unresolved |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_SP | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 1 | unresolved | 1 exact WF selections | 4 exact identities | unresolved split | unresolved |
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 2 | unresolved | 1 exact WF selections | 4 exact identities | unresolved split | unresolved |
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 4 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |

Evidence: [L3104 receipt](../../reference-data/provenance/frosty-2026-10-01-L3104-vehicle-seat-map.json) and `L3104/seat-map.json` in the run folder. The source/card count comparison is in the topic-page lead section.

### L3105 seat rows

Seat rows use the serialized source index. Equipment counts retain exact selected owner identities; they do not give active slots.

| Vehicle / root | seatIndex | role | weapons | capabilities | abilities / upgrades / countermeasures | canFire / exposed |
|---|---|---|---|---|---|---|
| boat/cb90 / VB_VEH_Boat_CB90 | 0 | unresolved | 7 exact WF selections | 19 exact identities | unresolved split | unresolved |
| boat/cb90 / VB_VEH_Boat_CB90 | 1 | unresolved | 5 exact WF selections | 10 exact identities | unresolved split | unresolved |
| boat/jetski / VB_VEH_Boat_JetSki | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| boat/jetski / VB_VEH_Boat_JetSki | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| boat/rhib / VB_VEH_Boat_RHIB | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| boat/rhib / VB_VEH_Boat_RHIB | 1 | unresolved | 1 exact WF selections | 5 exact identities | unresolved split | unresolved |
| boat/rhib / VB_VEH_Boat_RHIB | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| boat/rhib / VB_VEH_Boat_RHIB | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |

Evidence: [L3105 receipt](../../reference-data/provenance/frosty-2026-10-01-L3105-vehicle-seat-map.json) and `L3105/seat-map.json` in the run folder. The source/card count comparison is in the topic-page lead section.

### L3106 seat rows

Seat rows use the serialized source index. Equipment counts retain exact selected owner identities; they do not give active slots.

| Vehicle / root | seatIndex | role | weapons | capabilities | abilities / upgrades / countermeasures | canFire / exposed |
|---|---|---|---|---|---|---|
| car/couch / VB_VEH_Car_Couch | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/couch / VB_VEH_Car_Couch | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/couch / VB_VEH_Car_Couch | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/couch / VB_VEH_Car_Couch | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/flyer60 / VB_VEH_Car_Flyer60 | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/flyer60 / VB_VEH_Car_Flyer60 | 1 | unresolved | 1 exact WF selections | 7 exact identities | unresolved split | unresolved |
| car/flyer60 / VB_VEH_Car_Flyer60 | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/flyer60 / VB_VEH_Car_Flyer60 | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/flyer60 / VB_VEH_Car_Flyer60 | 4 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/flyer60 / VB_VEH_Car_Flyer60_SP | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/flyer60 / VB_VEH_Car_Flyer60_SP | 1 | unresolved | 1 exact WF selections | 6 exact identities | unresolved split | unresolved |
| car/flyer60 / VB_VEH_Car_Flyer60_SP | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/flyer60 / VB_VEH_Car_Flyer60_SP | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/flyer60 / VB_VEH_Car_Flyer60_SP | 4 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/jltv / VB_VEH_Car_JLTV | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/jltv / VB_VEH_Car_JLTV | 1 | unresolved | 3 exact WF selections | 14 exact identities | unresolved split | unresolved |
| car/jltv / VB_VEH_Car_JLTV | 2 | unresolved | 1 exact WF selections | 5 exact identities | unresolved split | unresolved |
| car/jltv / VB_VEH_Car_JLTV | 3 | unresolved | 1 exact WF selections | 5 exact identities | unresolved split | unresolved |
| car/marauder / VB_VEH_Car_Marauder | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/marauder / VB_VEH_Car_Marauder | 1 | unresolved | 3 exact WF selections | 15 exact identities | unresolved split | unresolved |
| car/marauder / VB_VEH_Car_Marauder | 2 | unresolved | 1 exact WF selections | 5 exact identities | unresolved split | unresolved |
| car/marauder / VB_VEH_Car_Marauder | 3 | unresolved | 1 exact WF selections | 5 exact identities | unresolved split | unresolved |
| car/ptv / VB_VEH_Car_PTV | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/ptv / VB_VEH_Car_PTV | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/ptv / VB_VEH_Car_PTV | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/ptv / VB_VEH_Car_PTV | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |

Evidence: [L3106 receipt](../../reference-data/provenance/frosty-2026-10-01-L3106-vehicle-seat-map.json) and `L3106/seat-map.json` in the run folder. The source/card count comparison is in the topic-page lead section.

### L3107 seat rows

Seat rows use the serialized source index. Equipment counts retain exact selected owner identities; they do not give active slots.

| Vehicle / root | seatIndex | role | weapons | capabilities | abilities / upgrades / countermeasures | canFire / exposed |
|---|---|---|---|---|---|---|
| car/quadbike / VB_VEH_Car_QuadBike | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/quadbike / VB_VEH_Car_QuadBike | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/thebeast / VB_VEH_Car_TheBeast | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/thebeast / VB_VEH_Car_TheBeast | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/thebeast / VB_VEH_Car_TheBeast | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/thebeast / VB_VEH_Car_TheBeast | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/vector / VB_VEH_Car_Vector | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/vector / VB_VEH_Car_Vector | 1 | unresolved | 1 exact WF selections | 5 exact identities | unresolved split | unresolved |
| car/vector / VB_VEH_Car_Vector | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/vector / VB_VEH_Car_Vector | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/vector / VB_VEH_Car_Vector | 4 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/vector / VB_VEH_Car_Vector_M05_CarChase | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/vector / VB_VEH_Car_Vector_M05_CarChase | 1 | unresolved | 1 exact WF selections | 5 exact identities | unresolved split | unresolved |
| car/vector / VB_VEH_Car_Vector_M05_CarChase | 2 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/vector / VB_VEH_Car_Vector_M05_CarChase | 3 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| car/vector / VB_VEH_Car_Vector_M05_CarChase | 4 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| motorcycle/dirtbike01 / VB_VEH_Motorcycle_DirtBike01 | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| motorcycle/dirtbike01 / VB_VEH_Motorcycle_DirtBike01 | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| motorcycle/dirtbike02 / VB_VEH_Motorcycle_DirtBike02 | 0 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |
| motorcycle/dirtbike02 / VB_VEH_Motorcycle_DirtBike02 | 1 | unresolved | 0 exact WF selections | 0 exact identities | unresolved split | unresolved |

Evidence: [L3107 receipt](../../reference-data/provenance/frosty-2026-10-01-L3107-vehicle-seat-map.json) and `L3107/seat-map.json` in the run folder. The source/card count comparison is in the topic-page lead section.

### L3108 seat rows

Seat rows use the serialized source index. Equipment counts retain exact selected owner identities; they do not give active slots.

| Vehicle / root | seatIndex | role | weapons | capabilities | abilities / upgrades / countermeasures | canFire / exposed |
|---|---|---|---|---|---|---|
| airplane/f14 / VB_VEH_Airplane_F14 | 0 | unresolved | 2 exact WF selections | 4 exact identities | unresolved split | unresolved |
| airplane/f14 / VB_VEH_Airplane_F14 | 1 | unresolved | 2 exact WF selections | 5 exact identities | unresolved split | unresolved |
| airplane/f16 / VB_VEH_Airplane_F16 | 0 | unresolved | 4 exact WF selections | 9 exact identities | unresolved split | unresolved |
| airplane/f22 / VB_VEH_Airplane_F22 | 0 | unresolved | 3 exact WF selections | 6 exact identities | unresolved split | unresolved |
| airplane/fa18f / VB_VEH_Airplane_FA18F | 0 | unresolved | 6 exact WF selections | 12 exact identities | unresolved split | unresolved |
| airplane/fa18f / VB_VEH_Airplane_FA18F | 1 | unresolved | 3 exact WF selections | 7 exact identities | unresolved split | unresolved |
| airplane/jas39 / VB_VEH_Airplane_JAS39 | 0 | unresolved | 4 exact WF selections | 8 exact identities | unresolved split | unresolved |
| airplane/jas39 / VB_VEH_SP_Assault_Airplane_JAS39 | 0 | unresolved | 3 exact WF selections | 7 exact identities | unresolved split | unresolved |
| airplane/su57 / VB_VEH_Airplane_SU57 | 0 | unresolved | 3 exact WF selections | 6 exact identities | unresolved split | unresolved |

Evidence: [L3108 receipt](../../reference-data/provenance/frosty-2026-10-01-L3108-vehicle-seat-map.json) and `L3108/seat-map.json` in the run folder. The source/card count comparison is in the topic-page lead section.

### L3109 seat rows

Seat rows use the serialized source index. Equipment counts retain exact selected owner identities; they do not give active slots.

| Vehicle / root | seatIndex | role | weapons | capabilities | abilities / upgrades / countermeasures | canFire / exposed |
|---|---|---|---|---|---|---|
| stationary/bgm71tow / VB_VEH_Stationary_BGM71TOW | 0 | unresolved | 1 exact WF selections | 2 exact identities | unresolved split | unresolved |
| stationary/cws / VB_VEH_Stationary_Turret_CROWS | 0 | unresolved | 3 exact WF selections | 6 exact identities | unresolved split | unresolved |
| stationary/gdf009 / VB_VEH_Stationary_GDF009 | 0 | unresolved | 1 exact WF selections | 3 exact identities | unresolved split | unresolved |
| stationary/m2mg / VB_VEH_Stationary_M2MG | 0 | unresolved | 1 exact WF selections | 4 exact identities | unresolved split | unresolved |
| stationary/phalanx / VB_VEH_Stationary_Phalanx | 0 | unresolved | 1 exact WF selections | 2 exact identities | unresolved split | unresolved |
| stationary/phalanx / VB_VEH_Stationary_Phalanx_SP | 0 | unresolved | 1 exact WF selections | 2 exact identities | unresolved split | unresolved |
| stationary/ssmbattery / VB_VEH_Stationary_SSMBattery | 0 | unresolved | 1 exact WF selections | 1 exact identities | unresolved split | unresolved |

Evidence: [L3109 receipt](../../reference-data/provenance/frosty-2026-10-01-L3109-vehicle-seat-map.json) and `L3109/seat-map.json` in the run folder. The source/card count comparison is in the topic-page lead section.

### L3111 seat rows

Seat rows use the serialized source index. Equipment counts retain exact selected owner identities; they do not give active slots.

| Vehicle / root | seatIndex | role | weapons | capabilities | abilities / upgrades / countermeasures | canFire / exposed |
|---|---|---|---|---|---|---|
| airplane/mq9 / VB_VEH_Airplane_MQ9 | 0 | unresolved | 0 exact WF selections | 1 exact identities | unresolved split | unresolved |
| drone/trv150 / VB_VEH_Drone_TRV150 | 0 | unresolved | 0 exact WF selections | 1 exact identities | unresolved split | unresolved |

Evidence: [L3111 receipt](../../reference-data/provenance/frosty-2026-10-01-L3111-vehicle-seat-map.json) and `L3111/seat-map.json` in the run folder. The source/card count comparison is in the topic-page lead section.

### Seat schema and closeout

| Seat field | Stored evidence / representation | Requirement before site use |
|---|---|---|
| vehicle / variant | Exact VB route, root hash and source lead | Do not merge base, SP, Cine or remote variants |
| entry identity | Root route + entry object + actual class + local key | Use full identity; AAV7A1 has two different entries at stored index 0 |
| seatIndex | Field_c8750d4f raw word and typed check | UI numbering needs a semantic same-owner control |
| role | null; entry chain retained | Join a role to this exact entry; EA family roles alone are insufficient |
| weapons | Exact WF selections with component/import/export GUID chains and raw checks | Keep alternatives separate; do not infer default or active slot |
| equipment configuration references | Exact U / WMD / Ability and other selected identities; component imports retained separately | Resolve capability kind and activation before classifying |
| abilities / upgrades / countermeasures | null when semantic split is unresolved | A route label alone does not establish kind or player availability |
| default / selected alternative | default null; source alternatives retained individually | Exact selector and default control required |
| canFire / exposed | null; serialized candidate fields and raw checks retained | Exact semantic field and same-owner control required |
| shared component context | One retained context with exact entry links; per-entry assignment null | Do not copy shared equipment onto each entry |
| card count | Per-root source total and operator comparison in count-checks.json | Retain disagreement; resolve exact card-to-root identity |
| evidence | Path, SHA-256, offset, bytes, typed value and chain per consequential operand | Keep run artifacts; no generated index build in this run |

Count reconciliation:

| Exact root | Source entries | Operator card comparison | Identity limit |
|---|---|---|---|
| VB_VEH_Tank_Abrams | 4 | MBT 2: differs | operator group comparison |
| VB_VEH_Tank_Bradley | 6 | IFV 6: agrees numerically | operator group comparison |
| VB_VEH_Tank_CV90 | 6 | IFV 6: agrees numerically | operator group comparison |
| VB_VEH_Tank_Leopard | 4 | MBT 2: differs | operator group comparison |
| VB_VEH_Tank_AAV7A1 | 2 | armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Tank_Gepard | 1 | AA 1: agrees numerically | operator group comparison |
| VB_VEH_Helicopter_AH64E | 2 | attack helicopter 2: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_AH6M | 4 | attack helicopter 2: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_AH6M_M05_SP_Cine | 4 | attack helicopter 2: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_SP_MH6M | 6 | attack helicopter 2: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_Eurocopter | 2 | attack helicopter 2: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_Eurocopter_SP | 2 | attack helicopter 2: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 16 | transport helicopter 5: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_MH47_SP | 1 | transport helicopter 5: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_UH60 | 5 | transport helicopter 5: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Boat_CB90 | 2 | No stated count | no stated card count |
| VB_VEH_Boat_JetSki | 2 | No stated count | no stated card count |
| VB_VEH_Boat_RHIB | 4 | No stated count | no stated card count |
| VB_VEH_Car_Couch | 4 | light transport 5: differs; armored transport 4: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Car_Flyer60 | 5 | light transport 5: agrees numerically; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Car_Flyer60_SP | 5 | light transport 5: agrees numerically; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Car_JLTV | 4 | light transport 5: differs; armored transport 4: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Car_Marauder | 4 | light transport 5: differs; armored transport 4: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Car_PTV | 4 | light transport 5: differs; armored transport 4: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Car_QuadBike | 2 | light transport 5: differs; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Car_TheBeast | 4 | light transport 5: differs; armored transport 4: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Car_Vector | 5 | light transport 5: agrees numerically; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Car_Vector_M05_CarChase | 5 | light transport 5: agrees numerically; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Motorcycle_DirtBike01 | 2 | light transport 5: differs; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Motorcycle_DirtBike02 | 2 | light transport 5: differs; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_F14 | 2 | attack jet 1: differs; fighter jet 1: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_F16 | 1 | attack jet 1: agrees numerically; fighter jet 1: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_F22 | 1 | attack jet 1: agrees numerically; fighter jet 1: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_FA18F | 2 | attack jet 1: differs; fighter jet 1: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_JAS39 | 1 | attack jet 1: agrees numerically; fighter jet 1: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_SP_Assault_Airplane_JAS39 | 1 | attack jet 1: agrees numerically; fighter jet 1: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_SU57 | 1 | attack jet 1: agrees numerically; fighter jet 1: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Stationary_BGM71TOW | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_Turret_CROWS | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_GDF009 | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_M2MG | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_Phalanx | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_Phalanx_SP | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_SSMBattery | 1 | No stated count | no stated card count |
| VB_VEH_Airplane_MQ9 | 1 | No stated count | no stated card count |
| VB_VEH_Drone_TRV150 | 1 | No stated count | no stated card count |

Results: the entry and selected-owner source coverage is complete. MBT count checks fail against the supplied card count; IFV checks agree. Selected equipment remains separate from defaults. Unknown imported targets and shared assignment limits are visible. No site changes or validation recordings are proposed.

Limits: Source entry and equipment containment is mapped. Complete active player seat loadouts are not established. seatIndex is the stored Field_c8750d4f candidate. UI numbering and role-to-entry identity remain unresolved. The operator card consistency check fails for MBTs and some variants. No class filter was used to force agreement. Exact U, WMD and Ability references remain equipment configuration identities unless their capability kind is controlled. They are not defaults or proof of availability. Shared component contexts are retained once, with per-entry assignment null. An empty station WF list is not proof that its occupant cannot fire. Role, defaults, canFire, exposed and activation remain null where no same-owner semantic control exists. Unresolved imported GUID targets remain visible in the per-station component import lists. No name-only target join was used. The one-edge graph route L3110 failed its positive control. It supplies no negative findings. Available ModBuilder source remains untraced. EA text is corroboration only and its MBT/IFV counts differ from the operator cards. EclipseFPS video access was throttled; no chapter claims or numbers were imported.

Next stage: resolve one exact semantic entry owner and reproduce its role, permission and default controls before extending any player loadout claim. Resolve the exact card-to-root identity and missing imported GUIDs. The available ModBuilder dependencies remain untraced. No further unsupported graph or name-only route is recommended.

Artifacts: `seat-map.json`, `count-checks.json`, `closeout-verification.json`, `where-not-to-look.json`, `handoff.md` and `cleanup.json` in `BF6 Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100`. [Closeout receipt](../../reference-data/provenance/frosty-2026-10-01-L3112-vehicle-seat-map-closeout.json).

Local batch commits:

| Lead | Commit |
|---|---|
| L3100 | `d0d3ac1c279eda815b4216ae6a9724e57e32d718` |
| L3101 | `4678bf878e7d4a51f9d50c154111666d2036384f` |
| L3102 | `fe6b33d0015272b03249f70ce28dc7db84985b15` |
| L3103 | `a440785a70d825a58ed74f07ada2630c059a4619` |
| L3104 | `3fdfdefbdcb2f91771b78554d8112eb3d2f8906f` |
| L3105 | `bfd8587ec02671055cf4bf8dae2fe195601cdfa2` |
| L3106 | `627325c94683b40b091aab82c96bec7b88469842` |
| L3107 | `57177af7ea6e9b81d41c73c0d5069a393bc59fdd` |
| L3108 | `52d51d67f38d7b8d3b0d395619a6a8cd7d9bd56f` |
| L3109 | `0d63957bd8a03d267e819c63457ea20a2f1d5a89` |
| L3110 | `60b8bd2c6eef71760eff77203b7bfe688e29338e` |
| L3111 | `e38447edd38ed7587bd20901a35a931e2d65a31f` |

The closing commit is recorded in `L3112-commits.json` after the atomic private-index commit. Nothing is pushed. Generated indexes await the shared reviewer rebuild.

## Vehicle seat defaults current run (L3150-L3199)

State: UI route census closed. Default loadouts remain unresolved. No default finding or site change is proposed.

Run: `2026-10-01T163631-0400-vehicle-seat-defaults`. Build 1.4.3.5, Head 4909002, descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`.

Coverage: 36 exact included roots and 92 source entry definitions. All 28 current catalog vehicle UI metadata assets are covered. The total census retains 41 raw UI assets, 2092 objects, 348 text rows and 675 import pairs. A further 1785 distinct retained source entry/selection/target operands were read again with zero byte or hash mismatches.

The UH60 door-gunner minigun, RHIB OpenGunner HMG and MBT seat 0 120 mm default controls did not pass the UI-to-owner/seat route. Their exact source equipment identities pass the separate raw reader controls. The failed default route supplies no negative seat finding. All 368 weapon/ability/countermeasure/upgrade default fields remain unresolved.

Classification: weapon alternatives below are source-established configuration selections. They are not an assertion of active options, unlock state or a factory default. Localized metadata is UI-stated in the separate UI table, with no exact gameplay-seat join. A name, image, repeated integer, numbered LOADOUT 1 or first array element is not used as a default selector.

The role column repeats the operator-confirmed roles only where the documented source entry association is clear. Unmapped roles remain unresolved. AAV7A1 retains its two distinct source objects at stored index 0; the source index does not identify two equal seats. An empty WF list is not proof that an occupant cannot fire. Selected owners with SP-labelled tails remain source configuration references under the included non-SP root and do not prove multiplayer availability.

All ability, countermeasure and upgrade alternatives remain unresolved as separate capability kinds. The equipment-reference count retains the exact selected U/WMD/Ability and other targets; route names do not assign a capability kind. Full GUID/import/pointer identities are in the seat artifact.

| Artifact in the run folder | SHA-256 |
|---|---|
| `seat-defaults.json` | `bb94f8da1ce147e37e6595a850aae23b61fac7f8a79d4d747faf1acadd55bf3e` |
| `ui-metadata-rows.json` | `837e6f4ad7177364ddbb73fb6b5999d7108a2cf302ccc28b4ab2387b3fa3626e` |
| `coverage-checks.json` | `cb6944f0e36ee94f553f69e8c3ef696349c2302cf61f3fc9c9764f4c9b6e24b5` |
| `where-not-to-look.json` | `1690ca315da3d12e0dbdb9ab0387b47936fa1281f60d9143568fc8192f032b02` |

Evidence: [L3154 receipt](../../reference-data/provenance/frosty-2026-10-01-L3154-vehicle-seat-default-ui-join-coverage.json) and the run folder `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T163631-0400-vehicle-seat-defaults`. `seat-defaults.json` has one row per full root/entry object/local-key identity and keeps the original seat-map.json pointer and hash.

### MBT and IFV

| Vehicle / root | Stored index / entry object | Role (operator) | Weapon default | Configured weapon alternatives (source-established) | Ability default / alternatives | Countermeasure default / alternatives | Upgrade default / alternatives | Other configuration references |
|---|---|---|---|---|---|---|---|---|
| tank/abrams / VB_VEH_Tank_Abrams | 0 / 26 | Driver | unresolved | WF_Vehicles_MBT_PrimaryWeapon_120mm; WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG; WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 19 |
| tank/abrams / VB_VEH_Tank_Abrams | 1 / 25 | Gunner | unresolved | WF_Vehicles_RWS_HMG; WF_Vehicles_RWS_AGL; WF_Vehicles_RWS_LMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 11 |
| tank/abrams / VB_VEH_Tank_Abrams | 2 / 42 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/abrams / VB_VEH_Tank_Abrams | 3 / 43 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/bradley / VB_VEH_Tank_Bradley | 0 / 28 | Driver | unresolved | WF_Vehicles_IFV_PrimaryWeapon_APFSDST; WF_Vehicles_IFV_PrimaryWeapon_HEAB; WF_Vehicles_IFV_PrimaryWeapon_Canister; WF_Vehicles_IFV_SecondaryWeapon_LightRockets; WF_Vehicles_IFV_SecondaryWeapon_TOW; WF_Vehicles_IFV_SecondaryWeapon_HomingATGM | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 15 |
| tank/bradley / VB_VEH_Tank_Bradley | 1 / 31 | Gunner | unresolved | WF_Vehicles_RWS_HMG; WF_Vehicles_RWS_AGL; WF_Vehicles_RWS_LMG; WF_Vehicles_RWS_TargetDesignator | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 12 |
| tank/bradley / VB_VEH_Tank_Bradley | 2 / 26 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/bradley / VB_VEH_Tank_Bradley | 3 / 29 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/bradley / VB_VEH_Tank_Bradley | 4 / 27 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/bradley / VB_VEH_Tank_Bradley | 5 / 30 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/cv90 / VB_VEH_Tank_CV90 | 0 / 32 | Driver | unresolved | WF_Vehicles_IFV_PrimaryWeapon_APFSDST; WF_Vehicles_IFV_PrimaryWeapon_HEAB; WF_Vehicles_IFV_PrimaryWeapon_Canister; WF_Vehicles_IFV_SecondaryWeapon_LightRockets; WF_Vehicles_IFV_SecondaryWeapon_TOW; WF_Vehicles_IFV_SecondaryWeapon_HomingATGM | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 15 |
| tank/cv90 / VB_VEH_Tank_CV90 | 1 / 31 | Gunner | unresolved | WF_Vehicles_RWS_HMG; WF_Vehicles_RWS_AGL; WF_Vehicles_RWS_LMG; WF_Vehicles_RWS_TargetDesignator | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 12 |
| tank/cv90 / VB_VEH_Tank_CV90 | 2 / 29 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/cv90 / VB_VEH_Tank_CV90 | 3 / 27 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/cv90 / VB_VEH_Tank_CV90 | 4 / 30 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/cv90 / VB_VEH_Tank_CV90 | 5 / 28 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/leopard / VB_VEH_Tank_Leopard | 0 / 25 | Driver | unresolved | WF_Vehicles_MBT_PrimaryWeapon_120mm; WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG; WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 19 |
| tank/leopard / VB_VEH_Tank_Leopard | 1 / 26 | Gunner | unresolved | WF_Vehicles_RWS_HMG; WF_Vehicles_RWS_AGL; WF_Vehicles_RWS_LMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 11 |
| tank/leopard / VB_VEH_Tank_Leopard | 2 / 42 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/leopard / VB_VEH_Tank_Leopard | 3 / 43 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |

### Attack helicopters

| Vehicle / root | Stored index / entry object | Role (operator) | Weapon default | Configured weapon alternatives (source-established) | Ability default / alternatives | Countermeasure default / alternatives | Upgrade default / alternatives | Other configuration references |
|---|---|---|---|---|---|---|---|---|
| helicopter/ah64e / VB_VEH_Helicopter_AH64E | 0 / 21 | Pilot | unresolved | WF_Vehicles_AttackHeli_PrimaryWeapon_LightRockets; WF_Vehicles_AttackHeli_PrimaryWeapon_HeavyRockets; WF_Vehicles_AttackHeli_PrimaryWeapon_SmartRockets; WF_Vehicles_AttackHeli_SecondaryWeapon_AirToAirMissile; WF_Vehicles_AttackHeli_SecondaryWeapon_TOW | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 13 |
| helicopter/ah64e / VB_VEH_Helicopter_AH64E | 1 / 20 | Gunner | unresolved | WF_Vehicles_AttackHeli_Passenger_PrimaryWeapon_Chaingun; WF_Vehicles_AttackHeli_Passenger_SecondaryWeapon_LockingMissile | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 4 |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M | 0 / 23 | Pilot | unresolved | WF_Vehicles_ScoutHeli_PrimaryWeapon_Minigun; WF_Vehicles_ScoutHeli_PrimaryWeapon_GAU19; WF_Vehicles_ScoutHeli_PrimaryWeapon_LR30; WF_Vehicles_ScoutHeli_SecondaryWeapon_Hellfire; WF_Vehicles_ScoutHeli_SecondaryWeapon_LightRockets; WF_Vehicles_ScoutHeli_SecondaryWeapon_SmartRockets; WF_Vehicles_ScoutHeli_SecondaryWeapon_AirToAirMissile | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 18 |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M | 1 / 24 | Passenger with support tools | unresolved | WF_Vehicles_ScoutHeli_Passenger_PrimaryWeapon_ThermalScanner; WF_Vehicles_ScoutHeli_Passenger_SecondaryWeapon_DirectionalJammer; WF_Vehicles_RWS_TargetDesignator | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 6 |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M | 2 / 35 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M | 3 / 36 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| helicopter/eurocopter / VB_VEH_Helicopter_Eurocopter | 0 / 20 | Pilot | unresolved | WF_Vehicles_AttackHeli_PrimaryWeapon_LightRockets; WF_Vehicles_AttackHeli_PrimaryWeapon_HeavyRockets; WF_Vehicles_AttackHeli_PrimaryWeapon_SmartRockets; WF_Vehicles_AttackHeli_SecondaryWeapon_TOW; WF_Vehicles_AttackHeli_SecondaryWeapon_AirToAirMissile | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 12 |
| helicopter/eurocopter / VB_VEH_Helicopter_Eurocopter | 1 / 21 | Gunner | unresolved | WF_Vehicles_AttackHeli_Passenger_PrimaryWeapon_Chaingun; WF_Vehicles_AttackHeli_Passenger_SecondaryWeapon_LockingMissile | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 4 |

### Transports

| Vehicle / root | Stored index / entry object | Role (operator) | Weapon default | Configured weapon alternatives (source-established) | Ability default / alternatives | Countermeasure default / alternatives | Upgrade default / alternatives | Other configuration references |
|---|---|---|---|---|---|---|---|---|
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 0 / 17 | Pilot | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 1 / 19 | Door gunner | unresolved | WF_Vehicles_TransportHeli_Gunner_Minigun | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 4 |
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 2 / 18 | Door gunner | unresolved | WF_Vehicles_TransportHeli_Gunner_Minigun | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 4 |
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 3 / 33 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 4 / 32 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| tank/aav7a1 / VB_VEH_Tank_AAV7A1 | 0 / 14 | unresolved | unresolved | WF_Vehicles_RWS_AGL-SP; WF_Vehicles_RWS_HMG-SP | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 4 |
| tank/aav7a1 / VB_VEH_Tank_AAV7A1 | 0 / 15 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |

### Boats

| Vehicle / root | Stored index / entry object | Role (operator) | Weapon default | Configured weapon alternatives (source-established) | Ability default / alternatives | Countermeasure default / alternatives | Upgrade default / alternatives | Other configuration references |
|---|---|---|---|---|---|---|---|---|
| boat/cb90 / VB_VEH_Boat_CB90 | 0 / 26 | Driver | unresolved | WF_Vehicles_PatrolBoat_PrimaryWeapon_M230LF; WF_Vehicles_PatrolBoat_PrimaryWeapon_GAU19; WF_Vehicles_PatrolBoat_SecondaryWeapon_RBS70; WF_Vehicles_PatrolBoat_SecondaryWeapon_MistralMissile; WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG; WF_Vehicles_PatrolBoat_Equipment_Torped47; WF_Vehicles_PatrolBoat_Equipment_NavalMines | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 19 |
| boat/cb90 / VB_VEH_Boat_CB90 | 1 / 25 | Gunner | unresolved | WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_HE; WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Smoke; WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Guided; WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Airburst; WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Illumination | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 10 |
| boat/jetski / VB_VEH_Boat_JetSki | 0 / 13 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| boat/jetski / VB_VEH_Boat_JetSki | 1 / 21 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| boat/rhib / VB_VEH_Boat_RHIB | 0 / 15 | Driver | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| boat/rhib / VB_VEH_Boat_RHIB | 1 / 16 | Gunner | unresolved | WF_Vehicles_OpenGunner_HMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 5 |
| boat/rhib / VB_VEH_Boat_RHIB | 2 / 26 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| boat/rhib / VB_VEH_Boat_RHIB | 3 / 25 | Passenger | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |

### Light vehicles

| Vehicle / root | Stored index / entry object | Role (operator) | Weapon default | Configured weapon alternatives (source-established) | Ability default / alternatives | Countermeasure default / alternatives | Upgrade default / alternatives | Other configuration references |
|---|---|---|---|---|---|---|---|---|
| car/flyer60 / VB_VEH_Car_Flyer60 | 0 / 14 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/flyer60 / VB_VEH_Car_Flyer60 | 1 / 15 | unresolved | unresolved | WF_Vehicles_OpenGunner_HMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 7 |
| car/flyer60 / VB_VEH_Car_Flyer60 | 2 / 29 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/flyer60 / VB_VEH_Car_Flyer60 | 3 / 31 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/flyer60 / VB_VEH_Car_Flyer60 | 4 / 30 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/jltv / VB_VEH_Car_JLTV | 0 / 20 | Driver | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/jltv / VB_VEH_Car_JLTV | 1 / 23 | Gunner | unresolved | WF_Vehicles_RWS_HMG; WF_Vehicles_RWS_AGL; WF_Vehicles_RWS_LMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 14 |
| car/jltv / VB_VEH_Car_JLTV | 2 / 22 | Passenger gunner | unresolved | WF_Vehicles_RWS_LMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 5 |
| car/jltv / VB_VEH_Car_JLTV | 3 / 21 | Passenger gunner | unresolved | WF_Vehicles_RWS_LMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 5 |
| car/marauder / VB_VEH_Car_Marauder | 0 / 21 | Driver | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/marauder / VB_VEH_Car_Marauder | 1 / 19 | Gunner | unresolved | WF_Vehicles_RWS_HMG; WF_Vehicles_RWS_AGL; WF_Vehicles_RWS_LMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 15 |
| car/marauder / VB_VEH_Car_Marauder | 2 / 20 | Passenger gunner | unresolved | WF_Vehicles_RWS_LMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 5 |
| car/marauder / VB_VEH_Car_Marauder | 3 / 22 | Passenger gunner | unresolved | WF_Vehicles_RWS_LMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 5 |
| car/ptv / VB_VEH_Car_PTV | 0 / 14 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/ptv / VB_VEH_Car_PTV | 1 / 29 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/ptv / VB_VEH_Car_PTV | 2 / 28 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/ptv / VB_VEH_Car_PTV | 3 / 30 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/quadbike / VB_VEH_Car_QuadBike | 0 / 14 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/quadbike / VB_VEH_Car_QuadBike | 1 / 26 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/thebeast / VB_VEH_Car_TheBeast | 0 / 14 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/thebeast / VB_VEH_Car_TheBeast | 1 / 24 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/thebeast / VB_VEH_Car_TheBeast | 2 / 25 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/thebeast / VB_VEH_Car_TheBeast | 3 / 26 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/vector / VB_VEH_Car_Vector | 0 / 15 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/vector / VB_VEH_Car_Vector | 1 / 14 | unresolved | unresolved | WF_Vehicles_OpenGunner_HMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 5 |
| car/vector / VB_VEH_Car_Vector | 2 / 30 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/vector / VB_VEH_Car_Vector | 3 / 29 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| car/vector / VB_VEH_Car_Vector | 4 / 31 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| motorcycle/dirtbike01 / VB_VEH_Motorcycle_DirtBike01 | 0 / 11 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| motorcycle/dirtbike01 / VB_VEH_Motorcycle_DirtBike01 | 1 / 18 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| motorcycle/dirtbike02 / VB_VEH_Motorcycle_DirtBike02 | 0 / 11 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |
| motorcycle/dirtbike02 / VB_VEH_Motorcycle_DirtBike02 | 1 / 18 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 0 |

### Jets

| Vehicle / root | Stored index / entry object | Role (operator) | Weapon default | Configured weapon alternatives (source-established) | Ability default / alternatives | Countermeasure default / alternatives | Upgrade default / alternatives | Other configuration references |
|---|---|---|---|---|---|---|---|---|
| airplane/f14 / VB_VEH_Airplane_F14 | 0 / 19 | Pilot | unresolved | WF_Vehicles_Airplane_PrimaryWeapon_Cannon; WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 4 |
| airplane/f14 / VB_VEH_Airplane_F14 | 1 / 20 | Second seat | unresolved | WF_Vehicles_NavalFighter_PrimaryWeapon_AIM54; WF_Vehicles_Airplane_Passenger_PrimaryWeapon_SemiActiveRadarMissile | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 5 |
| airplane/f16 / VB_VEH_Airplane_F16 | 0 / 20 | Single operator seat | unresolved | WF_Vehicles_Airplane_PrimaryWeapon_Cannon; WF_Vehicles_Airplane_SecondaryWeapon_LightRockets; WF_Vehicles_Airplane_SecondaryWeapon_AirToGroundMissile; WF_Vehicles_Airplane_Bomb_Mk82AIR | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 9 |
| airplane/f22 / VB_VEH_Airplane_F22 | 0 / 19 | Single operator seat | unresolved | WF_Vehicles_Airplane_PrimaryWeapon_Cannon; WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile; WF_Vehicles_Airplane_Bomb_GBU39 | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 6 |
| airplane/fa18f / VB_VEH_Airplane_FA18F | 0 / 26 | Pilot | unresolved | WF_Vehicles_Airplane_PrimaryWeapon_Cannon; WF_Vehicles_Airplane_PrimaryWeapon_Cannon; WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile; WF_Vehicles_Airplane_SecondaryWeapon_AntiRadiationMissile; WF_Vehicles_MultirolePlane_PrimaryWeapon_ZuniRockets; WF_Vehicles_Airplane_Bomb_Rockeye | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 12 |
| airplane/fa18f / VB_VEH_Airplane_FA18F | 1 / 27 | Second seat | unresolved | WF_Vehicles_Airplane_Passenger_PrimaryWeapon_SemiActiveRadarMissile; WF_Vehicles_Airplane_Bomb_BunkerBuster; WF_Vehicles_Airplane_TVMissile | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 7 |
| airplane/jas39 / VB_VEH_Airplane_JAS39 | 0 / 20 | Single operator seat | unresolved | WF_Vehicles_Airplane_PrimaryWeapon_Cannon; WF_Vehicles_Airplane_SecondaryWeapon_AirToGroundMissile; WF_Vehicles_Airplane_SecondaryWeapon_LightRockets; WF_Vehicles_Airplane_Bomb_Mk82AIR | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 8 |
| airplane/su57 / VB_VEH_Airplane_SU57 | 0 / 19 | Single operator seat | unresolved | WF_Vehicles_Airplane_PrimaryWeapon_Cannon; WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile_R73; WF_Vehicles_Airplane_Bomb_GBU39 | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 6 |

### AA

| Vehicle / root | Stored index / entry object | Role (operator) | Weapon default | Configured weapon alternatives (source-established) | Ability default / alternatives | Countermeasure default / alternatives | Upgrade default / alternatives | Other configuration references |
|---|---|---|---|---|---|---|---|---|
| tank/gepard / VB_VEH_Tank_Gepard | 0 / 19 | Single crew seat | unresolved | WF_Vehicles_AA_PrimaryWeapon_AAGP; WF_Vehicles_AA_PrimaryWeapon_AAAP; WF_Vehicles_AA_PrimaryWeapon_AAHV; WF_Vehicles_AA_SecondaryWeapon_AntiAirMissile; WF_Vehicles_AA_SecondaryWeapon_HighVelocityMissile; WF_Vehicles_AA_SecondaryWeapon_AimGuidedMissile | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 24 |

### Stationary

| Vehicle / root | Stored index / entry object | Role (operator) | Weapon default | Configured weapon alternatives (source-established) | Ability default / alternatives | Countermeasure default / alternatives | Upgrade default / alternatives | Other configuration references |
|---|---|---|---|---|---|---|---|---|
| stationary/bgm71tow / VB_VEH_Stationary_BGM71TOW | 0 / 14 | Single operator seat | unresolved | WF_Vehicles_Stationary_TOW | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 2 |
| stationary/cws / VB_VEH_Stationary_Turret_CROWS | 0 / 14 | Single operator seat | unresolved | WF_127_CWSCROWS_HMG; WF_CWS_AGL; WF_CWSCROWS_Spike | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 6 |
| stationary/gdf009 / VB_VEH_Stationary_GDF009 | 0 / 12 | Single operator seat | unresolved | WF_Vehicles_Stationary_AntiAir | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 3 |
| stationary/m2mg / VB_VEH_Stationary_M2MG | 0 / 14 | Single operator seat | unresolved | WF_Vehicles_OpenGunner_HMG | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 4 |
| stationary/phalanx / VB_VEH_Stationary_Phalanx | 0 / 10 | Single operator seat | unresolved | WF_Vehicles_SAA_PrimaryWeapon_20mmRotaryCannon | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 2 |
| stationary/ssmbattery / VB_VEH_Stationary_SSMBattery | 0 / 13 | Single operator seat | unresolved | WF_Vehicles_SSMBattery_SecondaryWeapon_AntiAirMissile | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 1 |

### Remote/drone source context

| Vehicle / root | Stored index / entry object | Role (operator) | Weapon default | Configured weapon alternatives (source-established) | Ability default / alternatives | Countermeasure default / alternatives | Upgrade default / alternatives | Other configuration references |
|---|---|---|---|---|---|---|---|---|
| airplane/mq9 / VB_VEH_Airplane_MQ9 | 0 / 11 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 1 |
| drone/trv150 / VB_VEH_Drone_TRV150 | 0 / 14 | unresolved | unresolved | No mapped WF in retained subtree | unresolved / unresolved | unresolved / unresolved | unresolved / unresolved | 1 |

### Closeout and next route

No proposals await the operator. No recordings are proposed. The UI schema declares IsSelected, VehicleSeat, VehicleEquipmentList and SlotId, but the inspected assets do not supply the live producer values or an exact default-owner chain. A new source route must bind those properties to the exact seat/gameplay owner and pass all three default controls before assigning a default. Do not repeat the prior card/category/image/numeric scans.

MH47, Couch, _SP, SP_, _Cine and _CarChase roots are excluded per the operator scope. The two remote/drone roots are retained as source context after the requested vehicle groups.

| Lead | Local commit |
|---|---|
| L3150 | `75bce859a8b8dba827fafdd1f432e88687bc18f0` |
| L3151 | Main: `5df8517e700588b4b69160c350ecf8245b39e9f6`; parallel: `6f2fe1ff757194df03de78b95658668727800cc5` |
| L3152 | Main: `5c57581b41565244b154aa2a3503d26ed54e4ec7`; parallel: `cc89af355e6bf0dd6c1a01e9cdb2dfe8dc765625` |
| L3153 | `9333b98f1688f0b9d9594ea6ed2a5ee999dc45f5` |
| L3154 | `fb63172fabea49af2b938fc014fbea9542b03e13` |
| L3155 | Reconciliation commit is recorded in `L3155-commits.json` and `handoff.md` after the private-index update. |

No generated files were built or committed. No file over 10 MB is committed. Nothing is pushed. `cleanup.json` records the run-folder audit.

<!-- tank-weak-spots-current-start -->
## Tank directional damage current run (L3200-L3249)

Run: `2026-10-01T164935-0400-tank-weak-spots`. Source pass closed at build 1.4.3.5, Head 4909002, descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. L3200-L3208 passed their extraction, identity and typed source checks. The required effective damage mechanism is unresolved.

Five vehicle roots and 40 parts have exact identifier, material, curve and bone-child chains. All six live parts per vehicle declare material 119. Abrams selects tank curves; CV90 selects IFV curves. Leopard, Bradley and AAV7A1 have null curve pointers in the checked parts. These facts do not establish default behavior. Root Field_9040392c is 1200 on Abrams/Leopard and 1000 on the other three. Effective health and normalization are unresolved.

RPG Damage raw 135 differs from own registry default 125. APFSDS StartDamage raw 150 differs from own registry default 130. Grid Field_674633de values are retained without a proven operation. The source does not yet reproduce RPG 188/375/500 or prove a lock-on bypass. No qualified multiplier proposal is made. Known-answer hits-to-kill use the operator health premise of 1000. Unknown IFV/AAV and side values remain unresolved.

[Source tables and close audit](../frosty/VEHICLES.md#tank-directional-damage-source-pass-l3200-l3208). Full run tables, controls and compact dead ends are cited by path and SHA-256 in the close audit. The handoff and cleanup receipt stay in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots`. Next source work requires an exact receiving operation for defaults, material response, angle evaluation and effective health. No recording is proposed. No site data, simulation or UI edit, generated build, capture or push occurred.

Lead commits: `2612472`, `936d22d`, `050bb5e`, `9af7ef9`, `a4e16f4`, `42b536f`, `4453d1d`, `f883d07`, `1743a15`. The close commit is recorded in the handoff after its atomic private-index commit.
<!-- tank-weak-spots-current-end -->

## Vehicle loadout slots current run (L3250-L3299)

Run: `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T-vehicle-loadout-slots-L3250`. Build 1.4.3.5, Head 4909002; descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. Source pass closed with unresolved applicability. L3257 is the canonical table; L3253/L3255 table presentation is superseded.

Results: all 1,124 capture routes passed. All 166 slot rows are unchanged from the 1.4.3.0 CSV, including raw hashes. 47 variants have one option. 151 Eq records were checked, with 149 referenced by slots. 79 options have exact seat-map owners; 72 remain unresolved. The five Eq controls passed. RHIB fixed configuration passed; its EqSlot remains unresolved. MBT 120 mm is a fixed component. Five MBT ammo options have exact producer-token/direct-WMD-condition chains on both MBTs.

Labels: `source-established` describes serialized identity and configuration. `first-preset` describes conditional Loadout 1 selection; default activation is unconfirmed. `unresolved` describes recipe applicability, active defaults or missing option consumers. Every root-to-recipe applicability flag is false. A source-associated slot is not an assigned game recipe.

Table evidence: `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T-vehicle-loadout-slots-L3250\vehicle-slot-table.json`, SHA-256 `7491470cbacff5d2ccb83c52b144fe5218d09d659b4fe05520bd152b879eadcc`. This file holds all ordered options, all three conditional preset selections, single-option flags and exact GUID/pointer/raw chains. `vehicle-slot-table.md` and `.csv` give readable rows.

### Seat rows

The 90 vehicle station definitions below retain exact root, serialized seat index and entry object. They are source candidates; this run does not certify native playable-seat availability. Duplicate seat indices keep separate entry identities. No operator-confirmed role is changed.

| Vehicle root label | Seat / entry | Slot result | Preset result | Exact source chain |
|---|---|---|---|---|
| VB_VEH_Tank_Abrams | 0 / 26 | source-established: 9 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[0] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Abrams | 1 / 25 | source-established: 3 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[1] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Abrams | 2 / 42 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[2] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Abrams | 3 / 43 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[3] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Leopard | 0 / 25 | source-established: 9 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[4] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Leopard | 1 / 26 | source-established: 3 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[5] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Leopard | 2 / 42 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[6] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Leopard | 3 / 43 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[7] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Bradley | 0 / 28 | source-established: 6 all-option variants; unresolved: 1 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[8] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Bradley | 1 / 31 | source-established: 4 all-option variants; unresolved: 3 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[9] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Bradley | 2 / 26 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[10] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Bradley | 3 / 29 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[11] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Bradley | 4 / 27 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[12] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Bradley | 5 / 30 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[13] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_CV90 | 0 / 32 | source-established: 6 all-option variants; unresolved: 1 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[14] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_CV90 | 1 / 31 | source-established: 4 all-option variants; unresolved: 3 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[15] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_CV90 | 2 / 29 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[16] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_CV90 | 3 / 27 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[17] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_CV90 | 4 / 30 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[18] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_CV90 | 5 / 28 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[19] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_AH64E | 0 / 21 | source-established: 6 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[20] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_AH64E | 1 / 20 | source-established: 2 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[21] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_Eurocopter | 0 / 20 | source-established: 6 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[22] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_Eurocopter | 1 / 21 | source-established: 2 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[23] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_AH6M | 0 / 23 | source-established: 6 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[24] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_AH6M | 1 / 24 | source-established: 2 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[25] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_AH6M | 2 / 35 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[26] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_AH6M | 3 / 36 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[27] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_UH60 | 0 / 17 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[28] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_UH60 | 1 / 19 | source-established: 1 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[29] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_UH60 | 2 / 18 | source-established: 1 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[30] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_UH60 | 3 / 33 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[31] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Helicopter_UH60 | 4 / 32 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[32] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_AAV7A1 | 0 / 14 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[33] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_AAV7A1 | 0 / 15 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[34] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Tank_Gepard | 0 / 19 | source-established: 7 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[35] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Boat_CB90 | 0 / 26 | source-established: 9 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[36] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Boat_CB90 | 1 / 25 | source-established: 6 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[37] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Boat_RHIB | 0 / 15 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[38] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Boat_RHIB | 1 / 16 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[39] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Boat_RHIB | 2 / 26 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[40] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Boat_RHIB | 3 / 25 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[41] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Boat_JetSki | 0 / 13 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[42] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Boat_JetSki | 1 / 21 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[43] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Flyer60 | 0 / 14 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[44] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Flyer60 | 1 / 15 | source-established: 1 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[45] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Flyer60 | 2 / 29 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[46] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Flyer60 | 3 / 31 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[47] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Flyer60 | 4 / 30 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[48] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_JLTV | 0 / 20 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[49] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_JLTV | 1 / 23 | source-established: 3 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[50] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_JLTV | 2 / 22 | source-established: 1 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[51] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_JLTV | 3 / 21 | source-established: 1 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[52] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Marauder | 0 / 21 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[53] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Marauder | 1 / 19 | source-established: 3 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[54] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Marauder | 2 / 20 | source-established: 1 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[55] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Marauder | 3 / 22 | source-established: 1 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[56] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_PTV | 0 / 14 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[57] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_PTV | 1 / 29 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[58] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_PTV | 2 / 28 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[59] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_PTV | 3 / 30 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[60] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_QuadBike | 0 / 14 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[61] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_QuadBike | 1 / 26 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[62] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_TheBeast | 0 / 14 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[63] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_TheBeast | 1 / 24 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[64] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_TheBeast | 2 / 25 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[65] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_TheBeast | 3 / 26 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[66] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Vector | 0 / 15 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[67] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Vector | 1 / 14 | source-established: 1 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[68] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Vector | 2 / 30 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[69] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Vector | 3 / 29 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[70] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Car_Vector | 4 / 31 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[71] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Motorcycle_DirtBike01 | 0 / 11 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[72] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Motorcycle_DirtBike01 | 1 / 18 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[73] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Motorcycle_DirtBike02 | 0 / 11 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[74] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Motorcycle_DirtBike02 | 1 / 18 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[75] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Airplane_F14 | 0 / 19 | source-established: 2 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[76] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Airplane_F14 | 1 / 20 | source-established: 2 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[77] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Airplane_F16 | 0 / 20 | source-established: 2 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[78] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Airplane_F22 | 0 / 19 | source-established: 1 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[79] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Airplane_FA18F | 0 / 26 | source-established: 9 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[80] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Airplane_FA18F | 1 / 27 | source-established: 6 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[81] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Airplane_JAS39 | 0 / 20 | source-established: 2 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[82] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Airplane_SU57 | 0 / 19 | source-established: 1 all-option variants; unresolved: 0 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[83] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Stationary_BGM71TOW | 0 / 14 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[84] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Stationary_Turret_CROWS | 0 / 14 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[85] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Stationary_GDF009 | 0 / 12 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[86] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Stationary_M2MG | 0 / 14 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[87] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Stationary_Phalanx | 0 / 10 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[88] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Stationary_SSMBattery | 0 / 13 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[89] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |

### Remote and drone context rows

These two definitions are context-only and are excluded from the 90 vehicle station count.

| Vehicle root label | Seat / entry | Slot result | Preset result | Exact source chain |
|---|---|---|---|---|
| VB_VEH_Airplane_MQ9 | 0 / 11 | unresolved slots; source-established entry/configuration | unresolved Loadout 1/2/3 and activation | JSON stations[90] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |
| VB_VEH_Drone_TRV150 | 0 / 14 | source-established: 0 all-option variants; unresolved: 1 partial candidates | first-preset: conditional only; Loadout 2/3 conditional; applicability and activation unresolved | JSON stations[91] entryChain, weapons; sourceAssociatedVariants/candidateVariants -> slots/options exact owners |

### Limits and next stages

Proposals awaiting the operator: none. Root/context-to-recipe selection and active default ownership are unresolved. The 47 inspected contexts pass name exclusions; this is not a playable-vehicle count. Nine partial associations remain distinct; six recipe-selected references are not projected to their candidate stations. 72 remaining Eq producer branches have no qualifying consumer in the controlled direct component schema. This is not proof that the effects are absent.

Reopen only with an exact root/context selector that imports the numbered recipe, an explicit activation owner, or a typed option consumer outside the checked schema. Do not repeat the failed UI-metadata route or name/marker/shared-Feature joins. No site data, simulator, UI or recording changes were made. No push.

### Local lead commits

- L3250: `4cd22819519cb48877647475c874f6f5ecdefa65`.
- L3251: `cad33286d2a394e0a9751da57315fab3f175403e`.
- L3252: `915579dec74f6abab01361d63b238d82e792f229`.
- L3253: `4f35a90e329cce3dff4b6eafee413d55881d4656`.
- L3254: `37eb90426a0270af81bbab3e752f42704c81ed5d`.
- L3255: `729e6f3af7c424777cf9905330dd6168902bcdf9`.
- L3256: `c0a00ddc0baf56e88f29b780b6ae372bbdf32253`.
- L3257: `2fec66f16bd38118be8f55991f2615d8e11208cf`. Source pass closed; handoff.md and cleanup.json are in the run folder.
