# Modes without a live multiplayer UI entry, plus Gauntlet (build 2.1.1.0)

Source: files in the Other work folder only. Tweakable values are client defaults (a server playlist can override them). Range is [min..max] as stored; [0..0] means no range was stored. The team-to-side mapping is not stored in the data; where I infer it, I say so. The round-logic graphs (GME_Sim_*_Round) expose only generic variables (ActivityStateMachine, MI_Sim_GameMode), so rule behaviour is inferred mostly from tweakable names.

## 1. Obliteration
**What the files say.** A bomb-carry mode: pick up a bomb (`Bomb_Pickup`), carry it to an enemy objective (`Objective_MCOM`), arm it (ArmTime / FastArmTime), then the fuse runs (FuseTime) and defenders can defuse (DefuseTime / FastDefuseTime). First to OBL_ScoreLimit wins. Overtime exists with a shorter fuse and a bomb-in-play end condition. Bombs time out when carried (180 s) or dropped (80 s) and reset; two extra bombs are added after 1050 s. Catch-up logic reveals spawn locations when the score gap is 1 or more. UI view-models: Obliteration_BombGraphList (friendly/enemy/neutral bombs, armed bombs) and MP_Outcome_Obliteration_MCOMData (friendly/enemy MCOMS). Objective table `AD_Objective_Obliteration` GEMs: Sector, Objective_MCOM, Bomb_Pickup, HQ, AutomaticAA, Insertion (19 variants), Insertion_Event (2), VehicleSpawner (24), VehicleSpawner_Forward, StationarySpawner (3), VehicleResupplyStation, Reinforcement(_Intro), B1Bomber_TrailerSpawner, Battle_Pickup (5), Collection_Event. 64 target players, minimum 16, 25-minute cap. It also uses the shared `MUT_Carriable_Plant_Objective` (9 tweakables: bomb shader type 1 [0..1], colour type 2 [0..10], occlusion 1 [0..2], opacity 0.75 [0..1], pickup interact duration 0.0 [0..60], kill switch false, carried-icon visibility style 0 [0..3], icon blink show/hide 5.0/5.0 [2..25]).
**Rule asset:** MUT_Obliteration, 58 tweakables. The round graphs GME_Sim/Pres_Obliteration_Round hold no named values.
**Rule values:**
- Assault Recommended = false
- Engineer Recommended = false
- OBL_AllowAttackTAOrders = true
- OBL_AllowDefendTAOrders = false
- OBL_AllowDefuseTAOrders = true
- OBL_AllowGuardTAOrders = true
- OBL_AreObjectiveIDsTeamBased = false
- OBL_ArmTime = 2.0 [0.0..60.0]
- OBL_BombCountAtStart = 1 [1..5]
- OBL_CarryTimeoutDuration = 180.0 [1.0..360.0]
- OBL_CommanderVoice = -1 [-1..0]
- OBL_DefuseBehavior = 0 [0..2]
- OBL_DefuseTime = 4.0 [0.0..60.0]
- OBL_DelayBeforeMidMatchBombs = 1050.0 [360.0..2400.0]
- OBL_DoesBombResetOnDeath = false
- OBL_DoesCarryTimeoutResetCarriable = false
- OBL_DoesTimeoutDuringCarry = true
- OBL_DoesTimeoutDuringDrop = true
- OBL_DoesTimeoutResetOnPickup = true
- OBL_DropTimeoutDuration = 80.0 [1.0..360.0]
- OBL_FastArmTime = 1.6 [0.0..60.0]
- OBL_FastDefuseTime = 3.0 [0.0..60.0]
- OBL_FuseTime = 35.0 [1.0..180.0]
- OBL_IncomingDuration_MatchStart = 40.0 [0.0..360.0]
- OBL_IncomingDuration_ObjectiveComplete = 30.0 [0.0..360.0]
- OBL_IncomingDuration_Reset = 15.0 [0.0..360.0]
- OBL_IsBombOvertimeEndCondition = true
- OBL_IsCarryAndDropTimeoutShared = false
- OBL_IsFriendlyHQOOBForCarrier = true
- OBL_IsOvertimeAllowed = true
- OBL_IsSpawnDelayLocationRevealCatchupEnabled = true
- OBL_MaxMatchDurationMins = 25.0 [5.0..40.0]
- OBL_MidMatchBombCount = 2 [1..5]
- OBL_MinPlayerCount = 16 [2..64]
- OBL_OOBReturnTime = 10 [1..300]
- OBL_Overtime_CarryTimeoutDuration = 300.0 [1.0..360.0]
- OBL_Overtime_DefuseBehavior = 2 [0..2]
- OBL_Overtime_DoesBombResetOnDeath = false
- OBL_Overtime_DoesCarryTimeoutResetCarriable = true
- OBL_Overtime_DoesTimeoutResetOnPickup = false
- OBL_Overtime_DropTimeoutDuration = 300.0 [1.0..360.0]
- OBL_Overtime_FuseTime = 10.0 [1.0..180.0]
- OBL_Overtime_IsCarryAndDropTimeoutShared = true
- OBL_RespawnDelay = 10.0 [1.0..300.0]
- OBL_ScoreDifferenceToEnableCatchup = 1 [0..4]
- OBL_ScoreLimit = 3.0 [1.0..5.0]
- OBL_SpawnDelay_MatchStart = 20.0 [0.0..360.0]
- OBL_SpawnDelay_ObjectiveComplete = 40.0 [0.0..360.0]
- OBL_SpawnDelay_Reset = 15.0 [0.0..360.0]
- OBL_SquadOrderCooldown = 10.0 [0.0..0.0]
- OBL_TacticalAdviceCooldown = 10.0 [0.0..0.0]
- OBL_TargetPlayerCount = 64 [2..64]
- OBL_Team1RespawnDelay = -1.0 [-1.0..300.0]
- OBL_Team2RespawnDelay = -1.0 [-1.0..300.0]
- OBL_TimeoutSoonWarningThreshold = 25 [1..99]
- OBL_iSoldierMandownType = 1 [0..2]
- Recon Recommended = false
- Support Recommended = false

**Maps with a layer.** 3 map entries, 2 with gameplay layouts.
- Contaminated (MP_Contaminated): layer `Obliteration0` plus `Obliteration_Global`. 6 Objective_MCOM, 12 Bomb_Pickup, 2 HQ, 1 Sector, 1 SpecialCombatArea (play-area boundary), 41 VehicleSpawner, 12 StationarySpawner, 8 VehicleResupplyStation, 16 Insertion, 3 Battle_Pickup (Minigun, 2 Railgun), 2 AutomaticAA. No faction overrides. Coordinates are (x, z).
  - HQs: (-79, -117) and (439, 197). Two HQs, so one per team (assignment not stored).
  - Bomb pickups (12): all inside x 72..210, z 32..224, a central cluster between the HQs.
  - M-COM-style targets (6): (293, 125), (264, 53), (263, 219) on the east side; (2, 139), (-20, 34) on the west; (118, -27) central-north. Which team defends which is not stored.
  - Battle pickups: Minigun (150, 90); Railgun (257, 201) and (-48, 42).
