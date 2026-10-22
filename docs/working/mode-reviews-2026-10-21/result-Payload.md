# Payload analysis, build 2.1.1.0

Source files: Payload-maps.txt, Payload-tweakables.txt, ui-text.txt, objective-table.json (empty, `{}`), map-names.json. Geometry computed by script on x/z (metres, straight lines). Ranges are the `[min..max]` in the data; `[0.0..0.0]` means no range declared. Values are client defaults and a server playlist can override them. Units are not stated in the data; seconds and metres per second are assumed where noted.

## 1. Mode rules (MUT_Payload, 62 tweakables)

UI text confirms (ui-text.txt): two rounds with teams switching roles; attackers escort the vehicle to the final checkpoint and must reach checkpoints before running out of time; stay close to keep it moving; if abandoned by attackers it moves back; defenders get close to make it stop; it retreats if the enemy is kept away long enough; round 1 attackers win by reaching the final checkpoint fastest or travelling furthest; round 2 attackers win by travelling further and faster than the round 1 result. A HARDCORE PAYLOAD variant exists as a name (Field_9e5045d8). No number appears in the UI text.

| Group | Tweakable | Value [range] | UI confirms |
|---|---|---|---|
| Speed | PL_fBaseSpeed | 1.75 | movement exists; value not stated |
| Speed | PL_fAttackerSpeedMultipliers | [0.0, 1.0, 1.33, 1.66, 2.1] [0.1..5.0] (index presumably attackers near, 0 to 4; inference) | "stay close to keep it moving" only |
| Speed | PL_fDefendersSpeedMultipliers | [0.0, 0.5] [0.1..5.0] (defenders-near multiplier; meaning inferred) | "defenders make it stop"; stop not visible as a value here (unresolved) |
| Speed | PL_fAttackersAcceleration / PL_fAttackersDeceleration | 4.0 / 0.5 [decel 0.1..3.0] | no |
| Speed | PL_fDefendersAcceleration / PL_fDefenderDeceleration | 2.0 / 0.5 [decel 0.1..3.0] | no |
| Exotic spline | PL_bUseExoticSplineSystem | true | no |
| Exotic spline | PL_fExoticSplineBaseSpeed | 1.0 | no |
| Exotic spline | PL_fExoticSplineAttackerSpeedMultipliers | [0.0, 1.0, 1.33, 1.66, 2.1] [0.1..5.0] | no |
| Exotic spline | PL_fExoticSplineDefendersSpeedMultipliers | [0.0, 0.5] [0.1..5.0] | no |
| Exotic spline | Pl_fExoticSplineDistanceToTravelInCheckpoint | 10.0 | no |
| Exotic spline | PL_fExoticSplineTimeMultiplierFirstSector / LaterSectors | 3.0 / 1.4 | no |
| Time | PL_bUseAutomaticTimeSystem | true | "reach checkpoints before running out of time" (time exists) |
| Time | PL_fTimeMultiplierFirstSector / LaterSectors | 3.0 / 1.4 (presumably time added per checkpoint scaled by sector length; inference) | no |
| Time | PL_iLowTimeWarning | 30 [0..120] | no |
| Time | PL_iUrgencyTimeThreshold / PL_fUrgencyDistanceThreshold | 30 [0..120] / 0.66 [0.0..1.0] | no |
| Time | PL_iLobbyPlayerCountStartTimer | 16 | no |
| Time | PL_iPlayersRequiredToStartTimer | 8 | no |
| Time | PL_iLobbyPlayerCountToSpeedUpTimer / PL_iPlayersRequiredToSpeedUpTimer | 16 / 16 | no |
| Checkpoint | Pl_fDistanceToTravelInCheckpoint | 15.0 | no |
| Checkpoint | PL_fCheckpointPassedPause1 / Pause2 | 2.0 / 2.0 | no |
| Checkpoint | PL_bEnableCheckpointCutscene | true | no |
| Checkpoint | PL_fOpenTime / PL_fCloseTime / PL_fTimeToUnlock | 20.0 / 3.0 / 15.0 (purpose inferred from names) | no |
| Retreat | PL_fRetreatTimer | 10.0 [0.0..100.0] (delay before retreat; no separate retreat-speed tweakable) | retreat exists, delay not stated |
| Retreat | PL_AwardSuccessfulRetreat | true | no |
| Mines | PL_bAllowMines / PL_bVisibleMines | true / false | not in UI text |
| Mines | CheckpointMines.ExplosionEntityData.BlastDamage / DamageMultiplier | 350.0 / 1.0 | no |
| Smoke | PL_bAllowPayloadSmoke / PL_fSmokeCooldownInteract | true / 45.0 [0.0..600.0] | no |
| Respawn | PL_fTeam1RespawnDelay / PL_fTeam2RespawnDelay | 8.0 / 8.0 | no |
| Out of bounds | PL_iOutOfBounds_TimeToReturn | 5 | no |
| Rating | PL_fRound1MajorSectorRatingThreshold / Minor | 0.33 / 0.66 | no |
| Rating | PL_fRound2MajorSectorRatingThreshold / Minor | 30.0 / 30.0 | no |
| Armor | PL_fPayloadArmorMultiplier | 1000.0 [0.0..1000.0] | no |
| Steering | PF_fSteeringThreshold / PF_fThrottleThreshold / PF_fThrottlePenalty / PF_fInitialStartingDist | 0.6 [0..1] / 0.5 [0..1] / 0.0 / 13.0 [0..20] | no |
| Misc | PL_bUseFlags true; PL_bUseBreacher true; PL_bAddRepairingEngineers false; PL_iSoldierMandownType 1; PL_fNoInteractivityTimeoutOverride 60.0 [0..600]; PL_iCommanderVoice 0; PL_bShowDebug false | as listed | no |
| Class hints | Engineer / Assault / Support / Recon Recommended | all false | no |

