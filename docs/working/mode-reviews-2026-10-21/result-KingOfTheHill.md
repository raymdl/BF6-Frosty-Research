# King of the Hill - build 2.1.1.0 data analysis

Source: KingOfTheHill-maps.txt, -tweakables.txt, ui-text.txt, objective-table.json, map-names.json, maps-tweakables.txt. Counts and extents computed with a script from the maps file.

## 1. Mode rules

### MUT_KOTH (50 tweakables; client defaults, a server playlist can override). Format: value [min..max]
Most ranges are stored as [0..0] or [0.0..0.0], which means "no range stored", not "fixed at 0". Only two have a real range.

| Tweakable | Value | UI confirms? |
|---|---|---|
| KOTH_iTargetScore (points target) | 250 | Yes: "First team to reach points target wins" (no number in UI) |
| KOTH_fScoreDelay (score tick interval; read as seconds between point awards, inference) | 1.0 | Partly: "gradually earns the occupying team points" |
| KOTH_fObjectiveActiveTime (hill duration / rotation time) | 90.0 | Yes: "New objectives become available after a set time" (no number) |
| KOTH_fInitialObjUnlockTime (first hill unlock) | 20.0 | No |
| KOTH_fRevealNextObjTime (next hill revealed in advance) | 10.0 | No (UI: objective "relocates") |
| KOTH_fRoundTime | 15.0 | UI: "most points when the time expires" confirms a time limit exists. 15.0 is probably minutes (inference; unit not in data) |
| KOTH_fCaptureTime | 0.0 | No (zero = instant) |
| KOTH_fNeutralizationTime | 0.0 | No |
| KOTH_bCaptureOnNeutralized | true | No |
| KOTH_bNeutralizeIfNoPlayers | true | No |
| KOTH_bNeutralizationIgnoresMajority | true | No |
| KOTH_fPlayerRespawnDelay / Team1RespawnDelay / Team2RespawnDelay | 0.0 / 0.0 / 0.0 | No |
| KOTH_iPlayerMaxSpawnCount | -1 (unlimited) | No |
| KOTH_iOutOfBounds_TimeToReturn | 5 | No |
| KOTH_bAllowVehicles | false | No |
| KOTH_iBigLeadThreshold | 50 | No |
| KOTH_fUrgencyPercentageThreshold / KOTH_fUrgencyTimeThreshold | 0.12 / 30.0 | No |
| KOTH_iLobbyPlayerCountStartTimer / ...ToSpeedUpTimer | 16 / 16 | No |
| KOTH_iAreaSwapScoreThreshold | -10 | No (spawn-area swap logic, inference) |
| Spawn scoring: PrimarySpawnScore 3; FriendlyProximityNearScore 1 (radius 0..20); EnemyProximityNearScore -20 (0..20); EnemyProximityFarScore -2 (20.1..40); PreviousDeathProximityScore -20 (0..20); RecentlyUsedScore -1, RecentlyUsedDuration 3.0 | as listed | No |
| KOTH_bEnableOrders true; bAllowQuickRespawnBeaconDeploy false; bSoldierBleedoutOnSquadWipe false; iSoldierMandownType 1; bTacticalAdviceEnabled false; iCommanderVoice -1 | as listed | No |
| KOTH_fAudioFalloffDistanceToObjective | 1.0 [1.0..200.0] (real range) | No |
| KOTH_fNoInteractivityTimeoutOverride | 60.0 [0.0..600.0] (real range) | No |
| Class "Recommended" flags (Assault, Engineer, Support, Recon) | all false | No |

- Not found in MUT_KOTH: points per second held (only the 1.0 ScoreDelay tick; the points added per tick is not named), a sequence/random-order setting, any XP value.
- Per-map MUT files (maps-tweakables.txt) hold only Conquest initial scores (1200), a Dumbo vehicle OOB time and similar; no KOTH values.
- A "HARDCORE KING OF THE HILL" title exists in the UI text; no hardcore-specific KOTH tweakables are in the file.

### GME_Sim_KOTH_Round (83 objects, 6 named variables, all null defaults)
LastTeam, SpecifiedCapturePoint(Objective), TargetScore, ActivityStateMachine, MI_Sim_GameMode, WinningTeam. No numbers; the logic reads TargetScore from MUT_KOTH and tracks the active CapturePoint ("SpecifiedCapturePoint"). GME_Pres_KOTH_Round has only MI_Pres_GameMode; GM_KOTH_LaunchFunction has LaunchParameters/ActivityParameters (null). Shared SimEx_CaptureVolume has SoldiersOnPoint, AllSoldiersOnPoint, SoldiersExitedPoint, SoldiersDeadOrExited, AllVehiclesOnPoint (all null).

