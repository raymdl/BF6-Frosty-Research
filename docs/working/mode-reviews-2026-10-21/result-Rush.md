# Battlefield 6 Rush: decoded data analysis (build 2.1.1.0)

Sources: `Rush-maps.txt`, `Rush-tweakables.txt`, `maps-tweakables.txt`, `ui-text.txt`, `objective-table.json`, `map-names.json` in this folder; counts and geometry computed by script (`parse_rush.py`, `final.py`, `build.py` in the parent folder).

Scope of the data, up front:
- `Rush-maps.txt` (second capture, layers also found directly under `_Layers_Gameplay`) lists 18 maps and all 18 carry Rush gameplay instances in layer `Rush0`: Siege of Cairo, Empire State, Wake Island, Blackwell Fields, Iberian Offensive, Liberation Peak, Contaminated, Area 51, Manhattan Bridge, Eastwood, Operation Firestorm, Railway to Golmud, Tsuru Reef, New Sobek City, Vegas Strip, Cairo Bazaar, Hagental Base, Mirak Valley.
- Saints Quarter (MP_LIMESTONE) is not in the file and has no Rush layer.
- The per-sector ticket count is NOT a tweakable (details in 1.1).
- The UI text confirms rules only qualitatively; it states no number (details in 1.9).

## 1. Mode rules

### 1.0 Where the rules live

| Object | Content |
|---|---|
| `Rush/Mode/MUT_Rush` | 110 tweakables (all listed below) |
| `Rush/Mode/GM_Rush_LaunchFunction` | 4 objects; only `ActivityParameters` and `LaunchParameters`, both null |
| `Rush/Round/GME_Pres_Rush_Round` | presentation graph (36 objects); one named variable `MI_Pres_GameMode`, null |
| `Rush/Round/GME_Sim_Rush_Round` | simulation round graph (76 objects); only `ActivityStateMachine` and `MI_Sim_GameMode` are named, both null. All round constants (ticket grants per sector, the order of sectors, win conditions) are unnamed constants inside the graph and are not exposed |
| `_Shared/GEMS/MCOM/...`, `Plant/...`, `Reinforcement/...` | shared M-COM and reinforcement logic (1.7) |
| `objective-table.json` | `AD_Objective_Rush` (and a Halloween-style `AD_Objective_SpookyRush` with Marker_Altar, Marker and Collection_Event) |

Values below are client defaults as `value [min..max]`; a server playlist can override them. A range of `[0..0]` appears on many entries and means the editor stored no usable range (it does not mean the value must be 0).

### 1.1 Lives and reinforcements

| Tweakable | Value [range] | Reading |
|---|---|---|
| `R_iInitialTickets` | 75 [0..0] | attackers' starting lives (reinforcements); the only lives number in the mode. It equals the top of the threshold ranges below. Not UI-confirmed |
| `R_iRemainingRespawnsThreshold1` | 50 [0..75] | remaining-lives threshold 1 (announcement or UI step) |
| `R_iRemainingRespawnsThreshold3` | 25 [0..75] | threshold 3; there is no Threshold2 in the file |
| `R_iUrgencyRemainingRespawnsThreshold` | 10 [0..0] | urgency state when this few lives remain |
| `R_SoldierDeathScoreBleed` | 1 [0..10] | lives lost per soldier death (by name; unit not stated) |
| `R_ReinforcementsAnnouncementDelay` | 5.0 [0.1..30.0] | delay before the reinforcement announcement |
| `R_fSectorReinforcementsDuration` | 5.0 [0.0..1000.0] | duration of the reinforcement step after a sector is taken. This is a time, not a ticket amount |

Per-sector ticket count: not a tweakable. `SimEx_SetSectorReinforcement` exposes only two references (`MI_Reinforcements`, `MI_Sim_HQ`) and no number; `SimEx_Reinforcement` exposes `BattlePickups`, `VehicleSpawners`, `BattalionCount` and `MI_Sim_VehicleSpawner_ExternalSettings`. The amount awarded per sector is therefore either an unnamed constant in `GME_Sim_Rush_Round` or comes from the Reinforcement prefab (`GMPF_Reinforcement`, `GMPF_Reinforcement_Intro` in the objective table). The UI says "Earn reinforcements after taking each sector" but gives no amount.

### 1.2 Arm and defuse times

| Tweakable | Value [range] |
|---|---|
| `R_ArmTime` | 2.0 s [0..60] |
| `R_FastArmTime` | 1.6 s [0..60] |
| `R_DefuseTime` | 5.0 s [0..60] |
| `R_FastDefuseTime` | 4.0 s [0..60] |
| `R_DisableFastInteract` | false |

Seconds are by name and range; the data states no unit. Fast variants are the shorter times used by `SimEx_MCOMInteract` (it has `FastInteractTime`, `PlayerStartFastInteract`, `PlayerStopFastInteract`); what qualifies an interaction as fast is not in these files.

### 1.3 Fuse time

| Tweakable | Value [range] |
|---|---|
| `R_FuseTime` | 30.0 [0..180] |
| `R_iUrgencyRemainingFuseThreshold` | 45.0 [0..0] |

The urgency threshold (45) is larger than the fuse (30), so on defaults the urgency state would apply for the entire fuse. Not UI-confirmed.

### 1.4 Sector timings and orders

| Tweakable | Value [range] |
|---|---|
| `R_iSectorTime` | 15 [10..180] (unit not stated) |
| `R_fSectorAdvanceDuration` | 40.0 [0..0] |
| `R_fSectorCleanUpDurationMin` / `Max` | 15.0 / 45.0 [0..1000] |
| `R_fSectorCleanUpEndedEarlyThreshold` | 10.0 [5..15] |
| `R_fSectorTakenDuration` | 6.0 [0..1000] |
| `R_fSectorReinforcementsDuration` | 5.0 [0..1000] |
| `R_fUrgencyRemainingSectorTimeThreshold` | 60.0 [0..120] |
| `R_fSectorRating_Minor` / `Major` | 0.66 / 0.33 [0..1] |
| `R_AttackerAdvanceInitialReminderDelay` / `R_AttackerAdvanceReminderIncrementDelay` | 30.0 / 15.0 [0..0] |
| `R_fTimeToMarkDefenders` | 5.0 [0..0] |
| `R_fAttackOrderReactivationDelay` | 20.0 [0..360] |
| `R_fSquadOrderCooldown` | 30.0 [0..0] |
| `R_fTacticalAdviceCooldown` | 60.0 [0..0] |
| `R_fNoInteractivityTimeoutOverride` | 120.0 [0..600] |
| `R_bAllowAttackTAOrders` / `DefuseTAOrders` / `GuardTAOrders` / `DefendTAOrders` | true / true / true / false |
| `Rush_iLobbyPlayerCountStartTimer` / `ToSpeedUpTimer` | 16 [0..128] / 24 [0..0] |
| `R_Win_FirstSpanMinutes` / `SecondSpanMinutes` | 25.0 / 15.0 [0..60] |
| `R_MaxCaptureMultiplier` | 5 [1..128] |
| `R_ObjectiveDealDamageToPlayers` | false |
| `R_iSoldierMandownType` | 1 [0..2] |
| `R_bStickyHQIcons`, `R_ShowObjectiveCallOutString`, `R_bShowPlayerNamesAfterInteraction`, `R_CheckAllSquadMates` | false, true, true, false |
| `R_ObjectiveCallOutStringVisDistance` | 100.0 [0..0] |
| `R_AwardSuccessfulRetreat`, `R_RetreatersSpotting_NoOcclusion`, `_InWorld`, `_InMinimap` | all true |
| `R_iCommanderVoice` | 0 [0..0] |
| `Assault / Recon / Engineer / Support Recommended` | all false |

The meaning of "sector advance", "clean-up" (a post-capture window in which the losing side clears out, by its name) and "sector rating minor/major" is by name only; the graph logic that uses them is unnamed.

### 1.5 Respawn

| Tweakable | Value [range] |
|---|---|
| `R_GlobalRespawnDelay` | 10.0 [0..0] |
| `R_TeamSpecificRespawnDelay` | true |
| `R_T1_RespawnDelays` | one array (field `Field_ffba60f0`) of 15 values, all 12.0 |
| `R_T2_RespawnDelays` | one array of 15 values, all 12.0 |

With `R_TeamSpecificRespawnDelay` true, the team arrays (12 s, probably indexed by an unnamed count) most likely apply and the 10 s global is the fallback; the data does not show which index is read.

### 1.6 Vehicle cooldown fallbacks and out of bounds

- Vehicle cooldown fallbacks: none. No Rush tweakable (or shared M-COM, Plant or Reinforcement variable) holds a vehicle respawn, cooldown or fallback timer. `SimEx_Reinforcement.MI_Sim_VehicleSpawner_ExternalSettings` and `SimEx_SetVehicleTeam` (`VehicleQueryResult`, `TeamId`) only reference the pads' own settings and assign the owning team. Vehicle timers must therefore live in the vehicle spawner prefabs (`GMPF_VehicleSpawner_*`), not in the mode.
- Out of bounds: `R_iOutOfBounds_TimeToReturn` = 5 [0..0] (infantry; unit not stated). Per-map: `MP_Dumbo_VehicleOOBtime` = 10 [1..15] (Manhattan Bridge). The other per-map tweakables are Conquest `*_CQ_iInitialScore` = 1200 (Abbasid, Aftermath, Badlands, Battery, Capstone, Dumbo, Eastwood, Firestorm, Outskirts, Tungsten), `SpawnPreventionRadius_Small` = 40.0 (Abbasid, Siege of Cairo), `SpawnPreventionRadius_LargeModes_Battery` = 45.0 (Iberian Offensive) and Golmud train flags (`Golmud_Escalation_EnableMovingTrain`, `Golmud_MovingTrain_StreamIn`, `Golmud_Conquest_EnableMovingTrain`, all true). No per-map Rush tweakable exists; Saints Quarter has an empty `MUT_Limestone`; Eastwood has only the Conquest score.

### 1.7 XP and score values (all `MUT_Rush`)

Objective: `R_ObjectiveCapturedXP` 200 [0..500], `R_ObjectiveNeutralizedXP` 200 [0..500], `R_SectorCapturedXP` 100 [0..100], `R_ObjectiveSecuringXP` 15, `R_ObjectiveHoldingXP` 15, `R_ControlPanelClaimed` 10.
Combat: `R_PlayerKilledXP` 50, `R_Headshot` 20, `R_TakedownKill` 25 [0..100], `R_MultiKillXP` 50 [0..0], `R_AvengerOrSaviorKill` 10, `R_PilotKill` 50 [0..250], `R_EnemySpottedXP` 5, `R_PlayerAssistedSpotXP` 10, `R_PlayerAssistedDamageXP` 50, `R_PlayerAssistedSmokeXP` 40, `R_PlayerAssistedDisruptionXP` 40, `R_EnemyDisruptedXP` 20.
Support: `R_HealingXP` 20, `R_PlayerRevivedXP` 50, `R_PlayerWasRevivedXP` 15, `R_ReviveOrHealConcealed` 10, `R_ResupplyXP` 20, `R_VehicleRepairingXP` 20, `R_PlayerAssistedRepairXP` 50, `R_SpawnOnYouXP` 10, `R_SpawnOnBeaconXP` 10, `R_SpawnOnVehicleXP` 10, `R_RetreatSuccessfulXP` 50.
Vehicles and gadgets: `R_VehicleDestroyedXP` 50, `R_VehicleDisabledXP` 10, `R_VehicleDamagedLightXP` 5 [0..0], `R_VehicleDamagedHeavyXP` 20 [0..0], `R_PlayerAssistedVehicleDestroyXP` 50, `R_PlayerAssistedDriverXP` 50, `R_PlayerAssistedPassengerXP` 40, `R_PlayerAssistedTurretXP` 50, `R_EnemyForcedBailXP` 50, `R_EnemyForcedCrashXP` 50, `R_RangerDestroyedXP` 75, `R_TVMissileDestroyedXP` 10, `R_EIDOSDestroyXP` 10, `R_ExplosiveDestroyedXP` 10, `R_EquipmentDestroyedXP` 10.
Time, bonuses: `R_TimeXPpM` 250 [0..500], `R_Win_FirstSpanXPpM` 130, `R_Win_SecondSpanXPpM` 100, `R_Win_ThirdSpanXPpM` 80 (all [0..500]; per minute by name), `R_PlayingWithFriendsXP` 1000 [0..5000], `R_SportsmanshipMultiplier` 1.0 [0..10].
All the unmarked ranges above are [0..100]. No XP value is stated by the UI text.

