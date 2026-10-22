# Strikepoint (build 2.1.1.0) - decoded data analysis

Sources: Strikepoint-tweakables.txt, Strikepoint-maps.txt, objective-table.json, ui-text.txt, maps-tweakables.txt.
Distances are horizontal (x/z). Which HQ belongs to which team, and which team attacks, is not stored; the two HQs per layout are spawn areas on opposite sides of the objective.

## 1. Mode rules

### What the UI text states
- One life per round, no redeploys.
- Objective unlocked / active "after a set amount of time".
- Win a round by securing the objective, or by occupying the objective area for longer than the enemy when the round ends; eliminating the enemy team also wins the round.
- First to win 6 rounds ("First team to secure a majority of rounds wins").
- Hardcore Strikepoint exists as a separate mode name.

### MUT_Strikepoint tweakables (client defaults; name = value [min..max as stored]; a "0..0" range means no range is stored, not a real range)
| Tweakable | Value | Range | UI confirms? |
|---|---|---|---|
| SP_iRoundsToWin | 6 | [3..0] (min 3, max not stored) | Yes, "First to win 6 rounds" |
| SP_iRoundTime | 3 | [0..0] | Not stated in UI. Unit not in data (minutes assumed) |
| SP-iOvertimeLength | 60 | [0..60] | Overtime not named in UI; the "occupy longer than the enemy when the round ends" rule fits it. Unit not in data (seconds assumed) |
| SP_fCaptureProgressTarget | 25.0 | [0.0..90.0] | No (secure time; unit not stored) |
| SP_fCaptureTime | 0.0 | [0.0..30.0] | No |
| SP_fCaptureTime_NeutralizationFactor | 0.0 | [0.0..30.0] | No |
| SP_f[]CaptureTimeMultipliers | {Field_ffba60f0: [0.0, 1.0]} | - | No (array, field name unresolved) |
| SP_fCaptureLockTimer | 30.0 | [0.0..30.0] | No |
| SP_bDownedPlayersCountedAsAlive | false | - | Indirectly (one life) |
| SP_iSoldierMandownType | 0 | [0..2] | No |
| SP_bAutoRequestRevive | true | - | No |
| SP_bAllowLevelReset | true | - | No |
| SP_fLevelResetDelay | 3.0 | [0.0..8.0] | No |
| SP_iOutOfBounds_TimeToReturn | 5 | [0..0] | No |
| SP_iLobbyPlayerCountStartTimer | 8 | [0..0] | No |
| SP_iLobbyPlayerCountToSpeedUpTimer | 8 | [0..0] | No |
| SP_fNoInteractivityTimeoutOverride | 45.0 | [0.0..600.0] | No |
| SP_bEnableOrders | true | - | No |
| SP_bTacticalAdviceEnabled | false | - | No |
| SP_bUseNotEnoughTimeLeftWarning | false | - | No |
| SP_iCommanderVoice | -1 | [0..0] | No |
| SP_fUrgencyThresholdTime / EnemyCapture / FriendlyCapture | 30.0 / 0.5 / 0.66 | [0..120] / [0..1] / [0..1] | No (audio urgency) |
| SP_iUrgencyThresholdAlive | 1 | [0..0] | No |
| SP_fAudioFalloffDistanceToObjective | 200.0 | [1.0..400.0] | No |
| Assault / Support / Engineer / Recon Recommended | false each | - | No |

Not found in the data: any named respawn tweakable (lack of respawn is carried by the UI text and SP_bDownedPlayersCountedAsAlive=false, not by a number), a named "objective unlock time" tweakable, and any XP tweakable. The objective unlock delay therefore lives either in unnamed constants of GME_Sim_Strikepoint_Round or in the per-map Strikepoint_Tweaks instance (see open questions).