Not present as named tweakables (do not assume): round time, base time or time added per checkpoint (only the two multipliers above), push radius, stop radius, player counts per radius (the multiplier arrays may be indexed by counts; not stated), retreat speed, overtime, XP values, per-metre scoring. These would live in the round-logic graphs or the vehicle/volume prefabs, not extracted here. The rating threshold pairs differ in scale between rounds (fractions 0.33/0.66 in round 1, 30.0 in round 2); what they rate is not stated (open question).

UI view models (runtime bindings with null defaults; they carry names only, no numbers):
- Payload_Distance_ViewModelEx: CheckpointActiveInt, MI_Pres_Gem_Checkpoint, DistanceToNextCheckpoint, AttackerScoreFloat, AttackerScoreTarget. The HUD shows distance to the next checkpoint and an attacker score with a target (target presumably the round 1 result; inference).
- Payload_Points_ViewModelEx: SectionsRawProgress / SectionsRawTargetProgress, AttackingTeamProgression, DefendingTeamProgression, AttackingTeamSectorsCompleted, DefendingTeamSectionsCompleted, SectionsTotalCount, CheckpointsPassedFriendly / Enemy, IsPayloadMovingForward, AttackingTeamIsPlayerTeam, ScoreIndicatorCollection, TeamPoints. Scoring is by progress through sections; the per-distance values are not in this data.

## 2. Maps

Payload-maps.txt holds 11 map blocks. Ten have Payload instances; MP_GOLMUDRAILWAY (Railway to Golmud) has only the asset `MP_Payload0_Schematic` and zero GEM instances (empty stub). The "8 maps lacking a Payload layer" cannot be reproduced exactly from the files given: map-names.json lists 19 maps, of which only Siege of Cairo, Blackwell Fields, Iberian Offensive, Liberation Peak, Manhattan Bridge and New Sobek City appear in Payload-maps.txt. Without a block in this file: Operation Firestorm, Eastwood, Saints Quarter, Empire State, Mirak Valley, Fort Lyndon, and the Portal maps (Area 22B, Downtown, Redline Storage, Defense Nexus, Golf Course, Marina, Portal Sandbox); also Tsuru Reef, Vegas Strip and Area 51 by the README list (not in map-names.json; absent only from this file, not verified elsewhere).

Method. Order: the Payload start is the GEM_Payload instance; checkpoints are ordered by a greedy nearest-neighbour chain from the start, which equals the order by straight-line distance from the start on every map. No spline or path data is in the extraction, so lengths are straight-line legs between points (a lower bound of the real road length). No Checkpoint instance marks the end of the route (Checkpoint count is one lower than the Sector count on every map), so I take the Sector marker farthest from the start as the final area (inference) and give the length both to the last Checkpoint and to that sector. HQ grouping: nearest of start, each checkpoint, or final sector by straight-line distance. The data does not label side or phase, so confidence is low to medium; an HQ within about 30 m of an anchor is reliable, longer distances are weak. "Sector boxes" are Sector marker points; the enclosing BOX/POLY phase areas are in the raw file.