### UI text
"Battle for control over multiple objectives that activate across the combat area." "Fight the enemy to capture and hold an objective that relocates across the map." "New objectives become available after a set time." "First team to reach points target wins." Loading tip: "Controlling the objective gradually earns the occupying team points"; "Win by reaching the points target first or by having most points when the time expires". Confirmed: single relocating objective, timed activation, points target, time-expiry tiebreak. UI states no numbers.

### AD_Objective_KOTH capture point variants
GEM_CapturePoint: default GMPF_CapturePoint_NoRepresentation; key 1 = GMPF_CapturePoint_OneTimeUse. Other entries: Sector (GMPF_Sector), PhaseBasedSpawnArea, CapturePoint_OutlineArea (GMPF_OutlineArea), CapturePoint_Proxy, Insertion (keys 0-18), vehicle/stationary spawners, reinforcement.
Anomaly: every placed KOTH CapturePoint has key=-1 and resolves to the name GMPF_CapturePoint, which is neither table prefab. So the layers do not match the table names; which prefab the live hills use is unclear. No hill uses key 1 (OneTimeUse).

## 2. Per map

Result: 10 maps carry KOTH instances; Mirak Valley has a layer asset but no instances; Wake Island, Contaminated and Cairo Bazaar have no KOTH layer. Not in this extraction at all: Area 51, Railway to Golmud, Vegas Strip, Hagental Base, Tsuru Reef and the Portal maps. The expected 14 maps with two lowercase 'koth' folders is not reproduced (no lowercase koth asset; all layer assets are MP_KOTH0). See open questions.

Common to all populated maps: layer MP_KOTH0 (+ MP_KOTH0_Schematic; Eastwood has none), 5 CapturePoints (key -1, GMPF_CapturePoint), 1 Sector, 4 Insertions, 1 Gem_PhaseBasedSpawnArea (Manhattan Bridge 2), no faction or named overrides. The Sector is a point (no box). Instance ids scatter with no spatial pattern, so the data does not order the hills. "Play area" = largest polygon containing the Sector (bbox only; the real shape is irregular, so this is an upper bound). Hill ids are indices in MP_KOTH0.

### Siege of Cairo (MP_ABBASID): MP_KOTH0, MP_KOTH0_schematic, MeshVariationDb_Win32; 12 TelemetryAreas
Hills: @3 [-155.8,66.7,49.8] (box 86/poly 45); @18 [-167.8,65.4,117.3] (poly 27); @43 [-173.7,64.8,-24.9] (poly 90); @54 [-205.2,67.1,60.0] (poly 94/5); @98 [-166.3,64.0,13.7] (box 26). No OutlineAreas. Sector @8 [-126.1,65.9,36.8] in poly 39 (43x79). Play area POLY78@105 bbox [-256,-82,-94,130] = 162x212. Hill spread 49x142 (north-south line).

### Empire State (MP_AFTERMATH): MP_KOTH0, MP_KOTH0_Schematic, staticmodelgroup.physics; 9 Telemetry
Hills: @7 [-578.5,64.2,21.8]; @13 [-601.4,55.5,-29.3]; @19 [-656.4,63.4,-18.6]; @69 [-653.0,54.6,34.4]; @72 [-554.2,58.7,-32.2]. No OutlineAreas. Sector @118 [-602.8,57.2,9.0]. Play area POLY89@30 [-708,-139,-507,141] = 201x280. Hill spread 102x67; hill heights vary 55-64.

### Blackwell Fields (MP_BADLANDS): MP_KOTH0, MP_KOTH0_Schematic; no Telemetry
Hills: @23 [301.4,75.4,-89.4] (box 13, 7x16); @32 [259.5,75.4,-86.0] (box 5, 16x11); @36 [314.5,75.4,-128.7] (box 31, 7x14); @65 [231.9,75.4,-98.5] (box 43, 13x9); @78 [230.9,75.4,-39.6] (box 15, 18x7). Each hill sits in its own small box. No OutlineAreas. Sector @49 [249.6,75.4,-83.7] in no polygon. No play-area polygon. Spread 84x89. All y = 75.4 (unusual).

