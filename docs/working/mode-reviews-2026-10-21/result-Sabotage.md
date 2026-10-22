# Sabotage, build 2.1.1.0 (Season 5)

Source: the `Sabotage/` work folder. Coordinates are metres; x/z is the map plane. Counts come from a parser script (`an.py`, in this folder) over `Sabotage-maps.txt`.

Correction to the brief: only 6 maps have a Sabotage layer, not 8. Together they hold 30+29+73+15+48+39 = 234 `GEM_Destructible`, which matches the stated total. Wake Island (MP_ATOLL) and Iberian Offensive (MP_BATTERY) appear in the extraction with only `MeshVariationDb_Win32` and no gameplay instances; counting those two gives the "8". The layer asset is always `MP_Sabotage0` (+ `MP_Sabotage0_Schematic`; Empire State, Blackwell Fields and Saints Quarter also carry `staticmodelgroup.physics`). There is no second or third layout layer. No faction overrides, no named overrides, and no per-map Sabotage tweakables (`maps-tweakables.txt` holds only Conquest scores, spawn radii, a Manhattan Bridge vehicle OOB time and Golmud trains).

## 1. Mode rules

### What the UI text states (`ui-text.txt`)
- Title "Sabotage". Short text: when attacking, destroy as many enemy equipment as possible; when defending, prevent the enemy from destroying the equipment.
- Long text: take turns in a race against the clock to destroy enemy equipment; attackers locate and destroy deployments of enemy equipment, defenders rally a defence and stop the attack.
- Round banners: "ATTACKER'S TURN - DESTROY EQUIPMENT" (first-round attacker: destroy all equipment before the time expires) and "DEFENDER'S TURN - STOP THE ENEMY ATTACK" (first-round defender: stop the enemy destroying all your equipment).
- A "HARDCORE SABOTAGE" string exists. Two entries are `<missing 01FAB882>` and `<missing 23BCBB70>`, so no text for them.
- Reading of the text: two teams, one attacking turn each, timed, the goal is equipment destroyed, with "all equipment" as the cap.

### MUT_Sabotage (68 tweakables)
Format is value and `[min..max]`. A range of `[0.0..0.0]` means the data declares no usable range, so it is unknown. "UI" marks whether the UI text confirms the concept. No number is confirmed by the UI text.

Timing and rounds
| Tweakable | Value | Range | UI confirms |
|---|---|---|---|
| SAB_fInitialRoundDuration | 6.0 | none | concept only (race the clock); unit not stated, minutes likely |
| SAB_fOvertimeDuration | 15.4 | none | no; unit not stated, seconds likely |
| SAB_fUrgencyTimeThreshold | 60.0 | none | no |
| SAB_fUrgencyPercentageThreshold | 0.2 | none | no |
| SAB_fNoInteractivityTimeoutOverride | 60.0 | 0..600 | no |
| SAB_iLobbyPlayerCountStartTimer | 16 | none | no |
| SAB_iLobbyPlayerCountToSpeedUpTimer | 16 | none | no |
| SAB_SetLateJoinerAfterFirstRound | true | bool | no |
| SAB_AllowLevelReset | true | bool | no |
| SAB_LayoutSelection | 1 | 0..2 | no. Only one layout layer (`MP_Sabotage0`) exists on every map |

There is no round-count tweakable. The UI view models carry `RoundCount` (null) and the crown layout has `IsRoundTwo` (true by default), so the mode is two rounds, one attack each, as the UI text's "first round" wording implies.

Equipment value and scoring
| Tweakable | Value | Range |
|---|---|---|
| SAB_SmallDestructibleValue | 1 | 1..open |
| SAB_MediumDestructibleValue | 1 | 1..open |
| SAB_LargeDestructibleValue | 1 | 1..open |
| SAB_fHealthThreshold | 0.75 | 0.0..1.0 |
| SAB_fDestructibleHealthModifier | 5.0 | 0.1..open |

Every destroyed piece is worth 1 point regardless of size, so score equals the number of targets destroyed. No time-bonus, per-kill score or XP tweakable exists among the 68. The UI view models carry time-taken and score-timestamp fields (below), so time looks like a tiebreak, not a bonus value. What SAB_fHealthThreshold gates is not shown.

