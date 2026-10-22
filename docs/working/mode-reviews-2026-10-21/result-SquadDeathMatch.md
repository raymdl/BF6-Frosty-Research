# Squad Deathmatch (build 2.1.1.0)

Sources: SquadDeathMatch-tweakables.txt (MUT_SquadDM, 54 tweakables), SquadDeathMatch-maps.txt (19 maps), ui-text.txt, objective-table.json (AD_Objective_SquadDM), maps-tweakables.txt. Coordinates in metres, x/z plane. Sizes are bbox sizes; a polygon's bbox over-states its area.

## 1. Mode rules

### UI text confirms (ui-text.txt)
- Four squads: "Face off against three other squads in a close-quarters firefight".
- Win by reaching the kill target first, or by highest squad kill count when time expires.
- A "Hardcore Squad Deathmatch" string exists (a separate variant; no tweakable differs for it in this data).
- No UI text states any number (target, time, rounds, respawn). Everything below is a client default that a server playlist may override. Units are not stored (the round times are presumably minutes; not confirmed).

### Tweakables, MUT_SquadDM (value [min..max]; [0..0] means no range is stored)
Score and rounds
- SDM_iTargetScore = 50 [0..0] (kill target)
- SDM_iRounds = 3 [0..0]; SDM_iRound1TargetScore = 50, SDM_iRound2TargetScore = 30, SDM_iRound3TargetScore = 20
- SDM_fRoundTime = 15.0; SDM_fRound1Time = 7.0, SDM_fRound2Time = 5.0, SDM_fRound3Time = 3.0 (all [0..0])
- SDM_isSquadShootOut = false (the multi-round targets and times probably belong to this shoot-out variant; inference)
- SDM_fOvertimeDuration = 1.0; SDM_iBigLeadThreshold = 20; SDM_bAnnounceLeadChangeInUI = true
- SDM_fUrgencyTimeThreshold = 60.0 [0..120]; SDM_fUrgencyPercentageThreshold = 0.12 [0..1] (urgency music/UI near end)
- SDM_LayoutSelection = 0 [0..0] (all maps have only layout 0)
Squads, respawn and safe spawn
- SDM_bEnableSquadSpawning = true; SDM_fPlayerRespawnDelay = 0.0; SDM_iPlayerMaxSpawnCount = -1 (unlimited); SDM_bAllowQuickRespawnBeaconDeploy = true
- SDM_iSoldierManDownType = 1 [0..2]; SDM_bSoldierBleedoutOnSquadWipe = false
- SDM_bEnableSquadWipePenalty = false; SDM_SquadWipePenalty = 0
- Spawn scoring (score per candidate spawn point): enemy proximity 0..20 m = -20 (SDM_fEnemyProximityMin/MaxRadius, SDM_iEnemyProximityScore); friendly near 0..20 m = +5; friendly far 20.1..50 m = +1; previous death position 0..20 m = -10. All [0..0].
- Lobby: SDM_iLobbyPlayerCountStartTimer = 16; SDM_iLobbyPlayerCountToSpeedUpTimer = 16; SDM_fNoInteractivityTimeoutOverride = 60.0 [0..600]
Vehicles
- SDM_bAllowVehicles = true; SDM_bVehicleCanSpawnAgain = true
- Vehicle spawn cooldown SDM_fMinVehicleSpawnTimer = 120.0, SDM_fMaxVehicleSpawnTimer = 480.0; SDM_fVehicleSpawnRevealTimer = 60.0; SDM_bShowSpawningVehicleIWI = true
Out of bounds
- SDM_iOutOfBounds_TimeToReturn = 5 (seconds, inferred). Map-level MP_Dumbo_VehicleOOBtime = 10 [1..15] exists but Manhattan Bridge has no SDM vehicles.
Killstreaks and others
- SDM_bKillStreaksAllowed = true; SDM_iKillStreakStart = 5; SDM_iKillStreakDelta = 5
- Class recommendation flags (Assault, Support, Engineer, Recon Recommended) = false; SDM_iCommanderVoice = -1
XP: no XP tweakable exists in MUT_SquadDM, GME_Sim_SquadDM_Round or the shared GEM logic listed. Not found.

### Round logic (GME_Sim_SquadDM_Round, named variables only)
ActivityStateMachine, WinningTeam, PlayersToEliminate, MI_Sim_GameMode, IsEndOfRound, Players, LastTeam. PlayersToEliminate and LastTeam suggest a last-squad-standing / elimination path (probably the shoot-out variant). GME_Pres_SquadDM_Round holds only MI_Pres_GameMode; GM_SquadDM_LaunchFunction has ActivityParameters and LaunchParameters (both null). No per-squad count tweakable exists; "four squads" is confirmed by the UI and by every map having exactly 4 Insertion instances.