### Round logic and UI view models
- GME_Sim_Strikepoint_Round (58 objects): named variables only out, MI_Sim_GameMode, AlivePerTeam, ActivityStateMachine, MI_LD_Strikepoint_Tweaks (all null; constants unnamed). It reads the Strikepoint_Tweaks interface and tracks AlivePerTeam; no numeric value is recoverable here.
- GME_Pres_Strikepoint_Round (35 objects), GM_Strikepoint_LaunchFunction (ActivityParameters, LaunchParameters null): no numbers.
- MP_UI_StrikePoint_OutcomeDataViewModel: TargetScore, CurrentRound, FriendlyScore, EnemyScore, RoundCollection_First/Second/Third, MIPres_RoundData (round history display with three round collections).
- Strikepoint_IndividualTeamCount_ViewModelEx: TeamIcon, TeamColor, NeutralColor, HealthStates (alive count per team).
- Shared SimEx_CaptureVolume (SoldiersOnPoint, AllSoldiersOnPoint, SoldiersExitedPoint, SoldiersDeadOrExited, AllVehiclesOnPoint) is the on-point counting used by capture.

### AD_Objective_Strikepoint - GEM to prefab
- Sector: GMPF_Sector. CapturePoint_OutlineArea: GMPF_OutlineArea. CapturePoint_Proxy: GMPF_CapturePoint_Proxy. HQ: GMPF_HQ. AutomaticAA: GMPF_AutomaticAA.
- CapturePoint variants: default `GMPF_CapturePoint_NoRepresentation`, key 1 = `GMPF_CapturePoint_OneTimeUse`. Every placed instance has key -1 and the maps file resolves it to `GMPF_CapturePoint` (a name not in this table) - see open questions.
- Insertion (arrival animation) keys 0-18: Cautious_Arrival (0), _Arrival_Corner (1), _LongDistance (2), OnSpot_v1/v2/v3 (3/4/5), Chaotic_Arrival_v1/v2/v3 (6/7/8), Chaotic_LongDistance (9), Chaotic_LongDistance_Cover (10), GAU_MH47_Exit_OnGround (11), GAU_MH47_FastRope (12), GAU_CornerStack (13), GAU_CoverToCover (14), OnSpot_v4 / v5 NOT_FOR_REVEAL (15/16), Vehicle_Quad (17), Vehicle_FlyerUnarmed (18). Insertion_Event: Airstrike (0), JetStraight (1).
- Insertion keys actually used: 0, 1, 2, 3, 4, 5, 6, 15, 16 (never 7-14, 17, 18). Most maps use OnSpot v1 + v3 (keys 3 and 5); Area 51 uses key -1 for all four.

### Per-map overrides
No map has namedOverrides. Every Strikepoint_Tweaks instance has key=-1 and variant=None (the mode definition does not list the module; its per-instance values are not decoded in the maps file). Faction swap (team1 = Pax Armata, team2 = NATO) on Siege of Cairo, Blackwell Fields, Railway to Golmud; all others use the engine default. maps-tweakables.txt holds only Conquest/vehicle values, nothing for Strikepoint.

## 2. Per-map layouts
Layer name is `MP_Strikepoint0` except Contaminated and Hagental Base (`Strikepoint0`). Every map has one Strikepoint0 layout layer; only Eastwood and New Sobek City carry two objective layouts in it. The maps file has no Flag entries; the four maps with a 'flag' layer folder whose assets are named Strikepoint (Iberian Offensive, Eastwood, Saints Quarter, Mirak Valley) exist in the catalog but were not extracted here.
"Objective area" = smallest polygon/box around the objective; "Play area" = largest polygon containing the objective and both HQs (bbox size, x by z, metres). "@n" = instance index in the layer.