Equipment (`VEH_GM_Destructible_<Size>.*`; sizes match `key` 0/1/2 = Small/Medium/Large)
| Property | Small | Medium | Large |
|---|---|---|---|
| MaxHealth [0..9999] | 100.0 | 250.0 | 500.0 |
| RegenerationDelay | 5.0 | 5.0 | 5.0 |
| RegenerationRate | 0.0 | 0.0 | 0.0 |
| RepairRateModifier | 0.5 | 0.5 | 0.5 |
| DisabledDamageThreshold | 0.0 | 0.0 | 0.0 |
| ClearDisabledDamageThreshold | 0.0 | 0.0 | 0.0 |
| Explosion InnerBlastRadius | 1.0 | 1.0 | 1.0 |
| Explosion BlastRadius | 5.0 | 5.0 | 5.0 |
| Explosion BlastDamage | 25.0 | 25.0 | 25.0 |
| Explosion ShockwaveRadius | 15.0 | 15.0 | 15.0 |
| Explosion ShockwaveDamage | 1.0 | 1.0 | 1.0 |
| Explosion DamageMultiplier | 1.0 | 1.0 | 1.0 |

Whether SAB_fDestructibleHealthModifier (5.0) multiplies MaxHealth (which would give 500 / 1250 / 2500) is not shown in the data and is unconfirmed. Regeneration rate 0 means no self-heal.

Respawn, out of bounds, soldier handling
| Tweakable | Value |
|---|---|
| SAB_fPlayerRespawnDelay | 12.0 |
| SAB_fTeam1RespawnDelay, SAB_fTeam2RespawnDelay | 0.0, 0.0 |
| SAB_iPlayerMaxSpawnCount | -1 (unlimited, inferred) |
| SAB_iSoldierOOBTimeToReturn | 5 (seconds, likely) |
| SAB_iSoldierMandownType | 1 |
| SAB_bSoldierBleedoutOnSquadWipe | false |

Objective HUD: SAB_bAllowObjectiveOverlay true; SAB_fAttackerObjectiveFarPlane 200.0 and SAB_fDefenderObjectiveFarPlane 200.0; SAB_fAttackerObjectiveYFOV 10.0; SAB_fDefenderObjectiveYFOV 40.0.

Other: SAB_iCommanderVoice 0. The four `<Class> Recommended` flags (Assault, Engineer, Support, Recon) are all false. XP: no XP value is in this data.

Not present despite the brief: round count, equipment count, time bonuses, per-destruction score beyond the three equal values, XP.

### Round graphs
`GME_Sim_Sabotage_Round` exposes only MI_Sim_GameMode, Result, ActivityStateMachine. `GME_Pres_Sabotage_Round` exposes MI_Pres_GameMode and MI_Pres_SpecificModeData. `GM_Sabotage_LaunchFunction` has LaunchParameters and ActivityParameters. All are null, so there are no numbers in them.

### Shared zone logic (`SimEx_DestructibleZone`, 8 objects)
Five named variables, all unset defaults: `SoldiersDeadOrExitedPoint`, `CurrentHealth`, `SoldiersOnPoint`, `OwningTeamInt`, `AttackerInside`. So a zone tracks its owning team, the current health of its equipment, who is in the zone, and whether an attacker is inside. No thresholds appear in the named values. The same extraction also lists capture, MCOM, sector spotting and reinforcement logic, which is shared and not Sabotage-specific.

