# Team Deathmatch - build 2.1.1.0 analysis

Sources: TeamDeathMatch-tweakables.txt, TeamDeathMatch-maps.txt, ui-text.txt, objective-table.json, map-names.json, maps-tweakables.txt. Coordinates in metres, bboxes are [minx, minz, maxx, maxz]. "Inferred" marks my reading; the data labels nothing about teams or play-area meaning.

## 1. Mode rules

### 1.1 MUT_TeamDM tweakables (client defaults; a server playlist can override). Format: value [min..max]. A range of [0..0] means the file stores no real range (unbounded or unknown), not a fixed value.

Win condition and timing
| Tweakable | Value | Range | UI text confirms |
|---|---|---|---|
| TDM_iTargetScore | 100 | [0..0] | Yes: "reach the kill target first"; the number 100 is not in the UI text |
| TDM_fRoundTime | 15.0 | [0.0..0.0] | Time limit exists ("highest kill count when the time expires"); value and unit (minutes, inferred) not in UI text |
| TDM_fOvertimeDuration | 1.0 | [0.0..0.0] | No |
| TDM_iBigLeadThreshold | 20 | [0..0] | No (lead of 20 kills; big-lead announcement, inferred) |
| TDM_bAnnounceLeadChangeInUI | true | - | No |
| TDM_fUrgencyTimeThreshold | 60.0 | [0.0..60.0] | No |
| TDM_fUrgencyPercentageThreshold | 0.12 | [0.0..1.0] | No (12 % of target score = 12 kills left, inferred) |
| TDM_fLateSpawnTimeThreshold | 60.0 | [0.0..60.0] | No |
| TDM_iLobbyPlayerCountStartTimer | 16 | [0..0] | No |
| TDM_iLobbyPlayerCountToSpeedUpTimer | 16 | [0..0] | No |
| TDM_fNoInteractivityTimeoutOverride | 60.0 | [0.0..600.0] | No (AFK timeout, inferred) |

Respawn
| Tweakable | Value | Range |
|---|---|---|
| TDM_fPlayerRespawnDelay | 0.0 | [0.0..0.0] |
| TDM_fTeam1RespawnDelay | 0.0 | [0.0..0.0] |
| TDM_fTeam2RespawnDelay | 0.0 | [0.0..0.0] |
| TDM_iPlayerMaxSpawnCount | -1 (unlimited, inferred) | [0..0] |
| TDM_bAllowQuickRespawnBeaconDeploy | false | - |
| TDM_iSoldierMandownType | 1 | [0..0] |
| TDM_bSoldierBleedoutOnSquadWipe | false | - |

Spawn logic (scoring of candidate spawn points; higher score preferred, inferred)
| Tweakable | Value | Range |
|---|---|---|
| TDM_iPrimarySpawnScore | 3 | [0..0] |
| TDM_iFriendlyProximityScore | 1 | [0..0] |
| TDM_fFriendlyProximityMinRadius / MaxRadius | 0.0 / 20.0 | [0..0] |
| TDM_iEnemyProximityNearScore | -20 | [0..0] |
| TDM_fEnemyProximityNearMinRadius / MaxRadius | 0.0 / 20.0 | [0..0] |
| TDM_iEnemyProximityFarScore | -2 | [0..0] |
| TDM_fEnemyProximityFarMinRadius / MaxRadius | 20.1 / 40.0 | [0..0] |
| TDM_iPreviousDeathProximityScore | -20 | [0..0] |
| TDM_fPreviousDeathProximityMinRadius / MaxRadius | 0.0 / 20.0 | [0..0] |
| TDM_iRecentlyUsedScore | -1 | [0..0] |
| TDM_fRecentlyUsedDuration | 3.0 | [0.0..0.0] |
| TDM_iAreaSwapScoreThreshold | -10 | [0..0] (when the best score in the current area drops to this, spawning moves to the AlternateSpawnArea; inferred from the name and the GEM) |

Out of bounds
| TDM_iOutOfBounds_TimeToReturn | 5 | [0..0] (seconds, inferred) |

Other
| Tweakable | Value |
|---|---|
| TDM_bKillStreaksAllowed | true |
| TDM_iKillStreakStart / TDM_iKillStreakDelta | 5 / 5 |
| TDM_iCommanderVoice | -1 |
| Assault / Engineer / Support / Recon Recommended | all false |

XP: MUT_TeamDM has no XP tweakable. No XP value for Team Deathmatch exists in the supplied files; not reported.

### 1.2 Round logic and objective definition
- GME_Sim_TeamDM_Round has only named variables, all null at default: TargetScore, ActivityStateMachine, LastTeam, WinningTeam, MI_Sim_GameMode. GME_Pres_TeamDM_Round: MI_Pres_GameMode only. GM_TeamDM_LaunchFunction: LaunchParameters, ActivityParameters (null). So the target score (100) comes from MUT_TeamDM.TDM_iTargetScore feeding TargetScore (inferred); the win/lose graph constants are unnamed.
- The _Shared GEM logic dumped with the file (capture, MCOM, carriable bomb, destructible zone, reinforcement, supply station, vehicle superiority, sector spotting) is shared infrastructure; none of it has a TDM instance in any map (no CapturePoint, MCOM etc. in the maps file). Nothing mode-specific to read there.
- AD_Objective_TeamDM (objective-table.json) lists only 4 modules: Sector (default GMPF_Sector, no variants), AlternateSpawnArea (default GMPF_AlternateSpawnArea, no variants), Insertion (default Cautious_Arrival; 19 keys 0-18: Cautious Arrival / Arrival_Corner / LongDistance / OnSpot v1-v5 (v4, v5 are "NOT_FOR_REVEAL"), Chaotic Arrival v1-v3 / LongDistance / LongDistance_Cover, GAU CornerStack / CoverToCover / MH47 ExitOnGround / MH47 FastRope, Vehicle Quad, Vehicle FlyerUnarmed) and Insertion_Event (Airstrike, JetStraight). No map instantiates Insertion_Event; keys 2, 9-14, 16-18 are not used by any map either.
- Insertion keys used: 0 Arrival, 1 Arrival_Corner, 3 OnSpot_v1, 4 OnSpot_v2, 5 OnSpot_v3, 6/7/8 Chaotic_Arrival v1/v2/v3, 15 OnSpot_v4_NOT_FOR_REVEAL (Eastwood, Cairo Bazaar), and key -1 (Area 51; resolves to the default Cautious_Arrival).

### 1.3 What the UI text confirms
- Name "Team Deathmatch"; "Hardcore Team Deathmatch" exists as a separate string.
- "Face off against an enemy team in a close-quarters firefight where hostiles must be eliminated."
- "Eliminate enemies to reach the kill target first."
- "Kill enemies to increase the kill count for your team"; "Win by reaching the kill target first or by having the highest kill count when the time expires".
- Confirmed: kill target exists, time limit exists, win on most kills at time-out. Not stated in the UI text: 100 kills, 15 (minutes), respawn delay (0), spawn rules, out-of-bounds timer, XP. Overtime (1.0) and lead announcements are not described.
- Per-map tweakables (maps-tweakables.txt): none TDM specific. CQ initial scores (1200), SpawnPreventionRadius (Siege of Cairo 40 small, Iberian Offensive 45 large modes), Manhattan Bridge vehicle OOB 10 s, Golmud train flags are other-mode settings.

## 2. Maps (19; all use one layout variant, layer "MP_TeamDM0" / "TeamDM0", no _Small/_Large/_Team sets in any map)