### 1.8 Shared M-COM and reinforcement logic (variables only; defaults mostly null)

- `SimEx_MCOMInteract` (18 objects): `Enabled`, `PlayerStartInteract` / `PlayerStopInteract`, `PlayerStartFastInteract` / `PlayerStopFastInteract`, `InteractTime`, `FastInteractTime`, `PlayerInteraction`, `Interactions` [], `PlayersInteracting` [], `InteractingPlayers`, `IsPlayerLeadingInteract`, `ClosestToCompletion` (progress goes to the interactor closest to completion), `InteractingEODQuery`, `RemovedEODQuery`, `AlwaysExecute`. Interaction is multi-player and supports EOD bots (gadget).
- `SimEx_MCOM_EODBotInteract` (21 objects): `ArmTime`, `DisarmTime`, `isArming`, `IsDefusing`, `IsArmed`, `Position`, `EODBots`, `OldEODBots`, `InteractingEODs` [], `InteractingEODQuery`, `RemovedEODQuery`, `LeadingEODPlayer`, `LeadingEODID`, `LeadingPlayerContext`, `OldLeadingEODContext`, `UpdatedPlayerContext`. So EOD bots arm and defuse with the same times and a leading owner.
- `SimEx_Mcom` (6 objects, spatial): `AttackingTeam`, `SoldiersOnPoint`, `isAttackerTeamOnPoint`, `IsSomePlayerOnPoint` (presence test for the M-COM area).
- `SimEx_CheckMCOMStatus` (5 objects): `NumDestroyedObjectives`, `OwningTeamInt` = 1, `MI_Sim_Objective`. The default owning team is 1; read literally that makes team 1 the M-COM owner (defender), which contradicts "attackers = team 1". It is a graph default and not proof; see open questions.
- `SimEx_SetSectorReinforcement` (5 objects): `MI_Reinforcements`, `MI_Sim_HQ`: links a sector's reinforcement set to the HQ (spawn base) it enables.
- Not asked but relevant: `SimEx_Reinforcement` (`BattlePickups`, `VehicleSpawners`, `BattalionCount`), `SimEx_SectorSpotting` (`SpottingSharingRules`, `SectorSpottingSettings`), `SimEx_CaptureVolume`, `SimEx_DestructibleZone` (shared, mostly unused by Rush).
- Objective definition (`AD_Objective_Rush`): Sector, Objective_MCOM, HQ, AutomaticAA, Insertion (19 arrival variants), Insertion_Event (Airstrike, JetStraight), VehicleSpawner (24 keys: 0 Light Transport, 1 IFV, 2 Tank, 3 Mobile AA, 4 Attack Plane, 5 Fighter Plane, 6 Attack Helicopter, 7 Transport Helicopter, 8 Quad Bike, 9 APC, 10 Golf Cart, 11 RHIB, 12 Scout Helicopter, 13 Dirt Bike, 14 Patrol Boat, 15 Multirole Plane, 16 Naval Fighter Plane, 17-23 carrier jet launches), VehicleSpawner_Forward, StationarySpawner (0 HMG, 1 Anti-Tank, 2 Anti-Aircraft), VehicleResupplyStation, Reinforcement, Reinforcement_Intro, B1 Bomber trailer and intro cinematic vehicle, Battle_Pickup (0 Minigun, 1 Railgun, 2 Smoke Screen, 3 Artillery Strike, 4 DS Pulse).

### 1.9 What the UI text confirms

`ui-text.txt` (title "Rush"; a "HARDCORE RUSH" variant label also exists) states, as the game words it:
- Attackers: "Attack through multiple enemy sectors by destroying their M-COMs"; "We have limited lives"; "Enemy has unlimited lives"; "Destroy all M-COMs to win"; "Interact with an M-COM to arm explosives"; "Destroy M-COMs in all sectors before running out of lives"; "Retain lives by reviving your teammates"; "Earn reinforcements after taking each sector"; "Destroy the final M-COM to win the battle".
- Defenders: "Defend multiple sectors by stopping the enemy from destroying your M-COMs"; "We have unlimited lives"; "Enemy has limited lives – wear them down"; "Prevent enemies from arming explosives on M-COMs"; "Interact with an M-COM to defuse explosives"; "Win by fully depleting the attacker's lives before they destroy all M-COMs".
Confirmed qualitatively: limited vs unlimited lives, arm/defuse by interaction, reinforcements after each sector, revives refunding lives, win conditions. Not confirmed by any number: initial 75, thresholds, arm/defuse/fuse times, sector times, respawn delays, XP. The UI text never states a per-sector amount.

## 2. Per-map layers

Coordinates are (x, z) in metres. "S1" is the sector at the end of the chain that carries the insertion (arrival) animations; I treat that end as the attackers' start. Team 1 is assumed to attack unless a faction override is stated. Pad grouping uses the nearest real HQ, and each HQ is placed in the nearest sector region; "start base" and "final base" are HQs farther than 40 m from the end sector centre and beyond the chain end. Vehicle names are the pad classes the game uses (the concrete vehicle model per faction is not in this data).

### Siege of Cairo (MP_ABBASID)

- Assets: Rush, Rush0, Rush_Global, Rush_Global_EcsPrefab_ecsPrefab, Rush_Schematic, Rush_Team1, Rush_Team2, Rush0_Schematic, rush/MeshVariationDb_Win32, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {}; GEM counts: {"GEM_DeployCam": 1, "GEM_Sector": 4, "GEM_Objective_MCOM": 8, "GEM_Insertion": 6, "GEM_Battle_Pickup": 2, "GEM_HQ": 10, "GEM_VehicleSpawner": 3, "GEM_StationarySpawner": 2, "GEM_TelemetryArea": 4}
- Layout variants: all 40 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S4, S1 = attackers' side): S1 (91, -56) -> S2 (17, -88) -> S3 (-80, -51) -> S4 (-174, -18)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (112, -94); 43 m from S1 vs 296 m from S4). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @84 (122, -52) dist 31 m in B[93] P[23] | @11 (87, -38) y65; @15 (94, -74) y62 | B93[Rush0 71..183 x, -148..5 z]; P23[Rush0 47..132 x, -103..-6 z] | @31 (156, -82) start base (beyond S1) 70m; @85 (99, -53) sector 9m |
| S2 | @62 (18, -67) dist 21 m in B[48] P[92] | @30 (10, -107) y63; @72 (23, -69) y60 | B48[Rush0 -29..71 x, -141..13 z]; P92[Rush0 -30..70 x, -128..-9 z] | @26 (24, -77) sector 13m; @43 (24, -74) sector 15m |
| S3 | @8 (-82, -49) dist 2 m in B[101] P[7] | @64 (-78, -27) y64; @81 (-82, -74) y64 | B101[Rush0 -110..-29 x, -127..27 z]; P7[Rush0 -116..-3 x, -110..6 z] | @29 (-68, -57) sector 13m; @53 (-63, -55) sector 17m |
| S4 | @33 (-170, -24) dist 6 m in B[5] P[24] | @47 (-169, -3) y64; @69 (-178, -33) y65 | B5[Rush0 -251..-110 x, -105..49 z]; P24[Rush0 -203..-102 x, -83..40 z] | @94 (-152, -20) sector 21m; @99 (-220, 15) final base (beyond S4) 57m |

- Attackers' starting base (inferred): HQ @31 (156, -82)
- Defenders' final base (inferred): HQ @99 (-220, 15)
- Co-located HQ pairs (<12 m apart): @26+@43 (24, -77) (3 m); @29+@53 (-68, -57) (5 m)
- HQ instances at stray or shared default positions, ignored: @32 (39, 40), @83 (39, 40)
- Vehicle pads (3) by nearest HQ:
  - HQ @31 (156, -82) (start base (beyond S1)): 1 IFV
  - HQ @85 (99, -53) (in S1): 1 IFV
  - HQ @26 (24, -77) (in S2): 1 IFV
  - total: 3 IFV
- Emplacements (2): @49 Anti-Tank (-95, -68) (nearest S3); @66 Anti-Tank (-20, -94) (nearest S2)
- Deploy cams (1): @1 (-65, 272) (nearest S4)
- Battle pickups (placed, not active in live game per README) (2): @25 Minigun (166, -88) (nearest S1); @56 Minigun (78, -65) (nearest S1)
- Insertions (6) by nearest sector: S1:4, S2:2
- TelemetryArea: 4 (S1:1, S2:1, S3:1, S4:1)
- Unusual: Only map with `Rush_Team1` and `Rush_Team2` assets (team-specific sets); their contents are not in the instance dump.
- Unusual: DeployCam @1 sits at (-65, 272) with y=740, far from the play area (x -251..183, z -148..49); Outskirts has the same x/z.
- Unusual: Two HQ instances (@32, @83) sit on the shared default (39, 40) and were ignored.
- Unusual: Only 3 pads, all IFV, all in the S1/S2 half; the S3/S4 half has none. Emplacements are 2 Anti-Tank only.
- Unusual: Every sector has two HQs; S2 and S3 each hold a co-located pair (3 m and 5 m apart).


### Empire State (MP_AFTERMATH)

- Assets: Rush, Rush0, Rush_Global, Rush_Global_Schematic, Rush_VFX, Rush_VFX_Schematic, MeshVariationDb_Win32, staticmodelgroup.physics
- Faction overrides: {"team2": "Alliance/NATO", "team1": "Coalition/Pax Armata"}; GEM counts: {"GEM_SpecialCombatArea": 1, "GEM_Insertion": 6, "GEM_Sector": 4, "GEM_HQ": 8, "GEM_Battle_Pickup": 1, "GEM_TelemetryArea": 3, "GEM_Objective_MCOM": 6, "GEM_DeployCam": 1}
- Layout variants: all 30 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S3, S1 = attackers' side): S1 (-643, 29) -> S2 (-638, -28) -> S3 (-593, -129)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-614, 44); 33 m from S1 vs 174 m from S3). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @81 (-615, 27) dist 28 m in B[] P[31, 67, 72, 76, 82] | @45 (-630, 24) y59; @51 (-656, 34) y55 | P22[Rush0 -708..-591 x, -90..60 z]; P48[Rush0 -708..-591 x, -52..60 z]; P76[Rush0 -708..-594 x, -4..92 z]; P82[Rush0 -708..-594 x, -4..92 z] | @52 (-609, 99) start base (beyond S1) 77m; @65 (-628, 66) sector 40m |
| S2 | @47 (-659, -17) dist 23 m in B[] P[22, 48, 62] | @39 (-621, -47) y59; @44 (-656, -10) y63 | P22[Rush0 -708..-591 x, -90..60 z]; P48[Rush0 -708..-591 x, -52..60 z]; P62[Rush0 -708..-591 x, -52..0 z] | @20 (-643, -17) sector 13m; @34 (-635, -29) sector 3m |
| S3 | @32 (-623, -108) dist 36 m in B[] P[16, 73] | @25 (-575, -115) y53; @83 (-612, -142) y54 | P16[Rush0 -702..-549 x, -169..-44 z] | @12 (-568, -168) final base (beyond S3) 46m; @42 (-688, -153) final base (beyond S3) 98m; @70 (-636, -106) sector 49m; @84 (-688, -153) final base (beyond S3) 98m |

- Attackers' starting base (inferred): HQ @52 (-609, 99)
- Defenders' final base (inferred): HQ @12 (-568, -168), @42 (-688, -153), @84 (-688, -153)
- Co-located HQ pairs (<12 m apart): @42+@84 (-688, -153) (0 m)
- Vehicle pads: none in this layer
- Deploy cams (1): @29 (-600, -50) (nearest S2)
- Battle pickups (placed, not active in live game per README) (1): @13 Minigun (-594, 113) (nearest S1)
- Special combat areas (1): @3 (-573, -46) (nearest S2)
- Insertions (6) by nearest sector: S1:6
- TelemetryArea: 3 (S1:1, S2:1, S3:1)
- Unusual: Layer assets live directly under _Layers_Gameplay (Rush, Rush0, Rush_Global, Rush_VFX); only Rush0 holds instances.
- Unusual: Four Sector markers but only three M-COM pairs (6 M-COMs, 2 per sector). Marker @6 (-605, 204) lies at the start end, 100+ m beyond the S1 pair, with no M-COM, with HQ @52 and Battle_Pickup Minigun @13 around it; the 6 insertions form two groups of 3: one near HQ @52 and marker @6 (z 76 to 101), one on the S1 M-COMs (z 0 to 4); I count it as the attackers' start zone, not a sector with M-COMs.
- Unusual: Faction override: team 1 = Pax Armata, team 2 = NATO.
- Unusual: HQ @42 and @84 are both at (-688, -153) with no container; no vehicle pads or emplacements.
- Unusual: DeployCam @29 at y=1388 (overview camera); SpecialCombatArea @3 at (-573, -46).


