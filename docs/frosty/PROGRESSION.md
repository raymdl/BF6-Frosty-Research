# Progression and experience

[Frosty docs](README.md) · [Soldier](SOLDIER.md) · [Gadgets](GADGETS.md) · [Vehicles](VEHICLES.md)

What the game data says about experience, stat events and match outcome bonuses. The persistence graphs emit events and hold rules;
amounts are tunables (defaults in L4034, [Soldier](SOLDIER.md)). Game-mode rules are in L4029 ([Gadgets](GADGETS.md)).

## L4027 - Persistence (experience and stat event) graphs (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4027-persistence-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/persistence.md`).

- Passive mastery experience (`ActSimEx_Persistence_PlayerOwner`, 0x17304 to 0x17b00): off when kill switch `DisablePassiveMasteryXP` is set; ticks every `PassiveMasteryXP_Interval` seconds only while firing or within 10 s of the last shot; amount = scalar x interval / 60, scalar chosen for vehicle, secondary or primary (anything else uses primary).
- Battle royale placement experience (`SimEx_Persistence_OutcomeXPBonus_Granite` and the losing-squads variant): budget per mode (solo, duo, trio, squad) x `BR - MatchPlayed_PlacementWeights`[placement - 1] / sum of weights, divided by 100, truncated, x 100.
- Match-time experience per minute is chosen by game mode: `Override_MatchPlayed_XPpM` when non-zero, else `All - MatchPlayed_XPpM`.
- Multi-kill timeout is chosen by chain length: 1 uses `MultiKill2`, 2 `MultiKill3`, 3 `MultiKill4`, otherwise `MultiKill5`. `QuickDrawTimeout_Seconds` applies only to one weapon group.
- Survival bonus experience is read from an array at index teams alive - 1, per battle royale sub-mode.
- Capture-point time events fire from a per-soldier accumulator at the `ObjectiveSecuring`, `Holding` and `Controlling` trigger intervals.
- `OnGraniteWin` reads the win streak unless kill switch `Granite_IgnoreWinStreak` is set.
- Areas-visited tracking uses a 60 constant (read as seconds).

9 raw-offset checks matched.

## Default values for the L4027 rules (from the L4034 table)

Shipped defaults decoded from `GRX_Persistence_Glacier` and `MutatorDatabase_CH1`; the full list is the L4034 table
(`expression-graphs/tunables-joined.tsv` in the run folder). These rows are decoded values, not individually raw-checked,
and can be overridden remotely.

| Rule | Default |
|---|---|
| Match-time experience per minute | 250 for all modes; every per-mode value and the override are 0 |
| Passive mastery experience | every 30 s; scalar 1.0 primary, 0.5 secondary, 0.5 vehicle |
| Multi-kill timeouts (2, 3, 4, 5 kills) | 5, 6, 7, 8 s |
| Battle royale experience budget | solo 400000, duo 200000, trio 150000, squad 100000 |
| Battle royale placement weights | 3500, 3000, 2700, 2400, 2200, 2100, 2000, 1955, ... (falling list) |
| Battle royale survival bonus per step | solo 50, duo 100, trio 150, squad 200 |
| Gauntlet placement experience | 8000, 6500, 4000, 3500, 2250, 2000, 1750, 1500, 800, 700, 600, 500 |
| Event throttles | spotted 15 s, supply 10 s, gadget used 30 s, vehicle repaired 1.5 s, match-played 60 s |

Related game-mode default (rule in L4029): capture speed multipliers by players inside are 0, 1, 1.25, 1.5, 1.75
(`Granite_f[]CaptureSpeedMultipliers`), and the assault class capture modifier is 1.2.