Play-area method: the data has no CombatArea instance (only SpecialCombatArea on 3 maps), so "play area" = the largest MP_TeamDM0 polygon that contains the Sector and Insertions (inferred), or the union of the telemetry/global shapes where no such polygon exists. No map extent is in the supplied files, so the position relative to the whole map cannot be given; I give the position relative to the map's own coordinate frame only. A TelemetryArea is a stats area, not a spawn.

Recurring placeholder: Sector and AlternateSpawnArea at exactly (-120.2, 65.9, 31.3) (y 98.3 on New Sobek City) appear on 8 maps with no relation to the other geometry; (-52.5, 64.0, 0.0) on Area 51 and Vegas Strip. Treated as unplaced/default, see open questions.

### Siege of Cairo (MP_ABBASID)

- Layer assets: TeamDM_Global_Schematic, MP_TeamDM0, MP_TeamDM0_Schematic, TeamDM, TeamDM_Art, TeamDM_Global, TeamDM_Global_ecsprefab_ecsPrefab, TeamDM_Telemetry
- Faction override:  {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- Instances:
  - MP_TeamDM0@4 Insertion key=1 Insertion_Cautious_Arrival_Corner pos=[-218.3, 66.7, 50.4] in boxes[] polys[14, 16]
  - MP_TeamDM0@9 Insertion key=0 Insertion_Cautious_Arrival pos=[-103.3, 64.3, 63.4] in boxes[] polys[5, 16]
  - MP_TeamDM0@18 Insertion key=0 Insertion_Cautious_Arrival pos=[-222.6, 66.7, 65.2] in boxes[] polys[14, 16]
  - MP_TeamDM0@23 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-163.2, 72.3, 69.4] in boxes[33] polys[16]
  - MP_TeamDM0@28 Insertion key=1 Insertion_Cautious_Arrival_Corner pos=[-110.2, 64.2, 72.0] in boxes[] polys[5, 16]
  - MP_TeamDM0@37 Sector key=-1 Sector pos=[-161.5, 72.3, 69.4] in boxes[33] polys[16]
- Areas:
  - BOX@8 (MP_TeamDM0) bbox=[-189, 22, -133, 38] contains []
  - BOX@33 (MP_TeamDM0) bbox=[-189, 38, -133, 74] contains ['AlternateSpawnArea@23', 'Sector@37']
  - POLY9@5 (MP_TeamDM0) bbox=[-133, 22, -90, 100] contains ['Insertion#0@9', 'Insertion#1@28']
  - POLY9@6 (MP_TeamDM0) bbox=[-230, 74, -102, 130] contains []
  - POLY12@14 (MP_TeamDM0) bbox=[-236, 20, -189, 89] contains ['Insertion#1@4', 'Insertion#0@18']
  - POLY27@16 (MP_TeamDM0) bbox=[-236, 22, -94, 113] contains ['Insertion#1@4', 'Insertion#0@9', 'Insertion#0@18', 'AlternateSpawnArea@23', 'Insertion#1@28', 'Sector@37']
- Notes: Layout: single (MP_TeamDM0; older-style asset names TeamDM, TeamDM_Art, TeamDM_Global, TeamDM_Telemetry instead of TeamDeathMatch_*). Play area (inferred): POLY27@16 x -236..-94, z 22..113 = 142 x 91 m; it contains every instance. Sector@37 and AlternateSpawnArea@23 are 1.7 m apart inside BOX@33 (-189..-133, 38..74), near the centre of the shape union (-236..-90, 20..130). Insertions: 2 Cautious_Arrival_Corner + 2 Cautious_Arrival in two clusters (west POLY12@14 at x about -220, east POLY9@5 at x about -105) = the two spawn ends. POLY9@6 (-230..-102, 74..130) contains nothing and extends north of the play polygon. Team 1 = Pax Armata (swapped from default). No TelemetryArea.

### Empire State (MP_AFTERMATH)

- Layer assets: MP_TeamDM0, MP_TeamDM0_Schematic, TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, TeamDeathMatch_VFX, TeamDeathMatch_VFX_Schematic, generated/DD_MP_TeamDM0_Schematics, generated/DD_MP_TeamDM0_Volumes
- Faction override:  {}
- Instances:
  - MP_TeamDM0@3 TelemetryArea key=-1 None pos=[-612.9, 54.0, -144.4] in boxes[] polys[12]
  - MP_TeamDM0@9 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-555.5, 58.7, -31.1] in boxes[] polys[]
  - MP_TeamDM0@15 Sector key=-1 Sector pos=[-605.0, 54.8, -109.8] in boxes[] polys[12]
  - MP_TeamDM0@23 TelemetryArea key=-1 None pos=[-638.7, 53.8, -144.0] in boxes[] polys[12]
  - MP_TeamDM0@24 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-574.9, 53.8, -173.9] in boxes[] polys[12]
  - MP_TeamDM0@29 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-674.9, 53.7, -41.6] in boxes[] polys[12]
  - MP_TeamDM0@30 TelemetryArea key=-1 None pos=[-580.8, 54.0, -160.2] in boxes[] polys[12]
  - MP_TeamDM0@31 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-690.7, 53.8, -56.3] in boxes[] polys[12]
  - MP_TeamDM0@45 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-539.0, 54.1, -139.3] in boxes[] polys[12]
  - MP_TeamDM0@47 TelemetryArea key=-1 None pos=[-608.3, 53.8, -111.4] in boxes[] polys[12]
- Areas:
  - POLY61@12 (MP_TeamDM0) bbox=[-704, -209, -516, -28] contains ['TelemetryArea@3', 'Sector@15', 'TelemetryArea@23', 'Insertion#3@24', 'Insertion#3@29', 'TelemetryArea@30', 'Insertion#3@31', 'Insertion#3@45', 'TelemetryArea@47']
- Notes: Layout: single. Play area: POLY61@12 x -704..-516, z -209..-28 = 188 x 181 m (only shape). Sector@15 (-605,-110) near its centre. AlternateSpawnArea@9 (-555.5,-31.1) lies in the bbox but not inside the polygon shape (polys=[]), 3 m from the north edge. The 4 Insertions are all OnSpot_v1 (key 3), spread over the shape: (-575,-174), (-675,-42), (-691,-56), (-539,-139). 4 TelemetryAreas inside the polygon. VFX asset TeamDeathMatch_VFX present.

### Wake Island (MP_ATOLL)

- Layer assets: TeamDeathMatch, TeamDeathMatch_Global_Schematic, generated/AG_TeamDeathMatch_DynamicDD_Schematic_E1E21C68, generated/AG_TeamDeathMatch_DynamicDD_boxes_4B06FFAC, MP_TeamDM0, MP_TeamDM0_Schematic, TeamDeathMatch_Global
- Faction override:  {}
- Instances:
  - MP_TeamDM0@1 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[425.2, 100.7, 21.0] in boxes[1] polys[]
  - MP_TeamDM0@7 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[259.0, 105.2, -53.8] in boxes[3] polys[]
  - MP_TeamDM0@16 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[251.8, 105.9, -52.9] in boxes[3] polys[]
  - MP_TeamDM0@18 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[426.3, 100.7, 15.1] in boxes[1] polys[]
  - MP_TeamDM0@19 TelemetryArea key=-1 None pos=[440.8, 101.6, -32.1] in boxes[1] polys[]
  - MP_TeamDM0@21 TelemetryArea key=-1 None pos=[291.0, 102.4, -66.0] in boxes[3] polys[]
  - MP_TeamDM0@23 TelemetryArea key=-1 None pos=[381.5, 100.3, -98.8] in boxes[2] polys[]
  - MP_TeamDM0@29 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[305.4, 101.3, -95.9] in boxes[3] polys[]
  - MP_TeamDM0@30 Sector key=-1 Sector pos=[377.5, 102.7, -113.8] in boxes[2] polys[]
