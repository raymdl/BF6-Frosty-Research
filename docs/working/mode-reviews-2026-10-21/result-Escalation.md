# Escalation (Battlefield 6, build 2.1.1.0) - analysis

Source files: Escalation-maps.txt, Escalation-tweakables.txt (null-valued logic variables only; the ESC_ values are in existing-tweakables.txt, MUT_Escalation), maps-tweakables.txt, ui-text.txt, objective-table.json, map-names.json. All counts and distances below were computed by script (esc3.py, esc_parse.py in the parent folder); distances are 2D (x, z) in metres.

## 0. Scope (updated after the second capture)

11 maps have a full Escalation layer: Siege of Cairo (MP_ABBASID), Wake Island (MP_ATOLL), Iberian Offensive (MP_BATTERY), Liberation Peak (MP_CAPSTONE), Contaminated, Manhattan Bridge (MP_DUMBO), Eastwood, Operation Firestorm, Tsuru Reef (MP_ISOLATED), New Sobek City (MP_OUTSKIRTS), Mirak Valley (MP_TUNGSTEN). The first capture only saw the 8 stored in the Escalation subfolder (layer `MP_Escalation0`); the second found Wake Island, Contaminated and Tsuru Reef directly under `_Layers_Gameplay` (layer `Escalation0`).
- Railway to Golmud (MP_GOLMUDRAILWAY) has only 1 instance: CapturePoint@4 [-64.5, 738.6, 852.8] in `Escalation_Global` plus seven boxes (BOX@1, 2, 3, 5, 6, 7, 8; none contains the point); no HQ, no other flags. It is not a usable layout in this data (open question O1). Its MUT_Golmud has `Golmud_Escalation_EnableMovingTrain = true`.
- Area 51 (MP_DRYLAKE) and Vegas Strip (MP_PARADISE) have empty blocks. Empire State, Blackwell Fields, Saints Quarter, Cairo Bazaar and Hagental Base are not in the file (consistent with "no Escalation layer").
- factionOverrides now come from the data: team1 = Coalition/Pax Armata and team2 = Alliance/NATO on Siege of Cairo, Iberian Offensive, Operation Firestorm, Tsuru Reef (and the Golmud stub); team1 = Alliance/NATO and team2 = Coalition/Pax Armata on Eastwood; none (engine default) on Wake Island, Liberation Peak, Contaminated, Manhattan Bridge, New Sobek City, Mirak Valley. namedOverrides are empty everywhere.
- Variant names are resolved through AD_Objective_Escalation. All CapturePoints use `GMPF_CapturePoint` (key -1); the definition's Flag (key 0) and OneTimeUse (key 1) variants are unused.
- Shared skeleton: 7 CapturePoint (9 on Tsuru Reef), 6 HQ, 1 Collection_Event on most maps (always at 0,0,0, a logic placeholder), 0-3 Battle_Pickup (placed, not active in the live game; none on Wake Island and Tsuru Reef), Sector counts of 7 (5 on Wake Island and Tsuru Reef, so some sectors cover several flags).

## 1. Mode rules

### 1.1 What the UI text confirms (ui-text.txt)
- "Capture and hold more objectives to take territory." / "Hold objectives to advance your progress towards taking territory." (confirmed)
- "Hold more objectives than the enemy to advance your progress" (majority drives progress; confirmed)
- "Complete your progress before the enemy to take territory and remove objectives from the map"; "The removed objective will always be the one closest to your initial HQ" (confirmed: the team that takes territory loses the flag nearest ITS OWN initial HQ, so the map shrinks from the rear of the taker toward the middle)
- "First team to take three territories wins" (confirmed). With 7 flags, at most 5 territories can be taken before someone has 3 (3+2), so 2 flags always remain (Tsuru Reef has 9 flags, so 4 remain); matches `ESC_iPhaseAmount = 5`.
- A HARDCORE ESCALATION playlist title exists (Field_9e5045d8).

### 1.2 MUT_Escalation tweakables (client defaults; a server playlist can override). Format: name = value [min..max as dumped; many ranges are dumped as 0..0 and carry no information]. "UI" = confirmed by UI text; "inferred" = from the name only; nothing here states units, so seconds is assumed from the names.

Progress and territory
- ESC_iPhaseAmount = 5 [0..9] - number of phases (territories) possible; inferred, consistent with UI "first to three" (max 5 territory events).
- ESC_f[]PhaseLengths = [90.0, 162.0, 252.0, 3600.0] (array) - four values for five phases; per-phase time limits, last effectively unlimited; inferred, unconfirmed (open question O2).
- ESC_fPhaseTransitionLength = 40.0 - length of the territory-taken transition; inferred.
- ESC_fProgressTransitionTime = 10.0 - inferred.
- ESC_fProgressResetDelayOnTerritoryTaken = 6.0 [0.0..10.0] - progress reset delay after territory is taken; inferred.
- ESC_fObjectiveReintroductionTime = 4.0 - inferred (re-enabling the objectives after the removal).
- ESC_DisableObjectivesDuringTransition = false; ESC_ResetObjectivesOnPhaseEnd = false - objectives stay owned across the transition (inferred).
- ESC_fStartScoringTime = 5.0 - inferred.
- ESC_fRoundTimer = 120.0 [120.0..0.0] - inferred round/phase timer base (dumped range min 120).
- ESC_bShowPhaseTimer = true.
- ESC_fTEMPClassicCQMajorityBleedFrequency = 2.0 - "TEMP classic Conquest majority bleed": majority is applied every 2.0 (inferred).
- ESC_fWeightScaleTimeThreshold = 120.0 - inferred.
- ESC_fFirstPhaseUrgencyTimeThreshold = 30.0, ESC_fPhaseUrgencyTimeThreshold = 40.0, ESC_fGameUrgencyTimeThreshold = 50.0 - urgency (announcer/UI) thresholds; inferred.
- ESC_fDelayBeforeFirstMajorityEvent = 60.0; ESC_fDelayBeforeFirstMajorityEventLateJoin = 15.0 - delay before the "you have the majority" event; inferred.

Capture timing
- ESC_fCaptureTime = 20.0 - capture time (inferred, seconds).
- ESC_fNeutralizeTime = 20.0 - neutralize time (inferred).
- ESC_f[]CaptureSpeedMultipliers = [0.0, 1.0, 1.333, 1.666, 2.0] - speed by number of capturing players (index 0..4); inferred, the cap at 2.0x is at index 4 (whether index = player count or count-above-opponent is not stated).

Stalemate
- ESC_fStalematePredelay = 60.0; ESC_fStalematePredelay_PhaseStart = 120.0; ESC_fStalematePredelay_PhaseStart_Round0 = 180.0 (first phase of the match gets a longer pre-delay); ESC_fStalemateLowerThreshold = 30.0; ESC_fStaleMateDelayDecrement = 10.0 - all inferred from names (a stalemate = no majority holder; pre-delay before stalemate handling, shortened by 10 per step, lower bound 30). The stalemate provider (Ex_StalemateCommunicationProvider) has only variables StalemateLeader, EnemyIsWinningPhase, EnemyIsTakingTerritory, FriendlyIsTakingTerritory, FriendlyIsWinningPhase (all null defaults): it is a messaging provider, no numbers.

Respawn
- ESC_fTeam1RespawnDelay = 12.0; ESC_fTeam2RespawnDelay = 12.0 (equal on both teams).
- ESC_SoldierManDownType = 1 [0..2].

Vehicles and out-of-bounds
- ESC_fVehicleSpawnValueInterval = 90.0 [1.0..0.0] - vehicle spawn value interval; inferred.
- ESC_fOutOfBoundTime = 10 - out-of-bounds time (Manhattan Bridge sets MP_Dumbo_VehicleOOBtime = 10 [1..15] in its own MUT).

XP: MUT_Escalation has no XP tweakable. (No award values exist in this file; ESC_AwardSuccessfulRetreat = true is the only award-like flag.)

Squad, UI and lobby (not requested groups, listed for completeness)
- ESC_fSquadOrderCooldown = 30.0; ESC_fAttackOrderReactivationDelay = 20.0 [0.0..360.0]; ESC_fTacticalAdviceCooldown = 60.0; ESC_SpotRetreaters = false; ESC_iCommanderVoice = 0.
- ESC_iLobbyPlayerCountStartTimer = 32; ESC_iLobbyPlayerCountToSpeedUpTimer = 64; ESC_fNoInteractivityTimeoutOverride = 180.0 [0.0..600.0]; ESC_fAudioFalloffDistanceToObjective = 1.0 [1.0..200.0].
- Class recommendation flags all false: Assault, Engineer, Support, Recon "Recommended".

### 1.3 Round logic graphs
- GME_Sim_Escalation_Round (144 objects), GME_Pres_Escalation_Round (68 objects): only the named interface variables ActivityStateMachine, MI_Sim_GameMode, MI_Pres_GameMode survive (all null). The state machine, progress math and removal selection are in unnamed constants/nodes and could not be read here; the UI text is the only source for the removal rule (open question O3).
- Escalation_Leadership_ViewModel: AllowScoring, IsStalemate, IsFriendlyProgressing, IsEnemyProgressing, FriendlyHasMajority, EnemyHasMajority (flags only, no numbers). This confirms the model: majority (more flags held) -> that team progresses; neither -> stalemate.
- GMA_Escalation_Round_GemCollectionFilter (Source, ReturnValue) selects the objective gems for a round; MP_Outcome_TerritoryList_ViewModelEx lists the taken territories on the end-of-round screen.
- Per-map MUTs (maps-tweakables.txt): the only Escalation-specific value is Golmud_Escalation_EnableMovingTrain = true (also Golmud_MovingTrain_StreamIn = true). SpawnPreventionRadius_Small = 40.0 (Siege of Cairo) and SpawnPreventionRadius_LargeModes_Battery = 45.0 (Iberian Offensive) may apply; *_CQ_iInitialScore = 1200 is Conquest only.
- Objective definition AD_Objective_Escalation: CapturePoint default GMPF_CapturePoint with keys 0 = GMPF_CapturePoint_Flag and 1 = GMPF_CapturePoint_OneTimeUse; also lists StrategicAsset, VehicleSuperiorityCaptureVolume, CapturePoint_Proxy and Collection_Event (GMPF_CollectionEvent), Battle_Pickup (Minigun, Railgun, SmokeScreen, ArtilleryStrike, DSPulse), PsyGas modules. The layers use none of the alternate CapturePoint keys.