### Wake Island (MP_ATOLL)

- Assets: Rush, Rush_Global, Rush_Global_Schematic, generated/AG_Rush_DynamicDD_Schematic_A9B60BEC, generated/AG_Rush_DynamicDD_boxes_1857AB1E, Rush0, Rush0_Schematic, rush/MeshVariationDb_Win32, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {}; GEM counts: {"GEM_Sector": 5, "GEM_TelemetryArea": 10, "GEM_VehicleSpawner": 58, "GEM_Insertion": 16, "GEM_HQ": 10, "GEM_Objective_MCOM": 10, "GEM_StationarySpawner": 7}
- Layout variants: all 116 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S5, S1 = attackers' side): S1 (225, 373) -> S2 (424, 373) -> S3 (470, 151) -> S4 (376, -89) -> S5 (126, -136)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (181, 306); 81 m from S1 vs 445 m from S5). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @135 (200, 355) dist 30 m in B[] P[26, 57, 65, 124, 163] | @89 (216, 415) y99; @183 (233, 331) y99 | P26[Rush0 -426..895 x, 125..970 z]; P57[Rush0 -122..330 x, 113..1055 z]; P65[Rush0 -208..273 x, 231..997 z]; P124[Rush0 -122..280 x, 113..997 z] (+1 more) | @8 (284, 392) sector 62m; @45 (67, 320) start base (beyond S1) 167m; @132 (-108, 232) start base (beyond S1) 361m |
| S2 | @149 (464, 391) dist 43 m in B[56] P[26, 74, 85, 163] | @12 (433, 338) y106; @178 (415, 408) y103 | B56[Rush0 220..536 x, 259..1037 z]; P26[Rush0 -426..895 x, 125..970 z]; P74[Rush0 258..878 x, 146..1063 z]; P85[Rush0 220..517 x, 259..1037 z] (+1 more) | @48 (495, 370) sector 71m |
| S3 | @72 (485, 135) dist 21 m in B[] P[32, 94, 122, 126, 167] | @17 (488, 197) y106; @117 (452, 105) y104 | P32[Rush0 159..895 x, 20..273 z]; P94[Rush0 159..895 x, 20..273 z]; P122[Rush0 273..981 x, -93..1037 z]; P126[Rush0 205..739 x, -586..209 z] (+1 more) | @110 (459, 206) sector 56m; @139 (468, 34) sector 117m |
| S4 | @168 (364, -83) dist 13 m in B[] P[44, 62, 126, 143] | @98 (364, -45) y100; @157 (388, -133) y100 | P44[Rush0 298..894 x, -581..66 z]; P62[Rush0 170..894 x, -404..52 z]; P126[Rush0 205..739 x, -586..209 z]; P143[Rush0 205..894 x, -586..202 z] | @136 (392, -114) sector 29m; @144 (398, -72) sector 28m |
| S5 | @1 (130, -84) dist 51 m in B[176] P[31] | @9 (135, -149) y102; @43 (116, -122) y102 | B176[Rush0 -22..324 x, -610..198 z]; P31[Rush0 -75..352 x, -603..53 z] | @7 (102, -117) sector 30m; @119 (-47, -230) final base (beyond S5) 197m |

- Attackers' starting base (inferred): HQ @45 (67, 320), @132 (-108, 232)
- Defenders' final base (inferred): HQ @119 (-47, -230)
- Vehicle pads (58) by nearest HQ:
  - HQ @8 (284, 392) (in S1): 2 Light Transport, 1 Quad Bike
  - HQ @45 (67, 320) (start base (beyond S1)): 3 Light Transport, 1 Patrol Boat, 1 Quad Bike, 1 RHIB
  - HQ @132 (-108, 232) (start base (beyond S1)): 3 Light Transport, 3 Patrol Boat, 2 Quad Bike, 2 RHIB
  - HQ @48 (495, 370) (in S2): 5 Light Transport, 5 Patrol Boat, 3 RHIB
  - HQ @110 (459, 206) (in S3): 4 Light Transport, 1 Quad Bike
  - HQ @136 (392, -114) (in S4): 2 Patrol Boat, 2 RHIB
  - HQ @144 (398, -72) (in S4): 6 Light Transport, 1 IFV, 1 Patrol Boat
  - HQ @7 (102, -117) (in S5): 2 Light Transport, 1 Patrol Boat
  - HQ @119 (-47, -230) (final base (beyond S5)): 4 Patrol Boat, 1 IFV, 1 Light Transport
  - total: 26 Light Transport, 17 Patrol Boat, 8 RHIB, 5 Quad Bike, 2 IFV
- Emplacements (7): @10 HMG (47, -46) (nearest S5); @36 Anti-Aircraft (429, -64) (nearest S4); @52 HMG (65, -64) (nearest S5); @77 Anti-Aircraft (288, -186) (nearest S4); @105 Anti-Tank (530, -216) (nearest S4); @130 Anti-Tank (581, -137) (nearest S4); @175 HMG (601, -167) (nearest S4)
- Insertions (16) by nearest sector: S1:8, S2:8
- TelemetryArea: 10 (S1:2, S2:2, S3:2, S4:2, S5:2)
- Unusual: Naval layout: 58 pads, 26 Light Transport, 17 Patrol Boat, 8 RHIB, 5 Quad Bike, 2 IFV; no tank, no air vehicle.
- Unusual: The chain wraps an island group: S1 (225, 373) east to S2 (424, 373), south to S3 (470, 151), S4 (376, -89), then west to S5 (126, -136).
- Unusual: HQ @132 (-108, 232) and @45 (67, 320) are 361 m and 167 m from S1; @119 (-47, -230) is 197 m from S5.
- Unusual: Insertions form two groups of 8: one about 190 m west of S1 at x 0..40, z 230..270 (keys 0, 3, 16, 15), one at x 337..364, z 322..391 between S1 and S2 (keys 0, 3, 4, 5, 15, 16). The western group is on the start-base side and the eastern group lies between S1 and S2 (nearest S2, 75 m); all 16 are over 400 m from S5, so the orientation holds, but the start could also be read as the western group only.
- Unusual: Rush_Global holds 10 small polygons (ids 1-10), one per M-COM; each also contains that M-COM telemetry area (2 telemetry areas per sector).


### Blackwell Fields (MP_BADLANDS)

- Assets: Rush, Rush0, Rush0_Schematic, Rush_Global, Rush_Global_Schematic, Rush_Telemetry, generated/DD_Rush0_Schematics, generated/DD_Rush0_Volumes, rush/MeshVariationDb_Win32, rush/staticmodelgroup.physics, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}; GEM counts: {"GEM_VehicleSpawner": 6, "GEM_TelemetryArea": 4, "GEM_Battle_Pickup": 2, "GEM_Sector": 4, "GEM_StationarySpawner": 2, "GEM_Objective_MCOM": 8, "GEM_Insertion": 6, "GEM_HQ": 8}
- Layout variants: all 40 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S4, S1 = attackers' side): S1 (16, -397) -> S2 (114, -190) -> S3 (250, -128) -> S4 (265, -28)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-22, -427); 49 m from S1 vs 491 m from S4). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @16 (-182, -4) = shared default position dist 440 m | @42 (34, -385) y85; @72 (-2, -409) y85 | P4[Telemetry -42..91 x, -441..-318 z]; P11[Rush0 -34..110 x, -442..-189 z]; P54[Rush0 -34..79 x, -442..-320 z]; P66[Rush0 -34..115 x, -442..-150 z] | @43 (52, -346) sector 62m; @65 (62, -300) sector 107m; @84 (-68, -472) start base (beyond S1) 113m |
| S2 | @6 (-82, -4) = shared default position dist 269 m | @20 (124, -204) y75; @79 (104, -175) y74 | P1[Telemetry 55..157 x, -239..-139 z]; P10[Rush0 45..232 x, -243..-105 z]; P50[Rush0 -3..232 x, -250..-105 z]; P78[Rush0 -3..151 x, -250..-105 z] (+1 more) | @23 (140, -181) sector 27m |
| S3 | @60 (15, -12) = shared default position dist 262 m | @12 (233, -105) y76; @74 (268, -152) y77 | P24[Rush0 186..331 x, -235..-77 z]; P36[Rush0 186..331 x, -179..-77 z]; P57[Rush0 149..321 x, -242..-77 z]; P81[Rush0 186..321 x, -235..-77 z] | @27 (268, -152) sector 29m; @38 (214, -161) sector 49m |
| S4 | @63 (129, -22) = shared default position dist 135 m | @49 (293, -28) y76; @67 (237, -29) y75 | P76[Rush0 196..331 x, -78..19 z] | @21 (313, 42) final base (beyond S4) 85m; @83 (301, -83) sector 65m |

- Attackers' starting base (inferred): HQ @84 (-68, -472)
- Defenders' final base (inferred): HQ @21 (313, 42)
- Vehicle pads (6) by nearest HQ:
  - HQ @43 (52, -346) (in S1): 4 Quad Bike
  - HQ @84 (-68, -472) (start base (beyond S1)): 1 APC
  - HQ @23 (140, -181) (in S2): 1 APC
  - total: 4 Quad Bike, 2 APC
- Emplacements (2): @7 HMG (255, -108) (nearest S3); @55 HMG (280, -165) (nearest S3)
- Battle pickups (placed, not active in live game per README) (2): @4 Minigun (-54, -483) (nearest S1); @87 Minigun (61, -298) (nearest S1)
- Insertions (6) by nearest sector: S1:6
- TelemetryArea: 4 (S1:1, S2:1, S3:1, S4:1)
- Unusual: All four Sector markers sit on the default positions (-182,-4), (-82,-4), (15,-12), (129,-22) shared with five other maps, 135-440 m from the real M-COMs; sector extents here come from the M-COM groups and the Rush0 polygons they share (P11/P66/P54/P4, P10/P50/P78/P86/P1, P24/P36/P57/P81, P76).
- Unusual: Faction override: team 1 = Pax Armata, team 2 = NATO. If team 1 attacks, Pax Armata attacks here.
- Unusual: Only 6 pads: 4 Quad Bike at HQ @43, 2 APC; all in the S1/S2 half. 2 HMG emplacements both near S3.
- Unusual: HQ @84 (-68, -472) has Battle Pickup @4 Minigun beside it; Battle_Pickup instances are inactive in the live game.


### Iberian Offensive (MP_BATTERY)

- Assets: Rush, Rush0, Rush_Global_Schematic, Rush_Telemetry, MeshVariationDb_Win32
- Faction overrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}; GEM counts: {"GEM_HQ": 7, "GEM_Sector": 3, "GEM_TelemetryArea": 3, "GEM_Battle_Pickup": 2, "GEM_Objective_MCOM": 6, "GEM_Insertion": 6, "GEM_VehicleSpawner": 1}
- Layout variants: all 28 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S3, S1 = attackers' side): S1 (715, 110) -> S2 (784, 85) -> S3 (823, 42)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (680, 145); 50 m from S1 vs 176 m from S3). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @4 (640, 207) dist 122 m | @18 (700, 89) y75; @56 (729, 130) y77 | P3[Telemetry 650..794 x, 42..211 z]; P66[Rush0 671..779 x, 57..163 z] | @46 (721, 112) sector 7m; @48 (670, 156) start base (beyond S1) 64m |
| S2 | @28 (708, 192) dist 132 m | @36 (767, 68) y78; @41 (802, 101) y78 | P2[Telemetry 706..845 x, 25..147 z]; P19[Rush0 724..822 x, 29..136 z]; P32[Rush0 724..822 x, 29..136 z] | @51 (771, 73) sector 18m; @65 (770, 80) sector 15m |
| S3 | @15 (798, 154) dist 114 m | @14 (833, 57) y72; @45 (814, 28) y74 | P1[Telemetry 759..906 x, 0..120 z]; P11[Rush0 776..855 x, 14..106 z]; P31[Rush0 781..855 x, 14..106 z] | @1 (876, 72) final base (beyond S3) 61m; @8 (831, 50) sector 11m; @33 (832, 10) sector 34m |