- Areas:
  - BOX@1 (TeamDeathMatch_Global) bbox=[379, -159, 507, 43] contains ['Insertion#3@1', 'Insertion#5@18', 'TelemetryArea@19']
  - BOX@2 (TeamDeathMatch_Global) bbox=[323, -171, 450, 37] contains ['TelemetryArea@23', 'Sector@30']
  - BOX@3 (TeamDeathMatch_Global) bbox=[219, -171, 339, 28] contains ['Insertion#5@7', 'Insertion#3@16', 'TelemetryArea@21', 'AlternateSpawnArea@29']
- Notes: Layout: single. Play area = three overlapping boxes of TeamDeathMatch_Global chained along x: BOX@3 x 219..339, BOX@2 x 323..450, BOX@1 x 379..507, each about 120-128 x 199-208 m (z about -171..43); union 288 x 214 m. Insertions: 2 in BOX@3, 2 in BOX@1 (spawn ends); Sector@30 in the middle box BOX@2; AlternateSpawnArea@29 in BOX@3 (west end), 74 m from the Sector. One TelemetryArea per box. Whether the boxes are three sub-zones or one stretched area is not shown. Wake Island is the longest play area here.

### Blackwell Fields (MP_BADLANDS)

- Layer assets: MP_TeamDM0, MP_TeamDM0_Schematic, TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, generated/DD_MP_TeamDM0_Schematics, generated/DD_MP_TeamDM0_Volumes
- Faction override:  {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- Instances:
  - MP_TeamDM0@2 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[-49.0, 74.4, -303.1] in boxes[] polys[]
  - MP_TeamDM0@10 Insertion key=0 Insertion_Cautious_Arrival pos=[-48.4, 74.3, -299.1] in boxes[] polys[]
  - MP_TeamDM0@15 Sector key=-1 Sector pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - MP_TeamDM0@19 Insertion key=0 Insertion_Cautious_Arrival pos=[-177.9, 77.1, -338.3] in boxes[] polys[]
  - MP_TeamDM0@25 Insertion key=1 Insertion_Cautious_Arrival_Corner pos=[-168.9, 76.8, -336.8] in boxes[] polys[]
  - MP_TeamDM0@29 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
- Areas:
- Notes: Layout: single. No box or polygon in the TDM layer, so no play area is stored. Sector@15 and AlternateSpawnArea@29 are both at the shared default (-120.2, 65.9, 31.3). The 4 Insertions sit at z -299..-338, x -178..-48 (about 130 x 40 m cluster), about 330 m from the Sector. Team 1 = Pax Armata (swapped).

### Iberian Offensive (MP_BATTERY)

- Layer assets: MP_TeamDM0, MP_TeamDM0_Schematic, TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, generated/DD_MP_TeamDM0_Volumes_BD3DCAAE
- Faction override:  {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- Instances:
  - MP_TeamDM0@3 Sector key=-1 Sector pos=[756.8, 76.4, 87.1] in boxes[3] polys[]
  - MP_TeamDM0@5 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[756.8, 76.4, 87.1] in boxes[3] polys[]
  - MP_TeamDM0@22 TelemetryArea key=-1 None pos=[714.5, 83.2, 116.6] in boxes[] polys[1]
  - MP_TeamDM0@24 TelemetryArea key=-1 None pos=[776.4, 80.1, 78.8] in boxes[3] polys[]
  - MP_TeamDM0@36 TelemetryArea key=-1 None pos=[759.3, 73.3, 54.2] in boxes[2] polys[]
- Areas:
  - BOX@2 (TeamDeathMatch_Global) bbox=[728, 32, 797, 78] contains ['TelemetryArea@36']
  - BOX@3 (TeamDeathMatch_Global) bbox=[729, 36, 828, 142] contains ['Sector@3', 'AlternateSpawnArea@5', 'TelemetryArea@24']
  - POLY7@1 (TeamDeathMatch_Global) bbox=[663, 52, 765, 166] contains ['TelemetryArea@22']
- Notes: Layout: single. No Insertion instance at all (gem counts list none). Sector@3 and AlternateSpawnArea@5 are identical (756.8, 87.1) inside BOX@3 x 729..828, z 36..142 = 99 x 106 m. Other shapes: BOX@2 69 x 46 (TelemetryArea@36), POLY7@1 102 x 114 (x 663..765, TelemetryArea@22); union 165 x 134 m. Team 1 = Pax Armata (swapped).

### Liberation Peak (MP_CAPSTONE)

- Layer assets: TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, TeamDeathMatch_Telemetry, MP_TeamDM0, MP_TeamDM0_Schematic
- Faction override:  {}
- Instances:
  - MP_TeamDM0@3 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - MP_TeamDM0@9 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[164.7, 129.0, 62.4] in boxes[] polys[2, 10]
  - MP_TeamDM0@12 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[47.5, 138.5, 109.9] in boxes[] polys[1, 10]
  - MP_TeamDM0@20 TelemetryArea key=-1 None pos=[116.5, 129.3, 57.6] in boxes[] polys[2, 10]
  - MP_TeamDM0@25 TelemetryArea key=-1 None pos=[78.1, 142.1, 105.0] in boxes[] polys[1, 10]
  - MP_TeamDM0@26 TelemetryArea key=-1 None pos=[102.4, 133.1, 75.5] in boxes[] polys[3, 10]
  - MP_TeamDM0@28 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[50.6, 139.1, 113.0] in boxes[] polys[1, 10]
  - MP_TeamDM0@29 Sector key=-1 Sector pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - MP_TeamDM0@35 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[162.2, 129.6, 65.0] in boxes[] polys[2, 10]
- Areas:
  - POLY9@1 (TeamDeathMatch_Telemetry) bbox=[-5, 11, 125, 137] contains ['Insertion#3@12', 'TelemetryArea@25', 'Insertion#5@28']
  - POLY8@2 (TeamDeathMatch_Telemetry) bbox=[104, 11, 230, 128] contains ['Insertion#3@9', 'TelemetryArea@20', 'Insertion#5@35']
  - POLY8@3 (TeamDeathMatch_Telemetry) bbox=[64, 73, 190, 167] contains ['TelemetryArea@26']
  - POLY60@10 (MP_TeamDM0) bbox=[-2, 17, 213, 157] contains ['Insertion#3@9', 'Insertion#3@12', 'TelemetryArea@20', 'TelemetryArea@25', 'TelemetryArea@26', 'Insertion#5@28', 'Insertion#5@35']
- Notes: Layout: single (TeamDeathMatch_Telemetry asset). Play area: POLY60@10 x -2..213, z 17..157 = 215 x 140 m (MP_TeamDM0 layer); telemetry polygons POLY9@1 130 x 126, POLY8@2 126 x 117, POLY8@3 126 x 94, union 235 x 156. Insertions: 2 near (49,111) in POLY@1 and 2 near (163,64) in POLY@2 = two spawn ends about 122 m apart. Sector@29 and AlternateSpawnArea@3 at the shared default (-120.2, 65.9, 31.3), 118 m west of the play area.

### Contaminated (MP_CONTAMINATED)

- Layer assets: TeamDM0, TeamDeathMatch_Global, TeamDM0_Schematic, TeamDeathMatch, TeamDeathMatch_Global_Schematic, TeamDeathMatch_Telemetry, generated/AG_TeamDeathMatch_DynamicDD_Schematic_E1E21C68, generated/AG_TeamDeathMatch_DynamicDD_boxes_4B06FFAC
- Faction override:  {}
- Instances:
  - TeamDM0@2 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[332.4, 331.2, 68.3] in boxes[] polys[10]
  - TeamDM0@6 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[329.6, 330.9, 75.8] in boxes[] polys[10]
  - TeamDM0@13 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[198.8, 346.6, 3.4] in boxes[] polys[10]
  - TeamDM0@18 Sector key=-1 Sector pos=[263.5, 338.8, 20.1] in boxes[] polys[10]
  - TeamDM0@24 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - TeamDM0@25 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[192.6, 346.4, 7.6] in boxes[] polys[10]
- Areas:
  - POLY16@10 (TeamDM0) bbox=[175, -28, 341, 105] contains ['Insertion#3@2', 'Insertion#5@6', 'Insertion#3@13', 'Sector@18', 'Insertion#5@25']
- Notes: Layout: single, layer named TeamDM0 (not MP_TeamDM0); DynamicDD generated assets. Play area: POLY16@10 x 175..341, z -28..105 = 166 x 133 m. Sector@18 (263.5, 20.1) inside. AlternateSpawnArea@24 at the shared default (-120.2, 65.9, 31.3), 295 m west of the polygon. Insertions in two clusters, (331,72) and (196,5), 2 each. pos y is 331-347 here (other maps 50-230), no other TDM-specific content; no PsyGas instances.

### Area 51 (MP_DRYLAKE)

- Layer assets: TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, MP_TeamDM0, MP_TeamDM0_Schematic, generated/AG_TeamDeathMatch_DynamicDD_Schematic_E1E21C68, generated/AG_TeamDeathMatch_DynamicDD_boxes_4B06FFAC
- Faction override:  {}
- Instances:
  - MP_TeamDM0@1 Insertion key=-1 Insertion_Cautious_Arrival pos=[-52.5, 64.0, 64.0] in boxes[] polys[]
  - MP_TeamDM0@2 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-52.5, 64.0, 0.0] in boxes[] polys[]
  - MP_TeamDM0@3 Insertion key=-1 Insertion_Cautious_Arrival pos=[-48.6, 64.0, -64.0] in boxes[] polys[]
  - MP_TeamDM0@4 Insertion key=-1 Insertion_Cautious_Arrival pos=[-48.6, 64.0, 64.0] in boxes[] polys[]
  - MP_TeamDM0@5 Sector key=-1 Sector pos=[-52.5, 64.0, 0.0] in boxes[] polys[]
  - MP_TeamDM0@6 Insertion key=-1 Insertion_Cautious_Arrival pos=[-52.5, 64.0, -64.0] in boxes[] polys[]
- Areas:
- Notes: Layout: single. No box/polygon. All six instances are round-number stubs: Sector@5 and ASA@2 at (-52.5, 64, 0), Insertions at (-52.5,+-64) and (-48.6,+-64), all key=-1 (no variant selector) and y=64. Looks like unplaced template data, not a tuned layout. No usable play area.

### Manhattan Bridge (MP_DUMBO)

- Layer assets: MP_TeamDM0, MP_TeamDM0_Schematic, TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, TeamDeathMatch_VFX, TeamDeathMatch_VFX_Schematic
- Faction override:  {}
- Instances:
  - MP_TeamDM0@7 TelemetryArea key=-1 None pos=[-10.2, 63.0, -273.6] in boxes[24] polys[16]
  - MP_TeamDM0@10 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[26.6, 60.0, -198.0] in boxes[24] polys[16]
  - MP_TeamDM0@12 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[25.5, 59.7, -202.1] in boxes[24] polys[16]
  - MP_TeamDM0@14 SpecialCombatArea key=-1 None pos=[-40.9, 62.4, -343.8] in boxes[24] polys[]
  - MP_TeamDM0@15 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-66.0, 54.6, -303.4] in boxes[24] polys[16]
  - MP_TeamDM0@28 Sector key=-1 Sector pos=[-12.5, 63.0, -273.6] in boxes[24] polys[16]
  - MP_TeamDM0@29 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-10.9, 63.4, -273.3] in boxes[24] polys[16]
  - MP_TeamDM0@30 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[-66.6, 54.6, -307.2] in boxes[24] polys[16]