- Railway to Golmud (MP_GolmudRailway): layer `MP_Obliteration0` plus Global. 6 Objective_MCOM, 12 Bomb_Pickup, 6 HQ, 1 Sector, 1 SpecialCombatArea, 61 VehicleSpawner, 14 StationarySpawner, 11 VehicleResupplyStation, 16 Insertion, 3 Battle_Pickup (ArtilleryStrike, Railgun, Minigun), 2 AutomaticAA.
  - HQs (6): west group (-642, 358), (-801, 713), (-537, 871); east group (464, 385), (535, 600), (310, 897). Three per side, probably alternative spawn HQs per team (inference).
  - Bomb pickups (12): a strip along the middle, x -165..-78, z 204..1043 (north-south).
  - M-COM-style targets (6): (163, 753), (-108, 892), (-166, 897), (-470, 353), (-362, 770), (296, 359).
  - Battle pickups: ArtilleryStrike (-86, 393), Railgun (-72, 1058), Minigun (-154, 688).
- Eastwood (MP_Eastwood): layers `Obliteration`, `Obliteration0`, `Obliteration_Global` (+ Schematic); faction overrides team1 = Alliance/NATO, team2 = Coalition/Pax Armata. 6 Objective_MCOM, 12 Bomb_Pickup, 2 HQ, 1 Sector, 1 SpecialCombatArea, 44 VehicleSpawner, 12 StationarySpawner, 3 VehicleResupplyStation, 16 Insertion, 2 Battle_Pickup (both Minigun), 2 AutomaticAA.
  - HQs: (-345, 71) west and (378, -160) east-north (x, z).
  - Bomb pickups (12): central, x -29..161, z -51..191: a cluster around (35, -40) and a chain (92, 119), (136, 115), (161, 136), (90, 162), (52, 190), (133, 191).
  - M-COM-style targets (6): (-185, -5), (-102, 172), (10, 81), (74, 4), (219, 41), (203, -169). Four lie west-to-centre and two on the east side (team split not stored).
  - Battle pickups: Minigun (149, -81) and (-45, 94).
**State:** full rules plus layers on all 3 maps (Contaminated, Railway to Golmud, Eastwood). The most complete of the group.

## 2. Squad Obliteration
**What the files say.** Obliteration scaled for squads, same keys with a SQOBL_ prefix. Differences from Obliteration: 16 target players (minimum 8), 15-minute cap, score limit 2, one mid-match bomb after 1080 s, arm 4.0 s / fast arm 3.0 s, fuse 50 s, respawn delay 11 s, spawn delays 10/15/20 s, incoming durations 15/30/40 s. Carry/drop timeouts, overtime and defuse are identical to Obliteration. `GM_SquadObliteration_LaunchFunction` holds only LaunchParameters/ActivityParameters.
**Rule asset:** MUT_SquadObliteration, 58 tweakables.
**Rule values:**
- Assault Recommended = false
- Engineer Recommended = false
- Recon Recommended = false
- SQOBL_AllowAttackTAOrders = true
- SQOBL_AllowDefendTAOrders = false
- SQOBL_AllowDefuseTAOrders = true
- SQOBL_AllowGuardTAOrders = true
- SQOBL_AreObjectiveIDsTeamBased = false
- SQOBL_ArmTime = 4.0 [0.0..60.0]
- SQOBL_BombCountAtStart = 1 [1..5]
- SQOBL_CarryTimeoutDuration = 180.0 [1.0..360.0]
- SQOBL_CommanderVoice = -1 [-1..0]
- SQOBL_DefuseBehavior = 0 [0..2]
- SQOBL_DefuseTime = 4.0 [0.0..60.0]
- SQOBL_DelayBeforeMidMatchBombs = 1080.0 [360.0..2400.0]
- SQOBL_DoesBombResetOnDeath = false
- SQOBL_DoesCarryTimeoutResetCarriable = false
- SQOBL_DoesTimeoutDuringCarry = true
- SQOBL_DoesTimeoutDuringDrop = true
- SQOBL_DoesTimeoutResetOnPickup = true
- SQOBL_DropTimeoutDuration = 80.0 [1.0..360.0]
- SQOBL_FastArmTime = 3.0 [0.0..60.0]
- SQOBL_FastDefuseTime = 3.0 [0.0..60.0]
- SQOBL_FuseTime = 50.0 [1.0..180.0]
- SQOBL_IncomingDuration_MatchStart = 30.0 [0.0..360.0]
- SQOBL_IncomingDuration_ObjectiveComplete = 40.0 [0.0..360.0]
- SQOBL_IncomingDuration_Reset = 15.0 [0.0..360.0]
- SQOBL_IsBombOvertimeEndCondition = true
- SQOBL_IsCarryAndDropTimeoutShared = false
- SQOBL_IsFriendlyHQOOBForCarrier = true
- SQOBL_IsOvertimeAllowed = true
- SQOBL_IsSpawnDelayLocationRevealCatchupEnabled = true
- SQOBL_MaxMatchDurationMins = 15.0 [5.0..40.0]
- SQOBL_MidMatchBombCount = 1 [1..5]
- SQOBL_MinPlayerCount = 8 [2..16]
- SQOBL_OOBReturnTime = 10 [1..300]
- SQOBL_Overtime_CarryTimeoutDuration = 300.0 [1.0..360.0]
- SQOBL_Overtime_DefuseBehavior = 2 [0..2]
- SQOBL_Overtime_DoesBombResetOnDeath = false
- SQOBL_Overtime_DoesCarryTimeoutResetCarriable = true
- SQOBL_Overtime_DoesTimeoutResetOnPickup = false
- SQOBL_Overtime_DropTimeoutDuration = 300.0 [1.0..360.0]
- SQOBL_Overtime_FuseTime = 10.0 [1.0..180.0]
- SQOBL_Overtime_IsCarryAndDropTimeoutShared = true
- SQOBL_RespawnDelay = 11.0 [1.0..300.0]
- SQOBL_ScoreDifferenceToEnableCatchup = 1 [0..4]
- SQOBL_ScoreLimit = 2.0 [1.0..5.0]
- SQOBL_SpawnDelay_MatchStart = 15.0 [0.0..360.0]
- SQOBL_SpawnDelay_ObjectiveComplete = 20.0 [0.0..360.0]
- SQOBL_SpawnDelay_Reset = 10.0 [0.0..360.0]
- SQOBL_SquadOrderCooldown = 10.0 [0.0..0.0]
- SQOBL_TacticalAdviceCooldown = 10.0 [0.0..0.0]
- SQOBL_TargetPlayerCount = 16 [2..16]
- SQOBL_Team1RespawnDelay = -1.0 [-1.0..300.0]
- SQOBL_Team2RespawnDelay = -1.0 [-1.0..300.0]
- SQOBL_TimeoutSoonWarningThreshold = 25 [1..99]
- SQOBL_iSoldierMandownType = 1 [0..2]
- Support Recommended = false