### UI view models
- `MP_SabotageOutcome_ViewModelEx` (end of round): RoundCount, Midround_/EOR_ FriendlyScore and EnemyScore, FriendlyTimeRemaining and EnemyTimeRemaining, Midround_InitialTime, ScoreLabel and SecondaryScoreLabel, TargetSecondaryScore, EOR_FriendlyScoreTimestamps and EOR_EnemyScoreTimestamps (arrays, default empty), LocalPlayerIsAttacking. The outcome shows both teams' score, time remaining and when each point was scored.
- `MP_SabotageOutcome_ViewEx`: Outcome_FriendlyScore, Outcome_EnemyScore, Outcome_FriendlyTimeTaken, Outcome_EnemyTimeTaken, InitialTime, TargetScore, Midround_Score, Midround_Time, Midround_TimeLeft, IsEOR, LocalPlayerIsAttacking. Time taken per team supports time as a comparison value.
- `Sabotage_GMW_ScoreBarPoints_ViewModelEx`: MaximumSegments = 50, ScorePointSegmentCount, TeamPoints, TargetScore, AttackerScore, DefenderScore, FriendlyScore, EnemyScore, FriendlyColor, EnemyColor, IsLocalPlayerAttacking. The bar shows at most 50 segments.
- `Sabotage_GMW_CrownLayout_ViewEx`: SegmentSpacing = 4.0, IsRoundTwo = true, RightToLeft, ProgressBarLayoutSize, CrownTransform, IsCrownVisible, CrownColor, AttackerColor, DefenderColor, AttackerScore, DefenderScore, ScorePointSegmentCount. The crown marks a target score in round two (inferred from names).

## 2. Per-map data

Targets are `GEM_Destructible`. Variant key 0 = Small, 1 = Medium, 2 = Large (objective table). The data does not store which zone owns a target, so membership is inferred: each target goes to the zone it shares the smallest polygon or box with (ties by distance), checked against nearest-zone. "Container" is that smallest shared polygon or box. "Span" is the bbox of the member targets. HQ ownership and the attacking team are not stored.

### Siege of Cairo (MP_ABBASID): 30 targets, 3 zones, all Small
Assets: MP_Sabotage0, MP_Sabotage0_Schematic. 2 HQs, 1 Sector, 4 Insertions (keys 6, 6, 6, 8), no combat-area or telemetry instance.
| Zone | Targets | Container [minx,minz,maxx,maxz] | Span |
|---|---|---|---|
| @27 | 10 | [-6,-127,24,-108] (30x19) | [-0.5,-124.5,20.4,-115.9] |
| @43 | 11 | [9,-91,41,-60] (32x31) | [15.7,-80.8,32.5,-62.7] |
| @55 | 9 | [-21,-83,15,-43] (36x40) | [-14.3,-71.8,14.1,-52.6] |
HQs: @20 (-81.3,-59.8) west, with Insertions @31 and @33, polygon [-115,-108,-3,9]; @36 (66.9,-52.5) east, with Insertions @7 and @45, polygon [38,-112,92,-8]. They are 148 m apart. Sector @18 (25.1,-74.4) sits in zone @43's container. No combat area; all polygons together span 207x136 (x -115..92, z -127..9). Zones lie in a belt at x -21..41 between the HQs. Unusual: only Small targets; target @46 is in zone @55's container but nearer zone @43 (nearest-zone split would be 10/12/8).

### Empire State (MP_AFTERMATH): 29 targets, 2 zones
Assets: MP_Sabotage0, MP_Sabotage0_Schematic, staticmodelgroup.physics. 2 HQs, 1 Sector, 4 Insertions (keys 3, 3, 6, 6), 6 TelemetryAreas, 1 SpecialCombatArea.
| Zone | Targets | Keys | Container | Span |
|---|---|---|---|---|
| @12 | 14 | 6 Small, 7 Medium, 1 Large | [-666,26,-643,60] (23x34) | [-662.4,37.0,-643.4,57.0] |
| @31 | 15 | 6 Small, 8 Medium, 1 Large | [-637,8,-617,37] (20x29) | [-636.4,9.9,-617.5,31.2] |
HQs: @22 (-659.7,-40.5) in polygon [-708,-72,-612,-4] with Sector @3 (-631.6,-19.6) and SpecialCombatArea @44; @33 (-656.8,97.9) in polygon [-702,47,-612,148]. They are 138 m apart. Play area (the polygon holding the SpecialCombatArea and nearly everything): [-719,-167,-521,118] = 198 x 285. The layout is long and narrow (instances span 97 x 204). Unusual: telemetry areas @27 and @55 sit at y 107, about 50 m above the play ground (y 54-58); telemetry @11 lies at x -596, east of the strip. Target @39 (-662.4,37.0) is only in the larger polygons, so its zone @12 is by proximity.