- Areas:
  - BOX@24 (MP_TeamDM0) bbox=[-141, -362, 95, -165] contains ['TelemetryArea@7', 'Insertion#5@10', 'Insertion#3@12', 'SpecialCombatArea@14', 'Insertion#3@15', 'Sector@28', 'AlternateSpawnArea@29', 'Insertion#5@30']
  - POLY47@16 (MP_TeamDM0) bbox=[-116, -340, 71, -182] contains ['TelemetryArea@7', 'Insertion#5@10', 'Insertion#3@12', 'Insertion#3@15', 'Sector@28', 'AlternateSpawnArea@29', 'Insertion#5@30']
- Notes: Layout: single. SpecialCombatArea@14 present. Play area: POLY47@16 x -116..71, z -340..-182 = 187 x 158 m, inside BOX@24 x -141..95, z -362..-165 = 236 x 197 m (the box also contains the SpecialCombatArea at (-40.9,-343.8), 4 m beyond the polygon bbox). Sector@28 and ASA@29 1.6 m apart near (-11,-273). Insertions: 2 at (26,-200) east end, 2 at (-66,-305) west end.

### Eastwood (MP_EASTWOOD)

- Layer assets: MP_TeamDM0, MP_TeamDM0_Schematic, Small_Modes_Global, Small_Modes_Perimeter, TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, TeamDeathMatch_Telemetry, _Small_Modes, _Small_Modes_Perimeter, generated/DD_MP_TeamDM0_Schematics, generated/DD_MP_TeamDM0_Volumes
- Faction override:  {"team1": "Alliance/NATO", "team2": "Coalition/Pax Armata"}
- Instances:
  - MP_TeamDM0@3 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[132.3, 232.6, -37.0] in boxes[] polys[2]
  - MP_TeamDM0@4 TelemetryArea key=-1 None pos=[95.6, 229.3, 53.5] in boxes[] polys[4]
  - MP_TeamDM0@5 TelemetryArea key=-1 None pos=[137.7, 232.0, -18.7] in boxes[] polys[2]
  - MP_TeamDM0@9 Insertion key=15 Insertion_Cautious_OnSpot_v4_NOT_FOR_REVEAL pos=[138.7, 232.4, -22.4] in boxes[] polys[2]
  - MP_TeamDM0@10 Insertion key=1 Insertion_Cautious_Arrival_Corner pos=[-4.3, 233.1, 4.2] in boxes[] polys[1]
  - MP_TeamDM0@14 TelemetryArea key=-1 None pos=[26.4, 233.1, -16.4] in boxes[] polys[1]
  - MP_TeamDM0@16 TelemetryArea key=-1 None pos=[15.2, 231.6, 76.6] in boxes[] polys[]
  - MP_TeamDM0@20 TelemetryArea key=-1 None pos=[61.6, 245.9, 13.8] in boxes[] polys[3]
  - MP_TeamDM0@21 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-7.8, 233.0, -1.3] in boxes[] polys[1]
  - MP_TeamDM0@25 Sector key=-1 Sector pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - MP_TeamDM0@27 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