**Maps:** 4 layers (`SquadObliteration0` on each; positions are (x, z)). All are compact: 6 Objective_MCOM, 2 HQ, 1 Bomb_Pickup, 1 Sector, 4 Insertion, and no vehicle spawners. Only Cairo Bazaar also has `SquadObliteration`, `_Global` and a SpecialCombatArea, and a faction override (team1 NATO, team2 Pax Armata).
- Siege of Cairo (MP_Abbasid): bomb (-82, 1); M-COMs (20, 28), (-8, -108), (-154, 52), (-159, 111), (-175, -16), (-7, -44); HQs (116, -53) and (-245, 68). Targets lie in x -219..80, z -128..130.
- Empire State (MP_Aftermath): bomb (-604, -43); M-COMs (-586, -150), (-554, -34), (-649, 69), (-577, 23), (-647, -27), (-648, -85); HQs (-664, -157) and (-526, 46). All in x -708..-514, z -198..148.
- Iberian Offensive (MP_Battery): bomb (757, 136); M-COMs (803, 101), (706, 95), (795, 161), (719, 179), (694, 150), (766, 69); HQs (849, 54) and (636, 144). Box x 658..870, z 33..229.
- Cairo Bazaar (MP_Plaza): bomb (28, 98); M-COMs (11, 45), (76, 23), (-74, 52), (140, 149), (35, 157), (-22, 155); HQs (85, 235) and (-31, -39). Box x -98..162, z -30..207.
One bomb and six M-COM targets per map, in a small area. Which HQ belongs to which team is not stored.
**State:** full rules plus layers on 4 maps; unreleased (no UI entry).

## 3. Carrier Strike
**What the files say.** An assault on an aircraft carrier. The carrier has health (start 100000) with damage thresholds (light 0.7, medium 0.5, major 0.3, breach 0.3, critical 0.1, near-breach offset 0.05). `Exp_Sim_CarrierStrike_CarrierDamagedPersistenceLogic` tracks CarrierStartingHealth, CarrierCurrentHealth, DamagingPlayer, DamageValue. Each team starts with a score of 100. Objective table `AD_Objective_CarrierStrike` GEMs: Objective_MCOM (arm 4.0 s, defuse 8.0 s, fuse 40 s), `Objective_VLS_Battery` (missile battery; SSM battery pitch/yaw speed 0.5, reload 15 s), CapturePoint (Flag and OneTimeUse variants), VehicleSuperiorityCaptureVolume, StrategicAsset, DestructibleProxy, ObjectiveGroup, Sector, HQ, AutomaticAA, VehicleSpawner (24 variants), Insertion (19), and similar. UI: EOR_CarrierStrike_SummaryScreen_DataPackager with Local/Enemy CarrierStrike_MCOMData. `CS_UseDallasTreatment = true` ties it to the Tsuru Reef (Dallas) setup.
**Rule asset:** MUT_CarrierStrike (path Game/glaciermp/Gamemodes/CarrierStrike/), 50 tweakables.
**Rule values:**
- Assault Recommended = false
- CS_UseDallasTreatment = true
- CS_bAllowAttackTAOrders = true
- CS_bAllowDefendTAOrders = false
- CS_bAllowDefuseTAOrders = true
- CS_bAllowGuardTAOrders = true
- CS_bCapDamage = false
- CS_bDamageThrottle = false
- CS_bDisableVehicleSpawnerSubset = false
- CS_fArmTime = 4.0 [0.0..60.0]
- CS_fCaptureTime = 30.0 [0.0..0.0]
- CS_fCarrierBreachThreshold = 0.3 [0.0..1.0]
- CS_fCarrierCriticalThreshold = 0.1 [0.0..1.0]
- CS_fCarrierLightDamageThreshold = 0.7 [0.0..1.0]
- CS_fCarrierMajorDamageThreshold = 0.3 [0.0..1.0]
- CS_fCarrierMediumDamageThreshold = 0.5 [0.0..1.0]
- CS_fCarrierNearBreachOffset = 0.05 [0.0..1.0]
- CS_fDefuseTime = 8.0 [0.0..60.0]
- CS_fFastArmTime = 3.2 [0.0..60.0]
- CS_fFastDefuseTime = 6.0 [0.0..60.0]
- CS_fFuseTime = 40.0 [1.0..180.0]
- CS_fJetCinematicTimeout = 120.0 [0.0..600.0]
- CS_fNeutralizeTime = 30.0 [0.0..0.0]
- CS_fNoInteractivityTimeoutOverride = 120.0 [0.0..600.0]
- CS_fPlayerRespawnDelay = 12.0 [0.0..100.0]
- CS_fSSMBattery_ReloadTime = 15.0 [0.0..500.0]
- CS_fSSMBattery_RotationSpeed_Pitch = 0.5 [0.1..3.0]
- CS_fSSMBattery_RotationSpeed_Yaw = 0.5 [0.1..3.0]
- CS_fSpottingDuration = 5.0 [0.0..10.0]
- CS_fSquadOrderCooldown = 30.0 [0.0..0.0]
- CS_fTacticalAdviceCooldown = 60.0 [0.0..0.0]
- CS_fTeam1RespawnDelay = 12.0 [0.0..100.0]
- CS_fTeam2RespawnDelay = 12.0 [0.0..100.0]
- CS_fUrgencyPercentageThreshold = 0.1 [0.0..1.0]
- CS_fVehicleSpawnValueInterval = 60.0 [0.0..120.0]
- CS_f[]CaptureSpeedMultipliers = {"Field_ffba60f0": [0.0, 1.0, 1.333, 1.666, 2.0]} [0.0..0.0]
- CS_iCarrierDamageCap = 1000 [0..100000]
- CS_iCarrierStartingHealth = 100000 [0..1000000]
- CS_iCommanderVoice = 0 [0..0]
- CS_iInitialScoreTeam1 = 100 [0..100]
- CS_iInitialScoreTeam2 = 100 [0..100]
- CS_iLobbyPlayerCountStartTimer = 32 [0..128]
- CS_iLobbyPlayerCountToSpeedUpTimer = 64 [0..0]
- CS_iModeTime = 45 [10..180]
- CS_iOutOfBounds_TimeToReturn = 10 [0..0]
- CS_iSoldierMandownType = 1 [0..2]
- CS_iUrgencyTimeThreshold = 60 [0..120]
- Engineer Recommended = false
- Recon Recommended = false
- Support Recommended = false

