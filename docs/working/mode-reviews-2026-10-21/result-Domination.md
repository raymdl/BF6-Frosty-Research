# Domination analysis, build 2.1.1.0

Sources: Domination-maps.txt, Domination-tweakables.txt, ui-text.txt, objective-table.json, maps-tweakables.txt in the Domination folder. Numbers computed by script (an_dom.py, an2.py, gen_dom.py in modes-work).

## 1. Mode rules

### MUT_Domination (client defaults; [0..0] means no range recorded)
| Tweakable | Value | Range | UI text |
|---|---|---|---|
| DOM_fScoreTarget | 200.0 | 1..1000 | "First team to reach the points target wins" (the value itself is not stated) |
| DOM_fRoundtime | 15.0 (unit not stored; minutes inferred) | none | "...or by having the most points when the time expires" confirms a time limit |
| DOM_fScoreDelay | 4.0 | 0..1000 | none (seconds between score ticks, inferred) |
| DOM_fScoreDelays | [0.0, 3.5, 2.5, 1.5] | none | "Controlling each objective gradually earns you a set amount of points" (inferred: tick interval by objectives held 0/1/2/3, faster with more) |
| DOM_fCaptureTime | 10.0 | none | none |
| DOM_fNeutralizationTime | 10.0 | none | none |
| DOM_f[]CaptureAndNeutralisationTimeMultipliers | [0.0, 1.0, 1.25, 1.5, 2.0] | none | none (inferred: index = capturers on point 0..4; 1 player 1.0x, 4 players 2.0x) |
| DOM_fPlayerRespawnDelay / DOM_fTeam1RespawnDelay / DOM_fTeam2RespawnDelay | 0.0 / 0.0 / 0.0 | none | none |
| DOM_iPlayerMaxSpawnCount | -1 (unlimited) | none | none |
| DOM_iOutOfBounds_TimeToReturn | 5 | none | none |
| DOM_fObjectiveMaxDistance | 40.0 | none | none |
| DOM_fNoInteractivityTimeoutOverride | 60.0 | 0..600 | none |
| DOM_fUrgencyTimeThreshold / DOM_fUrgencyPercentageThreshold | 60.0 / 0.12 | 0..120 / 0..1 | none (urgency music/VO, inferred) |
| DOM_iLobbyPlayerCountStartTimer / ToSpeedUpTimer | 16 / 16 | none | none |
| DOM_iSoldierMandownType | 1 | 0..2 | none |
| DOM_bSoldierBleedoutOnSquadWipe | false | n/a | none |
| DOM_bAllowQuickRespawnBeaconDeploy | false | n/a | none |
| DOM_bEnableOrders / DOM_bTacticalAdviceEnabled | true / false | n/a | none |
| DOM_fAudioFalloffDistanceToObjective | 1.0 | 1..200 | none |
| Recon / Assault / Engineer / Support Recommended | false x4 | n/a | none |
| DOM_iCommanderVoice | -1 | none | none |
| Spawn-scoring weights (inferred from names): iObjectiveScoreIfFriendly 5, IfEnemy -5, IfNeutral -1, IfFriendlyContested 3; iTeamProximityNearScore 1 (radius 0..20); iEnemyProximityNearScore -6 (0..20); iPreviousDeathProximityNearScore -6 (0..20); iRecentlyUsedScore 1, fRecentlyUsedDuration 5.0 | as listed | none | none |

Not present in the data: points per objective per tick as a named value (no DOM_iPointsPerTick; the amount per tick is an unnamed constant in the round graph or capture GEM), any XP value, a vehicle setting. Round graphs GME_Sim_Domination_Round / GME_Pres_Domination_Round / GM_Domination_LaunchFunction hold only unnamed constants plus null interfaces (ArrayFloat, MI_Sim_GameMode, ActivityStateMachine, MI_Pres_GameMode, ActivityParameters, LaunchParameters); no further rules are recoverable. Shared capture logic (SimEx_CaptureVolume) names only SoldiersOnPoint, AllSoldiersOnPoint, AllVehiclesOnPoint, SoldiersExitedPoint, SoldiersDeadOrExited (all null). The Carriable_Plant, MCOM, Destructible entries in the dump are shared libraries not used by Domination.