- Areas:
  - POLY12@1 (TeamDeathMatch_Telemetry) bbox=[-23, -72, 97, 52] contains ['Insertion#1@10', 'TelemetryArea@14', 'Insertion#3@21']
  - POLY9@2 (TeamDeathMatch_Telemetry) bbox=[90, -84, 178, 33] contains ['Insertion#5@3', 'TelemetryArea@5', 'Insertion#15@9']
  - POLY16@3 (TeamDeathMatch_Telemetry) bbox=[33, -46, 116, 61] contains ['TelemetryArea@20']
  - POLY10@4 (TeamDeathMatch_Telemetry) bbox=[3, -6, 150, 94] contains ['TelemetryArea@4']
- Notes: Layout: single MP_TeamDM0, plus the shared Small_Modes_Global / Small_Modes_Perimeter layers (assets shared by small modes). No MP_TeamDM0-layer polygon; four telemetry polygons only: POLY12@1 120 x 124, POLY9@2 88 x 117, POLY16@3 83 x 107, POLY10@4 147 x 100; union x -23..178, z -84..94 = 201 x 178 m. Insertions: 2 near (-6,2) (west, POLY@1) and 2 near (136,-30) (east, POLY@2), about 146 m apart. Sector@25 and ASA@27 at the shared default (-120.2, 65.9, 31.3), outside. Insertion key 15 (OnSpot_v4_NOT_FOR_REVEAL) is used. TelemetryArea@16 (15,77) is in no shape. Team 1 = NATO (= default, explicitly set).

### Operation Firestorm (MP_FIRESTORM)

- Layer assets: TeamDeathMatch_Global, MP_TeamDM0, MP_TeamDM0_Schematic, TeamDeathMatch, TeamDeathMatch_Global_Schematic, TeamDeathMatch_Telemetry
- Faction override:  {}
- Instances:
  - MP_TeamDM0@1 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - MP_TeamDM0@3 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-160.4, 124.9, -154.0] in boxes[2] polys[31]
  - MP_TeamDM0@13 TelemetryArea key=-1 None pos=[-95.3, 125.0, -73.2] in boxes[] polys[31, 1]
  - MP_TeamDM0@17 TelemetryArea key=-1 None pos=[-146.1, 141.3, -135.7] in boxes[2] polys[31]
  - MP_TeamDM0@19 TelemetryArea key=-1 None pos=[-92.7, 125.0, -129.2] in boxes[3] polys[31]
  - MP_TeamDM0@23 Insertion key=6 Insertion_Chaotic_Arrival_v1 pos=[-169.6, 124.9, -151.3] in boxes[2] polys[31]
  - MP_TeamDM0@25 Sector key=-1 Sector pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - MP_TeamDM0@28 Insertion key=8 Insertion_Chaotic_Arrival_v3 pos=[-64.6, 124.9, -34.5] in boxes[] polys[31, 1]
  - MP_TeamDM0@30 TelemetryArea key=-1 None pos=[-92.6, 125.0, -73.2] in boxes[] polys[31, 1]
  - MP_TeamDM0@32 Insertion key=7 Insertion_Chaotic_Arrival_v2 pos=[-57.3, 124.9, -50.9] in boxes[] polys[31, 1]
- Areas:
  - BOX@2 (TeamDeathMatch_Telemetry) bbox=[-174, -165, -128, -98] contains ['Insertion#3@3', 'TelemetryArea@17', 'Insertion#6@23']
  - BOX@3 (TeamDeathMatch_Telemetry) bbox=[-127, -163, -50, -98] contains ['TelemetryArea@19']
  - BOX@4 (TeamDeathMatch_Telemetry) bbox=[-177, -97, -128, -15] contains []
  - POLY55@31 (MP_TeamDM0) bbox=[-191, -167, -39, -12] contains ['Insertion#3@3', 'TelemetryArea@13', 'TelemetryArea@17', 'TelemetryArea@19', 'Insertion#6@23', 'Insertion#8@28', 'TelemetryArea@30', 'Insertion#7@32']
  - POLY6@1 (TeamDeathMatch_Telemetry) bbox=[-128, -97, -49, -15] contains ['TelemetryArea@13', 'Insertion#8@28', 'TelemetryArea@30', 'Insertion#7@32']
- Notes: Layout: single (TeamDeathMatch_Telemetry). Play area: POLY55@31 x -191..-39, z -167..-12 = 152 x 155 m. Telemetry BOX@2 46 x 67, BOX@3 77 x 65, BOX@4 49 x 82, POLY6@1 79 x 82 tile the same footprint. Insertions: 2 north-west (-160,-154) Cautious_OnSpot_v1 and (-170,-151) Chaotic_Arrival_v1, 2 south-east (-65,-35) Chaotic_Arrival_v3 and (-57,-51) Chaotic_Arrival_v2: the only map with three Chaotic variants. Sector@25 and ASA@1 at the shared default (-120.2, 65.9, 31.3) (z 31, 43 m beyond the polygon).

### Railway to Golmud (MP_GOLMUDRAILWAY)

- Layer assets: MP_TeamDM0_Schematic
- Faction override:  {}
- Instances:
- Areas:
- Notes: Only asset MP_TeamDM0_Schematic. No GEM instance, no area. No stored Team Deathmatch layout on Railway to Golmud in this build (probably not offered; not verifiable from these files).

### Tsuru Reef (MP_ISOLATED)

- Layer assets: TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, MP_TeamDM0, MP_TeamDM0_Schematic, generated/AG_TeamDeathMatch_DynamicDD_Schematic_E1E21C68, generated/AG_TeamDeathMatch_DynamicDD_boxes_4B06FFAC
- Faction override:  {}
- Instances:
  - MP_TeamDM0@2 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-587.4, 103.2, -225.9] in boxes[] polys[1]
  - MP_TeamDM0@5 TelemetryArea key=-1 None pos=[-554.9, 105.7, -150.3] in boxes[] polys[3]
  - MP_TeamDM0@6 TelemetryArea key=-1 None pos=[-653.2, 102.5, -191.3] in boxes[] polys[2]
  - MP_TeamDM0@15 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-727.1, 129.7, 17.5] in boxes[] polys[]
  - MP_TeamDM0@19 Insertion key=7 Insertion_Chaotic_Arrival_v2 pos=[-660.6, 108.7, -118.0] in boxes[] polys[2]
  - MP_TeamDM0@21 TelemetryArea key=-1 None pos=[-620.6, 101.8, -220.3] in boxes[] polys[1]
  - MP_TeamDM0@25 Sector key=-1 Sector pos=[-595.7, 104.7, -156.3] in boxes[] polys[3]
  - MP_TeamDM0@30 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-656.3, 108.1, -123.3] in boxes[] polys[2]
  - MP_TeamDM0@33 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[-584.2, 103.4, -222.0] in boxes[] polys[1]
- Areas:
  - POLY7@1 (TeamDeathMatch_Global) bbox=[-674, -294, -547, -153] contains ['Insertion#3@2', 'TelemetryArea@21', 'Insertion#5@33']
  - POLY8@2 (TeamDeathMatch_Global) bbox=[-718, -257, -601, -86] contains ['TelemetryArea@6', 'Insertion#7@19', 'Insertion#3@30']
  - POLY10@3 (TeamDeathMatch_Global) bbox=[-652, -247, -494, -66] contains ['TelemetryArea@5', 'Sector@25']
- Notes: Layout: single. Play area = three polygons of TeamDeathMatch_Global: POLY7@1 127 x 141, POLY8@2 117 x 171, POLY10@3 158 x 181 (x -652..-494, z -247..-66); union x -718..-494, z -294..-66 = 224 x 228 m. Insertions: 2 in POLY@1 (south), 2 in POLY@2 (west; one is Chaotic_Arrival_v2). Sector@25 in POLY@3 (east). AlternateSpawnArea@15 at (-727.1, 129.7, 17.5) is 84 m beyond the +z edge of the union and 9 m west of it, and about 25 m above the rest (y about 104): misplaced or a deliberate high spawn.

