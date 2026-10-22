# Conquest analysis, build 2.1.1.0 (Season 5)

Sources: Conquest-maps.txt, Conquest-tweakables.txt (round-logic graphs only; the 59 MUT_Conquest rows are in existing-tweakables.txt), maps-tweakables.txt, ui-text.txt, objective-table.json, map-names.json. Counts were produced by scripts (folder cq-scripts next to modes-work), not by hand. Coordinates are (x, z) in metres, y noted where useful.

Conventions and limits used throughout:
- Letters (A, B, ...) are NOT stored. Flags are lettered by projecting their position onto the line from the lower-x HQ ("HQ-W") to the higher-x HQ ("HQ-E"); A is nearest HQ-W. Where the map runs mostly north-south or flags sit far off that line (Wake Island, Tsuru Reef, Area 51, Railway to Golmud) this is a weak guess. Confidence: MEDIUM on maps with a clear HQ axis, LOW on off-axis layouts (off-axis distance is printed per flag).
- Team1/team2 ownership of HQs, pads and flags is NOT stored. HQ-W/HQ-E are geometric labels only. Faction overrides come from factionOverrides (empty = engine default).
- Pad/emplacement grouping is by nearest anchor (HQ or flag, xz distance), not authored ownership. Distances are printed so doubtful assignments are visible. Air pads are often far from any flag, so their group is a convenience, not truth.
- Only layer Conquest0 holds gameplay instances. 18 maps have a Conquest layer (second capture: layers stored directly under _Layers_Gameplay, variants resolved through AD_Objective_Conquest); only Saints Quarter (MP_LIMESTONE) has none.
- Saints Quarter (MP_LIMESTONE) has no Conquest layer; its MUT_Limestone is empty (0 tweakables). Iberian Offensive has a full Conquest layer (section 2) and MUT_Battery with Battery_CQ_iInitialScore = 1200 and SpawnPreventionRadius_LargeModes_Battery = 45.0.

## 1. Mode rules (MUT_Conquest, GME_Sim_Conquest_Round)

What the game's own UI text says (ui-text.txt):
- "Fight to control objectives in a large-scale battle, wearing down the enemy until one side remains."
- Holding more objectives depletes enemy lives. Killing an enemy depletes their lives. Win by fully depleting the enemy's lives or by having more lives remaining when the time expires.
- Hardcore Conquest exists as a separate title string (no separate tweakables found).
So the UI confirms three concepts (flag bleed, kill bleed, time limit with most lives wins). It confirms NO numeric value.

Round logic: GME_Sim_Conquest_Round (40 objects) and GME_Pres_Conquest_Round (27 objects) expose only ActivityStateMachine and MI_Sim_GameMode (null); the launch function and gem collection filter have null parameters only. The shared GEM logic graphs (capture volume, sector spotting, reinforcement, supply station, vehicle spawner team, vehicle-superiority capture volume) list only null runtime variables, no numbers. Carriable_Plant, MCOM and Destructible shared graphs belong to other modes. All values below are MUT_Conquest client defaults (all 59 tweakables are listed); a server playlist can override them. "unbounded/not set" means the file shows [0..0].


#### Tickets / score / end of round

| Tweakable | Value | Range | Meaning (inferred from name unless stated) | UI text |
|---|---|---|---|---|
| CQ_iInitialScoreTeam1 | 1200 | unbounded/not set | Starting lives (tickets) team 1. Per-map MUT overrides the default (see table). | UI: lives exist (confirmed); 1200 not in UI text |
| CQ_iInitialScoreTeam2 | 1200 | unbounded/not set | Starting lives team 2. | as above |
| CQ_bUseClassicScoring | false | None | false = lives-based modern scoring; true would be classic ticket scoring (inferred from name). | not in UI |
| CQ_fDeathRatioMultiplier | 2.0 | unbounded/not set | Scale of life loss per kill/death (name; "Killing an enemy depletes their lives"). | UI confirms the mechanic, not the 2.0 |
| CQ_iModeTime | 45 | 10..180 | Round time limit. Unit not stored; minutes is likely (45 [10..180]), MEDIUM confidence. | UI confirms a time limit ("more lives remaining when the time expires"), not the value |
| CQ_bEndGameOnFullMajority | true | None | End the round when one side holds a full majority of flags. | not in UI |
| CQ_bUseTrueMajority | false | None | Majority = strictly more flags (true) vs. threshold based; false here. | not in UI |
| CQ_FullMajority_iFlagThresholdHigh | 6 | unbounded/not set | Flags a team needs for full majority when the map has many flags (6). | not in UI |
| CQ_FullMajority_iFlagThresholdLow | 3 | unbounded/not set | Flags needed on small flag counts (3). | not in UI |
| CQ_iFullMajorityCountDownLength_High | 60 | unbounded/not set | Countdown seconds (unit inferred) once full majority is reached, High flag layout. | not in UI |
| CQ_iFullMajorityCountDownLength_Low | 60 | unbounded/not set | Same, Low layout. | not in UI |
| CQ_iFullMajorityCountDownLength_Default | 60 | unbounded/not set | Same, Default. | not in UI |
| CQ_fDelayBeforeFirstMajorityEvent | 120.0 | unbounded/not set | Delay before the first majority announcement/event (120). | not in UI |
| CQ_fDelayBetweenAnyMajorityEvent | 30.0 | unbounded/not set | Gap between majority events (30). | not in UI |
| CQ_iHighScoreDeltaThreshold | 200 | unbounded/not set | Lead (lives) counted as high delta (200). | not in UI |
| CQ_iHighScoreDeltaPenalty | 1 | unbounded/not set | Penalty applied at high delta (1). | not in UI |
| CQ_iLowScoreDeltaThreshold | 100 | unbounded/not set | Lead counted as low delta (100). | not in UI |
| CQ_iLowScoreDeltaPenalty | 1 | unbounded/not set | Penalty at low delta (1). | not in UI |
| CQ_iMaxProgressToAllowPenalty | 5 | 0..6 | Highest progress stage (0..6) at which the delta penalty still applies (5). | not in UI |
| CQ_fScoreDeltaToActivateScoreCheck | 0.1 | 0.01..1.0 | Relative delta (10 percent) that triggers the score check. | not in UI |
| CQ_fProgressThreshold1 | 0.05 | 0.0..1.0 | Progress stage thresholds (fractions of match progress), 6 stages: 0.05 / 0.15 / 0.3 / 0.5 / 0.75 / 1.0. | not in UI |
| CQ_fProgressThreshold2 | 0.15 | 0.0..1.0 |  |  |
| CQ_fProgressThreshold3 | 0.3 | 0.0..1.0 |  |  |
| CQ_fProgressThreshold4 | 0.5 | 0.0..1.0 |  |  |
| CQ_fProgressThreshold5 | 0.75 | 0.0..1.0 |  |  |
| CQ_fProgressThreshold6 | 1.0 | 0.0..1.0 |  |  |
| CQ_fProgressCooldown | 120.0 | unbounded/not set | Cooldown between progress-stage announcements (120). | not in UI |
| CQ_iBigLeadThreshold | 20 | 0..100 | Lead threshold (20, range 0..100) for big-lead handling/announcement (percent likely). | not in UI |
| CQ_fUrgencyPercentageThreshold | 0.06 | 0.0..1.0 | Lives fraction (6 percent) at which urgency state starts. | not in UI |
| CQ_iUrgencyTimeThreshold | 60 | 0..120 | Seconds (60) of time left that trigger urgency. | not in UI |

#### Capture timing and player multipliers

| Tweakable | Value | Range | Meaning (inferred from name unless stated) | UI text |
|---|---|---|---|---|
| CQ_fCaptureTime | 30.0 | unbounded/not set | Seconds to capture a flag at base speed (30). | not in UI |
| CQ_fNeutralizeTime | 30.0 | unbounded/not set | Seconds to neutralize an enemy flag (30). | not in UI |
| CQ_f[]CaptureSpeedMultipliers | {"Field_ffba60f0": [0.0, 1.0, 1.333, 1.666, 2.0]} | unbounded/not set ([0.0..0.0]) | Array of 5: [0.0, 1.0, 1.333, 1.666, 2.0]. Most likely indexed by number of own players on the point: 0 -> 0, 1 -> 1.0, 2 -> 1.333, 3 -> 1.666, 4 or more -> 2.0 (inference, MEDIUM; index meaning not stored). | not in UI |

#### Bleed (life loss from flags)

| Tweakable | Value | Range | Meaning (inferred from name unless stated) | UI text |
|---|---|---|---|---|
| CQ_bUseDynamicBleedFrequency | true | None | Bleed tick interval scales with the flag lead (true). | UI confirms bleed from holding more objectives; dynamic scaling not in UI |
| CQ_fBleedFrequency | 5.0 | unbounded/not set | Base seconds per bleed tick (5.0). | as above |
| CQ_iBleedFrequencyScoreRange | 100 | unbounded/not set | Lives range (100) over which the frequency is adjusted. | not in UI |
| CQ_fBleedFrequencyLimitAddition | 3.0 | unbounded/not set | Max added to frequency (3.0). | not in UI |
| CQ_fBleedFrequencyLimitSubstract | 3.0 | unbounded/not set | Max subtracted from frequency (3.0). | not in UI |
| CQ_iBleedAmountOnCapture | 1 | unbounded/not set | Lives lost by the enemy when a flag is captured (1). | not in UI |
| CQ_bUseDeltaBleed | false | None | Bleed by flag difference (true) or per flag; false. | not in UI |
| CQ_fTEMPClassicCQMajorityBleedFrequency | 2.0 | unbounded/not set | "TEMP" classic-majority bleed interval (2.0); only relevant with classic scoring. | not in UI |

#### Respawn and downed state

| Tweakable | Value | Range | Meaning (inferred from name unless stated) | UI text |
|---|---|---|---|---|
| CQ_fPlayerRespawnDelay | 12.0 | 0.0..100.0 | Seconds (12) default respawn delay. | not in UI |
| CQ_fTeam1RespawnDelay | 12.0 | 0.0..100.0 | Team 1 respawn delay (12). | not in UI |
| CQ_fTeam2RespawnDelay | 12.0 | 0.0..100.0 | Team 2 respawn delay (12). | not in UI |
| CQ_iSoldierMandownType | 1 | 0..2 | Man-down behaviour enum 0..2 (1). | not in UI |

#### Vehicle cooldown fallbacks

None. MUT_Conquest has no tweakable of this kind; the round graph GME_Sim_Conquest_Round exposes only ActivityStateMachine and MI_Sim_GameMode (both null). Any cooldown or XP value must come from shared vehicle/progression data outside this extraction.

#### Out of bounds

| Tweakable | Value | Range | Meaning (inferred from name unless stated) | UI text |
|---|---|---|---|---|
| CQ_iOutOfBounds_TimeToReturn | 10 | unbounded/not set | Seconds a player may stay outside the combat area before dying (10). | not in UI |

#### XP

None. MUT_Conquest has no tweakable of this kind; the round graph GME_Sim_Conquest_Round exposes only ActivityStateMachine and MI_Sim_GameMode (both null). Any cooldown or XP value must come from shared vehicle/progression data outside this extraction.

#### Lobby and idle

| Tweakable | Value | Range | Meaning (inferred from name unless stated) | UI text |
|---|---|---|---|---|
| CQ_iLobbyPlayerCountStartTimer | 32 | 0..128 | Players needed to start the pre-round timer (32 [0..128]). | not in UI |
| CQ_iLobbyPlayerCountToSpeedUpTimer | 64 | unbounded/not set | Players at which the timer speeds up (64). | not in UI |
| CQ_fNoInteractivityTimeoutOverride | 120.0 | 0.0..600.0 | Idle/no-interaction timeout seconds (120 [0..600]). | not in UI |

#### Layout, UI, audio, squad (not rules)

| Tweakable | Value | Range | Meaning (inferred from name unless stated) | UI text |
|---|---|---|---|---|
| CQ_LayoutSelection | 0 | 0..3 | Layout selector 0..3 (0). Only layer Conquest0 exists in the data for every map, so 1..3 have no content in this build (MEDIUM). | not in UI |
| CQ_fTacticalAdviceCooldown | 60.0 | unbounded/not set | Tactical advice cooldown (60). | not in UI |
| CQ_fWeightScaleTimeThreshold | 300.0 | unbounded/not set | Time (300) after which weighting scales (name only; purpose unclear, LOW). | not in UI |
| CQ_fSquadOrderCooldown | 30.0 | unbounded/not set | Squad order cooldown (30). | not in UI |
| CQ_iCommanderVoice | 0 | unbounded/not set | Commander voice index (0). | not in UI |
| CQ_fAudioFalloffDistanceToObjective | 1.0 | 1.0..200.0 | Audio falloff distance (1.0 [1..200]). | not in UI |
| Assault Recommended | false | None | Class recommendation flag, false. | not in UI |
| Engineer Recommended | false | None | false. | not in UI |
| Support Recommended | false | None | false. | not in UI |
| Recon Recommended | false | None | false. | not in UI |