UI text confirmed: title "Domination"; "Drop into a close-quarters infantry-only battle to gain control of objectives and hold them for as long as possible."; "Fight to capture and hold more objectives than the enemy."; "First team to reach the points target wins."; "CONTROL OBJECTIVES: Controlling each objective gradually earns you a set amount of points"; "Win by reaching the points target first or by having the most points when the time expires"; a variant label "HARDCORE DOMINATION" exists. Only the win conditions and the capture-and-hold idea are confirmed; all numbers are from tweakables only. maps-tweakables.txt has no Domination values (only Conquest initial scores such as Abbasid_CQ_iInitialScore 1200, plus unrelated SpawnPreventionRadius_*).

### Objective table (AD_Objective_Capture_Domination) vs Conquest (AD_Objective_Conquest)
- CapturePoint: Domination default GMPF_CapturePoint_NoRepresentation (no physical flag); variant 1 = GMPF_CapturePoint_OneTimeUse. Conquest: default GMPF_CapturePoint, variant 0 = GMPF_CapturePoint_Flag, variant 1 = OneTimeUse. So Domination has no Flag variant and a no-representation default.
- Others: Sector (GMPF_Sector), SectorSpawns (GMPF_SectorSpawns), CapturePoint_OutlineArea (GMPF_OutlineArea), CapturePoint_Proxy (GMPF_CapturePoint_Proxy), Insertion (variants 0..18: Cautious_Arrival, Arrival_Corner, LongDistance, OnSpot v1-v5, Chaotic_Arrival v1-v3, Chaotic_LongDistance and _Cover, GAU_CornerStack, GAU_CoverToCover, GAU_MH47 Exit_OnGround and FastRope, Vehicle_Quad, Vehicle_FlyerUnarmed), Insertion_Event (Airstrike, JetStraight).
- Caveat: every placed Domination CapturePoint has key=-1 yet the extraction prints GMPF_CapturePoint, not the table default GMPF_CapturePoint_NoRepresentation (open question).

## 2. Per-map data