### AD_Objective_SquadDM (objective-table.json)
Modules defined: Sector, SafeSpawnArea, Insertion (19 variants, 0..18), Insertion_Event (Airstrike, JetStraight), VehicleSpawner_Forward, VehicleSpawner (24 variants), StationarySpawner (0 HMG, 1 AntiTank, 2 AntiAircraft), VehicleResupplyStation (default, Air), Reinforcement, Reinforcement_Intro, B1Bomber_TrailerSpawner, ReinforcementIntro_CinematicVehicle, Battle_Pickup. VehicleSpawner default (no key) = IFV; key 1 = IFV. Only IFV pads and AntiTank emplacements are placed in any map.

## 2. Maps

All 19 maps use one gameplay layer (MP_SquadDM0 or SquadDM0), no layout variants. Each has exactly 4 Insertions (one per squad). Unplaced Sector/SafeSpawnArea markers sit at the default position [-308.6, y, 59.9] (y 64 to 92.8). The play area is the largest MP_SquadDM0-layer polygon (inference; there is no CombatArea module, only SpecialCombatArea on 3 maps). Instance lines list positions as [x,z] for Insertions and [x,y,z] otherwise.

### Siege of Cairo (MP_ABBASID)

- Layer assets: SquadDM_Global, SquadDM_Global_Schematic, MP_SquadDM0, MP_SquadDM0_Schematic, SquadDM
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY48@30 [-263,-83,-94,130], size 169x213 m
- Other boxes/polygons: BOX@35 (MP_SquadDM0) [-234,23,-143,82] 91x59; BOX@46 (MP_SquadDM0) [-105,-86,-51,124] 54x210; BOX@63 (MP_SquadDM0) [-234,-86,-115,23] 119x109; POLY5@60 (MP_SquadDM0) [-143,-86,-105,82] 38x168; POLY6@69 (MP_SquadDM0) [-258,-24,-105,125] 153x149
- Insertions (4): @14 Cautious_OnSpot_v1 [-100.2,65.5] polys[30]; @47 Cautious_Arrival [-201,112.5] polys[30, 69]; @88 Cautious_LongDistance [-135.5,-52.7] polys[30]; @98 Cautious_OnSpot_v1 [-235.7,10.5] polys[30, 69]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: SafeSpawnArea@11 [-157.2,68.5,60] polys[30]; Sector@68 [-158.7,66.7,56.7] polys[30]
- SpecialCombatArea: @95 [-159.5,69,57.3] polys[30] boxes[35]
- TelemetryArea: 5
- Notes: Sector, SafeSpawnArea and SpecialCombatArea (@95, purpose not stated in data) all sit in BOX@35 (91x59 m) on the west side, inside the main polygon. Insertions: one long-distance, one arrival, two on-spot.

### Empire State (MP_AFTERMATH)

- Layer assets: MP_SquadDM0, MP_SquadDM0_Schematic, SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, SquadDeathMatch_VFX, SquadDeathMatch_VFX_Schematic, generated/DD_MP_SquadDM0_Schematics, generated/DD_MP_SquadDM0_Volumes, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch/staticmodelgroup.physics, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY36@30 [-615,-134,-507,42], size 108x176 m
- Insertions (4): @3 Chaotic_LongDistance [-606.8,-65.7] polys[30]; @18 Chaotic_Arrival_v1 [-602,6.7] polys[30]; @20 Cautious_OnSpot_v1 [-521.1,-2.9] polys[30]; @29 Cautious_OnSpot_v1 [-528.5,-79.8] polys[30]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: SafeSpawnArea@23 [-604.1,54.7,-57.1] polys[30]; Sector@54 [-604.1,54.7,-57.1] polys[30]
- TelemetryArea: 4
- Notes: Sector and SafeSpawnArea share an identical position. TelemetryArea @7 [-613.8,-54.7] lies on the polygon edge but is in no polygon. TelemetryArea @53 is at y=104.6 (about 50 m above the rest, likely a rooftop level). Insertions mix Chaotic (LongDistance, Arrival_v1) and Cautious on-spot v1 (x2).

### Wake Island (MP_ATOLL)

- Layer assets: SquadDeathMatch, SquadDeathMatch_Global_Schematic, generated/AG_SquadDeathMatch_DynamicDD_Schematic_A52E6B34, generated/AG_SquadDeathMatch_DynamicDD_boxes_12B486B1, MP_SquadDM0, MP_SquadDM0_Schematic, SquadDeathMatch_Global, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY10@2 [296,-166,480,18], size 184x184 m
- Other boxes/polygons: BOX@1 (SquadDeathMatch_Global) [355,-42,455,45] 100x87; BOX@3 (SquadDeathMatch_Global) [436,-75,507,45] 71x120; BOX@4 (SquadDeathMatch_Global) [222,-126,307,-30] 85x96; BOX@5 (SquadDeathMatch_Global) [228,-63,325,37] 97x100
- Insertions (4): @15 Cautious_OnSpot_v1 [475.5,2.1] polys[]; @18 Cautious_OnSpot_v1 [242.8,-79.5] polys[]; @22 Cautious_OnSpot_v3 [252.3,-23] polys[]; @29 Cautious_Arrival [425.4,20] polys[]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: SafeSpawnArea@1 [383,100.2,-54.2] polys[2]; Sector@26 [366.7,100.1,-65] polys[2]
- TelemetryArea: 5
- Notes: Play area is ambiguous. The only polygon (POLY10@2, 184x184) holds the Sector, SafeSpawnArea and one TelemetryArea, but all four Insertions and four TelemetryAreas lie outside it, in four boxes of the Global layer (BOX@1/3/4/5, union x 222..507, z -126..45 = 285x171 m). The boxes look like the real squad zones; the polygon looks like the central zone. All coordinates are around y=100.