**Maps:** 1 layer, Tsuru Reef (MP_Isolated): `CarrierStrike`, `CarrierStrike0`, `_Global`, `_Global_Cables`, schematic; factions team1 = Coalition/Pax Armata, team2 = Alliance/NATO. 95 instances: 49 VehicleSpawner, 16 Insertion, 8 Objective_VLS_Battery, 5 CapturePoint, 4 StationarySpawner (AntiAircraft and AntiTank), 4 Objective_MCOM, 3 ObjectiveGroup, 2 HQ, 2 DestructibleProxy, 1 Sector, 1 SpecialCombatArea. No instance is named carrier; the carrier-related ones are the M-COMs plus DestructibleProxy (the carrier health logic lives in the round graph). Coordinates (x, z):
- Two HQs at opposite ends of the long axis: (-685, 1154) and (-1289, -588). Each end has 2 M-COMs and 1 DestructibleProxy within about 50 m of its HQ: north (-727, 1164), (-662, 1146), proxy (-697, 1154); south (-1254, -613), (-1308, -572), proxy (-1276, -593). Probably the carrier breach targets, one pair per end (inference; the files do not label them).
- 5 CapturePoints between them: (-1054, -10), (-815, -8), (-814, 212), (-876, 522), (-643, 431). Three ObjectiveGroups: (-848, 154), (-665, 463), (-605, -229).
- 8 VLS missile batteries: 3 sector variants at (-995, -5), (-812, 606), (-940, 333); 5 plain at (-854, 193), (-893, 503), (-1100, -35), (-827, 9), (-653, 410).
- Vehicles (49): RHIB 12, PTV QuadBike 5, LightTransport 5, PatrolBoat 4, MultirolePlane 4, TransportHelicopter 4, ScoutHelicopter 2, NavalFighterPlane 2, Tank 2, MobileAA 2, IFV 1, and 6 IGC jet slots (keys 21-23, 2 each).
**State:** full rules plus a complete layer on Tsuru Reef; unreleased.