### Saints Quarter (MP_LIMESTONE)

- Layer assets: MP_TeamDM0, MP_TeamDM0_Schematic, TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, generated/DD_MP_TeamDM0_Schematics, generated/DD_MP_TeamDM0_Volumes
- Faction override:  {}
- Instances:
  - MP_TeamDM0@6 TelemetryArea key=-1 None pos=[290.2, 64.5, 98.3] in boxes[] polys[]
  - MP_TeamDM0@7 TelemetryArea key=-1 None pos=[328.9, 71.4, 134.4] in boxes[] polys[]
  - MP_TeamDM0@8 TelemetryArea key=-1 None pos=[335.1, 80.8, 100.2] in boxes[] polys[]
  - MP_TeamDM0@9 TelemetryArea key=-1 None pos=[371.1, 64.9, 101.8] in boxes[] polys[]
  - MP_TeamDM0@10 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[280.8, 66.6, 93.9] in boxes[] polys[]
  - MP_TeamDM0@12 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[331.5, 81.0, 101.6] in boxes[] polys[]
  - MP_TeamDM0@20 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[383.5, 66.6, 105.6] in boxes[] polys[]
  - MP_TeamDM0@27 Insertion key=4 Insertion_Cautious_OnSpot_v2 pos=[368.3, 62.7, 82.0] in boxes[] polys[]
  - MP_TeamDM0@30 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[280.9, 68.2, 115.4] in boxes[] polys[]
  - MP_TeamDM0@32 Sector key=-1 Sector pos=[330.1, 81.0, 101.7] in boxes[] polys[]
- Areas:
- Notes: Layout: single. No box/polygon. Footprint implied by instances only: Insertions x 281..384, z 82..115 (103 x 33), 4 TelemetryAreas x 290..371, z 98..134. Sector@32 (330.1,101.7) and ASA@12 (331.5,101.6) are 1.4 m apart at its centre. Variants OnSpot_v1 x3 and OnSpot_v2. Sector/ASA y=81 vs Insertions y 62-68. MUT_Limestone is empty.

### New Sobek City (MP_OUTSKIRTS)

- Layer assets: TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, generated/DD_MP_TeamDM0_Schematics, generated/DD_MP_TeamDM0_Volumes, MP_TeamDM0, MP_TeamDM0_Schematic
- Faction override:  {}
- Instances:
  - MP_TeamDM0@2 TelemetryArea key=-1 None pos=[45.3, 95.4, -74.6] in boxes[] polys[5]
  - MP_TeamDM0@7 Insertion key=0 Insertion_Cautious_Arrival pos=[-70.7, 95.7, -50.2] in boxes[4] polys[]
  - MP_TeamDM0@10 TelemetryArea key=-1 None pos=[-28.2, 95.8, -79.7] in boxes[4] polys[]
  - MP_TeamDM0@13 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-73.3, 95.8, -53.6] in boxes[4] polys[]
  - MP_TeamDM0@16 Sector key=-1 Sector pos=[-297.7, 92.9, 70.6] in boxes[] polys[]
  - MP_TeamDM0@19 TelemetryArea key=-1 None pos=[-102.7, 94.8, -71.0] in boxes[] polys[2]
  - MP_TeamDM0@20 Sector key=-1 Sector pos=[-120.2, 98.3, 31.3] in boxes[] polys[]
  - MP_TeamDM0@21 TelemetryArea key=-1 None pos=[-31.0, 94.8, -129.9] in boxes[] polys[1]
  - MP_TeamDM0@25 Insertion key=1 Insertion_Cautious_Arrival_Corner pos=[19.5, 95.1, -79.8] in boxes[4] polys[]
  - MP_TeamDM0@26 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-120.2, 98.3, 31.3] in boxes[] polys[]
  - MP_TeamDM0@30 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[14.6, 95.1, -73.8] in boxes[4] polys[]
  - MP_TeamDM0@32 TelemetryArea key=-1 None pos=[-28.0, 96.7, -20.8] in boxes[3] polys[]
  - MP_TeamDM0@40 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-120.2, 98.3, 31.3] in boxes[] polys[]
- Areas:
  - BOX@3 (TeamDeathMatch_Global) bbox=[-79, -49, 23, 4] contains ['TelemetryArea@32']
  - BOX@4 (TeamDeathMatch_Global) bbox=[-79, -109, 23, -47] contains ['Insertion#0@7', 'TelemetryArea@10', 'Insertion#3@13', 'Insertion#1@25', 'Insertion#3@30']
  - POLY5@1 (TeamDeathMatch_Global) bbox=[-79, -159, 22, -109] contains ['TelemetryArea@21']
  - POLY6@2 (TeamDeathMatch_Global) bbox=[-138, -155, -79, 4] contains ['TelemetryArea@19']
  - POLY6@5 (TeamDeathMatch_Global) bbox=[22, -159, 69, 2] contains ['TelemetryArea@2']
- Notes: Layout: single, but with duplicate modules: 2 Sectors, 2 AlternateSpawnAreas. No combat-area polygon. Telemetry/global shapes: BOX@3 102 x 53, BOX@4 102 x 62, POLY5@1 101 x 50, POLY6@2 59 x 159, POLY6@5 47 x 161; union x -138..69, z -159..4 = 207 x 163 m. All 4 Insertions are in BOX@4 (x -73..20, z -80..-50): a single cluster, unlike other maps with two ends. Sector@16 at (-297.7, 92.9, 70.6); Sector@20, ASA@26, ASA@40 at default (-120.2, 98.3, 31.3) (y 98.3 here); all outside the shapes.

### Vegas Strip (MP_PARADISE)

- Layer assets: TeamDeathMatch, TeamDeathMatch_Global_Schematic, MP_TeamDM0, MP_TeamDM0_Schematic, TeamDeathMatch_Global, generated/AG_TeamDeathMatch_DynamicDD_Schematic_E1E21C68, generated/AG_TeamDeathMatch_DynamicDD_boxes_4B06FFAC
- Faction override:  {}
- Instances:
  - MP_TeamDM0@6 Sector key=-1 Sector pos=[-52.5, 64.0, 0.0] in boxes[] polys[]
  - MP_TeamDM0@7 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-122.2, 49.8, 210.2] in boxes[] polys[14]
  - MP_TeamDM0@10 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-121.4, 49.8, 206.2] in boxes[] polys[14]
  - MP_TeamDM0@16 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-71.4, 49.8, 52.2] in boxes[] polys[14]
  - MP_TeamDM0@23 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-68.5, 49.8, 49.9] in boxes[] polys[14]
  - MP_TeamDM0@24 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-52.5, 64.0, 0.0] in boxes[] polys[]
- Areas:
  - POLY51@14 (MP_TeamDM0) bbox=[-233, 30, -27, 242] contains ['Insertion#3@7', 'Insertion#3@10', 'Insertion#3@16', 'Insertion#3@23']
- Notes: Layout: single. Play area: POLY51@14 x -233..-27, z 30..242 = 206 x 212 m. Insertions (all OnSpot_v1): 2 at (-122,208), 2 at (-70,51), ends about 165 m apart along z. Sector@6 and ASA@24 at (-52.5, 64, 0) (same stub value as Area 51), outside the polygon by 30 m in z.

### Cairo Bazaar (MP_PLAZA)