### Blackwell Fields (MP_BADLANDS): 73 targets, 6 zones
Assets: MP_Sabotage0, MP_Sabotage0_Schematic, staticmodelgroup.physics. 5 HQs, 2 Sectors, 8 Insertions (keys 0, 0, 0, 1, 1, 4, 5, 7), 1 SpecialCombatArea. Keys total: 33 Small, 34 Medium, 6 Large.

East group (polygon 42 [205,-178,331,-57]), 36 targets:
| Zone | Targets | Keys | Container | Span |
|---|---|---|---|---|
| @62 | 14 | 7S 6M 1L | BOX48 [260,-162,280,-142] 20x20 | [261.7,-161.3,279.0,-142.6] |
| @84 | 11 | 6S 4M 1L | BOX24 [222,-114,243,-72] 21x42 | [227.8,-109.1,238.6,-78.7] |
| @95 | 11 | 6S 4M 1L | BOX128 [281,-108,311,-88] 30x20 | [292.8,-107.8,304.9,-91.0] |

West group (polygon 19 [-132,-351,-56,-286]), 37 targets:
| Zone | Targets | Keys | Container | Span |
|---|---|---|---|---|
| @107 | 19 | 7S 11M 1L | BOX22 [-83,-318,-55,-293] 28x25 | [-82.7,-321.8,-60.6,-300.8] |
| @69 | 14 | 5S 7M 2L | POLY105 [-120,-349,-76,-307] 44x42 | [-106.5,-340.1,-84.7,-321.7] |
| @106 | 4 | 2S 2M | POLY105 (shared with @69) | [-110.6,-321.7,-99.9,-316.2] |
Zones @69 and @106 share the same containers (polygons 19, 32, 105), so the 18 targets in that cluster are split 14 / 4 only by distance; the true split is uncertain.

HQs: @5 (231.0,-24.4) and @8 (292.0,-24.4), both in BOX77 [205,-57,331,-10], 61 m apart; @51 (188.4,-159.2) with Insertions @50 and @116 (polygon 49); @6 (-175.8,-339.9) with Insertions @13 and @122 (polygon 47 [-204,-362,-112,-302]); @39 (-49.4,-286.6) with Insertion @18 (polygon 113). Sectors: @37 (-96.8,-326.6) in the west group, @44 (271.7,-118.7) in the east group. SpecialCombatArea @103 (198.6,-105.3) is only in polygon 32. Polygon 32 [-630,-942,745,589] (1375 x 1531) is a world-boundary polygon, not a sized play area; instances span 483 x 315 (x -176..307, z -340..-24). Unusual: two clusters of three zones about 480 m apart and 5 HQs (everywhere else 2), which suggests several layouts packed in one layer (see SAB_LayoutSelection, open question 3). It has the most targets (73), which is more than the 50 score-bar segments.

### Manhattan Bridge (MP_DUMBO): 15 targets, 3 zones, all Small
Assets: MP_Sabotage0, MP_Sabotage0_Schematic. 2 HQs, 1 Sector, 4 Insertions (keys 6, 7, 8, 8), 5 TelemetryAreas, 1 SpecialCombatArea.
| Zone | Targets | Container | Span |
|---|---|---|---|
| @19 | 5 | BOXes 13, 15, 34 (inner [-70,-410,-36,-371] 34x39) | [-61.8,-403.3,-50.1,-376.8] |
| @20 | 5 | POLYs 39, 42, 49 (inner [-45,-323,-6,-285] 39x38) | [-26.8,-313.1,-11.9,-291.2] |
| @50 | 5 | POLYs 32, 36, 37 (inner [-56,-357,-26,-332] 30x25) | [-43.4,-354.1,-27.8,-338.1] |
HQs: @4 (-134.4,-352.0) west and @51 (38.4,-352.0) east, 173 m apart. Zones are strung north-south at x -61..-22 between them (z about -403, -345, -301). Sector @46 (-41.1,-345.0) sits on zone @50, inside SpecialCombatArea @12's polygon [-97,-380,5,-302] (102 x 78). All polygons together span 210 x 160 (x -159..51, z -429..-269). Telemetry areas sit on both HQs (@30, @44) and on each zone (@10, @29, @33). Unusual: several polygons occur twice with identical bboxes (27/38, 1/9, 32/36, 39/49, 13/34). Exactly 5 targets per zone; smallest layer.