- Attackers' starting base (inferred): HQ @48 (670, 156)
- Defenders' final base (inferred): HQ @1 (876, 72)
- Co-located HQ pairs (<12 m apart): @51+@65 (771, 73) (7 m)
- Vehicle pads (1) by nearest HQ:
  - HQ @48 (670, 156) (start base (beyond S1)): 1 Light Transport
  - total: 1 Light Transport
- Battle pickups (placed, not active in live game per README) (2): @10 Minigun (667, 167) (nearest S1); @50 Minigun (709, 93) (nearest S1)
- Insertions (6) by nearest sector: S1:6
- TelemetryArea: 3 (one within 20 m of each Sector marker; S1:2, S2:1 counts by nearest M-COM centre, which is the wrong anchor here because the markers lie 114 to 132 m from their pairs)
- Unusual: Only 3 sectors and 1 vehicle pad (a Light Transport at the start HQ @48).
- Unusual: Sector markers (@4, @28, @15) sit 114-132 m from their M-COM pairs, outside the pairs' polygons, so extents come from the M-COM polygons (P66, P19/P32, P11/P31).
- Unusual: Faction override: team 1 = Pax Armata, team 2 = NATO. 2 Minigun pickups both near the start.
- Unusual: Compact: the whole chain spans about 150 m (x 700-830).


### Liberation Peak (MP_CAPSTONE)

- Assets: Rush, Rush0, Rush0_Schematic, Rush_Global, Rush_Global_Schematic, Rush_Telemetry, rush/MeshVariationDb_Win32, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {}; GEM counts: {"GEM_Objective_MCOM": 8, "GEM_HQ": 8, "GEM_VehicleSpawner": 12, "GEM_Insertion": 8, "GEM_Battle_Pickup": 2, "GEM_TelemetryArea": 8, "GEM_Sector": 4}
- Layout variants: all 50 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S4, S1 = attackers' side): S1 (-62, 114) -> S2 (117, 68) -> S3 (177, 162) -> S4 (150, 311)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-131, 131); 71 m from S1 vs 334 m from S4). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @122 (-182, -4) = shared default position dist 168 m | @7 (-47, 79) y134; @21 (-77, 149) y136 | P5[Rush0 -124..3 x, 38..226 z]; P22[Rush0 -124..44 x, 17..226 z] | @19 (-39, 92) sector 32m; @106 (-185, 167) start base (beyond S1) 133m |
| S2 | @79 (15, -12) = shared default position dist 129 m | @1 (134, 52) y130; @64 (101, 85) y134 | P80[Rush0 22..195 x, 0..144 z]; P88[Rush0 -69..168 x, 0..144 z]; P97[Rush0 22..231 x, 0..150 z] | @54 (37, 81) sector 81m; @113 (172, 65) sector 54m |
| S3 | @37 (129, -22) = shared default position dist 190 m | @6 (168, 175) y138; @114 (185, 150) y138 | P17[Rush0 113..266 x, 83..220 z]; P38[Rush0 65..266 x, 83..291 z]; P104[Rush0 113..266 x, 33..266 z] | @3 (170, 227) sector 64m; @16 (190, 113) sector 51m; @28 (199, 234) sector 75m |
| S4 | @45 (-82, -4) = shared default position dist 391 m | @48 (154, 345) y171; @105 (147, 278) y159 | P2[Rush0 51..209 x, 262..388 z] | @25 (184, 374) final base (beyond S4) 72m |

- Attackers' starting base (inferred): HQ @106 (-185, 167)
- Defenders' final base (inferred): HQ @25 (184, 374)
- Vehicle pads (12) by nearest HQ:
  - HQ @19 (-39, 92) (in S1): 2 IFV, 2 Light Transport
  - HQ @106 (-185, 167) (start base (beyond S1)): 1 IFV, 1 Light Transport, 1 Quad Bike, 1 Tank
  - HQ @113 (172, 65) (in S2): 1 IFV, 1 Light Transport
  - HQ @3 (170, 227) (in S3): 1 Light Transport, 1 Quad Bike
  - total: 5 Light Transport, 4 IFV, 2 Quad Bike, 1 Tank
- Battle pickups (placed, not active in live game per README) (2): @24 Minigun (-34, 79) (nearest S1); @120 Minigun (180, 95) (nearest S2)
- Insertions (8) by nearest sector: S1:8
- TelemetryArea: 8 (S1:2, S2:2, S3:2, S4:2)
- Unusual: All four Sector markers sit on the shared default positions (see Badlands); the real extents are the M-COM polygons (S1 P22/P5, S2 P80/P88/P97, S3 P104/P17/P38, S4 P2).
- Unusual: S4 is on high ground (M-COM y 171 and 159 vs 130-138 elsewhere), HQ @25 (184, 374) is the only HQ beyond S4.
- Unusual: S3 has three HQs (@3, @16, @28), the most of any sector on this map. The only Tank pad is at HQ @106, the start-base HQ.
- Unusual: All 8 insertions are OnSpot types (keys 3, 4, 5), none of the Arrival types.


### Contaminated (MP_CONTAMINATED)

- Assets: Rush, Rush0, Rush0_Schematic, Rush_Global, Rush_Global_Schematic, Rush_Telemetry, generated/AG_Rush_DynamicDD_Schematic_A9B60BEC, generated/AG_Rush_DynamicDD_boxes_1857AB1E, rush/MeshVariationDb_Win32, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {}; GEM counts: {"GEM_HQ": 10, "GEM_Sector": 4, "GEM_Objective_MCOM": 6, "GEM_Insertion": 16}
- Layout variants: all 36 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S5, S1 = attackers' side): S1 (-185, -48) -> S2 (-158, 60) -> S3 (-82, -13) -> S4 (-3, -74) -> S5 (146, -76)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-228, 42); 99 m from S1 vs 392 m from S5). I read that end as the attackers' start; the data has no team label. Confidence: low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | none (fewer markers than M-COM groups) | @45 (-185, -48) y64 | none | @32 (-170, -25) sector 27m |
| S2 | none (fewer markers than M-COM groups) | @43 (-158, 60) y67 | none | @14 (-271, 70) sector 114m |
| S3 | none (fewer markers than M-COM groups) | @20 (-82, -13) y64 | none | @15 (-82, -10) sector 3m; @30 (-82, -11) sector 2m |
| S4 | none (fewer markers than M-COM groups) | @12 (-3, -74) y60 | none | @17 (-14, -31) sector 44m; @44 (34, 4) sector 86m |
| S5 | none (fewer markers than M-COM groups) | @5 (146, -76) y62 | none | @1 (197, -98) final base (beyond S5) 55m; @4 (126, -37) sector 44m; @24 (191, -176) final base (beyond S5) 109m |

- Attackers' starting base (inferred): no HQ beyond S1; the S1 HQs serve the start
- Defenders' final base (inferred): HQ @1 (197, -98), @24 (191, -176)
- Co-located HQ pairs (<12 m apart): @15+@30 (-82, -10) (2 m)
- HQ instances at stray or shared default positions, ignored: @26 (39, 40)
- Vehicle pads: none in this layer
- Insertions (16) by nearest sector: S1:4, S2:12
- Unusual: Four Sector markers (@3, @31, @39, @46), all on shared default positions, but five distinct M-COM positions plus a sixth (@21 at (-8, 31), the same default x/z as Outskirts MCOM @35). No Rush0 polygons or boxes exist at all (no containers on any instance), so sectors cannot be formed from the data; the five groups above are one M-COM each and are NOT a proven sector layout.
- Unusual: No vehicle pads, emplacements, deploy cams or pickups: only HQ (10), Sector (4), M-COM (6) and Insertion (16).
- Unusual: Insertions: 12 nearest S2, 4 nearest S1; HQ @15 and @30 are 1 m apart at (-82, -10).
- Unusual: HQ @26 is on the shared default (39, 40) and was ignored.


### Area 51 (MP_DRYLAKE)

- Assets: Cables/CableSet_d008a7c1-fc9b-462c-9713-0c18a4fd25f8_09d507ff-8486-4147-b466-37344b326e96, Cables/CableSet_d008a7c1-fc9b-462c-9713-0c18a4fd25f8_3b4195cb-64c6-4982-8ae3-4507e27ba59c, Rush, Rush_Global_Schematic, Rush0, Rush0_Schematic, Rush_Global, Rush_Global_Cables, generated/AG_Rush_DynamicDD_Schematic_A9B60BEC, generated/AG_Rush_DynamicDD_boxes_1857AB1E, cables/cableset_d008a7c1-fc9b-462c-9713-0c18a4fd25f8_09d507ff-8486-4147-b466-37344b326e96_mesh, cables/cableset_d008a7c1-fc9b-462c-9713-0c18a4fd25f8_3b4195cb-64c6-4982-8ae3-4507e27ba59c_mesh, rush/MeshVariationDb_Win32, rush/staticmodelgroup.physics, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {}; GEM counts: {"GEM_VehicleSpawner": 46, "GEM_Objective_MCOM": 10, "GEM_Insertion": 8, "GEM_SpecialCombatArea": 2, "GEM_Sector": 5, "GEM_HQ": 10, "GEM_VehicleSpawner_Forward": 2, "GEM_StationarySpawner": 3}
- Layout variants: all 86 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S5, S1 = attackers' side): S1 (457, 996) -> S2 (396, 1123) -> S3 (202, 1194) -> S4 (30, 1207) -> S5 (-8, 946)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (690, 961); 236 m from S1 vs 698 m from S5). I read that end as the attackers' start; the data has no team label. Confidence: medium.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @132 (600, 925) dist 159 m in B[] P[90, 114] | @85 (484, 1005) y56; @126 (429, 987) y59 | P90[Rush0 387..671 x, 800..1102 z]; P114[Rush0 387..671 x, 800..1102 z] | @57 (971, 768) start base (beyond S1) 562m; @137 (499, 973) start base (beyond S1) 48m |
| S2 | @30 (428, 1164) dist 51 m in B[] P[40, 70, 72, 133] | @32 (417, 1161) y57; @113 (376, 1085) y68 | P40[Rush0 305..596 x, 1016..1274 z]; P70[Rush0 305..596 x, 1016..1274 z]; P72[Rush0 305..596 x, 1055..1274 z]; P133[Rush0 235..596 x, 1016..1274 z] | @35 (422, 1062) sector 66m; @49 (410, 1114) sector 16m |
| S3 | @52 (252, 1200) dist 50 m in B[75] P[28, 29, 109, 133] | @3 (180, 1171) y58; @46 (224, 1216) y56 | B75[Rush0 150..299 x, 1132..1250 z]; P28[Rush0 97..424 x, 1077..1305 z]; P109[Rush0 97..424 x, 1046..1351 z] | @20 (271, 1179) sector 70m; @82 (257, 1179) sector 57m |
| S4 | @23 (31, 1157) dist 49 m in B[] P[55, 123] | @67 (22, 1251) y60; @68 (38, 1163) y63 | P55[Rush0 -70..150 x, 1074..1306 z]; P123[Rush0 -167..150 x, 962..1426 z] | @51 (50, 1172) sector 40m; @66 (-60, 1193) sector 91m; @110 (87, 1184) sector 61m |
| S5 | @19 (-10, 952) dist 6 m | @7 (29, 955) y72; @27 (-45, 938) y87 | none | @128 (2, 820) final base (beyond S5) 127m |

- Attackers' starting base (inferred): HQ @57 (971, 768); HQ @137 (499, 973) lies in the S1 polygons (S1 sector HQ, attacker side)
- Defenders' final base (inferred): HQ @128 (2, 820)
- Vehicle pads (48) by nearest HQ:
  - HQ @57 (971, 768) (start base (beyond S1)): 3 Dirt Bike, 3 Light Transport, 2 Forward vehicle spawner, 2 Tank, 1 APC
  - HQ @137 (499, 973) (S1 sector HQ): 3 Dirt Bike, 2 Light Transport, 2 Quad Bike, 1 Tank
  - HQ @35 (422, 1062) (in S2): 2 Quad Bike
  - HQ @49 (410, 1114) (in S2): 2 Light Transport, 2 Quad Bike, 2 Tank
  - HQ @20 (271, 1179) (in S3): 2 Quad Bike, 1 Light Transport, 1 Tank
  - HQ @82 (257, 1179) (in S3): 4 Dirt Bike, 1 IFV, 1 Light Transport, 1 Tank
  - HQ @51 (50, 1172) (in S4): 1 Attack Helicopter, 1 Light Transport
  - HQ @66 (-60, 1193) (in S4): 2 Dirt Bike, 1 Attack Helicopter, 1 Light Transport, 1 Tank
  - HQ @110 (87, 1184) (in S4): 2 Dirt Bike, 1 Light Transport
  - total: 14 Dirt Bike, 12 Light Transport, 8 Quad Bike, 8 Tank, 2 Attack Helicopter, 2 Forward vehicle spawner, 1 APC, 1 IFV