## 4. Operations
**What the files say.** A multi-sector, two-map attacker/defender campaign. Map1 and Map2 each have a sector list (`Operations_fSecondMapStartDelay` 45 s, MaxTransitions 1). Attackers have battalions (InitialBattalions 3 [1..10]) with 200 tickets each (TicketsPerBattalion [10..300]); capturing sectors advances the push (round-graph variables BattalionActivated, BattalionDepleted, AtkOwns). Reinforcement ticket thresholds per sector: Map1 [100,100,100,75,75], Map2 [75,75,75,75], per map [100,75]. View-model fields: OperationTypeInt, ActiveMapInt, IsLocalPlayerTeamAttacking, SectorList_Map1/2, SectorCount_Map1/2, CurrentBattalions, BattalionHistory, MaxBattalions, SectorCapturedCount. Large XP tables and win-span XP-per-minute tables (first span 25 min, second 15 min). Lobby starts at 24 players, max 48. Special briefing intervals for Subsurface and Contamination (gas). Objective table `AD_Objective_Operations`: Sector, CapturePoint (2 variants), OutlineArea, StrategicAsset, VehicleSuperiorityCaptureVolume, HQ, PsyGas (6), MapBriefingOverride, spawners. This is a capture-point (Breakthrough-style) set, consistent with earlier Battlefield Operations.
**Rule asset:** MUT_Operations, 136 tweakables.
**Rule values:**
- Assault Recommended = false
- Engineer Recommended = false
- KillswitchOverride_EnableBattlePickups = true
- Operations_AlwaysShowIntroCinematicToLateJoiners = true
- Operations_AvengerOrSaviorKill = 10.0 [0.0..100.0]
- Operations_AwardSuccessfulRetreat = true
- Operations_Contamination_BriefingSectorInterval = 4.0 [0.0..8.0]
- Operations_ControlPanelClaimed = 10.0 [0.0..100.0]
- Operations_DisableFlagSpawnOnLosingSectorOwnership = true
- Operations_EIDOSDestroyXP = 10.0 [0.0..100.0]
- Operations_EnemyDisruptedXP = 20.0 [0.0..100.0]
- Operations_EnemyForcedBailXP = 50.0 [0.0..100.0]
- Operations_EnemyForcedCrashXP = 50.0 [0.0..100.0]
- Operations_EnemySpottedXP = 5.0 [0.0..100.0]
- Operations_EquipmentDestroyedXP = 10.0 [0.0..100.0]
- Operations_ExplosiveDestroyedXP = 10.0 [0.0..100.0]
- Operations_Generic_ReinforcementThresholdPerMap = {"Field_ffba60f0": [100.0, 75.0]} [0.0..0.0]
- Operations_Headshot = 20.0 [0.0..100.0]
- Operations_HealingXP = 20.0 [0.0..100.0]
- Operations_InitialBattalions = 3 [1..10]
- Operations_LayoutSelection = 0 [0..3]
- Operations_Map1_TicketReinforcementThresholdPerSector = {"Field_ffba60f0": [100.0, 100.0, 100.0, 75.0, 75.0]} [0.0..0.0]
- Operations_Map2_TicketReinforcementThresholdPerSector = {"Field_ffba60f0": [75.0, 75.0, 75.0, 75.0]} [0.0..0.0]
- Operations_MaxTransitions = 1 [1..10]
- Operations_MultiKillXP = 50.0 [0.0..0.0]
- Operations_ObjectiveCapturedXP = 200.0 [0.0..500.0]
- Operations_ObjectiveHoldingXP = 15.0 [0.0..100.0]
- Operations_ObjectiveNeutralizedXP = 200.0 [0.0..500.0]
- Operations_ObjectiveSecuringXP = 15.0 [0.0..100.0]
- Operations_OperationseamSpecificRespawnDelay = true
- Operations_PilotKill = 50.0 [0.0..250.0]
- Operations_PlayerAssistedDamageXP = 50.0 [0.0..100.0]
- Operations_PlayerAssistedDisruptionXP = 40.0 [0.0..100.0]
- Operations_PlayerAssistedDriverXP = 50.0 [0.0..100.0]
- Operations_PlayerAssistedPassengerXP = 40.0 [0.0..100.0]
- Operations_PlayerAssistedRepairXP = 50.0 [0.0..100.0]
- Operations_PlayerAssistedSmokeXP = 40.0 [0.0..100.0]
- Operations_PlayerAssistedSpotXP = 10.0 [0.0..100.0]
- Operations_PlayerAssistedTurretXP = 50.0 [0.0..100.0]
- Operations_PlayerAssistedVehicleDestroyXP = 50.0 [0.0..100.0]
- Operations_PlayerKilledXP = 50.0 [0.0..100.0]
- Operations_PlayerRevivedXP = 50.0 [0.0..100.0]
- Operations_PlayerWasRevivedXP = 15.0 [0.0..100.0]
- Operations_RangerDestroyedXP = 75.0 [0.0..100.0]
- Operations_ResupplyXP = 20.0 [0.0..100.0]
- Operations_RetreatSuccessfulXP = 50.0 [0.0..100.0]
- Operations_ReviveOrHealConcealed = 10.0 [0.0..100.0]
- Operations_SectorCapturedXP = 100.0 [0.0..100.0]
- Operations_SetLateJoinersAfterFirstRound = true
- Operations_SpawnOnBeaconXP = 10.0 [0.0..100.0]
- Operations_SpawnOnVehicleXP = 10.0 [0.0..100.0]
- Operations_SpawnOnYouXP = 10.0 [0.0..100.0]
- Operations_Subsurface_BriefingSectorInterval = 5.0 [0.0..8.0]
- Operations_TVMissileDestroyedXP = 10.0 [0.0..100.0]
- Operations_TakedownKill = 25.0 [0.0..100.0]
- Operations_TicketsPerBattalion = 200 [10..300]
- Operations_VehicleDamagedHeavyXP = 20.0 [0.0..0.0]
- Operations_VehicleDamagedLightXP = 5.0 [0.0..0.0]
- Operations_VehicleDestroyedXP = 50.0 [0.0..100.0]
- Operations_VehicleDisabledXP = 10.0 [0.0..100.0]
- Operations_VehicleRepairingXP = 20.0 [0.0..100.0]
- Operations_bShowObjectiveCallOutString = true
- Operations_bUseCustomSectorCount = false
- Operations_bUseStaticRespawnDelays = true
- Operations_fAttackOrderReactivationDelay = 20.0 [0.0..360.0]
- Operations_fAttackerAdvanceInitialReminderDelay = 30.0 [0.0..0.0]
- Operations_fAttackerAdvanceReminderIncrementDelay = 15.0 [0.0..0.0]
- Operations_fAttackerRespawnDelay = 12.0 [0.0..0.0]
- Operations_fAudioFalloffDistanceToObjective = 1.0 [1.0..200.0]
- Operations_fDefenderRespawnDelay = 12.0 [0.0..0.0]
- Operations_fGlobalRespawnDelay = 10.0 [0.0..0.0]
- Operations_fLobbyDuration = 6.0 [0.0..0.0]
- Operations_fNoInteractivityTimeoutOverride = 180.0 [0.0..600.0]
- Operations_fObjectiveCallOutStringVisDistance = 100.0 [0.0..0.0]
- Operations_fObjectiveCaptureTime = 30.0 [0.0..1000.0]
- Operations_fObjectiveNeutralizationTime = 30.0 [0.0..1000.0]
- Operations_fPlayingWithFriendsXP = 1000.0 [0.0..5000.0]
- Operations_fReadyPlayerDelay = 45.0 [0.0..0.0]
- Operations_fReinforcementsAnnouncementDelay = 5.0 [0.1..30.0]
- Operations_fSecondMapStartDelay = 45.0 [0.0..0.0]
- Operations_fSectorAdvanceDuration = 40.0 [0.0..0.0]
- Operations_fSectorCleanUpDurationMax = 45.0 [0.0..1000.0]
- Operations_fSectorCleanUpDurationMin = 15.0 [0.0..1000.0]
- Operations_fSectorCleanUpEndedEarlyThreshold = 10.0 [5.0..15.0]
- Operations_fSectorReinforcementsDuration = 5.0 [0.0..1000.0]
- Operations_fSectorTakenDuration = 6.0 [0.0..1000.0]
- Operations_fSportsmanshipMultiplier = 1.0 [0.0..10.0]
- Operations_fSquadOrderCooldown = 30.0 [0.0..0.0]
- Operations_fTacticalAdviceCooldown = 60.0 [0.0..0.0]
- Operations_fTimeToMarkDefenders = 5.0 [0.0..0.0]
- Operations_fTimeXPpM = 250.0 [0.0..500.0]
- Operations_fUrgencyCaptureThreshold = 30.0 [0.0..0.0]
- Operations_fUrgencyTimeThreshold = 30.0 [0.0..0.0]
- Operations_fVehicleCooldown_Fallback_Team1_AirCombat = 120.0 [0.0..300.0]
- Operations_fVehicleCooldown_Fallback_Team1_AirTransport = 60.0 [0.0..300.0]
- Operations_fVehicleCooldown_Fallback_Team1_Heavy = 120.0 [0.0..300.0]
- Operations_fVehicleCooldown_Fallback_Team1_Light = 15.0 [0.0..300.0]
- Operations_fVehicleCooldown_Fallback_Team1_Util = 60.0 [0.0..300.0]
- Operations_fVehicleCooldown_Fallback_Team2_AirCombat = 120.0 [0.0..300.0]
- Operations_fVehicleCooldown_Fallback_Team2_AirTransport = 60.0 [0.0..300.0]
- Operations_fVehicleCooldown_Fallback_Team2_Heavy = 120.0 [0.0..300.0]
- Operations_fVehicleCooldown_Fallback_Team2_Light = 15.0 [0.0..300.0]
- Operations_fVehicleCooldown_Fallback_Team2_Util = 60.0 [0.0..300.0]
- Operations_fWeightScaleTimeThreshold = 180.0 [0.0..0.0]
- Operations_fWin_FirstSpanMinutes = 25.0 [0.0..60.0]
- Operations_fWin_FirstSpanXPpM = 130.0 [0.0..500.0]
- Operations_fWin_SecondSpanMinutes = 15.0 [0.0..60.0]
- Operations_fWin_SecondSpanXPpM = 100.0 [0.0..500.0]
- Operations_fWin_ThirdSpanXPpM = 80.0 [0.0..500.0]
- Operations_f[]AttackerRespawnDelays = {"Field_ffba60f0": [12.0, 9.0, 6.0, 6.0, 6.0, 12.0, 9.0, 9.0, 6.0, 6.0, 12.0, 12.0, 12.0, 9.0, 6.0]} [0.0..0.0]
- Operations_f[]CaptureObjectiveCountMultipliers = {"Field_ffba60f0": [0.0, 1.0, 1.0, 1.0]} [0.0..0.0]
- Operations_f[]CapturePlayersMultipliers = {"Field_ffba60f0": [0.0, 1.0, 1.1, 1.1, 1.3, 1.3, 1.5, 1.5, 2.0]} [0.0..0.0]
- Operations_f[]CaptureTeamsMultipliers = {"Field_ffba60f0": [1.0, 1.0, 1.0]} [0.0..0.0]
- Operations_f[]DefenderRespawnDelays = {"Field_ffba60f0": [12.0, 12.0, 12.0, 12.0, 12.0, 9.0, 9.0, 12.0, 12.0, 12.0, 6.0, 6.0, 6.0, 9.0, 12.0]} [0.0..0.0]
- Operations_f[]NeutralizationObjectiveCountMultipliers = {"Field_ffba60f0": [0.0, 1.0, 1.0, 1.0]} [0.0..0.0]
- Operations_f[]NeutralizationTeamsMultipliers = {"Field_ffba60f0": [1.0, 1.0, 1.0]} [0.0..0.0]
- Operations_iCommanderVoice = 0 [0..0]
- Operations_iCustomSectorCount = 2 [0..0]
- Operations_iLobbyMaxPlayers = 48 [0..0]
- Operations_iLobbyPlayerCountStartTimer = 24 [0..0]
- Operations_iLobbyPlayerCountToSpeedUpTimer = 40 [0..0]
- Operations_iMaxCaptureMultiplier = 5 [1..128]
- Operations_iOutOfBounds_TimeToReturn = 10 [0..0]
- Operations_iRemainingRespawnsThreshold1 = 75 [0..100]
- Operations_iRemainingRespawnsThreshold2 = 50 [0..100]
- Operations_iRemainingRespawnsThreshold3 = 25 [0..100]
- Operations_iSectorTime = 20 [10..60]
- Operations_iSoldierDeathScoreBleed = 1 [0..10]
- Operations_iSoldierMandownType = 1 [0..2]
- Operations_iUrgencyRespawnsThreshold = 20 [0..0]
- Operations_iUrgencyTimeThreshold = 30 [0..0]
- Recon Recommended = false
- RetreatersSpotting_InMinimap = true
- RetreatersSpotting_InWorld = true
- RetreatersSpotting_NoOcclusion = true
- Support Recommended = false