Five maps (Wake Island, Blackwell Fields, Contaminated, Cairo Bazaar, Hagental Base) have identical layouts: payload at (-190, -190), checkpoints (-99.1, -181.9), (-20.9, -181.2), (33.8, -178.7), the same eight HQs, four sectors on round numbers (-140, -80, 10, 90 along z=-180 to -190), the same insertions, no mines, a straight line at y=70. This is a shared template copied into each map, not a per-map route. Confidence high that they are identical; whether they are used in live play is unknown.

### Per-map data

### Siege of Cairo (MP_ABBASID)

- Layer assets: Payload_Global_Schematic, MP_Payload0, MP_Payload0_Schematic, Payload, Payload_Global, payload/MeshVariationDb_Win32, payload_networkregistry_Win32, payload_templatedescriptorregistry
- factionOverrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"} (team1 = Pax Armata, team2 = Alliance/NATO; swapped from default)
- Payload start: @24 (-209.5, 67.9, 10.4)
- Route (greedy nearest-neighbour chain from the start, straight-line x/z legs; Euclidean-distance-from-start order gives the same order on every map): start -> CP1 @38 (-62.9, 33.8) [leg 148.5 m] -> CP2 @7 (29.8, 1.1) [leg 98.3 m]
- Route length start to last Checkpoint instance: 246.8 m. To the farthest Sector marker beyond it (@64, (121.9, -36.5), +99.5 m, assumed final destination, inference): 346.2 m.
- Mines (7): near CP1: @9 (-49.4, 30.6; 14 m from CP), @42 (-49.8, 36.6; 13 m from CP), @58 (-50.6, 33.8; 12 m from CP); near CP2: @3 (40.3, -6.9; 13 m from CP), @11 (41.3, -7.8; 15 m from CP), @67 (38.9, -7.9; 13 m from CP), @69 (40.1, -8.8; 14 m from CP)
- Sector boxes (Sector markers, not rectangles): @1 (-75.5, 10.6), @17 (104.0, -33.6), @19 (7.8, 23.8), @64 (121.9, -36.5)
- HQs by nearest anchor (start/checkpoint): CP1: @60 (-82.5, -68.5; 104 m); CP2: @16 (44.3, 11.9; 18 m), @72 (3.3, 25.2; 36 m), @73 (3.3, 25.4; 36 m), @74 (3.0, 25.2; 36 m); final sector: @13 (138.6, -107.4; 73 m), @36 (170.7, -92.2; 74 m), @59 (89.0, -20.2; 37 m)
- TelemetryArea: @22 (13.8, 28.4), @23 (-74.0, -24.8), @33 (115.0, -55.3), @51 (-154.9, -18.5); Insertion: @6 Cautious_Arrival (-90.6, -56.7), @56 Cautious_OnSpot_v3 (-27.5, 34.0), @65 Cautious_Arrival (-17.8, 34.1), @66 Cautious_OnSpot_v1 (-81.5, -61.3)

### Wake Island (MP_ATOLL)

- Layer assets: MP_Payload0_Schematic, Payload, Payload_Global, Payload_Global_Schematic, MP_Payload0, generated/AG_Payload_DynamicDD_Schematic_FA5B3FE3, generated/AG_Payload_DynamicDD_boxes_44F8C09F, payload/MeshVariationDb_Win32, payload_networkregistry_Win32, payload_templatedescriptorregistry
- factionOverrides: {}
- Payload start: @15 (-190.0, 70.0, -190.0)
- Route (greedy nearest-neighbour chain from the start, straight-line x/z legs; Euclidean-distance-from-start order gives the same order on every map): start -> CP1 @31 (-99.1, -181.9) [leg 91.3 m] -> CP2 @8 (-20.9, -181.2) [leg 78.2 m] -> CP3 @37 (33.8, -178.7) [leg 54.8 m]
- Route length start to last Checkpoint instance: 224.2 m. To the farthest Sector marker beyond it (@28, (90.0, -160.0), +59.2 m, assumed final destination, inference): 283.4 m.
- Mines: none
- Sector boxes (Sector markers, not rectangles): @6 (-140.0, -180.0), @12 (10.0, -180.0), @23 (-80.0, -190.0), @28 (90.0, -160.0)
- HQs by nearest anchor (start/checkpoint): start: @27 (-187.2, -189.5; 3 m); CP1: @16 (-127.7, -190.0; 30 m), @38 (-77.2, -190.3; 23 m), @40 (-107.8, -198.0; 18 m); CP2: @4 (-11.9, -191.3; 14 m); CP3: @2 (60.0, -180.0; 26 m), @34 (54.5, -187.0; 22 m); final sector: @1 (124.5, -188.3; 45 m)
- TelemetryArea: ; Insertion: @10 Cautious_Arrival (-81.5, -200.7), @21 Cautious_Arrival (-181.2, -180.2), @26 Cautious_Arrival (-187.8, -176.0), @36 Cautious_Arrival (-71.8, -191.3)