### Siege of Cairo (MP_ABBASID)
- Assets: Domination, Domination_Art, Domination_Global_Schematic, MP_Domination0, MP_Domination0_Schematic, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) Domination, MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- GEM counts: {"GEM_TelemetryArea": 7, "GEM_CapturePoint": 3, "GEM_Insertion": 4, "GEM_CapturePoint_OutlineArea": 2, "GEM_SpecialCombatArea": 1, "GEM_Sector": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @1 pos=(-164.1, 65.4, 90.4)
  - @58 pos=(-138.0, 66.7, 55.1)
  - @64 pos=(-206.7, 67.4, 60.4)
  - Edges (m): @1-@58 44, @1-@64 52, @58-@64 69
- Play area: POLY14@11 (large) / POLY30@32 (inner) bbox=[-280,-24,-49,170] = 231x194 m (bbox area 44814 m2); inner bbox=[-236, 22, -94, 130] = 142x108 m
- SpecialCombatArea MP_Domination0@46 pos=(-176.0, 65.4, 54.8)
- Sector MP_Domination0@50 pos=(-178.3, 66.8, 14.4)
- SectorSpawns MP_Domination0@66 pos=(-120.3, 65.6, 31.0)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Has a SpecialCombatArea (@46, in BOX@41). Layer Domination_Art present. Team1 = Pax Armata, team2 = Alliance/NATO (swapped from default). 7 TelemetryAreas. 2 OutlineAreas (@7,@22), both on the western CP (@64). Sector/SectorSpawns carry the placeholder values shared with six other maps.

### Empire State (MP_AFTERMATH)
- Assets: MP_Domination0, MeshVariationDb_Win32, staticmodelgroup.physics
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_Sector": 1, "GEM_SectorSpawns": 1, "GEM_DeployCam": 1, "GEM_Insertion": 4, "GEM_CapturePoint_OutlineArea": 1, "GEM_CapturePoint": 3}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @35 pos=(-653.0, 54.6, 34.4)
  - @37 pos=(-634.4, 58.9, -28.6)
  - @50 pos=(-602.9, 57.6, 14.6)
  - Edges (m): @35-@37 66, @35-@50 54, @37-@50 53
- Play area: POLY58@38 bbox=[-708,-86,-582,98] = 126x184 m (bbox area 23184 m2)
- Sector MP_Domination0@1 pos=(-674.0, 53.7, -57.5)
- SectorSpawns MP_Domination0@2 pos=(-721.3, 48.6, 294.4)
- DeployCam MP_Domination0@7 pos=(-600.0, 1387.5, -50.0)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Only map with a DeployCam (@7, y=1387.5). SectorSpawns @2 at (-721,48.6,294) lies about 190 m outside the play polygon. No telemetry. Layout runs N-S (163 m between the farthest insertions).

### Wake Island (MP_ATOLL)
- Assets: Domination, Domination_Global_Schematic, generated/AG_Domination_DynamicDD_Schematic_5BDA55B0, generated/AG_Domination_DynamicDD_boxes_EFCBB3E5, Domination_Global, MP_Domination0, MP_Domination0_Schematic, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_CapturePoint": 3, "GEM_Insertion": 4, "GEM_Sector": 1, "GEM_TelemetryArea": 3, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @2 pos=(362.8, 99.9, -54.0)
  - @22 pos=(341.4, 100.2, -116.0)
  - @28 pos=(378.4, 100.3, -99.0)
  - Edges (m): @2-@22 66, @2-@28 48, @22-@28 41
- Play area: no polygon; union of BOX@1,2,3 (Domination_Global) bbox=[310,-150,414,-24] = 104x126 m (bbox area 13104 m2)
- Sector MP_Domination0@14 pos=(208.3, 102.7, 375.8)
- SectorSpawns MP_Domination0@30 pos=(371.0, 100.1, -68.5)
- Insertions: 4; SectorSpawns instances: 1
- Notes: No polygon: play area is defined only by per-CP telemetry boxes (BOX@1,2,3 and the inner BOX@9,19,26). Sector @14 at (208,103,376) is about 430 m from the CPs. Tightest CP cluster (41-66 m).

### Blackwell Fields (MP_BADLANDS)
- Assets: Domination, Domination_Global, Domination_Global_Schematic, MP_Domination0, MP_Domination0_Schematic, generated/DD_MP_Domination0_Schematics, generated/DD_MP_Domination0_Volumes, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- GEM counts: {"GEM_Insertion": 4, "GEM_CapturePoint": 3, "GEM_Sector": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @7 pos=(-149.7, 76.6, -334.2)
  - @34 pos=(-69.8, 74.4, -308.9)
  - @36 pos=(-109.2, 75.8, -325.4)
  - Edges (m): @7-@34 84, @7-@36 41, @34-@36 43
- Play area: POLY77@14 bbox=[-204,-362,-33,-263] = 171x99 m (bbox area 16929 m2)
- Sector MP_Domination0@12 pos=(-178.3, 66.8, 14.4)
- SectorSpawns MP_Domination0@27 pos=(-120.3, 65.6, 31.0)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Team1 = Pax Armata, team2 = Alliance/NATO. Sector/SectorSpawns carry default placeholder values, 300+ m from the CPs. No telemetry areas.

### Iberian Offensive (MP_BATTERY)
- Assets: MP_Domination0, MP_Domination0_Schematic
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_Insertion": 4, "GEM_TelemetryArea": 3, "GEM_CapturePoint": 3, "GEM_Sector": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @32 pos=(735.8, 77.1, 124.8)
  - @34 pos=(690.8, 75.0, 124.4)
  - @35 pos=(755.5, 80.9, 77.9)
  - Edges (m): @32-@34 45, @32-@35 51, @34-@35 80
- Play area: POLY69@4 bbox=[660,33,827,166] = 167x133 m (bbox area 22211 m2)
- Sector MP_Domination0@41 pos=(788.7, 77.0, 94.9)
- SectorSpawns MP_Domination0@42 pos=(786.5, 77.2, 96.1)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Sector @41 and SectorSpawns @42 sit at the east edge of the polygon (789,95), about 35 m from CP @35.

### Liberation Peak (MP_CAPSTONE)
- Assets: Domination, Domination_Global, Domination_Global_Schematic, Domination_Telemetry, MP_Domination0, MP_Domination0_Schematic, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_Insertion": 4, "GEM_TelemetryArea": 3, "GEM_CapturePoint": 3, "GEM_Sector": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @13 pos=(146.2, 129.9, 59.8)
  - @28 pos=(109.5, 133.4, 83.5)
  - @32 pos=(60.8, 137.8, 98.6)
  - Edges (m): @13-@28 44, @13-@32 94, @28-@32 51
- Play area: POLY71@2 bbox=[-2,17,201,144] = 203x127 m (bbox area 25781 m2)
- Sector MP_Domination0@29 pos=(-178.3, 66.8, 14.4)
- SectorSpawns MP_Domination0@34 pos=(-120.3, 65.6, 31.0)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Sector/SectorSpawns at placeholder values; CP @32 is 94 m from CP @13. Insertions use OnSpot variants only.

### Contaminated (MP_CONTAMINATED)
- Assets: Dom, Dom_Global, Dom_Global_Schematic, Dom_Telemetry, Domination0, Domination0_Schematic, generated/AG_Domination_DynamicDD_Schematic_5BDA55B0, generated/AG_Domination_DynamicDD_boxes_EFCBB3E5, dom/MeshVariationDb_Win32, dom/staticmodelgroup.physics, dom_networkregistry_Win32, dom_templatedescriptorregistry
- Layout variants: one; instance layer(s) Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_TelemetryArea": 7, "GEM_CapturePoint": 3, "GEM_Insertion": 4, "GEM_Sector": 1, "GEM_SpecialCombatArea": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @5 pos=(163.5, 348.5, 0.7)
  - @35 pos=(70.5, 346.6, -48.1)
  - @39 pos=(117.8, 339.7, -26.8)
  - Edges (m): @5-@35 105, @5-@39 53, @35-@39 52
- Play area: POLY19@46 (Domination0) bbox=[-3,-114,204,63] = 207x177 m (bbox area 36639 m2)
- Sector Domination0@19 pos=(101.1, 349.4, -39.2)
- SpecialCombatArea Domination0@29 pos=(-2.4, 318.0, 63.4)
- SectorSpawns Domination0@31 pos=(101.2, 349.4, -39.3)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Layer names Domination0 / Dom (no MP_ prefix). CPs at y=340-350, SpecialCombatArea @29 at y=318. 7 TelemetryAreas; Dom_Telemetry POLY6@2 and POLY10@4 are CP-local. Largest CP gap 105 m.

### Area 51 (MP_DRYLAKE)
- Assets: Domination, Domination_Global, Domination_Global_Schematic, MP_Domination0, MP_Domination0_Schematic, generated/AG_Domination_DynamicDD_Schematic_5BDA55B0, generated/AG_Domination_DynamicDD_boxes_EFCBB3E5, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_CapturePoint": 3, "GEM_Insertion": 4, "GEM_Sector": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @1 pos=(-163.2, 64.0, 92.8)
  - @9 pos=(-134.4, 64.0, 57.0)
  - @11 pos=(-200.6, 64.0, 55.8)
  - Edges (m): @1-@9 46, @1-@11 53, @9-@11 66
- Play area: POLY27@15 bbox=[-237,22,-95,129] = 142x107 m (bbox area 15194 m2)
- Sector MP_Domination0@5 pos=(-178.3, 64.0, 14.4)
- SectorSpawns MP_Domination0@8 pos=(-120.3, 64.0, 31.0)
- Insertions: 4; SectorSpawns instances: 1
- Notes: CP and polygon (x,z) are within about 6 m of Siege of Cairo, and Sector/SectorSpawns use the same placeholder values: layout looks cloned from Siege of Cairo (all y=64.0). All insertions key -1 (default).

### Manhattan Bridge (MP_DUMBO)
- Assets: MP_Domination0, MP_Domination0_EcsPrefab_ecsPrefab, MP_Domination0_Schematic, MeshVariationDb_Win32
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_Sector": 1, "GEM_TelemetryArea": 3, "GEM_Insertion": 4, "GEM_CapturePoint": 3, "GEM_SectorSpawns": 1, "GEM_SpecialCombatArea": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @18 pos=(-46.7, 57.3, -228.3)
  - @28 pos=(41.6, 59.2, -224.0)
  - @41 pos=(0.0, 55.2, -272.0)
  - Edges (m): @18-@28 88, @18-@41 64, @28-@41 64
- Play area: POLY59@13 bbox=[-116,-340,111,-182] = 227x158 m (bbox area 35866 m2)
- Sector MP_Domination0@4 pos=(7.2, 111.4, -255.4)
- SectorSpawns MP_Domination0@19 pos=(-4.0, 57.3, -237.8)
- SpecialCombatArea MP_Domination0@39 pos=(-40.7, 62.4, -343.8)
- Insertions: 4; SectorSpawns instances: 1
- Notes: SpecialCombatArea @39 at z=-343.8 near the south edge of the polygon. BOX@24 and BOX@32 both bound CP @28. CP @41 (0,-272) is the southern outlier, 64-88 m from the others.

### Eastwood (MP_EASTWOOD)
- Assets: MP_Domination0, MP_Domination0_EcsPrefab_ecsPrefab, MP_Domination0_Schematic
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_CapturePoint": 3, "GEM_Insertion": 4, "GEM_TelemetryArea": 3, "GEM_Sector": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @7 pos=(75.8, 234.3, 15.1)
  - @17 pos=(131.7, 232.5, -27.8)
  - @35 pos=(13.3, 233.4, 14.1)
  - Edges (m): @7-@17 70, @7-@35 63, @17-@35 126
- Play area: POLY81@1 bbox=[-21,-79,166,87] = 187x166 m (bbox area 31042 m2)
- Sector MP_Domination0@26 pos=(788.7, 77.0, 94.9)
- SectorSpawns MP_Domination0@34 pos=(2.3, 235.8, 31.6)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Sector @26 at (788.7,77.0,94.9) is the Iberian Offensive Sector value, 790 m from the CPs (unplaced). Insertion @19 uses key 15 (OnSpot_v4_NOT_FOR_REVEAL). CP @17 is 126 m from CP @35.

### Operation Firestorm (MP_FIRESTORM)
- Assets: Domination, Domination_Global, Domination_Global_Schematic, Domination_Telemetry, MP_Domination0, MP_Domination0_Schematic, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_TelemetryArea": 3, "GEM_CapturePoint": 3, "GEM_Insertion": 4, "GEM_CapturePoint_OutlineArea": 3, "GEM_Sector": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @10 pos=(-110.4, 125.0, -132.2)
  - @11 pos=(-85.1, 125.0, -76.7)
  - @30 pos=(-149.8, 125.0, -60.1)
  - Edges (m): @10-@11 61, @10-@30 82, @11-@30 67
- Play area: POLY55@6 bbox=[-191,-167,-39,-12] = 152x155 m (bbox area 23560 m2)
- Sector MP_Domination0@23 pos=(-178.3, 66.8, 14.4)
- SectorSpawns MP_Domination0@35 pos=(-105.8, 124.8, -99.5)
- Insertions: 4; SectorSpawns instances: 1
- Notes: 3 OutlineAreas. Insertions use Chaotic_Arrival (keys 6, 8), as on Railway to Golmud. Sector at placeholder; SectorSpawns is placed (inside BOX@1).

### Railway to Golmud (MP_GOLMUDRAILWAY)
- Assets: Domination, generated/AG_Domination_DynamicDD_Schematic_5BDA55B0, generated/AG_Domination_DynamicDD_boxes_EFCBB3E5, Domination_Global, Domination_Global_Schematic, MP_Domination0, MP_Domination0_Schematic, domination/MeshVariationDb_Win32, domination/staticmodelgroup.physics, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_Insertion": 4, "GEM_TelemetryArea": 3, "GEM_CapturePoint": 3, "GEM_SectorSpawns": 1, "GEM_Sector": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @15 pos=(-116.0, 738.9, 875.6)
  - @27 pos=(-178.8, 743.0, 914.1)
  - @31 pos=(-53.0, 738.1, 834.1)
  - Edges (m): @15-@27 74, @15-@31 75, @27-@31 149
- Play area: POLY32@2 bbox=[-261,787,18,972] = 279x185 m (bbox area 51615 m2)
- SectorSpawns MP_Domination0@18 pos=(-84.7, 738.1, 869.0)
- Sector MP_Domination0@33 pos=(-111.6, 802.7, 767.3)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Largest play polygon by area (51615 m2). Chaotic_Arrival insertions on the west pair. Sector @33 at (-112,803,767) is about 20 m south of the polygon edge (z 787). CP @27 is 149 m from CP @31.

### Tsuru Reef (MP_ISOLATED)
- Assets: Domination, Domination_Global, Domination_Global_Schematic, MP_Domination0, MP_Domination0_Schematic, generated/AG_Domination_DynamicDD_Schematic_5BDA55B0, generated/AG_Domination_DynamicDD_boxes_EFCBB3E5, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- GEM counts: {"GEM_TelemetryArea": 3, "GEM_CapturePoint": 3, "GEM_Sector": 1, "GEM_Insertion": 4, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @7 pos=(-553.5, 109.8, -177.6)
  - @17 pos=(-652.7, 111.9, -141.1)
  - @37 pos=(-609.9, 103.7, -183.7)
  - Edges (m): @7-@17 106, @7-@37 57, @17-@37 60
- Play area: no polygon; union of BOX@1,2,3 (Domination_Global) bbox=[-683,-218,-527,-113] = 156x105 m (bbox area 16380 m2)
- Sector MP_Domination0@9 pos=(-595.7, 104.7, -155.9)
- SectorSpawns MP_Domination0@33 pos=(-872.7, 102.4, 511.1)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Team1 = Pax Armata, team2 = Alliance/NATO. SectorSpawns @33 at (-873,102,511) and the three TelemetryAreas (@3,@4,@6, near (-857,494)) are about 700 m from the CPs: unplaced/leftover. Only per-CP boxes/polys bound the play area. Sector @9 is next to the CPs.

### Saints Quarter (MP_LIMESTONE)
- Assets: MP_Domination0, MP_Domination0_Schematic
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_CapturePoint": 3, "GEM_Insertion": 4, "GEM_TelemetryArea": 4, "GEM_Sector": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @10 pos=(328.6, 69.0, 123.5)
  - @14 pos=(289.3, 64.5, 89.0)
  - @20 pos=(367.8, 63.8, 91.7)
  - Edges (m): @10-@14 52, @10-@20 50, @14-@20 79
- Play area: no polygon or box; CapturePoint+Insertion extent only bbox=[281,82,384,124] = 103x42 m (bbox area 4326 m2)
- Sector MP_Domination0@21 pos=(334.7, 81.0, 101.6)
- SectorSpawns MP_Domination0@25 pos=(332.8, 81.0, 101.7)
- Insertions: 4; SectorSpawns instances: 1
- Notes: No large polygon or box; only 3 small CP polygons (9-16 m across). 4 TelemetryAreas (one per CP plus one at the sector @15). Smallest footprint (103x42 m, CP+insertion extent).

### New Sobek City (MP_OUTSKIRTS)
- Assets: Domination, Domination_Global, Domination_Global_Schematic, MP_Domination0, MP_Domination0_Schematic, generated/DD_MP_Domination0_Schematics, generated/DD_MP_Domination0_Volumes, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_CapturePoint": 3, "GEM_Insertion": 4, "GEM_TelemetryArea": 5, "GEM_Sector": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @1 pos=(-65.4, 95.9, -99.7)
  - @2 pos=(-0.3, 95.8, -99.9)
  - @15 pos=(-32.7, 95.8, -57.4)
  - Edges (m): @1-@2 65, @1-@15 53, @2-@15 53
- Play area: POLY46@45 (inner BOX@1 Domination_Global 102x62) bbox=[-94,-126,34,-25] = 128x101 m (bbox area 12928 m2)
- Sector MP_Domination0@24 pos=(-34.9, 119.7, -85.6)
- SectorSpawns MP_Domination0@32 pos=(-38.1, 108.5, -97.6)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Two nested bounds: Domination_Global BOX@1 (102x62) and MP_Domination0 POLY46 (128x101). 5 TelemetryAreas; Domination_Global POLY6@3 [-138,-155,-79,4] holds only a TelemetryArea. Sector at y=119.7 (24 m above the CPs).

### Vegas Strip (MP_PARADISE)
- Assets: Domination, Domination_Global, Domination_Global_Schematic, MP_Domination0, MP_Domination0_Schematic, generated/AG_Domination_DynamicDD_Schematic_5BDA55B0, generated/AG_Domination_DynamicDD_boxes_EFCBB3E5, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_CapturePoint": 3, "GEM_Insertion": 4, "GEM_Sector": 1, "GEM_SectorSpawns": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @2 pos=(-102.0, 44.2, 123.3)
  - @7 pos=(-129.2, 51.5, 197.0)
  - @14 pos=(-169.1, 53.4, 139.5)
  - Edges (m): @2-@7 79, @2-@14 69, @7-@14 70
- Play area: POLY51@9 bbox=[-233,30,-27,242] = 206x212 m (bbox area 43672 m2)
- Sector MP_Domination0@13 pos=(-178.3, 64.0, 14.4)
- SectorSpawns MP_Domination0@19 pos=(-120.3, 64.0, 31.0)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Sector/SectorSpawns at placeholder values. Longest N-S layout: CPs span z 123..197.

### Cairo Bazaar (MP_PLAZA)
- Assets: Domination, Domination_Global, Domination_Global_Schematic, MP_Domination0, MP_Domination0_Schematic, generated/AG_Domination_DynamicDD_Schematic_5BDA55B0, generated/AG_Domination_DynamicDD_boxes_EFCBB3E5, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {"team1": "Alliance/NATO", "team2": "Coalition/Pax Armata"}
- GEM counts: {"GEM_Insertion": 4, "GEM_CapturePoint": 3, "GEM_SectorSpawns": 1, "GEM_SpecialCombatArea": 1, "GEM_Sector": 1, "GEM_CapturePoint_OutlineArea": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @4 pos=(-49.0, 64.6, -6.5)
  - @19 pos=(-62.2, 64.2, -70.8)
  - @21 pos=(5.3, 65.6, 27.5)
  - Edges (m): @4-@19 66, @4-@21 64, @19-@21 119
- Play area: POLY79@29 bbox=[-108,-116,44,91] = 152x207 m (bbox area 31464 m2)
- SectorSpawns MP_Domination0@9 pos=(-120.3, 65.6, 31.0)
- SpecialCombatArea MP_Domination0@13 pos=(20.0, 67.2, 93.2)
- Sector MP_Domination0@23 pos=(-178.3, 66.8, 14.4)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Team1 = Alliance/NATO, team2 = Pax Armata (explicit, equals default). SpecialCombatArea @13. One OutlineArea. CP @21 is 119 m from CP @19. Sector/SectorSpawns at placeholder. Insertion @8 uses key 15.

### Hagental Base (MP_SUBSURFACE)
- Assets: Domination, Domination0, Domination0_Schematic, Domination_Global, Domination_Global_Schematic, generated/AG_Domination_DynamicDD_Schematic_5BDA55B0, generated/AG_Domination_DynamicDD_boxes_EFCBB3E5, domination/MeshVariationDb_Win32, domination_networkregistry_Win32, domination_templatedescriptorregistry
- Layout variants: one; instance layer(s) Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_TelemetryArea": 4, "GEM_CapturePoint": 3, "GEM_Insertion": 4, "GEM_SectorSpawns": 1, "GEM_Sector": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @2 pos=(172.5, 62.0, -80.1)
  - @11 pos=(219.1, 66.6, -50.4)
  - @13 pos=(163.6, 65.9, -27.2)
  - Edges (m): @2-@11 55, @2-@13 54, @11-@13 60
- Play area: POLY12@33 (Domination0) bbox=[99,-160,282,13] = 183x173 m (bbox area 31659 m2)
- SectorSpawns Domination0@35 pos=(-120.3, 65.6, 31.0)
- Sector Domination0@36 pos=(186.6, 66.8, -43.0)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Layers Domination0 / Domination_Global (no MP_ prefix). Nested bounds: POLY12 (183x173), Domination_Global BOX@2 (137x137), POLY5/POLY6. 4 TelemetryAreas.

### Mirak Valley (MP_TUNGSTEN)
- Assets: MP_Domination0, MP_Domination0_Schematic, MeshVariationDb_Win32, staticmodelgroup.physics
- Layout variants: one; instance layer(s) MP_Domination0; no _Small/_Large/_Team split in the names.
- Faction overrides: {}
- GEM counts: {"GEM_Insertion": 4, "GEM_CapturePoint": 3, "GEM_TelemetryArea": 3, "GEM_SectorSpawns": 1, "GEM_Sector": 1}
- Capture points (all key=-1, extraction variant GMPF_CapturePoint; no letters or order stored):
  - @3 pos=(4.2, 86.1, -334.3)
  - @16 pos=(38.4, 86.1, -379.4)
  - @30 pos=(75.1, 86.0, -355.6)
  - Edges (m): @3-@16 57, @3-@30 74, @16-@30 44
- Play area: POLY24@24 bbox=[-59,-441,131,-276] = 190x165 m (bbox area 31350 m2)
- SectorSpawns MP_Domination0@33 pos=(23.1, 86.0, -335.8)
- Sector MP_Domination0@36 pos=(8.6, 92.4, -338.8)
- Insertions: 4; SectorSpawns instances: 1
- Notes: Sector @36 inside the CP @3 polygon (POLY8@6). Compact triangle, 44-74 m edges.

## 3. Cross-map table

| Map | Layouts | Objectives per layout | Play area bbox (m) | bbox area m2 | CP edge range m |
|---|---|---|---|---|---|
| Siege of Cairo | 1 | 3 | 231x194 | 44814 | 44-69 |
| Empire State | 1 | 3 | 126x184 | 23184 | 53-66 |
| Wake Island | 1 | 3 | 104x126 | 13104 | 41-66 |
| Blackwell Fields | 1 | 3 | 171x99 | 16929 | 41-84 |
| Iberian Offensive | 1 | 3 | 167x133 | 22211 | 45-80 |
| Liberation Peak | 1 | 3 | 203x127 | 25781 | 44-94 |
| Contaminated | 1 | 3 | 207x177 | 36639 | 52-105 |
| Area 51 | 1 | 3 | 142x107 | 15194 | 46-66 |
| Manhattan Bridge | 1 | 3 | 227x158 | 35866 | 64-88 |
| Eastwood | 1 | 3 | 187x166 | 31042 | 63-126 |
| Operation Firestorm | 1 | 3 | 152x155 | 23560 | 61-82 |
| Railway to Golmud | 1 | 3 | 279x185 | 51615 | 74-149 |
| Tsuru Reef | 1 | 3 | 156x105 | 16380 | 57-106 |
| Saints Quarter | 1 | 3 | 103x42 | 4326 | 50-79 |
| New Sobek City | 1 | 3 | 128x101 | 12928 | 53-65 |
| Vegas Strip | 1 | 3 | 206x212 | 43672 | 69-79 |
| Cairo Bazaar | 1 | 3 | 152x207 | 31464 | 64-119 |
| Hagental Base | 1 | 3 | 183x173 | 31659 | 54-60 |
| Mirak Valley | 1 | 3 | 190x165 | 31350 | 44-74 |

Layout reading: every map has exactly one Domination layout (instance layer MP_Domination0, or Domination0 on Contaminated and Hagental Base) with exactly 3 CapturePoints, 1 Sector, 1 SectorSpawns, 4 Insertions. No _Small/_Large/_Team/numbered variants exist in the layer names (the 0 is a single index). The play area used here is the large polygon containing all three CPs plus insertions. What type that polygon is (CombatArea, Sector area, telemetry) is not labelled; only SpecialCombatArea instances (Siege of Cairo, Contaminated, Manhattan Bridge, Cairo Bazaar) are named as combat areas.

## 4. Key findings
1. Exactly one 3-point layout on all 19 maps (3-flag triangle, edges 40-149 m). Score tick interval tightens with objectives held (3.5 / 2.5 / 1.5 s per DOM_fScoreDelays, inferred), target 200, round time 15.
2. Many Sector/SectorSpawns instances are unplaced default values: (-178.3,66.8,14.4) and (-120.3,65.6,31.0) appear on Siege of Cairo, Blackwell Fields, Liberation Peak, Operation Firestorm, Vegas Strip, Cairo Bazaar, Area 51; Eastwood's Sector is Iberian Offensive's position; Tsuru Reef (SectorSpawns, 700 m), Wake Island (Sector, 430 m) and Empire State (SectorSpawns, 190 m) lie far from the play area, Railway to Golmud Sector is 20 m outside it. The play area cannot be taken from the Sector on those maps.
3. Area 51 is a near clone of Siege of Cairo in (x,z): CPs within about 6 m, polygon within 1 m.

## 5. Open questions
- All CapturePoints key=-1 print GMPF_CapturePoint, while the table default is GMPF_CapturePoint_NoRepresentation: which prefab actually spawns? (every CapturePoint, e.g. Abbasid MP_Domination0@1/@58/@64)
- Points per tick and XP are not named anywhere; per-tick amount is probably a constant in GME_Sim_Domination_Round. Unit of DOM_fRoundtime and the indexing of DOM_fScoreDelays / multipliers are assumed.
- What the polygons are (CombatArea vs Sector vs telemetry): Abbasid POLY14@11 vs POLY30@32; Outskirts BOX@1 vs POLY46@45; Hagental Base POLY12@33 vs BOX@2.
- Unplaced Sector/SectorSpawns: Eastwood Sector @26, Tsuru Reef SectorSpawns @33, Wake Island Sector @14, Empire State SectorSpawns @2, Railway to Golmud Sector @33, plus default-value cases (Blackwell Fields @12/@27, Liberation Peak @29/@34, Operation Firestorm @23, Vegas Strip @13/@19, Cairo Bazaar @9/@23, Area 51 @5/@8, Siege of Cairo @50/@66). Does the engine derive spawns from the CPs instead?
- Tsuru Reef TelemetryAreas @3/@4/@6 near (-857,494) are 700 m from the CPs; New Sobek City POLY6@3 (Domination_Global) holds only a TelemetryArea.
- Side assignment: only Siege of Cairo, Blackwell Fields, Tsuru Reef (team1 = Pax Armata) and Cairo Bazaar (team1 = Alliance/NATO) have overrides. HQ side per CP is not stored; each map has two insertion clusters of two, which implies the two team sides but not which CP is nearest.
- Eastwood Insertion @19 and Cairo Bazaar Insertion @8 use key 15 (OnSpot_v4_NOT_FOR_REVEAL).
- [0..0] ranges are not usable as bounds.
- map-names.json in the folder lists Portal maps and omits several Domination maps; names here come from the README.