## 2. Reading guide for the per-map sections
- Side W / side E: the two initial HQs are not labelled team1/team2 in the data. They are inferred as the HQ pair farthest apart (each has 4-27 vehicle pads around it; 8 Insertions on 7 maps, none on Wake Island, Iberian Offensive, Liberation Peak and Tsuru Reef; the nearest flag is 64 m to 604 m away, Siege of Cairo closest at 75 / 64 m). Which of them is team1 (NATO) is unknown; sides are named by lower / higher x. Confidence on the initial pair: high (Siege of Cairo, Iberian Offensive, Liberation Peak, Manhattan Bridge, Eastwood, Operation Firestorm, Mirak Valley, Contaminated), medium on New Sobek City (two HQs per base) and low on Wake Island and Tsuru Reef (island maps: the farthest-apart HQs hold air and boat pads, while the land vehicle pads sit at flag-side HQs, see their sections).
- The other 4 HQ instances sit near flags (0 to 86 m, except Tsuru Reef HQ@75 at 194 m; flag-side forward spawn areas). On Iberian Offensive two of them (HQ@76, HQ@102) are duplicates of the E initial HQ HQ@73 at the same point, so there is no flag-side HQ on the E side.
- Removal order = flags ranked by 2D distance from that side's initial HQ, nearest first, when that side takes territory. The two teams' removals only interact if both want the same flag; "Overlap" lists whether the top-3 of each side share a flag (at most 5 removals happen, 3 by the winner and 2 by the loser).
- Vehicle pads are assigned to the nearest of all 6 HQs and the flags (7, or 9 on Tsuru Reef); HQs within about 110 m of an initial HQ that are listed as W-/E-cluster are merged into it. The "flags" figure in the cross-map table is therefore "other anchors": it includes pads at flag-side HQs (Wake Island 22 of 25, Tsuru Reef 14 of 23, Operation Firestorm 3 of 10, Liberation Peak 2 of 6). Class names as in the game (Tank, IFV, LightTransport, PTV_QuadBike, MobileAA, APC and so on).
- Positions are [x, y, z].

## 3. Cross-map table

| Map | Objectives at start | Initial HQ instances (index, x/z) | Pads per side (nearest anchor; third value = other anchors) | Air vehicles | team1 / team2 |
|---|---|---|---|---|---|
| Contaminated | 7 | W@114 [-151, -232] / E@128 [434, 190] | HQ-W 16 / HQ-E 17 / flags 5 (total 38) | yes: AttackHelicopter 2, AttackPlane 2, FighterPlane 2, ScoutHelicopter 4 | default |
| Eastwood | 7 | W@117 [-401, 122] / E@235 [378, -160] | HQ-W 20 / HQ-E 20 / flags 13 (total 53) | yes: AttackHelicopter 2, ScoutHelicopter 2, TransportHelicopter 2 | NATO / Pax Armata |
| Iberian Offensive | 7 | W@23 [576, 111] / E@73 [920, 134] | HQ-W 4 / HQ-E 4 / flags 0 (total 8) | no | Pax Armata / NATO |
| Liberation Peak | 7 | W@6 [-312, 100] / E@108 [275, 451] | HQ-W 15 / HQ-E 15 / flags 6 (total 36) | yes: AttackHelicopter 2, AttackPlane 2, FighterPlane 2 | default |
| Manhattan Bridge | 7 | W@12 [-262, -435] / E@9 [179, -243] | HQ-W 13 / HQ-E 13 / flags 6 (total 32) | yes: AttackHelicopter 2, ScoutHelicopter 2 | default |
| Mirak Valley | 7 | W@65 [-461, -240] / E@2 [497, -528] | HQ-W 27 / HQ-E 27 / flags 8 (total 62) | yes: AttackHelicopter 4, AttackPlane 4, FighterPlane 4, ScoutHelicopter 2, TransportHelicopter 4 | default |
| New Sobek City | 7 | W@191 [-189, 3] / E@140 [153, 21] | HQ-W 17 / HQ-E 17 / flags 5 (total 39) | yes: AttackHelicopter 2, ScoutHelicopter 2, TransportHelicopter 2 | default |
| Operation Firestorm | 7 | W@93 [-758, 209] / E@68 [560, -230] | HQ-W 22 / HQ-E 22 / flags 10 (total 54) | yes: AttackHelicopter 2, AttackPlane 2, FighterPlane 2, ScoutHelicopter 2, TransportHelicopter 2 | Pax Armata / NATO |
| Siege of Cairo | 7 | W@200 [-281, 66] / E@37 [159, -83] | HQ-W 10 / HQ-E 10 / flags 4 (total 24) | no | Pax Armata / NATO |
| Tsuru Reef | 9 | W@94 [-1156, 843] / E@21 [-436, -678] | HQ-W 12 / HQ-E 12 / flags 23 (total 47) | yes: AttackPlane 2, FighterPlane 2, TransportHelicopter 4 | Pax Armata / NATO |
| Wake Island | 7 | W@67 [-701, 308] / E@32 [202, -639] | HQ-W 17 / HQ-E 17 / flags 25 (total 59) | yes: AttackHelicopter 2, MultirolePlane 4, NavalFighterPlane 4, TransportHelicopter 4 | default (NATO / Pax Armata) |

Air = pad classes AttackHelicopter, ScoutHelicopter, TransportHelicopter, FighterPlane, AttackPlane, MultirolePlane, NavalFighterPlane. No air: Siege of Cairo, Iberian Offensive. Helicopters only: Manhattan Bridge, Eastwood, New Sobek City. Wake Island: attack and transport helicopters, multirole and naval fighter planes. Liberation Peak: attack helicopter, attack plane, fighter plane. Contaminated: attack and scout helicopters, attack plane, fighter plane. Tsuru Reef: transport helicopters, attack plane, fighter plane. Operation Firestorm and Mirak Valley: full set. Pads per side = nearest anchor (initial HQ plus its flag-side HQs); Wake Island and Tsuru Reef have most land pads at flag-side HQs or flags, so their W/E totals are not comparable to the other maps (Wake Island: HQ@2 and HQ@55 land groups of 11 each; Tsuru Reef: HQ@96 6, HQ@75 4).

## 4. Per-map detail (generated from the layer instances)