#### Per-map Conquest values (maps-tweakables.txt)

| Map | Conquest initial score (per-map MUT) | Other per-map tweakables |
|---|---|---|
| Siege of Cairo | 1200 (Abbasid_CQ_iInitialScore) | SpawnPreventionRadius_Small = 40.0 |
| Empire State | 1200 (Aftermath_CQ_iInitialScore) |  |
| Blackwell Fields | 1200 (Badlands_CQ_iInitialScore) |  |
| Liberation Peak | 1200 (Capstone_CQ_iInitialScore) |  |
| Manhattan Bridge | 1200 (Dumbo_CQ_iInitialScore) | MP_Dumbo_VehicleOOBtime = 10 [1..15] (vehicle out-of-bounds time; the only vehicle-related timer found) |
| Eastwood | 1200 (Eastwood_CQ_iInitialScore) |  |
| Operation Firestorm | 1200 (FireStorm_CQ_iInitialScore) |  |
| New Sobek City | 1200 (Outskirts_CQ_iInitialScore) |  |
| Mirak Valley | 1200 (Tungsten_CQ_iInitialScore) |  |
| Railway to Golmud | none (MUT_Golmud has no CQ score; MUT_Conquest default 1200 applies) | Golmud_Conquest_EnableMovingTrain = true; Golmud_Escalation_EnableMovingTrain = true; Golmud_MovingTrain_StreamIn = true |
| Iberian Offensive | 1200 (Battery_CQ_iInitialScore) | SpawnPreventionRadius_LargeModes_Battery = 45.0 |
| Saints Quarter | none (empty MUT) | no Conquest layer |
| Wake Island | none (no MUT; default 1200) |  |
| Contaminated | none (no MUT; default 1200) |  |
| Area 51 | none (no MUT; default 1200) |  |
| Tsuru Reef | none (no MUT; default 1200) |  |
| Vegas Strip | none (no MUT; default 1200) |  |
| Cairo Bazaar | none (no MUT; default 1200) |  |
| Hagental Base | none (no MUT; default 1200) |  |

Every per-map initial score is 1200, identical to the MUT_Conquest default (CQ_iInitialScoreTeam1/2 = 1200). The per-map key names suggest they override the mode default (MEDIUM; the read order is not stored). MUT_Propaganda (test range) has 0 tweakables.

## 2. Maps


### Siege of Cairo (MP_ABBASID)

- Layer assets: Conquest_Telemetry, Conquest_Global, Conquest_Global_Schematic, Conquest_Global_ecsprefab_ecsPrefab, Conquest, Conquest0_Schematic, conquest/MeshVariationDb_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry, Game/GlacierMP/Levels/MP_Abbasid/_Layers_Gameplay/Conquest0.
- factionOverrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- GEM counts: {"GEM_CapturePoint": 5, "GEM_VehicleResupplyStation": 4, "GEM_Insertion": 16, "GEM_VehicleSpawner": 4, "GEM_VehicleSpawner_Forward": 4, "GEM_CapturePoint_OutlineArea": 6, "GEM_Collection_Event": 1, "GEM_Battle_Pickup": 2, "GEM_Sector": 1, "GEM_HQ": 2}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` are not among this map's assets.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@190` pos (-276, 74) y=67 polys=[188]
  - HQ-E `@182` pos (122, -60) y=65 polys=[67]
- HQ-to-HQ distance 419 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@98` (-156, 50) y=67 key=-1 t=0.29 off-axis 16 m; OutlineArea x1 (dist 6 m; @134)
  - B `@6` (-178, -29) y=65 key=-1 t=0.30 off-axis 66 m; OutlineArea x1 (dist 1 m; @34)
  - C `@124` (-80, -14) y=62 key=-1 t=0.51 off-axis 21 m; OutlineArea x1 (dist 7 m; @86)
  - D `@1` (-2, -63) y=60 key=-1 t=0.72 off-axis 42 m; OutlineArea x2 (dist 3/2 m; @71,214)
  - E `@146` (28, 18) y=64 key=-1 t=0.73 off-axis 44 m; OutlineArea x1 (dist 5 m; @48)
  - OutlineArea instances: 6 total, 0 farther than 150 m from any flag (none)
- Vehicle spawner pads: 4 total (IFV 2, Tank 2)
  - near HQ-W: 2 pads (IFV 1, Tank 1); distance median 27 m, max 28 m
  - near HQ-E: 2 pads (IFV 1, Tank 1); distance median 36 m, max 52 m
  - Air pads: none
- Forward spawners: 4 (VehicleSpawner_Forward 4)
  - by nearest anchor: HQ-W 2 (VehicleSpawner_Forward 2); HQ-E 2 (VehicleSpawner_Forward 2)
- Stationary emplacements: none
- Automatic AA: none
- Resupply stations: 4 (Ground 4)
  - by nearest anchor: HQ-W 1 (Ground 1); HQ-E 1 (Ground 1); flag B 1 (Ground 1); flag E 1 (Ground 1)
- No SpecialCombatArea instance; largest Conquest0 polygon (objective area, not a play area: it holds no HQ; LOW confidence): @169 bbox [-253.0, -128.0, 88.0, 130.0]
- Other: TelemetryArea 0; Battle_Pickup 2 (Battle_Pickup_Minigun 1, Battle_Pickup_Railgun 1); Collection_Event 1 (CollectionEvent 1); Sector 1 (Sector 1)
  - Battle_Pickup `@60` Minigun (-128, -7)
  - Battle_Pickup `@216` Railgun (-48, 25)

### Empire State (MP_AFTERMATH)

- Layer assets: Conquest, Conquest0, Conquest0_Schematic, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, Conquest_VFX, Conquest_VFX_Schematic, Winter_Conquest, Winter_Conquest0, generated/DD_Conquest0_Schematics, generated/DD_Conquest0_Volumes, conquest/MeshVariationDb_Win32, conquest/staticmodelgroup.physics, conquest_networkregistry_Win32, conquest_templatedescriptorregistry, winter_conquest/MeshVariationDb_Win32, winter_conquest_networkregistry_Win32.
- factionOverrides: {}
- GEM counts: {"GEM_Sector": 1, "GEM_StationarySpawner": 6, "GEM_Insertion": 16, "GEM_CapturePoint": 5, "GEM_TelemetryArea": 8, "GEM_Battle_Pickup": 2, "GEM_HQ": 3, "GEM_CapturePoint_OutlineArea": 1, "GEM_Collection_Event": 1}
- Layout variants: only layer `Conquest0` carries gameplay data (plus `Winter_Conquest0` asset, not decoded in this extraction). `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (3), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-1(lowest x) `@162` pos (-674, -150) y=56 polys=[94]
  - HQ-2 `@154` pos (-555, -142) y=54 polys=[170] (no Insertions: non-spawn marker; the live spawn HQs are @162 and @97, 8 Insertions each)
  - HQ-3 `@97` pos (-526, 46) y=64 polys=[142]
- HQ-to-HQ distance 246 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@23` (-571, -140) y=54 key=-1 t=0.29 off-axis 77 m; no OutlineArea
  - B `@119` (-656, -19) y=63 key=-1 t=0.47 off-axis 64 m; no OutlineArea
  - C `@179` (-602, -31) y=56 key=-1 t=0.56 off-axis 14 m; no OutlineArea
  - D `@80` (-556, -31) y=60 key=-1 t=0.68 off-axis 23 m; no OutlineArea
  - E `@189` (-649, 69) y=54 key=-1 t=0.77 off-axis 113 m; OutlineArea x1 (dist 4 m; @151)
  - OutlineArea instances: 1 total, 0 farther than 150 m from any flag (none)
- Vehicle spawner pads: 0 total (-)
  - Air pads: none
- Forward spawners: none
- Stationary emplacements: 6 (HMG 6)
  - by nearest anchor: HQ-1(lowest x) 2 (HMG 2); HQ-3 1 (HMG 1); flag C 2 (HMG 2); flag E 1 (HMG 1)
- Automatic AA: none
- Resupply stations: none
- No SpecialCombatArea instance; largest Conquest0 polygon (inferred play area, LOW confidence): @170 bbox [-708.0, -198.0, -514.0, 148.0]
- Other: TelemetryArea 8; Battle_Pickup 2 (Battle_Pickup_Minigun 2); Collection_Event 1 (CollectionEvent 1); Sector 1 (Sector 1)
  - Battle_Pickup `@77` Minigun (-677, -48)
  - Battle_Pickup `@127` Minigun (-525, -40)

### Wake Island (MP_ATOLL)

- Layer assets: Conquest, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, generated/AG_Conquest_DynamicDD_Schematic_2E9D5A6C, generated/AG_Conquest_DynamicDD_boxes_7A2324E9, Conquest0, Conquest0_Schematic, Conquest_Cover, Conquest_Global, conquest/MeshVariationDb_Win32, conquest/staticmodelgroup.physics, conquest_networkregistry_Win32, conquest_templatedescriptorregistry.
- factionOverrides: {}
- GEM counts: {"GEM_VehicleSpawner": 40, "GEM_Insertion": 16, "GEM_HQ": 2, "GEM_StationarySpawner": 10, "GEM_CapturePoint": 7, "GEM_TelemetryArea": 7, "GEM_VehicleResupplyStation": 6, "GEM_AutomaticAA": 2, "GEM_Collection_Event": 1, "GEM_Sector": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@78` pos (-683, 324) y=115 polys=[197]
  - HQ-E `@5` pos (220, -592) y=115 polys=[130]