- Layer assets: TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, MP_TeamDM0, MP_TeamDM0_Schematic, generated/AG_TeamDeathMatch_DynamicDD_Schematic_E1E21C68, generated/AG_TeamDeathMatch_DynamicDD_boxes_4B06FFAC
- Faction override:  {"team1": "Alliance/NATO", "team2": "Coalition/Pax Armata"}
- Instances:
  - MP_TeamDM0@1 Sector key=-1 Sector pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - MP_TeamDM0@9 SpecialCombatArea key=-1 None pos=[20.0, 67.2, 93.2] in boxes[] polys[]
  - MP_TeamDM0@13 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[-79.2, 64.4, -86.9] in boxes[] polys[]
  - MP_TeamDM0@14 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[20.2, 65.3, 39.3] in boxes[] polys[]
  - MP_TeamDM0@16 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-72.0, 64.4, -88.5] in boxes[] polys[]
  - MP_TeamDM0@17 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - MP_TeamDM0@20 Insertion key=15 Insertion_Cautious_OnSpot_v4_NOT_FOR_REVEAL pos=[23.8, 65.9, 48.8] in boxes[] polys[]
- Areas:
- Notes: Layout: single. SpecialCombatArea@9 at (20.0, 67.2, 93.2); no box/polygon stored. Footprint implied by instances: Insertions x -79..24, z -88.5..48.8 (103 x 137). Ends: 2 near (-75,-88) and 2 near (22,44), about 164 m apart. Sector@1 and ASA@17 at the shared default (-120.2, 65.9, 31.3). Insertion key 15 (NOT_FOR_REVEAL) is used. Team 1 = NATO (= default, explicitly set).

### Hagental Base (MP_SUBSURFACE)

- Layer assets: TeamDM0, TeamDM0_Schematic, TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, generated/AG_TeamDeathMatch_DynamicDD_Schematic_E1E21C68, generated/AG_TeamDeathMatch_DynamicDD_boxes_4B06FFAC
- Faction override:  {}
- Instances:
  - TeamDM0@1 Insertion key=4 Insertion_Cautious_OnSpot_v2 pos=[251.1, 64.6, -115.9] in boxes[2] polys[21]
  - TeamDM0@3 SpecialCombatArea key=-1 None pos=[-87.1, 64.0, -57.1] in boxes[] polys[]
  - TeamDM0@7 TelemetryArea key=-1 None pos=[96.6, 66.3, 97.7] in boxes[] polys[]
  - TeamDM0@13 Sector key=-1 Sector pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - TeamDM0@15 TelemetryArea key=-1 None pos=[89.5, 66.3, 97.7] in boxes[] polys[]
  - TeamDM0@16 TelemetryArea key=-1 None pos=[92.6, 66.3, 97.7] in boxes[] polys[]
  - TeamDM0@17 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[254.8, 64.6, -108.2] in boxes[2] polys[21]
  - TeamDM0@23 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-120.2, 65.9, 31.3] in boxes[] polys[]
  - TeamDM0@27 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[142.7, 67.1, -26.9] in boxes[] polys[21, 1]
  - TeamDM0@29 TelemetryArea key=-1 None pos=[-125.6, 64.0, 100.0] in boxes[] polys[]
  - TeamDM0@30 Insertion key=4 Insertion_Cautious_OnSpot_v2 pos=[137.9, 67.1, -27.1] in boxes[] polys[21, 1]
- Areas:
  - BOX@2 (TeamDeathMatch_Global) bbox=[178, -151, 315, -14] contains ['Insertion#4@1', 'Insertion#3@17']
  - POLY12@21 (TeamDM0) bbox=[102, -163, 288, 12] contains ['Insertion#4@1', 'Insertion#3@17', 'Insertion#3@27', 'Insertion#4@30']
  - POLY5@1 (TeamDeathMatch_Global) bbox=[98, -67, 216, 12] contains ['Insertion#3@27', 'Insertion#4@30']
  - POLY6@3 (TeamDeathMatch_Global) bbox=[99, -174, 264, -67] contains []
- Notes: Layout: single (layer named TeamDM0). SpecialCombatArea@3 at (-87.1, 64, -57.1), outside every shape. Play area: POLY12@21 x 102..288, z -163..12 = 186 x 175 m; Global shapes BOX@2 137 x 137, POLY5@1 118 x 79, POLY6@3 165 x 107; union 217 x 186. Insertions: 2 near (253,-112) (east, BOX@2) and 2 near (140,-27) (south-west, POLY5@1), about 141 m apart. POLY6@3 (99..264, -174..-67) contains nothing. Sector@13 and ASA@23 at the shared default (-120.2, 65.9, 31.3). TelemetryAreas @7,@15,@16 within 7 m of each other near (93, 98) and @29 at (-125.6,100), all outside the polygon.

### Mirak Valley (MP_TUNGSTEN)

- Layer assets: MP_TeamDM0, MP_TeamDM0_Schematic, TeamDeathMatch, TeamDeathMatch_Global, TeamDeathMatch_Global_Schematic, TeamDeathMatch_Telemetry, generated/DD_MP_TeamDM0_Schematics, generated/DD_MP_TeamDM0_Volumes
- Faction override:  {}
- Instances:
  - MP_TeamDM0@3 Sector key=-1 Sector pos=[-1.2, 86.0, -349.1] in boxes[1, 2] polys[12]
  - MP_TeamDM0@4 AlternateSpawnArea key=-1 AlternateSpawnArea pos=[-12.0, 80.9, -377.0] in boxes[] polys[12]
  - MP_TeamDM0@7 TelemetryArea key=-1 None pos=[0.6, 87.3, -343.0] in boxes[1, 2] polys[12]
  - MP_TeamDM0@19 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[-48.7, 86.1, -309.7] in boxes[1, 2] polys[12]
  - MP_TeamDM0@25 Insertion key=4 Insertion_Cautious_OnSpot_v2 pos=[4.9, 86.1, -338.3] in boxes[1, 2] polys[12]
  - MP_TeamDM0@26 TelemetryArea key=-1 None pos=[-24.5, 91.2, -330.0] in boxes[1, 2] polys[12]
  - MP_TeamDM0@29 Insertion key=5 Insertion_Cautious_OnSpot_v3 pos=[-52.3, 86.1, -316.3] in boxes[1, 2] polys[12]
  - MP_TeamDM0@31 Insertion key=3 Insertion_Cautious_OnSpot_v1 pos=[6.2, 86.1, -329.5] in boxes[1, 2] polys[12]
  - MP_TeamDM0@34 TelemetryArea key=-1 None pos=[-8.1, 86.4, -308.1] in boxes[1, 2] polys[12]
  - MP_TeamDM0@35 Sector key=-1 Sector pos=[-1.7, 86.0, -350.9] in boxes[1, 2] polys[12]
- Areas:
  - BOX@1 (TeamDeathMatch_Telemetry) bbox=[-69, -368, 21, -290] contains ['Sector@3', 'TelemetryArea@7', 'Insertion#3@19', 'Insertion#4@25', 'TelemetryArea@26', 'Insertion#5@29', 'Insertion#3@31', 'TelemetryArea@34', 'Sector@35']
  - BOX@2 (TeamDeathMatch_Telemetry) bbox=[-69, -368, 21, -290] contains ['Sector@3', 'TelemetryArea@7', 'Insertion#3@19', 'Insertion#4@25', 'TelemetryArea@26', 'Insertion#5@29', 'Insertion#3@31', 'TelemetryArea@34', 'Sector@35']
  - POLY35@12 (MP_TeamDM0) bbox=[-81, -387, 45, -281] contains ['Sector@3', 'AlternateSpawnArea@4', 'TelemetryArea@7', 'Insertion#3@19', 'Insertion#4@25', 'TelemetryArea@26', 'Insertion#5@29', 'Insertion#3@31', 'TelemetryArea@34', 'Sector@35']