**Maps:** 4 map entries per the brief, but those layers hold only mesh databases (no GEMs, no sectors, capture points or HQs). No layout data exists for Operations in these files.
**State:** rules and UI/round logic detailed; map layers are stubs. Rules-only.

## 5. Raid
**What the files say.** An attacker/defender sector mode with a reach check: 10 attackers (RAID_iReachNumPlayersNeeded) must stay on a point for 10 s (RAID_fReachTimeToHold); `Raid_Reach_ViewModel` has AttackersOnPoint, ReachCollection, ReachTarget. Objectives are captured (30 s) and neutralised (30 s) with player-count and objective-count multiplier tables (same shape as Operations). New sectors unlock after 15 s, sector time 10, clear-target time 10 s. Per-team respawn delay tables of 15 entries each.
**Rule asset:** MUT_Raid, 20 tweakables.
**Rule values:**
- Assault Recommended = false
- Engineer Recommended = false
- RAID_fCaptureObjectiveCountMultipliers = {"Field_ffba60f0": [0.0, 1.0, 1.0, 1.0]} [0.0..0.0]
- RAID_fCapturePlayersMultipliers = {"Field_ffba60f0": [0.0, 1.0, 1.1, 1.1, 1.3, 1.3, 1.5, 1.5, 2.0]} [0.0..0.0]
- RAID_fCaptureTeamsMultipliers = {"Field_ffba60f0": [1.0, 1.0, 1.0]} [0.0..0.0]
- RAID_fClearTargetTime = 10.0 [1.0..1000.0]
- RAID_fNeutralizationObjectiveCountMultipliers = {"Field_ffba60f0": [0.0, 1.0, 1.0, 1.0]} [0.0..0.0]
- RAID_fNeutralizationTeamsMultipliers = {"Field_ffba60f0": [1.0, 1.0, 1.0]} [0.0..0.0]
- RAID_fObjectiveCaptureTime = 30.0 [0.0..1000.0]
- RAID_fObjectiveNeutralizationTime = 30.0 [0.0..1000.0]
- RAID_fReachTimeToHold = 10.0 [0.0..1000.0]
- RAID_fRespawnDelay_T1 = {"Field_ffba60f0": [12.0, 9.0, 6.0, 6.0, 6.0, 12.0, 9.0, 9.0, 6.0, 6.0, 12.0, 12.0, 12.0, 9.0, 6.0]} [0.0..0.0]
- RAID_fRespawnDelay_T2 = {"Field_ffba60f0": [12.0, 12.0, 12.0, 12.0, 12.0, 9.0, 9.0, 12.0, 12.0, 12.0, 6.0, 6.0, 6.0, 9.0, 12.0]} [0.0..0.0]
- RAID_fTimeToUnlockNewSector = 15.0 [0.0..1000.0]
- RAID_iReachNumPlayersNeeded = 10 [1..100]
- RAID_iSectorTime = 10 [0..999]
- RAID_iTimeWarningThreshold = 120 [0..999]
- RAID_iUrgencyTimeThreshold = 60 [0..999]
- Recon Recommended = false
- Support Recommended = false

**Maps:** none found in the given files.
**State:** rules only (plus one HUD view-model); no layers.

## 6. Shutdown
**What the files say.** A device mode: a device is deployed (10 s), stays planted 45 s, can be disarmed (10 s), is destroyed (5 s), and when dropped lasts 45 s. Holding it ticks score (1 per 3.0 s, bonus 10) toward a round target of 90 in a 7-minute round (minutes assumed).
**Rule asset:** MUT_Shutdown, 14 tweakables.
**Rule values:**
- Assault Recommended = false
- Engineer Recommended = false
- Recon Recommended = false
- Shutdown_fDeviceDeployDuration = 10.0 [0.0..0.0]
- Shutdown_fDeviceDestroyedDuration = 5.0 [0.0..0.0]
- Shutdown_fDeviceDisarmDuration = 10.0 [0.0..0.0]
- Shutdown_fDeviceDroppedDuration = 45.0 [0.0..0.0]
- Shutdown_fDevicePlantedDuration = 45.0 [0.0..0.0]
- Shutdown_fObjectiveScoreTickRate = 3.0 [0.0..0.0]
- Shutdown_fRoundDuration = 7.0 [0.0..0.0]
- Shutdown_iObjectiveScoreBonus = 10 [0..0]
- Shutdown_iObjectiveScorePerTick = 1 [0..0]
- Shutdown_iRoundTargetScore = 90 [0..0]
- Support Recommended = false

**Maps:** none found. **State:** rules only (stub).