### Blackwell Fields (MP_BADLANDS)

- Layer assets: MP_Payload0, MP_Payload0_Schematic, Payload, Payload_Global, Payload_Global_Schematic, generated/DD_MP_Payload0_Schematics, generated/DD_MP_Payload0_Volumes, payload/MeshVariationDb_Win32, payload_networkregistry_Win32, payload_templatedescriptorregistry
- factionOverrides: {}
- Payload start: @11 (-190.0, 70.0, -190.0)
- Route (greedy nearest-neighbour chain from the start, straight-line x/z legs; Euclidean-distance-from-start order gives the same order on every map): start -> CP1 @17 (-99.1, -181.9) [leg 91.3 m] -> CP2 @2 (-20.9, -181.2) [leg 78.2 m] -> CP3 @6 (33.8, -178.7) [leg 54.8 m]
- Route length start to last Checkpoint instance: 224.2 m. To the farthest Sector marker beyond it (@5, (90.0, -160.0), +59.2 m, assumed final destination, inference): 283.4 m.
- Mines: none
- Sector boxes (Sector markers, not rectangles): @5 (90.0, -160.0), @8 (10.0, -180.0), @24 (-80.0, -190.0), @30 (-140.0, -180.0)
- HQs by nearest anchor (start/checkpoint): start: @26 (-187.2, -189.5; 3 m); CP1: @18 (-127.7, -190.0; 30 m), @28 (-107.8, -198.0; 18 m), @35 (-77.2, -190.3; 23 m); CP2: @36 (-11.9, -191.3; 14 m); CP3: @19 (54.5, -187.0; 22 m), @22 (60.0, -180.0; 26 m); final sector: @38 (124.5, -188.3; 45 m)
- TelemetryArea: ; Insertion: @15 Cautious_Arrival (-81.5, -200.7), @16 Cautious_Arrival (-187.8, -176.0), @25 Cautious_Arrival (-181.2, -180.2), @34 Cautious_Arrival (-71.8, -191.3)

### Iberian Offensive (MP_BATTERY)

- Layer assets: MP_Payload0, MP_Payload0_EcsPrefab_ecsPrefab, MP_Payload0_Schematic, MeshVariationDb_Win32
- factionOverrides: {}
- Payload start: @24 (815.6, 89.2, 222.7)
- Route (greedy nearest-neighbour chain from the start, straight-line x/z legs; Euclidean-distance-from-start order gives the same order on every map): start -> CP1 @40 (752.5, 167.8) [leg 83.6 m] -> CP2 @34 (764.8, 112.0) [leg 57.1 m]
- Route length start to last Checkpoint instance: 140.8 m. To the farthest Sector marker beyond it (@2, (815.3, 73.5), +63.5 m, assumed final destination, inference): 204.3 m.
- Mines: none
- Sector boxes (Sector markers, not rectangles): @2 (815.3, 73.5), @8 (792.2, 194.7), @17 (761.4, 132.3)
- HQs by nearest anchor (start/checkpoint): start: @11 (822.1, 214.9; 10 m); CP1: @30 (774.0, 184.7; 27 m), @32 (746.9, 144.0; 24 m); CP2: @18 (777.2, 96.2; 20 m), @20 (761.0, 130.9; 19 m); final sector: @31 (851.2, 51.8; 42 m)
- TelemetryArea: @7 (765.4, 129.3), @16 (802.6, 204.8), @22 (830.7, 64.0); Insertion: @4 Cautious_OnSpot_v2 (828.3, 232.6), @9 Cautious_OnSpot_v2 (792.9, 168.9), @21 Cautious_OnSpot_v2 (756.6, 174.9), @23 Cautious_OnSpot_v2 (834.3, 230.3)