### Blackwell Fields (MP_BADLANDS)

- Layer assets: KOTH_SQDM_Cover, MP_SquadDM0, MP_SquadDM0_Schematic, SQDM, SQDM_Global_Schematic, generated/DD_MP_SquadDM0_Schematics, generated/DD_MP_SquadDM0_Volumes, sqdm/MeshVariationDb_Win32, sqdm_networkregistry_Win32, sqdm_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY16@22 [201,-177,331,-6], size 130x171 m
- Insertions (4): @18 Cautious_Arrival [315.8,-145.7] polys[22]; @27 Cautious_OnSpot_v3 [212.3,-52.2] polys[22]; @29 Cautious_OnSpot_v5_NOT_FOR_REVEAL [207.7,-157.6] polys[22]; @31 Cautious_Arrival_Corner [301.1,-16.8] polys[22]
- Vehicle pads (3): @2 IFV [272.1,75.4,-87.1] polys[22]; @4 IFV [269.6,77.2,-152.1] polys[22]; @25 IFV [247.5,75.4,-27.7] polys[22]
- Stationary emplacements (0): none
- Safe spawn / Sector: Sector@1 [-308.6,78.1,59.9] polys[]; SafeSpawnArea@7 [253.2,75.4,-80.1] polys[22]
- TelemetryArea: 0
- Notes: Sector is at the unplaced default position [-308.6,78.1,59.9] and is outside the play area. Three IFV pads all along the east edge (x 247..272). The layer set uses KOTH_SQDM_Cover (a King of the Hill cover asset reused) and SQDM-named assets. Insertion @29 is variant v5 "NOT_FOR_REVEAL".

### Iberian Offensive (MP_BATTERY)

- Layer assets: MP_SquadDM0, MP_SquadDM0_Schematic, SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, generated/DD_MP_SquadDM0_Volumes_38597F12, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY79@20 [651,57,808,230], size 157x173 m
- Other boxes/polygons: POLY7@1 (SquadDeathMatch_Global) [651,136,764,232] 113x96; POLY7@2 (SquadDeathMatch_Global) [736,108,811,209] 75x101; POLY9@3 (SquadDeathMatch_Global) [654,55,769,156] 115x101
- Insertions (4): @8 Chaotic_Arrival_v1 [669.6,128.9] polys[20, 3]; @12 Chaotic_Arrival_v1 [791,166.1] polys[20, 2]; @14 Chaotic_Arrival_v1 [726.2,74.3] polys[20, 3]; @19 Chaotic_Arrival_v1 [691.2,219.9] polys[20, 1]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: Sector@16 [715.9,74.7,150.5] polys[20, 1, 3]; SafeSpawnArea@32 [715.9,74.7,150.5] polys[20, 1, 3]
- TelemetryArea: 3
- Notes: All four Insertions use Chaotic_Arrival_v1. Three Global sub-polygons (POLY@1, @2, @3) overlap the main polygon and partition it into three zones; Sector and SafeSpawnArea (same position) fall in zones 1 and 3 and the main polygon.

### Liberation Peak (MP_CAPSTONE)

- Layer assets: SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, SquadDeathMatch_Telemetry, MP_SquadDM0, MP_SquadDM0_Schematic, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY51@91 [-24,0,232,172], size 256x172 m
- Other boxes/polygons: POLY9@1 (SquadDeathMatch_Telemetry) [-36,-5,128,137] 164x142; POLY8@2 (SquadDeathMatch_Telemetry) [104,-2,240,135] 136x137; POLY8@3 (SquadDeathMatch_Telemetry) [64,73,197,186] 133x113
- Insertions (4): @2 Cautious_OnSpot_v3 [92.2,139.8] polys[3, 91]; @5 Cautious_OnSpot_v1 [20.5,62.5] polys[1, 91]; @25 Cautious_OnSpot_v1 [175.7,105.3] polys[2, 91]; @31 Cautious_OnSpot_v3 [144.7,28.5] polys[2, 91]
- Vehicle pads (5): @11 IFV [55.2,139.5,110.3] polys[1, 91]; @12 IFV [166.9,129.8,70.3] polys[2, 91]; @43 IFV [32.9,133.9,70.3] polys[1, 91]; @47 IFV [94,133.4,59.8] polys[1, 91]; @89 IFV [138.3,134,91.9] polys[3, 91]
- Stationary emplacements (0): none
- Safe spawn / Sector: Sector@19 [-308.6,78.1,59.9] polys[]; SafeSpawnArea@21 [98,136.9,74] polys[1, 91]
- TelemetryArea: 3
- Notes: Five IFV pads, the second most after Cairo Bazaar (tied with Eastwood and Mirak Valley). Sector is at the unplaced default position (outside the play area). Telemetry layer holds three overlapping zone polygons inside the main polygon.

