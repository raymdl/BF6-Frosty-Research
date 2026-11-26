# Gadget mechanics overview

A plain-English reader aid: one card per gadget, 71 cards, saying what the gadget does, the stored numbers
that matter, what changed since October, what is not known, and what could be shown on a site. It is a summary,
not a record. The records are [GADGETS.md](../frosty/GADGETS.md) and the technical
[gadget guide](GADGET_RESEARCH_GUIDE.html); check a number there before using it.

Written 26 November 2026 against game version 2.1.2.5.

## How far to trust it

- **Where the cards come from.** Four worker models wrote them from the technical guide (last updated 10 October
  2026, read on game version 1.4.3.5) and GADGETS.md. They were told to add nothing from memory.
- **Card check.** A second set of workers then compared every number on every card with the guide: about 720
  numbers, 25 flagged. All 25 were traced: 24 come from GADGETS.md, which the checkers did not have, and one was a
  miscount that is now fixed. A check by a small model can miss things, so GADGETS.md stays the record.
- **What was re-checked on 2.1.2.5.** Two things only: every named gadget setting in the game's gadget settings
  table (compared between 1.4.3.5 and 2.1.2.5; the result is each card's "Changed since October" line), and the lock
  settings inside each lock-on launcher's own file (identical on both builds).
- **Values inside each gadget's own files.** Also re-checked: all 829 gadget files that differ between 1.4.3.5 and
  2.1.2.5 were read on both builds and compared value by value. About 35 gameplay files hold a real change; they are
  listed in "Values that changed inside gadget files" below and noted on the cards concerned. The other differences
  are re-saved layout, artwork, sound, icons and logic-graph bookkeeping. Limits: the comparison pairs values by
  field, so it can miss a change hidden among entries that were added or removed in the same field, and it does not
  read the logic graphs themselves.
- **Not covered.** Mission, loot and battle royale items have no card.
- **Units.** The game files rarely state a unit. A bare number in a card has no confirmed unit.
- **Two sources for one number.** Many gadgets hold a value in their own file and another in the settings table.
  Earlier research found EA's stated numbers follow the settings table where the two disagree. The cards say which
  source a number comes from only where the technical notes do.

## What stands out across all gadgets

- **Settings removed since October.** These named settings no longer exist, so any number quoted from them is out
  of date or now lives somewhere unnamed: C4 arm delay 0.5; four EOD Bot detection and tracking settings; the laser
  designator's world-lock time, cooldown, angle and 500 spotting distance; M320 LVG blast radius 3.5; four
  thermobaric settings (fire damage duration 4 among them); airburst smoke-blocking radius 2.5; the drone's
  destroy-gadget cooldown 5; the Vehicle Supply Crate's 15 supplies and 15 max time; the Supply Pouch's "regeneration
  25 for 4"; Adrenaline Shot rank 5.
- **Settings changed.** Frag grenade delay after bounce 1.4 to 1.1; Assault Ladder ramp angle 52 to 45; Supply Pouch
  throw delay (0, then 1, now 0.1); one unowned "Range" setting 3 to 15.
- **Settings added.** A full named set for the IGLA and for the Signal Jammer (new in 2.1.2.0); five REDSEC
  ammunition amounts; an AT Mine transport detection interval of 2; four PTKM-1R civilian-vehicle settings.
- **Lock-on launchers did not change.** Stinger, Javelin, IGLA, MBT-LAW, AT4, RPG-7 and the laser designator hold
  the same lock settings in their own files on both builds.
- **Least understood.** Field upgrades, call-in strikes, Sabotage, Precision Strike, the payload and UAV drones,
  night vision, armor, Active Resupply, Ammo Bag and Medic Crate have little or nothing safe to show.

## Which number does the game use?

Many gadgets hold a value twice: once in the gadget's own file and once in the game's central settings list. Where
the two disagree, the game files do not say which one is used. The project's working rule since October is that
the settings list wins. The evidence all points that way, and today's checks add to it, but only one gadget value
has been read in a match.

What supports the rule:

- **A balance change made in the settings list only.** In 2.1.2.5 EA's notes say the Supply Pouch throw delay was
  reduced. The settings list went from 1.0 to 0.1; the pouch's own file still says 1.0. (Three other unnamed values
  in the file changed in the same patch, so this is not a clean case.)
- **An earlier case of the same kind.** A scout helicopter minigun heat value changed in the settings list alone
  between two builds (recorded in October).
- **EA's stated numbers.** Where EA has published a number for a disputed value, it has matched the settings list.
- **One in-game reading.** In October an RPG hit on a tank's rear dealt 500, the settings-list prediction.
- **No convergence since October.** For 22 gadget weapon files and 8 named values each (capacity, magazines, reload
  time, fire rate and the replenish settings), 153 pairs agree on both builds and 14 disagree on both. None of the
  disagreements was resolved in either direction between October and now.

The 14 standing disagreements are mostly reload time (settings list 0.5, file 0) on placed gadgets, where it may
not matter. Three are worth a look in game because they are easy to see:

| Gadget | Settings list | Own file | Quick check in game |
|---|---|---|---|
| C4 | 4 carried | 3 carried | **Done, 26 November 2026: 4 charges in game. The settings list is right.** |
| IGLA | Lock time 1.0, range 700 (840 painted), minimum 50 | Lock time 1.8 and 1.2, range 600 and 800, minimum 39 | Time the lock tone on a hovering helicopter |
| AT Mine | Blast damage 195 | 300 | One mine under a full-health tank, read the damage |

C4 has now been checked and matches the settings list. If the IGLA also locks in about 1 second and the mine does 195, the rule holds for gadgets too and the
cards' settings-list numbers can be used. One clear result the other way would mean each gadget has to be checked
on its own.

## In-game names

The cards use the names in the game files. The game shows different names for many of them. From the game's own
menu data (read at 2.1.1.0; not re-read since):

| Name in the files and on the cards | Name shown in game | Short name |
|---|---|---|
| AT Mine | Anti-Vehicle Mine | AV Mine |
| AT4 | Aim-Guided Launcher | M136 AT |
| Adrenaline Shot | Adrenaline Injector | Adrenaline  Injector |
| Airburst Incendiary Launcher | Incendiary Airburst Launcher | Sich G1 WP |
| Ammo Bag | Supply Bag | Supply Bag |
| AntiTank Grenade | Anti-Vehicle Grenade | AV Grenade |
| Assault Ladder | Assault Ladder | Assault Ladder |
| C4 | Demolition Charge | C-4 Explosives |
| Claymore | Anti-Personnel Mine | AP Mine |
| Concussion Grenade | Stun Grenade | Stun Grenade |
| Decoy | Sniper Decoy | Sniper Decoy |
| Defibrilator | Defibrillator | Defibrillator |
| Deployable Cover | Deployable Cover | Deployable Cover |
| Deployable Mortar | Portable Mortar | LWCMS |
| Drill Launcher | Breaching Projectile Launcher | X95 BRE |
| Drone | Recon Drone | Recon Drone |
| EIDOS | Grenade Intercept System | GPDIS |
| EOD ATMine | EOD ATMine | EOD ATMine |
| EOD Bot | EOD Bot | EOD Bot |
| EOD Demining Charge | EOD Demining Charge | EOD Demining Charge |
| Flashbang Grenade | Flash Grenade | Flash Grenade |
| Frag Grenade | Fragmentation Grenade | Frag Grenade |
| GasMask | Protective Mask | Protective Mask |
| Incendiary Grenade | Incendiary Grenade | Incen Grenade |
| Javelin | Long-Range Launcher | MAS 148 |
| Lancet | Hardware Suppression System | Suppression |
| M26 Mass Dragonsbreath | Incendiary-Round Shotgun | SS26 |
| M26 Mass Slug | Underbarrel Shotgun | Shotgun |
| M320 HE | High Explosive Launcher | M320A1 HE |
| M320 Smoke | Smoke Grenade Launcher | M320A1 SMK |
| M320 Thermobaric | Thermobaric Grenade Launcher | M320A1 THRM |
| M4 SLAM | Tripwire Sensor AV Mine | M4A1 SLAM |
| MBT-LAW | Auto-Guided Launcher | MBT-LAW |
| MPAPS | Missile Intercept System | MP-APS |
| MiniV40 Grenade | Mini Frag Grenade | Mini Grenade |
| MobileJammer | Handheld Jammer | Jammer |
| PLD | Laser Designator | Laser Designator |
| PTKM-1R | Acoustic Sensor AV Mine | PTKM-1R |
| Proximity Grenade | Throwable Proximity Detector | Proximity Detector |
| RPG7v2 | Unguided Rocket Launcher | RPG-7V2 |
| Repair Tool | Repair Tool | Repair Tool |
| SA18 IGLA | Active Locking Air-Defense Launcher | Igla |
| Smoke Grenade | Smoke Grenade | Smoke Grenade |
| Spawn Beacon | Deploy Beacon | Deploy Beacon |
| Stinger | Air-Defense Launcher | SLM-93A |
| Supply Pouch | Supply Pouch | Supply Pouch |
| T-UGS | Motion Sensor | Motion Sensor |
| Throwing Knife | Throwing Knife | Throwing Knife |
| Tracer Dart Gun | Tracer Dart | Tracer Dart |
| Vehicle Supply Crate | Vehicle Supply Crate | Supply Crate |

## Values that changed inside gadget files

Between 1.4.3.5 and 2.1.2.5, in gameplay files (not artwork, sound, icons or logic graphs). Unnamed means the game
files do not say what the number is.

| Gadget | Change |
|---|---|
| PTKM-1R | Projectile blast damage 160 to 142 |
| AT Mine | One unnamed number 0 to 0.1 |
| Ceramic Armor | Spawn delay 2.0 to 1.725 |
| Laser Designator | Duration 9 to 2, in both of its files |
| Mobile Jammer | Eleven changes in its weapon file: two numbers 0.467 to 1.0, one unnamed delay 1.0 to 1.5, eight flags |
| Supply Crate | Deploy time 0.68 to 0.65; one unnamed projectile number 2 to 1; one direction value flipped |
| Deployable Cover | Own-file ammunition: capacity 30 and 6 magazines to capacity 1 and 1 magazine |
| C4 | Two unnamed counts 2 to 1; one blast-curve point 0.99579 to 1.0 |
| Sniper Decoy | Two unnamed counts (10 to 8, 9 to 7) and flags on each of its 15 pose files |
| Spawn Beacon | Position offset and one flag |
| Supply Pouch | The three firing-block values, covered in GADGETS.md |
| Recon drone, Deployable Mortar, Payload drone, Railgun | One or two on-off flags each |

No like-for-like value change was found in the gameplay files of the frag, smoke, flashbang, concussion,
incendiary, Mini V40 and anti-tank grenades, the throwing knife, the Claymore, the M4 SLAM, the launchers (RPG-7,
AT4, MBT-LAW, Javelin, Stinger, IGLA, Panzerfaust 3, M320 family, airburst, breaching dart), the Defibrillator,
Repair Tool, Adrenaline Shot, MP-APS, EIDOS, T-UGS, Tracer Dart, Assault Ladder or the gas mask. Their file
differences are layout, artwork and sound.

## Healing, supply and revive