### Iberian Offensive (MP_BATTERY): MP_KOTH0, MP_KOTH0_Schematic; 3 Telemetry; 4 OutlineAreas
Hills: @27 [756.2,82.0,175.7] (poly 10, no outline); @55 [723.7,79.1,174.2] (poly 37, outline @53); @64 [693.1,74.6,132.2] (poly 31, outlines @1 and @32); @79 [728.1,76.0,146.4] (poly 87, outline @25); @85 [732.7,77.0,116.3] (poly 61, no outline). Sector @28 [725.7,88.0,132.6] in no polygon. No play-area polygon. Spread 63x59. Outline pairing is by shared polygon (inference).

### Liberation Peak (MP_CAPSTONE): MP_KOTH0, MP_KOTH0_Schematic; 5 Telemetry
Hills: @36 [138.6,133.9,112.0]; @59 [101.8,131.3,44.8]; @71 [146.2,129.9,59.8]; @86 [60.8,137.8,98.6]; @90 [108.8,133.4,83.5] (poly 20, 25x20). No OutlineAreas. Sector @5 [99.4,133.3,78.4], about 10 m from hill @90. Play area POLY54@38 [-35,0,232,172] = 267x172. Spread 85x67.

### Manhattan Bridge (MP_DUMBO): MP_KOTH0, MP_KOTH0_EcsPrefab_ecsPrefab (only map with it), MP_KOTH0_Schematic; 6 Telemetry; 2 PhaseBasedSpawnAreas; 1 SpecialCombatArea
Hills: @9 [-5.6,61.6,-398.3] (box 16/poly 76); @73 [-17.9,55.2,-304.3]; @83 [0.5,57.4,-222.1] (box 30); @106 [-29.7,55.0,-322.7] (boxes 10, 112); @109 [-34.3,64.0,-259.2] (box 71). OutlineArea @87 [-30.1,56.7,-323.4] pairs with @106 (box 112, 24x20). Sector @80 [-41.2,62.1,-345.2] sits in box 10 (73x75), the same box as SpecialCombatArea @21; play area POLY35@58 [-138,-437,115,-166] = 253x271. Spread 35x176 (line along z).

### Eastwood: MP_KOTH0, MeshVariationDb_Win32 (no Schematic); no Telemetry
Hills: @13 [76.5,233.1,-30.3] (box 3); @37 [35.2,234.3,-12.5] (box 7); @49 [106.5,229.3,24.7] (poly 2); @54 [75.8,234.3,15.1] (no container); @83 [48.0,234.3,41.5] (box 80). No OutlineAreas. Sector @26 [788.7,77.0,94.9] is about 700 m from the hills and at y 77 vs hills at y 229-234: inconsistent. No play-area polygon. Spread 71x72.

### Operation Firestorm (MP_FIRESTORM): MP_KOTH0, MP_KOTH0_Schematic; 5 Telemetry; 9 OutlineAreas
Hills: @55 [-146.4,125.0,-59.6] (poly 79, no outline); @57 [-67.8,125.0,-122.2] (box 12; outlines @29,@40,@118); @58 [-110.4,125.0,-132.2] (box 32; outlines @52,@94); @62 [-85.1,125.0,-76.7] (poly 109; outline @64); @76 [-157.5,124.9,-117.7] (poly 87; outlines @1,@31,@85). Sector @114 [-111.3,124.8,-99.9]. Play area POLY10@81 [-237,-213,0,18] = 237x231. Spread 90x73. Up to 3 outlines per hill (purpose unknown).

### Saints Quarter (MP_LIMESTONE): MP_KOTH0, MP_KOTH0_Schematic; 4 Telemetry; 1 OutlineArea
Hills: @8 [294.8,64.5,96.6] (poly 52); @10 [239.0,66.5,105.6] (no container); @60 [370.6,64.1,96.1] (poly 16; outline @62); @70 [337.2,65.8,104.0] (poly 45); @71 [329.1,69.5,131.2] (poly 49, shared with Sector). Sector @55 [336.6,69.1,134.4] in poly 49 (17x21), 3.4 m from hill @71. No large play-area polygon. Spread 132x35 (east-west).