### Contaminated (MP_CONTAMINATED)

- Layer assets: SquadDM0, SquadDM0_Schematic, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, SquadDeathMatch_Telemetry, SquadDeathMatch, generated/AG_SquadDeathMatch_DynamicDD_Schematic_A52E6B34, generated/AG_SquadDeathMatch_DynamicDD_boxes_12B486B1, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch/staticmodelgroup.physics, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY24@39 [75,13,236,166], size 161x153 m
- Other boxes/polygons: POLY9@1 (SquadDeathMatch_Telemetry) [75,75,216,166] 141x91; POLY17@2 (SquadDeathMatch_Telemetry) [82,13,236,131] 154x118
- Insertions (4): @3 Cautious_OnSpot_v3 [79,114.8] polys[39, 1]; @7 Cautious_OnSpot_v1 [141.9,47.3] polys[39, 2]; @17 Cautious_OnSpot_v1 [192.2,142] polys[39, 1]; @33 Cautious_OnSpot_v3 [205.1,59.9] polys[39, 2]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: SafeSpawnArea@10 [269.3,298,178.2] polys[]; Sector@51 [271.3,298,175.4] polys[]
- TelemetryArea: 2
- Notes: SafeSpawnArea (@10), Sector (@51) and TelemetryAreas @18, @56 are at x 263..338, z 175..241, y about 297, outside the main polygon (x 75..236, z 13..166) and in no polygon; the Insertions are at y 308..340. Raises the question of whether these are leftover from another layout or sit on a different vertical level.

### Area 51 (MP_DRYLAKE)

- Layer assets: SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, MP_SquadDM0, MP_SquadDM0_Schematic, generated/AG_SquadDeathMatch_DynamicDD_Schematic_A52E6B34, generated/AG_SquadDeathMatch_DynamicDD_boxes_12B486B1, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): none (no polygon/box), size - m
- Insertions (4): @1 Cautious_Arrival [121.7,0.2] polys[]; @2 Cautious_Arrival [47.9,64.8] polys[]; @3 Cautious_Arrival [18.5,-1.3] polys[]; @5 Cautious_Arrival [48.9,-78] polys[]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: SafeSpawnArea@4 [-308.6,64,59.9] polys[]; Sector@6 [-308.6,64,59.9] polys[]
- TelemetryArea: 0
- Notes: The layer has only 6 instances and no polygon, box, TelemetryArea or combat area. Sector and SafeSpawnArea are at the unplaced default x/z (y=64). The four Insertions all have key=-1 (default Cautious_Arrival) and all are at y=64.0, so the play area cannot be bounded; the instance extent is 103x143 m. Looks unfinished or placeholder; may rely on a combat area from another asset.

### Manhattan Bridge (MP_DUMBO)

- Layer assets: MP_SquadDM0, MP_SquadDM0_Schematic, SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, SquadDeathMatch_VFX, SquadDeathMatch_VFX_Schematic, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY54@8 [-117,-452,58,-233], size 175x219 m
- Other boxes/polygons: BOX@21 (MP_SquadDM0) [-135,-463,77,-221] 212x242
- Insertions (4): @23 Cautious_OnSpot_v1 [38.7,-407.4] polys[8]; @26 Cautious_OnSpot_v1 [2.6,-250] polys[8]; @27 Cautious_OnSpot_v1 [-64.9,-294.8] polys[8]; @49 Cautious_OnSpot_v1 [-70.3,-434] polys[8]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: Sector@28 [-41.1,58,-345.2] polys[8]; SafeSpawnArea@45 [-24.8,54.5,-353.7] polys[8]
- SpecialCombatArea: @46 [-41.1,62.4,-344] polys[8] boxes[21]
- TelemetryArea: 1
- Notes: SpecialCombatArea @46 sits next to Sector and SafeSpawnArea inside BOX@21. All four Insertions are on-spot v1. The map has a tweakable MP_Dumbo_VehicleOOBtime = 10 [1..15] but no SDM vehicles.

### Eastwood (MP_EASTWOOD)

- Layer assets: MP_SquadDM0, MP_SquadDM0_Schematic, SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, generated/DD_MP_SquadDM0_Schematics, generated/DD_MP_SquadDM0_Volumes, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch/staticmodelgroup.physics, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY40@1 [-365,-65,-74,148], size 291x213 m
- Insertions (4): @6 Cautious_Arrival [-89,37.9] polys[1]; @8 Cautious_OnSpot_v3 [-165.6,126.6] polys[1]; @17 Cautious_Arrival [-345.9,46.4] polys[1]; @18 Cautious_Arrival_Corner [-202,-49.5] polys[1]
- Vehicle pads (5): @2 IFV [-169,231.7,-20.6] polys[1]; @10 IFV [-303.4,229.7,-22.2] polys[1]; @22 IFV [-251,230.6,117.4] polys[1]; @30 IFV [-201.6,232.6,44.6] polys[1]; @31 IFV [-107.8,234.9,65.3] polys[1]
- Stationary emplacements (0): none
- Safe spawn / Sector: SafeSpawnArea@20 [-170,231.9,-10.5] polys[1]; Sector@29 [-170,231.9,-10.5] polys[1]
- TelemetryArea: 0
- Notes: Five IFV pads spread over the whole polygon (z -22..117). Sector and SafeSpawnArea share position [-170,-10.5]. Insertions: @6 and @17 Cautious_Arrival, @18 Arrival_Corner, @8 on-spot v3.