| Map | Layouts | Objective (CP@idx) pos | HQ A (idx) / dist to objective | HQ B (idx) / dist | HQ-HQ | Objective area | Play area | Tweaks inst |
|---|---|---|---|---|---|---|---|---|
| Siege of Cairo | 1 | [-1.7, 60.2, -61.4] @5 | [65.9, 62.1, -71.2] @26 / 68.3 | [-78.9, 64.2, -75.7] @18 / 78.5 | 144.9 | box 60x43, poly 11x27 | poly 192x103 | @22 |
| Empire State | 1 | [-555.1, 58.7, -31.7] @10 | [-531.0, 53.9, -90.4] @7 / 63.5 | [-605.3, 57.8, 17.0] @14 / 69.9 | 130.6 | poly 20x19 | poly 108x158 | @11, @12 |
| Wake Island | 1 | [105.0, 102.2, -108.1] @7 | [167.9, 100.5, -37.0] @12 / 94.9 | [9.4, 99.6, -164.2] @3 / 110.8 | 203.2 | poly 25x37 (Global 66x63) | poly 214x187 | @6 |
| Blackwell Fields | 1 | [-109.2, 75.8, -325.4] @4 | [-48.1, 74.3, -299.0] @3 / 66.6 | [-177.9, 77.1, -338.3] @6 / 69.9 | 135.6 | none stored | none stored | @7 |
| Iberian Offensive | 1 | [776.4, 82.0, 169.9] @11 | [850.4, 84.1, 179.4] @1 / 74.6 | [707.7, 75.9, 199.3] @6 / 74.7 | 144.1 | poly 23x16 | poly 191x101 | @15 |
| Liberation Peak | 1 | [108.8, 133.5, 83.5] @2 | [29.6, 134.0, 70.0] @8 / 80.3 | [181.5, 135.0, 121.1] @12 / 81.8 | 160.3 | poly 25x20 (telemetry box 62x58) | poly 216x150 | @10 |
| Contaminated | 1 | [117.0, 339.7, -26.1] @3 | [73.7, 347.5, -92.5] @4 / 79.3 | [162.9, 340.6, 42.8] @7 / 82.8 | 162.1 | telemetry box 52x54 | poly 198x163 | @1 |
| Area 51 | 1 | [-51.2, 64.0, 1.3] @7 | [-51.2, 64.0, 76.8] @6 / 75.5 | [-51.2, 64.0, -76.8] @5 / 78.1 | 153.6 | box 18x19 | none stored | @9 |
| Manhattan Bridge | 1 | [-39.2, 56.0, -243.6] @23 | [23.6, 59.6, -203.6] @37 / 74.5 | [-102.5, 54.7, -276.2] @10 / 71.2 | 145.5 | poly 24x19, boxes 37x42 and 37x93 | poly 169x118 | @12 |
| Eastwood L1 | 2 | [197.1, 240.1, -166.5] @5 | [136.9, 236.5, -134.4] @26 / 68.2 | [266.3, 243.5, -197.7] @15 / 75.9 | 144.1 | poly 9x13 | poly 164x93 | none |
| Eastwood L2 |  | [75.8, 234.3, 15.1] @7 | [136.3, 232.5, -30.5] @17 / 75.8 | [0.8, 233.1, 3.9] @19 / 75.8 | 139.8 | box 52x57 | none stored | @9 |
| Operation Firestorm | 1 | [-85.0, 125.0, -76.9] @2 | [-55.9, 124.9, -156.1] @5 / 84.4 | [-157.4, 125.9, -17.7] @4 / 93.5 | 171.6 | poly 20x23 (telemetry box 41x31) | poly 152x155 | @14 |
| Railway to Golmud | 1 | [-164.6, 743.0, 900.0] @5 | [-173.9, 738.4, 826.6] @6 / 74.0 | [-132.2, 754.4, 973.2] @3 / 80.0 | 152.4 | poly 18x21 (Global box 36x31) | poly 138x180 | @7 |
| Tsuru Reef | 1 | [-607.2, 103.6, -181.7] @8 | [-618.2, 107.4, -125.8] @5 / 57.0 | [-563.7, 108.7, -241.9] @4 / 74.3 | 128.3 | poly 29x29 (Global box 57x60) | none stored | @6 |
| Saints Quarter | 1 | [335.7, 65.8, 101.8] @12 | [283.1, 66.5, 90.7] @8 / 53.8 | [399.4, 64.2, 87.6] @1 / 65.3 | 116.3 | poly 12x12 | none stored | @10 |
| New Sobek City L1 | 2 (uncertain) | [-26.5, 95.9, -80.6] @23 | [48.2, 94.9, -99.8] @37 / 77.1 and [-83.1, 96.3, -83.5] @41 / 56.7; also @22 [-15.4, 96.0, -84.7] / 11.8 | see open questions | - | poly 16x22, Global box 102x62 | poly 158x94 | @33 |
| New Sobek City L2 |  | [-93.4, 96.7, -19.0] @35 | @41 / 65.3; @32 [-51.2, 109.5, 76.5] / 104.4 | - | - | Global poly 49x125 | (same 49x125) | none |
| Vegas Strip | 1 | [-70.2, 44.1, 59.7] @4 | [-39.3, 44.4, 2.2] @5 / 65.3 | [-103.5, 42.2, 121.2] @7 / 69.9 | 135.2 | poly 14x11 | poly 107x147 | @9 |
| Cairo Bazaar | 1 | [-21.4, 65.3, 24.7] @4 | [27.7, 64.2, 2.5] @8 / 53.9 | [-52.9, 65.4, 67.1] @6 / 52.8 | 103.3 | box 13x10 | poly 153x123 | none |
| Hagental Base | 1 | [219.7, 66.6, -49.6] @9 | [155.6, 66.1, -34.9] @14 / 65.8 | [256.1, 64.3, -113.9] @19 / 73.9 | 127.8 | box 28x28 | poly 155x173 | none |
| Mirak Valley | 1 | [270.4, 86.6, -440.6] @5 | [252.9, 84.1, -528.7] @3 / 89.8 | [311.5, 83.1, -354.2] @8 / 95.7 | 184.1 | poly 30x24 | poly 153x201 | @7 |

