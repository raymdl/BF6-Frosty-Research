# How to read a mode work folder

Each `<Mode>-maps.txt` is an extraction of one Battlefield 6 game mode's per-map gameplay layers, decoded
from the raw game data of build 2.1.1.0 (Season 5, 21 October 2026). Coordinates are world units
(metres); `pos=[x, y, z]`, y is height; use x and z for map-plane geometry. Map internal names map to
in-game names in `map-names.json` (MP_Battery = Iberian Offensive, MP_Limestone = Saints Quarter,
MP_Isolated = Tsuru Reef, MP_Paradise = Vegas Strip, MP_Plaza = Cairo Bazaar, MP_Subsurface = Hagental Base,
MP_Atoll = Wake Island, MP_DryLake = Area 51, MP_GolmudRailway = Railway to Golmud, MP_Contaminated = Contaminated).

Per map:
- `assets`: the layer assets found for this mode on this map (the mode layer, `_Global`, `_Schematic`,
  `_Telemetry`, `generated/DD_*` destruction/volume sets, `_Cover`, registries).
- `factionOverrides`: which faction each team id plays (empty = engine default: team1 = Alliance/NATO,
  team2 = Coalition/Pax Armata). In attacker/defender modes, which team attacks is not stored on the
  instances; infer it and say so.
- `namedOverrides`: per-instance interface values the layer sets (name: value). Usually empty.
- `gem counts`: number of each gameplay module (GEM) instance; `other imports`: non-GEM prefabs.
- Instance lines: `<layer>@<index> <Module> key=<k> variant=<GMPF_...> pos=[x,y,z] boxes=[...] polys=[...]`
  - `key` is the instance's variant selector; `variant` resolves it through the mode's objective
    definition (`objective-table.json`: for each GEM, the default prefab and the prefab per key). A
    `variant=None` means the mode's definition does not list that module (it is placed but served by
    another definition or unused). `key=-1` = no selector.
  - Modules seen across modes: `CapturePoint` (flag / capture objective; in Domination, KOTH and
    Strikepoint its variants differ from Conquest), `CapturePoint_OutlineArea` (minimap outline), `Sector`
    and `HQ` (sector markers and headquarters spawn areas), `Objective_MCOM` (Rush M-COM), `Payload`
    and `Checkpoint` (Payload vehicle and its checkpoints), `Mine`, `Bomb_Pickup` (Obliteration), `Destructible`
    and `DestructibleZone` (Sabotage equipment targets / destruction), `SectorSpawns`, `AlternateSpawnArea`,
    `SafeSpawnArea`, `ProximitySpawns` (spawn logic), `CombatArea` / `SpecialCombatArea` (play-area
    boundaries), `Strikepoint_Tweaks` (per-map Strikepoint settings), `VehicleSpawner` (vehicle pad; the
    variant names the class: Tank, IFV, APC, LightTransport, MobileAA, AttackHelicopter, ScoutHelicopter,
    TransportHelicopter, FighterPlane, AttackPlane, MultirolePlane, NavalFighterPlane, RHIB, PatrolBoat,
    PTV_QuadBike/DirtBike/GolfCart, carrier jet launches), `VehicleSpawner_Forward`, `StationarySpawner`
    (HMG, AntiTank, AntiAircraft emplacements), `AutomaticAA`, `VehicleResupplyStation`, `Insertion`
    (deploy arrival animations), `Battle_Pickup` (placed but not active in the live game), `DeployCam`,
    `TelemetryArea`, `Reinforcement*` (intro reinforcements), `PsyGas*` (Contaminated gas).
  - `boxes=[...]` / `polys=[...]`: indices of the rectangles / polygons that contain the instance.
- `BOX@<index> (<layer>) bbox=[minx, minz, maxx, maxz] contains=[...]`: a 4-point rectangle.
- `POLY<n>@<index> (<layer>) bbox=... contains=[...]`: irregular polygons (combat areas, telemetry areas,
  spawn regions, objective areas).

Other files:
- `<Mode>-tweakables.txt`: the mode's `MUT_<Mode>` tweakables (`name = value [min..max]`; these are the
  client defaults, a server playlist can override them), plus the round-logic graphs (`GME_Sim_*_Round`:
  named variables only, constants are unnamed) and shared GEM logic tweakables (`_Shared/GEMS/...`).
- `maps-tweakables.txt`: per-map `MUT_<map>` tweakables (12 maps have one), e.g. Conquest initial score.
- `ui-text.txt`: the game's own UI description of the mode (rules as the game states them).
- `objective-table.json`: the mode's objective definition, GEM -> prefab per variant key.

Nothing in the data labels which team an HQ, spawner or objective belongs to, nor objective order or
letters. Derive spatially and from the layer names (`<Mode>0`, `<Mode>_Team1`, `_Global`, `_Small`, `_Large`
and so on, which tell you which layout variant a set belongs to). State your inference and confidence;
do not invent data. Name maps and vehicles as the game does.