### Liberation Peak (MP_CAPSTONE)

- Layer assets: MP_Payload0, MP_Payload0_Schematic, Payload, Payload_Cover, Payload_Global_Schematic, Payload_Telemetry, Payload_Global, payload/MeshVariationDb_Win32, payload_networkregistry_Win32, payload_templatedescriptorregistry
- factionOverrides: {}
- Payload start: @75 (-16.6, 135.2, 112.6)
- Route (greedy nearest-neighbour chain from the start, straight-line x/z legs; Euclidean-distance-from-start order gives the same order on every map): start -> CP1 @42 (54.9, 62.5) [leg 87.3 m] -> CP2 @63 (151.3, 97.4) [leg 102.5 m]
- Route length start to last Checkpoint instance: 189.8 m. To the farthest Sector marker beyond it (@31, (169.0, 142.1), +48.1 m, assumed final destination, inference): 237.9 m.
- Mines (8): near CP1: @9 (61.4, 62.2; 7 m from CP), @47 (65.4, 65.1; 11 m from CP), @50 (63.1, 63.9; 8 m from CP), @58 (65.0, 61.6; 10 m from CP); near CP2: @24 (161.7, 102.4; 12 m from CP), @43 (161.5, 98.8; 10 m from CP), @65 (159.5, 100.3; 9 m from CP), @67 (162.4, 100.6; 12 m from CP)
- Sector boxes (Sector markers, not rectangles): @15 (137.0, 101.1), @25 (166.3, 142.7), @31 (169.0, 142.1), @76 (34.9, 79.0)
- HQs by nearest anchor (start/checkpoint): start: @48 (-37.8, 111.4; 21 m); CP1: @69 (34.5, 70.4; 22 m); CP2: @12 (101.1, 86.5; 51 m), @74 (150.8, 94.8; 3 m); final sector: @72 (186.9, 159.2; 25 m), @78 (211.3, 233.8; 101 m)
- TelemetryArea: @13 (169.0, 136.0), @23 (174.1, 118.4), @26 (-9.7, 95.0), @73 (103.0, 76.2); Insertion: @28 Chaotic_Arrival_v1 (78.3, 67.6), @37 Cautious_OnSpot_v2 (-41.8, 115.9), @61 Cautious_Arrival (-41.4, 127.6), @62 Cautious_OnSpot_v2 (84.9, 68.7)

### Contaminated (MP_CONTAMINATED)

- Layer assets: Payload, Payload0, Payload0_Schematic, Payload_Global, Payload_Global_Schematic, Payload_Telemetry, generated/AG_Payload_DynamicDD_Schematic_FA5B3FE3, generated/AG_Payload_DynamicDD_boxes_44F8C09F, payload/MeshVariationDb_Win32, payload_networkregistry_Win32, payload_templatedescriptorregistry
- factionOverrides: {}
- Payload start: @38 (-190.0, 70.0, -190.0)
- Route (greedy nearest-neighbour chain from the start, straight-line x/z legs; Euclidean-distance-from-start order gives the same order on every map): start -> CP1 @62 (-99.1, -181.9) [leg 91.3 m] -> CP2 @14 (-20.9, -181.2) [leg 78.2 m] -> CP3 @29 (33.8, -178.7) [leg 54.8 m]
- Route length start to last Checkpoint instance: 224.2 m. To the farthest Sector marker beyond it (@17, (90.0, -160.0), +59.2 m, assumed final destination, inference): 283.4 m.
- Mines: none
- Sector boxes (Sector markers, not rectangles): @17 (90.0, -160.0), @31 (-80.0, -190.0), @40 (-140.0, -180.0), @55 (10.0, -180.0)
- HQs by nearest anchor (start/checkpoint): start: @33 (-187.2, -189.5; 3 m); CP1: @9 (-77.2, -190.3; 23 m), @24 (-107.8, -198.0; 18 m), @61 (-127.7, -190.0; 30 m); CP2: @2 (-11.9, -191.3; 14 m); CP3: @18 (54.5, -187.0; 22 m), @48 (60.0, -180.0; 26 m); final sector: @13 (124.5, -188.3; 45 m)
- TelemetryArea: ; Insertion: @12 Cautious_Arrival (-71.8, -191.3), @30 Cautious_Arrival (-81.5, -200.7), @36 Cautious_Arrival (-181.2, -180.2), @49 Cautious_Arrival (-187.8, -176.0)