## 7. Spooky Rush
**What the files say.** A Halloween event variant of Rush (SPKYRS_ prefix): sectors, attackers with respawn tickets (75 initial), defenders, sector time 10. Objectives are `Objective_Marker_Altar` / `Objective_Marker` rather than M-COMs. Hallucination-based text, delayed despawn on death (3 s), and a `Collection_Event` loot mechanic (base drop rate 0.2, max 25 per player and 400 per round, auto pickup, contract carrier marked on AI only, shown to the killer only) suggesting kills drop collectibles. Objective table `AD_Objective_SpookyRush`: Sector, Objective_Marker_Altar, Objective_Marker, HQ, Insertion, VehicleSpawner (24), StationarySpawner, Battle_Pickup (5), Collection_Event.
**Rule asset:** MUT_SpookyRush, 48 tweakables, plus GM launch function and GME_Sim/Pres round graphs.
**Rule values:**
- SPKYRS_AllowAttackTAOrders = true
- SPKYRS_AllowDefendTAOrders = false
- SPKYRS_AllowDefuseTAOrders = true
- SPKYRS_AllowGuardTAOrders = true
- SPKYRS_Assault Recommended = false
- SPKYRS_AttackOrderReactivationDelay = 20.0 [0.0..360.0]
- SPKYRS_AttackerRespawnDelays = {"Field_ffba60f0": [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]} [1.0..60.0]
- SPKYRS_CollectionEvent_BaseDropRate = 0.2 [0.0..1.0]
- SPKYRS_CollectionEvent_IsAutoPickup = true
- SPKYRS_CollectionEvent_MarkOnlyAIAsContractCarrier = true
- SPKYRS_CollectionEvent_MaxSpawnPerPlayer = 25 [0..0]
- SPKYRS_CollectionEvent_MaxSpawnPerRound = 400 [0..0]
- SPKYRS_CollectionEvent_ShowContractOnlyForKiller = true
- SPKYRS_CommanderVoice = 0 [0..0]
- SPKYRS_DelayedDespawnOnDeath = true
- SPKYRS_DelayedDespawnOnDeathDuration = 3.0 [0.0..30.0]
- SPKYRS_EncounterType = 2 [0..3]
- SPKYRS_Engineer Recommended = false
- SPKYRS_InitialTickets = 75 [10..300]
- SPKYRS_InstantDespawnOnDeath = false
- SPKYRS_LobbyPlayerCountStartTimer = 16 [4..16]
- SPKYRS_LobbyPlayerCountToSpeedUpTimer = 16 [4..16]
- SPKYRS_OutOfBounds_TimeToReturn = 10 [0..0]
- SPKYRS_Recon Recommended = false
- SPKYRS_RemainingRespawnsThreshold1 = 50 [0..300]
- SPKYRS_RemainingRespawnsThreshold2 = 25 [0..300]
- SPKYRS_RetreatersSpotting_InMinimap = false
- SPKYRS_RetreatersSpotting_InWorld = false
- SPKYRS_RetreatersSpotting_NoOcclusion = false
- SPKYRS_RoundEndingDelay = 7.5 [0.0..10.0]
- SPKYRS_SectorAdvanceDuration = 10.0 [0.0..300.0]
- SPKYRS_SectorCleanUpDurationMax = 5.0 [0.0..300.0]
- SPKYRS_SectorCleanUpDurationMin = 0.0 [0.0..300.0]
- SPKYRS_SectorCleanUpEndedEarlyThreshold = 10.0 [5.0..15.0]
- SPKYRS_SectorRating_Major = 0.33 [0.0..1.0]
- SPKYRS_SectorRating_Minor = 0.66 [0.0..1.0]
- SPKYRS_SectorReinforcementsDuration = 5.0 [0.0..300.0]
- SPKYRS_SectorTakenDuration = 5.0 [0.0..120.0]
- SPKYRS_SectorTime = 10 [5..20]
- SPKYRS_SoldierMandownType = 0 [0..2]
- SPKYRS_SquadOrderCooldown = 30.0 [0.0..0.0]
- SPKYRS_Support Recommended = false
- SPKYRS_TacticalAdviceCooldown = 60.0 [0.0..0.0]
- SPKYRS_TimeToMarkDefenders = 5.0 [0.0..300.0]
- SPKYRS_UrgencyRemainingFuseThreshold = 0.8 [0.0..1.0]
- SPKYRS_UrgencyRemainingRespawnsThreshold = 15 [0..300]
- SPKYRS_UrgencyRemainingSectorTimeThreshold = 120.0 [0.0..600.0]
- SPKYRS_UseHallucinationBasedText = true

**Maps:** 1 layer, Area 51 (MP_DryLake): `SpookyRush`, `spookyrush0`, `_Global`, `_Disabled`, `_Lighting`, `_VFX` and art layers `Art_ColdHangar`, `Art_CommunicationCenter`, `Art_Crater`. 78 instances: 45 VehicleSpawner (18 PTV QuadBike, 18 DirtBike, 7 LightTransport, 1 IFV, 1 TransportHelicopter), 11 Battle_Pickup (all DSPulse), 6 HQ, 4 Sector, 4 Objective_Marker_Altar, 4 Insertion, 1 Objective_Marker, 1 Collection_Event, 1 GadgetBlocking, 1 SpecialCombatArea. No M-COMs. Coordinates (x, z):
- Altars (4): (542, 936) and (516, 1050) in the east group; (222, 1002) and (227, 962) in the central group. One plain `Objective_Marker` at (-25, 933), with a GadgetBlocking volume at (-4, 931) and an HQ at (-8, 1045).
- HQs (6): (-292, 962), (-8, 1045), (224, 1006) (on the central altars), (292, 1052), (541, 987), (1011, 816). Sectors (4): (-354, 1009), (202, 927), (253, 927), (886, 874). A west-to-east line of sectors with HQ spawn areas, as in a Rush push; altars take the place of M-COMs. SpecialCombatArea centred (307, 1014).
- Versus the Rush layout: there is no Rush map file in this folder, so I cannot diff it. The objective table shows the difference in kind: Rush places Objective_MCOM, this mode places Marker_Altar / Marker plus Collection_Event and DSPulse battle pickups, and no M-COMs.
**State:** full rules plus a full layer on Area 51; a finished event mode with no UI entry.

