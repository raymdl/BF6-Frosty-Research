# REDSEC armor plates: raw data, theories and tests

Prepared 9 November 2026 for [raymdl/BF6-Weapon-Analyzer#69](https://github.com/raymdl/BF6-Weapon-Analyzer/issues/69). Game build **2.1.1.0** (Season 5, current as of this date).

**Read this first.** Everything here is raw data from the game files, lined up with what EA and creators have said. None of it has been checked in-game by us. The site does not show it because we cannot validate it to the site's standard. Where something is a theory, it says so, and section 6 lists tests anyone can run to confirm or rule it out. Results are welcome on the issue.

Companion file: [redsec-armor-curves-2.1.1.0.csv](redsec-armor-curves-2.1.1.0.csv) (every weapon's plate and health damage curves as point lists, plus damage at 0/25/50/75/100 m).

## 1. Short version

- **Every bullet has two damage curves.** One is used against health (the one the site shows). The other is used against armor plates. They differ in damage and in where drop-off happens. The plate curve is in the same weapon files multiplayer uses; REDSEC does not have its own weapons.
- **Plates are 40 HP each, 2 in Battle Royale (80 total), 1 at the start.** EA states this; the files store matching 0 / 40 / 80 amounts but no field says "per plate". Gauntlet armor is 40.
- **Damage against plates is lower than against health at close range, and drops off later.** Typical pattern: health drops at 21 m and 75 m, plates at 31 m, 46 m and 85 m. This matches EA's "drop-off ranges vs armor extended by 10 m".
- **There is probably also a chest multiplier against armor**: 0.84 for automatic weapons, 0.91 for DMRs, 0.67 for bolt-action snipers, 1.0 for pistols and shotguns (EA, update 1.3.3.0). Whether it reduces the plate damage, the health damage, or both is not settled, and one ceramic-armor file swaps that chest for a material with much higher values (×3 to ×4); see theory T2.
- **Carry-over when a plate breaks is not stored in any file we can read.** EA says extra damage goes to health. Under the most likely model it rarely changes shots to kill (section 5).
- **Unknowns:** headshots and limb shots against plates, the exact carry-over rule, replate time.

## 2. How the files model armor

| Piece | What the files hold | Confidence |
|---|---|---|
| Plate damage per bullet | Each bullet (`PD_*`) has an armor damage curve (`TweakableArmorDamageCurve`) beside its health curve. Same file for multiplayer and REDSEC; no REDSEC override of weapon damage was found in any mode table. | Stored |
| Plate amount | Starting-armor affectors hold ceramic (BR) amounts 0 / 40 / 80 and a Gauntlet soft-armor amount of 40. Vest-tier affector steps 0 / 40 / 80. | Stored; "40 per plate" is EA's wording |
| Gauntlet plates | Mode setting `Gauntlet_StartingArmorPlates` = 3. The Gauntlet starting-armor affector also holds an entry of unknown kind (-1) with amount 242. | Stored; not reconciled with "Gauntlet armor is 40" |
| Vest tiers | `SoldierInitialArmorVestTier` = 1, `SoldierMaxArmorTier` = 1, `SoldierArmorVestTierSize` = 230 (unit unknown). Game text: "This armor upgrade gives you an additional armor plate slot." | Stored; meaning partly unknown |
| Chest against armor | An armored soldier's chest uses a separate hit material (579) whose multipliers are exactly EA's 0.84 / 0.91 / 0.67 (1.0 for pistols and shotguns). These equal the normal limb multipliers for the same bullet classes. One ceramic (BR-type) armor affector swaps this chest material to another (238) reading 3 / 3.8 / 4 / 2.51 / 1.475 (automatic / DMR / bolt-action / pistol / shotgun); another ceramic affector keeps 579. Which one BR applies, and what 238 is for, is not known. | Stored; how either applies to plates is a theory |
| Armored head | A separate head material for armored soldiers. The ceramic affector that keeps chest 579 also swaps the head to a material with the normal headshot multipliers. | Stored; what it does in play is unknown |
| Armor bar | One bar that fills and empties; no per-plate segments in the HUD widget. There is an "armor break" hit indicator option. | Stored |
| Carry-over, curve choice, replate time | Not found in any readable file. Likely engine code or logic graphs we cannot decode. | Not found |

Other REDSEC details found in passing: Battle Royale loot weapons are the multiplayer weapons with preset attachments; a BR modifier raises repair-tool damage ×1.55.

## 3. What EA has said

| Date | Source | Statement |
|---|---|---|
| 4 Dec 2025 | [REDSEC Community Update - Armor](https://www.ea.com/games/battlefield/redsec/news/redsec-community-update-armor) | BR armor is 80 HP (2 plates × 40); Gauntlet 40. Armor is extra health on top of normal health. Once armor is gone, "everything works like you're used to" from other modes. Drop-off vs armor extended 10 m for all guns. Automatic weapons lose their closest max-damage step vs armor (example: 7.62×39 close range 33.4 → 27.3). |
| 16 Feb 2026 | [Armor, Looting and More](https://www.ea.com/games/battlefield/redsec/news/redsec-community-update-armor-looting-and-more) | Players drop at least 2 plates on death. |
| 14 Apr 2026 | [Battle Royale 101](https://www.ea.com/games/battlefield/redsec/news/battlefield-redsec-battle-royale-101) | Start with 1 of 2 plates. Once armor is gone, "any additional damage will impact health". Armor bar turns grey when broken. |
| 26 Jun 2026 | [Update 1.3.3.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-3-0) | Chest multiplier vs armor: automatics 1 → 0.84, DMRs 1 → 0.91, snipers 0.8 → 0.67. |
| 15 Sep 2026 | [Update 1.4.3.0](https://www.ea.com/games/battlefield/redsec/news/battlefield-6-game-update-1-4-3-0) | Interdictor does 100 to armor regardless of hit location or distance. |
| 12 Oct 2026 (live 13 Oct) | [Update 2.1.1.0](https://www.ea.com/en/games/battlefield/redsec/news/battlefield-6-game-update-2-1-1-0) | Plate application 20% faster by default, Quick Plating a further 12%. Engineer Field Training level 2: armor replating 33% faster. Support level 3: reviving a teammate applies a plate; Deployable Cover spawns a lootable plate. A list of weapons and ranges that now "take one more bullet to kill vs armor" (used as a check in section 4). |

EA has not stated: headshot or limb behaviour against plates, the exact carry-over rule, base replate time, or plate damage by caliber beyond the one example.

## 4. Theories

Each theory has a strength rating and the test in section 6 that settles it.

**T1. Plates take damage from the armor curve. Strong.** The armor curves are stored per bullet. EA's 2.1.1.0 list of "one more bullet vs armor" weapons and ranges matches the curve changes in the files to within a metre for 18 of its 23 weapons under every model we tried (for example, 5.56 rifles past 46 m, 9 mm SMGs 9-85 m), and for 21 of 23 once T2 is included. The files also change two weapons EA does not list, the DRS-IAR and M16A4 (one more bullet past 46 m, like the other 5.56 weapons), so 25 site weapons change in all. TheXclusiveAce's damage-log readings match the curve values (KORD 17.76 against the stored 17.74; M433 about 21.4 against 21.56; drop-off at 31 m and 85 m). *Test 1.*

**T2. The chest multiplier (0.84 / 0.91 / 0.67) also reduces plate damage. Medium.** EA announced it as a multiplier "vs armor" and the armored chest stores it. The 2.1.1.0 check supports it: for the SG 553R, SOR-300SC and SCW-10, EA's ranges come out right with the multiplier on plates under any carry-over rule; without it, only a scaled carry-over (leftover share of the bullet at health damage) fits. TheXclusiveAce's videos appear to predate 1.3.3.0, when automatics were at 1.0, so their raw-curve readings do not contradict this. The values equal the normal limb multipliers, so an armored chest hit would be scaled like a limb hit. The rating stays Medium because one ceramic affector replaces this chest material with one reading ×3 to ×4 (section 2), and we cannot tell which affector BR uses. *Test 2 settles it in one shot.*

**T3. When a plate breaks, the leftover damage of that bullet goes to health. Medium.** EA says extra damage impacts health. TheXclusiveAce reports that the breaking bullet splits between plate and health. Without the T2 multiplier, neither "no carry-over" nor 1:1 carry-over reproduces EA's SG 553R / SOR-300SC ranges; with the multiplier, every carry-over rule fits. Section 5 shows both outcomes where they differ. *Test 3.*

**T4. After the plates are gone, hits use the normal health curve. Likely.** EA's December 2025 armor article says that once armor is gone, everything works as in other modes. The one observation against it: TheXclusiveAce logged a KORD hit doing 17.76 to health where he expected about 20 (the health curve's close-range value is 20.67). 17.74 is the KORD's plate value. Possible explanations: the breaking bullet's health share uses the plate curve, or an armored soldier keeps taking plate-curve damage while the vest is worn. *Test 4.*

**T5. Headshots skip the plates. Weak.** TheXclusiveAce saw a headshot kill a player with low health without breaking their plate. The files give armored soldiers a separate head material with normal headshot multipliers, which suggests the head is not plated. *Test 5.*

**T6. Limb hits drain plates like chest hits. Unknown.** The armor bar is a single pool, so any hit that touches armor drains the same bar, but nothing says whether arms and legs are covered. Because the armored chest multipliers equal the limb multipliers, damage numbers alone cannot separate the two; whether the bar moves can. *Test 6.*

**T7. The DMR change in 2.1.1.0 applies at all ranges, not "past 21 m". Medium.** EA says the M39 EMR and SVDM take one more bullet past 21 m. The files show their plate damage going from 41.5 / 37.6 / 34.4 to a flat 27.5, which adds a bullet at every range under every model we tried. Either EA's range is loose or something else limits it. *Test 7.*

**T8. Ammo types have their own plate curves. Likely.** Ammo-variant bullets (for example the `_Match` DMR rounds) carry their own armor curves; this doc covers each weapon's standard ammo only. TheXclusiveAce found no consistent ammo effect against plates. Which ammo BR loot weapons use was not traced.

## 5. Shots to kill against plates

Chest hits only, no headshots, 100 health. Each cell is **unarmored / 1 plate (40) / 2 plates (80)**. This uses theories T1 + T2 + normal health curve after the plates break. Where a cell shows a range such as `5-6`, the lower number is "leftover damage carries into health" and the higher is "leftover is lost" (T3). Shotguns are left out (per-pellet damage; their curves are in section 7).

If T2 turns out to be wrong (no multiplier on plates), most automatic-weapon counts against 2 plates drop by one, a few low-damage weapons by two. If the ×3 to ×4 material (section 2) applies to plates instead, plates break in one or two hits and these counts are far too high; test 2 shows which.

| Weapon | Class | Chest x vs armor | 10 m | 25 m | 40 m | 60 m | 80 m | 100 m |
|---|---|---|---|---|---|---|---|---|
| AK4D | Assault Rifle | 0.84 | 3 / 5 / 7 | 4 / 6 / 8 | 4 / 6 / 8 | 4 / 6 / 8 | 5 / 7 / 9 | 5 / 8 / 10 |
| B36A4 | Assault Rifle | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| EF88 | Assault Rifle | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| KORD 6P67 | Assault Rifle | 0.84 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 9 / 12 | 6 / 10 / 13 | 7 / 11 / 14 | 7 / 11 / 15 |
| L85A3 | Assault Rifle | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| M16A4 | Assault Rifle | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| M433 | Assault Rifle | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| Mk 24 | Assault Rifle | 0.84 | 4 / 6 / 8 | 4 / 6 / 8 | 4 / 6 / 8 | 4 / 6 / 8 | 5 / 7 / 9 | 5 / 8 / 10 |
| NVO-228E | Assault Rifle | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 10 | 6 / 9 / 11 | 6 / 9 / 12 |
| SOR-556 Mk2 | Assault Rifle | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| TR-7 | Assault Rifle | 0.84 | 3 / 5 / 7 | 4 / 6 / 8 | 4 / 6 / 8 | 4 / 6 / 8 | 5 / 7 / 9 | 5 / 8 / 10 |
| VCR-2 | Assault Rifle | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| AK-205 | Carbine | 0.84 | 6 / 9 / 12 | 7 / 10 / 13 | 7 / 11 / 14 | 7 / 11 / 14 | 8 / 12 / 15 | 8 / 12 / 16 |
| BROD 3 | Carbine | 0.84 | 5 / 7-8 / 10 | 6 / 8-9 / 11 | 6 / 9 / 12 | 6 / 9 / 12 | 7 / 10 / 13 | 7 / 11 / 14 |
| GRT-BC | Carbine | 0.84 | 5 / 7-8 / 10 | 6 / 8-9 / 11 | 6 / 9 / 12 | 6 / 9 / 12 | 7 / 10 / 13 | 7 / 11 / 14 |
| M277 | Carbine | 0.84 | 4 / 7 / 9 | 4 / 7 / 9 | 4 / 7 / 9 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 |
| M417 A2 | Carbine | 0.84 | 4 / 6 / 8 | 5 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 6 / 9 / 11 | 6 / 9 / 12 |
| M4A1 | Carbine | 0.84 | 5 / 7-8 / 10 | 6 / 8-9 / 11 | 6 / 9 / 12 | 6 / 9 / 12 | 7 / 10 / 13 | 7 / 11 / 14 |
| QBZ-192 | Carbine | 0.84 | 5 / 7-8 / 10 | 6 / 8-9 / 11 | 6 / 9 / 12 | 6 / 9 / 12 | 7 / 10 / 13 | 7 / 11 / 14 |
| SG 553R | Carbine | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 6 / 9 / 11 | 6 / 9 / 12 | 7 / 10 / 13 | 7 / 11 / 14 |
| SOR-300SC | Carbine | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 6 / 9 / 11 | 6 / 9 / 12 | 7 / 10 / 13 | 7 / 11 / 14 |
| CZ3A1 | SMG | 0.84 | 5 / 8 / 11 | 6 / 10 / 13 | 7 / 11 / 15 | 7 / 11 / 15 | 8 / 12 / 16 | 8 / 12 / 16 |
| KV9 | SMG | 0.84 | 5 / 8 / 11 | 6 / 10 / 13 | 7 / 11 / 15 | 7 / 11 / 15 | 8 / 12 / 16 | 8 / 12 / 16 |
| PP-19 | SMG | 0.84 | 5 / 8 / 11 | 6 / 10 / 13 | 7 / 11 / 15 | 7 / 11 / 15 | 8 / 12 / 16 | 8 / 12 / 16 |
| PW5A3 | SMG | 0.84 | 5 / 8 / 11 | 6 / 10 / 13 | 7 / 11 / 15 | 7 / 11 / 15 | 8 / 12 / 16 | 8 / 12 / 16 |
| PW7A2 | SMG | 0.84 | 6 / 9 / 12 | 7 / 11 / 14 | 7 / 11 / 14 | 7 / 11 / 14 | 8 / 12 / 15 | 8 / 12 / 16 |
| RSPR | SMG | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 6 / 9 / 11 | 6 / 9 / 12 | 7 / 10 / 13 | 7 / 11 / 14 |
| SCW-10 | SMG | 0.84 | 4 / 7 / 9 | 5 / 8 / 11 | 6 / 10 / 13 | 6 / 10 / 13 | 7 / 11 / 14 | 7 / 11 / 14 |
| SGX | SMG | 0.84 | 5 / 8 / 11 | 6 / 10 / 13 | 7 / 11 / 15 | 7 / 11 / 15 | 8 / 12 / 16 | 8 / 12 / 16 |
| SL9 | SMG | 0.84 | 5 / 8 / 11 | 6 / 10 / 13 | 7 / 11 / 15 | 7 / 11 / 15 | 8 / 12 / 16 | 8 / 12 / 16 |
| UMG-40 | SMG | 0.84 | 5 / 7-8 / 10 | 6 / 8-9 / 11 | 6 / 9 / 12 | 6 / 9 / 12 | 7 / 10 / 13 | 7 / 11 / 14 |
| USG-90 | SMG | 0.84 | 6 / 9 / 12 | 7 / 10 / 13 | 7 / 11 / 14 | 7 / 11 / 14 | 8 / 12 / 15 | 8 / 12 / 16 |
| DRS-IAR | LMG | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| KTS100 MK8 | LMG | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| L110 | LMG | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| M/60 | LMG | 0.84 | 3 / 5 / 7 | 4 / 6 / 8 | 4 / 6 / 8 | 4 / 6 / 8 | 5 / 7 / 9 | 5 / 8 / 10 |
| M121 A2 | LMG | 0.84 | 3 / 5 / 7 | 4 / 6 / 8 | 4 / 6 / 8 | 4 / 6 / 8 | 5 / 7 / 9 | 5 / 8 / 10 |
| M123K | LMG | 0.84 | 4 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 10 / 13 |
| M240L | LMG | 0.84 | 3 / 5 / 7 | 4 / 6 / 8 | 4 / 6 / 8 | 4 / 6 / 8 | 5 / 7 / 9 | 5 / 8 / 10 |
| M250 | LMG | 0.84 | 4 / 7 / 9 | 4 / 7 / 9 | 4 / 7 / 9 | 4 / 7 / 9 | 4 / 7 / 9 | 4 / 7 / 9 |
| RPK-74M | LMG | 0.84 | 5 / 8 / 11 | 6 / 9 / 12 | 6 / 9 / 12 | 6 / 10 / 13 | 7 / 11 / 14 | 7 / 11 / 15 |
| RPKM | LMG | 0.84 | 4 / 6 / 8 | 5 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 6 / 9 / 11 | 6 / 9 / 12 |
| Z84M | LMG | 0.84 | 3 / 5 / 7 | 4 / 6 / 8 | 4 / 6 / 8 | 4 / 6 / 8 | 5 / 7 / 9 | 5 / 8 / 10 |
| GRT-CPS | DMR | 0.91 | 4 / 5-6 / 7 | 4 / 6 / 7 | 4 / 6 / 7-8 | 4 / 6 / 7-8 | 4 / 6 / 8 | 4 / 6 / 8 |
| LMR27 | DMR | 0.91 | 4 / 5-6 / 7 | 4 / 6 / 7 | 4 / 6 / 7-8 | 4 / 6 / 7-8 | 4 / 6 / 8 | 4 / 6 / 8 |
| M39 EMR | DMR | 0.91 | 3 / 5 / 6-7 | 3 / 5 / 7 | 3 / 5 / 7 | 3 / 5 / 7 | 3 / 5 / 7 | 3 / 5 / 7 |
| SVDM | DMR | 0.91 | 3 / 5 / 6-7 | 3 / 5 / 7 | 3 / 5 / 7 | 3 / 5 / 7 | 3 / 5 / 7 | 3 / 5 / 7 |
| SVK-8.6 | DMR | 0.91 | 2 / 3 / 4 | 2 / 3 / 4 | 2 / 3 / 4 | 2 / 3 / 4 | 2 / 3 / 4 | 2 / 3 / 4 |
| VSSM | DMR | 0.84 | 4 / 6 / 8 | 5 / 7 / 9 | 5 / 8 / 10 | 5 / 8 / 10 | 6 / 9 / 11 | 6 / 9 / 12 |
| ELR-40 | Sniper Rifle | 0.67 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 3 / 3-4 |
| Interdictor | Sniper Rifle | 1 | 2 / 2-3 / 2-3 | 2 / 2-3 / 2-3 | 2 / 2-3 / 2-3 | 2 / 2-3 / 2-3 | 2 / 2-3 / 2-3 | 2 / 2-3 / 2-3 |
| L115 | Sniper Rifle | 0.67 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 2-3 / 3-4 | 1 / 2 / 3 |
| M2010 ESR | Sniper Rifle | 0.67 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 2-3 / 3-4 | 1 / 2 / 3 | 1 / 2 / 3 |
| Mini Scout | Sniper Rifle | 0.67 | 2 / 3 / 4 | 2 / 3 / 4 | 2 / 3 / 4 | 2 / 4 / 5 | 2 / 4 / 5 | 2 / 4 / 5 |
| PSR | Sniper Rifle | 0.67 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 2-3 / 3-4 | 1 / 2 / 3 |
| SV-98 | Sniper Rifle | 0.67 | 2 / 3 / 3-4 | 2 / 3 / 3-4 | 2 / 2-3 / 3-4 | 1 / 2 / 3 | 2 / 2-3 / 3-4 | 2 / 3 / 4 |
| ES 5.7 | Sidearm | 1 | 6 / 8 / 10 | 7 / 9-10 / 12 | 7 / 10 / 13 | 7 / 10 / 13 | 8 / 11 / 14 | 8 / 12 / 15 |
| GGH-22 | Sidearm | 1 | 5 / 7 / 8-9 | 6 / 8 / 10 | 6 / 9 / 11 | 6 / 9 / 11 | 7 / 10 / 12 | 7 / 10 / 13 |
| M357 Trait | Sidearm | 1 | 3 / 4 / 5 | 4 / 5-6 / 6-7 | 4 / 6 / 7 | 4 / 6 / 8 | 5 / 7 / 8-9 | 5 / 7 / 9 |
| M44 | Sidearm | 1 | 2 / 3 / 3-4 | 3 / 4 / 4-5 | 3 / 5 / 6 | 3 / 5 / 6 | 4 / 5-6 / 7 | 4 / 6 / 8 |
| M45A1 | Sidearm | 1 | 4 / 5-6 / 7 | 5 / 7 / 8-9 | 6 / 8 / 10 | 7 / 10 / 12 | 8 / 12 / 15 | 8 / 12 / 15 |
| P18 | Sidearm | 1 | 5 / 7 / 8-9 | 6 / 8 / 10 | 7 / 10 / 12 | 7 / 10 / 13 | 8 / 11 / 14 | 8 / 12 / 15 |
| vz. 61 | Sidearm | 0.84 | 7 / 10-11 / 14 | 8 / 11-12 / 14-15 | 8 / 12 / 16 | 8 / 12 / 16 | 9 / 13 / 17 | 9 / 14 / 18 |

## 6. Tests anyone can run

**Where to test.** A Battlefield Portal custom experience with spawn armor turned on (the files hold a `SpawnWithArmor` setting: 1 = soft, 2 = ceramic, the BR type), with a friend or bots, gives a controlled target. Set `SpawnWithArmor` to 2 (ceramic) to stand in for Battle Royale; soft armor (1) uses different material swaps and would not settle the BR questions. A friend in a Battle Royale match works too. Record video so hits can be counted frame by frame, and use the death recap / damage log, which shows per-hit numbers. Measure range with the in-game rangefinder or the ping distance. Note the date and game version with every result.

| # | Test | What to record | What it tells us |
|---|---|---|---|
| 1 | Shoot a fully plated target in the chest at a range just inside and just outside a plate drop-off (for a 5.56 rifle: 29 m and 33 m, then 44 m and 48 m). | Per-hit damage from the damage log. | Confirms the armor curves and their drop-off points (T1). |
| 2 | One chest hit on a plated target with a B36A4 / M433 / EF88 at about 10 m. | The damage number for that hit. | Record whatever number appears. **21.56** means no multiplier on plates; **18.11** (21.56 × 0.84) means the 0.84 multiplier applies (T2); about **64.7** (21.56 × 3) means the ceramic ×3 material applies. Any other number is new information. Repeat with a DMR and a bolt-action rifle if possible. |
| 3 | Target with **1 plate** (40). BROD 3 at 10-20 m, or vz. 61 at 25-30 m. | Hits to kill, from video. | BROD 3: 7 = leftover carries over, 8 = it is lost. vz. 61: 11 vs 12 (T3). Also read the damage log for the bullet that breaks the plate: does its listed damage exceed what the plate had left? |
| 4 | Break a target's plates, then keep shooting the chest at 10 m with a 5.56 rifle. | Per-hit damage after the bar turns grey. | 26.05 = normal health curve; 21.56 or 18.11 = plate curve still applies while the vest is worn (T4). |
| 5 | Headshot a fully plated target. | Whether the armor bar moves; damage number. | If the bar is untouched and health drops, heads are not plated (T5). |
| 6 | Shoot a fully plated target only in the legs or arms. | Whether the armor bar moves. | Says whether limbs are covered (T6). |
| 7 | SVDM or M39 EMR chest hits on a fully plated target at 10 m and at 40 m. | Hits to kill. | Expected under T1 + T2: 6-7 at 10 m and 7 at 40 m. If 10 m is clearly lower, EA's "past 21 m" is right and something we have not found limits the change (T7). |
| 8 | Same as test 2 with each ammo type on one weapon. | Damage number per ammo. | Whether ammo changes plate damage (T8). |
| 9 | Time a full replate (default, then with Quick Plating). | Seconds, from video. | Replate time; files hold no readable value. |

## 7. Damage curves for every weapon

Damage per bullet (per pellet for shotguns), standard ammo, by distance. "Ramp" means damage changes smoothly between the two distances.

¹ The site's M45A1 health curve differs from the curve stored on its bullet; the site value is shown.

| Weapon | Class | Bullet | Damage to plates (armor curve) | Damage to health (normal curve) | Plate curve changed in 2.1.1.0 |
|---|---|---|---|---|---|
| AK4D | Assault Rifle | `PD_762x51mmNATO` | 27.48 (0-31 m); 26.05 (31-85 m); 20.67 (85 m+) | 35.22 (0-21 m); 26.05 (21-75 m); 20.67 (75 m+) |  |
| B36A4 | Assault Rifle | `PD_556x45mmNATO` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| EF88 | Assault Rifle | `PD_556x45mmNATO` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| KORD 6P67 | Assault Rifle | `PD_545x39mm` | 17.74 (0-31 m); 17.13 (31-46 m); 14.62 (46-85 m); 12.76 (85 m+) | 20.67 (0-21 m); 17.13 (21-75 m); 14.62 (75 m+) | yes |
| L85A3 | Assault Rifle | `PD_556x45mmNATO` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| M16A4 | Assault Rifle | `PD_556x45mmNATO` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| M433 | Assault Rifle | `PD_556x45mmNATO` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| Mk 24 | Assault Rifle | `PD_65x48mm` | 26.05 (0-100 m); 20.67 (100 m+) | 26.05 (0-75 m); 20.67 (75 m+) | new weapon |
| NVO-228E | Assault Rifle | `PD_762x39mm` | 20.67 (0-85 m); 17.13 (85 m+) | 35.22 (0-9 m); 27.48 (9-21 m); 21.56 (21-36 m); 20.67 (36-75 m); 17.13 (75 m+) | yes |
| SOR-556 Mk2 | Assault Rifle | `PD_556x45mmNATO` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| TR-7 | Assault Rifle | `PD_762x51mmNATO` | 27.48 (0-31 m); 26.05 (31-85 m); 20.67 (85 m+) | 35.22 (0-21 m); 26.05 (21-75 m); 20.67 (75 m+) |  |
| VCR-2 | Assault Rifle | `PD_556x45mmNATO` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| AK-205 | Carbine | `PD_545x39mm_Carbine` | 17.74 (0-31 m); 15.07 (31-46 m); 14.62 (46-85 m); 12.76 (85 m+) | 20.67 (0-9 m); 17.74 (9-21 m); 15.07 (21-36 m); 14.62 (36-75 m); 12.76 (75 m+) |  |
| BROD 3 | Carbine | `PD_556x45mmNATO_Carbine` | 21.56 (0-31 m); 17.74 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-9 m); 21.56 (9-21 m); 17.74 (21-36 m); 17.13 (36-75 m); 14.62 (75 m+) |  |
| GRT-BC | Carbine | `PD_556x45mmNATO_Carbine` | 21.56 (0-31 m); 17.74 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-9 m); 21.56 (9-21 m); 17.74 (21-36 m); 17.13 (36-75 m); 14.62 (75 m+) |  |
| M277 | Carbine | `PD_68x51mm_Carbine` | 20.67 at all ranges | 26.05 (0-75 m); 20.67 (75 m+) |  |
| M417 A2 | Carbine | `PD_762x51mmNATO_Carbine` | 27.48 (0-31 m); 21.56 (31-46 m); 20.67 (46-85 m); 17.13 (85 m+) | 35.22 (0-9 m); 27.48 (9-21 m); 21.56 (21-36 m); 20.67 (36-75 m); 17.13 (75 m+) |  |
| M4A1 | Carbine | `PD_556x45mmNATO_Carbine` | 21.56 (0-31 m); 17.74 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-9 m); 21.56 (9-21 m); 17.74 (21-36 m); 17.13 (36-75 m); 14.62 (75 m+) |  |
| QBZ-192 | Carbine | `PD_58x42mm_Carbine` | 21.56 (0-31 m); 17.74 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-9 m); 21.56 (9-21 m); 17.74 (21-36 m); 17.13 (36-75 m); 14.62 (75 m+) |  |
| SG 553R | Carbine | `PD_762x39mm_Carbine` | 20.67 (0-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 35.22 (0-9 m); 26.05 (9-21 m); 20.67 (21-36 m); 17.13 (36-75 m); 14.62 (75 m+) | yes |
| SOR-300SC | Carbine | `PD_.300BLK_Carbine` | 20.67 (0-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 35.22 (0-9 m); 26.05 (9-21 m); 20.67 (21-36 m); 17.13 (36-75 m); 14.62 (75 m+) | yes |
| CZ3A1 | SMG | `PD_9x19mm_PDW` | 20.67 (0-9 m); 17.13 (9-19 m); 14.62 (19-31 m); 12.76 (31 m+) | 26.05 (0-9 m); 20.67 (9-21 m); 17.13 (21-36 m); 14.62 (36-75 m); 12.76 (75 m+) | yes |
| KV9 | SMG | `PD_9x19mm_PDW` | 20.67 (0-9 m); 17.13 (9-19 m); 14.62 (19-31 m); 12.76 (31 m+) | 26.05 (0-9 m); 20.67 (9-21 m); 17.13 (21-36 m); 14.62 (36-75 m); 12.76 (75 m+) | yes |
| PP-19 | SMG | `PD_9x19mm_PDW` | 20.67 (0-9 m); 17.13 (9-19 m); 14.62 (19-31 m); 12.76 (31 m+) | 26.05 (0-9 m); 20.67 (9-21 m); 17.13 (21-36 m); 14.62 (36-75 m); 12.76 (75 m+) | yes |
| PW5A3 | SMG | `PD_9x19mm_PDW` | 20.67 (0-9 m); 17.13 (9-19 m); 14.62 (19-31 m); 12.76 (31 m+) | 26.05 (0-9 m); 20.67 (9-21 m); 17.13 (21-36 m); 14.62 (36-75 m); 12.76 (75 m+) | yes |
| PW7A2 | SMG | `PD_46x30_PDW` | 17.13->14.62 ramp (0-31 m); 14.62 (31-85 m); 12.76 (85 m+) | 17.13 (0-21 m); 14.62 (21-75 m); 12.76 (75 m+) |  |
| RSPR | SMG | `PD_762x39mm_PDW` | 20.67 (0-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 35.22 (0-9 m); 26.05 (9-21 m); 20.67 (21-36 m); 17.13 (36-75 m); 14.62 (75 m+) | new weapon |
| SCW-10 | SMG | `PD_10x25mm_PDW` | 26.05 (0-9 m); 20.67 (9-19 m); 17.13 (19-31 m); 14.62 (31 m+) | 35.22 (0-9 m); 26.05 (9-21 m); 20.67 (21-36 m); 17.13 (36-75 m); 14.62 (75 m+) | yes |
| SGX | SMG | `PD_9x19mm_PDW` | 20.67 (0-9 m); 17.13 (9-19 m); 14.62 (19-31 m); 12.76 (31 m+) | 26.05 (0-9 m); 20.67 (9-21 m); 17.13 (21-36 m); 14.62 (36-75 m); 12.76 (75 m+) | yes |
| SL9 | SMG | `PD_9x19mm_PDW` | 20.67 (0-9 m); 17.13 (9-19 m); 14.62 (19-31 m); 12.76 (31 m+) | 26.05 (0-9 m); 20.67 (9-21 m); 17.13 (21-36 m); 14.62 (36-75 m); 12.76 (75 m+) | yes |
| UMG-40 | SMG | `PD_.40SW_PDW` | 21.56 (0-31 m); 17.74 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-9 m); 21.56 (9-21 m); 17.74 (21-36 m); 17.13 (36-75 m); 14.62 (75 m+) |  |
| USG-90 | SMG | `PD_57x28mm_PDW` | 17.74 (0-31 m); 15.07 (31-46 m); 14.62 (46-85 m); 12.76 (85 m+) | 20.67 (0-9 m); 17.74 (9-21 m); 15.07 (21-36 m); 14.62 (36-75 m); 12.76 (75 m+) |  |
| DRS-IAR | LMG | `PD_556x45mmNATO_MG` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| KTS100 MK8 | LMG | `PD_556x45mmNATO_MG` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| L110 | LMG | `PD_556x45mmNATO_MG` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| M/60 | LMG | `PD_762x51mmNATO_MG` | 27.48 (0-31 m); 26.05 (31-85 m); 20.67 (85 m+) | 35.22 (0-21 m); 26.05 (21-75 m); 20.67 (75 m+) |  |
| M121 A2 | LMG | `PD_762x51mmNATO_MG` | 27.48 (0-31 m); 26.05 (31-85 m); 20.67 (85 m+) | 35.22 (0-21 m); 26.05 (21-75 m); 20.67 (75 m+) |  |
| M123K | LMG | `PD_556x45mmNATO_MG` | 21.56 (0-31 m); 20.67 (31-46 m); 17.13 (46-85 m); 14.62 (85 m+) | 26.05 (0-21 m); 20.67 (21-75 m); 17.13 (75 m+) | yes |
| M240L | LMG | `PD_762x51mmNATO_MG` | 27.48 (0-31 m); 26.05 (31-85 m); 20.67 (85 m+) | 35.22 (0-21 m); 26.05 (21-75 m); 20.67 (75 m+) |  |
| M250 | LMG | `PD_68x51mm_MG` | 20.67 at all ranges | 26.05 at all ranges |  |
| RPK-74M | LMG | `PD_545x39mm_MG` | 17.74 (0-31 m); 17.13 (31-46 m); 14.62 (46-85 m); 12.76 (85 m+) | 20.67 (0-21 m); 17.13 (21-75 m); 14.62 (75 m+) | yes |
| RPKM | LMG | `PD_762x39mm_MG` | 27.48 (0-31 m); 21.56 (31-46 m); 20.67 (46-85 m); 17.13 (85 m+) | 35.22 (0-9 m); 27.48 (9-21 m); 21.56 (21-36 m); 20.67 (36-75 m); 17.13 (75 m+) |  |
| Z84M | LMG | `PD_762x54mmR_MG` | 27.48 (0-31 m); 26.05 (31-85 m); 20.67 (85 m+) | 35.22 (0-21 m); 26.05 (21-75 m); 20.67 (75 m+) | new weapon |
| GRT-CPS | DMR | `PD_556x45mmNATO_Semi` | 29.4 (0-31 m); 27.5 (31-85 m); 26.2 (85 m+) | 29.4 (0-21 m); 27.5 (21-75 m); 26.2 (75 m+) |  |
| LMR27 | DMR | `PD_556x45mmNATO_Semi` | 29.4 (0-31 m); 27.5 (31-85 m); 26.2 (85 m+) | 29.4 (0-21 m); 27.5 (21-75 m); 26.2 (75 m+) |  |
| M39 EMR | DMR | `PD_762x51mmNATO_Semi` | 27.5 at all ranges | 41.5 (0-21 m); 37.6 (21-75 m); 34.4 (75 m+) | yes |
| SVDM | DMR | `PD_762x54mmR_Semi` | 27.5 at all ranges | 41.5 (0-21 m); 37.6 (21-75 m); 34.4 (75 m+) | yes |
| SVK-8.6 | DMR | `PD_.338LapuaMagnum_Semi` | 66.7 (0-19 m); 57.2 (19-31 m); 52.4 (31 m+) | 66.7 (0-9 m); 57.2 (9-21 m); 52.4 (21 m+) |  |
| VSSM | DMR | `PD_9x39mm_Semi` | 27.48 (0-31 m); 21.56 (31-46 m); 20.67 (46-85 m); 17.13 (85 m+) | 35.22 (0-9 m); 27.48 (9-21 m); 21.56 (21-36 m); 20.67 (36-75 m); 17.13 (75 m+) |  |
| ELR-40 | Sniper Rifle | `PD_.375EnABELR_Match` | 80 (0-120 m); 80->100 ramp (120-150 m); 100 (150-180 m); 100->62 ramp (180-210 m); 62 (210 m+) | 80 (0-120 m); 80->100 ramp (120-150 m); 100 (150-180 m); 100->62 ramp (180-210 m); 62 (210 m+) | new weapon |
| Interdictor | Sniper Rifle | `PD_.416Barrett` | 100 at all ranges | 80 (0-100 m); 80->100 ramp (100-120 m); 100 (120-160 m); 100->80 ramp (160-180 m); 80 (180 m+) |  |
| L115 | Sniper Rifle | `PD_.338LapuaMagnum2` | 80 (0-75 m); 80->100 ramp (75-100 m); 100 (100-133 m); 100->62 ramp (133-175 m); 62 (175 m+) | 80 (0-75 m); 80->100 ramp (75-100 m); 100 (100-133 m); 100->62 ramp (133-175 m); 62 (175 m+) |  |
| M2010 ESR | Sniper Rifle | `PD_.300WinMag` | 80 (0-54 m); 80->100 ramp (54-75 m); 100 (75-100 m); 100->62 ramp (100-133 m); 62 (133 m+) | 80 (0-54 m); 80->100 ramp (54-75 m); 100 (75-100 m); 100->62 ramp (100-133 m); 62 (133 m+) |  |
| Mini Scout | Sniper Rifle | `PD_556x45mmNATO_Bolt` | 62 (0-21 m); 62->58 ramp (21-75 m); 58 (75 m+) | 62 (0-21 m); 62->58 ramp (21-75 m); 58 (75 m+) |  |
| PSR | Sniper Rifle | `PD_.338NormaMagnum` | 80 (0-75 m); 80->100 ramp (75-90 m); 100 (90-120 m); 100->62 ramp (120-160 m); 62 (160 m+) | 80 (0-75 m); 80->100 ramp (75-90 m); 100 (90-120 m); 100->62 ramp (120-160 m); 62 (160 m+) |  |
| SV-98 | Sniper Rifle | `PD_762x54mmR_Bolt` | 80 (0-36 m); 80->100 ramp (36-54 m); 100 (54-75 m); 100->62 ramp (75-100 m); 62 (100 m+) | 80 (0-36 m); 80->100 ramp (36-54 m); 100 (54-75 m); 100->62 ramp (75-100 m); 62 (100 m+) |  |
| 18.5KS-K | Shotgun | `PD_12gaNo01Buck275_Semi` | 5 (0-15 m); 5->2.8 ramp (15-16 m); 2.8 (16-21 m); 2.8->2 ramp (21-22 m); 2 (22 m+) | 5 (0-15 m); 5->2.8 ramp (15-16 m); 2.8 (16-21 m); 2.8->2 ramp (21-22 m); 2 (22 m+) |  |
| DB-12 | Shotgun | `PD_12gaNo01Buck275_Pump` | 5 (0-15 m); 5->3.3 ramp (15-16 m); 3.3 (16-21 m); 3.3->2.5 ramp (21-22 m); 2.5 (22 m+) | 5.6 (0-15 m); 5.6->3.3 ramp (15-16 m); 3.3 (16-21 m); 3.3->2.5 ramp (21-22 m); 2.5 (22 m+) |  |
| M1014 | Shotgun | `PD_12gaNo01Buck300_Semi` | 7.2 (0-8 m); 7.2->5 ramp (8-9 m); 5 (9-15 m); 5->3.1 ramp (15-16 m); 3.1 (16-21 m); 3.1->2.3 ramp (21-22 m); 2.3 (22 m+) | 7.2 (0-8 m); 7.2->5 ramp (8-9 m); 5 (9-15 m); 5->3.1 ramp (15-16 m); 3.1 (16-21 m); 3.1->2.3 ramp (21-22 m); 2.3 (22 m+) |  |
| M87A1 | Shotgun | `PD_12gaNo01Buck300_Pump` | 8.4 (0-8 m); 8.4->7.2 ramp (8-9 m); 7.2 (9-15 m); 7.2->5.6 ramp (15-16 m); 5.6 (16-30 m); 5.6->3.8 ramp (30-31 m); 3.8 (31 m+) | 8.4 (0-8 m); 8.4->7.2 ramp (8-9 m); 7.2 (9-15 m); 7.2->5.6 ramp (15-16 m); 5.6 (16-30 m); 5.6->3.8 ramp (30-31 m); 3.8 (31 m+) |  |
| ES 5.7 | Sidearm | `PD_57x28mm` | 20 (0-19 m); 17.7 (19-31 m); 15 (31-46 m); 14.3 (46-85 m); 12.5 (85 m+) | 20 (0-9 m); 17.7 (9-21 m); 15 (21-36 m); 14.3 (36-75 m); 12.5 (75 m+) |  |
| GGH-22 | Sidearm | `PD_.40SW` | 25 (0-19 m); 21.5 (19-31 m); 17.7 (31-46 m); 16.7 (46-85 m); 14.3 (85 m+) | 25 (0-9 m); 21.5 (9-21 m); 17.7 (21-36 m); 16.7 (36-75 m); 14.3 (75 m+) |  |
| M357 Trait | Sidearm | `PD_.357Magnum` | 50 (0-19 m); 37.5 (19-31 m); 27.3 (31-46 m); 25 (46-85 m); 20 (85 m+) | 50 (0-9 m); 37.5 (9-21 m); 27.3 (21-36 m); 25 (36-75 m); 20 (75 m+) |  |
| M44 | Sidearm | `PD_.44Magnum` | 66.7 (0-19 m); 59.9 (19-31 m); 33.4 (31-85 m); 25 (85 m+) | 66.7 (0-9 m); 59.9 (9-21 m); 33.4 (21-75 m); 25 (75 m+) |  |
| M45A1 ¹ | Sidearm | `PD_.45ACP` | 33.4 (0-19 m); 25 (19-31 m); 20 (31-46 m); 16.7 (46-64 m); 14.3->12.5 ramp (64-85 m); 12.5 (85 m+) | 33.4 (0-9 m); 25 (9-21 m); 20 (21-36 m); 16.7 (36-54 m); 14.3 (54-75 m); 12.5 (75 m+) |  |
| P18 | Sidearm | `PD_9x19mm` | 25 (0-19 m); 20 (19-31 m); 16.7 (31-46 m); 14.3 (46-85 m); 12.5 (85 m+) | 25 (0-9 m); 20 (9-21 m); 16.7 (21-36 m); 14.3 (36-75 m); 12.5 (75 m+) |  |
| vz. 61 | Sidearm | `PD_32ACP_PDW` | 15.07 (0-31 m); 13.09 (31-46 m); 12.76 (46-85 m); 11.32 (85 m+) | 17.13 (0-9 m); 15.07 (9-21 m); 13.09 (21-36 m); 12.76 (36-75 m); 11.32 (75 m+) |  |

## 8. Sources and method

- Game files: build 2.1.1.0, read with the Frosty research tools. Bullet curves come from lead L4076 (67 site weapons, every value checked against raw bytes). REDSEC armor settings were captured and decoded on 9 November 2026 (lead L4085, [receipt](../../reference-data/provenance/frosty-2026-11-09-L4085-redsec-armor-settings.json)). Write-ups: [SOLDIER.md](../frosty/SOLDIER.md) sections L4085, L4076, L3380, L3370.
- EA articles as linked in section 3.
- TheXclusiveAce's videos (older builds, used for mechanics only, not values): [video 1](https://www.youtube.com/watch?v=-320zKNfKys&t=410s), [video 2](https://www.youtube.com/watch?v=xshIzOo3150&t=277s).
- The section 4 check of EA's 2.1.1.0 list compares shots to kill on the old and new plate curves at every metre from 0 to 150 m, against a 100 health + 80 armor target, under six combinations of T2 and T3.