### New Sobek City (MP_OUTSKIRTS): MP_KOTH0, MP_KOTH0_Schematic; 5 Telemetry; 3 OutlineAreas
Hills: @7 [8.6,96.2,-104.5] (poly 99); @63 [-52.1,96.0,-55.4] (poly 71; outlines @11,@57); @75 [-66.6,96.1,-113.8] (poly 36); @105 [62.6,96.3,-97.0] (poly 40); @107 [93.3,97.5,-54.1] (box 43; outline @53). Sector @13 [21.7,94.9,-122.2]. Play area POLY74@87 [-163,-181,168,11] = 331x192. Spread 160x60 (east-west).

### Mirak Valley (MP_TUNGSTEN)
Assets MP_KOTH0, MP_KOTH0_Schematic, MeshVariationDb_Win32 but gem counts {} and no instance lines. Hill count unknown.

### No KOTH layer in the data
Wake Island (MP_ATOLL), Contaminated, Cairo Bazaar (MP_PLAZA): only MeshVariationDb_Win32 (Contaminated also staticmodelgroup.physics). Area 51, Railway to Golmud, Vegas Strip, Hagental Base, Tsuru Reef: no block in this file (absence of a layer cannot be confirmed from this file; the brief says the first four lack one).

## 3. Cross-map table
Hills are always 5 where instances exist. Play area = largest polygon bbox containing the Sector; "-" = none found. Spread = bbox of the 5 hills.

| Map | Hills | Outlines | Play-area bbox (m) | Hill spread (m) |
|---|---|---|---|---|
| Siege of Cairo | 5 | 0 | 162 x 212 | 49 x 142 |
| Empire State | 5 | 0 | 201 x 280 | 102 x 67 |
| Blackwell Fields | 5 | 0 | - | 84 x 89 |
| Iberian Offensive | 5 | 4 | - | 63 x 59 |
| Liberation Peak | 5 | 0 | 267 x 172 | 85 x 67 |
| Manhattan Bridge | 5 | 1 | 253 x 271 | 35 x 176 |
| Eastwood | 5 | 0 | - | 71 x 72 |
| Operation Firestorm | 5 | 9 | 237 x 231 | 90 x 73 |
| Saints Quarter | 5 | 1 | - | 132 x 35 |
| New Sobek City | 5 | 3 | 331 x 192 | 160 x 60 |
| Mirak Valley | layer, no instances | ? | ? | ? |
| Wake Island, Contaminated, Cairo Bazaar | none | | | |
| Area 51, Railway to Golmud, Vegas Strip, Hagental Base, Tsuru Reef | not in extraction | | | |

Ordering: no map data orders the hills. Instance ids do not follow geography (Siege of Cairo hills by z: @43, @98, @3, @54, @18). No sequence/random tweakable exists, so selection is probably runtime logic around SpecifiedCapturePoint (inference, low confidence). If RoundTime 15.0 is minutes and ObjectiveActiveTime 90 s, a full round is about 10 activations over 5 hills (arithmetic on an unconfirmed unit).

## 4. Open questions
1. KOTH_fRoundTime = 15.0: unit (minutes?) and role; UI confirms only that a time limit exists.
2. Points awarded per KOTH_fScoreDelay tick (1.0) is not named; points per second held is not derivable. No XP tweakables in MUT_KOTH.
3. Hill order (random vs fixed) lives in GME_Sim_KOTH_Round (ActivityStateMachine, SpecifiedCapturePoint), not in the extracted data.
4. CapturePoint prefab mismatch: layers resolve to GMPF_CapturePoint (key -1); the table lists NoRepresentation (default) and OneTimeUse (key 1).
5. Eastwood Sector MP_KOTH0@26 at [788.7,77.0,94.9] vs hills at x 35-107, y ~230.
6. Mirak Valley: MP_KOTH0 present, 0 instances extracted.
7. Brief expects 14 KOTH maps incl. two lowercase 'koth' folders; the file has no lowercase koth asset (only MP_KOTH0_schematic in Siege of Cairo) and no blocks for Area 51, Railway to Golmud, Vegas Strip, Hagental Base, Tsuru Reef. Needs a rerun or other source.
8. Single-height hills: Blackwell Fields all y 75.4 (@23,@32,@36,@65,@78), Operation Firestorm y 125.0 (placeholder-like).
9. Duplicate outlines: Iberian Offensive @1/@32 for hill @64; Operation Firestorm @1/@31/@85 and @29/@40/@118.
10. No play-area polygon for Blackwell Fields, Iberian Offensive, Eastwood, Saints Quarter (CombatArea not among extracted modules).