## 8. Tank Hunt
**What the files say.** A vehicle-centred mode: score for destroying a tank (3), eliminations on, points per tank off, tank control points off. The proximity tables are spawn-selection weights (enemy near -35 / far -4, teammates near 33 / far 7 / very far 3, previous death -13), with squad spawning on. Armor multiplier 1.5, vehicle spawn time 45 s, round time 12 min, target score 20 (units assumed).
**Rule asset:** MUT_TankHunt, 46 tweakables.
**Rule values:**
- Assault Recommended = false
- Engineer Recommended = false
- Recon Recommended = false
- Support Recommended = false
- TH_OOB_Time = 10 [0..0]
- TH_bEnableSquadSpawning = true
- TH_fEnemyProximityFarMaxRadius = 35.0 [0.0..0.0]
- TH_fEnemyProximityFarMinRadius = 15.0 [0.0..0.0]
- TH_fEnemyProximityNearMaxRadius = 15.0 [0.0..0.0]
- TH_fEnemyProximityNearMinRadius = 0.0 [0.0..0.0]
- TH_fEnemyWorldIconFlashTime = 3.0 [0.0..0.0]
- TH_fPreviousDeathProximityMaxRadius = 20.0 [0.0..0.0]
- TH_fPreviousDeathProximityMinRadius = 0.0 [0.0..0.0]
- TH_fPreviousDeathProximityScore = -13 [0..0]
- TH_fTeamProximityFarMaxRadius = 35.0 [0.0..0.0]
- TH_fTeamProximityFarMinRadius = 15.0 [0.0..0.0]
- TH_fTeamProximityNearMaxRadius = 15.0 [0.0..0.0]
- TH_fTeamProximityNearMinRadius = 0.0 [0.0..0.0]
- TH_fTeamProximityVeryFarMaxRadius = 50.0 [0.0..0.0]
- TH_fTeamProximityVeryFarMinRadius = 35.0 [0.0..0.0]
- TH_iEnemyProximityFarScore = -4 [0..0]
- TH_iEnemyProximityNearScore = -35 [0..0]
- TH_iLobbyPlayerCountStartTimer = 16 [0..0]
- TH_iLobbyPlayerCountToSpeedUpTimer = 16 [0..0]
- TH_iTeamProximityFarScore = 7 [0..0]
- TH_iTeamProximityNearScore = 33 [0..0]
- TH_iTeamProximityVeryFarScore = 3 [0..0]
- bTH_EnablePointsForEliminations = true
- bTH_EnablePointsForTankControl = false
- bTH_PointsPerTank = false
- bTH_SoldierBleedoutOnSquadWipe = false
- fTH_ArmorMultiplier = 1.5 [0.1..0.0]
- fTH_RoundTime = 12.0 [0.0..0.0]
- fTH_SpawnSelectDelayIntro = 3.0 [0.0..0.0]
- fTH_SpawnSelectDelayMidRound = 10.0 [0.0..0.0]
- fTH_TeamScoringCooldown = 2.0 [0.0..0.0]
- fTH_VehicleSpawnPreventionRadius = 3.5 [0.0..0.0]
- fTH_VehicleSpawnTime = 45.0 [0.0..0.0]
- iTH_BigLeadThreshold = 0 [0..0]
- iTH_ProgressCheckpointFirst = 0 [0..0]
- iTH_ProgressCheckpointSecond = 0 [0..0]
- iTH_ProgressCheckpointThird = 15 [0..0]
- iTH_ScoreForDestroyingTank = 3 [0..1000]
- iTH_SoldierManDownType = 1 [0..2]
- iTH_TargetScore = 20 [0..0]
- iTH_UrgencyTimeThreshold = 60 [0..0]

**Maps:** none found. **State:** rules only.

## 9. Squad Shootout
**What the files say.** A multi-round squad match: 3 rounds with target scores 50 / 30 / 20 and times 7 / 5 / 3 (minutes assumed).
**Rule asset:** MUT_SquadShootout, 11 tweakables.
**Rule values:**
- Assault Recommended = false
- Engineer Recommended = false
- Recon Recommended = false
- SQUADSO_fRound1Time = 7.0 [0.0..0.0]
- SQUADSO_fRound2Time = 5.0 [0.0..0.0]
- SQUADSO_fRound3Time = 3.0 [0.0..0.0]
- SquadSO_iRound1TargetScore = 50 [0..0]
- SquadSO_iRound2TargetScore = 30 [0..0]
- SquadSO_iRound3TargetScore = 20 [0..0]
- SquadSO_iRounds = 3 [0..0]
- Support Recommended = false

**Maps:** none found. **State:** rules only (small stub).

## 10. Free Roam
**What the files say.** An empty round-based shell: GME_Sim/Pres_Freeroam_Round reference MI_FreeRoam_Tweaks (no values), plus DiceEx_Freeroam_LaunchFunction. Objective table `AD_RoundBasedMode_FreeRoam` holds only a DeployCam. No MUT asset.
**Maps:** none found. **State:** stub.

## 11. Gauntlet
**What the files say (UI text).** "Battle to complete a series of missions. Squads with the lowest scores in each mission are eliminated. The last squad standing wins." Panels: AVOID ELIMINATION (qualify every mission to reach the final), COMPLETE MISSIONS (objectives and locales change each mission; points for objectives, kills, revives), REINFORCEMENTS (a top performer from an eliminated squad joins you when you lose a squadmate). A "HARDCORE GAUNTLET" label exists. No MUT_Gauntlet asset in the files.
**Map layers (2):**
- Tsuru Reef (MP_Isolated): `DallasGauntlet` layers (Layer, Layout, Layout_Global, Layout_JetsOnly, two Extraction layers, schematics, IsolatedModesMetadata and IsolatedLayoutsMetadata, mesh databases). Contents: 6 HQ, 18 VehicleSpawner (6 FighterPlane, 6 MultirolePlane, 6 NavalFighterPlane), 6 Insertion, 51 Gauntlet_JetsOnly_Stockpile, 23 Gauntlet_JetsOnly_CloudVFX, and one each of ProximitySpawns, SpecialCombatArea, TelemetryArea, CombatArea. So the layer shows a jets-only air-combat mission with stockpile points over the reef, plus extraction layouts; other missions are not visible.
- Empire State (MP_Aftermath): only `Partition_UI`; no gameplay objects.
**State:** live mode; layers on Tsuru Reef only (Empire State is UI only).

## Summary table

| Mode | Rule asset | Tweakables | Maps with layers | State |
|---|---|---|---|---|
| Obliteration | MUT_Obliteration | 58 | Contaminated, Railway to Golmud, Eastwood | full rules + layers |
| Squad Obliteration | MUT_SquadObliteration | 58 | Siege of Cairo, Empire State, Iberian Offensive, Cairo Bazaar | full rules + 4 layers |
| Carrier Strike | MUT_CarrierStrike | 50 | Tsuru Reef | full rules + 1 layer |
| Operations | MUT_Operations | 136 | Contaminated, Hagental Base, Mirak Valley, Liberation Peak (layers captured in modes-layers2; see GAME_MODES_2026-10-21.md, Operations section) | full rules + 4 layers |
| Raid | MUT_Raid | 20 | none | rules only |
| Shutdown | MUT_Shutdown | 14 | none | rules only (stub) |
| Spooky Rush | MUT_SpookyRush | 48 | Area 51 | full rules + 1 layer |
| Tank Hunt | MUT_TankHunt | 46 | none | rules only |
| Squad Shootout | MUT_SquadShootout | 11 | none | rules only (stub) |
| Free Roam | none | 0 | none | stub |
| Gauntlet | none | 0 | Tsuru Reef (jets-only layout); Empire State UI only | live; layers on 1 map |