### Eastwood (MP_EASTWOOD): 48 targets, 3 zones
Assets: MP_Sabotage0, MP_Sabotage0_Schematic. 2 HQs, 3 Sectors, 4 Insertions (keys 4, 5, 15, 15), 1 SpecialCombatArea. Keys: 16 Small, 23 Medium, 9 Large.
| Zone | Targets | Keys | Container | Span |
|---|---|---|---|---|
| @45 | 16 | 7S 5M 4L | POLY60 [187,-206,233,-174] 46x32 | [199.6,-202.1,223.9,-176.7] |
| @50 | 16 | 4S 9M 3L | POLY30 [167,-149,242,-117] 75x32 | [190.2,-141.6,228.1,-125.4] |
| @78 | 16 | 5S 9M 2L | POLY61 [172,-180,223,-154] 51x26 | [175.1,-174.8,221.4,-156.1] |
16 / 16 / 16 by container; by nearest zone it would be 14 / 16 / 18, because targets @57 and @79 are nearer @78 but sit in @45's polygons. HQs: @26 (252.2,-163.2) east and @71 (129.0,-138.6) west, 126 m apart. Sectors: @22 (181.5,-147.5) in zone @50's polygons; @23 (-172.0,-7.0) and @59 (61.9, y 348.3, 27.3) are in no polygon. SpecialCombatArea @34 (193.9,-134.4). Play area: polygon 5 [37,-253,340,-44] = 303 x 209. Unusual: gameplay height is about 233-244, a high plateau; Sector @59 is at y 348, about 110 m above everything else, and both @23 and @59 are far outside the play area (likely unused). Insertions @20 and @76 use variant 15 `Cautious_OnSpot_v4_NOT_FOR_REVEAL`.

### Saints Quarter (MP_LIMESTONE): 39 targets, 3 zones (one with no targets)
Assets: MP_Sabotage0, MP_Sabotage0_Schematic, staticmodelgroup.physics. 2 HQs, 1 Sector, 4 Insertions (all key 3), 4 TelemetryAreas, no SpecialCombatArea. Keys: 18 Small, 19 Medium, 2 Large.
| Zone | Targets | Keys | Container | Span |
|---|---|---|---|---|
| @20 | 19 | 10S 9M | POLY62 [322,95,341,108] 19x13 | [323.2,96.4,339.7,106.9] |
| @56 | 20 | 8S 10M 2L | POLY13 [357,76,380,112] 23x36 | [364.4,78.9,377.8,107.3] |
| @37 | 0 | none | only the map polygon 43 [302,61,392,146] | no member |
Zone @37 (326.6, y 68.7, 128.7) has no target anywhere near; all 39 targets are in the clusters at @20 and @56 (nearest-zone split 19 / 20). HQs: @53 (282.9,105.6) west in polygon 27 [266,55,316,143]; @29 (382.1,76.8) east in polygon 34; 103 m apart. Sector @65 (327.0,111.8) is in polygon 43 (302..392, 61..146 = 90 x 85). No combat area; all polygons together span 146 x 93. Unusual: zone @20's container is only 19 x 13 m yet holds 19 targets (0.08 per square metre of box; this is the densest box on any map, computed from container bboxes).

