# Game modes other than Breakthrough: rules, maps and layouts (build 2.1.1.0, 21 Oct 2026)

Working note, not a closed lead. Companion to `BREAKTHROUGH_SECTORS_2026-10-19.md`, same method.
Per-mode detail (every map, every instance index, open questions) is in
`mode-reviews-2026-10-21/result-<Mode>.md`; this note is the synthesis.

Captures (all under `builds\2.1.1.0\reports\`, recorded): `modes-layers-2026-10-21` (2,034 routes: every
`_layers_gameplay/<mode>/` asset of the 19 live maps for every mode folder except Breakthrough, every
`Gamemodes/<Mode>/` asset, the 17 level roots), `modes-layers2-2026-10-21` (1,154 routes: the layer
assets that sit directly under `_layers_gameplay/` such as `Conquest0`, `Rush_Global`, `Sabotage`, and the
shared layers `SharedAssets_*`, `_small_modes*`, `esc_cq_*`), `modes-gems-2026-10-21` (150 routes: GEM
blueprints and prefabs the other modes use, Gauntlet core). The mode rule assets `MUT_*` of the live
modes were already in `capture\collection\raw`. Decoded with `frosty-ebx-decode.py`; extraction by
`modes_extract.py` (a mode-agnostic version of `frosty-breakthrough-extract.py`, kept as `scripts/frosty-modes-extract.py`) and
`modes_mut.py` (kept as `scripts/frosty-modes-tweakables.py`); variant keys resolved through each mode's own `AD_Objective_<Mode>` table.
Per-map analyses were written by one Sonnet subagent per mode from the extraction text files; I merged
their results and corrected where the second capture changed the data. Patch-note passages for modes
and maps: `reference-data/patch-notes/modes-and-maps-passages-2026-10-21.md` (through WebFetch's
summariser, wording as returned).

## What is in the files, and what is not

- **Modes with a live UI entry** (`UIGameModeMetadata`): Conquest, Breakthrough, Rush, Escalation,
  Domination, Team Deathmatch, Squad Deathmatch, King of the Hill, Strikepoint, Payload, Sabotage,
  plus Gauntlet and the four Battle Royale sizes (Granite). Every live map's `UILevelDescriptionMetadata`
  imports loading-screen tips for Breakthrough, Conquest, Domination, Escalation, KOTH, Payload, Rush,
  SDM, Strikepoint and TDM (all ten on all 19 maps, Sabotage has no tip set), so the tips do not say
  which modes a map really offers.
- **Modes with rule assets but no UI entry**: Obliteration, Squad Obliteration, Carrier Strike,
  Operations, Raid, Shutdown, Spooky Rush (Halloween event, layer on Area 51), Tank Hunt, Squad
  Shootout, Free Roam. See the last section.
- **Rules** come from `MUT_<Mode>` tweakables (client defaults, overridable by a server playlist; units
  are never stored, so "15.0" round times are read as minutes and small timers as seconds, inferred).
  Round-logic graphs (`GME_Sim_<Mode>_Round`) expose variable names only; their constants are unnamed.
  No mode's XP table is named except Breakthrough's and Operations'. Points-per-tick values of the
  score modes (Domination, KOTH) are not named anywhere.
- **Layouts** come from per-map layer instances (GEM modules with positions). Team, side, objective
  letter and order are never stored; they are inferred spatially and marked as such.
- **Caution on layer quality.** Several small-mode layers look like templates or stubs rather than the
  live layout: five Payload maps share one identical route on round-number coordinates; Area 51's
  Domination triangle is Siege of Cairo's to within 6 m; many Sector / spawn-area markers sit at one
  shared default position across unrelated maps; several maps store no play-area polygon. Where a mode
  is live on a map and the file shows a template, the live layout may be loaded from somewhere this
  capture did not reach (Portal/experience data, or runtime layer selection). In-game checks are listed
  at the end.

## Mode by map (layer with gameplay instances in the files)

x = layer with instances, o = layer assets but no gameplay instances (schematic/mesh only), - = none.
BT = Breakthrough (from the 19 Oct note), CQ Conquest, Esc Escalation, Dom Domination, TDM, SDM,
KOTH King of the Hill, SP Strikepoint, Pay Payload, Sab Sabotage.

| Map | BT | CQ | Rush | Esc | Dom | TDM | SDM | KOTH | SP | Pay | Sab |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Siege of Cairo | x | x | x | x | x | x | x | x | x | x | x |
| Empire State | x | x | x | - | x | x | x | x | x | - | x |
| Wake Island | x | x | x | x | x | x | x | o | x | x | o |
| Blackwell Fields | x | x | x | - | x | x | x | x | x | x | x |
| Iberian Offensive | - | x | x | x | x | x | x | x | x | x | o |
| Liberation Peak | x | x | x | x | x | x | x | x | x | x | - |
| Contaminated | x | x | x | x | x | x | x | o | x | x | - |
| Area 51 | x | x | x | o | x | x | x | - | x | - | - |
| Manhattan Bridge | x | x | x | x | x | x | x | x | x | x | x |
| Eastwood | x | x | x | x | x | x | x | x | x | - | x |
| Operation Firestorm | x | x | x | x | x | x | x | x | x | - | - |
| Railway to Golmud | x | x | x | o | x | o | x | - | x | o | - |
| Tsuru Reef | x | x | x | x | x | x | x | - | x | - | - |
| Saints Quarter | - | - | - | - | x | x | x | x | x | - | x |
| New Sobek City | x | x | x | x | x | x | x | x | x | x | - |
| Vegas Strip | x | x | x | o | x | x | x | - | x | - | - |
| Cairo Bazaar | x | x | x | - | x | x | x | o | x | x | - |
| Hagental Base | x | x | x | - | x | x | x | - | x | x | - |
| Mirak Valley | x | x | x | x | x | x | x | o | x | - | - |

Iberian Offensive has Conquest and Rush layers (found in the second capture, stored directly under
`_Layers_Gameplay`) but no Breakthrough; Saints Quarter has only the small modes (Domination, TDM,
SDM, KOTH, Strikepoint, Sabotage). Eastwood's Rush layer and Empire State's Rush layer were likewise
only found in the second capture.

## Faction per map

Team 1 = Alliance/NATO and team 2 = Coalition/Pax Armata unless the layer overrides it. Overrides are
per mode and are not consistent across modes on the same map (for example Siege of Cairo swaps to
Pax Armata as team 1 in Conquest, Domination, TDM, Payload and Strikepoint but not in every mode;
Cairo Bazaar sets NATO as team 1 explicitly in Domination). The per-map section of
`result-Maps.md` lists the override per mode.

## Mode rules at a glance (client defaults from `MUT_<Mode>`; units inferred)

| Mode | Win condition | Score / tickets | Round time | Capture / objective timing | Respawn | OOB return | Vehicles |
|---|---|---|---|---|---|---|---|
| Conquest | deplete enemy lives, or more lives at time-out; full-majority countdown ends it early | 1200 lives per team (default and every per-map `*_CQ_iInitialScore`); death ratio 2.0; bleed tick 5 s dynamic by lead, 1 life per capture | 45 (10-180) | capture 30 s, neutralise 30 s, player multipliers 0/1/1.333/1.666/2.0 | 12 s | 10 s | pads per map; no cooldown tweakable (unlike Breakthrough) |
| Rush | attackers destroy every M-COM in every sector before their lives run out; defenders stop them | attackers 75 lives (`R_iInitialTickets`), warnings at 50 and 25, urgency at 10; 1 life per death; per-sector reinforcement amount not named | win-XP spans 25 / 15 min; sector time 15 (10-180, unit unstated) | arm 2.0 s (fast 1.6), defuse 5.0 s (fast 4.0), fuse 30 s; sector taken 6 s, clean-up 15-45 s (early end threshold 10), advance 40 s, reinforcements 5 s | 12 s both teams every sector (global fallback 10) | not in `MUT_Rush` | pads per map; no cooldown fallback |
| Escalation | first to take three territories (hold the majority of flags to fill progress; taker loses the flag nearest its own HQ) | 5 phases, phase lengths 90/162/252/3600 (4 values for 5 phases) | 120 base timer | capture 20 s, neutralise 20 s, multipliers 0/1/1.333/1.666/2.0; stalemate pre-delays 180/120/60 s | 12 s | 10 s | pads per map; spawn value interval 90 |
| Domination | first to 200 points, or most at time-out | score tick 4.0 s base; tick delays by flags held 0/3.5/2.5/1.5 s; points per tick unnamed | 15 | capture 10 s, neutralise 10 s, multipliers 0/1/1.25/1.5/2.0; max objective distance 40 | 0 | 5 s | none (infantry) |
| Team Deathmatch | first to 100 kills, or most at time-out | overtime 1.0; big lead 20 | 15 | spawn scoring: enemy near -20 (0-20 m), far -2 (20-40 m), previous death -20, friendly +1, primary +3; area swap at -10 | 0 | 5 s | none |
| Squad Deathmatch | four squads, first to 50 kills, or most at time-out | shoot-out set 50/30/20 in 7/5/3 is present but `SDM_isSquadShootOut` = false | 15 | spawn scoring enemy -20, friendly +5/+1, death -10; killstreaks from 5 every 5 | 0 | 5 s | allowed: IFV pads on 6 maps, cooldown 120-480 s, reveal 60 s |
| King of the Hill | first to 250 points, or most at time-out | score tick 1.0 s, points per tick unnamed; big lead 50 | 15 | one hill at a time: first unlock 20 s, hill active 90 s, next revealed 10 s ahead; capture and neutralise 0 (instant), capture on neutralised | 0 | 5 s | disabled (`KOTH_bAllowVehicles` false) |
| Strikepoint | first to 6 rounds (min 3); win a round by securing the objective, holding it longer at round end, or eliminating the enemy | capture progress target 25 (0-90), capture lock 30 | 3 per round, overtime 60 | objective unlock delay not named (per-map `Strikepoint_Tweaks` instance or unnamed constants) | none (one life; downed not counted alive) | 5 s | none |
| Payload | two rounds, teams swap; round 1 reach the final checkpoint fastest or travel furthest, round 2 beat that | base speed 1.75; attacker speed multipliers 0/1/1.33/1.66/2.1 (by attackers near); defenders 0/0.5; retreat after 10 s | not named; time multiplier 3.0 first sector, 1.4 later | checkpoint pause 2+2 s, open 20 / close 3 / unlock 15; checkpoint mines 350 blast damage; smoke cooldown 45 s | 8 s both teams | 5 s | payload armour x1000 |
| Sabotage | two turns, one attack each; most equipment destroyed, time as tiebreak | 1 point per piece regardless of size (Small/Medium/Large health 100/250/500, health modifier 5.0) | 6.0 initial, overtime 15.4 | layout selection 1 (0-2) | 12 s | 5 s | none |

Numbers the UI text confirms: none. The UI text confirms only the concepts (kill target, points target, time limit, three territories, six rounds, two Payload rounds, Sabotage turns). Lobby timers: Conquest and Escalation start at 32 and speed up at 64, Domination, TDM, SDM, KOTH, Payload and Sabotage at 16, Strikepoint at 8.

## Conquest

Rules above, 59 tweakables; no vehicle cooldown fallbacks and no XP table in `MUT_Conquest` (Breakthrough
has both). `CQ_LayoutSelection` = 0 (range 0-3) and every map has one `Conquest0` layer in the files.
Full-majority thresholds: 6 flags (high layouts) or 3 (low), 60 s countdown. Per-map initial score is
1200 on all 12 maps that have a `MUT_<map>` asset.

Eighteen maps have a `Conquest0` layer with instances (only Saints Quarter has none). Flags per map,
HQs, and vehicle pads grouped by nearest anchor (HQ-W / HQ-E by x position, since team identity is
not stored; "near flags" = neutral pads whose nearest anchor is a flag):

| Map | Flags | HQs | Pads W / E / near flags | Total pads | Air vehicles | Notes |
|---|---|---|---|---|---|---|
| Siege of Cairo | 5 | 2 | 2 / 2 / 0 | 4 (IFV 2, Tank 2) | no | 4 forward spawners; no SpecialCombatArea |
| Empire State | 5 | 3 | 0 / 0 / 0 | 0 | no | infantry only; @162 and @97 carry 8 insertions each (the live spawns), the third HQ @154 has none (non-spawn marker) |
| Wake Island | 7 | 2 | 11 / 11 / 18 | 40 | yes | flags far off the HQ line, letter order weak |
| Blackwell Fields | 6 | 2 | 11 / 11 / 6 | 28 | yes | |
| Iberian Offensive | 5 | 2 | 3 / 3 / 2 | 8 (LightTransport 6, IFV 2) | no | 3 forward spawners near HQ-W; no SpecialCombatArea |
| Liberation Peak | 6 | 2 | 10 / 10 / 6 | 26 | yes | |
| Contaminated | 6 | 2 | 10 / 10 / 4 | 24 | yes | 6 gas zones; 10 outline areas for 6 flags |
| Area 51 | 9 | 2 | 16 / 16 / 29 | 61 | yes | most pads (17 light transports, 17 quads); a CapturePoint_Proxy 18 m from one flag |
| Manhattan Bridge | 5 | 2 | 6 / 6 / 2 | 14 | yes | vehicle OOB time 10 s per map |
| Eastwood | 5 | 2 | 10 / 10 / 14 | 34 | yes | |
| Operation Firestorm | 5 | 2 | 15 / 15 / 7 | 37 | yes | 6 forward spawners; 17 outline areas for 5 flags |
| Railway to Golmud | 7 | 2 | 21 / 21 / 19 | 61 | yes | train toggles in `MUT_Golmud` |
| Tsuru Reef | 9 | 2 | 10 / 10 / 20 | 40 | yes | |
| New Sobek City | 5 | 2 | 9 / 9 / 3 | 21 | yes | |
| Vegas Strip | 5 | 2 | 11 / 11 / 12 | 34 | yes | |
| Cairo Bazaar | 5 | 2 | 2 / 2 / 0 | 4 (IFV 2, LightTransport 2) | no | 4 AntiTank emplacements |
| Hagental Base | 5 | 2 | 0 / 0 / 0 | 0 | no | infantry only; gas assets listed but no gas zone instance |
| Mirak Valley | 5 | 2 | 16 / 16 / 10 | 42 | yes | one flag 233 m off the HQ line |

On every map the two HQs carry the same pad count with the same class mix (mirrored sets); maps differ
in the neutral pads near flags. Flag letters are a spatial guess (projection along the HQ-W to HQ-E
axis) and are weak on the island and desert maps. Battle pickups are placed on 14 maps (placed but not
active in the live game). Per-map detail with every flag and pad position is in `result-Conquest.md`.
Faction overrides in Conquest: team 1 = Pax Armata on Siege of Cairo, Blackwell Fields, Operation
Firestorm, Railway to Golmud and Tsuru Reef; NATO set explicitly on Eastwood and Cairo Bazaar; default
elsewhere.
## Rush

Rules above, 110 tweakables in `MUT_Rush`. The per-sector reinforcement amount is not a tweakable
(the shared `SimEx_SetSectorReinforcement` logic exposes references only), the same gap as
Breakthrough's. Eighteen maps have a `Rush0` layer with instances; Saints Quarter has none. Every
sector holds two M-COMs except where noted. The attackers' start is read as the chain end where the
insertion (arrival) instances cluster, medium-low confidence; `SimEx_CheckMCOMStatus.OwningTeamInt`
defaults to 1, which would make team 1 the M-COM owner, so team 1 may be the defender in Rush. Pads
are split by chain half (start base plus front half = attackers, back half plus final base =
defenders), a static spatial reading.

| Map | M-COM stations | M-COMs per station | Pads attackers / contested / defenders | Total pads | Air | Notes |
|---|---|---|---|---|---|---|
| Siege of Cairo | 4 | 2/2/2/2 | 3 / 0 / 0 | 3 | no | |
| Empire State | 3 | 2/2/2 | 0 | 0 | no | fourth sector marker at the start end with no M-COM |
| Wake Island | 5 | 2 each | 32 / 5 / 21 | 58 (LightTransport 26, PatrolBoat 17, RHIB 8, no tank) | no | |
| Blackwell Fields | 4 | 2 each | 6 / 0 / 0 | 6 | no | |
| Iberian Offensive | 3 | 2 each | 1 / 0 / 0 | 1 (LightTransport) | no | |
| Liberation Peak | 4 | 2 each | 10 / 0 / 2 | 12 | no | |
| Contaminated | 4 markers | 6 M-COMs, pairing unresolved | 0 | 0 | no | no pads, emplacements or pickups |
| Area 51 | 5 | 2 each | 27 / 11 / 10 | 48 (46 + 2 Forward) | AttackHelicopter 2 | |
| Manhattan Bridge | 4 | 2 each | 0 | 0 | no | 5 markers for 4 M-COM pairs |
| Eastwood | 4 | 2 each | 4 GolfCart, 1 APC | 5 | no | 2 HMG; two sector markers 110 m above the M-COMs |
| Operation Firestorm | 3 | 2 each | 2 / 0 / 2 | 4 | no | |
| Railway to Golmud | 5 | 2 each | 24 / 5 / 12 | 41 | ScoutHelicopter 2 | |
| Tsuru Reef | 3 | 2 each | 8 / 4 / 1 | 13 | no | |
| New Sobek City | 4 (6 markers) | 2 each | 0 | 0 | no | duplicated sector markers, one stray M-COM at a default position |
| Vegas Strip | 4 | 2 each | 5 / 0 / 1 | 6 | no | |
| Cairo Bazaar | 4 | 2 each | 1 / 0 / 3 | 4 | no | |
| Hagental Base | 5 | 2 each | 0 | 0 | no | |
| Mirak Valley | 4 | 2/3/2/2 | 9 (IFV 3, LightTransport 3, Tank 2, Quad 1) | 9 | no | 3 AntiTank; six stray M-COMs and two HQs whose x/z match New Sobek City exactly (excluded) |

Rush is far lighter on vehicles than Breakthrough: six maps have no pads at all, and only Area 51 and
Railway to Golmud place air vehicles. On six maps the Sector markers sit at shared default positions,
so sectors there are grouped by M-COM pairs and shared polygons. The 1.0.1.0 and 1.1.3.0 notes say Rush
layouts were revised for attacker-defender balance (see the patch-note passages).


## Escalation

Eleven maps have a full Escalation layer (Siege of Cairo, Wake Island, Iberian Offensive, Liberation
Peak, Contaminated, Manhattan Bridge, Eastwood, Operation Firestorm, Tsuru Reef, New Sobek City, Mirak
Valley). Railway to Golmud has a single capture point in `Escalation_Global` and no HQ (its `MUT_Golmud`
enables the Escalation moving train, so a layout probably exists elsewhere); Area 51 and Vegas Strip
have empty layers; the other five maps have none. Every layout is 7 flags (9 on Tsuru Reef) with 6 HQ
instances: two initial bases (the farthest-apart pair, each with its own pad set; 8 insertions each on seven maps, none on Wake Island, Iberian Offensive, Liberation Peak and Tsuru Reef) and
four forward spawn areas near flags (on Iberian Offensive two of them duplicate the E initial HQ). "Other anchors" counts pads nearer a flag-side HQ or a flag than an initial HQ, so on Wake Island (22 of 25) and Tsuru Reef (14 of 23) most of it sits at flag-side HQs. The removal rule (the taker loses the flag nearest its own initial
HQ) means the map shrinks from each team's rear; the two teams' predicted top-3 removals share a flag
only on New Sobek City and Wake Island.

| Map | Flags | Initial HQs (index, x/z) | Pads W / E / other anchors | Air | team1 / team2 |
|---|---|---|---|---|---|
| Siege of Cairo | 7 | @200 [-281,66] / @37 [159,-83] | 10 / 10 / 4 | none | Pax Armata / NATO |
| Wake Island | 7 | @67 [-701,308] / @32 [202,-639] | 17 / 17 / 25 (PatrolBoat 21, Tank 6, LT 6, IFV 4, Multirole 4, NavalFighter 4, TrHeli 4, Quad 4, AtkHeli 2, MobAA 2, RHIB 2) | yes | default |
| Iberian Offensive | 7 | @23 [576,111] / @73 [920,134] | 4 / 4 / 0 | none | Pax Armata / NATO |
| Liberation Peak | 7 | @6 [-312,100] / @108 [275,451] | 15 / 15 / 6 | AtkHeli 2, AtkPlane 2, Fighter 2 | default |
| Contaminated | 7 | @114 [-151,-232] / @128 [434,190] | 16 / 17 / 5 (Dirt 12, LT 6, IFV 4, Tank 4, ScoutHeli 4, AtkHeli 2, AtkPlane 2, Fighter 2, MobAA 2) | yes | default |
| Manhattan Bridge | 7 | @12 [-262,-435] / @9 [179,-243] | 13 / 13 / 6 | AtkHeli 2, ScoutHeli 2 | default |
| Eastwood | 7 | @117 [-401,122] / @235 [378,-160] | 20 / 20 / 13 | AtkHeli 2, ScoutHeli 2, TrHeli 2 | NATO / Pax Armata (explicit) |
| Operation Firestorm | 7 | @93 [-758,209] / @68 [560,-230] | 22 / 22 / 10 | full set | Pax Armata / NATO |
| Tsuru Reef | 9 | @94 [-1156,843] / @21 [-436,-678] | 12 / 12 / 23 (RHIB 12, PatrolBoat 6, Quad 6, IFV 4, Tank 4, TrHeli 4, Dirt 4, AtkPlane 2, Fighter 2, LT 2, APC 1) | yes | Pax Armata / NATO |
| New Sobek City | 7 | @191 [-189,3] / @140 [153,21] | 17 / 17 / 5 | AtkHeli 2, ScoutHeli 2, TrHeli 2 | default |
| Mirak Valley | 7 | @65 [-461,-240] / @2 [497,-528] | 27 / 27 / 8 | full set | default |

Both initial bases always carry the same pad count and class mix (mirrored sets). Which base is team 1
is not stored; the island maps' initial-HQ pick is low confidence because their farthest-apart HQs hold
only air and boat pads. `ESC_f[]PhaseLengths` has four entries for five phases (open).

## Domination

One layout per map on all 19 maps: exactly 3 capture points, 1 sector, 1 sector-spawn module and 4
insertions, no flag model (the Domination capture point default is `GMPF_CapturePoint_NoRepresentation`;
Conquest's is `GMPF_CapturePoint` with a Flag variant). Flag triangles have 40-149 m edges. Play-area
polygons (where stored) run from Saints Quarter 103x42 m (instances only) to Railway to Golmud
279x185 m; Siege of Cairo 231x194, Manhattan Bridge 227x158, Vegas Strip 206x212 and Contaminated
207x177 are the next largest. Seven maps keep their Sector and SectorSpawns at shared default
positions, and Area 51's triangle matches Siege of Cairo's within 6 m, so some of these layers are
templates (see the in-game checks).

## Team Deathmatch and Squad Deathmatch

One layout per map (`MP_TeamDM0`, `MP_SquadDM0`), 4 insertions each (one per squad in SDM). No combat
area module: the play area is the largest layer polygon, from Siege of Cairo 142x91 m (TDM) and Saints
Quarter 99x67 m (SDM) to Wake Island 288x214 m (TDM, three chained boxes) and Railway to Golmud
348x274 m (SDM). Railway to Golmud has no TDM instances at all (schematic only). On eight TDM maps the
Sector and AlternateSpawnArea sit at one shared default position; Area 51's TDM layer is stub data
(round-number coordinates, no shape).

Squad Deathmatch vehicles: IFV pads only, 28 in all, on Blackwell Fields 3, Liberation Peak 5, Eastwood
5, Railway to Golmud 4, Cairo Bazaar 6 (plus 4 AntiTank emplacements), Mirak Valley 5; nothing on the
other 13 maps. No tank, helicopter, boat or plane pad anywhere in SDM.

## King of the Hill

Ten maps carry a KOTH layer with instances, each with exactly 5 candidate hills, 1 sector, 4 insertions
and a phase-based spawn area: Siege of Cairo, Empire State, Blackwell Fields, Iberian Offensive,
Liberation Peak, Manhattan Bridge, Eastwood, Operation Firestorm, Saints Quarter, New Sobek City. Mirak
Valley has the layer asset but no instances; Wake Island, Contaminated and Cairo Bazaar have mesh data
only; Area 51, Railway to Golmud, Vegas Strip, Hagental Base and Tsuru Reef have no KOTH layer. Hill
order is not stored (instance ids do not follow geography; the round graph tracks a
`SpecifiedCapturePoint`). Hill spreads: 49x142 m (Siege of Cairo, north-south line) to 160x60 m (New
Sobek City). With 15-minute rounds and 90 s per hill, a full round is about 10 activations over 5 hills.

## Strikepoint

All 19 maps have a Strikepoint layer; Eastwood and New Sobek City carry two objective layouts in it (21
layouts in all). Each layout is one objective capture point between two HQs 103-203 m apart, each HQ
53-111 m from the objective (Cairo Bazaar tightest, Wake Island widest), with a `Strikepoint_Tweaks`
instance on 17 maps (two on Empire State, none on Cairo Bazaar and Hagental Base) whose values the
extraction does not decode. The objective unlock delay is not a named tweakable. Four maps also have a
`flag` layer folder whose assets are named Strikepoint (Iberian Offensive, Eastwood, Saints Quarter,
Mirak Valley); they hold no gameplay instances in this capture.

## Payload

Ten maps have Payload instances; Railway to Golmud has a schematic only; Empire State, Area 51,
Eastwood, Operation Firestorm, Tsuru Reef, Saints Quarter, Vegas Strip and Mirak Valley have no layer.
Five of the ten (Wake Island, Blackwell Fields, Contaminated, Cairo Bazaar, Hagental Base) share one
identical template: payload at (-190,-190), three checkpoints on a straight 224 m line at y 70, the same
eight HQs and four sectors. Only five maps have a map-specific route:

| Map | Checkpoints | Straight-line length to last checkpoint / to final sector | Mines | HQs |
|---|---|---|---|---|
| Siege of Cairo | 2 | 247 / 346 m | 7 | 8 (three stacked at one point) |
| Iberian Offensive | 2 | 141 / 204 m | 0 | 6 |
| Liberation Peak | 2 | 190 / 238 m | 8 | 6 |
| Manhattan Bridge | 2 | 227 / 273 m | 8 | 6 |
| New Sobek City | 2 | 366 / 435 m | 8 | 7 (three Payload instances, one used) |

No instance marks the route end (checkpoint count is one below sector count), so the farthest sector
marker is read as the final checkpoint; real spline lengths will be longer than the straight lines.
Mines sit in clusters of 3-4 within 15 m of each checkpoint. The payload vehicle type is not named in
the objective table.

## Sabotage

Six maps have a Sabotage layer with targets (Wake Island and Iberian Offensive have mesh data only):

| Map | Zones | Targets per zone | Targets (Small/Medium/Large) | HQs | Play area |
|---|---|---|---|---|---|
| Siege of Cairo | 3 | 10 / 11 / 9 | 30 (30/0/0) | 2, 148 m apart | polygons span 207x136 m |
| Empire State | 2 | 14 / 15 | 29 (12/15/2) | 2, 138 m | 198x285 m |
| Blackwell Fields | 6 | 14 / 11 / 11 and 19 / 14 / 4 | 73 (33/34/6) | 5 | two clusters 480 m apart |
| Manhattan Bridge | 3 | 5 / 5 / 5 | 15 (15/0/0) | 2, 173 m | 210x160 m |
| Eastwood | 3 | 16 / 16 / 16 | 48 (16/23/9) | 2, 126 m | 303x209 m |
| Saints Quarter | 3 (one empty) | 19 / 20 / 0 | 39 (18/19/2) | 2, 103 m | polygons span 146x93 m |

Zone membership is inferred from shared polygons. Every piece is worth one point whatever its size;
the score bar shows at most 50 segments although Blackwell Fields places 73 targets, and
`SAB_LayoutSelection` = 1 (range 0-2) may pick one of its two clusters. Which HQ attacks first is not
stored.

## Modes without a live UI entry, and Gauntlet

| Mode | Rule asset | Tweakables | Layers on live maps | What it is, from the files |
|---|---|---|---|---|
| Obliteration | `MUT_Obliteration` | 58 | Contaminated, Railway to Golmud, Eastwood (6 M-COM targets, 12 bomb pickups, 2 or 6 HQs each) | bomb carry: pick up, arm at an enemy target (fuse 35 s), defuse; score limit 3; 64 players |
| Squad Obliteration | `MUT_SquadObliteration` | 58 | Siege of Cairo, Empire State, Iberian Offensive, Cairo Bazaar (6 M-COMs, 1 bomb, 2 HQs, compact box) | the same for 16 players, score limit 2, fuse 50 s, 15-minute cap |
| Carrier Strike | `MUT_CarrierStrike` | 50 | Tsuru Reef (2 HQs, 4 M-COMs, 8 VLS batteries, 5 capture points, 49 pads of which 12 RHIB) | assault on a carrier with health 100,000 and damage thresholds 0.7/0.5/0.3/0.1; both teams start at score 100 |
| Operations | `MUT_Operations` | 136 | Contaminated + Hagental Base (Operation Augur, live); Mirak Valley + Liberation Peak (unreleased pair, Breakthrough-derived) | two-map sector campaign, 3 battalions of 200 tickets, with XP table; see the Operations section below |
| Spooky Rush | `MUT_SpookyRush` | 48 | Area 51 (4 altars, 1 marker, 6 HQs, 4 sectors, 11 DSPulse pickups, no M-COMs) | Halloween Rush variant: altars instead of M-COMs, 75 attacker tickets, kill-drop collection event (drop rate 0.2, 25 per player, 400 per round) |
| Raid | `MUT_Raid` | 20 | none | sector push where 10 attackers must hold a point for 10 s |
| Shutdown | `MUT_Shutdown` | 14 | none | device deploy 10 s / planted 45 s / disarm 10 s, score to 90 in a 7-minute round |
| Tank Hunt | `MUT_TankHunt` | 46 | none | tank-kill scoring (3 per tank), target 20, 12-minute round, vehicle spawn 45 s |
| Squad Shootout | `MUT_SquadShootout` | 11 | none | 3 rounds, targets 50/30/20 in 7/5/3 (the same set sits in `MUT_SquadDM`) |
| Free Roam | none | 0 | none | empty shell |
| Gauntlet | none in these files | 0 | Tsuru Reef jets-only layout (6 HQs, 18 plane pads, 51 stockpiles); Empire State UI partition only | live Battle Royale side mode; its rules live in the Granite assets, not captured |

Mode-rule assets of all these except Gauntlet were already in the main capture. Spooky Rush is the
live Halloween event at the time of writing; its Area 51 layer is the only event layout in the files.

## Operations (added 21 Oct 2026)

Operations is the two-map Breakthrough campaign. The rule asset `MUT_Operations` (136 tweakables, values
in `result-Other.md` section 4) gives attackers `InitialBattalions` 3 of `TicketsPerBattalion` 200,
`MaxTransitions` 1 (one map change), `fSecondMapStartDelay` 45 s, capture and neutralise 30 s, lobby 24
players starting and 48 max. Reinforcement thresholds are per sector: Map1 [100, 100, 100, 75, 75] (five
sectors), Map2 [75, 75, 75, 75] (four sectors), so the rule asset is tuned for exactly the live pair.
The loc strings describe the mode as "Battle across multiple maps to secure enemy sectors by capturing
their objectives", with "Earn reinforcements after taking each sector", "When a new battalion is deployed,
attackers receive additional vehicles or weapon support at their HQ", and "NEXT MAP: {0:s}". The only
named operation in the strings is **Operation Augur** (title, four challenge strings, five challenge
descriptions). "Operation Gladius" and "Operation Ember Strike" are campaign missions; Firestorm is a map.

The first modes capture took only the `_layers_gameplay/operations/MeshVariationDb` files, which is why
the table above used to say "mesh databases only"; `modes-layers2-2026-10-21` captured the actual layers
(`MP_Operations0`, `Operations`, `Operations_Global`, schematics, Hagental's `Operations_Callins*`). The
extraction script skipped them because the layer name carries an `MP_` prefix; the corrected extraction
is `mode-reviews-2026-10-21/extraction/Operations-maps.txt` (424 GEM instances, 4 maps).

**Map pairing** is stored in two `Operations_NextLevel_*` assets, each holding one level path:

| Asset | Loads next | Referenced from |
|---|---|---|
| `Operations_NextLevel_Contaminated` | `MP_Subsurface` (Hagental Base) | not referenced by a captured layer; Contaminated's `MP_Operations0` carries the `GEM_SwapLevel` |
| `Operations_NextLevel_Tungsten_Capstone` | `MP_Capstone` (Liberation Peak) | Mirak Valley's `_Layers_Gameplay/Operations` (as a boxed value) and its `Operations_Global` `GEM_SwapLevel` |

So the files hold two operations: Contaminated then Hagental Base (Operation Augur, confirmed by the two
`T_UI_Operations_<map>_01_LoadingScreen` textures, which exist only for Contaminated and Subsurface) and
Mirak Valley then Liberation Peak, which has no loading screen, no name string and no challenge strings.
`Enum_Operations` (the `OperationTypeInt` of the view model) has two values, `Any` = 0 and `Hagental` = 1;
`Enum_OperationsOutcome` is GameEnd / MapSwitch / BattalionLost. The UI movies are
`Glacier_S2_Operations_Map_01/02_*` (intro, outro, background; map 2 has separate attacker and defender
intros): Season 2 naming, one set only.

**What each layer holds** (`Operations-maps.txt`; Breakthrough counts from `BREAKTHROUGH_SECTORS_2026-10-19.extraction.txt`):

| Map | Role | Sectors / CPs / HQs in the Operations layer | Operations-only GEMs | Faction override |
|---|---|---|---|---|
| Contaminated | Augur map 1 | none (uses the Breakthrough layout: 5 sectors in-game) | 10 Reinforcement, 10 Reinforcement_Intro, 32 VehicleSpawner_Forward, 41 VehicleSpawner (10 APC, 10 IFV, 9 Tank, 8 quad, 4 LT), 17 PsyGasZone (16 ArtilleryStrike, 1 Outdoors), 7 PsyGasArtilleryStrike, 8 PsyGas_Activator, 2 MCOM, 6 HQ, 60 Insertion, MapBriefingOverride, SwapLevel | team 1 NATO, team 2 Pax Armata |
| Hagental Base | Augur map 2 | none in `MP_Operations0`; the `Operations` layer binds 4 `MI_LD_D_SectorInfo` / `GemInfo_Sector` entries (4 sectors in-game) | 8 Reinforcement, 12 Reinforcement_Intro, 16 Battle_Pickup (Minigun), 5 PsyGasZone (SubCorridor), 6 PsyGas_Activator, 48 Insertion, MapBriefingOverride, SwapLevel; `Operations_Callins_Locations` 20 call-in points (radius 3 m) | none (default NATO attacks) |
| Mirak Valley | second pair, map 1 | 3 / 6 / 6 (Breakthrough: 4 / 6 / 6; the 3 sectors sit at the Breakthrough positions, all 6 CPs are 5 to 20 m from the Breakthrough ones) | none: 12 VehicleSpawner (5 IFV, 5 Tank, 2 LT), 10 stationary, 4 resupply, 16 Insertion, SwapLevel in `Operations_Global` | none |
| Liberation Peak | second pair, map 2 | 5 / 7 / 10 (Breakthrough: 5 / 7 / 10; sectors and 4 CPs at the Breakthrough positions, 3 CPs moved 6 to 16 m) | none: 15 VehicleSpawner (6 Tank, 6 quad, 3 LT), 9 stationary, 7 resupply, 16 Insertion; no SwapLevel, no NextLevel | none |

The two Augur layers are additive: they carry the battalion machinery (reinforcement spawn sets, the
gas, the map swap, the briefing override) and leave the sector and capture-point set to the Breakthrough
layout, which matches the 1.4.2.0 note "Visual boundary lines for Objective A in Sector 2 have been
improved in Operations and Breakthrough" on Hagental Base. The Mirak Valley and Liberation Peak layers are
instead self-contained copies of their Breakthrough layouts with no reinforcement, gas or briefing
objects, and Mirak Valley's `Operations_Global_Schematic` still references `TestingLevel_Layout00` and
`CHIITest_Layout00`; they read as an earlier or unfinished operation, not a release-ready one. Why Mirak
Valley drops the fourth Breakthrough sector (at [246, 200, -397]) and why the capture points differ by a
few metres is not resolved; the Breakthrough layer may simply have been revised after the Operations copy
was taken.

**Area 51 and Vegas Strip.** Neither `MP_DryLake` nor `MP_Paradise` has any Operations asset in the
2.1.1.0 catalog (manifest and loc strings dated 13 Oct 2026, game head 5382784): no
`_Layers_Gameplay/*Operations*`, no `Operations_NextLevel_*` naming either level, no Operations loading
screen, no UI movie set beyond the Season 2 one, and no operation name other than Augur in the strings. If
an Area 51 and Vegas Strip operation is coming, it is not in this build's files; re-check after the next
update by grepping the new manifest for `operations` on `drylake` / `paradise` and the loc for a new
"Operation <name>" title.

## Per map

`result-Maps.md` has, for each of the 19 maps, the faction override per mode, the map extent, the
per-map tweakables, the union of vehicle classes across modes, the play-area polygons per mode and the
unusual assets. Points that stand out:

- **Modes per map (layers with instances, the 11 live modes including Breakthrough):** Siege of Cairo
  and Manhattan Bridge 11; Blackwell Fields, Liberation Peak, Eastwood and New Sobek City 10; Empire
  State, Wake Island, Iberian Offensive, Contaminated and Operation Firestorm 9; Tsuru Reef, Cairo
  Bazaar, Hagental Base and Mirak Valley 8; Area 51, Vegas Strip and Railway to Golmud 7; Saints
  Quarter 6.
- **Iberian Offensive** (Gibraltar, Upper Town): Conquest (5 flags, 8 pads, no air), Rush, Escalation
  (7 flags, 8 pads, no air), Payload (2 checkpoints, 141 m straight line, no mines), KOTH (5 hills),
  Domination, Strikepoint, TDM (no insertion instances), SDM, Squad Obliteration; no Breakthrough,
  Sabotage shell only. It is the only large-mode map with no air vehicles in any mode.
- **Saints Quarter** (also Gibraltar, Upper Town, a different coordinate frame): small modes only,
  Sabotage (39 targets, 3 zones), KOTH (5 hills), Domination, Strikepoint, TDM, SDM. No Conquest,
  Breakthrough, Rush, Escalation or Payload although the loading-screen tips list them.
- **Eastwood** has no Payload; **Empire State** no Escalation or Payload; **Operation Firestorm** no
  Payload; **Mirak Valley** no Payload and a KOTH shell only; Railway to Golmud's TDM and Payload are
  shells.
- **Faction overrides differ between modes on 12 of 19 maps**; they are consistent on Wake Island,
  Liberation Peak, Manhattan Bridge, Eastwood, Saints Quarter, New Sobek City and Hagental Base.
- `UILevelDescriptionMetadata` rows (country, coordinates, description) exist for 11 maps only; Wake
  Island, Contaminated, Area 51, Railway to Golmud, Tsuru Reef, Vegas Strip, Cairo Bazaar and Hagental
  Base have no row in the captured asset (another UI asset or a seasonal variant may hold them).

## What needs an in-game check

The files cannot settle these; each is one match or one deploy screen.

1. **Small-mode layouts that look like templates.** Domination on Area 51 (same triangle as Siege of
   Cairo), the five identical Payload routes (Wake Island, Blackwell Fields, Contaminated, Cairo Bazaar,
   Hagental Base), TDM on Area 51 (stub coordinates). If the live layouts differ, the live data comes
   from a source this capture did not reach.
2. **Mode availability**: whether Saints Quarter really has no Conquest, Rush, Escalation or Payload;
   whether Eastwood, Empire State, Operation Firestorm and Mirak Valley have no Payload; whether KOTH
   exists on Wake Island, Contaminated, Cairo Bazaar, Mirak Valley.
3. **Conquest ticket count** 1200 per team on every map (no per-map difference in the files) and the
   45-minute time limit; whether the full-majority countdown (60 s) is live.
4. **Sides**: which team attacks first in Rush, Payload and Sabotage per map, and which HQ is team 1 in
   Conquest and Escalation (mirrored pad sets make this matter less for vehicles).
5. **Strikepoint objective unlock delay** and round time (3), not named in the files.
6. **Sabotage round length** (6.0, unit unstated) and whether all 73 Blackwell Fields targets count.
7. **KOTH hill order** (fixed sequence or random), and the points per tick in KOTH and Domination.

## Open questions in the files

- Variant resolution: with per-mode tables, Domination, KOTH and Strikepoint capture points (key -1)
  resolve to `GMPF_CapturePoint_NoRepresentation`; the first-pass result files say `GMPF_CapturePoint`
  for them (written before the per-mode tables were used). The live prefab is unconfirmed either way.
- `GEM_Strikepoint_Tweaks`, `GEM_Payload`, `GEM_Checkpoint` and `GEM_Mine` instances carry per-instance
  data that the extractor does not decode (it reads position, key and interface overrides only).
- The `Flag` layer folders (Strikepoint-named shells) and `Winter_Domination` on Empire State were not
  decoded beyond asset names.
- Points per tick (Domination, KOTH), the Strikepoint unlock delay, Payload round time and push radii,
  and the Sabotage round count live in unnamed round-graph constants, as the Breakthrough ticket count
  does.
- No mode but Breakthrough and Operations names its XP values; the shared progression data was not
  captured.