Per-map notes
- Siege of Cairo: 5 TelemetryAreas; team1/team2 faction swap. Empire State: two Tweaks instances (@11 at [-578.4,54.2,-57.8], @12 at [-555.7,62.3,-31.5]), 6 TelemetryAreas, extra Strikepoint_VFX layer.
- Wake Island: objective outline also appears in Strikepoint_Global (66x63); largest HQ spacing of all.
- Blackwell Fields: no boxes or polygons for any instance (no stored play area or objective area); HQ@6 and Insertion@5 share the coordinates [-177.9,77.1,-338.3]; its Sector@1 and Tweaks@7 sit at [-51.3,66.1,82.8] / [-51.9,66.4,81.4], about 400 m from the objective (default placement).
- Contaminated: Sector@9 at the same default [-51.3,66.1,82.8], not at the objective; HQ@4 is 7.8 m above the objective. Area 51: HQs at x=-51.2, z=+-76.8 (exactly mirrored).
- Cairo Bazaar: SpecialCombatArea @3; no Tweaks instance; Sector@5 at default [-51.3,66.1,82.8]. Hagental Base: no Tweaks instance. Manhattan Bridge: SpecialCombatArea @1 and a CapturePoint_OutlineArea @9. Railway to Golmud: only map with a DeployCam (@1 at [-108.7,1098.9,882.5]); HQ@3 is 11.4 m above the objective.
- Eastwood: two complete objective layouts in one layer, ~220 m apart (L1 north-east, L2 south-west); only L2 has a Tweaks instance (@9) and L2 is enclosed by no polygon (only a 52x57 box). Stray Sector@20 at the default [-51.3,66.1,82.8] (y 66 while the map is at y ~235).
- New Sobek City: 12 TelemetryAreas, 8 Insertions, 4 HQs, 2 CPs, 2 Sectors, one CapturePoint_OutlineArea (@45); only one Tweaks (@33) and one Outline, both at layout 1. Stray Sector@42 (y 108.4) at the default x/z.
- Iberian Offensive: Sector at [777.1,82.1,147.5], 22 m off the objective. All four Insertions use OnSpot_v3.

