# Breakthrough: sides, sectors and vehicle spawners per map (build 2.1.1.0, 19 Oct 2026)

Working note, not a closed lead. Source captures (all under `builds\2.1.1.0\reports\`, recorded):
`breakthrough-layers-2026-10-19` (per-map Breakthrough layers, level roots, GM/MUT/AD assets),
`breakthrough-teams-2026-10-19` (team data, faction metadata), `breakthrough-gems-2026-10-19` and
`breakthrough-gems2-2026-10-19` (GEM blueprints, GMPF variants, model interfaces),
`breakthrough-registries-2026-10-19`, `breakthrough-mi-2026-10-19`, `breakthrough-globals-2026-10-19`
(gameplay global layers, plus the lowercase Atoll and Golmud Breakthrough layers).
Decoded with `frosty-ebx-decode.py`; extraction script and per-map text files are in the session scratchpad.

## How the data encodes it

- **Factions per team.** `LPF_Teams_Team1vsTeam2` binds team 1 to `BFTeamData_Alliance`
  (`ID_FACTION_ALLIANCE`, `ID_GAMEMODE_TEAM_US`, Alliance icon = NATO) and team 2 to
  `BFTeamData_Coalition` (`ID_FACTION_COALITION`, `ID_GAMEMODE_TEAM_RU`, Pax Armata icon).
  A map's Breakthrough layer can override the two faction slots (ids 227737705 / 227737706) with the
  faction ids 607944106 (Alliance) or -1865993703 (Coalition). Eight maps do; the rest use the default.
- **Attackers.** `DiceEx_Sector` computes `AttackingTeam`/`DefendingTeam` from an `InvertTeamRoles`
  input (default off). No map sets it. The round logic names `SectorTeam1Deaths` and
  `Team2ScoreToBeReset`, which fits team 1 attacking. **Team 1 = attackers is inferred, not read from a
  literal**; in-game matches on 19 Oct 2026 agree, and the EA 1.4.2.0 Portal notes say capture points
  "are now automatically assigned to Team 2", i.e. team 2 defends.
- **Vehicle spawners.** Each `GEM_VehicleSpawner` instance carries a variant key; `AD_Objective_Breakthrough`
  maps the key to a GMPF prefab: 0 LightTransport, 1 IFV (CV90 name), 2 Tank (Abrams name), 3 MobileAA
  (Gepard), 4 AttackPlane, 5 FighterPlane (F-22), 6 AttackHelicopter (AH-64E), 7 TransportHelicopter
  (UH-60), 8 PTV_QuadBike, 9 APC, 10 PTV_GolfCart, 11 RHIB, 12 ScoutHelicopter (AH-6M), 13 PTV_DirtBike,
  14 PatrolBoat (CB90), 15 MultirolePlane (F/A-18F), 16 NavalFighterPlane (F-14), 17-23 carrier jet
  launches. No key = IFV. The prefab names one NATO vehicle; `LPF_VehicleSpawner_FactionPicker` picks the
  faction's model at runtime, so the tables below give the vehicle class, not the faction-specific model.
  Stationary spawner keys: 0 HMG, 1 AntiTank, 2 AntiAircraft.
- **Pads belong to HQs** (EA 1.4.3.0 Portal notes: "HQs can now be linked to Sectors, VehicleSpawners can
  be linked to HQs"). `DiceEx_SetVehicleSpawners` takes `HQEnabled` and sets `VehiclesEnabled` on the
  spawners `Assigned` to that HQ (`OnlyUpdateOnHQEnabled`), so a pad is live when its HQ is live. The
  assignment itself is not serialized; nearest-HQ grouping reproduces the in-game sets (Area 51: the HQ@42
  group of 8 pads is one side's set exactly). Per-phase tables use HQ groups: attackers draw on the HQ
  on their side of the sector, defenders on the HQ on theirs. `Enum_VehicleSpawnerEnabler` (All / None /
  SingleRandom) and `LinkAlternateSpawn` exist, which would explain sets smaller than a group.
- **Team and sector per spawner/HQ are not stored.** The HQ interface has `Team`/`AltTeam` (defaults 1/2)
  and the sector interface `SectorValue`, but no instance in any layer overrides them (checked: instance
  override lists empty, raw slot sizes match the 144-byte layout, companion registries hold nothing). The
  sector logic (`GameModeControlsHQ`, `InvertedHQ`) assigns HQs at runtime. So sector order and the side a
  spawner serves are **derived spatially** from sector boxes/polygons and HQ positions. Each per-map
  section states its confidence.
- **Player count.** Not in the client map or mode data. `MI_Sim_GameState.MaxPlayers` exists but no map,
  mode, launch function or tweakable sets it. The only related literal is a constant 32 in
  `GM_Breakthrough_LaunchFunction`, and `MUT_Breakthrough` has `BT_LayoutSelection` = 0 (range 0-3,
  so four layouts exist and the client default is layout 0) and `BT_iCustomSectorCount` = 2 with
  `BT_bUseCustomSectorCount` off. The lobby timer tweakables start at 24 players and speed up at 48. Player count per map is a server playlist setting.

## Faction per map (team 1 = inferred attackers)

| Map | Display name | Team 1 | Team 2 | Source |
|---|---|---|---|---|
| MP_Abbasid | Siege of Cairo | Pax Armata | NATO | layer override |
| MP_Badlands | Blackwell Fields | Pax Armata | NATO | layer override |
| MP_Isolated | Tsuru Reef (EA maps page; "resort" assets) | Pax Armata | NATO | layer override |
| MP_Paradise | Vegas Strip (EA maps page; "vegas"/"strip"/"casino" assets) | Pax Armata | NATO | layer override |
| MP_Plaza | Cairo Bazaar (EA maps page; "market" assets; "Archway Plaza" is a loc string for it) | Pax Armata | NATO | layer override |
| MP_Contaminated | Contaminated (EA maps page; German airbase assets) | NATO | Pax Armata | layer override |
| MP_Eastwood | Eastwood | NATO | Pax Armata | layer override |
| MP_FireStorm | Operation Firestorm | NATO | Pax Armata | layer override |
| MP_Aftermath | Empire State | NATO | Pax Armata | default |
| MP_Capstone | Liberation Peak | NATO | Pax Armata | default |
| MP_Dumbo | Manhattan Bridge | NATO | Pax Armata | default |
| MP_Outskirts | New Sobek City | NATO | Pax Armata | default |
| MP_Subsurface | Hagental Base (operator; loc 2544B1A9, "hangars at the heart of the facility") | NATO | Pax Armata | default |
| MP_Tungsten | Mirak Valley | NATO | Pax Armata | default |
| MP_Atoll | Wake Island (EA maps page; carrier assets) | NATO | Pax Armata | default |
| MP_DryLake | Area 51 (EA maps page; "area51"/"lab_"/"hangar" assets) | NATO | Pax Armata | default |
| MP_GolmudRailway | Railway to Golmud (EA maps page) | NATO | Pax Armata | default |

MP_Battery (Iberian Offensive) and MP_Limestone (Saints Quarter) have no Breakthrough layer in this build.

No seasonal UI level metadata exists in 2.1.1.0; the newer maps have map art and loading screens but no
metadata entry. Names for the newer maps come from the EA maps page
(https://www.ea.com/games/battlefield/battlefield-6/features/maps), each checked against setting words in
the level's asset routes. Hagental Base (MP_Subsurface) is not on that page. The Hagental Base description ("NATO is desperate to
reclaim it" from Pax Armata) fits NATO attacking on MP_Subsurface, where team 1 is NATO by default; this is
the one narrative cross-check for team 1 = attackers.

## Vehicle classes to in-game names

From the L3306 archetype table in VEHICLES.md plus the GMPF blueprint names; faction pairing from an
in-game sample on 19 Oct 2026 (NATO side listed first).

| Spawner class | NATO | Pax Armata | Archetype |
|---|---|---|---|
| Tank | M1A2 SEPv3 | Leo A4 | arch_mbt |
| IFV | M3A3 Bradley | Strf 09 A4 | arch_ifv |
| APC | LTV | Traverser Mark 2 | arch_carapc |
| LightTransport | Glider 96 | VECTOR | arch_lighttrans |
| PTV_DirtBike | M1030-M1 | TM/O 450 | arch_motorcycle |
| PTV_QuadBike | Rugged MV740 | (same) | arch_car |
| PTV_GolfCart | Turfpro PTV Royal | (same) | arch_car |
| MobileAA | Cheetah 1A2 | GE-26 PAX | arch_antiair |
| AttackHelicopter | M77E Falchion | Panthera KHT | arch_heliattack |
| ScoutHelicopter | AH-6 Little Bird | (MH-350, no blueprint saved) | arch_heliscout |
| TransportHelicopter | UH-79 | (same seen in sample) | arch_helitrans |
| AttackPlane | F-61V | F-39E | arch_jetattack |
| FighterPlane | F-97 Kestrel | Su-57 | arch_fighterplane |
| MultirolePlane | F/A-81F Super Spectre | | arch_jetmultirole |
| NavalFighterPlane | F-74A Seacat | | arch_jetfleet |
| RHIB | 7.7m NSW RHIB | | arch_inflatableboat |
| PatrolBoat | RCB-90 Patrol Boat | | arch_patrolboat |
| Stationary HMG / AntiTank / AntiAircraft / AutomaticAA | M2 HMG / TOW / GDF-009 / Phalanx | | stationary |

## In-game check (19 Oct 2026, thirteen matches)

- Sides: Railway to Golmud (NATO attacks), Manhattan Bridge (NATO attacks) and Vegas Strip (Pax attacks)
  match team 1 = attackers with the faction table above. Area 51 (NATO attacks, confirmed by the operator
  after a first mislabelled note) fits too. Four maps, four matches with team 1 = attackers.
- Sector counts: Vegas Strip is 3 sectors in-game; the fourth marker (S59, no spawners) is not a sector.
  Area 51 is 4 (confirms the B+C merge). Railway to Golmud is 4, so one of the five polygon areas is not
  a sector. Manhattan Bridge is 3.
- Vehicles: the in-game set per side per sector is 5 to 9 vehicles; the per-phase pools here are every
  pad in the area, so they are an upper bound. Area 51 in-game "sector 3" attackers (M77E, M1A2,
  Bradley, 3 Glider 96, 2 M1030-M1) equal the area A pool exactly (AtkHeli, Tank, IFV, LT x3, Dirt x2),
  which validates the extraction but shows the phase numbering there is off by one. Area 51 defenders at
  sector 2 (operator unsure between 1 and 2: 4 TM/O 450, VECTOR, Strf 09 A4, UH-79 = Dirt x4, LT x1,
  IFV x1, TrHeli x1) are a subset of the B+C pool the report gives phase 2 defenders (Dirt x12, LT x11,
  IFV x3, TrHeli x2, ...), consistent with the chain but with a gated subset of the pads live. Vegas Strip sector 2
  (attackers Strf 09 + Traverser, defenders LTV + Bradley) fits the alternate reading where the staging
  block is the defenders'. Manhattan Bridge showed no vehicles on either side despite IFV, quad and
  light-transport pads in the layer, which points at a layout (player-count) variant with vehicles off.
- Second batch (Wake Island, Contaminated, Liberation Peak, Cairo Bazaar, Tsuru Reef): sector counts
  5, 5, 5, 3, 4 (Wake Island and Contaminated were 6 in the first reading; one marker pair merged on each).
  Liberation Peak reversed to west-to-north-east with both attacker samples (Tank + IFV) on exact HQ groups.
  Tsuru Reef pinned south-to-north with attackers at sectors 1 and 2 on HQ@150 and HQ@316 as near-exact
  groups. Cairo Bazaar fits as is. Contaminated's defender sample (Dirt x1, LT x2) fits no single HQ group.
  Wake Island's two attacker samples fit the start-end groups HQ@185 and HQ@506 only, two phases earlier
  than logged, so its chain is still low confidence.
- Third batch (Blackwell Fields, Siege of Cairo, Eastwood, New Sobek City): Siege of Cairo attackers at
  sector 1 (IFV + APC) equal the start HQ group exactly. Eastwood reversed to west-to-east (sector 2
  attackers TrHeli + IFV = HQ@100 + HQ@1). New Sobek City is 3 sectors, not 4 (S15 merged into S207),
  with the two defender sets exact on HQ@156 and HQ@71. Blackwell Fields was first logged as NATO
  attacking; the operator corrected it to Pax Armata attacking, which matches the layer override and the
  reversed chain the samples fit (sides and chain were both noted the wrong way round in the first log).
  All 17 side assignments in the faction table are now consistent with every match sampled.
  "None" entries in a sample may mean every vehicle was out at the time and are treated as weak.
- Official cross-check: the EA 1.4.3.0 update notes list Tsuru Reef Breakthrough changes per sector
  (attacker APC at S1 and S2, attacker LT and no defender APC at S3, defender Quad at S2, S4 reduced to one
  capture point). The HQ-group table agrees on all four sectors, including the capture-point counts
  (2, 2, 2, 1). Saved patch notes in `reference-data/patch-notes/` are an inventory with URLs only; the
  full articles were fetched on 19 Oct and the Breakthrough passages saved as
  `reference-data/patch-notes/breakthrough-passages-2026-10-19.md`. Update 1.1.3.0 states per-sector
  attacker/defender vehicle changes for Manhattan Bridge, Mirak Valley, New Sobek City, Operation
  Firestorm, Liberation Peak and Siege of Cairo; those are checked in the map sections. Result: the
  2.1.1.0 data no longer matches several of them (no tank pads at all on Siege of Cairo or New Sobek City,
  Mirak Valley defenders still hold pads, Manhattan Bridge sector 3 defenders still hold an IFV and quads),
  while the 2026 in-game samples do match the data. The Dec 2025 notes describe a superseded layout; only
  the 1.4.3.0 Tsuru Reef notes are current, and those agree. Manhattan Bridge's sector 2 HQ pair is
  resolved by the note (HQ194 defenders with the AT emplacement, HQ93 the sector 3 attackers' IFV).
- Opus review (19 Oct): every HQ-group count checked against the grouping output; stale first-pass prose
  fixed or removed; Wake Island chain rebuilt on the reviewer's 5-sector reading. Reviews are in
  `breakthrough-reviews-2026-10-19/`. Three samples carry one vehicle more than the assigned HQ group
  (Golmud: a start-HQ attack jet at sector 2; Tsuru Reef: a dirt bike; Contaminated: two LTs from the next
  HQ), so some pads of the previous or next HQ stay live. The single-HQ-per-side rule is an approximation.
- Open: per-pad sector and layout gating is not in the layer files; the schematic layout entries are the
  next lead.

## Objectives per sector (capture points, attack order)

"Data" is the chain split of GEM_CapturePoint instances; "Live" is the operator's in-game count where
given. Where the layer holds more points than the live mode shows, the extras are near-duplicates or a
second layout's set (see notes), consistent with the per-map layout toggles in the schematics.

| Map | Live (operator) | Data split | Total pts | Note |
|---|---|---|---|---|
| Siege of Cairo | 2/1/2/1 | 2/1/2/1 | 6 | agrees |
| Empire State | 1/2/1 | 1/2/1 (+3 extra) | 7 | extras: a duplicate 0.9 m from another point, and a north flank pair |
| Blackwell Fields | 1/1/3 | 1/1/3 | 5 | agrees; reversed chain (Pax attacks) |
| Liberation Peak | 1/2/2/1/1 | 1/2/2/1/1 | 7 | agrees |
| Manhattan Bridge | 1/2/2 | 1/2/2 | 5 | agrees after reversing the chain (west to east); see section |
| Eastwood | 1/2/1 | 1/2/1 | 4 | agrees |
| Operation Firestorm | 1/2/1 | 1/2/1 | 4 | agrees |
| New Sobek City | 2/1/2 | 2/1/2 (+1 extra) | 6 | extra: CP@177, isolated off the chain line |
| Vegas Strip | 2/2/2 | 2/2/2 (+1 extra) | 7 | S1 CP48/CP124, S2 CP133/CP38, S3 CP24/CP114 (z -25, by Sector@51); extra: CP@103 at (128,-46) off the chain with the dropped Sector@59 and padless HQ@144 |
| Cairo Bazaar | 2/2/2 | 2/2/2 | 6 | agrees |
| Hagental Base | 2/1/1/2 | 2/1/1/2 | 6 | agrees after merging markers; 4 sectors |
| Mirak Valley | 2/2/2 | 2/2/2 | 6 | agrees after merging the two middle markers; 3 sectors |
| Contaminated | 1/2/2/1 (memory) | 1/2/2/2/1 (+1 extra) | 9 | match log said 5 sectors; extra is a near-duplicate 33 m from another |
| Tsuru Reef | 2/2/2/1 | 2/2/2/1 | 7 | agrees (operator screenshots of all four sectors, Pax attacking): S1 and S2 on the south-west island, S3 on the central island with the attackers' zone extending into the harbour, S4 a single objective in the town below the northern industrial base; matches EA 1.4.3.0 notes |
| Railway to Golmud | 2/2/1/2 | 2/2/1/2 | 7 | agrees |
| Wake Island | 2/2/2/2/2 | 2/2/2/2/2 (+1 extra) | 11 | agrees; operator screenshot of the last sector shows A and B close together on the tail arm of the atoll, attackers' area to the west over the sea; the layer holds three points there (CP@367, CP@441, CP@220 along z 420; CP@441 and CP@220 44 m apart), one unused |
| Area 51 | 2/2/2/1 | 2/2/2/1 (+1 extra) | 8 | agrees; operator screenshot of sector 3 shows A and B side by side (CP@193, CP@39) with the attackers' HQ beyond A and the defenders' HQ well beyond B; CP@168 (53,1131), 110 m off the line, is the extra |

## Other Breakthrough data in the files (added 19 Oct 2026, evening)

Source: `MUT_Breakthrough` (119 named tweakables), `GME_Sim_Breakthrough_Round` (round logic),
`MI_Sim_SectorSettings`, the per-map layers (non-vehicle GEM kinds) and `fs_us_loc.strings.tsv`.
Full tweakable dump: `breakthrough-reviews-2026-10-19/mut-breakthrough-table.txt`; per-map extras:
`breakthrough-reviews-2026-10-19/bt-extras.txt`.

### Mode rules (MUT_Breakthrough, client defaults; a server playlist can override any of them)

| Rule | Value | Notes |
|---|---|---|
| Objective capture time | 30 s | `BT_fObjectiveCaptureTime` |
| Objective neutralisation time | 30 s | `BT_fObjectiveNeutralizationTime` |
| Capture speed by players on the point | x0, x1, x1.333, x1.666, x2.0 | `CapturePlayersMultipliers` for 0..4+ players; `BT_iMaxCaptureMultiplier` 5 |
| Capture/neutralise by objective count or teams | all x1 | the multiplier arrays are flat |
| Respawn delay | 12 s attackers, 12 s defenders, every sector | `AttackerRespawnDelays` / `DefenderRespawnDelays` (15 entries each, all 12); `BT_fGlobalRespawnDelay` 10; `BT_bTeamSpecificRespawnDelay` on |
| Sector taken pause | 6 s | `BT_fSectorTakenDuration` |
| Clean-up phase | 15-45 s | `BT_fSectorCleanUpDurationMin/Max`; ends early at threshold 10 (`BT_fSectorCleanUpEndedEarlyThreshold`, range 5-15); the loc string says the faster attackers clear defenders the sooner the next sector starts |
| Advance phase | 40 s | `BT_fSectorAdvanceDuration` (attackers move up; reminder at 30 s, +15 s increments) |
| Reinforcements phase | 5 s | `BT_fSectorReinforcementsDuration`; announcement delay 5 s |
| Sector time | 20 | `BT_iSectorTime`, unit not stated (round logic has `TotalTime`, `StartingTime`, `IsOvertime`, so a per-sector clock with overtime exists) |
| Remaining-respawn warnings | 75 / 50 / 25 | `BT_iRemainingRespawnsThreshold1-3`; urgency at 30 respawns or 60 s (`BT_iUrgencyRespawnsThreshold`, `BT_fUrgencyTimeThreshold`) |
| Score bleed per soldier death | 1 | `BT_iSoldierDeathScoreBleed` (range to 10) |
| Out of bounds | 10 s to return | `BT_iOutOfBounds_TimeToReturn`; `MUT_Dumbo` sets `MP_Dumbo_VehicleOOBtime` 10 (range 1-15) |
| Vehicle respawn fallback (per team, same both) | Light 15 s, Util 60 s, Heavy 120 s, AirCombat 120 s, AirTransport 60 s | `BT_fVehicleCooldown_Fallback_Team1/2_*`; used when a spawner has no own value |
| Man-down type | 1 | `BT_iSoldierMandownType` (range to 2) |
| Retreaters | spotted in world, minimap, no occlusion; successful retreat awarded (50 XP) | `RetreatersSpotting_*`, `BT_AwardSuccessfulRetreat` |

Attacker reinforcement count per sector is **not** a tweakable. The round logic names the variables
(`InitialTickets`, `AttackerStartTickets`, `ReinforcementCount`, `PreviousSectorDeaths`,
`SectorTeam1Deaths`, `Team2ScoreToBeReset`, `TicketAdded`) and holds unnamed constants (200 with range
0-1000, 100, 20, 2000, 2), but the decoded graph does not say which constant feeds which variable, so
the per-sector ticket count stays unread from the client. Loc strings describe the rule: "Earn
reinforcements after taking each sector", "Take final sector to win the battle", "killing the attackers
until they run out of reinforcements". "REINFORCEMENTS REMOVED PER KILL" is a Portal setting label.

XP (same asset): kill 50, headshot +20, takedown 25, pilot kill 50, multi-kill 50, revive 50, being
revived 15, heal 20, resupply 20, repair 20, spot 5, objective capture 200, neutralise 200, securing 15,
holding 15, sector captured 100, vehicle destroyed 50, disabled 10, assists 40-50, playing with friends
1000, time XP 250 per minute, win XP by span 130/100/80 per minute over 25/15 minute spans.

### Sector and HQ interfaces

`MI_Sim_SectorSettings` exposes `SectorID`, `SectorInitialOwner` (+`Set` flag), `isSingleSector` and
`SectorObjectivesActiveCount`; `MI_Sim_Sector` has `SectorValue`, `SecondarySectorValue`,
`SectorRating`, `TreatLikeSingleSector`, `AlwaysDisplaySectors`, `ShowEnemyHQOnSpawn`,
`RetreatTimerLength`, `AdvanceTimerLength`, `NumOfRetreaters`, `MI_Sim_Battlepickups` and
`MI_PsyGas_SectorData`. `MI_LD_HQ` has `Team`, `AltTeam`, `HQEnabled`, `VehicleSpawnersEnabled`,
`ForceRedeploy`. None of these is overridden per instance in any layer (see above), which is why the
report infers them spatially. `SectorObjectivesActiveCount` existing as a runtime input is consistent
with the live objective count per sector being chosen at runtime (layout), not per capture point.

### Battle pickups (GEM_Battle_Pickup) -- placed in the layers but NOT active in the live game

Operator (19 Oct 2026): battle pickups are not currently active in Breakthrough. The layers still carry
the placements below (the 1.1.3.0 notes once tied their spawn to the sector enabling), so treat this as
dormant data: a layout toggle or server setting keeps them off, and nothing in the client marks that.
Variants: 0 Minigun, 1 Railgun, 2 SmokeScreen, 3 ArtilleryStrike, 4 DSPulse (no map uses 4). Nearest
layer object in brackets (indices as in the scratchpad map files).

| Map | Pickups |
|---|---|
| Siege of Cairo | Minigun x2 (CP50 in S187; CP71 in S311) |
| Empire State | 1 generic pickup (no variant key) at HQ89 |
| Blackwell Fields | Minigun x2 (HQ135, HQ64) |
| Liberation Peak | Minigun (HQ184), Railgun (CP3 / HQ213) |
| Contaminated | Minigun (HQ209, east end) |
| Manhattan Bridge | Minigun (HQ123, the attackers' padless start) |
| Eastwood | Minigun (HQ1) |
| Operation Firestorm | Railgun (CP164 in S103) |
| Railway to Golmud | SmokeScreen x5, ArtilleryStrike x3 (one on CP212), spread along the whole chain |
| New Sobek City | Minigun (CP18 in S207) |
| Hagental Base | Minigun (HQ180) |
| Mirak Valley | Railgun (CP71 / HQ218), Minigun (HQ39) |
| Wake Island, Area 51, Tsuru Reef, Vegas Strip, Cairo Bazaar | none |

### Vehicle resupply stations (GEM_VehicleResupplyStation; key 0 = Air variant)

Wake Island 5, Blackwell Fields 2, Liberation Peak 4, Contaminated 9, Area 51 4, Eastwood 5 (1 air),
Operation Firestorm 8 (3 air entries at one point, duplicates), Railway to Golmud 6 (1 air), Tsuru Reef
1, New Sobek City 4, Cairo Bazaar 2, Siege of Cairo 1. None on Empire State, Manhattan Bridge, Vegas
Strip, Hagental Base or Mirak Valley. Positions and nearest HQ are in `bt-extras.txt`.

### Other layer objects

- `GEM_AutomaticAA` x2 on Area 51 only, both at the west end by HQ@236 (the defenders' final base in
  the current reading). Loc string 43B1700D: an AA missile battery protects enemy-owned sector airspace
  and is claimed by taking the sector.
- `GEM_VehicleSpawner_Forward` (forward spawners, enabled by `ForwardSpawnerEnabled`): Area 51 x4 at
  the far east (HQ@96 base), Operation Firestorm x2, New Sobek City x2, Vegas Strip x1.
- Contaminated: 44 `GEM_PsyGasZone` (Outdoors, Underground; 6 unkeyed ones ~800 m south of the map,
  probably a template store), 4 `GEM_PsyGasArtilleryStrike`, 5 activators; gas is tied to sectors through
  `MI_PsyGas_SectorData`.
- `GEM_Insertion` x16 per map (deploy arrival animations: Cautious/Chaotic Arrival, OnSpot, LongDistance,
  MH-47 fast rope on Golmud and Area 51), `GEM_Insertion_Event` x5 on Siege of Cairo (airstrike and jet
  fly-by during deploy), `GEM_SpecialCombatArea` 17 in all, `GEM_DeployCam` on Firestorm, Golmud and
  Hagental, `GEM_GadgetBlocking` x1 on Mirak Valley, `GEM_CapturePoint_OutlineArea` (minimap outlines).
- Per-map `MUT_<map>` tweakables hold only Conquest initial score (1200 everywhere), spawn-prevention
  radii and Golmud train toggles; nothing Breakthrough-specific.
- `Breakthrough_Layout00-03` are empty marker assets (316 bytes each): the layout is a selector value,
  the layout content lives in the per-map schematic toggles.

## Per-map sector chains (spatial inference by subagents, Opus-reviewed; indices refer to the scratchpad map files)

Numbers are the instance index after "@" in the map files. Side rule: spawners in the sector being attacked serve defenders, spawners in the previously captured sector or the start base serve attackers.

## Siege of Cairo (MP_ABBASID)
Chain runs west to east along x. Attackers (team1 = Coalition) start at the west base, POLY21@21, which holds HQ313 plus APC104 and IFV167 and lies outside every sector box. Confidence in direction: high.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Start base (POLY21@21, no sector box) | none | HQ313 | APC x1 (104), IFV x1 (167) | Attackers during sector 1 | High |
| S1 = Sector@187, BOX253 + BOX218 (split box, z -75..23 and 23..134) | CP50, CP102 | HQ33 (in 218) | IFV x1 (61) | Defenders | Medium: only one spawner |
| S2 = Sector@311, BOX265 | CP71 | HQ8, HQ63 (adjacent pair) | APC x1 (119), IFV x1 (180) | Defenders while S2 is attacked, attackers once S2 is captured | Medium |
| S3 = Sector@221, BOX105 + BOX152 (split, z -18..79 and -126..-18) | CP284 (105), CP276 (152) | HQ74, HQ283 (152) | IFV x1 (277, in 105) | Defenders | Medium |
| S4 = Sector@95, BOX304 | CP312 | HQ198 (sector HQ), HQ151 (in final-base POLY24@179) | IFV x1 (47, in POLY24@179 with HQ151) | Defenders (final base) | Medium |

Anomalies:
- S1 and S3 are split boxes.
- BOX152 has HQs and a capture point but no spawner.
- The defenders' final base sits inside BOX304 (POLY24@179) rather than beyond it.
- 2 spawner classes: APC x2, IFV x5 (7 spawners).

### Per-phase vehicles (attack vs defense)
Built on HQ pad groups. HQs ordered along the chain; the defenders' HQ of phase N flips to the attackers once sector N is captured (HQ pairs at one spot cannot be told apart, so they are marked unresolved).

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ313: APC x1, IFV x1 | HQ33: IFV x1 |  |
| 2 | HQ33: IFV x1 | HQ8: IFV x1 / HQ63: APC x1 | HQ8 and HQ63 are coincident, one per side unresolved |
| 3 | the one of HQ8/HQ63 not used by defenders | HQ283: IFV x1 / HQ74: none | HQ283 and HQ74 coincident, unresolved |
| 4 | the one of HQ283/HQ74 not used by defenders | HQ151: IFV x1 (final base); HQ198: none |  |
| unassigned | - | - | none; every pad-bearing HQ is used |

Sample check (Siege of Cairo, Pax attacking, sector 1 attackers IFV x1 + APC x1): matches phase 1 attackers HQ313 (APC x1, IFV x1) exactly. Direction and start base confirmed.

Patch-note check (1.1.3.0): "Added an additional Attacker tank in sector 1 and 3". The data has no Tank pad on Abbasid (only APC and IFV), and the later in-game sample (sector 1 attackers IFV x1 + APC x1) also shows no tank. So either a later update removed the added tanks, or this data predates the patch. I cannot tell whether the APC key (9) maps differently; the sample's APC matches HQ313's APC pad, which argues against a remap. Sides unchanged: HQ313 (sector 1 attackers) and HQ33/HQ8/HQ63 groups remain as tabulated.

## Empire State (MP_AFTERMATH)
No boxes exist on this map; everything is polygons. The chain runs along z. The direction is a guess: I picked north (z +110) to south (z -167) with low confidence, because both ends have an HQ-only region with no sector marker. North is POLY18@110 (HQ114, whose pad group is HMG x1, 73 m away). South is POLY33@57 / POLY27@145 (HQ89 plus HMG71). The south end has the only emplacement, which suits a defenders' final base, so I chose north as the attackers' start.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Start base (POLY18@110) | none | HQ114 | HMG x1 (nearest-pad group of HQ114) | Attackers | Low (direction uncertain) |
| S1 = north zone (z -11..108, POLY35@9, POLY29@53). Markers Sector@20 and Sector@95 (both) share identical polygons | CP22, CP87, CP171 | HQ135 | HMG x2 (69, 151); HQ-group view gives HQ135 HMG x1 and HQ114 HMG x1 | Defenders | Low |
| S2 = middle zone (z -63..7, POLY19@150, POLY7@125). Its marker is not clear; Sector@83 lies at its south edge, in POLY29@94 and POLY27@175 as well as the south polygons | CP5, CP50, CP161 | HQ29, HQ176 | HMG x1 (88) | Defenders | Low |
| S3 = south zone (POLY27@108, POLY33@33; z -205..-52) | CP129 | HQ154, HQ157, HQ172 | none | Defenders | Low |
| Final base (POLY33@57 / POLY27@145) | none | HQ89 | HMG x1 (71) | Defenders | Low |

Anomalies:
- 3 sector markers cover only 2 distinct polygons on the north side (Sector@20 and Sector@95 are duplicates).
- Sector@83 straddles the middle and south zones.
- There are no vehicle spawners at all, only 4 HMG StationarySpawners. Spawner classes: HMG x4.
- The sector order in the table is inferred from capture point groups, not from markers.

### Per-phase vehicles (attack vs defense)
Built on HQ pad groups. HQs ordered along the chain; the defenders' HQ of phase N flips to the attackers once sector N is captured (HQ pairs at one spot cannot be told apart, so they are marked unresolved).

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ114: HMG x1 | HQ135: HMG x1 | direction uncertain |
| 2 | HQ135: HMG x1 | HQ176: HMG x1 / HQ29: none | north-to-south order is a guess |
| 3 | HQ176 / HQ29: HMG x1 or none | HQ89: HMG x1 (final); HQ154, HQ172, HQ157: none |  |
| unassigned | - | - | none |

Objective-count note (operator recalls Empire State as 1/2/1 = 4 objectives; the layer has 7 capture points): proposed live set: S1 = CP171 (-608, 62; nearest HQ135 17 m, in the sector marker area), S2 = CP5 (-639, -38) + CP50 (-556, -31), S3 = CP129 (-594, -113). Extras: CP161 (0.9 m from CP50, a duplicate) and CP22 (-652, 33) + CP87 (-649, 78), the outer north flank points, likely another layout's set. Confidence low: CP22/CP87 versus CP171 for the north point cannot be separated from the data, and CP50 versus CP161 is a coin flip.

## Blackwell Fields (MP_BADLANDS)
Direction (operator-confirmed: Pax Armata attacks, samples were recorded from the other side's view): the chain runs west/north-west to east. Attackers start at HQ64 (final base in the forward reading, POLY26@146, no pads); the defenders' final base is the east base POLY10@3 (HQ109, Tank x1, AT x1). The first table below is listed in the old forward order (east to west) and is a spatial inventory only; sector numbers S1 to S3 are reversed for play: sector 1 = Sector@28, sector 2 = Sector@139, sector 3 = Sector@116. The forward per-phase table is superseded. Direction confidence: medium to high (fits all samples).

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Start base (POLY10@3, z -13..136) | none | HQ109 | Tank x1 (143), AntiTank x1 | Attackers during S1 | High |
| S1 = Sector@116, POLY25@108 / POLY5@3 (small boxes 53, 39, 151 are single-CP outlines) | CP1, CP120, CP149 | HQ107 | APC x1 (121), AntiTank x1 | Defenders | Medium |
| S2 = Sector@139, POLY45@45 / POLY33@57 / POLY17@60 / POLY7@2 | CP26 | HQ98 | Tank x1 (157), AntiTank x2 (18, 77), HMG x1 (119) | Defenders | Medium |
| S3 = Sector@28, POLY32@51 / POLY19@63 / POLY9@1 | CP14 | HQ48, HQ135 (POLY13@37, adjacent to S2/S3) | APC x1 (168, POLY13@37) | Defenders (APC168 may also serve attackers after S2 is captured) | Low to medium |
| Final base (POLY26@146) | none | HQ64 | none | Defenders | Medium |

Anomalies:
- APC168 and HQ48/HQ135 sit in POLY13@37, between S2 and S3, and overlap S3's POLY32@51.
- The final base (HQ64) has no spawners.
- The two AntiTank spawners at S1 split between HQ109 and HQ107 by the HQ-group data (loosest assignments on the map, 96-97 m).
- Spawner classes: Tank x2, APC x2, AntiTank x4, HMG x1 (4 vehicle and 5 stationary spawners).

### Per-phase vehicles (attack vs defense) -- SUPERSEDED forward chain, kept for reference only
Built on HQ pad groups. HQs ordered along the chain; the defenders' HQ of phase N flips to the attackers once sector N is captured (HQ pairs at one spot cannot be told apart, so they are marked unresolved).

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ109: Tank x1, AT x1 | HQ107: APC x1, AT x1 |  |
| 2 | HQ107: APC x1, AT x1 | HQ98: Tank x1, AT x2, HMG x1 |  |
| 3 | HQ98: Tank x1, AT x2, HMG x1 | HQ135: APC x1; HQ48: none; HQ64 (final): none | HQ135 is closest to S3 but 96m from its marker |
| unassigned | - | - | none |

### Per-phase vehicles (attack vs defense) -- MAIN (reversed chain)
Operator confirmed Pax attacking, so the reversed chain fits all three samples (none, none, APC x1; "none" is weak evidence). Start HQ64; HQ135/HQ48 are a pair near sector 1/2; final base HQ109.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ64: none | HQ48: none (HQ135 is the pair partner) | matches sample |
| 2 | HQ135: APC x1 | HQ98: Tank x1, AT x2, HMG x1 | matches sample |
| 3 | HQ98: Tank x1, AT x2, HMG x1 | HQ107: APC x1, AT x1 | |
| final | - | HQ109: Tank x1, AT x1 (final base) | |

## Liberation Peak (MP_CAPSTONE)
Direction (fixed by an in-game sample: NATO attackers had Tank x1 + IFV x1 in both sector 1 and sector 2, which only HQ184 and HQ205 match): the chain runs from the west base to the north-east. Attackers start at POLY31@73 (HQ184, outside every box); the defenders' final base is POLY34@215 (HQ2). Confidence: high. Only Sector@48 and Sector@75 are real markers. Sector@46, @94 and @103 sit at the same coordinates as Abbasid Sector@95, @311 and @221 and are stray copies, so sectors 2 to 4 are taken from boxes and have no valid marker.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Start base (POLY31@73) | none | HQ184 | IFV x1 (84), Tank x1 (320) | Attackers during S1 | High (sample) |
| S1 = Sector@75, BOX5 / POLY21@123 | CP304 | HQ205 | IFV x1 (10), Tank x1 (160) | Defenders in S1, attackers in S2 | High (sample) |
| S2 = BOX2 + BOX1 / POLY35@116 (split, no valid marker) | CP3 (BOX2), CP77 (BOX1) | HQ213, HQ263 (same position) | IFV x1 (165), Tank x1 (169) | Defenders | Medium |
| S3 = BOX6 + BOX7 / POLY45@209 (split, no valid marker) | CP51 (BOX6), CP42 (BOX7) | HQ189, HQ272 | IFV x1 (179) | Defenders | Medium |
| S4 = BOX4 / POLY53@144 (no valid marker) | CP155 | HQ246, HQ266 | IFV x1 (290), QuadBike x2 (65, 240) | Defenders | Medium |
| S5 = Sector@48, BOX3 / POLY29@308 | CP41 | HQ188 | IFV x1 (93), LightTransport x1 (235), QuadBike x1 (126) | Defenders | Medium |
| Final base (POLY34@215) | none | HQ2 | IFV x1 (12), LightTransport x1 (185), QuadBike x2 (249, 277) | Defenders | Medium |

Anomalies:
- S2 and S3 are split boxes.
- Sector@46, @94 and @103 are stray markers.
- HQ213 and HQ263 duplicate each other.
- 4 spawner classes: IFV x7, Tank x3, QuadBike x5, LightTransport x2 (17 spawners).

### Per-phase vehicles (attack vs defense)
Note: the in-game sample (NATO attackers Tank x1 + IFV x1 in sectors 1 and 2) forced the west-to-north-east direction used above.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ184: IFV x1, Tank x1 (start base, west) | HQ205: IFV x1, Tank x1 |  |
| 2 | HQ205: IFV x1, Tank x1 | HQ213: IFV x1, Tank x1 / HQ263: none | HQ213 and HQ263 share a position |
| 3 | HQ213 / HQ263 (the one not used by defenders) | HQ189: IFV x1 / HQ272: none | 12 m apart; same ambiguity |
| 4 | HQ189 / HQ272 (the one not used by defenders) | HQ246: IFV x1 / HQ266: Quad x2 | HQ246 and HQ266 are 35 m apart; both could be defenders' HQs |
| 5 | HQ246 / HQ266 (the one not used by defenders) | HQ188: IFV x1, LT x1, Quad x1; HQ2 (final): IFV x1, LT x1, Quad x2 | defenders total IFV x2, LT x2, Quad x3 |
| unassigned | - | - | none |

Patch-note check (1.1.3.0): Sector 3 "Removed Defender tank": agrees, phase 3 defenders (HQ189 IFV x1 / HQ272 none) hold no tank. Sector 5 "Added 2 Attacker IFVs; removed the Defender transport": does not agree with this data. Phase 5 attackers (HQ246 IFV x1 / HQ266 Quad x2) hold at most 1 IFV, and the phase 5 defenders (HQ188, HQ2) still have a LightTransport. No HQ-side or direction change fits both statements (the in-game samples fix the direction), so the data most likely predates the patch, or a later update changed it again. No table change.

Sector-count note (operator remembers 1/2/2/1 objectives, the match log said 5 sectors): the data's 1/2/2/1/1 fits the 5-sector log, so it is kept. The 1/2/2/1 recollection may have merged the last two single-point sectors.

## Manhattan Bridge (MP_DUMBO)
**Chain reversed after the operator's objective count (1/2/2).** The chain runs west to east, NATO (team 1)
attacking: S1 = Sector@243 (CP8), S2 = Sector@73 (CP202, CP9), S3 = Sector@189 (CP176, CP241). Attackers start
at HQ123 in the far west (POLY13@238, no pads), which also fits the sector 1 sample (no attacker vehicles);
the defenders' final base is HQ17 in the east (POLY16@95, IFV x1, LT x1, Quad x1). The original east-to-west
reading (2/2/1) had been chosen because HQ17 is the only end base with vehicle pads; it is kept below for the
box/poly detail, but its sector order and sides are superseded by this table.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S243: CP8) | HQ123: none | HQ24: IFV x1, Quad x2, HMG x1 | sample: no vehicles either side; defenders' pads would need the enabler off, or the match ran a vehicle-less layout |
| 2 (S73: CP202, CP9) | HQ24: IFV x1, Quad x2 | HQ194: AT x1 / HQ93: IFV x1, Quad x2 | pair 55 m apart, unresolved |
| 3 (S189: CP176, CP241) | the one of HQ93/HQ194 not used by defenders (HQ93 gives the attackers an IFV, as 1.1.3.0 notes) | HQ111: IFV x1; final HQ17: IFV x1, LT x1, Quad x1 |  |

Original (superseded) reading: the chain runs from east (x about 200) to west. Attackers start at POLY16@95 (HQ17, outside every sector box), which touches Sector@189's POLY13@235. The defenders' final base is POLY13@238 in the far west (HQ123). Direction confidence: high.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Start base (POLY16@95) | none | HQ17 | IFV x1 (197), LightTransport x1 (234), QuadBike x1 (232) | Attackers during S1 | High |
| S1 = Sector@189, POLY13@235 / POLY10@110, BOX4 + BOX5 (CP outlines) | CP176 (BOX5/206), CP241 (BOX4/122) | HQ111 (BOX4) | IFV x1 (126) | Defenders | Medium |
| S2 = Sector@73, BOX1 / POLY14@98 / POLY18@91 | CP202 (BOX1), CP9 (BOX3) | HQ93, HQ194 | IFV x1 (208), QuadBike x2 (90, 146), AntiTank x1 (25, BOX3) | Defenders | High |
| S3 = Sector@243, POLY15@84 / POLY9@100 / POLY22@193 | CP8 | HQ24 | IFV x1 (141), QuadBike x2 (128, 173), HMG x1 (179) | Defenders | High |
| Final base (POLY13@238) | none | HQ123 | none | Defenders | Medium |

Anomalies:
- Sector@189 and Sector@243 lie in no box; they are in polygons only.
- The final base has no spawners.
- Spawner classes total 5: IFV x4, QuadBike x5, LightTransport x1, AntiTank x1, HMG x1 (10 vehicle and 2 stationary spawners).

### Per-phase vehicles (attack vs defense)
Built on HQ pad groups. HQs ordered along the chain; the defenders' HQ of phase N flips to the attackers once sector N is captured (HQ pairs at one spot cannot be told apart, so they are marked unresolved).

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ17: IFV x1, LT x1, Quad x1 | HQ111: IFV x1 |  |
| 2 | HQ111: IFV x1 | HQ93: IFV x1, Quad x2 / HQ194: AT x1 | HQ93 and HQ194 are 55 m apart; both could be defenders' HQs; HQ93 is closer to Sector@73 |
| 3 | the one of HQ93/HQ194 not used by defenders | HQ24: IFV x1, Quad x2, HMG x1; HQ123 (final): none |  |
| unassigned | - | - | none |

Note: an in-game sample showed no vehicles on either side in Dumbo sector 1; the table above does not match it (possible phase-1 enabler effect).

Patch-note check (1.1.3.0, Manhattan Bridge = MP_DUMBO): "Removed Defender vehicles in Sector 2 and 3; added an Attacker IFV in Sector 3". The pair in phase 2 resolves with the note: HQ194 (AT emplacement only) is the sector 2 defenders' HQ, HQ93 (IFV x1, Quad x2) is the phase 3 attackers' HQ, which gives the sector 3 attackers an IFV (agrees). Sector 3 defenders (HQ24: IFV x1, Quad x2, HMG x1) still hold vehicles in this data, which contradicts the note, so the data likely predates the patch or a later update changed it. Reversing the chain does not help (the sector 2 and 3 defenders would then be HQ94/HQ93 and HQ111/HQ17, all with vehicles). No direction change; table kept with HQ194 = phase 2 defenders, HQ93 = phase 3 attackers.

All sides are inferred spatially; nothing in the data labels teams. Atk = attackers, Def = defenders. Numbers like S191 are Sector marker indices; box/poly numbers are shape indices.

## Eastwood (MP_EASTWOOD)
Chain (med, reversed after in-game sample): west to east, NATO (team1) attacking. Attackers start west at HQ@76 (Tank x1); order S191 -> S151 -> S182; defenders' final base east (HQ@34 IFV+HMG, HQ@164 none). Sample forced the reversal: attackers at sector 2 had TrHeli x1 + IFV x1 = HQ@100 (TrHeli, Cart x2) + HQ@1 (IFV, AT), which both lie between S191 and S151; the old east-to-west chain had only HQ@79 (APC, Cart x2) there. The golf carts are not in the sample (probably not counted). No sector has a box; only polys. 4 CPs for 3 sectors.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (west, poly13) | none | HQ@76 (-335,-68) | Tank x1 (@199) | Atk | Med |
| 1: S191 (poly9/17/168/176) | CP41 (-180,13) | HQ@1 (-96,65) | IFV x1 (@172), AT x1 (@86) | Def | Med |
| 2: S151 (poly3, poly58/122/25) | CP85 (49,42), CP65 (192,-170) | HQ@100 (-42,71), HQ@79 (east side, 77,-31) | HQ@100: TrHeli x1, GolfCart x2; HQ@79: APC x1, GolfCart x2, HMG x1, AT x2 | HQ@1 and HQ@100 Atk (sample); HQ@79 Def | Med |
| 3: S182 (poly1; poly58/122/25) | CP184 (77,-31) | HQ@79 on CP184, HQ@34, HQ@164 | HQ@34: IFV x1, HMG x1 | Atk uses HQ@79 group; Def uses HQ@34 + HQ@164 (none) | Low-Med |

Anomalies: no sector has a box; CP85 sits on the edge of both S151 and S182 polys; 4 CPs for 3 sectors. Operator layout 1/2/1: CP65 (192,-170, near HQ@34) is put in sector 2 with CP85 (S1: CP41; S3: CP184); spatially CP65 sits east of CP184, so this is the operator's recollection overriding position. Totals: VehicleSpawner 9 (Tank1, IFV2, APC1, TransportHeli1, GolfCart4), Stationary 5 (HMG2, AT3). 7 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of their HQ group.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S191) | HQ@76: Tank x1 | HQ@1: IFV x1, AT x1 |  |
| 2 (S151) | HQ@1: IFV x1; HQ@100: TrHeli x1, Cart x2 | HQ@79: APC x1, Cart x2, HMG x1, AT x2 | Matches sample (TrHeli x1 + IFV x1; carts not mentioned) |
| 3 (S182) | HQ@79: APC x1, Cart x2 (HQ@100 may persist) | HQ@34: IFV x1, HMG x1; final HQ@164 none | Low-Med |
| Unassigned |  |  | none |

## Operation Firestorm (MP_FIRESTORM)
Chain (low-med): east to west. Attackers start in the large east base (HQ@158; Quad x2, LightTransport x2, IFV, Tank, TransportHeli, Forward); defenders' final base is HQ@8 in the west (IFV+Tank), outside all sector boxes. Order S103 -> S196 -> S216 -> west base.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (east, poly40) | none | HQ@158 (375,-118) | Tank x1 (@214), IFV x1 (@187), LightTransport x2, QuadBike x2, TransportHeli x1 (@197), Forward x1 (@140) | Atk | Med |
| 1: S103 (boxes 153,4) | CP164 | HQ@163 | IFV x1 (@44), Tank x1 (@47), Forward x1 (@229) | Def | Med |
| 2: S196 (box1; box169 sub-area) | CP233, CP243 (box151/3 outside box1, in poly32) | HQ@54, HQ@170 | IFV x2 (@198,@206), Tank x1 (@120) | Def (Atk later) | Med |
| 3: S216 (box2) | CP87 | HQ@93 | IFV x1 (@48), Tank x1 (@179) | Def | Med |
| Def final base (west, poly190) | none | HQ@8 | IFV x1 (@18), Tank x1 (@36) | Def (last phase/after S216) | Low-Med |

Anomalies: CP243 lies in its own boxes 151/3, outside S196's box1 (assigned by polygon 32); direction is a guess because both ends have IFV+Tank; Forward@229 is inside the S103 box and could serve attackers once S103 falls. Totals: VehicleSpawner 16 (IFV6, Tank5, Quad2, LightTransport2, TransportHeli1) + Forward 2. 6 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of the HQ group they belong to.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S103) | HQ@158: Tank x1, IFV x1, LT x2, Quad x2, TrHeli x1, Fwd x1 | HQ@163: IFV x1, Tank x1, Fwd x1 |  |
| 2 (S196) | HQ@163: IFV x1, Tank x1, Fwd x1 | HQ@54: Tank x1, IFV x2; HQ@170 none | HQ@54/@170 are a pair 6 m apart |
| 3 (S216) | HQ@54: Tank x1, IFV x2; HQ@170 none | HQ@93: IFV x1, Tank x1; final HQ@8: IFV x1, Tank x1 | Defenders total IFV x2, Tank x2 |
| Unassigned |  |  | none |

### Patch-note check (1.1.3.0)

Operation Firestorm. Sector 2 "adjusted defender armour": consistent (defenders hold HQ@54 Tank x1, IFV x2; no contradiction). Sector 3 "added 2 Attacker tanks and 1 Attacker IFV; removed the Defender tank": does NOT fit cleanly. The sector 3 attackers' group (HQ@54: Tank x1, IFV x2) has one tank, and the sector 3 defenders still hold Tank x2 (HQ@93 + final HQ@8). No single HQ group has Tank x2 + IFV x1, and reversing the chain (west to east) does not produce one either (attackers' sector 3 would still be HQ@54). Direction and sides left unchanged; the extracted layer probably reflects a different build than 1.1.3.0 (later updates), so the notes are not forcing a change here.

## New Sobek City (MP_OUTSKIRTS)
Chain (low-med, revised for in-game sample): west to east, NATO (team1) attacking, 3 sectors in-game. Merge: S15 (-26,-84) is folded into S207 (-129,-131) as sector 1; operator layout 2/1/2 (5 of the 6 layer CPs): sector 1 = CP18 + CP144, sector 2 = S175 with CP109 only, sector 3 = S131 with CP122 + CP103. Odd one out: CP177 (-142,-168), isolated in its own box150, 76 m from CP18 and far south of the chain line, so probably unused in the live layout; CP109 stays in S175 because it is 5 m from HQ@156 (the Quad group) while CP103 (61,-98) lies 44 m from the S175 marker and toward S131. Low-Med confidence. Attackers start west (HQ@56: Fwd2, IFV, LT); defenders' final base east (HQ@71: LT + IFV; HQ@152 empty). Sample: Pax defenders sector 2 Quad x1 = HQ@156 exactly, sector 3 LT x1 + IFV x1 = HQ@71 exactly; sector 1 "none" is weak evidence (HQ@46, HQ@73, HQ@94 hold APC, LT x2, IFV in that area, so they were probably taken or not all enabled). East-to-west was tested and fits worse (LT count and extras do not match).

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (poly146) | none | HQ@56 | Forward x2 (@158,@167), IFV x1 (@166), LightTransport x1 (@190) | Atk | Med |
| 1: S207 + S15 merged (box2, poly216; poly184/212/215/3) | CP18, CP144 (CP177 box150 dropped as unused) | HQ@46, HQ@73, HQ@94 | APC x1 (@194), HMG x2, AT x2, IFV x1 (@105), LightTransport x2 (@135,@219) | Def | Low-Med |
| 2: S175 (poly126/140/1) | CP109 | HQ@156, HQ@157 | QuadBike x1 (@57), HMG x1 (@33), AT x1 (@77) | Def | Med |
| 3: S131 (poly30 only) | CP122, CP103 | HQ@152 (205,-158), final HQ@71 | HQ@71: LightTransport x1 (@61), IFV x1 (@133); HQ@152 none | Def | Med |

Anomalies: only S207 has a box; S131 has no sub-polygon and no pads; the HQ@71 base is about 92 m from S175. Totals: VehicleSpawner 9 (Quad1, LightTransport4, IFV3, APC1) + Forward 2 + Stationary 6 (HMG3, AT3). 7 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of their HQ group.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S207+S15) | HQ@56: Fwd x2, IFV x1, LT x1 | HQ@46: APC x1, HMG x2, AT x1; HQ@73: LT x2, AT x1; HQ@94: IFV x1 | Sample "none" weak; if only part is enabled, defenders hold a subset |
| 2 (S175) | HQ@46/@73/@94 set (same vehicles) | HQ@156: Quad x1; HQ@157: HMG x1, AT x1 | Matches sample Quad x1 |
| 3 (S131) | HQ@156: Quad x1 | HQ@152 none; final HQ@71: LT x1, IFV x1 | Matches sample LT x1 + IFV x1 |
| Unassigned |  |  | none |

### Patch-note check (1.1.3.0)

New Sobek City. The extracted layer has no Tank pads at all (only Quad, LT, IFV, APC), so "Sector 2: added 1 Defender tank and IFV" and "Sector 3: removed Defender tank and LT" cannot be reproduced from this data. The in-game sample (defenders sector 2 Quad x1, sector 3 LT x1 + IFV x1) matches the HQ groups exactly (HQ@156, HQ@71), so a later update has superseded those notes (reading A: notes are older than the build; reading B, a different sector numbering, also fails because no HQ group holds a tank). Table unchanged; the sample is trusted over the notes.

## Vegas Strip (MP_PARADISE)
Attackers = Pax Armata (team1). Chain (med): north to south, 3 sectors confirmed in-game. Attackers start in the north base (HQ@32, z=422-499, outside all sector shapes). Order S27 -> S23 -> S51 (S59 dropped).

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (north, poly20/105) | none | HQ@32 | APC x1 (@41), Tank x1 (@62), DirtBike x1 (@112), LightTransport x1 (@113) | Atk | Med-High |
| 1: S27 (box54; poly7/136/156) | CP48, CP124 (boxes 1,44) | HQ@28 | IFV x1 (@43), APC x1 (@125) | Def | Med |
| 2: S23 (poly81/123/26) | CP24, CP114 (z=-25), CP38, CP133 | HQ@116 (south edge), HQ@8, HQ@47 (north staging block z 108-172) | staging block: LightTransport x1 (@4), APC x1 (@15), IFV x1 (@131), Forward x1 (@87) | HQ@47 block (LT, APC, IFV, Fwd) serves phase 2 defenders and phase 3 attackers per the in-game sample; HQ@8/HQ@116 have no pads | Low-Med |
| 3: S51 (poly135, south) | none | HQ@115, HQ@137 | APC x2 (@39,@61), IFV x2 (@84,@155) | Def (south end, reads like a final base) | Med |

Anomalies: dropped S59, CP103, HQ@144 (and HQ@100) sit at y=226 versus y~50 elsewhere and have no pads; S51's polygon has no CP; S23 holds 4 CPs. 7 CPs total. Totals: VehicleSpawner 13 (APC5, IFV4, LightTransport2, Tank1, DirtBike1) + Forward 1. 6 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of the HQ group they belong to.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S27) | HQ@32: APC x1, Tank x1, Dirt x1, LT x1 | HQ@28: IFV x1, APC x1 | Sample: defenders sector 1 IFV (APC not listed in sample) |
| 2 (S23) | HQ@28: IFV x1, APC x1 | HQ@47: LT x1, IFV x1, APC x1, Fwd x1 | Sample: attackers IFV+APC matches HQ@28 exactly; defenders APC (LTV) + IFV is a subset of HQ@47. HQ@8 and HQ@116 (none) sit at S23 CPs |
| 3 (S51) | HQ@47: LT x1, IFV x1, APC x1, Fwd x1 | HQ@137: APC x2, IFV x1; final HQ@115: IFV x1 | Defenders total APC x2, IFV x2; direction north to south; S59 dropped |
| Unassigned |  |  | HQ@8, HQ@116, HQ@100, HQ@144: all none (HQ@144 belonged to dropped S59) |

## Cairo Bazaar (MP_PLAZA)
Attackers = Pax Armata (team1). Chain (med): south to north. Attackers start in the south base (poly42/46: HQ@147, IFV@99, outside sector shapes); the north HQ@50 (poly109, no spawners) is the defenders' last base. Order S182 -> S56 -> S143.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (south) | none | HQ@147 (-62,-71) | IFV x1 (@99) | Atk | Med |
| 1: S182 (poly91/127/156) | CP177, CP40 | HQ@52 | none | Def | Med |
| 2: S56 (-182,-4, no polys; stray marker) | CP162, CP90 (poly48/126/139, assigned by elimination) | HQ@158 | IFV x1 (@112), HMG x2 (@74,@80), AT x1 (@142) | Def | Low |
| 3: S143 (poly138/183) | CP2, CP93 | HQ@10, HQ@31, HQ@113 | HMG x1 (@35), AT x2 (@58,@181) | Def | Med |
| Def final base (north) | none | HQ@50 (150,231) | none | Def | Low |

Anomalies: S56 (-182.4, 66.6, -3.9) is identical to Eastwood S191 and lies outside the other sectors' x range, so it is probably a displaced marker; the HQ@158 pad group sits between S182 and S143 and is assigned to the middle phase. Totals: VehicleSpawner 2 (IFV2) + Stationary 6 (HMG3, AT3). 3 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of their HQ group.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S182) | HQ@147: IFV x1 | HQ@52: none | Start IFV is HQ@147 (south); matches sample IFV x1 |
| 2 (S56 middle) | HQ@52: none | HQ@158: IFV x1, HMG x2, AT x1 | Matches sample: attackers none; HQ@158 group moves to defenders here |
| 3 (S143) | HQ@158: IFV x1 (HMG/AT emplacements stay defender assets) | HQ@113 none, HQ@31: HMG x1, AT x1, HQ@10: AT x1, final HQ@50 none | Defenders total HMG x1, AT x2 |
| Unassigned |  |  | none |

Sample note (Cairo Bazaar): attackers sector 1 = IFV x1, sector 2 = none; this forced the start IFV onto HQ@147 and the HQ@158 IFV group onto the sector 2 defenders. Direction stays south to north.

## Hagental Base (MP_SUBSURFACE)
No vehicle spawners at all (HQ/CP only). Direction undetermined; listed west to east (arbitrary). 6 Sector markers form 4 sectors (operator layout 2/1/1/2): S1 = S145 (CP73, CP57), S2 = S147 (CP70), S3 = S53+S84 merged (CP138), S4 = S105+S193 merged (CP135, CP66); the chain ends with the 2-point sector.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| S145 (box1; poly60/188/199) | CP73, CP57 (poly5/208, west) | HQ@92 | none | n/a | n/a |
| S147 (poly69/196/3) | CP70 | HQ@110, HQ@16 | none | n/a | n/a |
| S53 (boxes 174,2) + S84 (box2) | CP138 | HQ@68, HQ@80, HQ@120 | none | n/a | n/a |
| S105 (box8) + S193 (poly131/4) | CP135, CP66 | HQ@48 | none | n/a | n/a |
| Outer HQs | none | HQ@180 (-260,107) west, HQ@116 (273,-127) east | none | candidate start bases, side unknown | Low |

Anomalies: S53+S84 share box2 and S105+S193 share poly131 (split or duplicate markers). Totals: 0 spawner classes.

### Per-phase vehicles (attack vs defense)

No vehicle spawners.

## Mirak Valley (MP_TUNGSTEN)
Chain (low-med): west to east. Attackers start west (HQ@39, LightTransport+Tank+IFV); defenders' final base east (HQ@199, Tank+IFV). Both ends are nearly equal, so direction is a guess. Operator layout 2/2/2 with 3 sectors: S75 and S139 are merged into one middle sector. Order S217 -> S75+S139 -> S32.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (poly224) | none | HQ@39 | Tank x1 (@137), IFV x1 (@281), LightTransport x1 (@5) | Atk | Med |
| 1: S217 (poly13; box6 sub-area) | CP71 (box6), CP186 (box5) | HQ@218 | Tank x1 (@80), IFV x1 (@196) | Def | Med |
| 2: S75 + S139 merged (box1, poly322) | CP311, CP178 (boxes 179,4) | HQ@116, HQ@312 | LightTransport x2 (@131, @271), IFV x1 (@215), Tank x1 (@328) | Def | Med |
| 3: S32 (poly266) | CP23 (box3), CP287 (box2) | HQ@110 | Tank x1 (@25), IFV x1 (@30) | Def | Med |
| Def final base (east, poly295) | none | HQ@199 | Tank x1 (@214), IFV x1 (@298) | Def (or Atk if reversed) | Low |

Anomalies: S75 and S139 share poly322; every sector has spawners. Totals: VehicleSpawner 13 (Tank5, IFV5, LightTransport3). 3 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of the HQ group they belong to.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S217) | HQ@39: Tank x1, IFV x1, LT x1 | HQ@218: Tank x1, IFV x1 | Direction low confidence |
| 2 (S75+S139) | HQ@218: Tank x1, IFV x1 | HQ@116: LT x2; HQ@312: IFV x1, Tank x1 | Merged sector; both defender HQs in one phase |
| 3 (S32) | HQ@116: LT x2; HQ@312: IFV x1, Tank x1 | HQ@110: Tank x1, IFV x1; final HQ@199: Tank x1, IFV x1 | Defenders total Tank x2, IFV x2 |
| Unassigned |  |  | none |

### Patch-note check (1.1.3.0)

The Mirak Valley notes (all pads attackers', sector 1 attackers Tank x2 + IFV x1, sectors 2 and 3 an IFV each) could not be matched to a map: Mirak Valley is not identified among the maps in this batch, and MP_TUNGSTEN (4 sectors, no HQ group with Tank x2 + IFV x1, LT x2 at HQ@116) does not fit. No change made.

Abbrev: LT = LightTransport, Dirt/Quad = PTV_DirtBike/QuadBike. Grouping is by HQ pad group (bt-hq-groups.txt); HMG/AT/AA are emplacements counted with the nearest HQ. The earlier area-based sector tables were removed because they disagreed with the HQ groups.

## Contaminated (MP_CONTAMINATED)
Chain runs SE to NW: start HQ@209 (SE, x~440), final HQ@368 (NW, no pads). Team1 = Alliance/NATO attackers. In-game it has 5 sectors, so Sector@377 and @277 (20 m apart) are one sector: S1 Sector@226 (CP@183), S2 Sector@181 (CP@52, @82), S3 Sector@377/@277 (CP@452, @75, @309), S4 Sector@180 (CP@231, @351), S5 Sector@9 (CP@228). Totals: 23 vehicle pads (Dirt 8, LT 6, Tank 4, APC 3, IFV 2) and 9 emplacements (HMG 3, AT 6); no pads outside every poly. Direction: medium-high.

### Per-phase vehicles (attack vs defense)

Sample: Pax defenders at sector 2 had Dirt 1 + LT 2 only. No single HQ holds that (HQ@210 Dirt 1; HQ@155 LT 2 with Tank 1, IFV 1, AT 1). It is a subset only of the union HQ@210 + HQ@155, so it exceeds any single group: either the S3 HQ@155 is live for defenders in phase 2 or the LT pads belong to another HQ. Needs an in-game check.

| Phase | Attackers' HQ (index) and vehicles | Defenders' HQ (index) and vehicles | Note |
|---|---|---|---|
| 1 | HQ@209 (start): LT 1, APC 1, Tank 1, Dirt 1 | HQ@97: Tank 1, APC 1, Dirt 2, AT 2 | |
| 2 | HQ@97: Tank 1, APC 1, Dirt 2 | HQ@210: Dirt 1 | sample Dirt 1 + LT 2 exceeds the group (fits only HQ@210 + HQ@155 together): error vs model |
| 3 | HQ@390: LT 1, APC 1, HMG 1, AT 1 | HQ@155 + HQ@262: Tank 1, LT 3, IFV 1, Dirt 2, AT 1, HMG 1 | HQ@390 vs HQ@443 as attackers is arbitrary: both lie on the Sector@181 side (56 m and 31 m) and the model has no rule to pick; HQ@443 (Dirt 2, Tank 1, AT 1) listed unassigned |
| 4 | HQ@155 + HQ@262 (handed over): Tank 1, LT 3, IFV 1, Dirt 2, AT 1, HMG 1 | HQ@98: LT 1 | |
| 5 | HQ@98: LT 1 | HQ@8: IFV 1, HMG 1, AT 1; final HQ@368: none | |
| Unassigned | HQ@443: Dirt 2, Tank 1, AT 1; HQ@47, HQ@256: none | | |

### Capture-point layouts (operator 1/2/2/1 vs log 5 sectors)

Positions (x,z): CP@183 (264,211); CP@52 (109,183); CP@82 (154,89); CP@75 (25,99); CP@452 (-4,57); CP@309 (-27,39); CP@231 (-138,-17); CP@351 (-89,-118); CP@228 (-141,-252). Near-duplicates: CP@452 and CP@309 are 33 m apart and each sits on one of the two merged markers (Sector@377 exact, Sector@277 within 9 m); CP@75 is ~50 m from CP@452 and has its own box7 with HQ@155 at 13 m. CP@351 has its own box (253/5) and poly with HQ@47 but no Sector marker, 120-135 m from its neighbours CP@231 and CP@228. The current table (1/2/3/2/1) is unchanged.
- 4-sector reading (1/2/2/1, 6 points): CP@183 | CP@52, CP@82 | CP@75, CP@309 | CP@228. Extras: CP@452 (duplicate of CP@309's site), CP@231 and CP@351 (the Sector@180 pair, whose HQ@98 has only LT 1). Low confidence; which of the middle trio is dropped is arbitrary.
- 5-sector reading (1/2/2/2/1, 8 points): CP@183 | CP@52, CP@82 | CP@75, CP@309 | CP@231, CP@351 | CP@228. Extra: CP@452 only (one of the near-duplicate pair; CP@309 could be dropped instead). Medium confidence; this matches the log with 8 of the 9 points.

## Tsuru Reef (MP_ISOLATED)
Chain runs S to N (Sector@188, @36, @168, @169; z -219 to 413), start HQ@150 (poly310), final HQ@133 (poly155). Team1 = Coalition/Pax Armata attackers. Direction is settled by the Tsuru Reef samples (medium-high). Totals: 42 vehicle pads (LT, Quad, RHIB, Dirt, APC, IFV, PatrolBoat) and 2 emplacements (HMG, AT). S4 (Sector@169) has HQ@336 (LT 2, Dirt 1, Quad 1, HMG 1) beside it, plus the final HQ@133.

### Per-phase vehicles (attack vs defense)

Samples (Pax attacking): S1 attackers APC 1, LT 1, RHIB 2, Quad 2, Dirt 2; S2 attackers APC 1, LT 1, RHIB 2, Quad 2. S2 is a subset of HQ@316 (RHIB 3). S1 matches HQ@150 except Dirt (sample 2 vs group 1): the extra dirt bike is not covered by HQ@150, and HQ@316 has none, so its source is unknown (error vs model).

| Phase | Attackers' HQ (index) and vehicles | Defenders' HQ (index) and vehicles | Note |
|---|---|---|---|
| 1 | HQ@150 (start): RHIB 2, Dirt 1, Quad 2, APC 1, LT 1 | HQ@316: Quad 2, RHIB 3, LT 1, APC 1 | sample Dirt 2 exceeds HQ@150 Dirt 1; source of second dirt bike unknown |
| 2 | HQ@316: Quad 2, RHIB 3, LT 1, APC 1 | HQ@3: LT 1, RHIB 1, Quad 2, Dirt 1 | |
| 3 | HQ@132: LT 2, Quad 1, Dirt 1 | HQ@76 + HQ@31: LT 2, RHIB 2, Quad 2, IFV 1, PatrolBoat 1 (HQ@76: LT 1, RHIB 1, Quad 1; HQ@31: LT 1, IFV 1, PatrolBoat 1, Quad 1, RHIB 1) | handover breaks after phase 2 (HQ@3 is not reused): HQ@132 and HQ@76 both lie between S2 and S3, HQ@31 (38 m from CP@338) is on S3's defender side, so it is a plausible phase-3 defender as well as the phase-4 attacker |
| 4 | HQ@31: LT 1, IFV 1, PatrolBoat 1, Quad 1, RHIB 1 | HQ@336: LT 2, Dirt 1, Quad 1, HMG 1; final HQ@133: LT 1, RHIB 2, PatrolBoat 1, IFV 1, Quad 2, AT 1 | final base joins in last phase |
| Unassigned | none | | all 8 HQs used |

### Patch-note check (1.4.3.0)

Capture points per sector in the chain from MP_ISOLATED.txt: S1 Sector@188 has 2 (CP@217, @246), S2 Sector@36 has 2 (CP@134, @272), S3 Sector@168 has 2 (CP@97, @338), S4 Sector@169 has 1 (CP@45); 7 total. The chain is unchanged by this check.
- S1: agrees. Attackers HQ@150 has APC 1 (and RHIB 2, matching the 2 added RHIBs); 2 capture points (A and B). HQ@150 still lists LT 1 beside the APC, which the notes do not explain (it could be a second LT pad).
- S2: agrees. Attackers HQ@316 has APC 1; defenders HQ@3 has Quad 2; 2 capture points. HQ@3 still has LT 1.
- S3: agrees, with a caveat. Attackers HQ@132 has LT 2 and no APC; defenders HQ@76 + HQ@31 have no APC. The data shows 2 capture points, which fits an added point only if the old S3 had 1; 3 would make 8 total against the 7 in the file, so 2 is the supported count.
- S4: agrees. 1 capture point (CP@45); defenders HQ@336 and HQ@133 have no APC.

## Railway to Golmud (MP_GOLMUDRAILWAY)
Chain runs S to N, confirmed 4 sectors in-game, NATO attacking (default factions): start HQ@269 (south), S1 CP@71/@99 (HQ@271, Sector@267), S2 CP@301/@212 (HQ@111), S3 CP@158 (HQ@48), S4 CP@321/@348 (HQ@306), final HQ@154. Sector@272 and @280 sit at the attackers' start (HQ@269) and Sector@89 is a stray; none is a chain sector. Totals: 51 vehicle pads (including the two stray-position AttackPlane pads, which belong to HQ@269, and a dummy IFV at 0,0,0 from Breakthrough_Cover) and 6 emplacements (HMG 2, AT 3, AA 1): 11 spawner classes.

### Per-phase vehicles (attack vs defense)

| Phase | Attackers' HQ (index) and vehicles | Defenders' HQ (index) and vehicles | Note |
|---|---|---|---|
| 1 | HQ@269 (start, south): LT 2, APC 1, Dirt 2, IFV 2, Tank 1, AtkPlane 2 | HQ@271: APC 2, Dirt 2, LT 1, Tank 2, ScoutHeli 1 | HQ@271 is on Sector@267 |
| 2 | HQ@271: APC 2, Dirt 2, LT 1, Tank 2, ScoutHeli 1, plus AtkPlane 1 from HQ@269 | HQ@111 (HQ@261 twin has no pads): Dirt 2, Tank 1, AA 1, ScoutHeli 1, APC 1, Quad 2, IFV 2, LT 4, AT 1 | sample exceeds HQ@271 by AtkPlane 1: the start HQ's plane pads stay live at sector 2 (deviation from the model). Defenders' sample (Dirt 2, LT 1, Tank 1, IFV 1) is a subset of HQ@111. Medium |
| 3 | HQ@111: as above | HQ@48 (HQ@328 twin none): APC 1, Dirt 5, IFV 3, LT 1, Tank 1, HMG 1 | |
| 4 | HQ@48: as above | HQ@306: Quad 2, Dirt 1, IFV 1, HMG 1; final HQ@154: IFV 2, Dirt 1, LT 2, AT 2 | final base joins in last phase |
| Unassigned | HQ@328, HQ@261: none | | duplicate twins at the same position as HQ@48 and HQ@111; AttackPlane @177/@257 (z -664/-789) are in HQ@269's group (maxdist 911 m) |

Class abbreviations: LT = LightTransport, PB = PatrolBoat, RHIB, Quad = PTV_QuadBike, Dirt = PTV_DirtBike, Tank, IFV, APC, AtkHeli, TrHeli, MobAA, Fwd = VehicleSpawner_Forward. Indices are the `@` instance indices.

## Wake Island (MP_ATOLL)
Chain direction (inferred, low-medium confidence, 5 sectors, adopted from review-D.md and checked against the three in-game samples): attackers start on the carrier (HQ@198) -> Sector@404+@30 merged (defenders @347) -> Sector@7 (HQs @506+@185) -> Sector@178 (HQs @255+@207+@267) -> Sector@157 (no HQ) -> Sector@137 (final, HQs @120/@49/@38). Sector@30 is merged into @404 (95 m apart, CP@82 is 104 m from @347, no HQ or pads of its own). Weak point: the Sector@7 -> Sector@178 leg (about 620 m) is untested by any sample.

Anomalies:
- No Sector marker has a BOX (boxes=[] for all 6). Sector areas were taken from POLYs: 7=POLY@5/45/285/511, 30=POLY@9, 404=POLY@6/28, 178=POLY@2/8 + BOX@395, 157=POLY@3/474, 137=POLY@4/20/7.
- Sector 157 has no HQ (only 2 LT, 1 HMG, 1 AT). Sector 30 has no HQ and only one AntiTank.
- Sector 178 is split: BOX@395 (CP@33, HQ@207/267) and POLY@8 (CP@394, HQ@255).
- Water spawners in shared polys (121/234/257/271) are assigned by nearest sector; low confidence.
- No carrier-jet pads exist in this file; @198 is the carrier (HQ and TrHeli pads at y=115 against sea level 98).
- Totals: 102 VehicleSpawner + 6 StationarySpawner accounted for in the area table below.

Area table (pads grouped by area; use the HQ-group table further down for sides and phase sets):

| Area | Capture points | HQs | Vehicle spawners (class x count) | Likely side | Confidence |
|---|---|---|---|---|---|
| West base (BOX@392, poly 285) | none | @185 | LT x4, Quad x1, Tank x1, PB x4, RHIB x2 = 12 | Defenders of Sector@7 (with @506); attackers in phase 3 once @7 falls | Medium |
| Sector@7 (POLY@5/45/511) | @262, @59 | @506 | LT x3, Quad x1, Tank x1, IFV x1, PB x6 = 12 | Defenders phase 2; attackers phase 3 | Medium |
| Sector@30 (POLY@9) | @82 | none | none; AT x1 (@379) | Merged into @404 (phase 1) | Low |
| Sector@404 (POLY@6/28/121) | @324 | @347 | LT x5, IFV x1, PB x5, RHIB x1 = 12 (area count with pool boats is 13); HMG x1 (@424) | Defenders phase 1; attackers phase 2 | Medium |
| Sector@178 (BOX@395 + POLY@8/2) | @33, @394 | @207, @267, @255 | LT x9, Tank x2, IFV x1, Quad x1, PB x6, RHIB x5 = 24 | Defenders phase 3; attackers phase 4 | Medium |
| Sector@157 (POLY@3/474, BOX@52) | @326, @369 | none | LT x2; HMG x1, AT x1 | Defenders phase 4 (no HQ; pads unclear) | Low |
| Sector@137 (POLY@4/20/7, final) | @367, @220, @441 | @38, @49, @120, @246, @344 | LT x11, Quad x1, Tank x2, IFV x1, PB x3, RHIB x4 = 22; AA x1, AT x1 | Defenders phase 5 | Medium |
| Carrier / naval (BOX@479/483, outside sectors) | none | @198 | PB x6, RHIB x9, TrHeli x2 = 17 | Attackers phase 1 (start) | High (sample 1) |

Area counts and HQ-group counts differ slightly (areas use polys, HQ groups use the nearest HQ); the per-phase sets below use HQ groups.

### Per-phase vehicles (attack vs defense)

Sample check on the adopted chain (all subsets):
- Sample 1 (TrHeli x2, RHIB x9, PB x4) is a subset of @198 only (PB 4 of 6): phase 1 attackers.
- Sample 3 (Tank x1, RHIB x2, PB x3, LT x3) is a subset of @506+@185 (LT 7, Tank 2, PB 10, RHIB 2): phase 3 attackers, so @185 and @506 land at phase 3 as attackers (after Sector@7 falls) and at phase 2 as defenders.
- Sample 4 (Quad x1, RHIB x1, LT x3, PB x3, Tank x1, IFV x1) is a subset of @255+@207+@267 (LT 9, Tank 2, IFV 1, Quad 1, PB 7, RHIB 5): phase 4 attackers. No single HQ holds it (@506 lacks RHIB), so the earlier "@506 at phase 4" claim was wrong.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (Sector@404+@30) | @198 (carrier): PB x6, RHIB x9, TrHeli x2 | @347: LT x5, IFV x1, PB x5, RHIB x1, AT x1, HMG x1 | Sample 1 subset |
| 2 (Sector@7) | @347: LT x5, IFV x1, PB x5, RHIB x1, AT x1, HMG x1 | @506+@185: LT x7, Quad x2, Tank x2, IFV x1, PB x10, RHIB x2 | No sample |
| 3 (Sector@178) | @506+@185: LT x7, Quad x2, Tank x2, IFV x1, PB x10, RHIB x2 | @255+@207+@267: LT x9, Tank x2, IFV x1, Quad x1, PB x7, RHIB x5, AT x1, HMG x1 | Sample 3 subset (attackers) |
| 4 (Sector@157) | @255+@207+@267: LT x9, Tank x2, IFV x1, Quad x1, PB x7, RHIB x5, AT x1, HMG x1 | none at Sector@157; @49 (LT x8, Tank x2, Quad x1) is the nearest on the defenders' side, low confidence | Sample 4 subset (attackers) |
| 5 (Sector@137, last) | @255 group (or @49 if captured earlier) | @120+@49+@38: LT x13, Tank x2, Quad x1, IFV x1, PB x3, RHIB x4, AA x1, AT x1 | Final; no sample |
| Unassigned | @246, @344 (0 pads) | | |

## Area 51 (MP_DRYLAKE)
Chain direction (inferred, east to west, forced by the in-game attackers' sample 1 = HQ@96 exactly): attackers start at the east base (HQ@96, BOX@141, with the only usable Sector marker @166); the final defenders' HQ is @236 at the far west (with 2 AutomaticAA).

Anomalies:
- Sector@82, @89, @149 sit at about (-82..128, z 0..-38), far from the map (z 800-1200), in no box or poly. Positions unusable, so sectors were derived from the CP/HQ clusters.
- The east box BOX@141 holds Sector@166 plus the start base (HQ, 4 Fwd spawners) and no capture point.
- Spawners: 70 VehicleSpawner = W 8 + A 8 + B 20 + C 17 + D 10 + E 7; plus 4 Fwd, 5 StationarySpawner, 2 AutomaticAA.

Area table (by polygon; sides follow the east-to-west chain):

| Phase/Sector | Capture points | HQs | Vehicle spawners (class x count) | Likely side | Confidence |
|---|---|---|---|---|---|
| East base BOX@141 (Sector@166) | none | @96 | LT x2, Dirt x2, APC x1, Tank x1, TrHeli x1 = 7; Fwd x4 | Attackers' start (phase 1) | High (sample 1) |
| S1 Area D (POLY@12/71/104) | @266, @29 | @46 | LT x3, Dirt x2, Quad x2, APC x1, Tank x1, AtkHeli x1 = 10 | Defenders phase 1; attackers phase 2 | Medium |
| S2 Area C (POLY@35/203) | @209, @126 | @118, @232 | LT x5, Dirt x6, IFV x2, Tank x1, AtkHeli x1, TrHeli x1, Quad x1 = 17 | Defenders phase 2 (@118); attackers phase 3 (@118+@232) | Medium |
| S3 Area B (POLY@157/142) | @193, @39, @168 | @112, @173, @190 | LT x6, Dirt x6, Quad x2, Tank x2, IFV x1, APC x1, MobAA x1, TrHeli x1 = 20 | Defenders phase 3 (@112) | Low-medium |
| S4 Area A (POLY@28/163/251) | @66 | @42 | LT x3, Tank x1, AtkHeli x1, IFV x1, Dirt x2 = 8; HMG x3, AT x2 | Attackers phase 4 (@42 group); emplacements stay behind | Medium |
| West base (POLY@61/251) | none | @236 | LT x2, Tank x1, AtkHeli x1, Quad x2, Dirt x2 = 8; AutoAA x2 | Defenders' final base (phase 4) | Medium |

### Per-phase vehicles (attack vs defense)

HQ-group based. The in-game sample forces the chain to run east to west: attackers at sector 1 (TrHeli, Tank, APC, 2 LT, 2 Dirt) equals exactly the HQ@96 group (excluding its 4 Fwd pads), so HQ@96 is the attackers' start and this replaces my earlier west-to-east guess. Sectors (east to west): S1 = CP@266/@29 (HQ@46), S2 = CP@209/@126 (HQ@118/@232), S3 = CP@193/@39/@168 (HQ@112/@173/@190), S4 = CP@66 (HQ@42), final HQ@236 at the far west.

In-game samples: attackers at sector 1 = HQ@96 (exact). Attackers at a later sector = exactly HQ@42 (AtkHeli, Tank, IFV, 3 LT, 2 Dirt); it lands at phase 4 (HQ@42 is the HQ between S3 and S4), so the log's "3" lands at phase 4. The operator was unsure of that number; "3 sectors captured" is only an assumption. Defenders at sector 2 (4 Dirt, LT, IFV, TrHeli) fit HQ@118 as a subset (Dirt x5); HQ@173 has only Dirt x3 so does not strictly fit.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S1: CP@266/@29) | @96 (start): Dirt x2, APC x1, LT x2, Tank x1, TrHeli x1, Fwd x4 | @46: Dirt x2, Quad x2, APC x1, LT x3, Tank x1, AtkHeli x1 | Attackers match in-game sample 1 exactly (Fwd not in sample) |
| 2 (S2: CP@209/@126) | @46: Dirt x2, Quad x2, APC x1, LT x3, Tank x1, AtkHeli x1 | @118: LT x3, AtkHeli x1, Dirt x5, TrHeli x1, IFV x1 | Defenders match in-game sample as a subset; @46 plays defenders in phase 1 and attackers here |
| 3 (S3: CP@193/@39; CP@168 unused) | @118+@232: LT x4, AtkHeli x1, Dirt x5, TrHeli x1, IFV x1, Tank x1 | @42: HMG x3, AT x2, LT x3, AtkHeli x1, Tank x1, Dirt x2, IFV x1 | Operator screenshot (sector 3, NATO attacking, M3A3 Bradley in hand): attackers' HQ lies beyond A on the attackers' side and the defenders' HQ well beyond B, past both objectives, so the defenders' HQ is @42 (x -23), not @112/@173 (x 150-160, which sit on objective A = CP@193). Screen x is mirrored against data x. @42 then flips to the attackers for phase 4. The logged "3" attackers' sample (AtkHeli, Tank, IFV, LT x3, Dirt x2) is a subset of @118+@232 |
| 4 (S4: CP@66, last) | @190: LT x1, IFV x1, Quad x1, MobAA x1, Tank x1, Dirt x1 (plus @42 minus its AtkHeli: HMG x3, AT x2, LT x3, Tank x1, Dirt x2, IFV x1) | @236 (final): LT x2, Tank x1, AtkHeli x1, AutoAA x2, Quad x2, Dirt x2 | Community report (Discord, 19 Oct): attackers get a mobile AA in the last sector and no attack helicopter. @190 holds the map's only MobAA pad, so it is the last-sector attackers' group; @42's AtkHeli pad must be disabled (enabler) or belong to another layout. The logged "3" sample (AtkHeli, Tank, IFV, LT x3, Dirt x2) is a subset of the phase 3 attackers' @118+@232, so it was sector 3 after all |
| Unassigned | @112: Dirt x3, LT x3, Quad x2, Tank x1, APC x1; @173: IFV x1, Dirt x3, LT x3, TrHeli x1 | | @112 and @173 (10 m apart) sit on objective A of sector 3; after the screenshot they are not the sector 3 defenders' HQ, so they are a second layout's pair or a forward HQ |

Community report (Discord, 19 Oct) also says the defenders get no attack helicopter in sectors 1 or 2. The data gives the sector 1 defenders (@46) and sector 2 defenders (@118) one AtkHeli pad each, and the operator's sector 2 defenders' sample (Dirt x4, LT, IFV, TrHeli) indeed had none, so those pads are disabled live or belong to another layout. Attack helicopters on Area 51 would then be: attackers in sectors 2 and 3 (@46 from phase 2, @118 from phase 3), defenders in sectors 3 and 4 (@42, @236).