### Operation Firestorm (MP_FIRESTORM)

- Layer assets: SquadDeathMatch_Global, MP_SquadDM0, MP_SquadDM0_Schematic, SquadDeathMatch, SquadDeathMatch_Global_Schematic, SquadDeathMatch_Telemetry, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY65@25 [-332,-167,-44,-4], size 288x163 m
- Other boxes/polygons: BOX@1 (SquadDeathMatch_Telemetry) [-172,-164,-49,-14] 123x150; BOX@2 (SquadDeathMatch_Telemetry) [-332,-146,-249,-14] 83x132; BOX@3 (SquadDeathMatch_Telemetry) [-249,-163,-172,-14] 77x149
- Insertions (4): @5 Chaotic_Arrival_v1 [-310.2,-133.3] polys[25]; @16 Chaotic_Arrival_v3 [-281.7,-28.5] polys[25]; @26 Chaotic_LongDistance [-68.3,-158.8] polys[25]; @46 Chaotic_Arrival_v1 [-64.6,-34.5] polys[25]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: Sector@19 [-308.6,78.1,59.9] polys[]; SafeSpawnArea@34 [-308.6,78.1,59.9] polys[]
- TelemetryArea: 3
- Notes: Sector and SafeSpawnArea are at the unplaced default position, outside the play area. Three Telemetry boxes tile the play area in x (-332..-49, z -164..-14, union 283x150). Insertions are Chaotic (Arrival_v1 x2, Arrival_v3, LongDistance).

### Railway to Golmud (MP_GOLMUDRAILWAY)

- Layer assets: SquadDeathMatch, SquadDeathMatch_Global_Schematic, generated/AG_SquadDeathMatch_DynamicDD_Schematic_A52E6B34, generated/AG_SquadDeathMatch_DynamicDD_boxes_12B486B1, MP_SquadDM0, MP_SquadDM0_Schematic, SquadDeathMatch_Global, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch/staticmodelgroup.physics, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY58@8 [-314,697,34,971], size 348x274 m
- Other boxes/polygons: POLY6@1 (SquadDeathMatch_Global) [-314,822,-132,967] 182x145; POLY10@2 (SquadDeathMatch_Global) [-314,709,-132,823] 182x114; POLY6@3 (SquadDeathMatch_Global) [-132,822,33,967] 165x145; POLY14@4 (SquadDeathMatch_Global) [-143,699,33,823] 176x124
- Insertions (4): @15 Cautious_OnSpot_v3 [-277.1,716.6] polys[8, 2]; @26 Cautious_OnSpot_v4_NOT_FOR_REVEAL [-49.3,720.6] polys[8, 4]; @31 Cautious_OnSpot_v2 [-239.3,922] polys[8, 1]; @38 Cautious_OnSpot_v1 [-53.1,924.8] polys[8, 3]
- Vehicle pads (4): @13 IFV [-136.4,728.8,730.2] polys[8, 4]; @14 IFV [-66.3,737.8,850.8] polys[8, 3]; @28 IFV [-123.8,751.4,963] polys[8, 3]; @41 IFV [-281.2,732.6,793] polys[8, 2]
- Stationary emplacements (0): none
- Safe spawn / Sector: SafeSpawnArea@1 [-140.6,738.2,875.5] polys[8, 1]; Sector@11 [-308.6,78.1,59.9] polys[]; SafeSpawnArea@24 [-137.5,740.2,879.8] polys[8, 1]
- TelemetryArea: 4
- Notes: Largest play area. Four IFV pad instances have key=-1, so the class comes from the objective definition default (IFV), not from an explicit selector. Two SafeSpawnAreas, 5.3 m apart (@1 and @24), the only map where two sit together. Sector is at the unplaced default. Four Global sub-polygons tile the main polygon. Insertion @26 is v4 "NOT_FOR_REVEAL". The Golmud moving-train tweakables exist only for Escalation and Conquest.

### Tsuru Reef (MP_ISOLATED)