- Notes: Layout: single. 2 Sectors (@3 and @35, 1.8 m apart) and 2 identical boxes BOX@1 = BOX@2 (-69..21, -368..-290 = 90 x 78): duplicated instances. Play area: POLY35@12 x -81..45, z -387..-281 = 126 x 106 m (smallest of all maps). ASA@4 at (-12.0, -377.0) is inside the polygon near the south edge, 9 m beyond the boxes. Insertions: 4 in a tight group x -52..6, z -338..-310 (OnSpot v1 x2, v2, v3).

## 3. Cross-map table

Play-area size = width (x) x depth (z) of the inferred play area, metres. "Shapes" notes where it is a union of telemetry/global shapes instead of one polygon.

| Map | Layouts | Play area (x by z) | Source | Spawn areas (ASA) | Insertions | Sector |
|---|---|---|---|---|---|---|
| Siege of Cairo | 1 | 142 x 91 | POLY27@16 | 1, inside (-163,69) | 4 | 1 |
| Empire State | 1 | 188 x 181 | POLY61@12 | 1, on rim (-556,-31) | 4 | 1 |
| Wake Island | 1 | 288 x 214 (3 boxes ~125 x 205) | shapes | 1, inside (305,-96) | 4 | 1 |
| Blackwell Fields | 1 | none stored | - | 1 at default placeholder | 4 | 1 (default) |
| Iberian Offensive | 1 | 99 x 106 (union 165 x 134) | BOX@3 / shapes | 1, = Sector (757,87) | 0 | 1 |
| Liberation Peak | 1 | 215 x 140 | POLY60@10 | 1 at default placeholder | 4 | 1 (default) |
| Contaminated | 1 | 166 x 133 | POLY16@10 | 1 at default placeholder | 4 | 1 |
| Area 51 | 1 | none (stub data) | - | 1 at stub (-52.5,0) | 4 | 1 (stub) |
| Manhattan Bridge | 1 | 187 x 158 (box 236 x 197) | POLY47@16 | 1, inside (-11,-273) | 4 | 1 |
| Eastwood | 1 | 201 x 178 | shapes | 1 at default placeholder | 4 | 1 (default) |
| Operation Firestorm | 1 | 152 x 155 | POLY55@31 | 1 at default placeholder | 4 | 1 (default) |
| Railway to Golmud | none | none | - | 0 | 0 | 0 |
| Tsuru Reef | 1 | 224 x 228 (3 polys ~125 x 165) | shapes | 1 at (-727,17), outside | 4 | 1 |
| Saints Quarter | 1 | none (instances span ~103 x 52) | - | 1, = Sector (332,102) | 4 | 1 |
| New Sobek City | 1 (duplicate modules) | 207 x 163 | shapes | 2 at default placeholder | 4 | 2 |
| Vegas Strip | 1 | 206 x 212 | POLY51@14 | 1 at stub (-52.5,0), outside | 4 | 1 (stub) |
| Cairo Bazaar | 1 | none (instances span ~103 x 137) | - | 1 at default placeholder | 4 | 1 (default) |
| Hagental Base | 1 | 186 x 175 (union 217 x 186) | POLY12@21 | 1 at default placeholder | 4 | 1 (default) |
| Mirak Valley | 1 | 126 x 106 | POLY35@12 | 1, inside (-12,-377) | 4 | 2 |

By area, smallest to largest: Siege of Cairo 12,922 m2, Mirak Valley 13,356, Contaminated 22,078, Operation Firestorm 23,560, Liberation Peak 30,100, Hagental Base 32,550, Empire State 34,028, Manhattan Bridge 29,546 (polygon), Vegas Strip 43,672; union-only maps Eastwood 201 x 178, New Sobek City 207 x 163, Tsuru Reef 224 x 228, Wake Island 288 x 214 (largest). Iberian Offensive 99 x 106 box (union 165 x 134).

## 4. Open questions (instance indices)

1. Shared default position (-120.2, 65.9, 31.3): Sector/ASA on Blackwell Fields (Sector@15, ASA@29), Liberation Peak (ASA@3, Sector@29), Contaminated (ASA@24 only), Eastwood (Sector@25, ASA@27), Operation Firestorm (ASA@1, Sector@25), Cairo Bazaar (Sector@1, ASA@17), Hagental Base (Sector@13, ASA@23); New Sobek City (Sector@20, ASA@26, ASA@40) with y 98.3. Identical coordinates across unrelated maps mean the spawn areas are not placed by position here. Is the Sector/ASA centre unused (spawn areas defined by the shapes instead) or is the instance transform just not exported? The data does not say.
2. Area 51 (Sector@5, ASA@2, Insertions @1 @3 @4 @6) and Vegas Strip (Sector@6, ASA@24): stub (-52.5, 64, 0). Area 51 has no shape and key=-1 for all insertions; is TDM on Area 51 a real layout? Vegas Strip has a real polygon (POLY51@14) and real insertions, so only its Sector/ASA are stubs.
3. Iberian Offensive has no Insertion (gem counts list none) and no placed insertion variant: what arrival animation does it use? (Sector@3, ASA@5 coincide.)
4. Railway to Golmud has only MP_TeamDM0_Schematic and no instances: is Team Deathmatch absent on that map?
5. Tsuru Reef ASA@15 at (-727.1, 129.7, 17.5) is outside the play area shapes and 25 m higher: intended?
6. New Sobek City: 2 Sectors and 2 ASAs. Sector@16 (-297.7, 70.6) is far outside; ASA@26 and ASA@40 are identical. Duplicate or two spawn regions (ASA@40 as the swap target)? Same for Mirak Valley Sector@3 and Sector@35 (1.8 m apart, one layout; BOX@1 = BOX@2).
7. Play area: no CombatArea instance in any map. Is the combat area the MP_TeamDM0 polygon (Siege of Cairo POLY27@16, Empire State POLY61@12, Liberation Peak POLY60@10, Contaminated POLY16@10, Manhattan Bridge POLY47@16, Operation Firestorm POLY55@31, Vegas Strip POLY51@14, Hagental Base POLY12@21, Mirak Valley POLY35@12)? Maps without such a polygon (Wake Island, Eastwood, Tsuru Reef, New Sobek City, Iberian Offensive) rely on Telemetry/Global shapes; Blackwell Fields, Area 51, Saints Quarter, Cairo Bazaar have none stored (the combat area probably comes from a shared or level-wide layer not in this extract).
8. SpecialCombatArea on Manhattan Bridge (@14), Cairo Bazaar (@9), Hagental Base (@3): no shape attached, position only; Hagental Base's lies outside every shape. Purpose (vehicle/air OOB?) not shown.
9. Team sides: factionOverrides swap Pax Armata to team 1 on Siege of Cairo, Blackwell Fields, Iberian Offensive; Eastwood and Cairo Bazaar set the default explicitly. Nothing says which team uses which Insertion pair.
10. Unused data: Insertion_Event (Airstrike, JetStraight) and Insertion keys 2, 9-14, 16-18 are defined but unused; TDM_fRoundTime unit, TDM_iOutOfBounds_TimeToReturn unit, XP values not in the files.
11. Hardcore Team Deathmatch string exists; no separate hardcore tweakables are in the TDM file.