### Manhattan Bridge (MP_DUMBO)

- Layer assets: MP_Payload0, MP_Payload0_EcsPrefab_ecsPrefab, MP_Payload0_Schematic, MeshVariationDb_Win32
- factionOverrides: {}
- Payload start: @42 (32.0, 61.1, -182.4)
- Route (greedy nearest-neighbour chain from the start, straight-line x/z legs; Euclidean-distance-from-start order gives the same order on every map): start -> CP1 @18 (-25.6, -276.5) [leg 110.3 m] -> CP2 @43 (-115.2, -352.0) [leg 117.2 m]
- Route length start to last Checkpoint instance: 227.5 m. To the farthest Sector marker beyond it (@16, (-147.1, -384.0), +45.2 m, assumed final destination, inference): 272.7 m.
- Mines (8): near CP1: @14 (-38.4, -278.4; 13 m from CP), @24 (-35.2, -276.2; 10 m from CP), @39 (-38.4, -273.3; 13 m from CP), @46 (-41.6, -275.2; 16 m from CP); near CP2: @12 (-131.2, -352.6; 16 m from CP), @40 (-128.6, -349.8; 14 m from CP), @66 (-124.8, -351.4; 10 m from CP), @68 (-127.4, -353.9; 12 m from CP)
- Sector boxes (Sector markers, not rectangles): @16 (-147.1, -384.0), @29 (-28.5, -267.8), @63 (-75.5, -332.8)
- HQs by nearest anchor (start/checkpoint): start: @60 (33.6, -184.0; 2 m); CP1: @21 (-19.2, -275.2; 7 m); CP2: @6 (-108.8, -352.0; 6 m), @8 (-72.0, -331.2; 48 m), @53 (-147.2, -352.0; 32 m); final sector: @11 (-147.2, -473.6; 90 m)
- TelemetryArea: @7 (-19.1, -238.8), @9 (-148.4, -356.0), @19 (-70.1, -327.7); Insertion: @10 Cautious_OnSpot_v3 (-69.4, -323.2), @13 Cautious_OnSpot_v1 (-67.2, -320.0), @20 Cautious_LongDistance (37.2, -178.7), @50 Cautious_Arrival (32.0, -177.6); DeployCam: @34 (-65.4, 207.0)

### New Sobek City (MP_OUTSKIRTS)

- Layer assets: MP_Payload0, MP_Payload0_EcsPrefab_ecsPrefab, MP_Payload0_Schematic, Payload, Payload_Global, Payload_Global_Schematic, generated/DD_MP_Payload0_Schematics, generated/DD_MP_Payload0_Volumes, payload/MeshVariationDb_Win32, payload/staticmodelgroup.physics, payload_networkregistry_Win32, payload_templatedescriptorregistry
- factionOverrides: {}
- Payload start: @28 (-230.3, 95.0, 10.6); @51 (-242.8, 97.0, 11.7); @68 (-152.1, 91.6, -167.9)
- Route (greedy nearest-neighbour chain from the start, straight-line x/z legs; Euclidean-distance-from-start order gives the same order on every map): start -> CP1 @20 (19.1, -79.0) [leg 265.0 m] -> CP2 @2 (119.7, -77.6) [leg 100.6 m]
- Route length start to last Checkpoint instance: 365.6 m. To the farthest Sector marker beyond it (@69, (158.1, -135.7), +69.6 m, assumed final destination, inference): 435.3 m.
- Mines (8): near CP1: @9 (32.6, -89.6; 17 m from CP), @26 (32.3, -83.2; 14 m from CP), @48 (31.7, -92.8; 19 m from CP), @53 (34.2, -86.7; 17 m from CP); near CP2: @8 (124.2, -92.8; 16 m from CP), @18 (126.7, -92.8; 17 m from CP), @29 (119.4, -92.2; 15 m from CP), @67 (121.3, -94.4; 17 m from CP)
- Sector boxes (Sector markers, not rectangles): @13 (85.4, -89.3), @54 (-16.5, -58.7), @69 (158.1, -135.7)
- HQs by nearest anchor (start/checkpoint): start: @61 (-118.4, -48.3; 126 m); CP1: @10 (-15.0, -59.8; 39 m); CP2: @34 (112.0, -81.2; 9 m), @38 (86.5, -89.2; 35 m), @57 (85.9, -89.4; 36 m); final sector: @33 (169.9, -197.1; 63 m), @70 (157.9, -136.4; 1 m)
- TelemetryArea: @1 (13.8, 28.4), @4 (88.5, -87.2), @19 (171.5, -199.8), @46 (-10.2, -66.1), @55 (-120.3, -43.2); Insertion: @16 Cautious_OnSpot_v1 (-104.0, -54.9), @31 Cautious_OnSpot_v3 (55.6, -78.4), @35 Cautious_OnSpot_v1 (49.8, -80.6), @63 Cautious_OnSpot_v3 (-100.0, -67.0)