- Layer assets: SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, MP_SquadDM0, MP_SquadDM0_Schematic, generated/AG_SquadDeathMatch_DynamicDD_Schematic_A52E6B34, generated/AG_SquadDeathMatch_DynamicDD_boxes_12B486B1, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): union of 3 Global polys [-718,-294,-494,-66], size 224x228 m
- Other boxes/polygons: POLY8@1 (SquadDeathMatch_Global) [-718,-257,-601,-86] 117x171; POLY7@2 (SquadDeathMatch_Global) [-674,-294,-547,-153] 127x141; POLY10@3 (SquadDeathMatch_Global) [-652,-247,-494,-66] 158x181
- Insertions (4): @9 Cautious_OnSpot_v1 [-593.5,-236.6] polys[2]; @47 Cautious_OnSpot_v3 [-528,-182.6] polys[3]; @69 Cautious_OnSpot_v3 [-672.3,-189.5] polys[1]; @71 Cautious_OnSpot_v1 [-589,-111.7] polys[3]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: SafeSpawnArea@45 [-602,105.4,-164.8] polys[2]; Sector@61 [-598.5,78.1,-590.2] polys[]
- TelemetryArea: 0
- Notes: No MP_SquadDM0 polygon: three overlapping Global polygons (117x171, 127x141, 158x181); the union is 224x228 m. Sector is at [-598.5,78.1,-590.2], about 330 m south of the play area (unplaced). SafeSpawnArea lies only in POLY@2. No TelemetryArea.

### Saints Quarter (MP_LIMESTONE)

- Layer assets: MP_SquadDM0, MP_SquadDM0_Schematic, SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, generated/DD_MP_SquadDM0_Schematics, generated/DD_MP_SquadDM0_Volumes, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): none (no polygon/box), size - m
- Insertions (4): @12 Cautious_OnSpot_v1 [280.8,115.4] polys[]; @18 Cautious_OnSpot_v2 [318.3,67.5] polys[]; @23 Cautious_OnSpot_v2 [368.3,82] polys[]; @43 Cautious_OnSpot_v1 [379.5,129.8] polys[]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: Sector@19 [334.5,80.8,101.2] polys[]; SafeSpawnArea@47 [334.6,80.7,101.2] polys[]
- TelemetryArea: 4
- Notes: No polygon, box or combat area. Sector and SafeSpawnArea share a position at the middle of the instance extent (99x67 m), so the extent is the best estimate of the play area and the smallest of all maps. Two Insertions are on-spot v2, two are v1.

### New Sobek City (MP_OUTSKIRTS)

- Layer assets: SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, generated/DD_MP_SquadDM0_Schematics, generated/DD_MP_SquadDM0_Volumes, MP_SquadDM0, MP_SquadDM0_Schematic, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY69@41 [-100,-144,84,-10], size 184x134 m
- Other boxes/polygons: BOX@2 (SquadDeathMatch_Global) [-79,-49,23,4] 102x53; BOX@3 (SquadDeathMatch_Global) [-79,-109,23,-47] 102x62; POLY6@1 (SquadDeathMatch_Global) [-114,-155,-79,4] 35x159; POLY5@4 (SquadDeathMatch_Global) [-79,-159,22,-109] 101x50; POLY6@5 (SquadDeathMatch_Global) [22,-159,87,2] 65x161
- Insertions (4): @6 Cautious_OnSpot_v1 [47.7,-32.4] polys[5, 41]; @19 Cautious_OnSpot_v3 [-65.2,-108.9] polys[41]; @30 Cautious_OnSpot_v1 [-61.9,-36.7] polys[41]; @38 Cautious_Arrival [40.2,-115.1] polys[5, 41]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: SafeSpawnArea@11 [-308.6,92.8,59.9] polys[]; Sector@15 [-6.2,103.6,-80.6] polys[41]; Sector@32 [649.4,86.1,1112.9] polys[]; SafeSpawnArea@46 [-99.4,93.4,-102.6] polys[1]
- TelemetryArea: 10
- Notes: Two Sectors and two SafeSpawnAreas, the only map with doubles: Sector @15 and SafeSpawnArea @46 are real, Sector @32 [649.4,86.1,1112.9] and SafeSpawnArea @11 [-308.6,92.8,59.9] are unplaced defaults. SafeSpawnArea @46 [-99.4,-102.6] is inside Global POLY@1 but not in the main polygon (its western edge). Ten TelemetryAreas, the most.

### Vegas Strip (MP_PARADISE)

- Layer assets: SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, MP_SquadDM0, MP_SquadDM0_Schematic, generated/AG_SquadDeathMatch_DynamicDD_Schematic_A52E6B34, generated/AG_SquadDeathMatch_DynamicDD_boxes_12B486B1, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY46@28 [-165,150,40,356], size 205x206 m
- Insertions (4): @4 Cautious_OnSpot_v1 [26.4,226.2] polys[28]; @9 Cautious_OnSpot_v1 [-1.2,344.4] polys[28]; @11 Cautious_OnSpot_v1 [-136.9,336.6] polys[28]; @22 Cautious_OnSpot_v1 [-97.3,187.4] polys[28]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: Sector@7 [-94.2,56,-67.7] polys[]; SafeSpawnArea@25 [-30.8,51.3,264] polys[28]
- TelemetryArea: 0
- Notes: Sector [-94.2,-67.7] is about 220 m south of the play area (z 150..356); SafeSpawnArea is inside. All four Insertions are on-spot v1. No TelemetryArea.

### Cairo Bazaar (MP_PLAZA)