- Emplacements (3): @44 Anti-Aircraft (54, 1140) (nearest S4); @48 HMG (5, 1202) (nearest S4); @97 Anti-Tank (13, 1270) (nearest S4)
- Special combat areas (2): @16 (-10, 1192) (nearest S4); @119 (198, 1259) (nearest S3)
- Insertions (8) by nearest sector: S1:8
- Unusual: Largest start base: HQ @57 (971, 768) is 562 m from the first sector and has 3 Light Transport, 3 Dirt Bike, 2 Forward vehicle spawners, 2 Tank, 1 APC; 8 insertions (key 3 OnSpot) form two clusters, 4 near x 900 (start polygon) and 4 near x 450 to 500 (S1).
- Unusual: Air: 2 Attack Helicopter pads (HQ @51 and @66, both in S4 region). No fixed-wing.
- Unusual: S5 M-COMs @7 (29, 955) y72 and @27 (-45, 938) y87 are higher than every other Area 51 M-COM (y 56-68) and sit in no container at all, as does HQ @128 (2, 820, y65) and Sector marker @19.
- Unusual: Two SpecialCombatArea instances (@16 at (-10, 1192), @119 at (198, 1259)) inside S4/S3.


### Manhattan Bridge (MP_DUMBO)

- Assets: Rush, Rush0, Rush_Global, Rush_Global_Schematic, Rush_Telemetry, Rush_VFX, Rush_VFX_Schematic, MeshVariationDb_Win32
- Faction overrides: {"team1": "Alliance/NATO", "team2": "Coalition/Pax Armata"}; GEM counts: {"GEM_TelemetryArea": 6, "GEM_HQ": 8, "GEM_Objective_MCOM": 8, "GEM_Battle_Pickup": 2, "GEM_Insertion": 8, "GEM_Sector": 5, "GEM_DeployCam": 1, "GEM_SpecialCombatArea": 1}
- Layout variants: all 39 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S4, S1 = attackers' side): S1 (-137, -473) -> S2 (-52, -382) -> S3 (-21, -247) -> S4 (80, -208)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-168, -479); 31 m from S1 vs 367 m from S4). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @54 (-118, -462) dist 21 m in B[] P[40, 4] | @16 (-138, -450) y54; @48 (-137, -495) y54 | P4[Telemetry -179..-76 x, -558..-400 z]; P40[Rush0 -179..-76 x, -537..-417 z] | @17 (-106, -458) sector 35m; @19 (-234, -496) start base (beyond S1) 99m |
| S2 | @84 (-66, -398) dist 21 m in B[] P[11, 57, 1] | @10 (-76, -358) y54; @33 (-28, -404) y54 | P1[Telemetry -129..76 x, -528..-287 z]; P11[Rush0 -112..58 x, -511..-287 z] | @7 (-70, -416) sector 39m; @75 (-41, -345) sector 38m |
| S3 | @50 (-37, -244) dist 16 m in B[] P[66, 6] | @89 (-47, -221) y57; @91 (5, -273) y55 | P6[Rush0 103..199 x, -291..-165 z]; P66[Rush0 -102..58 x, -343..-201 z] | @21 (-37, -241) sector 18m; @70 (-33, -241) sector 13m |
| S4 | @46 (84, -225) dist 17 m in B[] P[67, 5] | @49 (94, -221) y59; @53 (66, -194) y62 | P5[Telemetry -38..111 x, -315..-147 z]; P67[Rush0 -21..111 x, -285..-166 z] | @5 (154, -224) final base (beyond S4) 75m; @45 (75, -206) sector 6m |

- Attackers' starting base (inferred): HQ @19 (-234, -496)
- Defenders' final base (inferred): HQ @5 (154, -224)
- Co-located HQ pairs (<12 m apart): @21+@70 (-37, -241) (5 m)
- Vehicle pads: none in this layer
- Deploy cams (1): @62 (-65, -394) (nearest S2)
- Battle pickups (placed, not active in live game per README) (2): @22 Minigun (-122, -461) (nearest S1); @80 Minigun (-217, -514) (nearest S1)
- Special combat areas (1): @83 (-41, -344) (nearest S2)
- Insertions (8) by nearest sector: S1:8
- TelemetryArea: 6 (S1:2, S2:1, S3:1, S4:2)
- Unusual: Five Sector markers for four M-COM pairs: @63 (-26, -365) and @84 (-66, -398) both lie in the S2 polygons (P11); the 5th marker has no M-COM pair of its own.
- Unusual: Faction override: team 1 = NATO, team 2 = Pax Armata (equals the default). DeployCam @62 at y=229 (overview camera).
- Unusual: No vehicle pads or emplacements. HQ @21 and @70 are 5 m apart in S3.
- Unusual: The chain bends: S1-S2-S3 run north-south along x -137..0, S4 swings east to x 80.


### Eastwood (MP_EASTWOOD)

- Assets: Rush0
- Faction overrides: {}; GEM counts: {"GEM_TelemetryArea": 8, "GEM_HQ": 8, "GEM_Insertion": 16, "GEM_StationarySpawner": 2, "GEM_Sector": 4, "GEM_Objective_MCOM": 8, "GEM_VehicleSpawner": 5, "GEM_Battle_Pickup": 1}
- Layout variants: all 52 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S4, S1 = attackers' side): S1 (-90, 191) -> S2 (31, 28) -> S3 (100, -14) -> S4 (209, -155)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-128, 186); 39 m from S1 vs 480 m from S4). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @52 (-172, -7) dist 214 m | @25 (-81, 212) y235; @45 (-98, 170) y235 | P24[Rush0 -256..25 x, 102..299 z]; P59[Rush0 -147..93 x, -25..245 z]; P94[Rush0 -147..-38 x, 118..245 z] | @3 (-37, 119) sector 89m; @20 (-6, 164) sector 88m; @41 (-215, 176) start base (beyond S1) 126m |
| S2 | @81 (-28, 65) dist 69 m in B[] P[59, 92] | @19 (9, 13) y233; @97 (52, 43) y234 | P2[Rush0 -52..125 x, -45..115 z]; P15[Rush0 -52..96 x, -42..115 z]; P46[Rush0 -52..96 x, -42..115 z]; P72[Rush0 -52..169 x, -84..115 z] | @13 (29, 46) sector 18m |
| S3 | @14 (62, 27) dist 56 m in B[] P[2, 10, 62, 72] | @53 (76, -32) y233; @78 (124, 5) y232 | P10[Rush0 19..169 x, -197..77 z]; P60[Rush0 28..166 x, -70..48 z]; P62[Rush0 19..166 x, -70..77 z]; P72[Rush0 -52..169 x, -84..115 z] | @43 (100, -26) sector 12m; @69 (132, -88) sector 81m; @73 (110, -101) sector 88m |
| S4 | @36 (273, -160) dist 64 m | @57 (203, -169) y240; @82 (214, -142) y238 | P98[Rush0 146..256 x, -207..-116 z] | @18 (265, -190) final base (beyond S4) 66m |

- Attackers' starting base (inferred): HQ @41 (-215, 176)
- Defenders' final base (inferred): HQ @18 (265, -190)
- Vehicle pads (5) by nearest HQ:
  - HQ @3 (-37, 119) (in S1): 2 Golf Cart
  - HQ @41 (-215, 176) (start base (beyond S1)): 1 APC
  - HQ @13 (29, 46) (in S2): 2 Golf Cart
  - total: 4 Golf Cart, 1 APC
- Emplacements (2): @12 HMG (37, 42) (nearest S2); @35 HMG (212, -134) (nearest S4)
- Battle pickups (placed, not active in live game per README) (1): @74 Minigun (-156, 168) (nearest S1)
- Insertions (16) by nearest sector: S1:16
- TelemetryArea: 8 (S1:1, S2:3, S3:2, S4:2)
- Unusual: Layer assets: only `Rush0` is listed. Heights are about 233 (M-COM y 232-240).
- Unusual: Sector markers are unreliable: @14 (62, 348, 27) and @81 (-28, 341, 65) sit at y 341-348 (110 m above the M-COMs), @52 (-172, -7) is 214 m from S1, @36 (273, -160) is 64 m from S4.
- Unusual: Vehicle pads: 4 Golf Cart (2 at HQ @3 in S1, 2 at HQ @13 in S2) and 1 APC at the start HQ @41. 2 HMG emplacements, 1 Minigun pickup.
- Unusual: S3 has three HQs (@43, @69, @73); @69 and @73 are 81-88 m from the M-COMs.
- Unusual: All 16 insertions are at the S1 end.


### Operation Firestorm (MP_FIRESTORM)

- Assets: Rush, Rush0, Rush0_Schematic, Rush_Cover, Rush_Global, Rush_Global_Schematic, Rush_Telemetry, rush/MeshVariationDb_Win32, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {"team1": "Alliance/NATO", "team2": "Coalition/Pax Armata"}; GEM counts: {"GEM_VehicleSpawner": 4, "GEM_TelemetryArea": 6, "GEM_HQ": 6, "GEM_Insertion": 8, "GEM_VehicleResupplyStation": 5, "GEM_Battle_Pickup": 2, "GEM_Sector": 3, "GEM_Objective_MCOM": 6, "GEM_DeployCam": 1}
- Layout variants: all 41 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S3, S1 = attackers' side): S1 (51, -117) -> S2 (-101, -112) -> S3 (-278, -71)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (139, -87); 93 m from S1 vs 418 m from S3). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @30 (15, -12) = shared default position dist 111 m | @33 (62, -143) y121; @80 (40, -91) y121 | P68[Rush0 -34..114 x, -226..-12 z] | @20 (75, -118) sector 24m; @46 (223, -76) start base (beyond S1) 177m |
| S2 | @47 (-82, -4) = shared default position dist 109 m | @49 (-86, -77) y125; @97 (-116, -147) y125 | P10[Rush0 -204..-28 x, -226..-12 z] | @75 (-69, -104) sector 33m; @76 (-137, -126) sector 39m |
| S3 | @37 (-182, -4) = shared default position dist 117 m | @74 (-290, -96) y134; @105 (-267, -46) y134 | P85[Rush0 -311..-192 x, -204..-11 z] | @16 (-397, -55) final base (beyond S3) 120m; @67 (-252, -101) sector 40m |

- Attackers' starting base (inferred): HQ @46 (223, -76)
- Defenders' final base (inferred): HQ @16 (-397, -55)
- Vehicle pads (4) by nearest HQ:
  - HQ @20 (75, -118) (in S1): 1 Tank
  - HQ @46 (223, -76) (start base (beyond S1)): 1 Tank
  - HQ @16 (-397, -55) (final base (beyond S3)): 1 IFV
  - HQ @67 (-252, -101) (in S3): 1 Tank
  - total: 3 Tank, 1 IFV
- Vehicle resupply stations (5): @28 (19, -93) (nearest S1); @31 (-133, -132) (nearest S2); @51 (-373, -48) (nearest S3); @69 (-255, -140) (nearest S3); @71 (242, -88) (nearest S1)
- Deploy cams (1): @101 (-65, -231) (nearest S2)
- Battle pickups (placed, not active in live game per README) (2): @29 Minigun (60, -119) (nearest S1); @66 Railgun (186, -99) (nearest S1)
- Insertions (8) by nearest sector: S1:8
- TelemetryArea: 6 (S1:2, S2:2, S3:2)
- Unusual: Only 3 sectors. Sector markers sit on default positions (see Badlands).
- Unusual: 5 vehicle resupply stations (2 near S1, 1 S2, 2 S3) and 1 deploy cam @101 at y=1500 (overview camera).
- Unusual: Pads: 3 Tank and 1 IFV; the Tank pads are at HQ @20 and @46 (start side) and @67 (S3).
- Unusual: Battle pickups: Minigun @29 and Railgun @66 (the only Railgun placement in Rush).
- Unusual: Faction override: team 1 = NATO, team 2 = Pax Armata (equals the default).


### Railway to Golmud (MP_GOLMUDRAILWAY)