### Defibrillator
**What the game says it does:** Revives squad members and teammates. You charge it for a full-health revive. It can also hurt enemies.
**How it works (from the game files):**
- Charge time is 1.0 for a full charge, with a floor of 0.3 (unit not stated in the files; EA's 1.2.3.0 patch notes call them seconds: 1 s full charge, 0.35 s minimum).
- A "revive upgrade" reduction of 0.7 is subtracted from the charge time, which gives 0.3 when it applies (unconfirmed: the reduction is read as an active-revive upgrade only from its name).
- On a friendly target the game uses a revive effect file with six health values: 50, 60, 70, 80, 90, 100 (read as health restored; unconfirmed). Which value applies, and how charge turns into health, is not read.
- On an enemy it uses a damage effect file with six values from 50 to 100 in steps of 10 (unconfirmed which branch is the enemy one; inferred from effect names).
- Reach: friendly range 2.0, enemy range 1.5 (units not stated). It can also destroy enemy gadgets within range 2.0 and an angle of 45.
- Carries 3 magazines, starts with 3, and refills after a delay of 4 (unit not stated).
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Which health value is used for which charge level.
- The stored minimum charge is 0.3, but EA's note says 0.35. The gap is unexplained.
- What the 13-row curve and the older "FasterRecharge" 1.5 and 1.0 numbers do (not placed in any rule).
- Who owns the FasterRecharge selector.
- Whether the revive entry list starts counting at 0 or 1.
**Could go on the site now:** Solid: full charge 1.0 and stored minimum 0.3 (show as stored defaults; mention EA's 0.35 note), 3 magazines, friendly range 2.0 and enemy range 1.5 (units need an in-game check). Needs an in-game check first: health restored per charge level, damage to enemies.

### Supply Pouch
**What the game says it does:** A single-use pouch that restocks ammo and medical supplies for you or teammates. GADGETS.md (newer) says the text means it fully restores health and gives part of the ammo for primary and secondary weapons. The guide said "some health restored", which GADGETS.md says had the two halves reversed. GADGETS.md wins.
**How it works (from the game files):**
- Healing effect stores 0 for the instant heal, 20 for heal over time, and an unnamed 2.5. The unit of the 20 and its timing are not stated. EA's notes (1.1.3.0: initial heal removed, heals over time only) fit this.
- Ammo effect has three entries holding 2, 3 and 4 (meaning not stated; which weapon type takes which is not stored).
- Carried: magazine size 1, 3 magazines, refill delay 39 (unit not stated). GADGETS.md says the settings rows changed in 2.1.1.0 to capacity 3 and 1 magazine, and the file numbers swapped back in 2.1.2.0. Which pair the game uses is unknown.
- Thrown speed 20. A lifetime of 60 is a candidate (unconfirmed). The "30 / 15" numbers on screen are UI-only, not timers.
- Newer finding: the pouch picks the first nearby soldier who passes two "needs it" checks, then always applies ammo, auto-refill and healing. A one-second rule treats the thrower differently at first (unconfirmed).
- The guide also listed "health regeneration 25 for 4"; see below.
**Changed since October:**
- Throw-to-fire delay setting (the wait before you can fire a weapon after throwing a pouch): 0.0 -> 0.1. GADGETS.md adds that it was 0, then 1 in 2.1.1.0, then 0.1 in 2.1.2.5.
- Setting removed: SupplyPouch_HealthRegenerationRate (was 25.0).
- Setting removed: SupplyPouch_RegenerationDuration (was 4.0).
- Out of date: the guide's "health regeneration 25 for 4" row. GADGETS.md says it was not found in the 2.1.2.5 settings. The healing numbers 0, 20 and 2.5 have not moved.
- GADGETS.md lists carried-count and refill changes in 2.1.1.0 that this ledger does not show. Treat the carried-count numbers above as unsettled.
**Not known yet:**
- Unit and timing of heal 20, and what 2.5 does.
- What 2, 3 and 4 mean for ammo.
- Pickup radius, cooldown, gas mask and night-vision amounts (not found).
- Whether 0.1 is the whole throw-to-fire delay.
- Which carried-count pair the game uses.
**Could go on the site now:** Solid: heal over time 20 with no instant heal (unit needs an in-game check), the 0.1 post-throw delay (stored; whole delay unconfirmed), refill delay 39 (unit not stated). Needs a check: ammo per pickup, carried count, lifetime.

### Supply Crate / Supply Bag
**What the game says it does:** Resupplies nearby infantry weapons and gadgets, and regenerates health, including under fire.
**How it works (from the game files):**
- Every 5.0 it runs a pulse (inferred from the rule's shape) on soldiers in the crate's zone who are alive and on the owner's team.
- Each pulse gives one of five ammo effects per weapon slot, each lasting 4.95 (read as a duration; unconfirmed). Zone size and ammo amount per pulse are not in the rule.
- Ammo effect files hold an unnamed number: 20 for rifle, machine gun and SMG/pistol, 5 for bolt/DMR and shotgun (meaning not stated).
- Healing uses the same effect as the pouch: 0 instant, 20 over time, an unnamed 2.5 (unit not stated).
- Carries 1 magazine, refill delay 15; opening takes 0.4 (units not stated).
- The rule's name says "granite", so it may not be the standard multiplayer rule (unconfirmed).
**Changed since October:** Nothing in the named settings. Inside its own files (re-checked 26 November 2026): Its deploy time went from 0.68 to 0.65, and one unnamed number in its projectile file from 2 to 1.
**Not known yet:**
- Zone radius and ammo amount per pulse.
- Whether healing works under fire (a setting called Ignore_Damage is only a configuration token).
- The size of the speed-up on pickup.
- Unit of heal 20.
- Whether the "granite" rule applies in normal multiplayer.
**Could go on the site now:** Solid: open time 0.4 and refill delay 15 (units unconfirmed); 5.0 pulse interval (shape inferred, so mark it). Needs an in-game check: ammo per pulse, heal rate, radius.

### Medic Crate
**What the game says it does:** Restores nearby friendly health.
**How it works (from the game files):**
- It shares the Supply Crate's healing effect: 0 instant, 20 over time, an unnamed 2.5 (unit not stated).
- Related effects for comparison: medical triage 0 / 20 / 1.0; emergency damage control extra heal takes 50 from a settings row, then 70 over time, and 2.0.
- Whether it is a separate multiplayer item at all is a candidate only.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Whether it exists as a separate item in multiplayer.
- Unit and timing of the 20.
**Could go on the site now:** Nothing yet. Its identity is unproved.

### Ammo Bag
**What the game says it does:** A deployable ammunition and medical supply bag.
**How it works (from the game files):**
- It shows the same name as Supply Crate in the reviewed records. No separate numbers are recorded for it.
- GADGETS.md says "Supply Bag" is EA's other name for the Supply Pouch. The sources do not settle which item "Ammo Bag" is.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Whether it is a separate item from Supply Crate.
**Could go on the site now:** Nothing.

### Vehicle Supply Crate
**What the game says it does:** A pallet that resupplies nearby friendly vehicles.
**How it works (from the game files):**
- Builds itself automatically in 0.6 and resupplies every 5.0 (units not stated; carried from older research).
- Carries 1 magazine, refill delay 120 (unit not stated).
- Ammo effect holds unnamed numbers 1, 0, 0 and 0.8.
**Changed since October:**
- Setting removed: VSC_Total Ammo Supplies (was 15, the guide's "15 supplies"). That number is now out of date.
- Setting removed: VSC_Resupply Neutral Vehicles Max Time (was 15.0, min 0, max 30). That number is now out of date.
**Not known yet:**
- Build time, pickup limits, amount per resupply and timing are separate stages, not one proved cooldown.
- Whether the removed settings moved elsewhere or were dropped.
**Could go on the site now:** Only build time 0.6 and interval 5.0 from the file values, with units unchecked. Do not show "15 supplies": its setting was removed.

### Adrenaline Shot
**What the game says it does:** A temporary sprint boost, less explosive and incendiary damage, and resistance to or removal of flash and stun effects.
**How it works (from the game files):**
- Three self effects (explosive damage cut, suppression, debuff removal) all last as long as the duration setting, 8 (min 0.1, max 10; unit not stated).
- The explosive effect stores 0.8, read as a 20% cut in explosive damage (unconfirmed; read from the field's name in similar effect files).
- The suppression effect stores -100 and the debuff-removal effect stores 247138971. Their meaning is unread.
- A separate self-heal effect stores heal over time 5, 10, 12.5, 15, 17.5, 20 and more ranks. It is tied to the shot by name only (unconfirmed).
- Carries 1 magazine, refill delay 45 (unit not stated).
**Changed since October:**
- Setting removed: AdrenalineShot_Rank (was 5). The guide's "rank 5" is now out of date.
**Not known yet:**
- Which ability triggers the effect rule.
- How rank picks a heal value, and the unit of the heal values.
- Meaning of -100 and 247138971.
**Could go on the site now:** Solid: duration 8 (unit unchecked), 0.8 explosive multiplier (name-read, so label as unconfirmed). Needs a check: heal amount, sprint boost size. Do not show rank 5.

### Repair Tool
**What the game says it does:** Repairs friendly vehicles and equipment, damages enemy assets, and overheats with long use.
**How it works (from the game files):**
- Repair and anti-repair amounts per second in the settings: standard 40 repair / 30 anti-repair; active repair 60 / 45. Battle Royale: 30 / 15 and 60 / 30. The unit is not stated. The guide doubts it is plain health per second (a 1200-health tank would take 30 s from empty).
- Range 2 and apply interval 0.1 (units not stated; the interval is a shared candidate, not a proven hit rate).
- Heat: 0.0142 per bullet, drops 0.4 per second; overheat threshold 0.15, penalty time 0.5 (configured heat, not the repair rate).
- The damage effect against enemy vehicles has seven values: 10, 5, 7.5, 12.5, 15, 17.5, 20. It is scaled by 1 vs tanks, 1.25 vs helicopters, 2 vs light vehicles. Ranks 3 and 5 would pick 12.5 and 17.5 (unconfirmed, joined by name).
- Several repairers stack: 2 to 8 repairers add 0.75, 0.58, 0.5, 0.4, 0.33, 0.28, 0.25 of a repairer, so the total tops out near double one repairer (unconfirmed).
- Reload time 3.59 (unit not stated).
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Unit of the per-second rows.
- Which row is the damage against enemy vehicles.
- Real range, heat-limited output and hit rate.
**Could go on the site now:** Stored and named: repair 40 and anti-repair 30 per second (standard), 60 / 45 (active repair), range 2, interval 0.1. All need an in-game unit check first.

### Restock Allies / ActiveMedic
**What the game says it does:** Resupplies and heals nearby allies for 10 seconds, and revives take only 1.7 seconds.
**How it works (from the game files):**
- Once per 1.0, it takes everything within 7 of you (unit not stated) and applies the Medic Crate healing and ammo refill effects with parameter 1.1 (read as a refresh time just above the pulse; unconfirmed).
- A self effect with parameter 10 runs on the first pulse (the 10 seconds is read from the screen text; unconfirmed).
- It works like a mobile crate for those 10 seconds (inferred from its shape).
- No source value for the 1.7-second revive has been found.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Where 1.7 comes from, and whether this state shortens the revive.
- Who receives the effects (filters not visible).
- Unit of the 7 radius.
- How long the pulse repeats.
**Could go on the site now:** Only the in-game text values (10 s, 1.7 s), labelled "stated by the game, not found in the files". Radius 7 needs a unit check. The 1.7 s needs an in-game timing.

### Active Resupply
**What the game says it does:** Use the special-ability input to drop a crate that instantly resupplies teammates once.
**How it works (from the game files):**
- No numeric rule has been traced for it. Only the text is recorded.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Everything numeric.
**Could go on the site now:** Nothing.

### Hemostatic smoke upgrade
**What the game says it does:** A smoke launcher upgrade advertising a 2.2 s revive, 12.5 hp per second regeneration after 2.5 s, and slower bleed-out.
**How it works (from the game files):**
- The regeneration effect stores rate 12.5, delay 2.5, amount 0 (units not stated). The first two match the screen text.
- The 2.2 matches the Support revive time stored in the files (2.2).
- Bleed-out is slowed by a multiplier setting (its value is not given in the guide).
- A related "faster regen" effect stores 30 and 2.5 (a different effect).
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Which classes can use it.
- How the slower bleed-out combines with the other timers.
- The game's actual regeneration operation.
**Could go on the site now:** 12.5 and 2.5 match both the screen text and the stored values, so they are the best candidates. Units still need an in-game check.

### Squad revive
**What the game says it does:** No in-game description recorded.
**How it works (from the game files):**
- Total drag-revive time is 4.72 (non-Support) and 2.2 (Support), with a 0.4 buffer (units not stated in the files; GADGETS.md calls them seconds).
- A revive-time reduction of 0.7 (min 0.5, max 1.5) exists. How it combines with the total is not known. The shortest allowed time is 0.1.
- On revive you get health from an 11-entry list: 100, 90, 80, 75, 70, 60, 50, 40, 30, 25, 20. A class rank picks the entry, but the rank is not matched to the list (unconfirmed which entry applies).
- A downed soldier bleeds out when health falls below -90. Drain rates are 1.6667, 2.2222, 3.3333 or 1.1111 by downed type, or 200 in a fast case (unit not stated; slowed by the Hemostatic setting).
- While dragging, moving faster than a threshold changes the revive speed, except in the first 0.75 and last 0.7 of the revive (the modifier value is not given).
- After a revive the soldier gets a short regeneration (rate 10, delay 0, amount 0).
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Whether 4.72 includes the 0.4 buffer.
- Which health entry goes with which rank.
- How the time reduction combines with the total.
- Where the 1.7 (ActiveMedic) fits.
- The missing owner file of the squad revive.
**Could go on the site now:** Solid: total 4.72 and Support 2.2 (named, re-read; unit not stated in the files). Needs a check: health given on revive (the operator describes half health on a tap, not measured), the 1.7 case, whether the buffer is inside the 4.72.

## Protection, concealment, detection and jamming

### MP-APS
**What the game says it does:** Tracks and destroys large incoming projectiles. It can intercept up to three, during a window that starts after it detects something.
**How it works (from the game files):**
- The device lives for 5 (unit not stated, probably seconds) by default. The stored range for this setting is 0 to 50. The timer is the device's lifetime, not a delay before it switches on.
- It stops after 3 interceptions by default (stored range 1 to 10). The in-game text also says three, but that match is a coincidence of numbers, not proof.
- With the owner's upgrade, the lifetime gets +3 and the interception count gets +2 (stored range for the +2 is 1 to 3). That gives 8 and 5 (unconfirmed, it is arithmetic on defaults; whether the owner holds the upgrade is tested by a check whose meaning is guessed from its name).
- Gadget stock: 1 charge, 1 spare, refills after 18 (unit not stated). A separate row stores an "active time" of 0 and a "recharge" of 20 (unconfirmed, nothing reads it yet).
- The effect file that does the actual intercepting was not found. The device's timer rule only counts time and interceptions.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- How far it reaches.
- What counts as an interceptable projectile.
- What starts the lifetime timer.
- How charges are used up and how recharge works.
- What the stored recharge of 20 is for.
**Could go on the site now:** Solid enough to show: default lifetime 5 and 3 interceptions (named, stored, not disputed; say "default, may be changed by the game remotely"). Upgrade bonuses (+3 and +2) are stored too but the upgrade link is guessed. Needs an in-game check: range, real lifetime in seconds, how many shots it really stops.

### EIDOS / GPDIS
**What the game says it does:** Tracks thrown and launched grenades. Up to three interceptions per window that starts when it detects something. (The in-game card calls it GPDIS; the internal name is EIDOS.)
**How it works (from the game files):**
- Same lifetime and interception settings as MP-APS: lifetime 5 (unit not stated), 3 interceptions by default. Same upgrade bonuses (+3 lifetime, +2 interceptions).
- It has its own range setting: 5 by default (stored range 0 to 20; unit not stated).
- The timer rule says: every 0.1 (unit not stated), look for projectiles inside that range, take the first one and count it. The enemy-only filter in that search is guessed (unconfirmed).
- It also shuts off if a "jammed" flag turns on. That the flag means radio jamming is guessed from file names (unconfirmed).
- While it is active the pickup is switched off (guessed from a channel name, unconfirmed).
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Real reach in the game (the 5 is not claimed as 5 metres).
- What counts as a grenade it will stop.
- What starts the lifetime timer.
- Charge use and recharge.
**Could go on the site now:** Solid: default lifetime 5, default interceptions 3, stored intercept range 5 (all named and stored; show without a unit). Needs an in-game check: real range, whether jamming really turns it off.

### Deployable Cover
**What the game says it does:** A repairable ballistic shield that blocks projectiles and explosive damage and wears down under fire.
**How it works (from the game files):**
- Four named parts, all on the front, each store 200.0. Do not add them to 800 health; the files do not say how the parts combine (unit not stated).
- Every 1.0 (unit not stated) a rule gives nearby soldiers two helper effects, one for explosive damage (stored 0.5, explosive flag set) and one for suppression (stored -100). It does this only for soldiers who pass an upgrade test (guessed to mean the cover upgrade). Both 0.5 and -100 are unconfirmed as to what they do (the -100 was never read by any rule).
- Gadget stock: 1 charge, 1 spare, refills after 30 (unit not stated). Active time 1, recharge 0.
- Another vehicle, the CB90, has a health setting with the same hidden name as one cover field; that CB90 name must not be copied onto the cover.
**Changed since October:** Nothing in the named settings. Inside its own files (re-checked 26 November 2026): The ammunition numbers in its own file went from capacity 30 with 6 magazines to capacity 1 with 1 magazine.
**Not known yet:**
- How the four 200 parts turn into total health and how much damage they resist.
- Radius and who receives the 1.0 pulse.
- What the stored 0.5 and -100 really do.
**Could go on the site now:** Little is solid. The four stored 200.0 part values and the 30 refill delay are stored and named, but showing "800 health" is not allowed. Needs an in-game check: total health, resistances, pulse radius.

### Smoke Grenade
**What the game says it does:** Gives temporary cover. It blocks spotting and clears infantry markers inside the smoke.
**How it works (from the game files):**
- Gadget stock: 1 charge, 2 spares, refills after 18 (unit not stated).
- One small smoke rule only affects the AI's sight. No rule for player spotting was found in it.
- A second rule runs every 0.5 (unit not stated). It puts out fires it finds and destroys gadgets in an overlapped list. Which gadgets are in that list is guessed (unconfirmed).
- A "fire put out" duration is stored: 1 (stored range 0 to 1.5, unit not stated).
- An older number, 10.0, once looked like a smoke lifetime. It is not one.
- Both smoke rules were read by a helper and not individually checked against raw bytes.
**Changed since October:** Nothing in the named settings. (The ledger has a smoke-blocking-radius row that belongs to the Airburst Incendiary by name; see the last section.)
**Not known yet:**
- Cloud size and how long it lasts.
- The rule that blocks or clears spotting for players.
- Which gadgets the 0.5 rule destroys.
**Could go on the site now:** Only the stock (1 charge, 2 spares, 18 refill) is solid. Cloud radius and duration need an in-game check.

### M320 Smoke
**What the game says it does:** An impact smoke round. It can be used on its own or under a weapon with a Gadget Mount.
**How it works (from the game files):**
- The standard and Hemostatic versions pick different payloads. Treat the payload choice as separate from how the weapon fires.
- The guide gives no numbers for this gadget.
**Changed since October:** Four settings on the M320 smoke projectile were removed from the named list: blast damage 0.0, damage multiplier 1.0, initial speed 350.0 and time to live 8.0 (unit not stated). Nothing in the card above used them. This is probably a renamed or moved item, not proof the values changed.
**Not known yet:**
- What happens from impact to cloud.
- The real size and duration of the cloud.
**Could go on the site now:** Nothing solid. The guide holds no numbers for it, and the removed settings need re-finding under a new name before any figure is shown.

### Flashbang Grenade
**What the game says it does:** Blinds. The strength depends on distance and on whether the target is looking toward the flash.
**How it works (from the game files):**
- Every soldier inside 12 (stored max range; unit not stated) who passes a visibility test is hit. Close range is under 6 (unit not stated).
- Blind time by view angle and distance (the guide labels these seconds): in front (angle under 60): 3.5 close, 2.5 far. Sides (up to 90): 1.5 close, 1.0 far. Behind: 0.6 close, 0.2 far.
- The rule adds 0.2 to the chosen time when it applies the effect (the reason for the 0.2 is not known).
- The angle is worked out by a chain guessed to be a dot product then an arc-cosine (unconfirmed). In some cases a second angle check is added; what it does is unknown.
- Fuse: shortest time before it can go off 1.1, delay after a bounce 1.4 (units not stated). Stock: 1 charge, 1 spare, refills after 30.
- The Stun Drill and the M320 flash store the same rows; the Stun Drill and its trigger flash use this same rule with their own settings.
- The newer notes agree with the guide on the fuse (flashbang 1.1 and 1.4). The grenade fuse default for frags changed, see below.
**Changed since October:** Nothing in the named settings for the flashbang. A frag grenade bounce delay changed 1.4 -> 1.1, but its name says frag, so it is not counted here (see the last section).
**Not known yet:**
- The real strength of the blindness.
- Why the extra 0.2 is added.
- What the second angle check does.
- Measured blind times in game.
**Could go on the site now:** Solid: the six blind-time numbers, close range 6, max range 12, angle limits 60 and 90, and the stock (all named and stored). Needs an in-game check: the +0.2, real blind effect, whether the numbers match what the player sees.

### Concussion Grenade
**What the game says it does:** Disorients targets and briefly prevents aiming down sights and sprinting.
**How it works (from the game files):**
- Three rings around the blast, each with its own radius and duration: close 5 and 3.5, middle 7 and 2.5, outer 9 and 1.5. The guide writes these as metres and seconds, but also says the units are unconfirmed.
- Soldiers in the sphere are picked by team and by a visibility test (both guessed from function names, unconfirmed). Each ring is read as the band between the previous ring and its own radius.
- Fuse: shortest time before it can go off 0.7, delay after a bounce 0.4. Stock: 1 charge, 1 spare, refills after 30 (units not stated).
- Several duration and strength inputs are stored as empty (null). Empty is not zero.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- What the effect does in detail and how strong each ring is (that is inside the effect files, which were not read).
**Could go on the site now:** Solid: the three ring sizes and times, the fuse numbers and the stock (stored and named, though possibly overridden by the game). Needs an in-game check: units, how strong each ring is, whether ADS and sprint block both last the full time.

### Gas Mask
**What the game says it does:** A mask that protects against VL-7 disorientation.
**How it works (from the game files):**
- Two reserves. The base mask holds 40 and uses 1.0 per tick of use; it recharges at 3 per tick while not worn, and the "depleted" flag clears at 20. Extra pickups add 11 each up to 44, then wait 1.0 before the next pickup. Units are not stated.
- Worn mask drains the extra reserve first, then the base. At base 0 the mask is forced off.
- The files hold three copies of these rules, chosen by mode. The numbers above are the default set. Battle Royale uses 20 / 1 / 20 / 1.0 for the base mask and 5 / 0 / 10 for the extra (pickup amount / extra max / pickup cooldown). Gauntlet matches the default set.
- Battle Royale only: with an upgrade, base max and recharge are scaled by 1.2 (the upgrade test is guessed from its name).
- Four on/off switches (restore state, unlimited use, only drain in gas, allow resupply when unlimited) can turn parts of the drain off.
- This rule was read by a helper and was not individually checked against raw bytes.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Whether the default set is what standard multiplayer actually uses (it is chosen when the Granite flag is false, which does not prove standard multiplayer calls it).
- Units of the durations.
- What the protection actually does.
**Could go on the site now:** Not yet. The numbers are stored, but it is not established that standard multiplayer uses this default set. Needs an in-game check first.

### Soft Armor and Ceramic Armor
**What the game says it does:** Both entries describe a standard small-arms ballistic vest insert.
**How it works (from the game files):**
- Armor works as swapped damage tables on the soldier. The chest table multiplies bullet damage by 0.84 for automatic weapons, 0.91 for DMRs and 0.67 for bolt-action. The head table gives 2.25 for bolt-action.
- The ceramic version switches the chest and head tables to others (bolt-action head 1.75); the soft version keeps both. Which direction each swap goes is a guess (unconfirmed).
- The chest values match the "chest against armor" lines in EA's 1.3.3.0 patch notes. That is a match of numbers only (unconfirmed link).
- Armor effects store 40, 80, 121 and 242 with a factor of 0.5. What these numbers mean is not confirmed.
- The Claymore damage rule multiplies by 0.67 if the target has armor (above 0). Finishing a revive can add ceramic armor (parameter 0.1).
- The newer notes say no standard multiplayer armor mechanic was established.
**Changed since October:** Nothing in the named settings. Inside its own files (re-checked 26 November 2026): Ceramic Armor spawn delay went from 2.0 to 1.725.
**Not known yet:**
- Whether these two gadgets exist in standard multiplayer.
- How much armor adds in health.
- What the 40 / 80 / 121 / 242 mean.
**Could go on the site now:** Nothing. The guide says these labels must not become a generic armor layer. Needs an in-game check that armor exists in standard multiplayer.

### T-UGS
**What the game says it does:** Marks moving enemies, vehicles and gadgets for the team. Crouching or prone infantry can avoid detection.
**How it works (from the game files):**
- Spotting radius 15 (stored max 50), mark duration 2 (stored max 5), delay between pulses 1.5. Units not stated.
- With the owner's upgrade the radius is multiplied by 1.5 (stored range 1.1 to 2.0; the upgrade test is guessed from its name). In battle royale it is multiplied by 2.0.
- It finds enemies in a sphere and splits them into soldiers, vehicles and gadgets. The vehicle and gadget switches are both on. Soldiers are always included. Vehicles are only marked if their speed is above 0.5.
- A "slow soldier" limit of 4 is stored, but whether it hides crouching or prone players is not proved (unconfirmed). Two constants, 0.5 and 2.5, are passed to the marking calls; their roles are unknown.
- Stock: 1 charge, 1 spare, refills after 30 (unit not stated).
- EA notes: the device is no longer destroyed when its owner dies, and marks persist better after the owner respawns.
- The rules were read by a helper and not individually checked against raw bytes.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- How targets are filtered.
- How long marks really persist.
- The pulse schedule and how many can be placed.
- How crouching or prone avoidance works.
**Could go on the site now:** Solid: radius 15, duration 2, pulse delay 1.5, upgrade multiplier 1.5 (stored and named; show with "default"). Needs an in-game check: real units, crouch and prone avoidance, device limit.

### Proximity Grenade / MTN-55
**What the game says it does:** Scans visible enemies once a second and marks their position for two seconds.
**How it works (from the game files):**
- Radius 7 (stored range 6 to 8), pulse delay 1, mark duration 2 (stored range 0.5 to 12). Units not stated. The timing matches the in-game text but that is a match of numbers, not proof of how it runs.
- Switches: line of sight on, vehicles on, gadgets off. Soldiers are always included. The meaning of each on/off is guessed from its name.
- With the owner upgrade the radius is multiplied by 1.5 (upgrade test guessed). In battle royale it is multiplied by 2.14.
- A speed limit is read beside a local constant of 2.0 for a soldier filter; its use is unresolved.
- The grenade outputs the spotted set, how many were spotted and the distance to the nearest enemy.
- Read by a helper and not individually checked against raw bytes. It is unclear whether moving vehicles are kept or removed.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- The scan schedule (the 1 is a stored row, but no rule using it was found).
- How movement states are treated.
- Which way each switch works.
**Could go on the site now:** Solid: radius 7, duration 2, delay 1, upgrade multiplier 1.5 (stored and named). Needs an in-game check: real range, whether vehicles are marked, how it treats crouching.

### Mobile Jammer
**What the game says it does:** A carried or thrown device that briefly disrupts nearby enemy equipment. (The newer notes say its in-game name changed to "Gadget Jammer" in build 2.1.2.0.)
**How it works (from the game files):**
- Radius 10, refills after 45 (units not stated). Stock: ammo 1 / 1 / -1 (the meaning of -1 is not established).
- With the owner's upgrade the radius is multiplied by 2.0 (stored range 1.1 to 5; upgrade test guessed).
- It finds things in a sphere, picks by team (guessed) and splits them into soldiers, projectiles and gadgets. Soldiers get a "jammed" effect and a lock-jam effect; projectiles get a "projectile jammed" effect. Both use parameter 0.2, read as a short refresh time because the pulse repeats (unconfirmed). Gadgets are collected but no effect on them is applied in this rule.
- Using it also jams the user for a stored time, then speeds up regeneration (parameter 0.0).
- The upgrade rule adds two spotting effects with values 0.5 and 1.5; their meaning and direction are guessed from names (unconfirmed).
- A "NumJams" output exists, but it is not shown to be a limit.
- The projectile's 30 / 50 / 15 settings are shared with mines and the proximity grenade. They are not jammer numbers.
**Changed since October:** Nothing in the named settings. The newer notes say the in-game name changed to "Gadget Jammer". Inside its own files (re-checked 26 November 2026): Its weapon file changed in eleven places: two numbers went from about 0.467 to 1.0, one unnamed delay from 1.0 to 1.5, and eight on-off flags flipped. None of these are named.
**Not known yet:**
- What the jam does in detail.
- How long it lasts in game.
- Which targets it can affect.
- Whether jams stack.
**Could go on the site now:** Solid: radius 10, refill delay 45, upgrade radius multiplier 2.0. Needs an in-game check: what the jam disables and for how long.

### Drone electronics disruption
**What the game says it does:** The recon drone can target gadgets through walls, hover to spot enemies, and give thermal vision.
**How it works (from the game files):**
- Two numbers equal registry rows named Max Distance and Max Angle: 80 and 2.5 (unconfirmed as to meaning, units not stated).
- Three distance thresholds 12 / 18 / 25 and a destroy value 1000 appear in the files but are not joined to the lock rules (unconfirmed). The destroy effect stores 1000 in its initial damage and damage-per-second fields. What that does to a gadget in game has not been measured.
- By its shape, locking a gadget for the full lock-on time destroys it. The rule that decides when progress counts was not fully read (unconfirmed).
- A "gadget lock cooldown" row stored 5 and a "lock-on time" row stored 0 (units not stated).
- EA 1.3.2.0 says close targets work through walls and distant ones need line of sight, with no distance given.
**Changed since October:** The "Drone_Destroy Gadget Cooldown" setting (5.0) was removed from the named list. The cooldown number above is out of date or moved. The lock-on time row is not in the ledger.
**Not known yet:**
- Which gadget types it can hit.
- How lock-on starts and resets.
- The wall and range thresholds.
- Whether the cooldown still exists under another name.
**Could go on the site now:** Nothing solid. The cooldown of 5 is gone from the named list. Everything else needs an in-game check.

### Laser Designator / PLD
**What the game says it does:** Binocular-style marking of vehicles and locations, with autonomous placement and remote access. Designated targets can be locked from further away and lose below-radar protection.
**How it works (from the game files):**
- Zoom levels 0 to 3 store max spotting distance 80 / 180 / 360 / 540 and angle 10 / 3.75 / 1.875 / 1.25 (candidates, units unconfirmed). Do not use these as a proved locking range table.
- Spot durations: soldiers 5, vehicles 30, gadgets 20 (candidates; handheld and deployed equal; units not stated). The mark effect itself uses MarkTargetDuration 15 (stored range 10 to 30). A vehicle also counts as spotted when laser paint progress reaches 0.5.
- EA changed designation from 20 to 9 seconds. A stored "Painter Max Duration" of 9 matches it, but that is a match of numbers only; it is not mapped to a control.
- EA 1.3.1.0 added a 20% lock-range benefit. The registry's air-vehicle lock ranges 650 and 780 are in a 1.2 ratio, which matches (not proof). For launchers the designated range is 1.2 times for the IGLA and Glaive but 1.25 times for the SLM-93A.
- With the owner upgrade (test guessed), spot time, range and angle are boosted. The mark effect also holds an unnamed 1.34.
- Stock: handheld 1 charge, 1 spare, 1 starting round, refills after 15; the controlled vehicle-weapon part has 0 spares and delay 5 (units not stated).
**Changed since October:** Inside its own files (re-checked 26 November 2026): A value named Duration went from 9 to 2 in both of its files. The separate settings-table entry for maximum painting time (9) did not change, and it is not established that the two are the same thing.
- Locking settings with "PLD" in the name: PLD_SecondaryLockingController lock time 1.5 -> 1.2. The second copy of this setting (1.2) was removed, so this is probably a duplicate-name shuffle and not a real change (the ledger says to treat these as uncertain).
- Removed: the "PLD_PrimaryLockingController" copy with lock time 1.5, min range 0.0, ray length 750.0, release-on-new-target 1.5, release 1.0, unlock -1.0; and the "PLD_SecondaryLockingController" copy with lock time 1.2, min range 0.0, ray length 750.0, release-on-new-target 1.5, release 1.0, unlock -1.0. Again likely duplicate-name collapse.
- Removed: PLD_Handheld Spotting Max Distance 500.0 (not used in the card above, but it was in the newer notes).
- Removed: PLD_World Lock On Time 1.0, PLD_World Locking Cooldown 0.5, PLD_World Locking Max Angle Deviance 20.0.
- No number in the card above is directly out of date, but the lock-time and range rows behind the "20% benefit" story may have moved.
**Not known yet:**
- The real designation timer in game.
- Which targets are filtered.
- When a lock breaks.
- How range adds up.
- Which gadget card the ambiguous in-game text belongs to.
**Could go on the site now:** Solid enough: the three spot durations 5 / 30 / 20 and MarkTarget 15 (stored; EA's 9 must stay separate). Needs an in-game check: the true range by zoom level, the designation timer, the 20% benefit, and the removed world-lock rows.

### Tracer Dart Gun
**What the game says it does:** Fires a magnetic dart that marks vehicles or personnel. Marked targets can be locked from further away and lose below-radar protection.
**How it works (from the game files):**
- Several of the dart's on/off and time settings are stored as empty (null). Do not read empty as zero, false or on.
- The dart projectile inherits speed 350 and life 20 (unit not stated; this is the projectile, a different owner from the mark effect's own time).
- The dart's mark effect once stored 11.0 next to a false flag. The same 11 is the stored value of the "locking signature multiplier" effect, but that link comes from the file name only (unconfirmed).
- Rule, read by a helper (not raw-checked): the mark's time is the dart's remaining life. On a player it attaches a marker. On a vehicle or gadget it applies the locking effect and the mark. A switch removes the mark when countermeasures fire; it is off by default.
- Stock: 1 charge, 3 spares, refills after 9; reload time 3.38 (units not stated).
- EA 1.4.2.0: marked targets can be locked by launchers.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- How long the mark lasts in game (the 20 is not shown to be the mark time).
- What the native locking signature effect does.
**Could go on the site now:** Solid: stock 1 / 3, refill delay 9, reload 3.38. Needs an in-game check: mark duration, how much the 11 changes lock range, whether it works through countermeasures.

### Hardware Suppression System / Lancet
**What the game says it does:** Spots nearby electronic and explosive gadgets and targets that are locking on. The text promises up to three combined missile interceptions and gadget destructions. The in-game card shows display name DGMK4; the internal name is Lancet.
**How it works (from the game files):**
- Detection distance 30 from the hip, 60 at zoom level 1 and 80 at zoom level 2. A UAV extends detection to 450. Driver spot duration 5. Units not stated.
- Time to fully track: 0.25 for general targets, 0.025 for projectiles.
- Switches, all on: target vehicle missiles and mines, detonate non-explosives, require line of sight.
- When a target is fully tracked, the driver is spotted for the stored time and tracked projectiles and gadgets are destroyed (parameter 0.0). This was a partial reading by a helper and not raw-checked.
- Reload time 3.233 (no registry row; unit not stated). The chain from the item to this rule was confirmed at build 1.4.3.5.
**Changed since October:** Nothing in the named settings. (Several EOD Bot tracking settings were removed, but they are named for the EOD Bot, so they are not counted here.)
**Not known yet:**
- Real range and timing in game.
- What "three combined" means in practice.
- How the game text joins to this chain.
**Could go on the site now:** Solid: the three detection distances 30 / 60 / 80, tracking times 0.25 / 0.025, reload 3.233 (stored and named). Needs an in-game check: units, the "three combined" count, which targets are actually stopped.

### UAV drone
**What the game says it does:** Spots enemy soldiers in the direction the operator is looking.
**How it works (from the game files):**
- No numbers are attached to this gadget in the guide. No source profile was found.
- Whether the gadget is available in standard play is listed as unclear.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Almost everything: range, timing, who can use it, whether it is in standard multiplayer.
**Could go on the site now:** Nothing. There is no stored number to show.

### Signal Jammer
**What the game says it does:** A deployable information denial device. Enemies inside its radius cannot spawn on squadmates and get restricted intel: distorted maps, spotting, killfeed and objective status. Tutorial text adds that the minimap and spotting are disrupted until the player leaves the radius or destroys the source gadget. (In-game model name: ADS-17 6Ghz.) New in build 2.1.2.0. The guide did not cover it; this card is from the newer notes only.
**How it works (from the game files):**
- It is a placed object built like a small vehicle. Health 25.0 (stored range 0 to 4095), health regeneration delay 5.0, regeneration rate 0.0. Units not stated.
- Radius: 21.0 for standard multiplayer, 100.0 for battle royale. Unit not stated.
- Stock: 1 charge, 1 spare, refills after 30 (unit not stated). Its weapon file reuses the Spawn Beacon's deploy-time table.
- Two effects exist: a "jammed" effect with no numbers and a "spot sharing" effect that stores 10.0 (what it means is unknown).
- Soldiers gain a "jammed" state when they hold at least one jammed marker. A new switch blocking squad spawns exists but is stored as off. What turns it on, and how the block works, is not traced.
- Available to Recon, last of 11 in the four Recon gadget slot lists. A kill switch for the ability is stored as off in one setting list. The unlock requirement was not in the captured files.
- Destroying it explodes with damage 0.0, blast radius 5.0 and shockwave radius 15.0. The 60.0 projectile life is a Spawn Beacon template value, not the jammer's lifetime.
- It checks for the Mobile Jammer's jam marker, and the Spawn Beacon checks for its own marker. What either check does is not traced.
**Changed since October:** Setting added (new gadget). Added settings: the whole vehicle block (max health 25.0, regeneration delay 5.0, repair rate modifier 1.0, blast radius 5.0, shockwave radius 15.0, inner blast radius 1.0, damage multiplier 1.0, shockwave damage 1.0) and the weapon block (refill delay 30.0, 1 charge, 1 spare, rate of fire 399.9, projectile speed 350.0, projectile life 60.0, spawn delay 0.5). Everything here is new, so there is no old number to go stale.
**Not known yet:**
- How the radius is applied (who is hit, whether line of sight matters, how often it ticks).
- How the minimap, killfeed and objective changes are made. No captured file reads the "jammed" state.
- How the squad-spawn block is wired.
- Any lifetime or placement limit. None found.
- Effects on drones, guided missiles or lock-on. None found.
**Could go on the site now:** Solid enough: radius 21 (standard multiplayer), health 25, regeneration delay 5, refill delay 30, 1 charge (stored and cross-checked against the update's setting list). Needs an in-game check: what the jam does, the radius unit, whether the squad-spawn block is on, and the unlock.

## Deployables, launchers and underbarrels

### Spawn Beacon
**What the game says it does:** A single-use spawn point for the player and each squad member. It goes inactive once the owner uses it. Squad deployment is switched off in Small Scale Battles.
**How it works (from the game files):**
- Ammo setup stores 1 round, 1 magazine, and -1 for rounds. These are resource settings, not a count of active beacons or "unlimited" use.
- The default list gives capacity 1, 1 magazine, automatic refill on, refill delay 30 (unit not stated).
- A small rule file sets "cannot be picked up" to true. By its name, the beacon cannot be picked up while a squadmate spawns on it. What triggers it is not shown.
- A yes/no switch stored as false has unknown meaning (true or false could mean on or off).
- Newer than the guide: the Signal Jammer (added in 2.1.2.0) is read by the beacon's file, but what that check does has not been traced.
- The 60 time-to-live seen on the beacon's projectile is a shared template value, not a proven beacon lifetime (unit not stated).
**Changed since October:** Nothing in the named settings. Inside its own files (re-checked 26 November 2026): A position offset and one on-off flag changed in its two files; no timing or count changed.
**Not known yet:**
- How long deploying takes.
- Whether placing a second beacon replaces the first or is blocked.
- What happens to the beacon when its owner dies.
- Whether "inactive" means destroyed or just unusable.
- What the new Signal Jammer link does to the beacon.
**Could go on the site now:** Nothing numeric is solid. The in-game description (single use, one spawn per squad member) could be shown as text. The refill delay 30 needs an in-game timing check first.

### Assault Ladder
**What the game says it does:** Placing it can give you a ladder, a bridge or a ramp.
**How it works (from the game files):**
- There is a separate placed object, physics and a ladder setting file.
- One plain use branch and three Assault branches (one is the ladder top) exist. They are not three working ladders.
- One vector (0.5, 3.84, 0.249939) is stored with no units stated.
- Two stored numbers, 30 and 6, are not shown to be cooldowns. The rule file for the projectile only reads two names that, by name, throttle usage statistics. It holds no placement or combat rule.
- Ramp angle was 52 in October (unit not stated). See below.
**Changed since October:**
- The ladder ramp angle default went from 52 to 45. The guide did not quote the 52, so no guide number is stale, but anything built on 52 should use 45.
**Not known yet:**
- How placement works and how far it reaches.
- Which branches actually activate.
- What the 30, 6 and the vector are.
- Whether the ramp angle is in degrees.
**Could go on the site now:** Nothing. The ramp angle 45 is a stored name and value but its unit is unstated, so check in game before showing it.

### EOD Bot
**What the game says it does:** A remote robot that repairs, arms and disarms M-COM stations, arms objectives remotely and then destroys itself, clears gadgets with cluster munitions, and places anti-vehicle mines.
**How it works (from the game files):**
- Repair 40 (75 while actively repairing), anti-repair 30 (45 active), repair range 3.2, apply interval 0.1 (units not stated, defaults can be overridden).
- Gadget spotting radius 40, interval 1.5; maximum detection distance 40 (unit not stated). The detection distance row no longer exists, see below.
- Maximum lifetime default 120, with a stored minimum 30 and maximum 360 (unit not stated). The life counts down every frame by a multiplier of 0 or 1 chosen by a condition that was not decoded. The bot is destroyed at 0.
- Damage-taking effect files store 0.65 for bullets and 0.6 for explosives. If these are damage multipliers, the bot takes 35% less bullet damage and 40% less explosive damage (inference, unconfirmed).
- Its mine stores blast damage 150, blast radius 2, inner radius 1.99, shockwave radius 4.5. Inner radius just under the radius would mean full damage everywhere inside (inference, unconfirmed).
- A kill switch controls whether the arm can arm objectives.
**Changed since October:**
- The setting for maximum detection distance (40) was removed, so that number in this card is out of date.
- Removed: the setting for whether the bot should detonate explosives (was false).
- Removed: time to full track (was 0.5).
- Removed: tracking max angle (was 12.5).
**Not known yet:**
- Control range.
- What the angle numbers (-180 / 180 / -22 / 45) and the 75 durability-like value mean.
- How objective completion works.
- Which condition makes the lifetime countdown run.
- Whether the removed tracking settings were replaced by something else.
**Could go on the site now:** Repair 40 and anti-repair 30 (stored, named, same as the repair tool pattern) are the best candidates. The mine blast damage 150 and radius 2 are stored but the damage reading needs an in-game check. Lifetime 120 needs a timing check, because the countdown condition is undecoded.

### Payload drone
**What the game says it does:** Can be placed for eliminated squadmates.
**How it works (from the game files):**
- The only numbers examined are 2.0 and 0.35, and they come from single-player routes. They are not multiplayer evidence.
- No current multiplayer payload setup has been identified.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Whether any multiplayer payload file exists in the current build.
- Any damage, radius or flight number for multiplayer.
**Could go on the site now:** Nothing.

### Recon drone
**What the game says it does:** No in-game description recorded.
**How it works (from the game files):**
- The drone has a life-time branch and an out-of-bounds branch. A branch is not a measured lifetime.
- Newer than the guide in the project notes: the default list holds a maximum lifetime of 80 and a 45 variant for the battle royale mode (units not stated). The guide said no duration was proved. Treat 80 as a stored default, not a measured flight time.
- Spotting: 60 distance unzoomed and 160 zoomed, angles 10 and 5, gadget spotting radius 40 every 1.5 (units not stated).
- Out-of-bounds timer rises at 1 times frame time, falls at 2 times, is capped by a named limit and checked every 0.25 s. The limit's default is 3, read as seconds (unconfirmed).
- Weapon default list: capacity 1, 1 magazine, refill delay 30. Rangefinder maximum 1000; nearby-projectile trigger range 0.5 (units not stated).
**Changed since October:**
- The "Drone_Destroy Gadget Cooldown" setting (was 5) was removed. This is a drone-named row; whether it applied to the recon drone specifically is not stated beyond the name.
**Not known yet:**
- Battery or flight time.
- Which mode reads which default row.
- Whether the recon-to-TRV150 variant link is real.
- Whether the 80 lifetime is a real in-match limit.
**Could go on the site now:** Spotting distances 60 and 160 and the 40 gadget radius are stored and named, but units are not stated, so check in game first. Lifetime 80 needs a flight timing.

### Night vision / NVG
**What the game says it does:** Both recorded descriptions are only "NVGs".
**How it works (from the game files):**
- Three number triples are stored: duration 51 / 1 / 99, degradation start 0.25 / 0 / 1, exposure offset -2 / -10 / 0. Which member is default, minimum or maximum, and the units, are not assigned.
- The gadget files reach a captured relay and a lighting setting. That is all that is shown.
- No depletion equation is known.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- What the triples mean.
- Whether night vision drains or has any time limit.
- What "exposure offset" does visibly.
**Could go on the site now:** Nothing. The card text is just "NVGs".

### Deployable Mortar
**What the game says it does:** Fires high-explosive or smoke rounds indirectly, with minimap or manual aiming. It reveals itself when it fires and gets more accurate with repeated shots at one place.
**How it works (from the game files):**
- Shell files (HE and smoke) both store launch speed y 48.3 and z 31.37, reload 2.65, heat per shell 0.03, heat drop 0.25 per second, magazine 1. Units for speed and reload are not stated.
- HE shell: unlimited magazines, refill delay 8. Smoke shell: 3 magazines, refill delay 45, refills 1. Weapon file: delay 90, 1 round, 1 magazine. Body: 50 health, no regeneration.
- HE blast damage 60, inner radius 2.444, blast radius 7.622. By the damage grid it does 60 to soldiers, 0 to tanks and IFVs, 60 to helicopters, jets, flyers and light vehicles (joined by name only, no EA figure).
- HE direct hit: registry damage 100 (own value 200).
- Estimate: speed about 57.6 and about 57 degrees, up to about 309 range with no drag and gravity 9.81 (unconfirmed, upper estimate). Reload 2.65, or 1.99, 2.21 or 1.65 with three multipliers (unconfirmed which applies).
- An older read of the weapon file showed a launch speed of z 0. That disagrees with the shell files and is not reconciled.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Real shell cadence.
- Which reload multiplier applies and when.
- How HE or smoke is selected.
- How the accuracy improvement works.
- Why the weapon file shows z 0.
**Could go on the site now:** HE blast damage 60 with radius 7.622 and the 50 health look solid (stored, named). The reload 2.65 needs the Supply Crate timing test first.

### Precision Strike
**What the game says it does:** An automated indirect-fire system described as directing 120 mm mortars.
**How it works (from the game files):**
- No stored numbers are recorded for this gadget.
- Call-in strike numbers listed elsewhere are candidates only. Nothing shows this gadget fires them.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Every number. Damage, radius, shell count and timing are unknown.
**Could go on the site now:** Nothing.

### M320 HE
**What the game says it does:** An impact explosive for structures and for infantry behind cover. Can be used alone or fitted under a weapon with a Gadget Mount.
**How it works (from the game files):**
- The 40 mm HE grenade stores blast damage 120, inner radius 1, blast radius 5. It has no stored falloff curve.
- By the damage grid: 120 on soldiers, 6 on tanks and IFVs, 96 on helicopters, jets, flyers, Vectors, RHIBs, quads and bikes (joined by name only, no EA figure).
- The impact object has a material but no damage number.
- No effective reload or total damage has been established.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Reload and ammo reserve.
- Whether damage falls off with distance in play.
- Effective damage in play.
**Could go on the site now:** Blast damage 120, blast radius 5 and inner radius 1 are stored and named. Radius units and the soldier-versus-vehicle results need an in-game check.

### M320 LVG
**What the game says it does:** A 40 mm low-velocity HE round, used alone or under a weapon.
**How it works (from the game files):**
- The guide gives no stored numbers for this gadget.
- The newer project notes list a blast radius of 3.5 with a stored minimum 2 and maximum 5 (unit not stated). This is now removed, see below.
**Changed since October:**
- The setting "M320_LVG_BlastRadius" (was 3.5) was removed. Where the blast radius now lives is not stated.
**Not known yet:**
- Damage, radius and reload in the current build.
- Where the radius is stored now.
**Could go on the site now:** Nothing. The 3.5 radius is out of date.

### M320 Flash
**What the game says it does:** Burrows through a surface and releases a flashbang on the far side.
**How it works (from the game files):**
- The flashbang, M320 flash and stun drill store the same rows. Blind duration in front 3.5 close and 2.5 far, sides 1.5 and 1.0, behind 0.6 and 0.2. Close range 6, maximum range 12. Angle in front 60 and sides 90 (units not stated).
- The flashbang rule file uses the view angle and range to pick the effect. The M320 flash is not named in it, so sharing this rule is only inferred (unconfirmed).
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Which main projectile the gadget uses in standard multiplayer.
- Whether the burrow depth, delay or range apply as expected.
- Units for durations and ranges.
**Could go on the site now:** The blind durations could be shown as "stored default", but units are unconfirmed, so one in-game timing is needed first.

### M320 Thermobaric
**What the game says it does:** Little initial damage, then it stuns and burns. Used alone or under a weapon.
**How it works (from the game files):**
- The grenade stores blast damage 50 in the default list (its own file holds 30), inner radius 2, blast radius 3. No falloff curve.
- By the damage grid: 50 (or 30) on soldiers, 2.5 on tanks and IFVs, 20 on helicopters and jets, 10 on flyers, Vectors, RHIBs, quads and bikes (joined by name only).
- The fire effect file stores a tick interval 0.4 and two stages, 8 / 2 and 5 / 1.5. What the two numbers in each stage mean is open (units not stated).
- The default list had a fire damage duration of 4.0 (now removed).
**Changed since October:**
- "Thermobaric fire damage duration" (was 4.0) was removed. The guide quoted this, so it is out of date.
- Removed: "Thermobaric NEW Only Sprint Penalty duration" (was 1.0).
- Removed: "Thermobaric full concussion effect duration" (was 1.0).
- Removed: "Thermobaric full concussion effects" (was false).
**Not known yet:**
- Whether the 50 or the 30 applies.
- What the burn stage numbers mean and how long the burn lasts.
- Why the burn numbers do not follow the incendiary pattern.
- What replaced the removed duration and concussion settings.
**Could go on the site now:** Nothing solid. Blast radius 3 and inner 2 are stored but the 50 versus 30 damage question (test: one grenade at a soldier's feet) and the removed duration make it unsafe.

### M26 MASS
**What the game says it does:** A bolt-action 12-gauge buckshot shotgun.
**How it works (from the game files):**
- Default list: capacity 5, 2 magazines, refill delay 60 (unit not stated).
- Reload 3.53 in the weapon file and the default list. The file also has an entry of 3 for rounds left. Which applies is not shown (units not stated).
- The 12-gauge frag projectile has no stored falloff curve.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Pellet count, damage and spread. None are recorded.
- Which reload entry applies.
- Which ammo path and firing file is used.
**Could go on the site now:** Capacity 5 and 2 magazines are stored and named. Reload needs an in-game timing. Damage cannot be shown.

### M26 MASS Dragonsbreath
**What the game says it does:** Reduced impact damage, with burning on the target and fire on the ground.
**How it works (from the game files):**
- No numbers are recorded in the guide.
- The project notes list a registry row for the maximum distance of low-damage effects of 20 (min 0, max 30, unit not stated). It is named for the Dragon round but is not tied to the burn in any source.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Burn damage and time.
- Impact damage.
- Whether the 20 relates to range.
**Could go on the site now:** Nothing.

### RPG-7V2
**What the game says it does:** An unguided impact rocket. It is stronger against the thinner side, top and rear armour.
**How it works (from the game files):**
- The projectile's own damage is 135, while the default list says 125. EA's dated tank figures are 188 front and 500 rear. They are not found by reading the 135 directly.
- The damage grid for its material gives 2 on tanks and IFVs, 9 on helicopters, 10 on jets, 5.5 on light vehicles, 5 on quads and bikes, 1 on soldiers. The own 135 was not run through it.
- Reload 3.4 in both the weapon file and the default list. Default list: capacity 1, 3 magazines, refill delay 18 (units not stated).
- Fire rate 150, launch speed z 117.99 (units not stated).
- October-era older read: blast damage 70, blast radius 6 (an old build, not current).
**Changed since October:** Nothing in the named settings. (Two unnamed rows, a bare "Radius" 6 to removed and a bare "Range", could touch this gadget. See the last section.)
**Not known yet:**
- What damage is dealt in play.
- Flight and activation details.
- Whether the 135 or the 125 applies.
**Could go on the site now:** Reload 3.4 and capacity 1 with 3 magazines. Damage needs an in-game test, because the stored 135 and the default 125 disagree.

### AT4 / M136
**What the game says it does:** A crosshair-guided anti-vehicle missile. Side, top and rear armour are described as weaker.
**How it works (from the game files):**
- Own damage 125. EA's dated tank figures are 207 front and 550 rear.
- Reload 3.66 in the weapon file, its rounds-left entry and the default list. Default list: capacity 1, 2 magazines, refill delay 30 (units not stated).
- The explosion stores blast radius 5, inner radius 2, shockwave radius 7.5, read as metres (unconfirmed, names inferred from other files). No falloff curve is stored.
- Fire rate 300, launch speed z 30 (units not stated).
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Damage in play.
- Flight behaviour and activation.
**Could go on the site now:** Capacity 1 with 2 magazines, reload 3.66 and refill delay 30 are stored with no dispute. Radius needs an in-game check, since the unit and the field names are inferred.

### MBT-LAW
**What the game says it does:** An aim-and-fire anti-tank missile with self-guided top attack.
**How it works (from the game files):**
- Own damage 100. EA's dated tank figure is 240 flat.
- The missile file stores max speed 300 and engine strength 100. EA's 1.3.1.0 speed range is 75 to 300 and acceleration range 50 to 100, so the stored values equal the upper ends of EA's ranges. EA's "acceleration" is read as engine strength (unconfirmed).
- The weapon file stores lock time 3 and lock range 650 in October (units not stated). EA states neither.
- Reload 3.4. Default list: capacity 1, 3 magazines, refill delay 18.
- Explosion: blast radius 4, inner radius 1, shockwave radius 6.5, read as metres (unconfirmed). No falloff curve.
- Newer project notes also store an unlock time of -1 and a release time of 5 for the October read.
**Changed since October:** Nothing found. The lock settings in this launcher's own file are identical on 1.4.3.5 and 2.1.2.5 (checked 26 November 2026). Several lock entries in the game's settings table share one name and sit in a different order on the two builds, which reads as change but is not shown to be one. The open point is older: the launcher's own file and the settings table hold different lock numbers, and which one the game uses is not settled.
**Not known yet:**
- Effective damage, flight path and activation.
- Current lock time and range.
- Whether lock settings apply to a player firing it.
**Could go on the site now:** Max speed 300, reload 3.4 and capacity 1 with 3 magazines are stored and match EA's upper range. Lock numbers wait on which source the game uses.

### Javelin
**What the game says it does:** A long-range lock-on launcher with faster and longer locking against targets painted by a laser or dart.
**How it works (from the game files):**
- Missile file stores max speed 60 (default list 70) and engine strength 40. EA's 1.3.1.0 notes give a speed of 60 to 70, so 60 equals EA's new value. EA states no acceleration.
- October lock numbers in the weapon file: lock time 1.4 (EA says 1.8 down to 1.4) and two lock ranges, 650 and 780 (ratio 1.2). Units not stated.
- The project notes have a second October read of the same file with different numbers: lock times 1.8 and 1, ranges 650 and 750, minimum range 39. The two October reads disagree and neither is confirmed.
- Reload is -1 in the file and the default list, so no timed reload is stored.
- Default list: capacity 1, 3 magazines, refill delay 30. Fire rate 300, launch speed z 10 (units not stated).
- The blast falloff curve exists in the project notes: full damage to 12.5% of the radius, then steps down to 67% and 33% (a curve file named for the Javelin). The guide does not mention it.
**Changed since October:** Nothing found. The lock settings in this launcher's own file are identical on 1.4.3.5 and 2.1.2.5 (checked 26 November 2026). Several lock entries in the game's settings table share one name and sit in a different order on the two builds, which reads as change but is not shown to be one. The open point is older: the launcher's own file and the settings table hold different lock numbers, and which one the game uses is not settled.
**Not known yet:**
- Effective lock benefit and flight.
- Which lock range applies to a painted target.
- Current lock time and range.
- Whether a timed reload exists.
- EA gives no base range.
**Could go on the site now:** Max speed 60 and capacity 1 with 3 magazines. Lock numbers wait on which source the game uses. Reload cannot be shown.

### Panzerfaust 3
**What the game says it does:** Only the generic label "Anti-Vehicle Launcher".
**How it works (from the game files):**
- Direct hit uses the same damage material as the RPG. Stored damage 100 is only in the weapon file (no default row, may be stale).
- Damage grid results: standard direct 200 on tanks and IFVs, 900 on helicopters, 1000 on jets, 550 on light vehicles, 500 on quads and bikes, 100 on soldiers.
- Standard blast 130 stored, 0 on tanks, 39 on light vehicles, 1105 on quads and bikes, 130 on soldiers.
- A second round (DM32) has direct 100 stored (100 on tanks, 700 on helicopters and jets, 450 on light vehicles, 1100 on quads and bikes) and blast 230 stored (0 on tanks, 69 on light vehicles, 1955 on quads and bikes, 230 on soldiers).
- All of these are before the aimed-hit factor.
- Reload 4.96 in the weapon file and rounds-left entry. No default row. Fire rate 257, launch speed z 162.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Real hit damage. The source expects 300 on a tank's side after the aimed-hit factor, but this has not been checked.
- Whether the 100 is stale.
- The full multiplayer name and menu entry.
- How the two rounds are chosen.
**Could go on the site now:** Reload 4.96 and fire rate are stored. The damage results should wait for the tank-side hit test.

### Railgun
**What the game says it does:** No in-game description recorded.
**How it works (from the game files):**
- Direct hit stored damage 150. By the damage grid: 375 on tanks and IFVs, 525 on helicopters and jets, 825 on light vehicles, 1350 on quads and bikes, 150 on soldiers (before the aimed-hit factor).
- The blast part stores 0 damage.
- Default list: projectile speed 1029 (read as m/s from the row name), capacity 1, 11 magazines, reload 4.266 (read as seconds). Damage falloff from 100 to 200 with 150 at both ends reads as no falloff (inference, unconfirmed).
- It uses the same blast curve file as C4 and the drone payloads. Which part uses it is not stated.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Whether a hit applies exactly these values. The source expects 750 on a tank's rear.
- Which part uses the borrowed blast curve.
- Whether the "no falloff" reading is right.
**Could go on the site now:** Stored damage 150, speed 1029, 11 magazines and reload 4.266 are stored and named. Damage on vehicles needs the tank-rear hit test.

### Stinger
**What the game says it does:** A lock-on air-defence launcher with self-guidance. It interacts with countermeasures.
**How it works (from the game files):**
- The gadget's own wrapper values are zero, but that does not make damage zero. The controlled values are damage 100, drag 0 and max speed 400, with inherited launch speed 350 and time to live 18.
- Missile files by name: one stores max speed 400 and engine strength 50, a second stores 350 and 200, and the vehicle file stores 540 and 65. EA's 1.3.1.0 speed range is 540 to 480, which neither launcher file stores. Which missile file is used is joined by name only (unconfirmed).
- October lock numbers in the weapon file: lock time 1.5 and lock ranges 550 and 687.5 (ratio 1.25). EA's base range is 650 to 550. Units not stated. The project notes have a different October read (lock range 650 and 750); both are unconfirmed.
- Reload 3.4, with 3.66 in its rounds-left entry. Default list: capacity 1, 3 magazines, refill delay 18.
- Explosion: blast radius 5, inner radius 1, shockwave radius 7.5, read as metres (unconfirmed). No falloff curve.
**Changed since October:** Nothing found. The lock settings in this launcher's own file are identical on 1.4.3.5 and 2.1.2.5 (checked 26 November 2026). Several lock entries in the game's settings table share one name and sit in a different order on the two builds, which reads as change but is not shown to be one. The open point is older: the launcher's own file and the settings table hold different lock numbers, and which one the game uses is not settled.
**Not known yet:**
- Missile speed in play.
- Which reload entry applies.
- Whether a designated helicopter can be locked at 675.
- The 1.25 ratio does not fit EA's 20% designator bonus. Cause unknown.
- Current lock numbers.
**Could go on the site now:** Capacity 1 with 3 magazines and refill delay 18 are stored. Lock numbers wait on which source the game uses, and missile speed needs a timing test.

### IGLA
**What the game says it does:** It needs you to keep tracking the target with your sight, and it can reacquire targets in flight.
**How it works (from the game files):**
- Current stored missile values (now named in the game's table): damage 100, max speed 480, engine strength 100, engine ignition delay 0.3, engine life 35, initial speed 500, time to live 40. Units not stated.
- Guidance switches on after 0.3. Turn angle limits 35 to 420 and a turn multiplier of 30 (units not stated). The missile's own lock settings list a ray length of 300 and "lock on targets below radar" true. Whether the weapon's lock settings override these is not stated.
- Explosion: blast damage 100, radius 5, inner radius 1, shockwave damage 1, shockwave radius 7.5.
- Weapon lock settings now named for the IGLA: laser-painted lock time 1.0, range 840, minimum range 50, release 0.5, unlock 0.5. Normal (secondary) lock time 1.0, range 700, minimum range 50, release 0.5, unlock 0.5. Units not stated. The 840 to 700 ratio is 1.2, which matches EA's "20%" designator bonus.
- Ammo: capacity 1, 3 magazines, refill delay 18, fire rate 300, forward shot speed z 50, a muzzle blast of 120 damage with radius 1. Reload 3.4 (a 2.33 entry also exists; which applies is unknown).
**Changed since October:** The IGLA's own file is unchanged (lock times 1.8 and 1.2, ranges 600 and 800, minimum range 39, checked 26 November 2026). The game's settings table holds different numbers, listed above, and now names them as IGLA rows:
- The missile max speed is 480 and engine strength 100. The guide said 640 and 65, so those are out of date. The new values match EA's 1.3.1.0 new speed (480) and the top of its acceleration range (100).
- The guide's damage 100, initial speed 500, time to live 40, and blast 5 / 1 / 7.5 still match the now-named rows.
- The lock times, ranges (840, 700) and ammo layout (3 magazines, refill 18, reload 3.4) match what the guide gave for October.
- Newly named only: minimum range 50 on both locks, release and unlock 0.5, turn angles, ignition delay, engine life 35, muzzle blast and shot speed z 50.
**Not known yet:**
- Effective damage, flight and activation in play.
- Which reload entry (3.4 or 2.33) applies.
- Whether the missile's ray length 300 or the weapon's 840 and 700 governs lock range.
- Missile speed in play.
- Some earlier project notes quote the October IGLA lock rows as 1.8 and 1.2 with ranges 600 and 800 and minimum range 39. That disagrees with both the guide and the current rows, which win here.
**Could go on the site now:** Max speed 480, blast damage 100 with radius 5, lock ranges 840 and 700, lock time 1.0, capacity 1 with 3 magazines. All are stored and named now. Check lock ranges in game, since units are not stated and the range owner is not settled.

### Drill Launcher / Breaching Dart
**What the game says it does:** A breaching round sticks on and, a moment later, releases a blinding blast on the far side of a surface. It does limited damage if it hits a soldier directly.
**How it works (from the game files):**
- The blast object stores damage 40 and radius 1, inner radius 1, shockwave damage 1 and radius 7. The same values exist for the gas version. The 40 has no default row, so it may be stale.
- By the damage grid: 16 on tanks and IFVs, 100 on helicopters, 120 on light vehicles, 40 on soldiers, before any aimed-hit factor.
- Reload 2.53 in the weapon file and rounds-left entry. No default row.
- A default row from a differently named file (X95BRE_BreachingDart, joined by name only) has capacity 1, 3 magazines, refill delay 15.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Effective damage, flight and activation.
- Whether the 40 is stale.
- Flash duration and delay.
- Whether the name join is correct.
**Could go on the site now:** Reload 2.53 is stored and unchallenged. Everything else needs an in-game check.

### Airburst Incendiary Launcher
**What the game says it does:** The menu describes a 25 m airburst and an incendiary cloud that hides vision and clears or prevents spotting.
**How it works (from the game files):**
- The main projectile has initial speed 250 and time to live 0.25. A lingering object has 0 and 5. The lingering 5 is not proved to be burn time.
- No stored 25 matching the airburst distance was found.
- Reload 2.53, same in the default list. Default list: capacity 1, 3 magazines, refill delay 30. Fire rate 100, launch speed z 100 (units not stated).
- The fire effect file stores interval 0.3 and one stage of 10 (whole number) and 15 (decimal), on the same body material as other fire. One reading: 10 damage over 15 seconds, one tick per 0.3 (unconfirmed). It fits the incendiary grenade but not the thermobaric.
**Changed since October:**
- The setting "AirburstIncendiary_SmokeBlockingRadius" (was 2.5) was removed. This is a smoke-blocking radius from the default list, not something the guide quoted.
**Not known yet:**
- Real damage per second and the burn time.
- The 25 m airburst source.
- What now holds the smoke-blocking radius.
- How the menu text maps to the game files.
**Could go on the site now:** Capacity 1 with 3 magazines, refill delay 30 and reload 2.53. The burn numbers need the health-lost-per-second test.

## Grenades, mines, explosives and call-ins

### Frag Grenade
**What the game says it does:** A grenade that starts its fuse when it hits something. It is good behind cover and hurts most when close.
**How it works (from the game files):**
- Blast damage 100, inner radius 1, blast radius 5 (units not stated; the guide reads them as metres, unconfirmed).
- Damage fades with distance in steps, from a stored curve: full damage out to 20% of the radius, then 80%, 60%, 40% and finally 20% at the edge. The step positions assume straight lines between points (unconfirmed).
- Against soldiers the stored damage multiplier is 100 (full). Against tanks and IFVs it is 0. Against helicopters, jets and light vehicles it is full.
- Fuse: GADGETS.md stores a minimum time before blast of 1.1 and a delay after a bounce of 1.4 in the October build (unit not stated).
**Changed since October:** Delay after bounce 1.4 -> 1.1. The 1.4 is out of date; use 1.1. No other number on this card changed in the named settings.
**Not known yet:**
- How the game blends between curve points (straight lines is an assumption).
- Total damage in a real match.
- Whether the guide's suggested tests hold: about 50 at 3.5 m and 20 at 4.5 m from a full-health soldier.
**Could go on the site now:** Blast damage 100, blast radius 5 and the 0 against tanks look solid (stored, named, not disputed). The bounce delay (1.1 now) is stored and confirmed by the ledger. Falloff steps and real damage at range need an in-game check first.

### Mini V40
**What the game says it does:** A lighter grenade with a longer throw and less damage than the Frag.
**How it works (from the game files):**
- Historical blast damage 40 versus 100 for the Frag, blast radius 5. This is an older source comparison, not a fresh read.
- Carry numbers: capacity 1, 2 magazines, refill delay 30 (units unconfirmed).
- Nothing stored proves the longer throw or the lighter carry load.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Throw range.
- Carry load effect.
- Current damage (the 40 is from older evidence).
**Could go on the site now:** Capacity 1 and 2 magazines are stored and named. The 40 damage and 5 radius need re-checking on the current build before showing.

### Anti-Tank Grenade
**What the game says it does:** A thrown grenade that opens a parachute and drops onto the target from above.
**How it works (from the game files):**
- Blast damage 50, inner radius 0.75, blast radius 1.5 (units not stated).
- After the game's damage multiplier by target type: 42.5 on soldiers, 150 on tanks and IFVs, 325 on helicopters, 500 on jets, 350 on small flyers, boats and bikes.
- No stored falloff with distance.
- Carry numbers: capacity 1, 2 magazines, refill delay 30 (units unconfirmed).
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- How the parachute top attack actually works.
- Whether 150 on a tank holds in play (suggested test: one grenade on a full-health tank).
- Falloff with distance.
**Could go on the site now:** Damage 50 and radius 1.5 are stored and named. The per-target numbers (150 on tanks and so on) are calculated from stored numbers and need one in-game check.

### Incendiary Grenade
**What the game says it does:** A short fire blast followed by burning. Going prone is said to reduce fire damage.
**How it works (from the game files):**
- Flight speed 300 and lifetime 10 (units not stated). The initial blast damage is 0 with blast radius 4.
- Fire damage lives in separate effect files, not the blast. Stored steps are pairs of numbers; read as damage then time they would be 15 until 2.5, 10 until 7, 5 until 10 (unconfirmed reading, units not stated).
- Fire check interval 0.1 (unit not stated). A separate exit-fire effect uses 3 / 1 at interval 0.2.
- Grenade radius 1.7, height 1.0, fire damage duration 2.5 (no link to the stored steps is shown).
- Carry numbers: capacity 1, 1 magazine, refill delay 30.
**Changed since October:** Setting removed: "Thermobaric fire damage duration" (was 4.0). The guide's card mentions this 4.0 as the thermobaric fire, so it is now out of date. Other thermobaric settings were also removed; see the last section.
**Not known yet:**
- Burn time and damage per tick.
- Whether the damage-and-time reading is right.
- Units (per tick or per second).
**Could go on the site now:** Initial blast 0 with radius 4, and the 10 lifetime of the projectile. Burn damage needs an in-game check first (health lost in the first and eighth second).

### Throwing Knife
**What the game says it does:** An arcing thrown blade. Headshots are described as lethal, and non-fatal hits delay health regeneration for 10 seconds.
**How it works (from the game files):**
- Firing values from the weapon file: rate of fire 550, magazine capacity 1, throw speed 44.97 (units not stated).
- A separate older projectile file stores damage 50 / 50, falloff 5 / 15, speed 350 and lifetime 10. The two owners and dates are not reconciled.
- Carry numbers: capacity 1, 5 magazines, refill delay 15 (units unconfirmed).
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Which damage figure applies now.
- Whether the 10 second regeneration delay is stored anywhere.
**Could go on the site now:** Capacity 1, 5 magazines and refill delay 15. Damage 50 needs an in-game check because the sources do not agree on owner and date.

### Decoy
**What the game says it does:** A decoy that copies the owner's stance, is spotted when placed, and can hide nearby friendly scope glint.
**How it works (from the game files):**
- Carry numbers: capacity 1, 3 magazines, refill delay 12 (units unconfirmed).
- A rule file applies an anti-glint effect lasting 2.1 every 2, within 5 of the decoy. Units are not stated, and the reading that cover is continuous is inferred.
- A separate fake effect fires at a random interval of 1.5 to 6.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Effective radius and lifetime.
- How the glint replacement really works.
**Could go on the site now:** Capacity and magazine counts only. Radius and timings need an in-game check.

### C4
**What the game says it does:** Charges you place and set off yourself, for use against structures, vehicles and soldiers.
**How it works (from the game files):**
- Blast damage 100, blast radius 3, inner radius 1, shockwave radius 5 (units not stated). An old row saying 180 is tied to no saved file, so 100 stands.
- EA's patch notes give 350 against tanks. This is a separate dated statement, not the 100.
- Falloff curve: full damage to 60% of the radius, then 80%, 40% and 20% at the edge. Steps assume straight lines (unconfirmed).
- Carry numbers: capacity 1, 4 magazines, refill delay 30 (units unconfirmed). The 4 was confirmed in game on 26 November 2026. Arm delay 0.5.
**Changed since October:** Setting removed: "C4_Arm Delay" (was 0.5), so the arm delay above is out of date. The old unattached damage rows for C4 (180 and related) were also removed, which fits the guide's finding that they were never used. GADGETS.md still lists arm delay 0.5 without a build note. Inside its own files (re-checked 26 November 2026): Two unnamed counts in its weapon file went from 2 to 1, and one point of its blast curve from 0.99579 to 1.0.
**Not known yet:**
- Whether a C-4 does 350 to a full-health tank in play (630 would mean the unused row is in use).
- Damage to a teammate at 2.5 and at 3.5.
- Where the arm delay now lives.
**Could go on the site now:** Blast damage 100, radius 3, and EA's 350 against tanks (labelled as an EA statement). Arm delay should wait for a check, since its setting was removed.

### Claymore
**What the game says it does:** A directional tripwire mine. Moving normally while crouched or prone is said to avoid setting it off.
**How it works (from the game files):**
- Damage comes from a formula: base damage x pellets x sprint modifier x range term x 0.67 if the target has armour, rounded to steps of 5. The base damage, pellet count and pellet limit values are not in the graph.
- The blast object holds BlastDamage 1 and the fragment damage is not found in stored data.
- An earlier match to EA's 50 was wrong: the values 30, 50 and 15 appear in eight different gadgets and are not damage figures. GADGETS.md and the guide agree on this correction.
- Carry numbers: capacity 1, 1 magazine, refill delay 30.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Base damage, pellet count and pellet limit.
- Damage at 1 m (suggested test: health lost to an enemy Claymore at 1 m).
- The trigger area.
**Could go on the site now:** Only the carry numbers and the shape of the formula. Damage numbers need an in-game check.

### AT Mine
**What the game says it does:** A mine armed on the ground to hit vehicles. You cannot stack them or place them too close together.
**How it works (from the game files):**
- Blast damage 300, blast radius 2 (older source table; units not stated). No stored falloff curve.
- The three values 30, 50, 15 shared with seven other gadgets are not its damage.
- Carry numbers: capacity 1, 3 magazines, refill delay 10 (units unconfirmed). Ability active time 1.8 (unit not stated).
**Changed since October:** Setting added: "ATMine_TransportDetectionInterval" = 2. It looks like a check interval for something carried or transported, but the name is all the source gives. Inside its own files (re-checked 26 November 2026): One unnamed number in its file went from 0 to 0.1.
**Not known yet:**
- What the new setting does.
- Trigger rules and in-play damage.
**Could go on the site now:** Capacity 1 and 3 magazines. Damage 300 and radius 2 come from an older table and need a recheck before showing.

### PTKM-1R
**What the game says it does:** Finds targets by sound and fires a top-attack payload.
**How it works (from the game files):**
- Explosion object: radius 4, inner radius 3.99, shockwave radius 8 (units not stated). An inner radius almost equal to the radius suggests full damage across it (unconfirmed).
- Only vehicles moving faster than a set speed and between a minimum and maximum range trigger it. Scan period 0.1. The speed and range values are not in the graph.
- Carry numbers: capacity 1, 1 magazine, refill delay 21 (units unconfirmed).
**Changed since October:** Settings added: civilian vehicle dispersion min 4 and max 12, and civilian vehicle velocity min 10 and max 30 (units not stated). These did not exist in October. Inside its own files (re-checked 26 November 2026): The blast damage in its projectile file went from 160 to 142.
**Not known yet:**
- Trigger radius, timing and damage.
- What the civilian vehicle settings do in play.
**Could go on the site now:** Capacity and refill delay. Everything about damage and trigger needs an in-game check.

### M4 SLAM
**What the game says it does:** A proximity device that fires a fast projectile at vehicles that come near.
**How it works (from the game files):**
- Body explosion: radius 1, inner radius 0.99, shockwave radius 3.5 (units not stated). An older table lists blast damage 100. No stored falloff curve.
- The shared 30, 50, 15 values are not its damage.
- Carry numbers: capacity 1, 3 magazines, refill delay 15 (units unconfirmed).
**Changed since October:** About 25 settings named "GS_M4SLAM..." (aim spread, camera recoil, minimum angles) were removed. They carry a "#2" duplicate-name tag, so they may be a reshuffle and not a real removal. None of the numbers on this card are listed as changed.
**Not known yet:**
- Trigger radius (the capture boundary blocks a radius claim).
- In-play damage.
**Could go on the site now:** Capacity, magazines and refill delay. Damage and trigger range need an in-game check.

### Field upgrades
**What the game says it does:** No in-game description recorded.
**How it works (from the game files):**
- Passive upgrades re-apply an effect on a timer, with the effect lasting slightly longer than the timer (inferred). Timer / effect time: low profile 1.0 / 1.1, stance flak 1.0 / 1.1, mechanized infantry 2.0 / 2.1, vehicle health plus 2.0 / 2.0, enhanced filtering every 0.333 (the guide says seconds; unconfirmed).
- Effect numbers: low profile spot time x 0.667 and spot delay 1.2; flak 0.67; adrenaline shot flak 0.8; giga shield 0.5; gadget over-repair 20; medical triage 20; emergency damage control extra heal 70; resilient auto-regeneration 30 and 2.5; hemostatic smoke 12.5 and 2.5. The roles of these numbers are inferred from names.
- Combat High: a chain of events within 5 of each other builds a stack up to 5. Each stack applies a healing entry (values 5 to 10). GADGETS.md says the events are kills; the guide leaves it open.
- Repeatable Reward stacks up to 4. The faster-armour-plate upgrade passes a 1.5 of unknown role.
**Changed since October:** Nothing in the named settings places itself here by name. "AdrenalineShot_Rank = 5" was removed; the guide mentions an adrenaline shot effect but no rank, so it is listed in the last section.
**Not known yet:**
- Which player action each condition stands for.
- What the numbers mean in play.
- Whether any of these is in standard multiplayer.
**Could go on the site now:** Nothing safely. The numbers are stored, but their roles are guessed from names. Each would need an in-game check.

### Mortar call-in
**What the game says it does:** No in-game description recorded.
**How it works (from the game files):**
- Optional ranging shots first, then volleys. Shells appear 300 above the target, moving down at 100, and land in a random circle.
- Defaults: 2 shells per volley, 2 volleys, fire delay 3.0, 4.0 between volleys, 1.0 between shells, dispersion 8.0, ranging shot count 0 (the guide reads seconds and metres from the names; unconfirmed).
- With the fire-support flag on, shell count is multiplied by 1.25 and rounded down (2 x 1.25 gives 2, so no extra shell at defaults; unconfirmed).
- The link to the Deployable Mortar is by name only. GADGETS.md adds nothing newer here.
**Changed since October:** Nothing in the named settings (the changed settings are not Mortar_ rows).
**Not known yet:**
- Which shell is spawned in play.
- The unexplained value 57.6.
- Whether the call-in exists in standard multiplayer.
**Could go on the site now:** Nothing yet; the unit and availability questions are open.

### Call-in strike munitions
**What the game says it does:** No in-game description recorded.
**How it works (from the game files):**
- Stored damage times a multiplier per target type. Examples: JAGM missile direct 175 (tank 350, helicopter 1575); JAGM blast 160; Mk82 bomb direct 450 (tank 900) and blast 335 (tank 1172.5); 155 mm shell direct 330 and blast 120; carrier-strike missile direct 1000 and blast 160. These files have no registry row, so the values may be stale.
- The kinetic strike file does direct 1000 to soldiers and light vehicles, and 0 to tanks and helicopters.
- Pattern defaults: 18 shells per volley, 1 volley, 0.5709 between shells, dispersion 45, fire delay 4, 2 ranging shots; JAGM map blast radius 10; warning radius 200; air strike warning delay 3 (units from names only).
- Names like "TEMP" and "Beach" hint at placeholder or map-specific files.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- Which call-in fires which file.
- EA figures.
- In-play damage.
**Could go on the site now:** Nothing yet. Even the stored figures are not linked to a named call-in. An in-game test (a tank hit by one JAGM) would come first.

### Sabotage
**What the game says it does:** No in-game description recorded.
**How it works (from the game files):**
- Hold-interact fills in 0.45. A second 30 bar fills only on the ground, read as recharge (unconfirmed).
- On completion it searches near the player (distance 2.4 plus 1, or 3.0 more with the upgrade; units unconfirmed), takes the first enemy vehicle with health, and turns off all its weapons for 29.
- On the vehicle, the sabotaged effect lasts 26, with state steps at 6.5, 10.5, 26 and 28.7. Immobilise lasts 26 minus the first state's 4.0 (22 at defaults, unconfirmed).
- The player 29 and the vehicle 26 differ with no stated reason.
**Changed since October:** Nothing in the named settings.
**Not known yet:**
- What the state steps mean.
- Whether it exists in standard multiplayer (the graph is Granite-named).
- Real in-play duration.
**Could go on the site now:** Nothing yet. Availability is unknown.

## New since October

Compared against the game's full file listing on each build, only three gadget folders are new since October: the
DS Pulse and the M320 AT (both added in 2.1.1.0) and the Signal Jammer (2.1.2.0, card above). The other folders that
first appear in the current capture already existed in October and were simply not captured then; they are mission,
loot and battle royale items (zipline, thermite and demolition charges, revive pen, keycards, cameras and so on) and
have no card.

### DS Pulse
**What the game says it does:** In-game text not looked up.
**How it works (from the game files):**
- A battle pickup that behaves like a firearm. Named settings: magazine 160, 1 magazine, fire rate 480 (unit not
  stated, read as rounds per minute on other weapons), projectile speed 300.
- Reload 6.7, or 5.83 with rounds left. Replenish delay 5, with automatic magazine replenish off.
- It appears in the battle royale loot tables as "Pulse Rifle", with a setting that disables it there set to true.
**Changed since October:** New in 2.1.1.0.
**Not known yet:**
- Damage, range and where it spawns in standard multiplayer.
- Whether it is currently enabled anywhere.
**Could go on the site now:** Nothing until its damage and availability are traced.

### M320 AT
**What the game says it does:** In-game text not looked up.
**How it works (from the game files):**
- An underbarrel M320 variant. Its folder holds four files (an ability, an unlock, a customisation entry and
  model data) and no weapon file of its own, so its firing values are not in its folder.
- The settings list has on-off switches for it under two weapon-skin names, all set to false.
**Changed since October:** New in 2.1.1.0.
**Not known yet:**
- Which weapon file and projectile it uses, and every number.
- Whether it is available to players.
**Could go on the site now:** Nothing.

## Site-ready stats at a glance

Each card's own verdict, gathered in one place. "Now" means stored, named and not disputed; it still waits on the
question above wherever the gadget holds a second, different value.

| Gadget | Could show now, and what needs a check first |
|---|---|
| Defibrillator | Solid: full charge 1.0 and stored minimum 0.3 (show as stored defaults; mention EA's 0.35 note), 3 magazines, friendly range 2.0 and enemy range 1.5 (units need an in-game check). Needs an in-game check first: health restored per charge level, damage to enemies. |
| Supply Pouch | Solid: heal over time 20 with no instant heal (unit needs an in-game check), the 0.1 post-throw delay (stored; whole delay unconfirmed), refill delay 39 (unit not stated). Needs a check: ammo per pickup, carried count, lifetime. |
| Supply Crate / Supply Bag | Solid: open time 0.4 and refill delay 15 (units unconfirmed); 5.0 pulse interval (shape inferred, so mark it). Needs an in-game check: ammo per pulse, heal rate, radius. |
| Medic Crate | Nothing yet. Its identity is unproved. |
| Ammo Bag | Nothing. |
| Vehicle Supply Crate | Only build time 0.6 and interval 5.0 from the file values, with units unchecked. Do not show "15 supplies": its setting was removed. |
| Adrenaline Shot | Solid: duration 8 (unit unchecked), 0.8 explosive multiplier (name-read, so label as unconfirmed). Needs a check: heal amount, sprint boost size. Do not show rank 5. |
| Repair Tool | Stored and named: repair 40 and anti-repair 30 per second (standard), 60 / 45 (active repair), range 2, interval 0.1. All need an in-game unit check first. |
| Restock Allies / ActiveMedic | Only the in-game text values (10 s, 1.7 s), labelled "stated by the game, not found in the files". Radius 7 needs a unit check. The 1.7 s needs an in-game timing. |
| Active Resupply | Nothing. |
| Hemostatic smoke upgrade | 12.5 and 2.5 match both the screen text and the stored values, so they are the best candidates. Units still need an in-game check. |
| Squad revive | Solid: total 4.72 and Support 2.2 (named, re-read; unit not stated in the files). Needs a check: health given on revive (the operator describes half health on a tap, not measured), the 1.7 case, whether the buffer is inside the 4.72. |
| MP-APS | Solid enough to show: default lifetime 5 and 3 interceptions (named, stored, not disputed; say "default, may be changed by the game remotely"). Upgrade bonuses (+3 and +2) are stored too but the upgrade link is guessed. Needs an in-game check: range, real lifetime in seconds, how many shots it really stops. |
| EIDOS / GPDIS | Solid: default lifetime 5, default interceptions 3, stored intercept range 5 (all named and stored; show without a unit). Needs an in-game check: real range, whether jamming really turns it off. |
| Deployable Cover | Little is solid. The four stored 200.0 part values and the 30 refill delay are stored and named, but showing "800 health" is not allowed. Needs an in-game check: total health, resistances, pulse radius. |
| Smoke Grenade | Only the stock (1 charge, 2 spares, 18 refill) is solid. Cloud radius and duration need an in-game check. |
| M320 Smoke | Nothing solid. The guide holds no numbers for it, and the removed settings need re-finding under a new name before any figure is shown. |
| Flashbang Grenade | Solid: the six blind-time numbers, close range 6, max range 12, angle limits 60 and 90, and the stock (all named and stored). Needs an in-game check: the +0.2, real blind effect, whether the numbers match what the player sees. |
| Concussion Grenade | Solid: the three ring sizes and times, the fuse numbers and the stock (stored and named, though possibly overridden by the game). Needs an in-game check: units, how strong each ring is, whether ADS and sprint block both last the full time. |
| Gas Mask | Not yet. The numbers are stored, but it is not established that standard multiplayer uses this default set. Needs an in-game check first. |
| Soft Armor and Ceramic Armor | Nothing. The guide says these labels must not become a generic armor layer. Needs an in-game check that armor exists in standard multiplayer. |
| T-UGS | Solid: radius 15, duration 2, pulse delay 1.5, upgrade multiplier 1.5 (stored and named; show with "default"). Needs an in-game check: real units, crouch and prone avoidance, device limit. |
| Proximity Grenade / MTN-55 | Solid: radius 7, duration 2, delay 1, upgrade multiplier 1.5 (stored and named). Needs an in-game check: real range, whether vehicles are marked, how it treats crouching. |
| Mobile Jammer | Solid: radius 10, refill delay 45, upgrade radius multiplier 2.0. Needs an in-game check: what the jam disables and for how long. |
| Drone electronics disruption | Nothing solid. The cooldown of 5 is gone from the named list. Everything else needs an in-game check. |
| Laser Designator / PLD | Solid enough: the three spot durations 5 / 30 / 20 and MarkTarget 15 (stored; EA's 9 must stay separate). Needs an in-game check: the true range by zoom level, the designation timer, the 20% benefit, and the removed world-lock rows. |
| Tracer Dart Gun | Solid: stock 1 / 3, refill delay 9, reload 3.38. Needs an in-game check: mark duration, how much the 11 changes lock range, whether it works through countermeasures. |
| Hardware Suppression System / Lancet | Solid: the three detection distances 30 / 60 / 80, tracking times 0.25 / 0.025, reload 3.233 (stored and named). Needs an in-game check: units, the "three combined" count, which targets are actually stopped. |
| UAV drone | Nothing. There is no stored number to show. |
| Signal Jammer | Solid enough: radius 21 (standard multiplayer), health 25, regeneration delay 5, refill delay 30, 1 charge (stored and cross-checked against the update's setting list). Needs an in-game check: what the jam does, the radius unit, whether the squad-spawn block is on, and the unlock. |
| Spawn Beacon | Nothing numeric is solid. The in-game description (single use, one spawn per squad member) could be shown as text. The refill delay 30 needs an in-game timing check first. |
| Assault Ladder | Nothing. The ramp angle 45 is a stored name and value but its unit is unstated, so check in game before showing it. |
| EOD Bot | Repair 40 and anti-repair 30 (stored, named, same as the repair tool pattern) are the best candidates. The mine blast damage 150 and radius 2 are stored but the damage reading needs an in-game check. Lifetime 120 needs a timing check, because the countdown condition is undecoded. |
| Payload drone | Nothing. |
| Recon drone | Spotting distances 60 and 160 and the 40 gadget radius are stored and named, but units are not stated, so check in game first. Lifetime 80 needs a flight timing. |
| Night vision / NVG | Nothing. The card text is just "NVGs". |
| Deployable Mortar | HE blast damage 60 with radius 7.622 and the 50 health look solid (stored, named). The reload 2.65 needs the Supply Crate timing test first. |
| Precision Strike | Nothing. |
| M320 HE | Blast damage 120, blast radius 5 and inner radius 1 are stored and named. Radius units and the soldier-versus-vehicle results need an in-game check. |
| M320 LVG | Nothing. The 3.5 radius is out of date. |
| M320 Flash | The blind durations could be shown as "stored default", but units are unconfirmed, so one in-game timing is needed first. |
| M320 Thermobaric | Nothing solid. Blast radius 3 and inner 2 are stored but the 50 versus 30 damage question (test: one grenade at a soldier's feet) and the removed duration make it unsafe. |
| M26 MASS | Capacity 5 and 2 magazines are stored and named. Reload needs an in-game timing. Damage cannot be shown. |
| M26 MASS Dragonsbreath | Nothing. |
| RPG-7V2 | Reload 3.4 and capacity 1 with 3 magazines. Damage needs an in-game test, because the stored 135 and the default 125 disagree. |
| AT4 / M136 | Capacity 1 with 2 magazines, reload 3.66 and refill delay 30 are stored with no dispute. Radius needs an in-game check, since the unit and the field names are inferred. |
| MBT-LAW | Max speed 300, reload 3.4 and capacity 1 with 3 magazines are stored and match EA's upper range. Lock numbers wait on which source the game uses. |
| Javelin | Max speed 60 and capacity 1 with 3 magazines. Lock numbers wait on which source the game uses. Reload cannot be shown. |
| Panzerfaust 3 | Reload 4.96 and fire rate are stored. The damage results should wait for the tank-side hit test. |
| Railgun | Stored damage 150, speed 1029, 11 magazines and reload 4.266 are stored and named. Damage on vehicles needs the tank-rear hit test. |
| Stinger | Capacity 1 with 3 magazines and refill delay 18 are stored. Lock numbers wait on which source the game uses, and missile speed needs a timing test. |
| IGLA | Max speed 480, blast damage 100 with radius 5, lock ranges 840 and 700, lock time 1.0, capacity 1 with 3 magazines. All are stored and named now. Check lock ranges in game, since units are not stated and the range owner is not settled. |
| Drill Launcher / Breaching Dart | Reload 2.53 is stored and unchallenged. Everything else needs an in-game check. |
| Airburst Incendiary Launcher | Capacity 1 with 3 magazines, refill delay 30 and reload 2.53. The burn numbers need the health-lost-per-second test. |
| Frag Grenade | Blast damage 100, blast radius 5 and the 0 against tanks look solid (stored, named, not disputed). The bounce delay (1.1 now) is stored and confirmed by the ledger. Falloff steps and real damage at range need an in-game check first. |
| Mini V40 | Capacity 1 and 2 magazines are stored and named. The 40 damage and 5 radius need re-checking on the current build before showing. |
| Anti-Tank Grenade | Damage 50 and radius 1.5 are stored and named. The per-target numbers (150 on tanks and so on) are calculated from stored numbers and need one in-game check. |
| Incendiary Grenade | Initial blast 0 with radius 4, and the 10 lifetime of the projectile. Burn damage needs an in-game check first (health lost in the first and eighth second). |
| Throwing Knife | Capacity 1, 5 magazines and refill delay 15. Damage 50 needs an in-game check because the sources do not agree on owner and date. |
| Decoy | Capacity and magazine counts only. Radius and timings need an in-game check. |
| C4 | Blast damage 100, radius 3, and EA's 350 against tanks (labelled as an EA statement). Arm delay should wait for a check, since its setting was removed. |
| Claymore | Only the carry numbers and the shape of the formula. Damage numbers need an in-game check. |
| AT Mine | Capacity 1 and 3 magazines. Damage 300 and radius 2 come from an older table and need a recheck before showing. |
| PTKM-1R | Capacity and refill delay. Everything about damage and trigger needs an in-game check. |
| M4 SLAM | Capacity, magazines and refill delay. Damage and trigger range need an in-game check. |
| Field upgrades | Nothing safely. The numbers are stored, but their roles are guessed from names. Each would need an in-game check. |
| Mortar call-in | Nothing yet; the unit and availability questions are open. |
| Call-in strike munitions | Nothing yet. Even the stored figures are not linked to a named call-in. An in-game test (a tank hit by one JAGM) would come first. |
| Sabotage | Nothing yet. Availability is unknown. |

## Settings changes that no card could claim

Named settings that changed, appeared or disappeared, whose owner the name does not give. Each worker's list, unmerged.

- Range [default] 3.0 -> 15.0: bare name; GADGETS.md also notes the row has no owner. Could be any gadget range, including Defibrillator or Repair Tool; not assigned.
- Radius [removed] 6.0: bare name, owner unknown.
- Drag [removed] 0.0: bare name, owner unknown.
- Drone_Destroy Gadget Cooldown [removed] 5.0: a drone setting; any link to the Repair Tool or Defibrillator "destroy gadget" effects is unclear.
- EODBot_Max Detection Distance 40.0, EODBot_Should Detonate Explosives false, EODBot_Time To Full Track 0.5, EODBot_Tracking Max Angle 12.5 (all removed): the EOD Bot shares repair rows with the Repair Tool in the guide, but these rows are about detection and tracking, so I did not attach them to the Repair Tool card.

- PrimaryLockingController and SecondaryLockingController rows (lock time, minimum range, ray length, unlock time, release time, release on new target, with numbers like #2, #3, #4). These are shared lock-on settings. The newer notes say the owning gadget is not known. They could be the Laser Designator or a launcher. Example: PrimaryLockingController lock time 1.0 -> 1.5, minimum range 0.0 -> 39.0, ray length 750 -> 687.5, unlock time -1.0 -> 0.5. The ledger itself warns that duplicate-name pairs may have shuffled order.
- "Range" 3.0 -> 15.0. The newer notes say the owner is not named.
- "Radius" 6.0, removed. The owner is not named.
- AirburstIncendiary_SmokeBlockingRadius 2.5, removed. Named for the Airburst Incendiary, not the Smoke Grenade.
- FragGrenade Detonation Delay After Bounce 1.4 -> 1.1. Named for the frag grenade. The newer notes already list the flashbang bounce delay as 1.4, so this row should not be applied to the flashbang card.
- WB_IGLA "Laser Painted Lock" rows (lock time 1.0, minimum range 50.0, ray length 840.0, release 0.5, unlock 0.5), added. They look related to designation, but the name says IGLA, so they were left off the Laser Designator card.
- EODBot_Max Detection Distance 40.0, EODBot_Time To Full Track 0.5, EODBot_Tracking Max Angle 12.5, EODBot_Should Detonate Explosives false, all removed. Named for the EOD Bot. They look similar to Lancet tracking rows, but the Lancet card does not use them.
- SupplyPouch rows and Thermobaric rows. Named for other gadgets.

- "Drag = 0.0" (removed): the IGLA and Stinger carry a drag value of 0 in the guide, but the row name is bare and the ledger does not name an owner.
- "Radius = 6.0" (removed): a bare name. The older RPG-7 blast radius was 6 and the project notes mention a "radius 6" for the RPG, but nothing ties this row to it.
- "Range" 3.0 to 15.0 (changed): a bare name. The project notes confirm its owner is not given either.
- "PrimaryLockingController", "SecondaryLockingController" and their #2, #3, #4 versions, including lock time, minimum range, ray length, release, unlock time changes and removals: owners not named. Lock-on launchers (Javelin, Stinger, MBT-LAW) are all affected. Interesting only as a hint: project notes say a registry pair with ray lengths 687.5 and 550 has no known owner, and these ledger rows carry the same numbers. I did not assign them.
- "PLD_..." lock rows (PLD_SecondaryLockingController.LockTime 1.5 to 1.2, PLD_PrimaryLockingController #2, PLD_World Lock On Time, PLD_World Locking Cooldown, PLD_World Locking Max Angle Deviance, PLD_Handheld Spotting Max Distance): these belong to the laser designator, not to a launcher in this section. They matter for the lock-on interplay (designated targets) but are not assigned to any card here.
- "PB_M320Smoke" projectile rows (removed: blast damage 0, initial speed 350, time to live 8) and "PB_M320StickyLauncher" rows (removed: initial speed 250, time to live 0): M320 projectiles with no card in this section's headings. They may relate to the M320 family.
- "PB_C4" rows (removed: blast damage 180, initial speed 0, time to live 0): C4, not in this section. The Railgun shares C4's blast curve file, but that is a different file.
- "FragGrenade_Detonation Delay After Bounce" 1.4 to 1.1 and "C4_Arm Delay" (removed): other gadgets.
- "VSC_Total Ammo Supplies" and "VSC_Resupply Neutral Vehicles Max Time" (removed): resupply, not my section.
- Many "WB_UAVJammer" and "VEH_UAVJammer" rows (added): the Signal Jammer, not in my section. Its weapon file reuses the Spawn Beacon's deploy-time table per the project notes, which may matter if a Spawn Beacon page is written.
- "SupplyPouch_..." rows and "GS_M4SLAM" rows (changed, removed): other gadgets.
- "PTKM1R_...", "ATMine_TransportDetectionInterval", and "BR_*_AmmoProvided" rows (added): vehicle, mine and battle-royale ammo rows, not mine.

- AirburstIncendiary_SmokeBlockingRadius = 2.5 (removed): the name points to the Airburst Incendiary, which is not in my section.
- Thermobaric NEW Only Sprint Penalty duration = 1.0, Thermobaric full concussion effect duration = 1.0, Thermobaric full concussion effects = False (all removed): thermobaric belongs to the 40 mm launcher, not my cards. Only "Thermobaric fire damage duration" is mentioned, under Incendiary, because that guide card names it.
- AdrenalineShot_Rank = 5 (removed): might belong to the Field upgrades card (adrenaline shot effects), but the guide gives no rank.
- Drone_Destroy Gadget Cooldown = 5.0 (removed): could relate to drones or call-ins; owner unclear.
- EODBot_Max Detection Distance, EODBot_Should Detonate Explosives, EODBot_Time To Full Track, EODBot_Tracking Max Angle (removed): EOD Bot settings; the EOD Bot mine shares the 30, 50, 15 values with the mines here but is not a card in my section.
- M320_LVG_BlastRadius = 3.5, PB_M320Smoke and PB_M320StickyLauncher rows (removed): 40 mm launcher rows.
- "Range" 3.0 -> 15.0 and "Radius" = 6.0 (removed): bare names with no owner. GADGETS.md also says the owner of "Range" is not given.
- PrimaryLockingController, SecondaryLockingController and PLD_ rows (lock time, minimum range, ray length and so on, changed or removed), plus PB_NS_IGLA and WB_IGLA rows (added): lock-on launcher rows, not my gadgets.
- VEH_UAVJammer and WB_UAVJammer rows (added): jammer gadget; not in my section.
- AssaultLadderConfig.RampAngle 52 -> 45, SupplyPouch_ and VSC_ rows, BR_ ammo-provided rows (added): other gadgets.