- HQ-to-HQ distance 1286 m. Capture points (7, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@175` (-114, 161) y=96 key=-1 t=0.40 off-axis 291 m; no OutlineArea
  - B `@17` (222, 420) y=99 key=-1 t=0.44 off-axis 713 m; no OutlineArea
  - C `@109` (410, 431) y=100 key=-1 t=0.54 off-axis 854 m; no OutlineArea
  - D `@163` (225, 147) y=99 key=-1 t=0.59 off-axis 523 m; no OutlineArea
  - E `@129` (106, -111) y=107 key=-1 t=0.67 off-axis 257 m; no OutlineArea
  - F `@209` (496, 216) y=106 key=-1 t=0.70 off-axis 765 m; no OutlineArea
  - G `@63` (379, -98) y=100 key=-1 t=0.81 off-axis 460 m; no OutlineArea
- Vehicle spawner pads: 40 total (RHIB 13, PatrolBoat 10, AttackHelicopter 3, LightTransport 3, PTV_QuadBike 3, Tank 3, MultirolePlane 2, TransportHelicopter 2, NavalFighterPlane 1)
  - near HQ-W: 11 pads (RHIB 6, PatrolBoat 2, AttackHelicopter 1, MultirolePlane 1, TransportHelicopter 1); distance median 79 m, max 119 m
  - near HQ-E: 11 pads (RHIB 6, PatrolBoat 2, AttackHelicopter 1, MultirolePlane 1, TransportHelicopter 1); distance median 62 m, max 131 m
  - near flag A: 2 pads (LightTransport 1, PatrolBoat 1); distance median 37 m, max 46 m
  - near flag B: 2 pads (PTV_QuadBike 1, Tank 1); distance median 77 m, max 101 m
  - near flag C: 5 pads (AttackHelicopter 1, LightTransport 1, NavalFighterPlane 1, PTV_QuadBike 1, Tank 1); distance median 82 m, max 146 m
  - near flag D: 4 pads (PatrolBoat 3, RHIB 1); distance median 33 m, max 133 m
  - near flag E: 2 pads (LightTransport 1, PatrolBoat 1); distance median 96 m, max 133 m
  - near flag G: 3 pads (PTV_QuadBike 1, PatrolBoat 1, Tank 1); distance median 35 m, max 70 m
  - Air pads: AttackHelicopter 3, TransportHelicopter 2, MultirolePlane 2, NavalFighterPlane 1
- Forward spawners: none
- Stationary emplacements: 10 (AntiTank 5, AntiAircraft 3, HMG 2)
  - by nearest anchor: flag B 1 (AntiTank 1); flag C 2 (AntiAircraft 1, AntiTank 1); flag E 3 (AntiAircraft 1, AntiTank 1, HMG 1); flag F 3 (AntiAircraft 1, AntiTank 1, HMG 1); flag G 1 (AntiTank 1)
- Automatic AA: 2 (AutomaticAA 2)
  - by nearest anchor: HQ-W 1 (AutomaticAA 1); HQ-E 1 (AutomaticAA 1)
- Resupply stations: 6 (Ground 3, Ground_Air 3)
  - by nearest anchor: HQ-W 1 (Ground_Air 1); HQ-E 1 (Ground_Air 1); flag B 1 (Ground 1); flag C 1 (Ground_Air 1); flag F 1 (Ground 1); flag G 1 (Ground 1)
- No SpecialCombatArea instance; largest Conquest0 polygon (objective area, not a play area: it holds no HQ; LOW confidence): @183 bbox [-509.0, -452.0, 823.0, 730.0]
- Other: TelemetryArea 7; Collection_Event 1 (CollectionEvent 1); Sector 1 (Sector 1)

### Blackwell Fields (MP_BADLANDS)

- Layer assets: Conquest, Conquest0, Conquest0_Schematic, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, generated/DD_Conquest0_Schematics, generated/DD_Conquest0_Volumes, conquest/MeshVariationDb_Win32, conquest/staticmodelgroup.physics, conquest_networkregistry_Win32, conquest_templatedescriptorregistry.
- factionOverrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- GEM counts: {"GEM_VehicleSpawner": 28, "GEM_CapturePoint": 6, "GEM_SpecialCombatArea": 1, "GEM_Insertion": 16, "GEM_VehicleResupplyStation": 5, "GEM_AutomaticAA": 2, "GEM_StationarySpawner": 5, "GEM_Battle_Pickup": 2, "GEM_TelemetryArea": 6, "GEM_HQ": 2, "GEM_Sector": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@111` pos (-140, -517) y=87 polys=[52, 129]
  - HQ-E `@84` pos (308, 62) y=72 polys=[126, 129]
- HQ-to-HQ distance 732 m. Capture points (6, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@90` (-106, -328) y=76 key=-1 t=0.23 off-axis 90 m; no OutlineArea
  - B `@3` (36, -387) y=84 key=-1 t=0.29 off-axis 59 m; no OutlineArea
  - C `@39` (-62, -170) y=71 key=-1 t=0.44 off-axis 152 m; no OutlineArea
  - D `@182` (107, -182) y=76 key=-1 t=0.57 off-axis 10 m; no OutlineArea
  - E `@170` (46, -28) y=70 key=-1 t=0.68 off-axis 153 m; no OutlineArea
  - F `@110` (262, -84) y=75 key=-1 t=0.80 off-axis 52 m; no OutlineArea
- Vehicle spawner pads: 28 total (LightTransport 8, APC 4, Tank 4, AttackHelicopter 2, AttackPlane 2, FighterPlane 2, IFV 2, MobileAA 2, PTV_DirtBike 2)
  - near HQ-W: 11 pads (APC 2, LightTransport 2, Tank 2, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 1, MobileAA 1); distance median 24 m, max 100 m
  - near HQ-E: 11 pads (APC 2, LightTransport 2, Tank 2, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 1, MobileAA 1); distance median 19 m, max 124 m
  - near flag A: 1 pads (LightTransport 1); distance median 25 m, max 25 m
  - near flag B: 1 pads (PTV_DirtBike 1); distance median 43 m, max 43 m
  - near flag C: 1 pads (LightTransport 1); distance median 12 m, max 12 m
  - near flag D: 1 pads (PTV_DirtBike 1); distance median 44 m, max 44 m
  - near flag E: 1 pads (LightTransport 1); distance median 14 m, max 14 m
  - near flag F: 1 pads (LightTransport 1); distance median 29 m, max 29 m
  - Air pads: AttackPlane 2, AttackHelicopter 2, FighterPlane 2
- Forward spawners: none
- Stationary emplacements: 5 (AntiTank 4, AntiAircraft 1)
  - by nearest anchor: flag A 1 (AntiTank 1); flag C 1 (AntiTank 1); flag E 2 (AntiAircraft 1, AntiTank 1); flag F 1 (AntiTank 1)
- Automatic AA: 2 (AutomaticAA 2)
  - by nearest anchor: HQ-W 1 (AutomaticAA 1); HQ-E 1 (AutomaticAA 1)
- Resupply stations: 5 (Ground 3, Ground_Air 2)
  - by nearest anchor: HQ-W 2 (Ground 1, Ground_Air 1); HQ-E 2 (Ground 1, Ground_Air 1); flag E 1 (Ground 1)
- SpecialCombatArea: 1 instance(s) (@8); containing polygons: @129 POLY13 bbox [-1097.0, -1315.0, 1182.0, 849.0] (2279 x 2164 m)
- Other: TelemetryArea 6; Battle_Pickup 2 (Battle_Pickup_Minigun 1, Battle_Pickup_Railgun 1); Sector 1 (Sector 1)
  - Battle_Pickup `@78` Railgun (-36, -173)
  - Battle_Pickup `@159` Minigun (127, -218)

### Iberian Offensive (MP_BATTERY)

- Layer assets: Game/GlacierMP/Levels/MP_Battery/_Layers_Gameplay/Conquest0.
- factionOverrides: {}
- GEM counts: {"GEM_CapturePoint": 5, "GEM_TelemetryArea": 5, "GEM_VehicleSpawner": 8, "GEM_Insertion": 16, "GEM_CapturePoint_OutlineArea": 2, "GEM_VehicleSpawner_Forward": 3, "GEM_Battle_Pickup": 3, "GEM_VehicleResupplyStation": 4, "GEM_Sector": 1, "GEM_Collection_Event": 1, "GEM_HQ": 2}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` are not among this map's assets.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@96` pos (579, 118) y=70 polys=[98]
  - HQ-E `@118` pos (924, 134) y=75 polys=[136]
- HQ-to-HQ distance 346 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@139` (640, 201) y=76 key=-1 t=0.19 off-axis 80 m; no OutlineArea
  - B `@15` (706, 98) y=75 key=-1 t=0.36 off-axis 26 m; no OutlineArea
  - C `@125` (779, 157) y=82 key=-1 t=0.58 off-axis 30 m; OutlineArea x2 (dist 9/8 m; @24,103)
  - D `@163` (825, 56) y=74 key=-1 t=0.70 off-axis 73 m; no OutlineArea
  - E `@1` (871, 209) y=86 key=-1 t=0.86 off-axis 77 m; no OutlineArea
  - OutlineArea instances: 2 total, 0 farther than 150 m from any flag (none)
- Vehicle spawner pads: 8 total (LightTransport 6, IFV 2)
  - near HQ-W: 3 pads (LightTransport 2, IFV 1); distance median 4 m, max 5 m
  - near HQ-E: 3 pads (LightTransport 2, IFV 1); distance median 11 m, max 12 m
  - near flag A: 1 pads (LightTransport 1); distance median 35 m, max 35 m
  - near flag E: 1 pads (LightTransport 1); distance median 80 m, max 80 m
  - Air pads: none
- Forward spawners: 3 (VehicleSpawner_Forward 3)
  - by nearest anchor: HQ-W 3 (VehicleSpawner_Forward 3)
- Stationary emplacements: none
- Automatic AA: none
- Resupply stations: 4 (Ground 4)
  - by nearest anchor: HQ-W 1 (Ground 1); HQ-E 1 (Ground 1); flag C 2 (Ground 2)
- No SpecialCombatArea instance; largest Conquest0 polygon (inferred play area, LOW confidence): @107 bbox [569.0, 3.0, 943.0, 292.0]
- Other: TelemetryArea 5; Battle_Pickup 3 (Battle_Pickup_Minigun 2, Battle_Pickup 1); Collection_Event 1 (CollectionEvent 1); Sector 1 (Sector 1)
  - Battle_Pickup `@36` Minigun (793, 155)
  - Battle_Pickup `@84` GMPF_Battle_Pickup (773, 112)
  - Battle_Pickup `@146` Minigun (690, 96)

### Liberation Peak (MP_CAPSTONE)

- Layer assets: Conquest, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, Conquest0, Conquest0_Schematic, conquest/MeshVariationDb_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry.
- factionOverrides: {}
- GEM counts: {"GEM_TelemetryArea": 6, "GEM_VehicleSpawner": 26, "GEM_Insertion": 16, "GEM_CapturePoint": 6, "GEM_CapturePoint_OutlineArea": 5, "GEM_HQ": 2, "GEM_VehicleResupplyStation": 7, "GEM_Battle_Pickup": 4, "GEM_SpecialCombatArea": 2, "GEM_Sector": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@49` pos (-312, 100) y=130 polys=[115, 163]
  - HQ-E `@63` pos (275, 451) y=139 polys=[80, 115]
- HQ-to-HQ distance 684 m. Capture points (6, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@25` (-161, 167) y=137 key=-1 t=0.24 off-axis 20 m; no OutlineArea
  - B `@79` (-30, 90) y=134 key=-1 t=0.35 off-axis 153 m; OutlineArea x1 (dist 14 m; @239)
  - C `@237` (109, 86) y=134 key=-1 t=0.52 off-axis 228 m; OutlineArea x1 (dist 8 m; @37)
  - D `@44` (40, 213) y=159 key=-1 t=0.53 off-axis 83 m; OutlineArea x1 (dist 18 m; @220)
  - E `@22` (186, 180) y=138 key=-1 t=0.68 off-axis 187 m; OutlineArea x1 (dist 4 m; @235)
  - F `@116` (142, 346) y=173 key=-1 t=0.75 off-axis 22 m; OutlineArea x1 (dist 7 m; @94)
  - OutlineArea instances: 5 total, 0 farther than 150 m from any flag (none)
- Vehicle spawner pads: 26 total (LightTransport 8, PTV_DirtBike 4, PTV_QuadBike 4, AttackHelicopter 2, AttackPlane 2, FighterPlane 2, IFV 2, Tank 2)
  - near HQ-W: 10 pads (LightTransport 2, PTV_DirtBike 2, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 1, PTV_QuadBike 1, Tank 1); distance median 19 m, max 547 m
  - near HQ-E: 10 pads (LightTransport 2, PTV_DirtBike 2, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 1, PTV_QuadBike 1, Tank 1); distance median 16 m, max 506 m
  - near flag A: 1 pads (LightTransport 1); distance median 8 m, max 8 m
  - near flag B: 1 pads (LightTransport 1); distance median 28 m, max 28 m
  - near flag D: 2 pads (PTV_QuadBike 2); distance median 27 m, max 27 m
  - near flag E: 1 pads (LightTransport 1); distance median 20 m, max 20 m
  - near flag F: 1 pads (LightTransport 1); distance median 46 m, max 46 m
  - Air pads: AttackPlane 2, FighterPlane 2, AttackHelicopter 2
- Forward spawners: none
- Stationary emplacements: none
- Automatic AA: none
- Resupply stations: 7 (Ground 5, Ground_Air 2)
  - by nearest anchor: HQ-W 2 (Ground 1, Ground_Air 1); HQ-E 3 (Ground 2, Ground_Air 1); flag B 1 (Ground 1); flag E 1 (Ground 1)
- SpecialCombatArea: 2 instance(s) (@90,143); containing polygons: @115 POLY40 bbox [-1350.0, -1247.0, 1249.0, 1397.0] (2599 x 2644 m); @211 POLY68 bbox [-220.0, -32.0, 266.0, 408.0] (486 x 440 m)
- Other: TelemetryArea 6; Battle_Pickup 4 (Battle_Pickup 2, Battle_Pickup_Minigun 2); Sector 1 (Sector 1)
  - Battle_Pickup `@69` Minigun (55, 223)
  - Battle_Pickup `@145` GMPF_Battle_Pickup (-42, 85)
  - Battle_Pickup `@205` Minigun (152, 44)
  - Battle_Pickup `@218` GMPF_Battle_Pickup (190, 167)

### Contaminated (MP_CONTAMINATED)

- Layer assets: Conquest, Conquest0, Conquest0_EcsPrefab_ecsPrefab, Conquest0_Schematic, Conquest_Cover, Conquest_GasPlacement, Conquest_GasPlacement_Schematic, Conquest_Global, Conquest_Loot, Conquest_Schematic, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Gas, Conquest_Gas_Telemetry, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Telemetry, generated/AG_Conquest_DynamicDD_Schematic_2E9D5A6C, generated/AG_Conquest_DynamicDD_boxes_7A2324E9, conquest/MeshVariationDb_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry.
- factionOverrides: {}
- GEM counts: {"GEM_Battle_Pickup": 3, "GEM_VehicleSpawner": 24, "GEM_SpecialCombatArea": 1, "GEM_PsyGasZone": 6, "GEM_Insertion": 16, "GEM_StationarySpawner": 11, "GEM_VehicleResupplyStation": 8, "GEM_CapturePoint": 6, "GEM_TelemetryArea": 6, "GEM_Sector": 1, "GEM_HQ": 2, "GEM_CapturePoint_OutlineArea": 10, "GEM_AutomaticAA": 2, "GEM_Collection_Event": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` are not among this map's assets.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@65` pos (-88, -116) y=331 polys=[249, 279]
  - HQ-E `@212` pos (443, 193) y=311 polys=[91, 279]
- HQ-to-HQ distance 615 m. Capture points (6, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@204` (-29, 38) y=323 key=-1 t=0.21 off-axis 103 m; no OutlineArea of its own (6 stacked OutlineAreas @130,138,140,153,173,261 sit at about (-282, -78) y=464, 203 m from HQ-W, not at the flag)
  - B `@228` (117, -26) y=340 key=-1 t=0.36 off-axis 26 m; no OutlineArea
  - C `@277` (146, 101) y=310 key=-1 t=0.51 off-axis 70 m; OutlineArea x2 (dist 3/2 m; @143,215)
  - D `@177` (108, 184) y=307 key=-1 t=0.52 off-axis 160 m; no OutlineArea
  - E `@286` (268, 50) y=334 key=-1 t=0.64 off-axis 36 m; OutlineArea x2 (dist 5/5 m; @127,149)
  - F `@34` (264, 211) y=297 key=-1 t=0.76 off-axis 106 m; no OutlineArea
  - OutlineArea instances: 10 total, 6 farther than 150 m from any flag (@130, @138, @140, @153, @173, @261)
- Vehicle spawner pads: 24 total (LightTransport 6, PTV_DirtBike 6, Tank 4, AttackHelicopter 2, IFV 2, PTV_QuadBike 2, ScoutHelicopter 2)
  - near HQ-W: 10 pads (PTV_DirtBike 3, LightTransport 2, Tank 2, AttackHelicopter 1, IFV 1, ScoutHelicopter 1); distance median 31 m, max 58 m
  - near HQ-E: 10 pads (PTV_DirtBike 3, LightTransport 2, Tank 2, AttackHelicopter 1, IFV 1, ScoutHelicopter 1); distance median 13 m, max 49 m
  - near flag B: 1 pads (LightTransport 1); distance median 25 m, max 25 m
  - near flag D: 2 pads (PTV_QuadBike 2); distance median 26 m, max 27 m
  - near flag E: 1 pads (LightTransport 1); distance median 29 m, max 29 m
  - Air pads: ScoutHelicopter 2, AttackHelicopter 2
- Forward spawners: none
- Stationary emplacements: 11 (AntiTank 5, HMG 5, AntiAircraft 1)
  - by nearest anchor: flag A 2 (AntiTank 1, HMG 1); flag B 2 (AntiTank 1, HMG 1); flag C 1 (HMG 1); flag D 2 (AntiAircraft 1, AntiTank 1); flag E 2 (AntiTank 1, HMG 1); flag F 2 (AntiTank 1, HMG 1)
- Automatic AA: 2 (AutomaticAA 2)
  - by nearest anchor: HQ-W 1 (AutomaticAA 1); HQ-E 1 (AutomaticAA 1)
- Resupply stations: 8 (Ground 6, Ground_Air 2)
  - by nearest anchor: HQ-W 2 (Ground 1, Ground_Air 1); HQ-E 2 (Ground 1, Ground_Air 1); flag A 1 (Ground 1); flag C 1 (Ground 1); flag E 1 (Ground 1); flag F 1 (Ground 1)
- SpecialCombatArea: 1 instance(s) (@16); containing polygons: @43 POLY50 bbox [-200.0, -128.0, 371.0, 315.0] (571 x 443 m); @142 POLY10 bbox [125.0, 79.0, 170.0, 118.0] (45 x 39 m); @279 POLY18 bbox [-346.0, -300.0, 598.0, 544.0] (944 x 844 m)
- Other: TelemetryArea 6; Battle_Pickup 3 (Battle_Pickup_Railgun 2, Battle_Pickup_Minigun 1); Collection_Event 1 (CollectionEvent 1); PsyGasZone 6 (PsyGasZone_Underground 3, PsyGasZone_Outdoors 2, PsyGasZone_Enclosed 1); Sector 1 (Sector 1)
  - Battle_Pickup `@3` Minigun (150, 90)
  - Battle_Pickup `@42` Railgun (257, 201)
  - Battle_Pickup `@145` Railgun (-48, 42)
  - PsyGasZone `@17` Outdoors (110, 190)
  - PsyGasZone `@41` Outdoors (262, 217)
  - PsyGasZone `@84` Enclosed (-32, 44)
  - PsyGasZone `@160` Underground (262, 54)
  - PsyGasZone `@262` Underground (111, -34)
  - PsyGasZone `@264` Underground (145, 104)

### Area 51 (MP_DRYLAKE)

- Layer assets: Conquest, Conquest0, Conquest0_Schematic, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, Conquest0_EcsPrefab_ecsPrefab, generated/AG_Conquest_DynamicDD_Schematic_2E9D5A6C, generated/AG_Conquest_DynamicDD_boxes_7A2324E9, conquest/MeshVariationDb_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry.
- factionOverrides: {}
- GEM counts: {"GEM_SpecialCombatArea": 2, "GEM_Insertion": 16, "GEM_VehicleSpawner": 61, "GEM_CapturePoint": 9, "GEM_VehicleResupplyStation": 4, "GEM_HQ": 2, "GEM_StationarySpawner": 4, "GEM_AutomaticAA": 2, "GEM_CapturePoint_Proxy": 1, "GEM_Sector": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@28` pos (-522, 877) y=63 polys=[184, 190]
  - HQ-E `@123` pos (1010, 771) y=104 polys=[112, 190]
- HQ-to-HQ distance 1536 m. Capture points (9, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@111` (-62, 912) y=93 key=-1 t=0.30 off-axis 67 m; no OutlineArea
  - B `@186` (-2, 1154) y=68 key=-1 t=0.33 off-axis 312 m; no OutlineArea
  - C `@194` (176, 1020) y=48 key=-1 t=0.45 off-axis 191 m; no OutlineArea
  - D `@64` (225, 1164) y=120 key=-1 t=0.47 off-axis 338 m; no OutlineArea
  - E `@11` (218, 819) y=103 key=-1 t=0.48 off-axis 6 m; no OutlineArea
  - F `@99` (232, 923) y=72 key=-1 t=0.49 off-axis 98 m; no OutlineArea
  - G `@50` (295, 1046) y=47 key=-1 t=0.52 off-axis 225 m; no OutlineArea
  - H `@22` (433, 1168) y=59 key=-1 t=0.61 off-axis 356 m; no OutlineArea
  - I `@162` (540, 982) y=59 key=-1 t=0.69 off-axis 178 m; no OutlineArea
  - CapturePoint_Proxy `@145` (225, 1146) (GMPF_CapturePoint_Proxy); nearest flag at 18 m
- Vehicle spawner pads: 61 total (LightTransport 17, PTV_QuadBike 17, PTV_DirtBike 6, AttackPlane 4, Tank 4, AttackHelicopter 3, APC 2, FighterPlane 2, IFV 2, MobileAA 2, TransportHelicopter 2)
  - near HQ-W: 16 pads (LightTransport 3, AttackPlane 2, PTV_DirtBike 2, PTV_QuadBike 2, APC 1, AttackHelicopter 1, FighterPlane 1, IFV 1, MobileAA 1, Tank 1, TransportHelicopter 1); distance median 37 m, max 837 m
  - near HQ-E: 16 pads (LightTransport 3, AttackPlane 2, PTV_DirtBike 2, PTV_QuadBike 2, APC 1, AttackHelicopter 1, FighterPlane 1, IFV 1, MobileAA 1, Tank 1, TransportHelicopter 1); distance median 38 m, max 844 m
  - near flag A: 2 pads (LightTransport 1, PTV_QuadBike 1); distance median 17 m, max 29 m
  - near flag B: 3 pads (LightTransport 1, PTV_QuadBike 1, Tank 1); distance median 36 m, max 64 m
  - near flag C: 1 pads (PTV_QuadBike 1); distance median 16 m, max 16 m
  - near flag D: 8 pads (LightTransport 4, PTV_QuadBike 4); distance median 33 m, max 36 m
  - near flag E: 6 pads (PTV_DirtBike 2, PTV_QuadBike 2, AttackHelicopter 1, LightTransport 1); distance median 24 m, max 76 m
  - near flag F: 3 pads (LightTransport 2, PTV_QuadBike 1); distance median 10 m, max 135 m
  - near flag G: 1 pads (PTV_QuadBike 1); distance median 19 m, max 19 m
  - near flag H: 3 pads (LightTransport 1, PTV_QuadBike 1, Tank 1); distance median 26 m, max 46 m
  - near flag I: 2 pads (LightTransport 1, PTV_QuadBike 1); distance median 38 m, max 40 m
  - Air pads: AttackPlane 4, AttackHelicopter 3, TransportHelicopter 2, FighterPlane 2
- Forward spawners: none
- Stationary emplacements: 4 (AntiAircraft 2, HMG 2)
  - by nearest anchor: flag B 2 (HMG 2); flag E 2 (AntiAircraft 2)
- Automatic AA: 2 (AutomaticAA 2)
  - by nearest anchor: HQ-W 1 (AutomaticAA 1); HQ-E 1 (AutomaticAA 1)
- Resupply stations: 4 (Ground 4)
  - by nearest anchor: HQ-W 1 (Ground 1); HQ-E 1 (Ground 1); flag D 1 (Ground 1); flag F 1 (Ground 1)
- SpecialCombatArea: 2 instance(s) (@2,205); containing polygons: @190 POLY6 bbox [-1524.0, -902.0, 2114.0, 2399.0] (3638 x 3301 m); @203 POLY32 bbox [-355.0, 722.0, 888.0, 1314.0] (1243 x 592 m)
- Other: TelemetryArea 0; Sector 1 (Sector 1)

### Manhattan Bridge (MP_DUMBO)

- Layer assets: Conquest, Conquest0, Conquest0_EcsPrefab_ecsPrefab, Conquest0_Schematic, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, Conquest_VFX, Conquest_VFX_Schematic, conquest/MeshVariationDb_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry, MeshVariationDb_Win32, staticmodelgroup.physics.
- factionOverrides: {}
- GEM counts: {"GEM_SpecialCombatArea": 1, "GEM_HQ": 2, "GEM_VehicleSpawner": 14, "GEM_CapturePoint": 5, "GEM_VehicleResupplyStation": 4, "GEM_TelemetryArea": 7, "GEM_Insertion": 16, "GEM_Battle_Pickup": 2, "GEM_CapturePoint_OutlineArea": 2, "GEM_StationarySpawner": 2, "GEM_Sector": 1, "GEM_Collection_Event": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@99` pos (-262, -442) y=52 polys=[5, 45]
  - HQ-E `@3` pos (179, -243) y=57 polys=[45, 104]
- HQ-to-HQ distance 484 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@183` (-148, -352) y=54 key=-1 t=0.29 off-axis 35 m; no OutlineArea
  - B `@127` (-28, -450) y=80 key=-1 t=0.44 off-axis 104 m; no OutlineArea
  - C `@32` (-41, -345) y=55 key=-1 t=0.50 off-axis 2 m; no OutlineArea
  - D `@170` (-38, -243) y=56 key=-1 t=0.59 off-axis 89 m; OutlineArea x2 (dist 10/8 m; @91,240)
  - E `@122` (82, -346) y=55 key=-1 t=0.73 off-axis 53 m; no OutlineArea
  - OutlineArea instances: 2 total, 0 farther than 150 m from any flag (none)
- Vehicle spawner pads: 14 total (LightTransport 6, IFV 2, PTV_QuadBike 2, ScoutHelicopter 2, Tank 2)
  - near HQ-W: 6 pads (LightTransport 3, IFV 1, ScoutHelicopter 1, Tank 1); distance median 19 m, max 32 m
  - near HQ-E: 6 pads (LightTransport 3, IFV 1, ScoutHelicopter 1, Tank 1); distance median 16 m, max 26 m
  - near flag A: 1 pads (PTV_QuadBike 1); distance median 7 m, max 7 m
  - near flag E: 1 pads (PTV_QuadBike 1); distance median 11 m, max 11 m
  - Air pads: ScoutHelicopter 2
- Forward spawners: none
- Stationary emplacements: 2 (AntiTank 2)
  - by nearest anchor: flag A 1 (AntiTank 1); flag E 1 (AntiTank 1)
- Automatic AA: none
- Resupply stations: 4 (Ground 2, Ground_Air 2)
  - by nearest anchor: HQ-W 2 (Ground 1, Ground_Air 1); HQ-E 2 (Ground 1, Ground_Air 1)
- SpecialCombatArea: 1 instance(s) (@1); containing polygons: @45 POLY15 bbox [-435.0, -704.0, 328.0, -20.0] (763 x 684 m); @115 POLY53 bbox [-260.0, -537.0, 151.0, -165.0] (411 x 372 m); @243 POLY22 bbox [-56.0, -358.0, -27.0, -332.0] (29 x 26 m); @285 POLY28 bbox [-74.0, -374.0, -6.0, -304.0] (68 x 70 m)
- Other: TelemetryArea 7; Battle_Pickup 2 (Battle_Pickup_Minigun 2); Collection_Event 1 (CollectionEvent 1); Sector 1 (Sector 1)
  - Battle_Pickup `@87` Minigun (-13, -295)
  - Battle_Pickup `@247` Minigun (-50, -383)

### Eastwood (MP_EASTWOOD)

- Layer assets: Conquest, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, generated/DD_Conquest0_Schematics, generated/DD_Conquest0_Volumes, conquest/MeshVariationDb_Win32, conquest/staticmodelgroup.physics, conquest_networkregistry_Win32, conquest_templatedescriptorregistry, Game/GlacierMP/Levels/MP_Eastwood/_Layers_Gameplay/Conquest0.
- factionOverrides: {"team1": "Alliance/NATO", "team2": "Coalition/Pax Armata"}
- GEM counts: {"GEM_Insertion": 16, "GEM_VehicleSpawner": 34, "GEM_HQ": 2, "GEM_StationarySpawner": 7, "GEM_SpecialCombatArea": 1, "GEM_TelemetryArea": 5, "GEM_VehicleResupplyStation": 5, "GEM_Sector": 1, "GEM_CapturePoint": 5, "GEM_Battle_Pickup": 2, "GEM_Collection_Event": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@142` pos (-400, 120) y=226 polys=[123, 130]
  - HQ-E `@16` pos (378, -160) y=242 polys=[123, 192]
- HQ-to-HQ distance 827 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@200` (-180, 13) y=233 key=-1 t=0.29 off-axis 26 m; no OutlineArea
  - B `@65` (-101, 169) y=234 key=-1 t=0.32 off-axis 148 m; no OutlineArea
  - C `@179` (70, 22) y=234 key=-1 t=0.57 off-axis 67 m; no OutlineArea
  - D `@171` (192, -170) y=240 key=-1 t=0.79 off-axis 72 m; no OutlineArea
  - E `@168` (271, 10) y=232 key=-1 t=0.81 off-axis 124 m; no OutlineArea
- Vehicle spawner pads: 34 total (PTV_GolfCart 10, LightTransport 8, APC 4, Tank 4, AttackHelicopter 2, IFV 2, MobileAA 2, TransportHelicopter 2)
  - near HQ-W: 10 pads (APC 2, LightTransport 2, Tank 2, AttackHelicopter 1, IFV 1, MobileAA 1, TransportHelicopter 1); distance median 19 m, max 41 m
  - near HQ-E: 10 pads (APC 2, LightTransport 2, Tank 2, AttackHelicopter 1, IFV 1, MobileAA 1, TransportHelicopter 1); distance median 13 m, max 46 m
  - near flag A: 1 pads (LightTransport 1); distance median 33 m, max 33 m
  - near flag B: 4 pads (PTV_GolfCart 3, LightTransport 1); distance median 99 m, max 144 m
  - near flag C: 5 pads (PTV_GolfCart 5); distance median 100 m, max 137 m
  - near flag D: 1 pads (LightTransport 1); distance median 39 m, max 39 m
  - near flag E: 3 pads (PTV_GolfCart 2, LightTransport 1); distance median 38 m, max 63 m
  - Air pads: AttackHelicopter 2, TransportHelicopter 2
- Forward spawners: none
- Stationary emplacements: 7 (AntiTank 4, HMG 2, AntiAircraft 1)
  - by nearest anchor: flag B 1 (AntiTank 1); flag C 3 (HMG 2, AntiTank 1); flag D 1 (AntiTank 1); flag E 2 (AntiAircraft 1, AntiTank 1)
- Automatic AA: none
- Resupply stations: 5 (Ground 3, Ground_Air 2)
  - by nearest anchor: HQ-W 2 (Ground 1, Ground_Air 1); HQ-E 2 (Ground 1, Ground_Air 1); flag C 1 (Ground 1)
- SpecialCombatArea: 1 instance(s) (@24); containing polygons: @123 POLY28 bbox [-660.0, -442.0, 689.0, 536.0] (1349 x 978 m)
- Other: TelemetryArea 5; Battle_Pickup 2 (Battle_Pickup_Minigun 2); Collection_Event 1 (CollectionEvent 1); Sector 1 (Sector 1)
  - Battle_Pickup `@117` Minigun (-45, 94)
  - Battle_Pickup `@202` Minigun (149, -81)

### Operation Firestorm (MP_FIRESTORM)

- Layer assets: Conquest, Conquest0, Conquest0_Schematic, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, conquest/MeshVariationDb_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry.
- factionOverrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- GEM counts: {"GEM_CapturePoint_OutlineArea": 17, "GEM_CapturePoint": 5, "GEM_VehicleSpawner": 37, "GEM_TelemetryArea": 5, "GEM_Insertion": 16, "GEM_HQ": 2, "GEM_VehicleResupplyStation": 7, "GEM_Sector": 1, "GEM_SpecialCombatArea": 1, "GEM_VehicleSpawner_Forward": 6, "GEM_Collection_Event": 1, "GEM_Battle_Pickup": 2}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@90` pos (-479, 51) y=136 polys=[29, 199]
  - HQ-E `@42` pos (343, -119) y=113 polys=[199, 235]
- HQ-to-HQ distance 839 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@28` (-285, -83) y=134 key=-1 t=0.26 off-axis 92 m; OutlineArea x3 (dist 34/28/6 m; @26,143,175)
  - B `@4` (-194, 50) y=126 key=-1 t=0.33 off-axis 57 m; OutlineArea x7 (dist 25/29/27/27/24/29/28 m; @3,49,165,178,206,234,237)
  - C `@47` (-88, -122) y=124 key=-1 t=0.50 off-axis 90 m; no OutlineArea
  - D `@249` (70, -111) y=121 key=-1 t=0.68 off-axis 47 m; OutlineArea x7 (dist 37/36/36/30/20/24/32 m; @9,78,100,109,127,226,253)
  - E `@25` (130, 75) y=122 key=-1 t=0.70 off-axis 147 m; no OutlineArea
  - OutlineArea instances: 17 total, 0 farther than 150 m from any flag (none)
- Vehicle spawner pads: 37 total (LightTransport 11, Tank 8, PTV_DirtBike 4, AttackHelicopter 2, AttackPlane 2, FighterPlane 2, IFV 2, MobileAA 2, ScoutHelicopter 2, TransportHelicopter 2)
  - near HQ-W: 15 pads (LightTransport 3, Tank 3, PTV_DirtBike 2, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 1, MobileAA 1, ScoutHelicopter 1, TransportHelicopter 1); distance median 43 m, max 378 m
  - near HQ-E: 15 pads (LightTransport 3, Tank 3, PTV_DirtBike 2, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 1, MobileAA 1, ScoutHelicopter 1, TransportHelicopter 1); distance median 43 m, max 332 m
  - near flag A: 1 pads (LightTransport 1); distance median 19 m, max 19 m
  - near flag B: 2 pads (LightTransport 1, Tank 1); distance median 50 m, max 78 m
  - near flag C: 1 pads (LightTransport 1); distance median 8 m, max 8 m
  - near flag D: 1 pads (LightTransport 1); distance median 42 m, max 42 m
  - near flag E: 2 pads (LightTransport 1, Tank 1); distance median 50 m, max 69 m
  - Air pads: ScoutHelicopter 2, AttackPlane 2, TransportHelicopter 2, FighterPlane 2, AttackHelicopter 2
- Forward spawners: 6 (VehicleSpawner_Forward 6)
  - by nearest anchor: HQ-W 3 (VehicleSpawner_Forward 3); HQ-E 3 (VehicleSpawner_Forward 3)
- Stationary emplacements: none
- Automatic AA: none
- Resupply stations: 7 (Ground 5, Ground_Air 2)
  - by nearest anchor: HQ-W 2 (Ground 1, Ground_Air 1); HQ-E 2 (Ground 1, Ground_Air 1); flag B 1 (Ground 1); flag C 1 (Ground 1); flag E 1 (Ground 1)
- SpecialCombatArea: 1 instance(s) (@56); containing polygons: @199 POLY12 bbox [-2079.0, -1681.0, 1678.0, 1773.0] (3757 x 3454 m)
- Other: TelemetryArea 5; Battle_Pickup 2 (Battle_Pickup_Minigun 2); Collection_Event 1 (CollectionEvent 1); Sector 1 (Sector 1)
  - Battle_Pickup `@149` Minigun (-150, -66)
  - Battle_Pickup `@220` Minigun (-9, -91)

### Railway to Golmud (MP_GOLMUDRAILWAY)

- Layer assets: Cables/CableSet_8dfa23a4-a6ff-49a1-8408-6054ee2bb491_fc8c1d4c-37cc-4ce3-9a7d-65bf40b2761c, Conquest, Conquest0_Cables1, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global_Cables, Conquest_Global_Cables_Cables, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, Conquest0_EcsPrefab_2_ecsPrefab, generated/AG_Conquest_DynamicDD_Schematic_2E9D5A6C, generated/AG_Conquest_DynamicDD_boxes_7A2324E9, Conquest0, Conquest0_Schematic, Conquest_Global, cables/cableset_8dfa23a4-a6ff-49a1-8408-6054ee2bb491_fc8c1d4c-37cc-4ce3-9a7d-65bf40b2761c_mesh, conquest/MeshVariationDb_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry, MeshVariationDb_Win32, staticmodelgroup.physics.
- factionOverrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- GEM counts: {"GEM_VehicleSpawner": 61, "GEM_Insertion": 16, "GEM_VehicleResupplyStation": 11, "GEM_Battle_Pickup": 7, "GEM_CapturePoint_OutlineArea": 1, "GEM_StationarySpawner": 18, "GEM_CapturePoint": 7, "GEM_Collection_Event": 1, "GEM_AutomaticAA": 2, "GEM_TelemetryArea": 7, "GEM_Sector": 1, "GEM_HQ": 2, "GEM_SpecialCombatArea": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@168` pos (-848, 733) y=698 polys=[82, 157]
  - HQ-E `@172` pos (590, 623) y=694 polys=[66, 82]
- HQ-to-HQ distance 1443 m. Capture points (7, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@225` (-489, 362) y=690 key=-1 t=0.27 off-axis 343 m; no OutlineArea
  - B `@43` (-172, 907) y=743 key=-1 t=0.46 off-axis 225 m; no OutlineArea
  - C `@277` (-137, 689) y=730 key=-1 t=0.49 off-axis 10 m; no OutlineArea
  - D `@139` (-115, 562) y=704 key=-1 t=0.52 off-axis 114 m; no OutlineArea
  - E `@289` (-117, 250) y=686 key=-1 t=0.53 off-axis 426 m; no OutlineArea
  - F `@71` (-67, 851) y=738 key=-1 t=0.53 off-axis 178 m; OutlineArea x1 (dist 23 m; @26)
  - G `@171` (278, 376) y=678 key=-1 t=0.80 off-axis 270 m; no OutlineArea
  - OutlineArea instances: 1 total, 0 farther than 150 m from any flag (none)
- Vehicle spawner pads: 61 total (PTV_DirtBike 17, LightTransport 11, Tank 7, IFV 5, PTV_QuadBike 4, MobileAA 3, ScoutHelicopter 3, APC 2, AttackHelicopter 2, AttackPlane 2, FighterPlane 2, TransportHelicopter 2, PTV_GolfCart 1)
  - near HQ-W: 21 pads (PTV_DirtBike 4, LightTransport 3, Tank 3, IFV 2, PTV_QuadBike 2, APC 1, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, MobileAA 1, ScoutHelicopter 1, TransportHelicopter 1); distance median 80 m, max 1188 m
  - near HQ-E: 21 pads (PTV_DirtBike 4, LightTransport 3, Tank 3, IFV 2, PTV_QuadBike 2, APC 1, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, MobileAA 1, ScoutHelicopter 1, TransportHelicopter 1); distance median 72 m, max 1136 m
  - near flag A: 4 pads (PTV_DirtBike 2, IFV 1, LightTransport 1); distance median 25 m, max 127 m
  - near flag B: 2 pads (PTV_DirtBike 1, PTV_GolfCart 1); distance median 81 m, max 123 m
  - near flag C: 3 pads (LightTransport 1, PTV_DirtBike 1, ScoutHelicopter 1); distance median 21 m, max 34 m
  - near flag E: 4 pads (PTV_DirtBike 2, LightTransport 1, MobileAA 1); distance median 31 m, max 47 m
  - near flag F: 2 pads (LightTransport 1, PTV_DirtBike 1); distance median 18 m, max 26 m
  - near flag G: 4 pads (PTV_DirtBike 2, LightTransport 1, Tank 1); distance median 26 m, max 203 m
  - Air pads: TransportHelicopter 2, ScoutHelicopter 3, AttackHelicopter 2, FighterPlane 2, AttackPlane 2
- Forward spawners: none
- Stationary emplacements: 18 (AntiTank 9, HMG 7, AntiAircraft 2)
  - by nearest anchor: flag A 1 (AntiTank 1); flag B 5 (AntiTank 2, HMG 2, AntiAircraft 1); flag C 1 (AntiTank 1); flag D 4 (HMG 2, AntiAircraft 1, AntiTank 1); flag E 4 (AntiTank 2, HMG 2); flag F 2 (AntiTank 1, HMG 1); flag G 1 (AntiTank 1)
- Automatic AA: 2 (AutomaticAA 2)
  - by nearest anchor: HQ-W 1 (AutomaticAA 1); HQ-E 1 (AutomaticAA 1)
- Resupply stations: 11 (Ground 9, Ground_Air 2)
  - by nearest anchor: HQ-W 2 (Ground 1, Ground_Air 1); HQ-E 2 (Ground 1, Ground_Air 1); flag A 2 (Ground 2); flag C 1 (Ground 1); flag E 1 (Ground 1); flag F 1 (Ground 1); flag G 2 (Ground 2)
- SpecialCombatArea: 1 instance(s) (@255); containing polygons: @82 POLY18 bbox [-3076.0, -1879.0, 2209.0, 2735.0] (5285 x 4614 m); @178 POLY58 bbox [-734.0, 1.0, 538.0, 1166.0] (1272 x 1165 m)
- Other: TelemetryArea 7; Battle_Pickup 7 (Battle_Pickup_ArtilleryStrike 5, Battle_Pickup_SmokeScreen 2); Collection_Event 1 (CollectionEvent 1); Sector 1 (Sector 1)
  - Battle_Pickup `@11` ArtilleryStrike (-32, 672)
  - Battle_Pickup `@15` SmokeScreen (-71, 1058)
  - Battle_Pickup `@123` SmokeScreen (-84, 172)
  - Battle_Pickup `@167` ArtilleryStrike (-410, 348)
  - Battle_Pickup `@257` ArtilleryStrike (227, 346)
  - Battle_Pickup `@283` ArtilleryStrike (-86, 393)
  - Battle_Pickup `@284` ArtilleryStrike (-289, 879)

### Tsuru Reef (MP_ISOLATED)

- Layer assets: Conquest, Conquest0, Conquest0_Schematic, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, Conquest0_EcsPrefab_ecsPrefab, generated/AG_Conquest_DynamicDD_Schematic_2E9D5A6C, generated/AG_Conquest_DynamicDD_boxes_7A2324E9, conquest/MeshVariationDb_Win32, conquest/staticmodelgroup.physics, conquest_networkregistry_Win32, conquest_templatedescriptorregistry.
- factionOverrides: {"team1": "Coalition/Pax Armata", "team2": "Alliance/NATO"}
- GEM counts: {"GEM_AutomaticAA": 2, "GEM_VehicleSpawner": 40, "GEM_Insertion": 16, "GEM_VehicleResupplyStation": 4, "GEM_CapturePoint": 9, "GEM_CapturePoint_OutlineArea": 8, "GEM_TelemetryArea": 9, "GEM_HQ": 2, "GEM_Sector": 1, "GEM_Collection_Event": 1, "GEM_StationarySpawner": 3, "GEM_SpecialCombatArea": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@164` pos (-1156, 843) y=102 polys=[71, 201]
  - HQ-E `@91` pos (-430, -680) y=108 polys=[71, 124]
- HQ-to-HQ distance 1687 m. Capture points (9, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@139` (-876, 522) y=102 key=-1 t=0.24 off-axis 114 m; OutlineArea x1 (dist 18 m; @147)
  - B `@169` (-928, 328) y=101 key=-1 t=0.33 off-axis 16 m; OutlineArea x1 (dist 16 m; @223)
  - C `@27` (-643, 431) y=109 key=-1 t=0.35 off-axis 285 m; OutlineArea x1 (dist 5 m; @242)
  - D `@158` (-814, 212) y=118 key=-1 t=0.43 off-axis 37 m; OutlineArea x1 (dist 4 m; @144)
  - E `@19` (-1054, -10) y=111 key=-1 t=0.48 off-axis 276 m; no OutlineArea
  - F `@69` (-815, -8) y=108 key=-1 t=0.54 off-axis 58 m; OutlineArea x1 (dist 24 m; @87)
  - G `@173` (-877, -264) y=106 key=-1 t=0.66 off-axis 225 m; OutlineArea x1 (dist 14 m; @168)
  - H `@183` (-609, -185) y=104 key=-1 t=0.69 off-axis 52 m; OutlineArea x1 (dist 3 m; @20)
  - I `@162` (-659, -311) y=102 key=-1 t=0.74 off-axis 48 m; OutlineArea x1 (dist 25 m; @198)
  - OutlineArea instances: 8 total, 0 farther than 150 m from any flag (none)
- Vehicle spawner pads: 40 total (RHIB 10, PTV_QuadBike 6, PTV_DirtBike 4, PatrolBoat 4, TransportHelicopter 4, APC 3, AttackPlane 2, FighterPlane 2, IFV 2, LightTransport 2, ScoutHelicopter 1)
  - near HQ-W: 10 pads (RHIB 4, PatrolBoat 2, TransportHelicopter 2, AttackPlane 1, FighterPlane 1); distance median 50 m, max 289 m
  - near HQ-E: 10 pads (RHIB 4, PatrolBoat 2, TransportHelicopter 2, AttackPlane 1, FighterPlane 1); distance median 68 m, max 438 m
  - near flag A: 2 pads (APC 1, PTV_DirtBike 1); distance median 23 m, max 30 m
  - near flag B: 1 pads (RHIB 1); distance median 34 m, max 34 m
  - near flag C: 3 pads (IFV 1, PTV_DirtBike 1, PTV_QuadBike 1); distance median 43 m, max 63 m
  - near flag D: 4 pads (PTV_QuadBike 3, APC 1); distance median 74 m, max 146 m
  - near flag E: 2 pads (PTV_QuadBike 1, ScoutHelicopter 1); distance median 51 m, max 60 m
  - near flag F: 3 pads (APC 1, PTV_DirtBike 1, PTV_QuadBike 1); distance median 83 m, max 93 m
  - near flag G: 1 pads (RHIB 1); distance median 35 m, max 35 m
  - near flag H: 3 pads (IFV 1, LightTransport 1, PTV_DirtBike 1); distance median 35 m, max 37 m
  - near flag I: 1 pads (LightTransport 1); distance median 33 m, max 33 m
  - Air pads: ScoutHelicopter 1, TransportHelicopter 4, AttackPlane 2, FighterPlane 2
- Forward spawners: none
- Stationary emplacements: 3 (AntiTank 2, HMG 1)
  - by nearest anchor: flag A 1 (AntiTank 1); flag D 1 (HMG 1); flag F 1 (AntiTank 1)
- Automatic AA: 2 (AutomaticAA 2)
  - by nearest anchor: HQ-W 1 (AutomaticAA 1); HQ-E 1 (AutomaticAA 1)
- Resupply stations: 4 (Ground 2, Ground_Air 2)
  - by nearest anchor: HQ-W 1 (Ground_Air 1); HQ-E 1 (Ground_Air 1); flag A 1 (Ground 1); flag F 1 (Ground 1)
- SpecialCombatArea: 1 instance(s) (@148); containing polygons: @38 POLY50 bbox [-1740.0, -897.0, 241.0, 895.0] (1981 x 1792 m); @71 POLY33 bbox [-2357.0, -1632.0, 923.0, 1921.0] (3280 x 3553 m)
- Other: TelemetryArea 9; Collection_Event 1 (CollectionEvent 1); Sector 1 (Sector 1)

### New Sobek City (MP_OUTSKIRTS)

- Layer assets: Cables/CableSet_63201709-5f96-4476-9f1e-74575bb47cf8_2ae6bc18-91e2-4560-a4bf-33a4688184e6, Cables/CableSet_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_4b721a03-fb66-497a-934c-333ffef20963, Cables/CableSet_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_4b721a03-fb66-497a-934c-333ffef20963.physics, Cables/CableSet_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_56989015-1ac3-4ec0-a0b6-41aa60cc450f, Cables/CableSet_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_56989015-1ac3-4ec0-a0b6-41aa60cc450f.physics, Cables/CableSet_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_9ff2f974-8a5a-4d6d-91cf-a15156b64ccf, Cables/CableSet_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_9ff2f974-8a5a-4d6d-91cf-a15156b64ccf.physics, Cables/CableSet_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_fabdf38f-af6e-4431-9c8a-338cca2385a9, Cables/CableSet_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_fabdf38f-af6e-4431-9c8a-338cca2385a9.physics, Conquest, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_Cables, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, generated/DD_Conquest0_Schematics, generated/DD_Conquest0_Volumes, Conquest0, Conquest0_Schematic, cables/cableset_63201709-5f96-4476-9f1e-74575bb47cf8_2ae6bc18-91e2-4560-a4bf-33a4688184e6_mesh, cables/cableset_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_4b721a03-fb66-497a-934c-333ffef20963_mesh, cables/cableset_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_56989015-1ac3-4ec0-a0b6-41aa60cc450f_mesh, cables/cableset_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_9ff2f974-8a5a-4d6d-91cf-a15156b64ccf_mesh, cables/cableset_c9975dce-f8db-4a8e-b5e8-d8ea11e0f2d2_fabdf38f-af6e-4431-9c8a-338cca2385a9_mesh, conquest/MeshVariationDb_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry, MeshVariationDb_Win32, staticmodelgroup.physics.
- factionOverrides: {}
- GEM counts: {"GEM_Insertion": 16, "GEM_Sector": 1, "GEM_StationarySpawner": 9, "GEM_VehicleSpawner": 21, "GEM_TelemetryArea": 7, "GEM_CapturePoint_OutlineArea": 4, "GEM_SpecialCombatArea": 1, "GEM_CapturePoint": 5, "GEM_VehicleResupplyStation": 4, "GEM_Battle_Pickup": 2, "GEM_HQ": 2}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@164` pos (-177, 0) y=93 polys=[6, 37, 75]
  - HQ-E `@153` pos (197, 12) y=90 polys=[37, 166]
- HQ-to-HQ distance 374 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@120` (-144, -162) y=92 key=-1 t=0.07 off-axis 163 m; no OutlineArea
  - B `@177` (-44, -56) y=96 key=-1 t=0.35 off-axis 60 m; OutlineArea x2 (dist 8/9 m; @122,129)
  - C `@161` (22, -151) y=93 key=-1 t=0.52 off-axis 157 m; no OutlineArea
  - D `@71` (62, -52) y=98 key=-1 t=0.63 off-axis 60 m; OutlineArea x2 (dist 8/4 m; @34,36)
  - E `@85` (148, -146) y=91 key=-1 t=0.86 off-axis 156 m; no OutlineArea
  - OutlineArea instances: 4 total, 0 farther than 150 m from any flag (none)
- Vehicle spawner pads: 21 total (LightTransport 7, AttackHelicopter 2, IFV 2, MobileAA 2, PTV_DirtBike 2, ScoutHelicopter 2, Tank 2, TransportHelicopter 2)
  - near HQ-W: 9 pads (LightTransport 2, AttackHelicopter 1, IFV 1, MobileAA 1, PTV_DirtBike 1, ScoutHelicopter 1, Tank 1, TransportHelicopter 1); distance median 19 m, max 32 m
  - near HQ-E: 9 pads (LightTransport 2, AttackHelicopter 1, IFV 1, MobileAA 1, PTV_DirtBike 1, ScoutHelicopter 1, Tank 1, TransportHelicopter 1); distance median 14 m, max 35 m
  - near flag A: 3 pads (LightTransport 3); distance median 37 m, max 40 m
  - Air pads: ScoutHelicopter 2, TransportHelicopter 2, AttackHelicopter 2
- Forward spawners: none
- Stationary emplacements: 9 (AntiTank 4, HMG 4, AntiAircraft 1)
  - by nearest anchor: flag A 2 (HMG 2); flag B 2 (AntiAircraft 1, AntiTank 1); flag C 1 (AntiTank 1); flag D 2 (AntiTank 1, HMG 1); flag E 2 (AntiTank 1, HMG 1)
- Automatic AA: none
- Resupply stations: 4 (Ground 4)
  - by nearest anchor: HQ-W 1 (Ground 1); HQ-E 1 (Ground 1); flag B 1 (Ground 1); flag D 1 (Ground 1)
- SpecialCombatArea: 1 instance(s) (@39); containing polygons: @37 POLY16 bbox [-453.0, -539.0, 431.0, 248.0] (884 x 787 m); @110 POLY79 bbox [-244.0, -222.0, 225.0, 8.0] (469 x 230 m)
- Other: TelemetryArea 7; Battle_Pickup 2 (Battle_Pickup_Minigun 1, Battle_Pickup_Railgun 1); Sector 1 (Sector 1)
  - Battle_Pickup `@106` Minigun (-72, -75)
  - Battle_Pickup `@155` Railgun (-14, -197)

### Vegas Strip (MP_PARADISE)

- Layer assets: Conquest, Conquest0, Conquest0_Schematic, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, generated/AG_Conquest_DynamicDD_Schematic_2E9D5A6C, generated/AG_Conquest_DynamicDD_boxes_7A2324E9, conquest/MeshVariationDb_Win32, conquest/staticmodelgroup.physics, conquest_networkregistry_Win32, conquest_templatedescriptorregistry.
- factionOverrides: {}
- GEM counts: {"GEM_VehicleSpawner": 34, "GEM_VehicleResupplyStation": 2, "GEM_Insertion": 16, "GEM_AutomaticAA": 2, "GEM_HQ": 2, "GEM_CapturePoint": 5, "GEM_StationarySpawner": 3, "GEM_Sector": 1, "GEM_SpecialCombatArea": 2}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@172` pos (-148, 471) y=50 polys=[24, 147]
  - HQ-E `@32` pos (114, -136) y=50 polys=[71, 147]
- HQ-to-HQ distance 661 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@106` (-66, 267) y=56 key=-1 t=0.33 off-axis 6 m; no OutlineArea
  - B `@113` (-192, 160) y=53 key=-1 t=0.41 off-axis 164 m; no OutlineArea
  - C `@61` (-98, 112) y=45 key=-1 t=0.53 off-axis 96 m; no OutlineArea
  - D `@126` (12, 115) y=52 key=-1 t=0.59 off-axis 6 m; no OutlineArea
  - E `@55` (-104, -24) y=59 key=-1 t=0.71 off-axis 155 m; no OutlineArea
- Vehicle spawner pads: 34 total (LightTransport 12, PTV_DirtBike 7, PTV_QuadBike 5, APC 2, IFV 2, MobileAA 2, TransportHelicopter 2, AttackHelicopter 1, PTV_GolfCart 1)
  - near HQ-W: 11 pads (LightTransport 4, PTV_DirtBike 2, APC 1, IFV 1, MobileAA 1, PTV_QuadBike 1, TransportHelicopter 1); distance median 19 m, max 60 m
  - near HQ-E: 11 pads (LightTransport 4, PTV_DirtBike 2, APC 1, IFV 1, MobileAA 1, PTV_QuadBike 1, TransportHelicopter 1); distance median 18 m, max 73 m
  - near flag A: 3 pads (LightTransport 1, PTV_DirtBike 1, PTV_QuadBike 1); distance median 52 m, max 57 m
  - near flag B: 5 pads (AttackHelicopter 1, LightTransport 1, PTV_DirtBike 1, PTV_GolfCart 1, PTV_QuadBike 1); distance median 48 m, max 119 m
  - near flag D: 2 pads (LightTransport 2); distance median 50 m, max 51 m
  - near flag E: 2 pads (PTV_DirtBike 1, PTV_QuadBike 1); distance median 46 m, max 49 m
  - Air pads: AttackHelicopter 1, TransportHelicopter 2
- Forward spawners: none
- Stationary emplacements: 3 (HMG 2, AntiAircraft 1)
  - by nearest anchor: flag B 1 (AntiAircraft 1); flag D 1 (HMG 1); flag E 1 (HMG 1)
- Automatic AA: 2 (AutomaticAA 2)
  - by nearest anchor: HQ-W 1 (AutomaticAA 1); HQ-E 1 (AutomaticAA 1)
- Resupply stations: 2 (Ground 2)
  - by nearest anchor: HQ-W 1 (Ground 1); HQ-E 1 (Ground 1)
- SpecialCombatArea: 2 instance(s) (@114,173); containing polygons: @145 POLY53 bbox [-299.0, -123.0, 107.0, 353.0] (406 x 476 m); @147 POLY15 bbox [-518.0, -349.0, 313.0, 617.0] (831 x 966 m)
- Other: TelemetryArea 0; Sector 1 (Sector 1)

### Cairo Bazaar (MP_PLAZA)

- Layer assets: Conquest, Conquest0, Conquest0_Schematic, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, generated/AG_Conquest_DynamicDD_Schematic_2E9D5A6C, generated/AG_Conquest_DynamicDD_boxes_7A2324E9, conquest/MeshVariationDb_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry.
- factionOverrides: {"team1": "Alliance/NATO", "team2": "Coalition/Pax Armata"}
- GEM counts: {"GEM_HQ": 2, "GEM_CapturePoint": 5, "GEM_VehicleSpawner": 4, "GEM_Insertion": 16, "GEM_StationarySpawner": 4, "GEM_Battle_Pickup": 2, "GEM_CapturePoint_OutlineArea": 5, "GEM_VehicleResupplyStation": 2, "GEM_Collection_Event": 1, "GEM_SpecialCombatArea": 1, "GEM_Sector": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@127` pos (-60, -48) y=64 polys=[124]
  - HQ-E `@2` pos (129, 223) y=64 polys=[56]
- HQ-to-HQ distance 330 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@53` (-21, 32) y=65 key=-1 t=0.27 off-axis 13 m; no OutlineArea
  - B `@3` (102, 16) y=62 key=-1 t=0.44 off-axis 96 m; OutlineArea x1 (dist 6 m; @131)
  - C `@36` (22, 97) y=67 key=-1 t=0.50 off-axis 16 m; OutlineArea x4 (dist 3/2/6/2 m; @47,82,96,107)
  - D `@89` (-56, 205) y=68 key=-1 t=0.64 off-axis 141 m; no OutlineArea
  - E `@78` (41, 161) y=65 key=-1 t=0.69 off-axis 37 m; no OutlineArea
  - OutlineArea instances: 5 total, 0 farther than 150 m from any flag (none)
- Vehicle spawner pads: 4 total (IFV 2, LightTransport 2)
  - near HQ-W: 2 pads (IFV 1, LightTransport 1); distance median 41 m, max 42 m
  - near HQ-E: 2 pads (IFV 1, LightTransport 1); distance median 21 m, max 27 m
  - Air pads: none
- Forward spawners: none
- Stationary emplacements: 4 (AntiTank 4)
  - by nearest anchor: HQ-W 1 (AntiTank 1); flag B 1 (AntiTank 1); flag D 1 (AntiTank 1); flag E 1 (AntiTank 1)
- Automatic AA: none
- Resupply stations: 2 (Ground 2)
  - by nearest anchor: HQ-W 1 (Ground 1); HQ-E 1 (Ground 1)
- SpecialCombatArea: 1 instance(s) (@114); containing polygons: @42 POLY26 bbox [13.0, 66.0, 37.0, 123.0] (24 x 57 m); @95 POLY97 bbox [-98.0, -38.0, 148.0, 253.0] (246 x 291 m)
- Other: TelemetryArea 0; Battle_Pickup 2 (Battle_Pickup_Minigun 2); Collection_Event 1 (CollectionEvent 1); Sector 1 (Sector 1)
  - Battle_Pickup `@18` Minigun (111, -13)
  - Battle_Pickup `@50` Minigun (-83, 187)

### Hagental Base (MP_SUBSURFACE)

- Layer assets: Conquest, Conquest0, Conquest0_EcsPrefab_ecsPrefab, Conquest0_Schematic, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Gas, Conquest_Gas_Placement, Conquest_Gas_Placement_Schematic, Conquest_Global, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team2, Conquest_Telemetry, Conquest_Telemetry_EcsPrefab_ecsPrefab, generated/AG_Conquest_DynamicDD_Schematic_2E9D5A6C, generated/AG_Conquest_DynamicDD_boxes_7A2324E9, conquest/MeshVariationDb_Win32, conquest_gas/MeshVariationDb_Win32, conquest_gas_networkregistry_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry.
- factionOverrides: {}
- GEM counts: {"GEM_CapturePoint": 5, "GEM_Insertion": 16, "GEM_StationarySpawner": 2, "GEM_TelemetryArea": 5, "GEM_Sector": 1, "GEM_HQ": 2, "GEM_Battle_Pickup": 2}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@112` pos (-254, 102) y=64 polys=[162]
  - HQ-E `@143` pos (275, -128) y=66 polys=[137]
- HQ-to-HQ distance 577 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@31` (-201, 27) y=64 key=-1 t=0.14 off-axis 48 m; no OutlineArea
  - B `@18` (-82, 14) y=66 key=-1 t=0.33 off-axis 12 m; no OutlineArea
  - C `@4` (13, -8) y=65 key=-1 t=0.50 off-axis 6 m; no OutlineArea
  - D `@97` (108, -27) y=66 key=-1 t=0.66 off-axis 26 m; no OutlineArea
  - E `@160` (219, -50) y=66 key=-1 t=0.86 off-axis 50 m; no OutlineArea
- Vehicle spawner pads: 0 total (-)
  - Air pads: none
- Forward spawners: none
- Stationary emplacements: 2 (HMG 2)
  - by nearest anchor: flag B 1 (HMG 1); flag D 1 (HMG 1)
- Automatic AA: none
- Resupply stations: none
- No SpecialCombatArea instance; largest Conquest0 polygon (objective area, not a play area: it holds no HQ; LOW confidence): @48 bbox [-232.0, -118.0, 257.0, 95.0]
- Other: TelemetryArea 5; Battle_Pickup 2 (Battle_Pickup_Minigun 2); Sector 1 (Sector 1)
  - Battle_Pickup `@145` Minigun (-73, 10)
  - Battle_Pickup `@146` Minigun (94, -32)

### Mirak Valley (MP_TUNGSTEN)

- Layer assets: Conquest, Conquest_CaptureAreaVisualisation, Conquest_CaptureAreaVisualisation_ecsprefab_ecsPrefab, Conquest_Cover, Conquest_Global, Conquest_Global_Cables, Conquest_Global_ecsprefab_ecsPrefab, Conquest_Lighting, Conquest_Schematic, Conquest_Team1, Conquest_Team1_EcsPrefab_ecsPrefab, Conquest_Team2, Conquest_Telemetry, generated/DD_Conquest0_Schematics, generated/DD_Conquest0_Volumes, conquest/MeshVariationDb_Win32, conquest_networkregistry_Win32, conquest_templatedescriptorregistry, Game/GlacierMP/Levels/MP_Tungsten/_Layers_Gameplay/Conquest0, MeshVariationDb_Win32, staticmodelgroup.physics.
- factionOverrides: {}
- GEM counts: {"GEM_StationarySpawner": 15, "GEM_CapturePoint": 5, "GEM_Insertion": 16, "GEM_TelemetryArea": 5, "GEM_VehicleSpawner": 42, "GEM_VehicleResupplyStation": 7, "GEM_AutomaticAA": 2, "GEM_SpecialCombatArea": 1, "GEM_Battle_Pickup": 3, "GEM_HQ": 2, "GEM_Sector": 1}
- Layout variants: only layer `Conquest0` carries gameplay data. `Conquest_Team1`/`Conquest_Team2` exist as assets but hold no gameplay instances in the extraction.
- HQs (2), sorted by x; team identity is NOT stored. HQ-W/HQ-E = lower/higher x only:
  - HQ-W `@169` pos (-461, -240) y=80 polys=[10, 42]
  - HQ-E `@196` pos (497, -528) y=87 polys=[42, 201]
- HQ-to-HQ distance 1000 m. Capture points (5, variant key shown), ordered along the HQ-W to HQ-E axis by projection t (0 = HQ-W, 1 = HQ-E; letters are not stored, this is a spatial guess):
  - A `@3` (-216, -303) y=84 key=-1 t=0.25 off-axis 10 m; no OutlineArea
  - B `@236` (-20, -332) y=91 key=-1 t=0.45 off-axis 39 m; no OutlineArea
  - C `@152` (82, -160) y=85 key=-1 t=0.50 off-axis 233 m; no OutlineArea
  - D `@116` (55, -368) y=91 key=-1 t=0.53 off-axis 26 m; no OutlineArea
  - E `@110` (266, -436) y=87 key=-1 t=0.75 off-axis 22 m; no OutlineArea
- Vehicle spawner pads: 42 total (LightTransport 10, PTV_QuadBike 7, Tank 5, PTV_DirtBike 4, AttackHelicopter 3, MobileAA 3, AttackPlane 2, FighterPlane 2, IFV 2, ScoutHelicopter 2, TransportHelicopter 2)
  - near HQ-W: 16 pads (LightTransport 3, PTV_DirtBike 2, PTV_QuadBike 2, Tank 2, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 1, MobileAA 1, ScoutHelicopter 1, TransportHelicopter 1); distance median 17 m, max 69 m
  - near HQ-E: 16 pads (LightTransport 3, PTV_DirtBike 2, PTV_QuadBike 2, Tank 2, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 1, MobileAA 1, ScoutHelicopter 1, TransportHelicopter 1); distance median 24 m, max 85 m
  - near flag A: 2 pads (LightTransport 1, PTV_QuadBike 1); distance median 31 m, max 48 m
  - near flag B: 1 pads (LightTransport 1); distance median 46 m, max 46 m
  - near flag C: 4 pads (AttackHelicopter 1, MobileAA 1, PTV_QuadBike 1, Tank 1); distance median 33 m, max 52 m
  - near flag D: 1 pads (LightTransport 1); distance median 31 m, max 31 m
  - near flag E: 2 pads (LightTransport 1, PTV_QuadBike 1); distance median 25 m, max 30 m
  - Air pads: AttackHelicopter 3, TransportHelicopter 2, AttackPlane 2, FighterPlane 2, ScoutHelicopter 2
- Forward spawners: none
- Stationary emplacements: 15 (HMG 8, AntiTank 5, AntiAircraft 2)
  - by nearest anchor: flag A 4 (HMG 3, AntiTank 1); flag B 3 (AntiAircraft 1, AntiTank 1, HMG 1); flag C 2 (AntiTank 1, HMG 1); flag D 3 (HMG 2, AntiAircraft 1); flag E 3 (AntiTank 2, HMG 1)
- Automatic AA: 2 (AutomaticAA 2)
  - by nearest anchor: HQ-W 1 (AutomaticAA 1); HQ-E 1 (AutomaticAA 1)
- Resupply stations: 7 (Ground 5, Ground_Air 2)
  - by nearest anchor: HQ-W 2 (Ground 1, Ground_Air 1); HQ-E 2 (Ground 1, Ground_Air 1); flag A 1 (Ground 1); flag C 1 (Ground 1); flag E 1 (Ground 1)
- SpecialCombatArea: 1 instance(s) (@53); containing polygons: @42 POLY12 bbox [-1229.0, -1434.0, 1229.0, 614.0] (2458 x 2048 m); @171 POLY58 bbox [-335.0, -601.0, 387.0, 37.0] (722 x 638 m)
- Other: TelemetryArea 5; Battle_Pickup 3 (Battle_Pickup_Railgun 2, Battle_Pickup_Minigun 1); Sector 1 (Sector 1)
  - Battle_Pickup `@55` Railgun (-77, -280)
  - Battle_Pickup `@59` Minigun (76, -187)
  - Battle_Pickup `@89` Railgun (65, -385)


### Saints Quarter (MP_LIMESTONE)

No Conquest layer in either capture; empty MUT_Limestone.


## 3. Cross-map summary

"Pads W / E / near flags" = pads whose nearest anchor is HQ-W / HQ-E / any flag. On Empire State the order is HQ-1 (lowest x) / HQ-2 / rest. Team1/team2 are not stored, so W/E is geometric. Air = any helicopter, plane or naval fighter pad.

| Map | Flags | HQs | Pads W / E / near flags | Total pads | Initial score | Air vehicles |
|---|---|---|---|---|---|---|
| Siege of Cairo | 5 | 2 | 2 / 2 / 0 | 4 | 1200 | no |
| Empire State | 5 | 3 (2 live spawns + 1 non-spawn marker) | 0 / 0 / 0 | 0 | 1200 | no |
| Wake Island | 7 | 2 | 11 / 11 / 18 | 40 | 1200 (default; no per-map value) | yes |
| Blackwell Fields | 6 | 2 | 11 / 11 / 6 | 28 | 1200 | yes |
| Iberian Offensive | 5 | 2 | 3 / 3 / 2 | 8 | 1200 | no |
| Liberation Peak | 6 | 2 | 10 / 10 / 6 | 26 | 1200 | yes |
| Contaminated | 6 | 2 | 10 / 10 / 4 | 24 | 1200 (default; no per-map value) | yes |
| Area 51 | 9 | 2 | 16 / 16 / 29 | 61 | 1200 (default; no per-map value) | yes |
| Manhattan Bridge | 5 | 2 | 6 / 6 / 2 | 14 | 1200 | yes |
| Eastwood | 5 | 2 | 10 / 10 / 14 | 34 | 1200 | yes |
| Operation Firestorm | 5 | 2 | 15 / 15 / 7 | 37 | 1200 | yes |
| Railway to Golmud | 7 | 2 | 21 / 21 / 19 | 61 | 1200 (default; no per-map value) | yes |
| Tsuru Reef | 9 | 2 | 10 / 10 / 20 | 40 | 1200 (default; no per-map value) | yes |
| New Sobek City | 5 | 2 | 9 / 9 / 3 | 21 | 1200 | yes |
| Vegas Strip | 5 | 2 | 11 / 11 / 12 | 34 | 1200 (default; no per-map value) | yes |
| Cairo Bazaar | 5 | 2 | 2 / 2 / 0 | 4 | 1200 (default; no per-map value) | no |
| Hagental Base | 5 | 2 | 0 / 0 / 0 | 0 | 1200 (default; no per-map value) | no |
| Mirak Valley | 5 | 2 | 16 / 16 / 10 | 42 | 1200 | yes |
| Saints Quarter | no layer | - | - | - | none | - |

Notes on the table:
- Area 51 flag count is 9 CapturePoint instances; a CapturePoint_Proxy (@145) is a separate 10th object 18 m from @64 (section 4).
- Every map with data has an equal pad count at the two HQs (Siege of Cairo 2/2, Iberian Offensive 3/3, Eastwood 10/10, Mirak Valley 16/16, Wake Island 11/11, Blackwell Fields 11/11, Liberation Peak 10/10, Contaminated 10/10, Area 51 16/16, Manhattan Bridge 6/6, Operation Firestorm 15/15, Railway to Golmud 21/21, Tsuru Reef 10/10, New Sobek City 9/9, Vegas Strip 11/11, Cairo Bazaar 2/2) with identical class mixes (computed, HIGH). That strongly suggests mirrored HQ pad sets; that nearest-HQ equals owned-by-that-team is MEDIUM. The maps differ in the neutral pads near flags.
- Empire State has 3 HQs and 0 pads; Hagental Base has 2 HQs and 0 pads (infantry-only layouts). Cairo Bazaar has 4 pads (2 IFV, 2 LightTransport) and no air.
- Flags: Empire State 5, Wake Island 7, Blackwell Fields 6, Liberation Peak 6, Contaminated 6, Area 51 9, Manhattan Bridge 5, Operation Firestorm 5, Railway to Golmud 7, Tsuru Reef 9, New Sobek City 5, Vegas Strip 5, Cairo Bazaar 5, Hagental Base 5. Siege of Cairo 5, Iberian Offensive 5, Eastwood 5, Mirak Valley 5.


## 4. Open questions and unresolved items

1. Resolved: Siege of Cairo, Eastwood, Mirak Valley and Iberian Offensive now have full Conquest0 data (5 flags, 2 HQs each). Remaining caveats: letters are the spatial guess only; Siege of Cairo and Iberian Offensive have no SpecialCombatArea instance (play area from the largest polygon, LOW); Mirak Valley flag @152 is 233 m off the HQ line so its letter is uncertain.
2. Empire State (MP_AFTERMATH): 3 HQs. @162 (-674,-150) and @97 (-526,46) each have a spawn polygon with Insertion points, and @97 shares polygon 142 with the Sector; @154 (-555,-142) lies only in the main polygon @170 with no Insertions. Which two are the live team HQs is unresolved; @154 may be a spare or an alternative layout (the Winter_Conquest0 asset is not decoded). Only 1 of 5 flags has an OutlineArea (flag E, @189, OutlineArea @151). No pads, 6 HMG emplacements, no SpecialCombatArea instance.
3. Area 51 (MP_DRYLAKE): CapturePoint_Proxy @145 at (225, 1146), 18 m from CapturePoint @64, both in box @178 / polygon @23. Probably a stand-in for that flag, so the playable flag count is 9 (MEDIUM) rather than 10. Not tested in game. No OutlineArea, no TelemetryArea, 61 pads (the most; 17 LightTransport and 17 quad bikes).
4. Letter order is a guess everywhere (see conventions). Wake Island, Tsuru Reef, Area 51 and Railway to Golmud flags sit hundreds of metres off the HQ-HQ line.
5. Battle_Pickup is placed on 14 of 18 maps (all except Wake Island, Area 51, Tsuru Reef, Vegas Strip) with Minigun, Railgun, SmokeScreen, ArtilleryStrike variants (the objective table also lists DSPulse). Placed but not active in the live game per the task brief; not verified here. Liberation Peak @145 and @218 and Iberian Offensive @84 use the base variant (GMPF_Battle_Pickup). Collection_Event (1 instance on each of 11 maps, pos 0,0,0) is a non-spatial logic object. Sector (1 per map) is a marker; on Empire State it lies in the spawn polygon of HQ @97.
6. PsyGasZone exists only on Contaminated (6: Outdoors @17, @41; Enclosed @84; Underground @160, @262, @264). Contaminated also lists Conquest_Gas, Conquest_GasPlacement and Conquest_Loot assets (not decoded); Hagental Base lists Conquest_Gas assets but has no PsyGasZone instance.
7. Contaminated has 10 OutlineArea instances for 6 flags, 6 of them more than 150 m from any flag (@130, @138, @140, @153, @173, @261): outlines are not one-per-flag there. Operation Firestorm has 17 outlines for 5 flags. Reason unknown.
8. SpecialCombatArea: most instances sit in two polygons (outer boundary and an inner/alternate one, e.g. Liberation Peak @115 and @211, Area 51 @190 and @203). Which is the live combat boundary is not stored. The outer one is the likely play boundary (MEDIUM). Wake Island, Empire State, Hagental Base, Siege of Cairo and Iberian Offensive have no SpecialCombatArea instance; their play area is inferred from the largest polygon only (LOW).
9. Vehicle cooldown fallbacks and XP: none exist in MUT_Conquest or its graphs. The only vehicle-related number found is MP_Dumbo_VehicleOOBtime = 10 (per-map). They must be in vehicle or progression assets outside this extraction.
10. VehicleSpawner_Forward appears on Operation Firestorm (6: 3 nearest each HQ), Siege of Cairo (4: 2 each HQ) and Iberian Offensive (3, all nearest HQ-W); what they spawn and their ownership is unknown.
11. Faction overrides: Siege of Cairo, Blackwell Fields, Operation Firestorm, Railway to Golmud, Tsuru Reef set team1 = Coalition/Pax Armata and team2 = Alliance/NATO; Eastwood and Cairo Bazaar set team1 = Alliance/NATO and team2 = Coalition/Pax Armata; Iberian Offensive and the other maps leave it empty (engine default).