- Assets: PF_MIL_UH60_BlackhawkHelicopter_01_Breakable, PF_MIL_UH60_BlackhawkHelicopter_01_InTransport, Rush, Rush_Global_Schematic, generated/AG_Rush_DynamicDD_Schematic_A9B60BEC, generated/AG_Rush_DynamicDD_boxes_1857AB1E, Rush0, Rush0_Schematic, Rush_Global, rush/MeshVariationDb_Win32, rush/staticmodelgroup.physics, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {}; GEM counts: {"GEM_TelemetryArea": 10, "GEM_VehicleSpawner": 41, "GEM_Objective_MCOM": 10, "GEM_Battle_Pickup": 7, "GEM_Sector": 5, "GEM_VehicleResupplyStation": 3, "GEM_HQ": 10, "GEM_Insertion": 8, "GEM_StationarySpawner": 2, "GEM_DeployCam": 1, "GEM_SpecialCombatArea": 1}
- Layout variants: all 98 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S5, S1 = attackers' side): S1 (-120, 562) -> S2 (-138, 676) -> S3 (-140, 797) -> S4 (-110, 894) -> S5 (-123, 1029)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-111, 416); 146 m from S1 vs 613 m from S5). I read that end as the attackers' start; the data has no team label. Confidence: medium.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @46 (-109, 475) dist 87 m in B[] P[29, 105] | @15 (-94, 563) y705; @101 (-146, 561) y705 | P29[Rush0 -486..288 x, 57..1217 z]; P105[Rush0 -390..165 x, 422..643 z] | @119 (-102, 277) start base (beyond S1) 285m; @124 (-104, 483) start base (beyond S1) 80m |
| S2 | @144 (-146, 664) dist 14 m in B[9] P[29, 138] | @69 (-124, 685) y730; @159 (-151, 667) y728 | P29[Rush0 -486..288 x, 57..1217 z]; P138[Rush0 -366..129 x, 589..730 z] | @127 (-128, 667) sector 13m; @169 (-128, 667) sector 13m |
| S3 | @56 (-86, 773) dist 58 m in B[] P[9, 29] | @139 (-167, 785) y736; @145 (-112, 809) y738 | P9[Rush0 -306..81 x, 678..840 z]; P29[Rush0 -486..288 x, 57..1217 z] | @58 (-137, 754) sector 42m; @155 (-137, 754) sector 42m |
| S4 | @86 (-145, 869) dist 42 m in B[] P[29, 141] | @31 (-60, 889) y738; @136 (-159, 899) y743 | P29[Rush0 -486..288 x, 57..1217 z]; P141[Rush0 -257..6 x, 817..954 z] | @85 (-133, 886) sector 25m; @199 (-128, 870) sector 31m |
| S5 | @57 (-133, 974) dist 56 m in B[] P[16, 29] | @4 (-155, 1044) y758; @49 (-91, 1014) y756 | P16[Rush0 -248..18 x, 927..1056 z]; P29[Rush0 -486..288 x, 57..1217 z] | @109 (-114, 1100) final base (beyond S5) 72m; @156 (-125, 999) sector 30m |

- Attackers' starting base (inferred): HQ @119 (-102, 277), @124 (-104, 483)
- Defenders' final base (inferred): HQ @109 (-114, 1100)
- Co-located HQ pairs (<12 m apart): @58+@155 (-137, 754) (0 m); @127+@169 (-128, 667) (0 m)
- Vehicle pads (41) by nearest HQ:
  - HQ @119 (-102, 277) (start base (beyond S1)): 2 Dirt Bike, 2 Light Transport, 2 Tank, 1 APC, 1 Scout Helicopter
  - HQ @124 (-104, 483) (start base (beyond S1)): 3 Dirt Bike, 2 Light Transport, 2 Tank, 1 APC, 1 Scout Helicopter
  - HQ @127 (-128, 667) (in S2): 2 IFV, 2 Tank, 1 APC, 1 Dirt Bike, 1 Light Transport
  - HQ @58 (-137, 754) (in S3): 2 Dirt Bike, 1 APC, 1 Light Transport, 1 Tank
  - HQ @85 (-133, 886) (in S4): 1 APC, 1 Dirt Bike, 1 IFV
  - HQ @199 (-128, 870) (in S4): 2 IFV, 2 Tank, 1 Dirt Bike
  - HQ @109 (-114, 1100) (final base (beyond S5)): 1 Tank
  - HQ @156 (-125, 999) (in S5): 2 IFV, 1 Light Transport
  - total: 10 Dirt Bike, 10 Tank, 7 IFV, 7 Light Transport, 5 APC, 2 Scout Helicopter
- Emplacements (2): @78 Anti-Tank (-155, 582) (nearest S1); @164 Anti-Tank (-122, 1059) (nearest S5)
- Vehicle resupply stations (3): @51 (-112, 1040) (nearest S5); @158 (-102, 208) (nearest S1); @200 (-118, 881) (nearest S4)
- Deploy cams (1): @171 (20, 576) (nearest S1)
- Battle pickups (placed, not active in live game per README) (7): @11 Smoke Screen (-169, 771) (nearest S3); @39 Smoke Screen (-170, 534) (nearest S1); @74 Smoke Screen (-165, 900) (nearest S4); @131 Smoke Screen (-18, 394) (nearest S1); @143 Artillery Strike (-72, 1065) (nearest S5); @160 Artillery Strike (-21, 566) (nearest S1); @177 Artillery Strike (-61, 894) (nearest S4)
- Special combat areas (1): @180 (-204, 389) (nearest S1)
- Insertions (8) by nearest sector: S1:7, S2:1
- TelemetryArea: 10 (S1:2, S2:2, S3:2, S4:2, S5:2)
- Unusual: Uniform north-south chain along x -160..-60 on the train line; M-COM y 705-758 (map base is high).
- Unusual: HQ duplicates: @58 and @155 at (-137, 754); @127 and @169 at (-128, 667) (same position, 0 m apart); every other sector has 1-2 HQs.
- Unusual: 41 pads: 10 Tank, 10 Dirt Bike, 7 Light Transport, 7 IFV, 5 APC, 2 Scout Helicopter (HQ @119 and @124, both in the start region).
- Unusual: 7 Battle_Pickup instances (4 Smoke Screen, 3 Artillery Strike) and 3 vehicle resupply stations; 1 SpecialCombatArea @180 near the start.
- Unusual: The start region has HQ @119 (285 m behind S1) and @124 (80 m): a long run-up before the first sector.


### Tsuru Reef (MP_ISOLATED)

- Assets: Rush, Rush0_Schematic, Rush_Global, Rush_Global_Schematic, Rush0, generated/AG_Rush_DynamicDD_Schematic_A9B60BEC, generated/AG_Rush_DynamicDD_boxes_1857AB1E, rush/MeshVariationDb_Win32, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}; GEM counts: {"GEM_Insertion": 16, "GEM_VehicleSpawner": 13, "GEM_Objective_MCOM": 6, "GEM_TelemetryArea": 6, "GEM_Sector": 3, "GEM_HQ": 6}
- Layout variants: all 50 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S3, S1 = attackers' side): S1 (-589, -170) -> S2 (-771, -20) -> S3 (-1032, -7)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-540, -226); 75 m from S1 vs 538 m from S3). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @40 (-581, -173) dist 9 m in B[] P[68, 93] | @10 (-613, -182) y104; @43 (-566, -158) y106 | P68[Rush0 -818..-481 x, -232..0 z]; P93[Rush0 -747..-481 x, -232..-81 z] | @34 (-653, -102) sector 93m; @67 (-649, -153) sector 62m; @79 (-465, -321) start base (beyond S1) 195m |
| S2 | @28 (-767, -31) dist 11 m in B[4] P[1, 57, 94] | @5 (-766, 2) y105; @60 (-776, -43) y104 | P1[Rush0 -849..-591 x, -153..138 z]; P57[Rush0 -849..-530 x, -191..138 z]; P94[Rush0 -1004..-591 x, -153..145 z] | @50 (-821, -3) sector 53m; @70 (-888, 12) sector 121m |
| S3 | @26 (-997, -5) dist 35 m in B[] P[16, 61] | @90 (-1046, 16) y111; @91 (-1018, -30) y111 | P16[Rush0 -1121..-929 x, -142..159 z]; P61[Rush0 -1121..-790 x, -147..160 z] | @47 (-1100, -127) final base (beyond S3) 138m |

- Attackers' starting base (inferred): HQ @79 (-465, -321)
- Defenders' final base (inferred): HQ @47 (-1100, -127)
- Vehicle pads (13) by nearest HQ:
  - HQ @67 (-649, -153) (in S1): 2 Dirt Bike, 2 Quad Bike, 1 Light Transport
  - HQ @79 (-465, -321) (start base (beyond S1)): 2 Light Transport, 1 Dirt Bike
  - HQ @50 (-821, -3) (in S2): 2 Light Transport, 1 Quad Bike, 1 RHIB
  - HQ @47 (-1100, -127) (final base (beyond S3)): 1 Quad Bike
  - total: 5 Light Transport, 4 Quad Bike, 3 Dirt Bike, 1 RHIB
- Insertions (16) by nearest sector: S1:16
- TelemetryArea: 6 (S1:2, S2:2, S3:2)
- Unusual: Faction override: team 1 = Pax Armata, team 2 = NATO.
- Unusual: All 16 insertions are at the S1 end (1 Arrival, 5 OnSpot v1, 1 OnSpot v2, 5 OnSpot v3, 2 Chaotic v1, 2 Chaotic v2).
- Unusual: 13 pads: 5 Light Transport, 4 Quad Bike, 3 Dirt Bike, 1 RHIB. No emplacements, no air.
- Unusual: Sector markers lie within 40 m of the M-COM centres (real placement); the three sectors run west (x -589, -771, -1032).


### New Sobek City (MP_OUTSKIRTS)

- Assets: Rush, Rush0, Rush0_Schematic, Rush_Global, generated/DD_Rush0_Schematics, generated/DD_Rush0_Volumes, Rush_Global_Schematic, rush/MeshVariationDb_Win32, rush/staticmodelgroup.physics, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {}; GEM counts: {"GEM_SpecialCombatArea": 1, "GEM_TelemetryArea": 8, "GEM_HQ": 9, "GEM_Objective_MCOM": 9, "GEM_Sector": 6, "GEM_Insertion": 6, "GEM_DeployCam": 2, "GEM_Battle_Pickup": 2}
- Layout variants: all 43 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S4, S1 = attackers' side): S1 (-140, -98) -> S2 (-66, -68) -> S3 (-12, -82) -> S4 (91, -52)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-178, -93); 39 m from S1 vs 272 m from S4). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @27 (-132, -99) dist 8 m in B[2] P[25] | @17 (-153, -87) y94; @91 (-128, -108) y92 | B2[Global -193..-123 x, -143..-50 z]; P25[Rush0 -173..-93 x, -136..-57 z] | @6 (-205, -100) start base (beyond S1) 65m; @89 (-132, -98) sector 8m |
| S2 | @16 (-67, -73) dist 4 m in B[7] P[19] | @13 (-61, -98) y97; @75 (-70, -38) y96 | P19[Rush0 -120..-32 x, -135..-9 z] | @60 (-67, -68) sector 2m; @64 (-69, -77) sector 10m |
| S3 | @100 (-12, -83) dist 0 m in B[7] P[57] | @44 (-15, -100) y97; @48 (-8, -64) y96 | B7[Global -79..23 x, -109..-47 z]; P57[Rush0 -46..35 x, -136..-10 z] | @30 (-5, -77) sector 8m; @33 (-10, -83) sector 2m; @78 (-5, -77) sector 8m |
| S4 | @29 (82, -56) dist 9 m in B[] P[79, 8] | @76 (97, -81) y96; @87 (84, -24) y97 | P8[Global 22..148 x, -144..13 z]; P79[Rush0 11..159 x, -133..-3 z] | @45 (148, -21) final base (beyond S4) 66m; @53 (76, -60) sector 17m |