## 3. Cross-map summary
| Map | Layouts | Objective-HQ distances (m) | Play area (m) |
|---|---|---|---|
| Siege of Cairo | 1 | 68.3 / 78.5 | 192x103 |
| Empire State | 1 | 63.5 / 69.9 | 108x158 |
| Wake Island | 1 | 94.9 / 110.8 | 214x187 |
| Blackwell Fields | 1 | 66.6 / 69.9 | none stored |
| Iberian Offensive | 1 | 74.6 / 74.7 | 191x101 |
| Liberation Peak | 1 | 80.3 / 81.8 | 216x150 |
| Contaminated | 1 | 79.3 / 82.8 | 198x163 |
| Area 51 | 1 | 75.5 / 78.1 | none stored |
| Manhattan Bridge | 1 | 74.5 / 71.2 | 169x118 |
| Eastwood | 2 | L1 68.2 / 75.9; L2 75.8 / 75.8 | L1 164x93; L2 none stored |
| Operation Firestorm | 1 | 84.4 / 93.5 | 152x155 |
| Railway to Golmud | 1 | 74.0 / 80.0 | 138x180 |
| Tsuru Reef | 1 | 57.0 / 74.3 | none stored |
| Saints Quarter | 1 | 53.8 / 65.3 | none stored |
| New Sobek City | 2? | L1 56.7 / 77.1 (+11.8); L2 65.3 / 104.4 | 158x94 |
| Vegas Strip | 1 | 65.3 / 69.9 | 107x147 |
| Cairo Bazaar | 1 | 52.8 / 53.9 | 153x123 |
| Hagental Base | 1 | 65.8 / 73.9 | 155x173 |
| Mirak Valley | 1 | 89.8 / 95.7 | 153x201 |

Totals: 21 objective layouts over 19 maps (Eastwood 2, New Sobek City 2, the rest 1). Objective-to-HQ distance ranges 52.8-110.8 m (excluding New Sobek City's 11.8 m HQ@22 and 104.4 m HQ@32); HQ-HQ 103-203 m. Cairo Bazaar is the tightest, Wake Island the widest. Most pairs are near-symmetrical (within ~10 m) except Wake Island, Tsuru Reef (57 vs 74), Saints Quarter (54 vs 65), Firestorm (84 vs 94).

## 4. Open questions (instance indices)
1. Objective unlock time, any round-start delay, and per-map values are not named in MUT_Strikepoint; they are in the unnamed constants of GME_Sim_Strikepoint_Round or in GEM_Strikepoint_Tweaks (decoded as variant=None, no values extracted). Tweaks instances: Cairo @22, Empire State @11 and @12, Wake @6, Blackwell @7, Iberian @15, Liberation Peak @10, Contaminated @1, Area 51 @9, Manhattan @12, Eastwood @9, Firestorm @14, Golmud @7, Tsuru Reef @6, Saints Quarter @10, New Sobek @33, Vegas @9, Mirak @7. Cairo Bazaar and Hagental Base have none (defaults, or the module is absent).
2. CapturePoint variant: table default is GMPF_CapturePoint_NoRepresentation (key 1 = OneTimeUse), but all 21 instances (key -1) resolve to GMPF_CapturePoint; which prefab is used, and its radius/time, is unconfirmed.
3. Empire State: why two Tweaks (@11 at the HQ side, @12 at the objective).
4. New Sobek City: grouping of 4 HQs and 2 CPs is uncertain. HQ@22 is only 11.8 m from CP@23 (inside the objective box); HQ@41 lies in both play polygons (34 and Global 1). Likely layout 1 = CP@23 with HQ@37 + HQ@22 or HQ@41, layout 2 = CP@35 with HQ@41 + HQ@32, but HQ@32 (y 109.5, no polygon) and Sector@42 sit outside all areas; layout 2 has no Tweaks, Outline or Sector at its CP. May be an unused or deprecated layout.
5. Eastwood: Sector@20 stray; L2 (CP@7) outside any play polygon; L1 (CP@5) has no Tweaks. Is only one layout active, or are both chosen per round or match?
6. Default-position Sectors at [-51.3,66.1,82.8]: Blackwell Fields @1, Contaminated @9, Eastwood @20, Cairo Bazaar @5, New Sobek City @42 (y 108.4). Unused or positioned by another layer.
7. No outer play polygon stored: Blackwell Fields (no areas at all), Area 51, Tsuru Reef, Saints Quarter, Eastwood L2. Boundary may come from a combat area in another layer.
8. Which team attacks and which HQ belongs to which team is not stored; the Pax Armata/NATO swap on Siege of Cairo, Blackwell Fields, Railway to Golmud suggests mirrored team assignment there.
9. Units of round time (3), overtime (60) and capture target (25) are not in the data; assumed minutes, seconds, seconds.
10. Hardcore Strikepoint rule differences are not in the decoded files.
11. Flag layer folders (assets named Strikepoint) for Iberian Offensive, Eastwood, Saints Quarter, Mirak Valley exist in the catalog but are not in the extracted maps file.