- Layer assets: SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, MP_SquadDM0, MP_SquadDM0_Schematic, generated/AG_SquadDeathMatch_DynamicDD_Schematic_A52E6B34, generated/AG_SquadDeathMatch_DynamicDD_boxes_12B486B1, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY42@34 [11,103,182,266], size 171x163 m
- Insertions (4): @1 Cautious_OnSpot_v1 [119.7,119.9] polys[34]; @9 Cautious_OnSpot_v3 [21.4,223] polys[34]; @16 Cautious_Arrival [145.3,231.5] polys[34]; @28 Cautious_OnSpot_v4_NOT_FOR_REVEAL [21.1,119.9] polys[34]
- Vehicle pads (6): @4 IFV [98.8,64.1,123.8] polys[34]; @13 IFV [84,64.2,186.4] polys[34]; @14 IFV [62,64.4,168.9] polys[34]; @15 IFV [113.9,64.3,188.1] polys[34]; @21 IFV [22,64.2,194.3] polys[34]; @30 IFV [132.7,64.6,230.5] polys[34]
- Stationary emplacements (4): @20 AntiTank [119.8,65.2,109.5]; @22 AntiTank [116.1,64.4,169.6]; @29 AntiTank [20.5,64.2,186.9]; @33 AntiTank [119.6,64.4,236.9]
- Safe spawn / Sector: Sector@31 [-308.6,78.1,59.9] polys[]; SafeSpawnArea@36 [-308.6,78.1,59.9] polys[]
- SpecialCombatArea: @3 [20,67.2,93.2] polys[] boxes[]
- TelemetryArea: 0
- Notes: Six IFV pads and four AntiTank emplacements. Each emplacement has a pad within 25 m: @29 to @21 (7.6 m), @33 to @30 (14.6 m), @22 to @15 (18.6 m), @20 to @4 (25.4 m). Sector and SafeSpawnArea are unplaced defaults. SpecialCombatArea @3 [20,67.2,93.2] is outside the polygon, about 10 m south of its edge. Insertion @28 is v4 "NOT_FOR_REVEAL". No TelemetryArea.

### Hagental Base (MP_SUBSURFACE)

- Layer assets: SquadDM0, SquadDM0_Schematic, SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, generated/AG_SquadDeathMatch_DynamicDD_Schematic_A52E6B34, generated/AG_SquadDeathMatch_DynamicDD_boxes_12B486B1, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY21@5 [-142,-102,148,83], size 290x185 m
- Insertions (4): @12 Cautious_OnSpot_v1 [-53.2,72.5] polys[5]; @40 Cautious_OnSpot_v1 [66.5,-79.1] polys[5]; @41 Cautious_OnSpot_v1 [114.8,-12.9] polys[5]; @76 Cautious_OnSpot_v1 [-102.7,13.9] polys[5]
- Vehicle pads (0): none
- Stationary emplacements (0): none
- Safe spawn / Sector: Sector@21 [7.5,78.1,-6.9] polys[5]; SafeSpawnArea@36 [6.6,78.1,-11.5] polys[5]
- TelemetryArea: 0
- Notes: Simple layout. Sector and SafeSpawnArea in the polygon; Sector at y=78.1 (a default-looking height) while Insertions are at y 64..66. All Insertions on-spot v1. No TelemetryArea.

### Mirak Valley (MP_TUNGSTEN)

- Layer assets: MP_SquadDM0, MP_SquadDM0_Schematic, SquadDeathMatch, SquadDeathMatch_Global, SquadDeathMatch_Global_Schematic, SquadDeathMatch_Telemetry, generated/DD_MP_SquadDM0_Schematics, generated/DD_MP_SquadDM0_Volumes, squaddeathmatch/MeshVariationDb_Win32, squaddeathmatch/staticmodelgroup.physics, squaddeathmatch_networkregistry_Win32, squaddeathmatch_templatedescriptorregistry
- Layout variants: one gameplay layer only (MP_SquadDM0 / SquadDM0), no _Small/_Large or numbered alternatives; matches SDM_LayoutSelection = 0.
- Play area (main polygon, inferred combat area): POLY25@31 [176,-550,409,-308], size 233x242 m
- Other boxes/polygons: POLY9@1 (SquadDeathMatch_Telemetry) [177,-465,327,-415] 150x50; POLY10@2 (SquadDeathMatch_Telemetry) [200,-437,358,-313] 158x124; POLY12@3 (SquadDeathMatch_Telemetry) [283,-525,390,-442] 107x83; POLY13@4 (SquadDeathMatch_Telemetry) [326,-468,409,-398] 83x70; POLY7@5 (SquadDeathMatch_Telemetry) [177,-548,283,-457] 106x91
- Insertions (4): @17 Cautious_OnSpot_v1 [279.4,-326.2] polys[31, 2]; @18 Cautious_OnSpot_v2 [327.4,-516.3] polys[31, 3]; @22 Cautious_OnSpot_v3 [197.4,-480.1] polys[31, 5]; @27 Cautious_OnSpot_v2 [373.2,-435.9] polys[31, 4]
- Vehicle pads (5): @12 IFV [305.3,83,-363.7] polys[31, 2]; @14 IFV [231,88.5,-391.5] polys[31, 2]; @21 IFV [339.4,83,-406.2] polys[31, 2]; @30 IFV [221.3,86.6,-443.5] polys[31, 1]; @37 IFV [317,83.4,-472.5] polys[31, 3]
- Stationary emplacements (0): none
- Safe spawn / Sector: SafeSpawnArea@13 [273.2,91.2,-393.9] polys[31, 2]; Sector@19 [279.6,86.5,-424.9] polys[31, 1]
- TelemetryArea: 5
- Notes: Five IFV pads from key=-1 (default IFV). Five Telemetry polygons subdivide the play area. Two Insertions are on-spot v2, one v1, one v3. Sector and SafeSpawnArea are inside.