- Attackers' starting base (inferred): HQ @6 (-205, -100)
- Defenders' final base (inferred): HQ @45 (148, -21)
- Co-located HQ pairs (<12 m apart): @30+@33 (-5, -77) (7 m); @30+@78 (-5, -77) (0 m); @33+@78 (-10, -83) (7 m); @60+@64 (-67, -68) (9 m)
- Vehicle pads: none in this layer
- Deploy cams (2): @51 (-65, 272) (nearest S2); @71 (-65, 272) (nearest S2)
- Battle pickups (placed, not active in live game per README) (2): @83 Minigun (-241, -108) (nearest S1); @90 Minigun (-2, -80) (nearest S3)
- Special combat areas (1): @1 (0, 0) (nearest S3)
- Insertions (6) by nearest sector: S1:6
- TelemetryArea: 8 (S1:2, S2:2, S3:2, S4:2)
- Unusual: No vehicle pads in the Rush layer (vehicles possibly come from elsewhere or are absent).
- Unusual: Six Sector markers for four M-COM pairs: @100 and @105 are both at (-12, -83), and @29 and @107 are both at (82, -56). Duplicated markers are unexplained.
- Unusual: M-COM @35 (-8, 31) sits on the shared default position (also Contaminated @21), over 100 m from every other M-COM, and has no containers; ignored.
- Unusual: HQ pairs: @30 and @78 are both at (-5, -77); @33 is 7 m away; @60 and @64 are 9 m apart. S3 therefore has three HQ instances.
- Unusual: DeployCam @51 and @71 are both at (-65, 272) y94 (the same x/z as the Abbasid cam), and SpecialCombatArea @1 is at (0, 0, 0).
- Unusual: Battle_Pickup Minigun @83 near the start HQ @6 and @90 inside S3.


### Vegas Strip (MP_PARADISE)

- Assets: Rush, Rush0, Rush0_Schematic, Rush_Global_Schematic, Rush_Global, generated/AG_Rush_DynamicDD_Schematic_A9B60BEC, generated/AG_Rush_DynamicDD_boxes_1857AB1E, rush/MeshVariationDb_Win32, rush/staticmodelgroup.physics, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}; GEM counts: {"GEM_Insertion": 16, "GEM_Objective_MCOM": 8, "GEM_HQ": 11, "GEM_Sector": 4, "GEM_VehicleSpawner": 6, "GEM_StationarySpawner": 1}
- Layout variants: all 46 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S4, S1 = attackers' side): S1 (-80, 260) -> S2 (-60, 187) -> S3 (-95, 124) -> S4 (-94, 2)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-49, 302); 52 m from S1 vs 303 m from S4). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @7 (-92, 273) dist 18 m in B[] P[33, 71] | @39 (-96, 252) y58; @62 (-64, 268) y56 | P33[Rush0 -172..-17 x, 211..328 z]; P71[Rush0 -170..5 x, 218..354 z] | @60 (-91, 262) sector 11m; @65 (-59, 375) start base (beyond S1) 117m |
| S2 | @20 (128, -26) dist 284 m | @28 (-80, 180) y52; @83 (-39, 195) y58 | P19[Rush0 -153..-36 x, 156..239 z]; P38[Rush0 -159..10 x, 137..306 z] | @14 (-94, 202) sector 37m; @52 (0, 143) sector 74m |
| S3 | @73 (13, -13) dist 173 m in B[] P[56] | @2 (-98, 130) y42; @78 (-91, 117) y52 | P16[Rush0 -131..34 x, -8..160 z]; P46[Rush0 -143..23 x, 63..165 z] | @24 (-74, 118) sector 21m; @48 (-119, 171) sector 53m |
| S4 | @25 (-83, -6) dist 13 m in B[] P[21, 56] | @63 (-70, -19) y60; @77 (-118, 22) y52 | none | @6 (-117, -46) final base (beyond S4) 53m; @11 (-82, -156) final base (beyond S4) 158m; @31 (205, -96) final base (beyond S4) 314m; @34 (-89, 53) sector 52m |

Correction after review: by container polygons HQ @48 (-119, 171) belongs to S2 and HQ @52 (0, 143) to S3 (the distance rule above swaps them); S2 = @14, @48; S3 = @24, @52. No pads at either. Sector markers @12 (38.4, 38.4), @20 and @73 sit on near-default grid positions, not the exact Siege of Cairo defaults.

- Attackers' starting base (inferred): HQ @65 (-59, 375)
- Defenders' final base (inferred): HQ @6 (-117, -46), @11 (-82, -156), @31 (205, -96)
- HQ instances at stray or shared default positions, ignored: @12 (38, 38)
- Vehicle pads (6) by nearest HQ:
  - HQ @60 (-91, 262) (in S1): 2 Dirt Bike, 1 APC
  - HQ @65 (-59, 375) (start base (beyond S1)): 1 APC
  - HQ @14 (-94, 202) (in S2): 1 APC
  - HQ @24 (-74, 118) (in S3): 1 APC
  - total: 4 APC, 2 Dirt Bike
- Emplacements (1): @57 Anti-Tank (-19, 109) (nearest S3)
- Insertions (16) by nearest sector: S1:14, S2:2
- Unusual: Faction override: team 1 = Pax Armata, team 2 = NATO.
- Unusual: Sector markers: @7 (-92, 273) and @25 (-83, -6) are real (13-18 m from M-COMs); @73 (13, -13) and @20 (128, -26) are 90+ m from any M-COM and look like default placements, so S2 and S3 have no usable marker.
- Unusual: HQ @12 (38, 38) is the shared default and was ignored; HQ @31 (205, -96) is 314 m off the chain with no containers (unused or stray); HQ @11 (-82, -156) is in box B79 158 m beyond S4 and is the far final base.
- Unusual: 6 pads only (4 APC, 2 Dirt Bike), all on the S1/S2/S3 side; one Anti-Tank emplacement @57 near S3.
- Unusual: The S3 M-COM pair is 15 m apart (@2 and @78), the closest pair of any Rush map; S2 is 43 m.
- Unusual: 14 of 16 insertions are at S1 (key 3 OnSpot v1).


### Cairo Bazaar (MP_PLAZA)

- Assets: Rush, Rush_Global_Schematic, Rush0, Rush0_Schematic, Rush_Global, generated/AG_Rush_DynamicDD_Schematic_A9B60BEC, generated/AG_Rush_DynamicDD_boxes_1857AB1E, rush/MeshVariationDb_Win32, rush/staticmodelgroup.physics, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}; GEM counts: {"GEM_HQ": 8, "GEM_Objective_MCOM": 8, "GEM_Insertion": 16, "GEM_Sector": 4, "GEM_SpecialCombatArea": 1, "GEM_VehicleSpawner": 4, "GEM_StationarySpawner": 2}
- Layout variants: all 43 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S4, S1 = attackers' side): S1 (-60, 136) -> S2 (-18, 10) -> S3 (90, 30) -> S4 (121, 154)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-60, 172); 35 m from S1 vs 182 m from S4). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @79 (-182, -4) = shared default position dist 186 m | @28 (-42, 119) y71; @83 (-78, 154) y73 | P5[Rush0 -97..-10 x, 100..179 z] | @4 (-62, 85) sector 52m; @24 (-62, 112) sector 24m; @90 (-44, 210) start base (beyond S1) 75m |
| S2 | @9 (-82, -4) = shared default position dist 65 m in B[] P[33, 75] | @6 (9, 30) y66; @38 (-46, -10) y65 | P75[Rush0 -108..41 x, -38..84 z] | @57 (12, 6) sector 31m |
| S3 | @98 (15, -12) = shared default position dist 85 m in B[] P[48, 75] | @10 (70, 48) y62; @93 (110, 11) y62 | P58[Rush0 36..147 x, -29..64 z]; P61[Rush0 36..148 x, -29..96 z] | @17 (122, 57) sector 42m; @27 (90, 24) sector 6m; @29 (58, 10) sector 37m |
| S4 | @94 (129, -22) = shared default position dist 175 m | @19 (96, 166) y64; @22 (147, 142) y64 | P76[Rush0 48..162 x, 95..199 z] | @52 (117, 217) final base (beyond S4) 64m |

- Attackers' starting base (inferred): HQ @90 (-44, 210)
- Defenders' final base (inferred): HQ @52 (117, 217)
- Vehicle pads (4) by nearest HQ:
  - HQ @24 (-62, 112) (in S1): 1 APC
  - HQ @27 (90, 24) (in S3): 3 Dirt Bike
  - total: 3 Dirt Bike, 1 APC
- Emplacements (2): @97 HMG (99, 11) (nearest S3); @99 Anti-Tank (18, 2) (nearest S2)
- Special combat areas (1): @32 (20, 93) (nearest S1)
- Insertions (16) by nearest sector: S1:16
- Unusual: Faction override: team 1 = Pax Armata, team 2 = NATO.
- Unusual: All four Sector markers (@9, @79, @94, @98) sit on the shared default positions; real extents are the M-COM polygons (S1 P5, S2 P75, S3 P58/P61, S4 P76).
- Unusual: Only 4 pads: 1 APC at HQ @24 (S1) and 3 Dirt Bike at HQ @27 (S3); emplacements HMG @97 and Anti-Tank @99.
- Unusual: All 16 insertions are at the S1 end (keys 0, 1, 3, 5, 15).
- Unusual: SpecialCombatArea @32 at (20, 93) between S1 and S2.


### Hagental Base (MP_SUBSURFACE)

- Assets: Rush, Rush0, Rush0_Schematic, Rush_Global, Rush_Global_Schematic, generated/AG_Rush_DynamicDD_Schematic_A9B60BEC, generated/AG_Rush_DynamicDD_boxes_1857AB1E, rush/MeshVariationDb_Win32, rush_networkregistry_Win32, rush_templatedescriptorregistry
- Faction overrides: {}; GEM counts: {"GEM_HQ": 10, "GEM_TelemetryArea": 5, "GEM_Objective_MCOM": 10, "GEM_Sector": 5, "GEM_Insertion": 6, "GEM_Battle_Pickup": 1, "GEM_DeployCam": 1}
- Layout variants: all 38 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S5, S1 = attackers' side): S1 (-163, 23) -> S2 (-71, 21) -> S3 (37, -21) -> S4 (115, -42) -> S5 (195, -68)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (-204, 55); 51 m from S1 vs 417 m from S5). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @35 (-182, -4) = shared default position dist 33 m in B[] P[83, 4] | @47 (-193, 28) y64; @75 (-133, 19) y67 | P83[Rush0 -228..-114 x, -26..93 z] | @41 (-189, 25) sector 26m; @82 (-243, 92) start base (beyond S1) 105m |
| S2 | @16 (-82, -4) = shared default position dist 27 m in B[3] P[40] | @57 (-66, 38) y67; @59 (-77, 4) y66 | B3[Global -141..-40 x, -20..76 z]; P40[Rush0 -114..-39 x, -26..82 z] | @56 (-75, 17) sector 6m; @62 (-86, 15) sector 16m |
| S3 | @55 (13, -9) dist 26 m in B[] P[6, 2] | @18 (38, 6) y65; @69 (37, -48) y65 | P2[Global -36..59 x, -107..94 z]; P6[Rush0 -40..71 x, -100..82 z] | @21 (14, -7) sector 28m; @66 (13, -8) sector 27m |
| S4 | @8 (129, -22) = shared default position dist 25 m in B[60, 5] P[] | @5 (106, -10) y66; @49 (123, -76) y64 | B5[Global 61..145 x, -90..19 z]; B60[Rush0 71..147 x, -100..11 z] | @2 (106, -27) sector 17m; @38 (86, -27) sector 33m |
| S5 | @65 (124, 38) dist 127 m | @50 (172, -92) y64; @53 (218, -45) y67 | P1[Global 146..258 x, -125..20 z]; P44[Rush0 147..255 x, -125..11 z] | @39 (210, -41) sector 32m; @48 (256, -114) final base (beyond S5) 76m |

- Attackers' starting base (inferred): HQ @82 (-243, 92)
- Defenders' final base (inferred): HQ @48 (256, -114)
- Co-located HQ pairs (<12 m apart): @21+@66 (14, -7) (2 m); @56+@62 (-75, 17) (11 m)
- Vehicle pads: none in this layer
- Deploy cams (1): @87 (0, 0) (nearest S3)
- Battle pickups (placed, not active in live game per README) (1): @85 Minigun (-246, 84) (nearest S1)
- Insertions (6) by nearest sector: S1:6
- TelemetryArea: 5 (S1:4, S2:1)
- Unusual: No vehicle pads, no emplacements: infantry-only layer.
- Unusual: Sector markers @35, @16, @8 are on default positions; @55 (13, -9) and @65 (124, 38, y74) are not; @65 lies off the chain with no container.
- Unusual: DeployCam @87 at (0, 233, 0) (overview cam, y 233).
- Unusual: Telemetry: 4 of the 5 telemetry areas lie in the S1 region (x -171..-118), 1 in S2, none in S3-S5.
- Unusual: Battle_Pickup Minigun @85 sits beside the start HQ @82.


### Mirak Valley (MP_TUNGSTEN)