### Siege of Cairo (MP_ABBASID)
- Layer assets: Escalation, Escalation_Global, Escalation_Global_Schematic, MP_Escalation0, MP_Escalation0_Schematic, MeshVariationDb_Win32. Instances sit in layer(s) ['MP_Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}. namedOverrides:  {}.
- Gem counts: VehicleSpawner 24, Insertion 16, TelemetryArea 7, HQ 6, CapturePoint 7, Sector 7, Battle_Pickup 3, CapturePoint_OutlineArea 7, Collection_Event 1
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@200 [-281.2, 66.7, 65.6]; side E = HQ@37 [158.7, 62.2, -82.7]; separation 464 m. Other HQ instances: HQ@12 [-244.2, 64.0, 25.4] near CP@132 (31 m); HQ@115 [66.4, 62.1, -28.8] near CP@151 (46 m); HQ@124 [112.9, 65.2, -59.0] near CP@151 (16 m); HQ@172 [-199.9, 64.0, 8.8] near CP@132 (26 m)
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@132 [-214.1, 64.2, 31.1]; Sector@114 [-220.6, 64.2, 29.8] (7 m); polys [14, 152]; dW 75 dE 390
  - CP@243 [-160.8, 66.2, 93.6]; Sector@88 [-167.5, 65.4, 94.7] (7 m); polys [112, 174]; dW 124 dE 365
  - CP@30 [-180.3, 64.8, -30.8]; Sector@143 [-178.3, 64.8, -28.3] (3 m); polys [223, 225]; dW 140 dE 343
  - CP@45 [-80.5, 62.8, -18.0]; Sector@147 [-76.6, 62.5, -11.6] (7 m); polys [108, 112]; dW 217 dE 248
  - CP@81 [31.0, 64.1, 16.2]; Sector@130 [24.0, 63.9, 9.5] (10 m); polys [122]; dW 316 dE 162
  - CP@217 [8.6, 62.9, -99.5]; Sector@36 [14.5, 62.5, -101.1] (6 m); polys [112, 211]; dW 334 dE 151
  - CP@151 [97.5, 64.6, -62.8]; Sector@166 [86.1, 64.6, -39.8] (26 m); polys [35]; dW 400 dE 64
- Predicted removal order, side W (closest to HQ W first): CP@132(75) > CP@243(124) > CP@30(140) > CP@45(217) > CP@81(316) > CP@217(334) > CP@151(400)
- Predicted removal order, side E (closest to HQ E first): CP@151(64) > CP@217(151) > CP@81(162) > CP@45(248) > CP@30(343) > CP@243(365) > CP@132(390)
  - Overlap of W top3 [132, 243, 30] and E top3 [151, 217, 81]: none. Max 5 removals before a win. Orders from nearby alternate HQ instances: W-cluster HQ@12: 132>30>243>45>81>217>151; W-cluster HQ@172: 132>30>243>45>81>217>151 | E-cluster HQ@115: 151>81>217>45>30>243>132; E-cluster HQ@124: 151>81>217>45>30>243>132
- Vehicle pads total 24: IFV 4, LightTransport 8, PTV_QuadBike 8, Tank 4
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - CP@132: 1 -> LightTransport 1
    - CP@151: 1 -> LightTransport 1
    - CP@30: 1 -> PTV_QuadBike 1
    - CP@81: 1 -> PTV_QuadBike 1
    - HQ-E: 10 -> IFV 2, LightTransport 3, PTV_QuadBike 3, Tank 2
    - HQ-W: 10 -> IFV 2, LightTransport 3, PTV_QuadBike 3, Tank 2
- Battle_Pickup (placed, not active in live game): 3 -> @38 Battle_Pickup_Minigun [45.5, 62.3, -118.1] (CP@217 41 m); @154 Battle_Pickup_Railgun [-105.2, 70.7, -7.0] (CP@45 27 m); @178 Battle_Pickup_Minigun [-206.6, 66.6, 117.2] (CP@243 52 m)
- Collection_Event: 1 -> @70 CollectionEvent [0.0, 0.0, 0.0] (CP@81 35 m)
- Insertion: 16 -> {'Insertion_Cautious_OnSpot_v3': 5, 'Insertion_Cautious_OnSpot_v1': 4, 'Insertion_Cautious_OnSpot_v2': 7}; nearer HQ W 8, nearer HQ E 8
- CapturePoint_OutlineArea: 7 outlines, 6 of 7 flags matched within 15 m (no outline near [132])
- TelemetryArea: 7
- Combat area: no CombatArea/SpecialCombatArea instance in the Escalation layer

### Wake Island (MP_ATOLL)
- Layer assets: Escalation, Escalation0, Escalation_Cover, Escalation_Global, Escalation_Global_Schematic, MeshVariationDb_Win32, staticmodelgroup.physics. Instances sit in layer(s) ['Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {}. namedOverrides:  {}.
- Gem counts: VehicleResupplyStation 4, HQ 6, VehicleSpawner 59, StationarySpawner 10, TelemetryArea 7, CapturePoint 7, Sector 5, Collection_Event 1
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@67 [-700.6, 116.7, 308.5]; side E = HQ@32 [202.5, 115.2, -638.9]; separation 1309 m. Other HQ instances: HQ@2 [107.4, 102.0, -113.9] near CP@26 (3 m); HQ@16 [228.2, 102.7, 394.0] near CP@137 (26 m); HQ@40 [379.5, 100.4, -100.5] near CP@117 (3 m); HQ@55 [-128.4, 100.2, 178.8] near CP@28 (22 m)
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@28 [-114.4, 96.0, 161.3]; Sector@44 [-148.3, 84.2, 282.6] (126 m); polys [19, 68, 98, 111, 1]; dW 604 dE 861
  - CP@137 [222.5, 98.8, 419.7]; Sector@114 [156.5, 98.5, 408.7] (67 m); polys [91, 111, 126, 4]; dW 930 dE 1059
  - CP@36 [410.5, 100.5, 430.7]; Sector@138 [379.2, 96.4, 203.8] (229 m); polys [74, 89, 7]; dW 1118 dE 1090
  - CP@59 [224.9, 99.2, 147.0]; Sector@138 [379.2, 96.4, 203.8] (164 m); polys [89, 2]; dW 939 dE 786
  - CP@100 [498.2, 106.2, 217.2]; Sector@138 [379.2, 96.4, 203.8] (120 m); polys [77, 89, 3]; dW 1202 dE 906
  - CP@26 [106.0, 106.6, -110.8]; Sector@136 [95.3, 105.3, -99.2] (16 m); polys [30, 113, 118, 122, 5]; dW 909 dE 537
  - CP@117 [380.2, 100.3, -98.0]; Sector@101 [376.3, 100.1, -86.4] (12 m); polys [30, 62, 6]; dW 1155 dE 569
- Predicted removal order, side W (closest to HQ W first): CP@28(604) > CP@26(909) > CP@137(930) > CP@59(939) > CP@36(1118) > CP@117(1155) > CP@100(1202)
- Predicted removal order, side E (closest to HQ E first): CP@26(537) > CP@117(569) > CP@59(786) > CP@28(861) > CP@100(906) > CP@137(1059) > CP@36(1090)
  - Overlap of W top3 [28, 26, 137] and E top3 [26, 117, 59]: OVERLAP {26}. Max 5 removals before a win. Orders from nearby alternate HQ instances:  | 
- Vehicle pads total 59: AttackHelicopter 2, IFV 4, LightTransport 6, MobileAA 2, MultirolePlane 4, NavalFighterPlane 4, PTV_QuadBike 4, PatrolBoat 21, RHIB 2, Tank 6, TransportHelicopter 4
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - CP@59: 3 -> PatrolBoat 1, RHIB 2
    - HQ-E: 17 -> AttackHelicopter 1, MultirolePlane 2, NavalFighterPlane 2, PatrolBoat 10, TransportHelicopter 2
    - HQ-W: 17 -> AttackHelicopter 1, MultirolePlane 2, NavalFighterPlane 2, PatrolBoat 10, TransportHelicopter 2
    - HQ@2: 11 -> IFV 2, LightTransport 3, MobileAA 1, PTV_QuadBike 2, Tank 3
    - HQ@55: 11 -> IFV 2, LightTransport 3, MobileAA 1, PTV_QuadBike 2, Tank 3
- Stationary emplacements: 10 -> @7 StationarySpawner_AntiTank [113.2, 103.1, -39.2] (CP@26 72 m); @8 StationarySpawner_AntiTank [229.2, 98.9, 297.1] (HQ@16 97 m); @15 StationarySpawner_AntiAircraft [470.0, 107.2, 112.8] (CP@100 108 m); @41 StationarySpawner_AntiAircraft [449.4, 104.0, 478.0] (CP@36 61 m); @48 StationarySpawner_AntiTank [546.9, 112.7, 481.0] (CP@36 145 m); @49 StationarySpawner_AntiTank [472.8, 107.2, 90.8] (CP@100 129 m); @66 StationarySpawner_HMG [444.6, 106.8, 109.9] (CP@100 120 m); @107 StationarySpawner_AntiTank [361.6, 100.1, -47.0] (CP@117 54 m); @127 StationarySpawner_AntiAircraft [81.0, 100.0, -14.0] (CP@26 100 m); @128 StationarySpawner_HMG [108.1, 106.6, -92.9] (CP@26 18 m)
- Vehicle resupply stations: 4 -> @1 VehicleResupplyStation_Air [205.3, 135.7, -632.0] (HQ-E 7 m); @21 VehicleResupplyStation_Air [-699.9, 135.6, 310.0] (HQ-W 2 m); @39 VehicleResupplyStation [0.8, 99.5, -171.2] (HQ@2 121 m); @129 VehicleResupplyStation [-307.9, 99.7, 76.0] (HQ@55 207 m)
- Collection_Event: 1 -> @60 CollectionEvent [0.0, 0.0, 0.0] (CP@26 153 m)
- CapturePoint_OutlineArea: 0 for 7 flags (flags with no outline within 15 m: [26, 28, 36, 59, 100, 117, 137])
- TelemetryArea: 7
- Combat area: no CombatArea/SpecialCombatArea instance in the Escalation layer

### Iberian Offensive (MP_BATTERY)
- Layer assets: Escalation, Escalation_Global, Escalation_Global_Schematic, MP_Escalation0, MP_Escalation0_Schematic, MeshVariationDb_Win32. Instances sit in layer(s) ['MP_Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}. namedOverrides:  {}.
- Gem counts: CapturePoint_OutlineArea 5, Sector 7, VehicleSpawner 8, VehicleSpawner_Forward 3, HQ 6, CapturePoint 7, Collection_Event 1, Battle_Pickup 2
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@23 [576.4, 69.5, 110.7]; side E = HQ@73 [920.1, 74.8, 134.5]; separation 345 m. Other HQ instances: HQ@48 [675.5, 78.1, 219.1] near CP@43 (40 m); HQ@76 [920.1, 74.8, 134.5] duplicate of HQ@73 (CP@62 is 85 m away); HQ@85 [618.5, 76.6, 174.9] near CP@43 (34 m); HQ@102 [920.1, 74.8, 134.5] duplicate of HQ@73
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@43 [639.8, 75.6, 201.4]; Sector@21 [633.6, 75.5, 195.1] (9 m); polys [55]; dW 111 dE 288
  - CP@58 [706.2, 75.0, 98.3]; Sector@122 [721.9, 74.9, 95.4] (16 m); polys [19]; dW 130 dE 217
  - CP@101 [722.6, 79.1, 174.7]; Sector@3 [699.5, 79.1, 188.8] (27 m); polys [37, 116]; dW 160 dE 202
  - CP@52 [769.3, 78.4, 68.3]; Sector@35 [784.6, 77.4, 74.2] (16 m); polys [19, 124]; dW 198 dE 165
  - CP@30 [778.6, 82.2, 157.4]; Sector@98 [765.4, 78.2, 125.0] (35 m); polys [19]; dW 208 dE 143
  - CP@62 [861.3, 74.4, 73.2]; Sector@115 [829.2, 80.0, 53.5] (38 m); polys [27, 79]; dW 287 dE 85
  - CP@39 [871.3, 85.7, 208.8]; Sector@2 [866.0, 85.6, 210.0] (5 m); polys [22]; dW 311 dE 89
- Predicted removal order, side W (closest to HQ W first): CP@43(111) > CP@58(130) > CP@101(160) > CP@52(198) > CP@30(208) > CP@62(287) > CP@39(311)
- Predicted removal order, side E (closest to HQ E first): CP@62(85) > CP@39(89) > CP@30(143) > CP@52(165) > CP@101(202) > CP@58(217) > CP@43(288)
  - Overlap of W top3 [43, 58, 101] and E top3 [62, 39, 30]: none. Max 5 removals before a win. Orders from nearby alternate HQ instances: W-cluster HQ@85: 43>101>58>30>52>39>62 | E duplicate HQ@76: 62>39>30>52>101>58>43; E duplicate HQ@102: 62>39>30>52>101>58>43
- Vehicle pads total 8: IFV 2, LightTransport 4, Tank 2
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - HQ-E: 4 -> IFV 1, LightTransport 2, Tank 1
    - HQ-W: 4 -> IFV 1, LightTransport 2, Tank 1
- Forward spawners: 3 -> @18 Forward [575.9, 69.5, 106.4] (HQ-W 4 m); @114 Forward [571.4, 69.5, 117.8] (HQ-W 9 m); @128 Forward [584.2, 69.5, 116.6] (HQ-W 10 m)
- Battle_Pickup (placed, not active in live game): 2 -> @89 Battle_Pickup_Minigun [786.8, 78.5, 50.0] (CP@52 25 m); @123 Battle_Pickup_Minigun [686.4, 79.0, 98.3] (CP@58 20 m)
- Collection_Event: 1 -> @71 CollectionEvent [0.0, 0.0, 0.0] (HQ-W 587 m)
- CapturePoint_OutlineArea: 5 for 7 flags (flags with no outline within 15 m: [30, 39, 43, 58])
- TelemetryArea: 0
- Combat area: no CombatArea/SpecialCombatArea instance in the Escalation layer

### Liberation Peak (MP_CAPSTONE)
- Layer assets: Escalation, Escalation_Global, Escalation_Global_Schematic, Escalation_Telemetry, MP_Escalation0, MP_Escalation0_Schematic, MeshVariationDb_Win32. Instances sit in layer(s) ['MP_Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {}. namedOverrides:  {}.
- Gem counts: VehicleSpawner 36, HQ 6, CapturePoint 7, TelemetryArea 13, CapturePoint_OutlineArea 3, Sector 7, Battle_Pickup 2
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@6 [-311.6, 130.3, 99.8]; side E = HQ@108 [275.1, 139.0, 451.1]; separation 684 m. Other HQ instances: HQ@39 [-70.7, 134.5, 91.2] near CP@9 (41 m); HQ@92 [149.4, 172.1, 352.0] near CP@155 (9 m); HQ@103 [191.3, 138.3, 180.5] near CP@124 (6 m); HQ@133 [-174.4, 137.7, 150.0] near CP@149 (26 m)
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@149 [-153.4, 137.4, 166.1]; Sector@116 [-173.1, 137.7, 151.3] (25 m); polys [34, 91, 100]; dW 172 dE 515
  - CP@9 [-30.1, 134.5, 89.8]; Sector@162 [-43.8, 134.5, 94.8] (15 m); polys [34, 97]; dW 282 dE 473
  - CP@28 [52.9, 137.8, 100.0]; Sector@125 [57.0, 137.3, 96.2] (6 m); polys [65, 184]; dW 365 dE 416
  - CP@137 [51.0, 158.4, 209.0]; Sector@84 [33.2, 158.2, 208.8] (18 m); polys [99, 184]; dW 379 dE 330
  - CP@29 [154.3, 129.7, 63.0]; Sector@127 [158.8, 130.1, 78.0] (16 m); polys [82, 184]; dW 467 dE 406
  - CP@124 [185.7, 138.3, 180.1]; Sector@188 [206.1, 138.5, 195.0] (25 m); polys [62, 113]; dW 504 dE 285
  - CP@155 [142.4, 173.1, 346.3]; Sector@74 [145.4, 171.4, 341.2] (6 m); polys [63, 96, 113]; dW 517 dE 169
- Predicted removal order, side W (closest to HQ W first): CP@149(172) > CP@9(282) > CP@28(365) > CP@137(379) > CP@29(467) > CP@124(504) > CP@155(517)
- Predicted removal order, side E (closest to HQ E first): CP@155(169) > CP@124(285) > CP@137(330) > CP@29(406) > CP@28(416) > CP@9(473) > CP@149(515)
  - Overlap of W top3 [149, 9, 28] and E top3 [155, 124, 137]: none. Max 5 removals before a win. Orders from nearby alternate HQ instances:  | 
- Vehicle pads total 36: AttackHelicopter 2, AttackPlane 2, FighterPlane 2, IFV 4, LightTransport 14, PTV_DirtBike 4, PTV_QuadBike 4, Tank 4
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - CP@137: 1 -> LightTransport 1
    - CP@149: 1 -> LightTransport 1
    - CP@155: 1 -> LightTransport 1
    - CP@28: 1 -> LightTransport 1
    - HQ-E: 15 -> AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 2, LightTransport 4, PTV_DirtBike 2, PTV_QuadBike 2, Tank 2
    - HQ-W: 15 -> AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 2, LightTransport 4, PTV_DirtBike 2, PTV_QuadBike 2, Tank 2
    - HQ@103: 1 -> LightTransport 1
    - HQ@39: 1 -> LightTransport 1
- Battle_Pickup (placed, not active in live game): 2 -> @153 Battle_Pickup_Railgun [32.4, 168.2, 236.6] (CP@137 33 m); @169 Battle_Pickup_Minigun [77.3, 134.2, 80.5] (CP@28 31 m)
- CapturePoint_OutlineArea: 3 for 7 flags (flags with no outline within 15 m: [9, 124, 149, 155])
- TelemetryArea: 13
- Combat area: no CombatArea/SpecialCombatArea instance in the Escalation layer

### Contaminated (MP_CONTAMINATED)
- Layer assets: Escalation, Escalation0, Escalation_Gas, Escalation_GasPlacement, Escalation_GasPlacement_Schematic, Escalation_Global, Escalation_Global_Schematic, MeshVariationDb_Win32. Instances sit in layer(s) ['Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {}. namedOverrides:  {}.
- Gem counts: Battle_Pickup 3, AutomaticAA 2, Sector 7, VehicleSpawner 38, StationarySpawner 10, Insertion 16, VehicleResupplyStation 4, CapturePoint_OutlineArea 3, TelemetryArea 7, CapturePoint 7, HQ 6, Collection_Event 1, PsyGasZone 9, SpecialCombatArea 1
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@114 [-151.0, 332.7, -232.4]; side E = HQ@128 [434.5, 310.4, 189.7]; separation 722 m. Other HQ instances: HQ@54 [304.8, 296.6, 177.4] near CP@113 (86 m); HQ@91 [-103.7, 331.3, -150.0] near CP@212 (58 m); HQ@183 [337.7, 324.6, 91.3] near CP@111 (55 m); HQ@232 [-164.5, 324.1, -21.8] near CP@89 (39 m)
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@212 [-60.8, 331.2, -111.5]; Sector@220 [-8.3, 64.3, 62.6] (182 m); polys [35, 43, 228]; dW 151 dE 580
  - CP@89 [-153.6, 322.9, 15.8]; Sector@220 [-8.3, 64.3, 62.6] (153 m); polys [43, 74, 237]; dW 248 dE 613
  - CP@41 [-29.7, 323.3, 39.6]; Sector@220 [-8.3, 64.3, 62.6] (31 m); polys [43, 154, 173]; dW 298 dE 488
  - CP@224 [10.2, 321.9, 248.0]; Sector@175 [110.5, 64.3, 182.7] (120 m); polys [43, 84, 154, 185]; dW 507 dE 428
  - CP@231 [148.9, 309.9, 100.8]; Sector@101 [141.2, 64.3, 110.9] (13 m); polys [43, 62, 154, 162]; dW 448 dE 299
  - CP@111 [302.2, 334.0, 49.0]; Sector@202 [255.9, 64.3, 50.6] (46 m); polys [17, 43, 244, 3]; dW 533 dE 193
  - CP@113 [220.1, 300.3, 191.7]; Sector@11 [268.1, 64.3, 220.9] (56 m); polys [43, 144, 145, 5]; dW 564 dE 214
- Predicted removal order, side W (closest to HQ W first): CP@212(151) > CP@89(248) > CP@41(298) > CP@231(448) > CP@224(507) > CP@111(533) > CP@113(564)
- Predicted removal order, side E (closest to HQ E first): CP@111(193) > CP@113(214) > CP@231(299) > CP@224(428) > CP@41(488) > CP@212(580) > CP@89(613)
  - Overlap of W top3 [212, 89, 41] and E top3 [111, 113, 231]: none. Max 5 removals before a win. Orders from nearby alternate HQ instances: W-cluster HQ@91: 212>89>41>231>224>111>113 | 
- Vehicle pads total 38: AttackHelicopter 2, AttackPlane 2, FighterPlane 2, IFV 4, LightTransport 6, MobileAA 2, PTV_DirtBike 12, ScoutHelicopter 4, Tank 4
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - CP@212: 1 -> PTV_DirtBike 1
    - CP@224: 2 -> PTV_DirtBike 2
    - CP@231: 1 -> PTV_DirtBike 1
    - CP@41: 1 -> PTV_DirtBike 1
    - HQ-E: 17 -> AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 2, LightTransport 3, MobileAA 1, PTV_DirtBike 4, ScoutHelicopter 2, Tank 2
    - HQ-W: 16 -> AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 2, LightTransport 3, MobileAA 1, PTV_DirtBike 3, ScoutHelicopter 2, Tank 2
- Stationary emplacements: 10 -> @13 StationarySpawner_AntiTank [299.9, 296.8, 222.9] (HQ@54 46 m); @16 StationarySpawner_AntiTank [-149.0, 323.0, 3.3] (CP@89 13 m); @20 StationarySpawner_AntiTank [268.0, 338.5, 23.7] (CP@111 43 m); @45 StationarySpawner_AntiTank [-72.3, 327.5, 216.2] (CP@224 88 m); @107 StationarySpawner_HMG [-16.9, 323.3, 52.3] (CP@41 18 m); @160 StationarySpawner_AntiTank [61.0, 317.1, 307.1] (CP@224 78 m); @190 StationarySpawner_AntiAircraft [-4.5, 321.5, 239.0] (CP@224 17 m); @204 StationarySpawner_HMG [108.0, 310.2, 74.6] (CP@231 49 m); @222 StationarySpawner_AntiTank [-63.5, 331.3, -83.8] (CP@212 28 m); @238 StationarySpawner_AntiTank [-85.2, 330.9, -153.8] (HQ@91 19 m, a W-cluster HQ; 103 m from the initial W HQ@114)
- Vehicle resupply stations: 4 -> @19 VehicleResupplyStation_Air [429.0, 310.5, 203.3] (HQ-E 15 m); @44 VehicleResupplyStation [422.2, 310.5, 175.7] (HQ-E 19 m); @72 VehicleResupplyStation_Air [-167.3, 334.4, -261.5] (HQ-W 33 m); @168 VehicleResupplyStation [-133.3, 332.3, -220.3] (HQ-W 21 m)
- AutomaticAA: 2 -> @2 AutomaticAA [440.5, 312.1, 196.3] (HQ-E 9 m); @192 AutomaticAA [-192.0, 335.7, -286.7] (HQ-W 68 m)
- Battle_Pickup (placed, not active in live game): 3 -> @1 Battle_Pickup_Minigun [174.0, 310.1, 101.2] (CP@231 25 m); @93 Battle_Pickup_Railgun [17.2, 325.7, 255.1] (CP@224 10 m); @225 Battle_Pickup_Minigun [-47.6, 323.4, 41.5] (CP@41 18 m)
- Collection_Event: 1 -> @76 CollectionEvent [0.0, 0.0, 0.0] (CP@41 50 m)
- Insertion: 16 -> {'Insertion_Cautious_OnSpot_v1': 6, 'Insertion_Cautious_OnSpot_v2': 6, 'Insertion_Cautious_OnSpot_v3': 4}; nearer HQ W 8, nearer HQ E 8
- CapturePoint_OutlineArea: 3 for 7 flags (flags with no outline within 15 m: [41, 111, 113, 212, 224, 231])
- TelemetryArea: 7
- SpecialCombatArea@147 pos [75.4, 319.4, 395.4]; polys POLY@43 bbox[-383, -396, 604, 523] (only combat-area object in the layer)

### Manhattan Bridge (MP_DUMBO)
- Layer assets: Escalation, Escalation_Art, Escalation_Art_Schematic, Escalation_Global, Escalation_Global_Schematic, Escalation_VFX, Escalation_VFX_Schematic, MP_Escalation0, MP_Escalation0_Schematic, MeshVariationDb_Win32, MeshVariationDb_Win32, staticmodelgroup.physics. Instances sit in layer(s) ['MP_Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {}. namedOverrides:  {}.
- Gem counts: VehicleSpawner 32, HQ 6, Insertion 16, Sector 7, VehicleResupplyStation 4, CapturePoint 7, TelemetryArea 7, CapturePoint_OutlineArea 1, Battle_Pickup 2, Collection_Event 1
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@12 [-262.4, 52.0, -435.2]; side E = HQ@9 [179.2, 57.3, -243.2]; separation 482 m. Other HQ instances: HQ@4 [65.0, 59.2, -240.1] near CP@165 (26 m); HQ@110 [82.3, 55.0, -350.4] near CP@19 (5 m); HQ@145 [-148.5, 53.9, -352.0] near CP@62 (0 m); HQ@153 [-166.2, 55.0, -463.6] near CP@49 (38 m)
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@49 [-128.6, 53.6, -457.6]; Sector@162 [-128.5, 65.1, -457.6] (0 m); polys [1, 37]; dW 136 dE 375
  - CP@62 [-148.5, 53.9, -352.0]; Sector@32 [-149.6, 56.1, -352.8] (1 m); polys [98]; dW 141 dE 345
  - CP@167 [-27.5, 79.7, -449.9]; Sector@7 [-32.2, 82.8, -452.7] (5 m); polys [122]; dW 235 dE 292
  - CP@111 [-41.4, 54.7, -345.0]; Sector@23 [-44.4, 59.9, -346.9] (4 m); polys [122]; dW 239 dE 243
  - CP@15 [-39.0, 56.0, -243.8]; Sector@180 [-37.8, 56.5, -243.8] (1 m); polys [122]; dW 294 dE 218
  - CP@19 [81.3, 55.0, -345.6]; Sector@176 [82.3, 56.6, -351.0] (5 m); polys [132]; dW 355 dE 142
  - CP@165 [44.8, 59.2, -224.0]; Sector@68 [44.8, 71.4, -223.6] (0 m); polys [93, 156, 172]; dW 373 dE 136
- Predicted removal order, side W (closest to HQ W first): CP@49(136) > CP@62(141) > CP@167(235) > CP@111(239) > CP@15(294) > CP@19(355) > CP@165(373)
- Predicted removal order, side E (closest to HQ E first): CP@165(136) > CP@19(142) > CP@15(218) > CP@111(243) > CP@167(292) > CP@62(345) > CP@49(375)
  - Overlap of W top3 [49, 62, 167] and E top3 [165, 19, 15]: none. Max 5 removals before a win. Orders from nearby alternate HQ instances: W-cluster HQ@153: 49>62>167>111>15>19>165 | E-cluster HQ@4: 165>15>19>111>167>62>49
- Vehicle pads total 32: AttackHelicopter 2, IFV 4, LightTransport 10, MobileAA 2, PTV_QuadBike 8, ScoutHelicopter 2, Tank 4
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - CP@111: 2 -> PTV_QuadBike 2
    - CP@165: 1 -> LightTransport 1
    - CP@62: 1 -> PTV_QuadBike 1
    - HQ-E: 13 -> AttackHelicopter 1, IFV 2, LightTransport 4, MobileAA 1, PTV_QuadBike 2, ScoutHelicopter 1, Tank 2
    - HQ-W: 14 -> AttackHelicopter 1, IFV 2, LightTransport 5, MobileAA 1, PTV_QuadBike 2, ScoutHelicopter 1, Tank 2
    - HQ@110: 1 -> PTV_QuadBike 1
- Vehicle resupply stations: 4 -> @10 VehicleResupplyStation [-230.4, 52.1, -435.2] (HQ-W 32 m); @72 VehicleResupplyStation_Air [167.7, 60.2, -217.0] (HQ-E 29 m); @73 VehicleResupplyStation_Air [-312.5, 54.6, -445.4] (HQ-W 51 m); @149 VehicleResupplyStation [158.4, 58.0, -248.0] (HQ-E 21 m)
- Battle_Pickup (placed, not active in live game): 2 -> @79 Battle_Pickup_Minigun [-36.0, 73.9, -476.6] (CP@167 28 m); @90 Battle_Pickup_Minigun [-51.3, 64.0, -220.8] (CP@15 26 m)
- Collection_Event: 1 -> @105 CollectionEvent [0.0, 0.0, 0.0] (CP@165 228 m)
- Insertion: 16 -> {'Insertion_Cautious_OnSpot_v1': 7, 'Insertion_Cautious_OnSpot_v3': 5, 'Insertion_Cautious_OnSpot_v2': 4}; nearer HQ W 8, nearer HQ E 8
- CapturePoint_OutlineArea: 1 for 7 flags (flags with no outline within 15 m: [15, 19, 49, 62, 111, 167])
- TelemetryArea: 7
- Combat area: no CombatArea/SpecialCombatArea instance in the Escalation layer

### Eastwood (MP_EASTWOOD)
- Layer assets: Escalation, Escalation_Global, Escalation_Global_Schematic, MP_Escalation0, MP_Escalation0_Schematic, MeshVariationDb_Win32, staticmodelgroup.physics. Instances sit in layer(s) ['MP_Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {"team1": "Alliance/NATO", "team2": "Coalition/Pax Armata"}. namedOverrides:  {}.
- Gem counts: VehicleSpawner 53, Insertion 16, StationarySpawner 9, Sector 7, CapturePoint 7, TelemetryArea 7, HQ 6, Battle_Pickup 3, Collection_Event 1, SpecialCombatArea 1, VehicleResupplyStation 4, CapturePoint_OutlineArea 2
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@117 [-401.4, 226.4, 121.7]; side E = HQ@235 [378.3, 241.8, -159.6]; separation 829 m. Other HQ instances: HQ@72 [-223.1, 231.4, 39.5] near CP@295 (55 m); HQ@161 [-139.7, 231.5, -28.5] near CP@295 (53 m); HQ@186 [315.3, 233.1, -62.6] near CP@168 (85 m); HQ@196 [193.6, 236.9, -135.2] near CP@61 (37 m)
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@295 [-178.9, 233.2, 7.5]; Sector@76 [-181.8, 233.1, 16.5] (9 m); polys [69, 193]; dW 250 dE 582
  - CP@103 [-76.3, 235.2, 168.2]; Sector@45 [-95.8, 234.4, 165.3] (20 m); polys [1, 47]; dW 328 dE 560
  - CP@282 [13.4, 233.6, 12.0]; Sector@286 [9.1, 231.6, 67.1] (55 m); polys [22, 238]; dW 429 dE 403
  - CP@152 [85.0, 234.3, 37.3]; Sector@115 [69.8, 234.3, 19.8] (23 m); polys [22, 130]; dW 494 dE 353
  - CP@302 [77.2, 233.1, -33.7]; Sector@251 [79.7, 234.7, -30.0] (4 m); polys [22, 132]; dW 503 dE 326
  - CP@168 [270.4, 232.7, 9.2]; Sector@303 [300.8, 232.7, -10.8] (36 m); polys [277, 324]; dW 681 dE 200
  - CP@61 [197.8, 240.1, -172.2]; Sector@53 [160.8, 244.0, -153.3] (42 m); polys [24, 97]; dW 667 dE 181
- Predicted removal order, side W (closest to HQ W first): CP@295(250) > CP@103(328) > CP@282(429) > CP@152(494) > CP@302(503) > CP@61(667) > CP@168(681)
- Predicted removal order, side E (closest to HQ E first): CP@61(181) > CP@168(200) > CP@302(326) > CP@152(353) > CP@282(403) > CP@103(560) > CP@295(582)
  - Overlap of W top3 [295, 103, 282] and E top3 [61, 168, 302]: none. Max 5 removals before a win. Orders from nearby alternate HQ instances:  | E-cluster HQ@186: 168>61>302>152>282>103>295
- Vehicle pads total 53: APC 4, AttackHelicopter 2, IFV 4, LightTransport 14, MobileAA 4, PTV_GolfCart 7, PTV_QuadBike 8, ScoutHelicopter 2, Tank 6, TransportHelicopter 2
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - CP@103: 2 -> LightTransport 1, PTV_GolfCart 1
    - CP@152: 4 -> PTV_GolfCart 4
    - CP@168: 3 -> LightTransport 1, PTV_GolfCart 2
    - CP@282: 1 -> LightTransport 1
    - CP@295: 1 -> LightTransport 1
    - CP@302: 1 -> LightTransport 1
    - CP@61: 1 -> LightTransport 1
    - HQ-E: 20 -> APC 2, AttackHelicopter 1, IFV 2, LightTransport 4, MobileAA 2, PTV_QuadBike 4, ScoutHelicopter 1, Tank 3, TransportHelicopter 1
    - HQ-W: 20 -> APC 2, AttackHelicopter 1, IFV 2, LightTransport 4, MobileAA 2, PTV_QuadBike 4, ScoutHelicopter 1, Tank 3, TransportHelicopter 1
- Stationary emplacements: 9 -> @20 StationarySpawner_AntiTank [-15.6, 236.6, 171.7] (CP@103 61 m); @38 StationarySpawner_AntiAircraft [-74.1, 235.4, 122.0] (CP@103 46 m); @86 StationarySpawner_AntiTank [121.6, 235.0, -121.8] (HQ@196 73 m); @150 StationarySpawner_AntiTank [-114.0, 234.1, 143.1] (CP@103 45 m); @166 StationarySpawner_HMG [94.3, 234.3, -1.1] (CP@302 37 m); @171 StationarySpawner_AntiTank [-6.8, 231.9, -37.2] (CP@282 53 m); @175 StationarySpawner_AntiAircraft [159.7, 240.1, -153.1] (HQ@196 38 m); @300 StationarySpawner_AntiTank [260.4, 232.2, 36.5] (CP@168 29 m); @319 StationarySpawner_HMG [37.3, 234.3, 42.5] (CP@282 39 m)
- Vehicle resupply stations: 4 -> @206 VehicleResupplyStation [361.3, 241.3, -151.9] (HQ-E 19 m); @214 VehicleResupplyStation_Air [409.9, 244.9, -195.0] (HQ-E 47 m); @259 VehicleResupplyStation [-372.5, 226.7, 112.1] (HQ-W 30 m); @280 VehicleResupplyStation_Air [-430.3, 226.4, 147.5] (HQ-W 39 m)
- Battle_Pickup (placed, not active in live game): 3 -> @129 Battle_Pickup_Railgun [12.0, 232.2, 83.7] (CP@282 72 m); @136 Battle_Pickup_Minigun [59.9, 244.6, 12.9] (CP@152 35 m); @225 Battle_Pickup_Railgun [148.8, 233.2, -63.0] (CP@302 77 m)
- Collection_Event: 1 -> @192 CollectionEvent [0.0, 0.0, 0.0] (CP@282 18 m)
- Insertion: 16 -> {'Insertion_Cautious_OnSpot_v3': 3, 'Insertion_Cautious_OnSpot_v1': 2, 'Insertion_Cautious_OnSpot_v4_NOT_FOR_REVEAL': 5, 'Insertion_Cautious_Arrival_Corner': 2, 'Insertion_Cautious_Arrival': 4}; nearer HQ W 8, nearer HQ E 8
- CapturePoint_OutlineArea: 2 for 7 flags (flags with no outline within 15 m: [61, 103, 152, 168, 295])
- TelemetryArea: 7
- SpecialCombatArea@199 pos [13.5, 233.8, 7.9]; polys POLY@22 bbox[-66, -160, 279, 326]; POLY@238 bbox[-7, -6, 38, 32] (only combat-area object in the layer)

### Operation Firestorm (MP_FIRESTORM)
- Layer assets: Escalation, Escalation_Cover, Escalation_Global, Escalation_Global_Schematic, Escalation_Telemetry, MP_Escalation0, MP_Escalation0_Schematic, MeshVariationDb_Win32. Instances sit in layer(s) ['MP_Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}. namedOverrides:  {}.
- Gem counts: Insertion 16, VehicleSpawner 54, TelemetryArea 7, CapturePoint 7, CapturePoint_OutlineArea 4, VehicleResupplyStation 10, AutomaticAA 4, HQ 6, Battle_Pickup 3, Sector 7, SpecialCombatArea 1, Collection_Event 1
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@93 [-758.2, 132.9, 208.6]; side E = HQ@68 [559.8, 110.5, -230.2]; separation 1389 m. Other HQ instances: HQ@106 [-504.3, 136.6, 57.1] near CP@222 (38 m); HQ@237 [368.9, 112.8, -119.2] near CP@64 (39 m); HQ@255 [-504.4, 136.6, 61.1] near CP@222 (39 m); HQ@318 [368.9, 112.7, -116.9] near CP@64 (37 m)
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@222 [-465.9, 137.0, 54.4]; Sector@146 [-462.5, 137.5, 45.9] (9 m); polys [57, 99, 111, 323]; dW 330 dE 1064
  - CP@300 [-279.6, 134.0, -61.8]; Sector@149 [-282.6, 133.7, -47.7] (14 m); polys [7, 98, 99]; dW 550 dE 856
  - CP@36 [-196.3, 125.5, 48.9]; Sector@138 [-201.0, 125.5, 48.9] (5 m); polys [18, 89]; dW 584 dE 806
  - CP@103 [-61.0, 122.7, -4.7]; Sector@320 [-52.1, 122.5, -6.4] (9 m); polys [89, 215]; dW 729 dE 660
  - CP@23 [127.5, 122.4, 74.4]; Sector@315 [132.0, 122.4, 77.5] (5 m); polys [83, 157, 230]; dW 896 dE 529
  - CP@266 [81.7, 120.2, -67.6]; Sector@256 [76.7, 120.1, -63.5] (6 m); polys [89, 283]; dW 884 dE 505
  - CP@64 [335.0, 113.3, -100.9]; Sector@219 [328.9, 113.8, -114.9] (15 m); polys [22, 84, 107, 230]; dW 1136 dE 259
- Predicted removal order, side W (closest to HQ W first): CP@222(330) > CP@300(550) > CP@36(584) > CP@103(729) > CP@266(884) > CP@23(896) > CP@64(1136)
- Predicted removal order, side E (closest to HQ E first): CP@64(259) > CP@266(505) > CP@23(529) > CP@103(660) > CP@36(806) > CP@300(856) > CP@222(1064)
  - Overlap of W top3 [222, 300, 36] and E top3 [64, 266, 23]: none. Max 5 removals before a win. Orders from nearby alternate HQ instances:  | 
- Vehicle pads total 54: AttackHelicopter 2, AttackPlane 2, FighterPlane 2, IFV 8, LightTransport 12, MobileAA 4, PTV_DirtBike 14, ScoutHelicopter 2, Tank 6, TransportHelicopter 2
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - CP@23: 2 -> LightTransport 1, PTV_DirtBike 1
    - CP@266: 1 -> LightTransport 1
    - CP@300: 2 -> LightTransport 1, PTV_DirtBike 1
    - CP@36: 1 -> LightTransport 1
    - CP@64: 1 -> LightTransport 1
    - HQ-E: 22 -> AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 4, LightTransport 2, MobileAA 2, PTV_DirtBike 6, ScoutHelicopter 1, Tank 3, TransportHelicopter 1
    - HQ-W: 22 -> AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 4, LightTransport 2, MobileAA 2, PTV_DirtBike 6, ScoutHelicopter 1, Tank 3, TransportHelicopter 1
    - HQ@106: 1 -> LightTransport 1
    - HQ@255: 1 -> LightTransport 1
    - HQ@318: 1 -> LightTransport 1
- Vehicle resupply stations: 10 -> @32 VehicleResupplyStation [338.7, 113.0, -113.8] (CP@64 13 m); @48 VehicleResupplyStation [172.3, 122.3, 122.4] (CP@23 66 m); @55 VehicleResupplyStation [18.7, 121.3, -92.7] (CP@266 68 m); @120 VehicleResupplyStation [-475.4, 136.7, 50.4] (CP@222 10 m); @147 VehicleResupplyStation [-255.2, 133.9, -139.8] (CP@300 82 m); @190 VehicleResupplyStation [557.4, 111.3, -212.9] (HQ-E 17 m); @220 VehicleResupplyStation_Air [-633.6, 132.2, 330.7] (HQ-W 174 m); @250 VehicleResupplyStation_Air [523.9, 110.6, -364.9] (HQ-E 139 m); @292 VehicleResupplyStation [-185.1, 124.8, 118.4] (CP@36 70 m); @326 VehicleResupplyStation [-736.9, 132.9, 173.9] (HQ-W 41 m)
- AutomaticAA: 4 -> @34 AutomaticAA [576.7, 113.8, -280.3] (HQ-E 53 m); @127 AutomaticAA [-534.0, 139.3, 80.6] (HQ@255 35 m); @132 AutomaticAA [-719.7, 134.6, 212.4] (HQ-W 39 m); @186 AutomaticAA [384.3, 116.4, -144.1] (HQ@237 29 m)
- Battle_Pickup (placed, not active in live game): 3 -> @82 Battle_Pickup_Minigun [-79.1, 130.1, -63.3] (CP@103 61 m); @164 Battle_Pickup_Railgun [85.1, 125.8, -156.1] (CP@266 89 m); @191 Battle_Pickup_Railgun [-232.1, 130.7, 60.3] (CP@36 38 m)
- Collection_Event: 1 -> @314 CollectionEvent [0.0, 0.0, 0.0] (CP@103 61 m)
- Insertion: 16 -> {'Insertion_Cautious_LongDistance': 5, 'Insertion_Cautious_OnSpot_v3': 3, 'Insertion_Cautious_Arrival': 3, 'Insertion_Cautious_OnSpot_v1': 3, 'Insertion_Cautious_OnSpot_v2': 2}; nearer HQ W 8, nearer HQ E 8
- CapturePoint_OutlineArea: 4 for 7 flags (flags with no outline within 15 m: [23, 64, 103, 222, 266, 300])
- TelemetryArea: 7
- SpecialCombatArea@229 pos [0.0, 0.0, 0.0]; polys POLY@89 bbox[-375, -350, 197, 289] (only combat-area object in the layer)

### Tsuru Reef (MP_ISOLATED)
- Layer assets: Escalation, Escalation0, Escalation_Global, Escalation_Global_Schematic, Escalation_Telemetry, MeshVariationDb_Win32, staticmodelgroup.physics. Instances sit in layer(s) ['Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}. namedOverrides:  {}.
- Gem counts: StationarySpawner 3, VehicleSpawner 47, Sector 5, HQ 6, CapturePoint 9, VehicleResupplyStation 2, Collection_Event 1
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@94 [-1155.9, 102.5, 843.3]; side E = HQ@21 [-436.1, 103.4, -678.5]; separation 1683 m. Other HQ instances: HQ@9 [-652.0, 108.7, 438.2] near CP@22 (14 m); HQ@54 [-590.4, 104.7, -162.8] near CP@87 (31 m); HQ@75 [-465.5, 101.0, -328.7] near CP@74 (194 m); HQ@96 [-869.1, 102.4, 512.1] near CP@55 (4 m)
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@55 [-872.7, 102.4, 510.4]; Sector@98 [-882.2, 102.4, 484.6] (27 m); polys [33, 39, 72]; dW 437 dE 1267
  - CP@56 [-932.6, 101.2, 325.1]; Sector@98 [-882.2, 102.4, 484.6] (167 m); polys [59, 72]; dW 564 dE 1120
  - CP@22 [-641.8, 108.6, 428.2]; Sector@47 [-658.7, 108.4, 432.3] (17 m); polys [59, 72]; dW 661 dE 1126
  - CP@24 [-813.7, 117.7, 211.8]; Sector@101 [-916.7, 132.5, 65.9] (179 m); polys [12]; dW 718 dE 967
  - CP@27 [-1054.2, 110.9, -10.7]; Sector@101 [-916.7, 132.5, 65.9] (157 m); polys [12]; dW 860 dE 910
  - CP@26 [-805.5, 108.2, -14.5]; Sector@101 [-916.7, 132.5, 65.9] (137 m); polys [12]; dW 927 dE 760
  - CP@16 [-864.9, 103.0, -286.1]; Sector@5 [-628.1, 101.9, -313.2] (238 m); polys [67, 85]; dW 1166 dE 581
  - CP@87 [-611.4, 103.7, -185.0]; Sector@32 [-587.6, 104.7, -160.1] (34 m); polys [67, 85]; dW 1164 dE 524
  - CP@74 [-658.8, 101.9, -310.9]; Sector@5 [-628.1, 101.9, -313.2] (31 m); polys [13, 85, 93]; dW 1257 dE 430
- Predicted removal order, side W (closest to HQ W first): CP@55(437) > CP@56(564) > CP@22(661) > CP@24(718) > CP@27(860) > CP@26(927) > CP@87(1164) > CP@16(1166) > CP@74(1257)
- Predicted removal order, side E (closest to HQ E first): CP@74(430) > CP@87(524) > CP@16(581) > CP@26(760) > CP@27(910) > CP@24(967) > CP@56(1120) > CP@22(1126) > CP@55(1267)
  - Overlap of W top3 [55, 56, 22] and E top3 [74, 87, 16]: none. Max 5 removals before a win. Orders from nearby alternate HQ instances:  | 
- Vehicle pads total 47: APC 1, AttackPlane 2, FighterPlane 2, IFV 4, LightTransport 2, PTV_DirtBike 4, PTV_QuadBike 6, PatrolBoat 6, RHIB 12, Tank 4, TransportHelicopter 4
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - CP@16: 1 -> RHIB 1
    - CP@24: 3 -> PTV_QuadBike 3
    - CP@26: 2 -> PTV_DirtBike 1, PTV_QuadBike 1
    - CP@27: 1 -> PTV_QuadBike 1
    - CP@56: 1 -> RHIB 1
    - CP@74: 1 -> LightTransport 1
    - HQ-E: 12 -> AttackPlane 1, FighterPlane 1, PatrolBoat 3, RHIB 5, TransportHelicopter 2
    - HQ-W: 12 -> AttackPlane 1, FighterPlane 1, PatrolBoat 3, RHIB 5, TransportHelicopter 2
    - HQ@54: 2 -> LightTransport 1, PTV_DirtBike 1
    - HQ@75: 4 -> IFV 2, Tank 2
    - HQ@9: 2 -> PTV_DirtBike 1, PTV_QuadBike 1
    - HQ@96: 6 -> APC 1, IFV 2, PTV_DirtBike 1, Tank 2
- Stationary emplacements: 3 -> @1 StationarySpawner_AntiTank [-816.9, 103.5, -107.5] (CP@26 94 m); @77 StationarySpawner_HMG [-855.3, 121.8, 132.1] (CP@24 90 m); @80 StationarySpawner_AntiTank [-856.8, 101.2, 549.5] (HQ@96 39 m)
- Vehicle resupply stations: 2 -> @76 VehicleResupplyStation [-695.4, 103.8, -64.6] (CP@26 121 m); @95 VehicleResupplyStation [-796.1, 102.5, 484.5] (HQ@96 78 m)
- Collection_Event: 1 -> @97 CollectionEvent [0.0, 0.0, 0.0] (HQ@75 570 m)
- CapturePoint_OutlineArea: 0 for 9 flags (flags with no outline within 15 m: [16, 22, 24, 26, 27, 55, 56, 74, 87])
- TelemetryArea: 0
- Combat area: no CombatArea/SpecialCombatArea instance in the Escalation layer

### New Sobek City (MP_OUTSKIRTS)
- Layer assets: Escalation, Escalation_Global, Escalation_Global_Schematic, MP_Escalation0, MP_Escalation0_Schematic, MeshVariationDb_Win32, MeshVariationDb_Win32, staticmodelgroup.physics. Instances sit in layer(s) ['MP_Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {}. namedOverrides:  {}.
- Gem counts: VehicleSpawner 39, Insertion 16, Sector 7, HQ 6, CapturePoint 7, CapturePoint_OutlineArea 1, TelemetryArea 7, Battle_Pickup 2, SpecialCombatArea 1
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@191 [-188.7, 93.0, 3.3]; side E = HQ@140 [153.4, 90.9, 21.1]; separation 343 m. Other HQ instances: HQ@44 [-159.5, 95.6, -37.1] near CP@54 (72 m); HQ@167 [-156.5, 94.0, -91.7] near CP@54 (32 m); HQ@184 [107.7, 94.4, -82.1] near CP@93 (52 m); HQ@201 [147.1, 93.1, -40.2] near CP@93 (74 m)
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@200 [-158.3, 91.6, -178.0]; Sector@177 [-158.3, 91.6, -175.9] (2 m); polys [83, 188]; dW 184 dE 370
  - CP@54 [-125.4, 91.8, -100.8]; Sector@85 [-127.6, 91.6, -100.3] (2 m); polys [24]; dW 122 dE 304
  - CP@127 [-71.2, 93.1, -157.4]; Sector@171 [-71.4, 93.3, -158.1] (1 m); polys [56, 216]; dW 199 dE 287
  - CP@165 [-35.3, 96.0, -79.6]; Sector@214 [-39.2, 96.0, -80.3] (4 m); polys [56, 192]; dW 174 dE 214
  - CP@148 [24.8, 92.6, -152.3]; Sector@190 [24.8, 92.6, -152.3] (0 m); polys [30, 56]; dW 264 dE 216
  - CP@93 [72.7, 97.3, -43.3]; Sector@248 [108.4, 97.4, -48.8] (36 m); polys [89, 204]; dW 266 dE 103
  - CP@199 [149.7, 90.6, -144.3]; Sector@13 [148.7, 91.0, -147.2] (3 m); polys [14, 125]; dW 369 dE 165
- Predicted removal order, side W (closest to HQ W first): CP@54(122) > CP@165(174) > CP@200(184) > CP@127(199) > CP@148(264) > CP@93(266) > CP@199(369)
- Predicted removal order, side E (closest to HQ E first): CP@93(103) > CP@199(165) > CP@165(214) > CP@148(216) > CP@127(287) > CP@54(304) > CP@200(370)
  - Overlap of W top3 [54, 165, 200] and E top3 [93, 199, 165]: OVERLAP {165}. Max 5 removals before a win. Orders from nearby alternate HQ instances: W-cluster HQ@44: 54>165>200>127>148>93>199; W-cluster HQ@167: 54>200>127>165>148>93>199 | E-cluster HQ@184: 93>199>148>165>127>54>200; E-cluster HQ@201: 93>199>148>165>127>54>200
- Vehicle pads total 39: AttackHelicopter 2, IFV 6, LightTransport 11, MobileAA 2, PTV_DirtBike 4, PTV_QuadBike 6, ScoutHelicopter 2, Tank 4, TransportHelicopter 2
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - CP@148: 1 -> LightTransport 1
    - CP@199: 1 -> LightTransport 1
    - CP@200: 1 -> LightTransport 1
    - CP@54: 1 -> LightTransport 1
    - CP@93: 1 -> LightTransport 1
    - HQ-E: 17 -> AttackHelicopter 1, IFV 3, LightTransport 3, MobileAA 1, PTV_DirtBike 2, PTV_QuadBike 3, ScoutHelicopter 1, Tank 2, TransportHelicopter 1
    - HQ-W: 17 -> AttackHelicopter 1, IFV 3, LightTransport 3, MobileAA 1, PTV_DirtBike 2, PTV_QuadBike 3, ScoutHelicopter 1, Tank 2, TransportHelicopter 1
- Battle_Pickup (placed, not active in live game): 2 -> @103 Battle_Pickup_Railgun [31.8, 90.2, -202.3] (CP@148 50 m); @176 Battle_Pickup_Railgun [-38.1, 96.2, -29.7] (CP@165 50 m)
- Insertion: 16 -> {'Insertion_Cautious_OnSpot_v2': 4, 'Insertion_Cautious_OnSpot_v1': 3, 'Insertion_Cautious_Arrival': 4, 'Insertion_Cautious_OnSpot_v3': 4, 'Insertion_Cautious_LongDistance': 1}; nearer HQ W 8, nearer HQ E 8
- CapturePoint_OutlineArea: 1 for 7 flags (flags with no outline within 15 m: [93, 127, 148, 165, 199, 200])
- TelemetryArea: 7
- SpecialCombatArea@212 pos [15.4, 92.6, -179.7]; polys POLY@56 bbox[-113, -221, 65, -3] (only combat-area object in the layer)

### Mirak Valley (MP_TUNGSTEN)
- Layer assets: Escalation, Escalation_Global, Escalation_Global_Schematic, MeshVariationDb_Win32, staticmodelgroup.physics, MP_Escalation0, MP_Escalation0_Schematic, MeshVariationDb_Win32. Instances sit in layer(s) ['MP_Escalation0']; single layout, no Small/Large/Team variants. factionOverrides:  {}. namedOverrides:  {}.
- Gem counts: Insertion 16, HQ 6, VehicleSpawner 62, Sector 7, TelemetryArea 7, CapturePoint 7, Battle_Pickup 3, AutomaticAA 2, SpecialCombatArea 1
- Initial HQs (inferred: the HQ pair farthest apart; sides named by x): side W = HQ@65 [-460.6, 79.6, -240.0]; side E = HQ@2 [497.2, 86.9, -527.9]; separation 1000 m. Other HQ instances: HQ@44 [274.5, 86.5, -421.6] near CP@70 (45 m); HQ@48 [-236.9, 83.8, -265.5] near CP@43 (48 m); HQ@66 [362.5, 82.4, -466.2] near CP@153 (40 m); HQ@74 [-320.3, 86.1, -224.0] near CP@17 (26 m)
- Capture points (listed in approximate order of distance from HQ W), nearest Sector, shared polygons, distance to HQ W / HQ E:
  - CP@17 [-294.6, 85.5, -227.4]; Sector@52 [-310.1, 82.7, -248.9] (27 m); polys [49, 219]; dW 166 dE 847
  - CP@43 [-189.2, 85.4, -261.8]; Sector@84 [-209.5, 86.6, -291.7] (36 m); polys [171, 219, 230]; dW 272 dE 736
  - CP@16 [-20.3, 91.2, -331.7]; Sector@45 [-3.8, 85.7, -302.1] (34 m); polys [145, 219]; dW 450 dE 553
  - CP@237 [81.6, 85.0, -159.5]; Sector@173 [75.5, 85.8, -175.4] (17 m); polys [145, 219]; dW 548 dE 555
  - CP@134 [55.4, 91.2, -368.0]; Sector@111 [74.2, 85.8, -339.2] (34 m); polys [1, 145, 219]; dW 532 dE 470
  - CP@70 [243.8, 87.0, -388.8]; Sector@155 [226.2, 86.6, -433.8] (48 m); polys [210, 213, 219]; dW 720 dE 289
  - CP@153 [323.5, 83.6, -474.4]; Sector@5 [328.8, 82.8, -442.3] (33 m); polys [104, 187, 219]; dW 818 dE 182
- Predicted removal order, side W (closest to HQ W first): CP@17(166) > CP@43(272) > CP@16(450) > CP@134(532) > CP@237(548) > CP@70(720) > CP@153(818)
- Predicted removal order, side E (closest to HQ E first): CP@153(182) > CP@70(289) > CP@134(470) > CP@16(553) > CP@237(555) > CP@43(736) > CP@17(847)
  - Overlap of W top3 [17, 43, 16] and E top3 [153, 70, 134]: none. Max 5 removals before a win. Orders from nearby alternate HQ instances:  | 
- Vehicle pads total 62: AttackHelicopter 4, AttackPlane 4, FighterPlane 4, IFV 8, LightTransport 16, MobileAA 4, PTV_DirtBike 4, PTV_QuadBike 4, ScoutHelicopter 2, Tank 8, TransportHelicopter 4
  - By nearest anchor (HQ-W/HQ-E include their flag-side HQ instances):
    - CP@134: 1 -> LightTransport 1
    - CP@153: 1 -> LightTransport 1
    - CP@16: 1 -> LightTransport 1
    - CP@17: 1 -> LightTransport 1
    - CP@237: 2 -> LightTransport 2
    - CP@43: 1 -> LightTransport 1
    - CP@70: 1 -> LightTransport 1
    - HQ-E: 27 -> AttackHelicopter 2, AttackPlane 2, FighterPlane 2, IFV 4, LightTransport 4, MobileAA 2, PTV_DirtBike 2, PTV_QuadBike 2, ScoutHelicopter 1, Tank 4, TransportHelicopter 2
    - HQ-W: 27 -> AttackHelicopter 2, AttackPlane 2, FighterPlane 2, IFV 4, LightTransport 4, MobileAA 2, PTV_DirtBike 2, PTV_QuadBike 2, ScoutHelicopter 1, Tank 4, TransportHelicopter 2
- AutomaticAA: 2 -> @148 AutomaticAA [526.1, 85.9, -540.0] (HQ-E 31 m); @168 AutomaticAA [-501.7, 81.7, -255.2] (HQ-W 44 m)
- Battle_Pickup (placed, not active in live game): 3 -> @60 Battle_Pickup_Minigun [62.2, 106.6, -390.7] (CP@134 24 m); @122 Battle_Pickup_Minigun [-24.7, 121.9, -300.7] (CP@16 31 m); @132 Battle_Pickup_Minigun [39.9, 84.9, -89.9] (CP@237 81 m)
- Insertion: 16 -> {'Insertion_Cautious_OnSpot_v2': 3, 'Insertion_Cautious_OnSpot_v3': 4, 'Insertion_Cautious_OnSpot_v1': 7, 'Insertion_Cautious_OnSpot_v4_NOT_FOR_REVEAL': 2}; nearer HQ W 8, nearer HQ E 8
- CapturePoint_OutlineArea: 0 for 7 flags (flags with no outline within 15 m: [16, 17, 43, 70, 134, 153, 237])
- TelemetryArea: 7
- SpecialCombatArea@236 pos [35.8, 81.9, -329.0]; polys POLY@145 bbox[-149, -582, 241, 37]; POLY@219 bbox[-1229, -1434, 1229, 614] (only combat-area object in the layer)

## 5. Open questions (instance indices refer to the layer instance index)

- O1. Railway to Golmud: only CapturePoint@4 in `Escalation_Global` exists (no HQ, no other flags, no pads) even though MUT_Golmud enables an Escalation moving train. Is the rest of the layout in an asset not captured? Area 51 and Vegas Strip have no Escalation layer in the data.
- O2. ESC_f[]PhaseLengths has 4 entries while ESC_iPhaseAmount = 5; ESC_fRoundTimer = 120 dumped with range [120..0]. Meaning of each is not stated in the data or UI.
- O3. The removal rule comes from the UI text only (round graph constants are unnamed). Not verified: straight-line vs path distance, and whether a removed flag's HQ instance is also disabled.
- O4. Which initial HQ is team1 / team2 is not stored; factionOverrides give team1 = Pax Armata on four layers, so "W/E" is not a team. Initial pair = farthest-apart HQs.
- O5. Iberian Offensive: HQ@73, HQ@76, HQ@102 are at the identical position [920.1, 74.8, 134.5]; the 3 Forward spawners (@18, @114, @128) are at the west base only.
- O6. Iberian Offensive has only 8 pads, no insertions, no TelemetryArea.
- O7. New Sobek City has two HQs per base (W: HQ@44 [-159.5, -37.1], HQ@191 [-188.7, 3.3]; E: HQ@140 [153.4, 21.1], HQ@201 [147.1, -40.2]). Picked 191/140; HQ@44 gives the same W order; flag HQ@167 changes it to 54>200>127>165>148>93>199. W top-3 and E top-3 share CP@165.
- O8. Wake Island: top-3 of each side share CP@26 (W: 28, 26, 137; E: 26, 117, 59), so a clash is possible there too. The farthest-apart HQs (@67 W, @32 E, 1309 m apart) hold the air pads, 10 PatrolBoats each and the naval fighters; the land groups (IFV 2, LightTransport 3, MobileAA 1, PTV_QuadBike 2, Tank 3 each) sit at HQ@55 [-128, 179] and HQ@2 [107, -114], 22 m and 3 m from flags CP@28 and CP@26. If those flag HQs are the real land bases, the distances (and which flag is "closest to the initial HQ") change. Also CP@36, CP@59, CP@100 share a single Sector@138 and CP@28 is 126 m from its nearest Sector.
- O9. Tsuru Reef has 9 CapturePoints but only 5 Sectors and 6 HQs, no TelemetryArea or outline areas. With 9 flags the 3+2 removals leave 4. HQ@96 sits on CP@55 (4 m), HQ@9 on CP@22 (14 m), HQ@75 is 194 m from any flag. Initial HQs are the 1683 m apart pair HQ@94 and HQ@21 (air, boat pads); land pads are at HQ@96 (APC, 2 IFV, 2 Tank) and HQ@75 (2 IFV, 2 Tank). Which are the real bases is unclear.
- O10. Contaminated: Sector markers sit at y about 64 while flags are at y about 300-334 and sectors are up to 182 m from their flag, so sector matching by distance is unreliable. Layers Escalation_Gas and Escalation_GasPlacement hold 9 PsyGasZone instances; whether gas is active in Escalation is not stated.
- O11. Collection_Event instances (at 0,0,0): Siege of Cairo @70, Iberian Offensive @71, Wake Island @60, Contaminated @76, Tsuru Reef @97, plus Manhattan Bridge, Eastwood and Operation Firestorm. Purpose unknown.
- O12. Battle_Pickup instances (Minigun, Railgun) are placed but not active in the live game.
- O13. Combat area: only SpecialCombatArea instances exist (Contaminated POLY@43 bbox [-383, -396, 604, 523], Eastwood, Operation Firestorm, New Sobek City, Mirak Valley). New Sobek City's polygon does not contain flags CP@54, CP@200, CP@93, CP@199. No combat-area object on Siege of Cairo, Wake Island, Iberian Offensive, Liberation Peak, Manhattan Bridge, Tsuru Reef.
- O14. CapturePoint_OutlineArea is present for only some flags (Siege of Cairo 7, Iberian Offensive 5, Operation Firestorm 4, Liberation Peak 3, Contaminated 3, Eastwood 2, Manhattan Bridge 1, New Sobek City 1; none on Wake Island, Tsuru Reef, Mirak Valley).