### Cairo Bazaar (MP_PLAZA)

- Layer assets: MP_Payload0, MP_Payload0_Schematic, Payload, Payload_Global, Payload_Global_Schematic, generated/AG_Payload_DynamicDD_Schematic_FA5B3FE3, generated/AG_Payload_DynamicDD_boxes_44F8C09F, payload/MeshVariationDb_Win32, payload_networkregistry_Win32, payload_templatedescriptorregistry
- factionOverrides: {}
- Payload start: @4 (-190.0, 70.0, -190.0)
- Route (greedy nearest-neighbour chain from the start, straight-line x/z legs; Euclidean-distance-from-start order gives the same order on every map): start -> CP1 @10 (-99.1, -181.9) [leg 91.3 m] -> CP2 @12 (-20.9, -181.2) [leg 78.2 m] -> CP3 @14 (33.8, -178.7) [leg 54.8 m]
- Route length start to last Checkpoint instance: 224.2 m. To the farthest Sector marker beyond it (@36, (90.0, -160.0), +59.2 m, assumed final destination, inference): 283.4 m.
- Mines: none
- Sector boxes (Sector markers, not rectangles): @17 (-140.0, -180.0), @36 (90.0, -160.0), @39 (-80.0, -190.0), @40 (10.0, -180.0)
- HQs by nearest anchor (start/checkpoint): start: @11 (-187.2, -189.5; 3 m); CP1: @26 (-127.7, -190.0; 30 m), @31 (-107.8, -198.0; 18 m), @35 (-77.2, -190.3; 23 m); CP2: @21 (-11.9, -191.3; 14 m); CP3: @24 (60.0, -180.0; 26 m), @32 (54.5, -187.0; 22 m); final sector: @23 (124.5, -188.3; 45 m)
- TelemetryArea: ; Insertion: @2 Cautious_Arrival (-181.2, -180.2), @3 Cautious_Arrival (-187.8, -176.0), @13 Cautious_Arrival (-71.8, -191.3), @41 Cautious_Arrival (-81.5, -200.7)

### Hagental Base (MP_SUBSURFACE)

- Layer assets: Payload, Payload0, Payload0_Schematic, Payload_Global, Payload_Global_Schematic, generated/AG_Payload_DynamicDD_Schematic_FA5B3FE3, generated/AG_Payload_DynamicDD_boxes_44F8C09F, payload/MeshVariationDb_Win32, payload_networkregistry_Win32, payload_templatedescriptorregistry
- factionOverrides: {}
- Payload start: @10 (-190.0, 70.0, -190.0)
- Route (greedy nearest-neighbour chain from the start, straight-line x/z legs; Euclidean-distance-from-start order gives the same order on every map): start -> CP1 @31 (-99.1, -181.9) [leg 91.3 m] -> CP2 @22 (-20.9, -181.2) [leg 78.2 m] -> CP3 @18 (33.8, -178.7) [leg 54.8 m]
- Route length start to last Checkpoint instance: 224.2 m. To the farthest Sector marker beyond it (@4, (90.0, -160.0), +59.2 m, assumed final destination, inference): 283.4 m.
- Mines: none
- Sector boxes (Sector markers, not rectangles): @4 (90.0, -160.0), @24 (-80.0, -190.0), @27 (-140.0, -180.0), @41 (10.0, -180.0)
- HQs by nearest anchor (start/checkpoint): start: @26 (-187.2, -189.5; 3 m); CP1: @13 (-77.2, -190.3; 23 m), @37 (-107.8, -198.0; 18 m), @39 (-127.7, -190.0; 30 m); CP2: @12 (-11.9, -191.3; 14 m); CP3: @34 (60.0, -180.0; 26 m), @36 (54.5, -187.0; 22 m); final sector: @35 (124.5, -188.3; 45 m)
- TelemetryArea: ; Insertion: @6 Cautious_Arrival (-71.8, -191.3), @15 Cautious_Arrival (-81.5, -200.7), @21 Cautious_Arrival (-187.8, -176.0), @29 Cautious_Arrival (-181.2, -180.2)