## 3. Cross-map table

| Map | Layouts | Play area (m) | Insertions | Vehicles | Emplacements |
|---|---|---|---|---|---|
| Siege of Cairo (MP_ABBASID) | 1 | 169x213 | 4 | none | none |
| Empire State (MP_AFTERMATH) | 1 | 108x176 | 4 | none | none |
| Wake Island (MP_ATOLL) | 1 | 184x184 | 4 | none | none |
| Blackwell Fields (MP_BADLANDS) | 1 | 130x171 | 4 | 3 IFV | none |
| Iberian Offensive (MP_BATTERY) | 1 | 157x173 | 4 | none | none |
| Liberation Peak (MP_CAPSTONE) | 1 | 256x172 | 4 | 5 IFV | none |
| Contaminated (MP_CONTAMINATED) | 1 | 161x153 | 4 | none | none |
| Area 51 (MP_DRYLAKE) | 1 | - | 4 | none | none |
| Manhattan Bridge (MP_DUMBO) | 1 | 175x219 | 4 | none | none |
| Eastwood (MP_EASTWOOD) | 1 | 291x213 | 4 | 5 IFV | none |
| Operation Firestorm (MP_FIRESTORM) | 1 | 288x163 | 4 | none | none |
| Railway to Golmud (MP_GOLMUDRAILWAY) | 1 | 348x274 | 4 | 4 IFV | none |
| Tsuru Reef (MP_ISOLATED) | 1 | 224x228 | 4 | none | none |
| Saints Quarter (MP_LIMESTONE) | 1 | - | 4 | none | none |
| New Sobek City (MP_OUTSKIRTS) | 1 | 184x134 | 4 | none | none |
| Vegas Strip (MP_PARADISE) | 1 | 205x206 | 4 | none | none |
| Cairo Bazaar (MP_PLAZA) | 1 | 171x163 | 4 | 6 IFV | 4 AntiTank |
| Hagental Base (MP_SUBSURFACE) | 1 | 290x185 | 4 | none | none |
| Mirak Valley (MP_TUNGSTEN) | 1 | 233x242 | 4 | 5 IFV | none |

Vehicle pads exist on 6 maps (Blackwell Fields 3, Liberation Peak 5, Eastwood 5, Railway to Golmud 4, Cairo Bazaar 6, Mirak Valley 5; 28 in total), all IFV (Golmud and Mirak Valley by default key). No tank, helicopter, boat or plane pad is placed anywhere. Emplacements exist only on Cairo Bazaar (4 AntiTank). Area 51 and Saints Quarter have no polygon (instance extent 103x143 m and 99x67 m). Wake Island's play area is ambiguous (see map notes).

## 4. Open questions

1. IFV pads: the in-game vehicle name per faction is not in this data (class only). With key=-1 on Golmud @13/@14/@28/@41 and Mirak Valley @12/@14/@21/@30/@37 the class is the default; confirm in game.
2. Sector markers at default position: Blackwell Fields @1, Liberation Peak @19, Operation Firestorm @19, Golmud @11, Cairo Bazaar @31, Area 51 @6, New Sobek City @32, Tsuru Reef @61 (and SafeSpawnArea Firestorm @34, Plaza @36, Area 51 @4, Outskirts @11). Do they matter if unplaced?
3. Contaminated: SafeSpawnArea @10, Sector @51 and TelemetryAreas @18, @56 are outside the main polygon (x 263..338) at y about 297.
4. Wake Island: polygon POLY10@2 versus boxes @1/3/4/5 as play area; Insertions @15, @18, @22, @29 lie outside the polygon.
5. Area 51 (6 instances, no area) and Saints Quarter (no area): which combat area bounds play?
6. Paradise Sector @7 is 220 m from the play area; Isolated Sector @61 is 330 m away.
7. SpecialCombatArea purpose: Siege of Cairo @95, Manhattan Bridge @46, Cairo Bazaar @3 (outside polygon).
8. Insertion variants "NOT_FOR_REVEAL": Blackwell Fields @29 (v5), Golmud @26 (v4), Cairo Bazaar @28 (v4).
9. Round times and target (7/5/3 and 50/30/20 versus 15 and 50): which set the live mode uses (depends on SDM_isSquadShootOut); time units not stored.
10. New Sobek City SafeSpawnArea @46 sits outside the main polygon; Golmud has two SafeSpawnAreas (@1, @24) 5.3 m apart.