### Maps without a Sabotage layer
`map-names.json` has 19 maps; subtracting the 6 above leaves 13: Operation Firestorm (MP_FIRESTORM), Area 22B (MP_GRANITE_MILITARYRND_PORTAL), Downtown (MP_GRANITE_DOWNTOWN_PORTAL), Liberation Peak (MP_CAPSTONE), Redline Storage (MP_GRANITE_MILITARYSTORAGE_PORTAL), Defense Nexus (MP_GRANITE_TECHCENTER_PORTAL), Fort Lyndon (MP_GRANITE), Iberian Offensive (MP_BATTERY, empty header in the file), Portal Sandbox (MP_PORTAL_SAND), Golf Course (MP_GRANITE_RESIDENTIALNORTH_PORTAL), Mirak Valley (MP_TUNGSTEN), Marina (MP_GRANITE_MARINA_PORTAL), New Sobek City (MP_OUTSKIRTS). Wake Island (MP_ATOLL) also has an empty header but is not in `map-names.json`. The brief's "11 without" therefore does not match this data (13 in the name list, 14 with Wake Island).

## 3. Cross-map table

| Map | Zones | Targets per zone | Targets (S/M/L) | HQs | Sectors | Play area (m) |
|---|---|---|---|---|---|---|
| Siege of Cairo | 3 | 10 / 11 / 9 | 30 (30/0/0) | 2 (148 m apart) | 1 | no combat area; polygons span 207 x 136 |
| Empire State | 2 | 14 / 15 | 29 (12/15/2) | 2 (138 m) | 1 | 198 x 285 |
| Blackwell Fields | 6 | 14 / 11 / 11 and 19 / 14 / 4 | 73 (33/34/6) | 5 | 2 | world polygon 1375 x 1531; instances span 483 x 315 |
| Manhattan Bridge | 3 | 5 / 5 / 5 | 15 (15/0/0) | 2 (173 m) | 1 | 210 x 160 (combat core 102 x 78) |
| Eastwood | 3 | 16 / 16 / 16 | 48 (16/23/9) | 2 (126 m) | 3 (2 outside polygons) | 303 x 209 |
| Saints Quarter | 3 (1 empty) | 19 / 20 / 0 | 39 (18/19/2) | 2 (103 m) | 1 | no combat area; polygons span 146 x 93 |
| Total | 20 | | 234 (124 / 91 / 19) | 15 | 9 | |

Totals check: Small 30+12+33+15+16+18 = 124; Medium 0+15+34+0+23+19 = 91; Large 0+2+6+0+9+2 = 19; sum 234.

## 4. Open questions (instance indices refer to `MP_Sabotage0` on the named map)
1. Zone-to-target links are not stored; membership is inferred. Weak spots: Siege of Cairo target @46; Eastwood targets @57 and @79; Blackwell Fields zones @69 vs @106 (same containers, 14 / 4 split by distance); Empire State target @39.
2. Saints Quarter zone @37 (326.6, 128.7) has no targets. Unused, a spare, or tied to Sector @65 (327.0, 111.8)?
3. Blackwell Fields has two three-zone clusters (east x 220..300, west x -110..-60) and 5 HQs (@5, @8, @51 east; @6, @39 west). Does SAB_LayoutSelection (1, range 0..2) pick a subset, or are both clusters used as attack and defence sites? Which HQ pairs with which cluster is unknown.
4. Which HQ is attacker and which defender is not stored; the first-round attacker is not in the data.
5. Eastwood Sectors @23 (-172, 231.5, -7) and @59 (61.9, 348.3, 27.3) lie outside every polygon: unused? Insertions @20 and @76 use the NOT_FOR_REVEAL variant 15.
6. Manhattan Bridge duplicates volumes (polygons 27/38, 1/9, 32/36, 39/49; boxes 13/34): two layout variants or a duplicate copy?
7. Siege of Cairo and Manhattan Bridge use only key 0 (Small); is the Small/Medium/Large split meaningful in play beyond health (all worth 1 point)?
8. Units of SAB_fInitialRoundDuration (6.0), SAB_fOvertimeDuration (15.4) and SAB_iSoldierOOBTimeToReturn (5), and whether SAB_fDestructibleHealthModifier (5.0) scales MaxHealth, are unconfirmed.
9. The score bar caps at 50 segments (MaximumSegments) but Blackwell Fields has 73 targets; how is the bar scaled, or is not every target counted?
10. Not found in the data: round count, any point value other than 1 per piece, time bonuses, XP. Two UI strings are missing (01FAB882, 23BCBB70).