- Assets: Rush, Rush0, MeshVariationDb_Win32, staticmodelgroup.physics
- Faction overrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}; GEM counts: {"GEM_VehicleSpawner": 9, "GEM_Objective_MCOM": 15, "GEM_HQ": 10, "GEM_Sector": 4, "GEM_DeployCam": 1, "GEM_StationarySpawner": 3, "GEM_TelemetryArea": 9, "GEM_Insertion": 8, "GEM_Battle_Pickup": 1}
- Layout variants: all 60 gameplay instances come from layer `Rush0` (no Small/Large variants exist); `Rush_Global`/`Rush_Telemetry` supply only containers (polygons/boxes).
- Sector chain (inferred order S1 -> S4, S1 = attackers' side): S1 (300, -421) -> S2 (-1, -375) -> S3 (-203, -274) -> S4 (-362, -247)
- Direction basis: every Insertion (arrival animation) cluster sits at the S1 end (centroid (371, -454); 78 m from S1 vs 762 m from S4). I read that end as the attackers' start; the data has no team label. Confidence: medium-low.

| Sector | Marker (Sector@idx) | M-COMs (instance, x z, y) | Containers shared by the M-COMs | HQs in this region (instance, x z, distance to M-COM centre) |
|---|---|---|---|---|
| S1 | @70 (275, -429) dist 26 m in B[] P[77] | @95 (280, -451) y86; @125 (321, -391) y84 | P77[Rush0 178..385 x, -548..-255 z] | @50 (249, -416) sector 51m; @52 (167, -378) sector 140m; @117 (461, -499) start base (beyond S1) 178m |
| S2 | @11 (58, -368) dist 59 m in B[] P[8] | @6 (-26, -344) y86; @34 (54, -374) y86; @53 (-31, -406) y87 | P8[Rush0 -102..276 x, -536..-238 z] | @127 (-40, -323) sector 65m |
| S3 | @123 (-178, -285) dist 27 m in B[] P[38] | @7 (-208, -307) y84; @57 (-197, -240) y86 | P38[Rush0 -278..-87 x, -425..-158 z] | @21 (-201, -284) sector 11m; @134 (-122, -315) sector 91m |
| S4 | @26 (-317, -252) dist 45 m in B[] P[41] | @37 (-387, -274) y86; @126 (-338, -220) y86 | P41[Rush0 -421..-259 x, -370..-137 z] | @10 (-466, -233) final base (beyond S4) 104m; @61 (-320, -251) sector 42m |

- Attackers' starting base (inferred): HQ @117 (461, -499)
- Defenders' final base (inferred): HQ @10 (-466, -233)
- HQ instances at stray or shared default positions, ignored: @16 (-166, -188), @100 (-23, -180)
- Vehicle pads (9) by nearest HQ:
  - HQ @50 (249, -416) (in S1): 2 Light Transport, 1 Quad Bike, 1 Tank
  - HQ @117 (461, -499) (start base (beyond S1)): 1 IFV, 1 Tank
  - HQ @127 (-40, -323) (in S2): 1 IFV, 1 Light Transport
  - HQ @134 (-122, -315) (in S3): 1 IFV
  - total: 3 IFV, 3 Light Transport, 2 Tank, 1 Quad Bike
- Emplacements (3): @18 Anti-Tank (-238, -259) (nearest S3); @22 Anti-Tank (-69, -354) (nearest S2); @94 Anti-Tank (73, -347) (nearest S2)
- Deploy cams (1): @17 (13, -428) (nearest S2)
- Battle pickups (placed, not active in live game per README) (1): @59 Minigun (191, -384) (nearest S1)
- Insertions (8) by nearest sector: S1:8
- TelemetryArea: 9 (S1:5, S2:2, S3:2)
- Unusual: 15 M-COM instances, but only 9 belong to the real chain (S1 2, S2 3, S3 2, S4 2). The other six are strays at y 96-97: @25 and @68 at (-15, -100), @39 and @44 at (-8, -64), @73 (84, -24), @110 (97, -81); these x/z match the New Sobek City M-COMs exactly. HQ @16 (-166, -188) and @100 (-23, -180) (also y 96-97, no container) look like the same stray set; all were excluded.
- Unusual: S2 is the only sector with three M-COMs (@6, @34, @53 in P8).
- Unusual: Faction override: team 1 = Pax Armata, team 2 = NATO. Only 6 containers exist in the layer.
- Unusual: Pads (9): 3 IFV, 3 Light Transport, 2 Tank, 1 Quad Bike; 3 Anti-Tank emplacements (S2 x2, S3); DeployCam @17 at y=1649 (overview camera).
- Unusual: Long run-up: start HQ @117 is 178 m east of S1 and the final base HQ @10 is 104 m beyond S4.


## 3. Cross-map table

Pads split: attackers = start base + the first floor(n/2) sectors; contested = the middle sector of a chain with an odd number of sectors; defenders = remaining sectors + final base. This is a static spatial reading, not a team label from the data.

| Map | M-COM stations (Sector markers if different) | M-COMs per station | Attacker start (inferred, chain S1 centre -> last) | Pads attackers (start base + front half) | Pads contested (middle sector, odd chains) | Pads defenders (back half + final base) | Pads total | Air vehicles |
|---|---|---|---|---|---|---|---|---|
| Siege of Cairo | 4 | 2/2/2/2 | (91, -56) -> (-174, -18) | 3 | 0 | 0 | 3 | no |
| Empire State | 3 (4 markers) | 2/2/2 | (-643, 29) -> (-593, -129) | 0 | 0 | 0 | 0 | no |
| Wake Island | 5 | 2/2/2/2/2 | (225, 373) -> (126, -136) | 32 | 5 | 21 | 58 | no |
| Blackwell Fields | 4 | 2/2/2/2 | (16, -397) -> (265, -28) | 6 | 0 | 0 | 6 | no |
| Iberian Offensive | 3 | 2/2/2 | (715, 110) -> (823, 42) | 1 | 0 | 0 | 1 | no |
| Liberation Peak | 4 | 2/2/2/2 | (-62, 114) -> (150, 311) | 10 | 0 | 2 | 12 | no |
| Contaminated | unresolved (4 markers, 6 M-COMs, no containers; 5 singles by x or 3 pairs) | unresolved | (-185, -48) -> (146, -76) | 0 | 0 | 0 | 0 | no |
| Area 51 | 5 | 2/2/2/2/2 | (457, 996) -> (-8, 946) | 27 | 11 | 10 | 48 | yes (2) |
| Manhattan Bridge | 4 (5 markers) | 2/2/2/2 | (-137, -473) -> (80, -208) | 0 | 0 | 0 | 0 | no |
| Eastwood | 4 | 2/2/2/2 | (-90, 191) -> (209, -155) | 5 | 0 | 0 | 5 | no |
| Operation Firestorm | 3 | 2/2/2 | (51, -117) -> (-278, -71) | 2 | 0 | 2 | 4 | no |
| Railway to Golmud | 5 | 2/2/2/2/2 | (-120, 562) -> (-123, 1029) | 24 | 5 | 12 | 41 | yes (2) |
| Tsuru Reef | 3 | 2/2/2 | (-589, -170) -> (-1032, -7) | 8 | 4 | 1 | 13 | no |
| New Sobek City | 4 (6 markers) | 2/2/2/2 | (-140, -98) -> (91, -52) | 0 | 0 | 0 | 0 | no |
| Vegas Strip | 4 | 2/2/2/2 | (-80, 260) -> (-94, 2) | 5 | 0 | 1 | 6 | no |
| Cairo Bazaar | 4 | 2/2/2/2 | (-60, 136) -> (121, 154) | 1 | 0 | 3 | 4 | no |
| Hagental Base | 5 | 2/2/2/2/2 | (-163, 23) -> (195, -68) | 0 | 0 | 0 | 0 | no |
| Mirak Valley | 4 | 2/3/2/2 | (300, -421) -> (-362, -247) | 8 | 0 | 1 | 9 | no |

## 4. Open questions (instance indices are the `@n` numbers in `Rush-maps.txt`)

1. Attacker side. Nothing in the data labels teams. I inferred the attackers' end from the Insertion (arrival animation) instances, which cluster at one end of every chain; the opposite reading (insertions belong to defenders, or to both teams) would flip every chain. `SimEx_CheckMCOMStatus.OwningTeamInt` defaults to 1, which, if it means the M-COM owner, would make team 1 the defender. Needs the round graph constants or a live-game check.
2. Saints Quarter (MP_LIMESTONE) has no Rush layer in either capture. Eastwood's capture lists only the `Rush0` asset (no Rush, Rush_Global or Telemetry), so its container set may be incomplete.
3. Per-sector tickets. Not a named tweakable. Where is the amount awarded by `SimEx_SetSectorReinforcement` set (unnamed constant in `GME_Sim_Rush_Round`, or `GMPF_Reinforcement`)? What unit do `R_iSectorTime` (15), `R_iOutOfBounds_TimeToReturn` (5) and `R_SoldierDeathScoreBleed` (1) use? Why is there no `R_iRemainingRespawnsThreshold2`?
4. Contaminated. 4 Sector markers (@3, @31, @39, @46, all on shared default positions), 6 M-COMs (@5, @12, @20, @21, @43, @45) and no containers at all. @21 (-8, 31) shares x/z with Outskirts @35. The M-COM to sector pairing, and whether @21 is live, is unresolved; no pads, emplacements, deploy cams or pickups exist in this layer.
5. Default-position Sector markers. Badlands (@6, @16, @60, @63), Capstone (@37, @45, @79, @122), Contaminated (above), Firestorm (@30, @37, @47), Plaza (@9, @79, @94, @98), Subsurface (@8, @16, @35) and Paradise (@73, @20, near-default) sit on (-182,-4), (-82,-4), (15,-12), (129,-22) or close, which are not the M-COM areas. Where are those sectors' real boxes? On these maps I grouped M-COMs by shared Rush0 polygon instead.
6. Outskirts. 6 Sector markers for 4 M-COM pairs (@100 and @105 at (-12, -83); @29 and @107 at (82, -56)); stray M-COM @35; HQ pairs @30/@78 (0 m) and @60/@64 (9 m) plus @33; DeployCam @51 and @71 identical; SpecialCombatArea @1 at (0, 0, 0). No pads in the layer.
7. Duplicated HQs. Golmud @58/@155 (-137, 754) and @127/@169 (-128, 667), Abbasid @26/@43 and @29/@53, Outskirts, Subsurface (@21/@66 at 1 m). Are these the same spawn used by two phases (defenders' HQ of phase k and attackers' HQ of phase k+1) or one HQ per team? Not testable here.
8. Stray or default HQs. Abbasid @32 and @83, Contaminated @26, Paradise @12 sit on (39, 40) (default); Paradise @31 (205, -96) has no containers and is 314 m off the chain; Paradise @11 (-82, -156) is the far final base HQ in B79.
9. Abbasid `Rush_Team1` and `Rush_Team2` assets: what do they place (team-specific sets, spawn restrictions)? They are not in the instance dump.
10. DryLake S5: M-COMs @7 and @27 (y72 and y87), Sector @19 and HQ @128 sit in no container and are higher than the rest; is that the final base's elevated bunker? Two SpecialCombatArea instances (@16, @119) and two `VehicleSpawner_Forward` pads at HQ @57.
11. Subsurface: Sector @65 (124, 74, 38) is off the chain and has no container; DeployCam @87 at (0, 233, 0); no pads or emplacements.
12. Battle_Pickup instances (Abbasid @25, @56; Badlands @4, @87; Capstone @24, @120; Firestorm @29, @66; Golmud @11, @39, @74, @131, @143, @160, @177; Outskirts @83, @90; Subsurface @85) are marked "placed but not active in the live game"; confirm none matter for Rush.
13. Pad ownership. `SimEx_SetVehicleTeam` assigns a vehicle's team at runtime; no pad has a team in the data, so the "attackers/defenders" pad split in section 3 is spatial only.
14. Vehicle names: the data gives only pad classes. The concrete vehicle model per faction (and Light Transport vs the in-game names of those classes) needs the vehicle spawner prefabs `GMPF_VehicleSpawner_*`.
15. Second-capture maps: Empire State marker @6 (-605, 204) has no M-COM (start zone or missing pair?); Manhattan Bridge has 5 markers for 4 M-COM pairs (@63 and @84 in one area); Eastwood markers @14, @81 sit at y 341-348 and @52, @36 are 64-214 m from the M-COMs; Mirak Valley has 6 stray M-COMs (@25, @68, @39, @44, @73, @110) and 2 stray HQs (@16, @100) at New Sobek City coordinates, and S2 holds three M-COMs (@6, @34, @53).