## 3. Cross-map table

Length is straight-line, start to last Checkpoint / to the assumed final sector.

| Map | Checkpoints | Route length (m) | Mines | HQs | Sector markers | Payload instances |
|---|---|---|---|---|---|---|
| Siege of Cairo | 2 | 247 / 346 | 7 | 8 | 4 | 1 |
| Wake Island | 3 | 224 / 283 | 0 | 8 | 4 | 1 |
| Blackwell Fields | 3 | 224 / 283 | 0 | 8 | 4 | 1 |
| Iberian Offensive | 2 | 141 / 204 | 0 | 6 | 3 | 1 |
| Liberation Peak | 2 | 190 / 238 | 8 | 6 | 4 | 1 |
| Contaminated | 3 | 224 / 283 | 0 | 8 | 4 | 1 |
| Manhattan Bridge | 2 | 227 / 273 | 8 | 6 | 3 | 1 |
| New Sobek City | 2 | 366 / 435 | 8 | 7 | 3 | 3 |
| Cairo Bazaar | 3 | 224 / 283 | 0 | 8 | 4 | 1 |
| Hagental Base | 3 | 224 / 283 | 0 | 8 | 4 | 1 |

Railway to Golmud: nothing (schematic asset only). Wake Island, Blackwell Fields, Contaminated, Cairo Bazaar and Hagental Base are one template. Only Siege of Cairo, Liberation Peak, Manhattan Bridge and New Sobek City have mines (7 or 8), in clusters of 3 to 4 within about 12 to 15 m of each checkpoint. Iberian Offensive has none.

## 4. Open questions

- Final checkpoint: no Checkpoint instance marks the end. Assumed the far Sector marker: Siege of Cairo @64, Iberian Offensive @2, Liberation Peak @31 (@25 is 3 m away), Manhattan Bridge @16, New Sobek City @69, template maps @5 (Blackwell Fields), @28 (Wake Island), @17 (Contaminated), @36 (Cairo Bazaar), @4 (Hagental Base).
- Route lengths are straight-line; real spline lengths are not in the data and will be longer.
- New Sobek City has three Payload instances: @28 (-230.3, 10.6), @51 (-242.8, 11.7; 13 m from @28) and @68 (-152.1, -167.9; about 180 m away, inside no shape). Only @28 was used as the start. HQ @38 and @57 sit 1 m apart, and HQ @70 sits 1 m from Sector @69.
- Siege of Cairo: HQ @72, @73, @74 are stacked within 0.3 m at (3.3, 25.2); HQ @16 is 41 m from them. It is the only map with swapped faction overrides (team1 Pax Armata, team2 Alliance/NATO). HQ @60 (-82.5, -68.5) sits in the start area with the insertions; no HQ lies near CP1 @38. Which side or phase each HQ serves is not stored.
- Manhattan Bridge: HQ @11 (-147.2, -473.6) is 90 m beyond the final sector. DeployCam @34 is at x -65.4, z 207.0, height 1800, about 400 m from the payload start and off the route (route runs to negative z).
- Liberation Peak: HQ @74 is 3 m from CP2 @63; HQ @78 (211.3, 233.8) is 101 m from the final sector.
- objective-table.json is empty, so Payload, Checkpoint, Mine and TelemetryArea show variant=None on all maps and the vehicle type cannot be named from this data.
- HQ counts (8 on four-sector maps, 6 on three-sector maps, 7 on New Sobek City) suggest two per sector (one per side), but nearest-anchor groups are uneven (template: 1/3/1/2/1 by start/CP1/CP2/CP3/final), so the per-side, per-phase split is not derivable spatially.
- Round time, radii, XP and per-distance score values are absent from MUT_Payload (section 1); rating thresholds (0.33/0.66 round 1, 30.0/30.0 round 2) are unexplained.
