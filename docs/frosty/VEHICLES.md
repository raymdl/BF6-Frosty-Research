# Vehicle comparison source evidence

Vehicles are research for a possible future Analyzer section. Cosmetics, skins and artwork are excluded. Site implementation is not authorized.

## Saved coverage merge and comparison map (L3018)

[L3018](../../reference-data/provenance/frosty-2026-09-30-L3018-vehicle-stat-map.json) merges the parent-reviewed L3011 coverage proposal into [vehicle-coverage.json](../../reference-data/frosty/vehicle-coverage.json). The original census and capture rows are retained. Each of the 46 exact blueprint roots has its reviewed profile and branch evidence pointers. There are 38 blueprint families, five separate role reviews, a Gepard/Cheetah customization alias and a distinct TRV150 spectator support role.

The 14 pinned coverage artifacts match. All 46 exact root raw hashes match. A parent raw recheck reads CB90 MaxHealth 1000 at offset 440, bytes `00007a44`, SHA-256 `2d8e05398f8f3f2b79159a8db1ec5a87d3033ac7c2469d0cb5f3c6c3f6911ad3`. L3001 supplies the exact actual-owner and wrapper naming proof.

The [working document](../working/VEHICLE_SITE_ADDITIONS.md) contains the stat list, family values and conditional validation proposals. The pinned external stat-map artifact records 684 stat decisions for 38 families and links all 46 exact root profiles. This is a source and validation plan, not 684 established gameplay values.

Configured MaxHealth and RepairRateModifier names are supported for 35 base families. Most names use the exact Class_f2a56983 owner key `e39565c4c24306f97c377628d6d9a47e` and member schema mapped by L3001. This transfer is schema inference, not an own-wrapper join for each root. AAV7A1, TheBeast and JetSki have different actual owner keys and receive no transferred health names. Base values must not be copied onto SP/Cine variants with different owners.

L3010 retains typed firing, ammo and projectile words on exact selected WF routes. Labels such as RateOfFire and MagazineCapacity remain candidate meanings in that context. The stat list identifies ten ground family groups with concrete typed paths, but a same-owner naming control must be named before a targeted lead. Re-reading a value without resolving that control does not produce a named player stat.

Effective health, repair speed, damage, reload, ammunition state, countermeasure timing, usable seats and handling remain unresolved. L3013 curve arrays do not establish units or interpolation. Selected entries and armament owners do not establish usable seats or default loadouts. MD slot/bone associations and MM state/input graphs do not establish physical equations. MH47 polymorphic components do not establish absent armament.

Seven global membership/configuration routes through 32 selected references are explicitly scoped out of the intrinsic comparison list. They remain unread available source, not terminal native/schema evidence. Unlock eligibility, mode admission, defaults and global player/AI policy would require a new approved stat and its exact selected dependency.

L3018 used saved 1.4.3.1 evidence at Head 4892087 and descriptor SHA-256 `99b49cfd8bdb5bb6f0181df8ac0d93a0396c1b7f07a1ba3ce8ca1cea45969640`, without a new capture. The operator approved the stat list and ordered Stage 2 work on 30 September. The 1.4.3.5 update check still decides carry-forward. In-game recordings require separate approval.

## MBT configured firing, ammo and launch vectors (L3019)

[L3019](../../reference-data/provenance/frosty-2026-09-30-L3019-vehicle-configured-stats.json) sources eight configured fields on six firing profiles selected by Abrams and Leopard. Fresh M4A1_WB and GRX_Weapons at Head 4892087 supply the exact own-wrapper name control. The parent build guard and exclusive-process check passed before capture. AH64E's known raw hash matched; the parent independently checked the three raw hashes because the collector's Get-FileHash command was unavailable.

The control's actual Class_35259f6b/key `503dde81ed5cf4d154423f8a5b58e439` exactly matches all six selected firing owners and their nested/member schemas. The raw M4A1 controls reproduce MagazineCapacity 31, RateOfFire 899.9990234375 and Shot.InitialSpeed.z 590. Worker proofs retain the exported wrapper GUIDs and exact raw hash/child/name/value pairs. Name transfer onto the MBT owners remains explicit schema inference, rather than an own-wrapper match on each WF.

| Selected WF profile | RateOfFire | MagazineCapacity | NumberOfMagazines | InitialAmmo | AutoReplenishDelay | Shot.InitialSpeed vector |
|---|---|---|---|---|---|---|
| MBT CoaxLMG, firing object 3 | 700 | 250 | 1 | -1 | 5 | [0, 0, 600] |
| MBT CoaxHMG, firing object 3 | 360 | 250 | 1 | -1 | 5 | [0, 0, 760] |
| RWS AGL, firing object 1 | 325 | 5 | 10 | -1 | 5 | [0, 1.2699999809265137, 100] |
| RWS LMG, firing object 5 | 720 | 250 | 1 | -1 | 5 | [0, 0, 600] |
| RWS HMG, firing object 3 | 400 | 250 | 1 | -1 | 5 | [0, 0, 760] |
| MBT 120mm, firing object 4 | 900 | 1 | 20 | -1 | 14 | [0, 0, 560] |

These are source values without assigned gameplay units. In particular, the 120mm RateOfFire 900 is not measured cannon RPM. NumberOfMagazines does not establish reserve rounds, InitialAmmo -1 does not prove infinite ammunition, and AutoReplenishDelay does not establish a displayed cooldown. Keep the full AGL vector. Effective projectile speed, damage, radius, native cadence and active/default loadout remain unresolved. No exact named same-owner damage/radius control was established inside the bounded assets, and no limit-only follow-up was launched.

The worker retained 114 new raw reads; the parent review found 124 unique retained checks including reused source proof. The two-family scope and all sampled hashes/bytes passed. A separate parent read confirms CoaxLMG RateOfFire 700. The updated external stat map is pinned by the receipt. These are findings; no gameplay test or site proposal was started.

## Configured armament, item 2 (L3020)

[L3020](../../reference-data/provenance/frosty-2026-09-30-L3020-vehicle-configured-stats.json) records 10 exact controlled firing profiles selected by Tank/AAV7A1, Tank/Bradley, Tank/CV90. The same-Head M4A1 own-wrapper control names these fields. Actual owner class/key and each nested/member descriptor match before labels transfer. This is explicit schema inference. The parent independently reread one RateOfFire operand and checked the worker scope, hashes and raw receipts.

| Selected WF | Firing object | RateOfFire | MagazineCapacity | NumberOfMagazines | InitialAmmo | AutoReplenishDelay | Shot.InitialSpeed |
|---|---|---|---|---|---|---|---|
| WF_Vehicles_RWS_AGL | 1 | 325.0 | 5 | 10 | -1 | 5.0 | [0.0, 1.2699999809265137, 100.0] |
| WF_Vehicles_RWS_LMG | 5 | 720.0 | 250 | 1 | -1 | 5.0 | [0.0, 0.0, 600.0] |
| WF_Vehicles_RWS_HMG | 3 | 400.0 | 250 | 1 | -1 | 5.0 | [0.0, 0.0, 760.0] |
| WF_Vehicles_IFV_SecondaryWeapon_HomingATGM | 4 | 150.0 | 1 | 6 | -1 | 20.0 | [0.0, 0.0, 80.0] |
| WF_Vehicles_IFV_PrimaryWeapon_Canister | 9 | 200.0 | 12 | 20 | -1 | 20.0 | [0.0, 0.0, 700.0] |
| WF_Vehicles_IFV_SecondaryWeapon_LightRockets | 6 | 300.0 | 2 | 4 | -1 | 20.0 | [0.0, 0.0, 120.0] |
| WF_Vehicles_IFV_PrimaryWeapon_APFSDST | 6 | 200.0 | 12 | 20 | -1 | 20.0 | [0.0, 0.0, 375.0] |
| WF_Vehicles_RWS_TargetDesignator | 1 | 550.0 | -1 | 1 | -1 | 5.0 | [0.0, 0.0, 350.0] |
| WF_Vehicles_IFV_SecondaryWeapon_TOW | 2 | 150.0 | 1 | 6 | -1 | 20.0 | [0.0, 0.0, 50.0] |
| WF_Vehicles_IFV_PrimaryWeapon_HEAB | 2 | 200.0 | 12 | 20 | -1 | 20.0 | [0.0, 0.0, 250.0] |

Tank/AAV7A1: Common/Hardware/Vehicles/_VehiclesCommon/WeaponData/RWS/WF_Vehicles_RWS_AGL-SP retains an unmatched firing owner 35259f6b/503dde81ed5cf4d154423f8a6d296a95; no name transfer or follow-up.

Tank/AAV7A1: Common/Hardware/Vehicles/_VehiclesCommon/WeaponData/RWS/WF_Vehicles_RWS_HMG-SP retains an unmatched firing owner 35259f6b/503dde81ed5cf4d154423f8a6d296a95; no name transfer or follow-up.

Configured values do not establish units, loaded/reserve rounds, infinite ammunition, effective fire rate, active/default loadouts, projectile damage or radius. No gameplay recording was made. Projectile damage/radius remains unresolved where no exact same-owner name control was available.

## Configured armament, item 3 (L3021)

[L3021](../../reference-data/provenance/frosty-2026-09-30-L3021-vehicle-configured-stats.json) records 6 exact controlled firing profiles selected by Tank/Gepard. The same-Head M4A1 own-wrapper control names these fields. Actual owner class/key and each nested/member descriptor match before labels transfer. This is explicit schema inference. The parent independently reread one RateOfFire operand and checked the worker scope, hashes and raw receipts.

| Selected WF | Firing object | RateOfFire | MagazineCapacity | NumberOfMagazines | InitialAmmo | AutoReplenishDelay | Shot.InitialSpeed |
|---|---|---|---|---|---|---|---|
| WF_Vehicles_AA_PrimaryWeapon_AAGP | 2 | 600.0 | 6 | 28 | -1 | 8.0 | [0.0, 0.0, 850.0] |
| WF_Vehicles_AA_PrimaryWeapon_AAAP | 6 | 240.0 | 8 | 16 | -1 | 8.0 | [0.0, 0.0, 560.0] |
| WF_Vehicles_AA_SecondaryWeapon_AimGuidedMissile | 1 | 120.0 | 2 | 3 | -1 | 16.0 | [0.0, 0.0, 50.0] |
| WF_Vehicles_AA_PrimaryWeapon_AAHV | 4 | 720.0 | 250 | 1 | -1 | 8.0 | [0.0, 0.0, 1175.0] |
| WF_Vehicles_AA_SecondaryWeapon_HighVelocityMissile | 4 | 60.0 | 4 | 2 | -1 | 16.0 | [0.0, 0.0, 117.5] |
| WF_Vehicles_AA_SecondaryWeapon_AntiAirMissile | 5 | 120.0 | 2 | 2 | -1 | 16.0 | [0.0, 0.0, 20.0] |

Configured values do not establish units, loaded/reserve rounds, infinite ammunition, effective fire rate, active/default loadouts, projectile damage or radius. No gameplay recording was made. Projectile damage/radius remains unresolved where no exact same-owner name control was available.

## Configured armament, item 4 (L3022)

[L3022](../../reference-data/provenance/frosty-2026-09-30-L3022-vehicle-configured-stats.json) records 4 exact controlled firing profiles selected by Car/Flyer60, Car/JLTV, Car/Marauder, Car/Vector. The same-Head M4A1 own-wrapper control names these fields. Actual owner class/key and each nested/member descriptor match before labels transfer. This is explicit schema inference. The parent independently reread one RateOfFire operand and checked the worker scope, hashes and raw receipts.

| Selected WF | Firing object | RateOfFire | MagazineCapacity | NumberOfMagazines | InitialAmmo | AutoReplenishDelay | Shot.InitialSpeed |
|---|---|---|---|---|---|---|---|
| WF_Vehicles_OpenGunner_HMG | 10 | 500.0 | 250 | 1 | -1 | 5.0 | [0.0, 0.0, 760.0] |
| WF_Vehicles_RWS_AGL | 1 | 325.0 | 5 | 10 | -1 | 5.0 | [0.0, 1.2699999809265137, 100.0] |
| WF_Vehicles_RWS_LMG | 5 | 720.0 | 250 | 1 | -1 | 5.0 | [0.0, 0.0, 600.0] |
| WF_Vehicles_RWS_HMG | 3 | 400.0 | 250 | 1 | -1 | 5.0 | [0.0, 0.0, 760.0] |

Configured values do not establish units, loaded/reserve rounds, infinite ammunition, effective fire rate, active/default loadouts, projectile damage or radius. No gameplay recording was made. Projectile damage/radius remains unresolved where no exact same-owner name control was available.

## Own-wrapper health names, item 5 (L3024)

[L3024](../../reference-data/provenance/frosty-2026-09-30-L3024-health-own-wrapper-check.json) reproduced the CB90 same-Head own-wrapper name control (MaxHealth 1000, RepairRateModifier 1). Each requested family selects actual Class_f2a56983/key `e39565c4c24306f97c377628132bba60`, which differs from the named CB90 owner.

Tank/AAV7A1: its selected `Field_95253068/Field_6b28f68f` wrapper pointer is raw zero at offset 1032; no health/repair names added, and this family attempt is closed.

Car/TheBeast: its selected `Field_95253068/Field_6b28f68f` wrapper pointer is raw zero at offset 1032; no health/repair names added, and this family attempt is closed.

Boat/JetSki: its selected `Field_95253068/Field_6b28f68f` wrapper pointer is raw zero at offset 1032; no health/repair names added, and this family attempt is closed.

The parent independently reread AAV7A1's null. Worker review passed 31 unique raw checks and the exact three-root scope. A null wrapper does not imply zero health or absent repair. Configured names remain unresolved; no follow-up, health proposal or recording was started.

## Configured armament, item 6 (L3025)

[L3025](../../reference-data/provenance/frosty-2026-09-30-L3025-vehicle-configured-stats.json) records 14 exact controlled firing profiles selected by airplane/f14, airplane/f16, airplane/f22, airplane/fa18f, airplane/jas39, airplane/su57. The same-Head M4A1 own-wrapper control names these fields. Actual owner class/key and each nested/member descriptor match before labels transfer. This is explicit schema inference. The parent independently reread one RateOfFire operand and checked the worker scope, hashes and raw receipts.

| Selected WF | Firing object | RateOfFire | MagazineCapacity | NumberOfMagazines | InitialAmmo | AutoReplenishDelay | Shot.InitialSpeed |
|---|---|---|---|---|---|---|---|
| WF_Vehicles_Airplane_Passenger_PrimaryWeapon_SemiActiveRadarMissile | 4 | 120.0 | 2 | 1 | -1 | 7.5 | [0.0, -10.0, 0.0] |
| WF_Vehicles_Airplane_PrimaryWeapon_Cannon | 1 | 1200.0 | -1 | -1 | -1 | 20.0 | [0.0, 0.0, 1100.0] |
| WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile | 4 | 120.0 | 2 | 1 | -1 | 10.0 | [0.0, 0.0, 20.0] |
| WF_Vehicles_NavalFighter_PrimaryWeapon_AIM54 | 6 | 150.0 | 1 | 4 | -1 | 20.0 | [0.0, -10.0, 0.0] |
| WF_Vehicles_Airplane_Bomb_Mk82AIR | 6 | 300.0 | 1 | 2 | -1 | 30.0 | [0.0, -10.0, 0.0] |
| WF_Vehicles_Airplane_SecondaryWeapon_AirToGroundMissile | 1 | 18.0 | 1 | 2 | -1 | 15.0 | [0.0, 0.0, 40.0] |
| WF_Vehicles_Airplane_SecondaryWeapon_LightRockets | 6 | 300.0 | 7 | 2 | -1 | 14.0 | [0.0, 0.0, 360.0] |
| WF_Vehicles_Airplane_Bomb_GBU39 | 6 | 120.0 | 1 | 4 | -1 | 20.0 | [0.0, -10.0, 0.0] |
| WF_Vehicles_Airplane_Bomb_BunkerBuster | 6 | 1200.0 | 1 | 2 | -1 | 10.0 | [0.0, -10.0, 0.0] |
| WF_Vehicles_Airplane_Bomb_Rockeye | 5 | 1200.0 | 1 | 2 | -1 | 30.0 | [0.0, -10.0, 0.0] |
| WF_Vehicles_Airplane_SecondaryWeapon_AntiRadiationMissile | 6 | 120.0 | 2 | 1 | -1 | 10.0 | [0.0, 0.0, 40.0] |
| WF_Vehicles_Airplane_TVMissile | 5 | 18.0 | 1 | 2 | -1 | 16.0 | [0.0, -10.0, 5.0] |
| WF_Vehicles_MultirolePlane_PrimaryWeapon_ZuniRockets | 4 | 300.0 | 4 | 2 | -1 | 16.0 | [0.0, 0.0, 360.0] |
| WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile_R73 | 1 | 120.0 | 2 | 1 | -1 | 10.0 | [0.0, -10.0, 20.0] |

Configured values do not establish units, loaded/reserve rounds, infinite ammunition, effective fire rate, active/default loadouts, projectile damage or radius. No gameplay recording was made. Projectile damage/radius remains unresolved where no exact same-owner name control was available.

## Configured armament, item 6 (L3026)

[L3026](../../reference-data/provenance/frosty-2026-09-30-L3026-vehicle-configured-stats.json) records 17 exact controlled firing profiles selected by helicopter/ah64e, helicopter/ah6m, helicopter/eurocopter. The same-Head M4A1 own-wrapper control names these fields. Actual owner class/key and each nested/member descriptor match before labels transfer. This is explicit schema inference. The parent independently reread one RateOfFire operand and checked the worker scope, hashes and raw receipts.

| Selected WF | Firing object | RateOfFire | MagazineCapacity | NumberOfMagazines | InitialAmmo | AutoReplenishDelay | Shot.InitialSpeed |
|---|---|---|---|---|---|---|---|
| WF_Vehicles_AttackHeli_Passenger_PrimaryWeapon_Chaingun | 6 | 625.0 | 12 | -1 | -1 | 8.0 | [0.0, 0.0, 805.0] |
| WF_Vehicles_AttackHeli_Passenger_SecondaryWeapon_LockingMissile | 2 | 18.0 | 1 | 4 | -1 | 20.0 | [0.0, 0.0, 20.0] |
| WF_Vehicles_AttackHeli_PrimaryWeapon_HeavyRockets | 1 | 300.0 | 4 | 2 | -1 | 16.0 | [0.0, 0.0, 360.0] |
| WF_Vehicles_AttackHeli_PrimaryWeapon_LightRockets | 1 | 300.0 | 12 | 2 | -1 | 18.0 | [0.0, 0.0, 360.0] |
| WF_Vehicles_AttackHeli_PrimaryWeapon_SmartRockets | 4 | 300.0 | 7 | 2 | -1 | 14.0 | [0.0, 0.0, 180.0] |
| WF_Vehicles_AttackHeli_SecondaryWeapon_AirToAirMissile | 5 | 120.0 | 2 | 1 | -1 | 10.0 | [0.0, 0.0, 20.0] |
| WF_Vehicles_AttackHeli_SecondaryWeapon_TOW | 3 | 18.0 | 1 | 4 | -1 | 20.0 | [0.0, 0.0, 50.0] |
| WF_Vehicles_RWS_TargetDesignator | 1 | 550.0 | -1 | 1 | -1 | 5.0 | [0.0, 0.0, 350.0] |
| WF_Vehicles_ScoutHeli_Passenger_PrimaryWeapon_ThermalScanner | 4 | 3600.0 | -1 | 1 | -1 | 5.0 | [0.0, 0.0, 350.0] |
| WF_Vehicles_ScoutHeli_Passenger_SecondaryWeapon_DirectionalJammer | 3 | 360.0 | -1 | 1 | -1 | 5.0 | [0.0, 0.0, 350.0] |
| WF_Vehicles_ScoutHeli_PrimaryWeapon_GAU19 | 9 | 800.0 | 100 | 4 | 200 | 20.0 | [0.0, 0.0, 860.0] |
| WF_Vehicles_ScoutHeli_PrimaryWeapon_LR30 | 2 | 250.0 | 6 | -1 | -1 | 20.0 | [0.0, 0.0, 265.0] |
| WF_Vehicles_ScoutHeli_PrimaryWeapon_Minigun | 3 | 1800.0 | 100 | 4 | 200 | 20.0 | [0.0, 0.0, 700.0] |
| WF_Vehicles_ScoutHeli_SecondaryWeapon_AirToAirMissile | 1 | 120.0 | 2 | 1 | -1 | 10.0 | [0.0, 0.0, 20.0] |
| WF_Vehicles_ScoutHeli_SecondaryWeapon_Hellfire | 2 | 18.0 | 1 | 4 | -1 | 40.0 | [0.0, 0.0, 20.0] |
| WF_Vehicles_ScoutHeli_SecondaryWeapon_LightRockets | 3 | 300.0 | 7 | 2 | -1 | 21.0 | [0.0, 0.0, 360.0] |
| WF_Vehicles_ScoutHeli_SecondaryWeapon_SmartRockets | 5 | 300.0 | 4 | 2 | -1 | 16.0 | [0.0, 0.0, 360.0] |

Configured values do not establish units, loaded/reserve rounds, infinite ammunition, effective fire rate, active/default loadouts, projectile damage or radius. No gameplay recording was made. Projectile damage/radius remains unresolved where no exact same-owner name control was available.

## Configured armament, item 6 (L3027)

[L3027](../../reference-data/provenance/frosty-2026-09-30-L3027-vehicle-configured-stats.json) records 13 exact controlled firing profiles selected by boat/cb90, boat/jetski, boat/rhib. The same-Head M4A1 own-wrapper control names these fields. Actual owner class/key and each nested/member descriptor match before labels transfer. This is explicit schema inference. The parent independently reread one RateOfFire operand and checked the worker scope, hashes and raw receipts.

| Selected WF | Firing object | RateOfFire | MagazineCapacity | NumberOfMagazines | InitialAmmo | AutoReplenishDelay | Shot.InitialSpeed |
|---|---|---|---|---|---|---|---|
| WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG | 3 | 700.0 | 250 | 1 | -1 | 5.0 | [0.0, 0.0, 600.0] |
| WF_Vehicles_PatrolBoat_Equipment_NavalMines | 1 | 900.0 | 1 | 4 | -1 | 20.0 | [0.0, 0.0, 0.0] |
| WF_Vehicles_PatrolBoat_Equipment_Torped47 | 3 | 900.0 | 1 | 2 | -1 | 20.0 | [0.0, 0.0, 10.0] |
| WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Airburst | 2 | 200.0 | 1 | 2 | -1 | 16.0 | [0.0, 0.0, 80.0] |
| WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Guided | 8 | 200.0 | 1 | 2 | -1 | 16.0 | [0.0, 0.0, 80.0] |
| WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_HE | 9 | 200.0 | 2 | 7 | -1 | 8.0 | [0.0, 0.0, 80.0] |
| WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Illumination | 4 | 200.0 | 1 | 2 | -1 | 16.0 | [0.0, 0.0, 80.0] |
| WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Smoke | 8 | 200.0 | 1 | 2 | -1 | 16.0 | [0.0, 0.0, 80.0] |
| WF_Vehicles_PatrolBoat_PrimaryWeapon_GAU19 | 5 | 1000.0 | 100 | 4 | 200 | 20.0 | [0.0, 0.0, 890.0] |
| WF_Vehicles_PatrolBoat_PrimaryWeapon_M230LF | 3 | 200.0 | 12 | -1 | -1 | 8.0 | [0.0, 0.0, 530.0] |
| WF_Vehicles_PatrolBoat_SecondaryWeapon_MistralMissile | 2 | 120.0 | 2 | 2 | -1 | 16.0 | [0.0, 0.0, 20.0] |
| WF_Vehicles_PatrolBoat_SecondaryWeapon_RBS70 | 2 | 150.0 | 1 | 6 | -1 | 20.0 | [0.0, 0.0, 50.0] |
| WF_Vehicles_OpenGunner_HMG | 10 | 500.0 | 250 | 1 | -1 | 5.0 | [0.0, 0.0, 760.0] |

boat/jetski: Common/Hardware/Vehicles/Boat/JetSki/VB_VEH_Boat_JetSki retains an unmatched firing owner /; no name transfer or follow-up.

Configured values do not establish units, loaded/reserve rounds, infinite ammunition, effective fire rate, active/default loadouts, projectile damage or radius. No gameplay recording was made. Projectile damage/radius remains unresolved where no exact same-owner name control was available.

## Configured armament, item 6 (L3028)

[L3028](../../reference-data/provenance/frosty-2026-09-30-L3028-vehicle-configured-stats.json) records 8 exact controlled firing profiles selected by stationary/bgm71tow, stationary/cws, stationary/gdf009, stationary/m2mg, stationary/phalanx, stationary/ssmbattery. The same-Head M4A1 own-wrapper control names these fields. Actual owner class/key and each nested/member descriptor match before labels transfer. This is explicit schema inference. The parent independently reread one RateOfFire operand and checked the worker scope, hashes and raw receipts.

| Selected WF | Firing object | RateOfFire | MagazineCapacity | NumberOfMagazines | InitialAmmo | AutoReplenishDelay | Shot.InitialSpeed |
|---|---|---|---|---|---|---|---|
| WF_Vehicles_Stationary_TOW | 3 | 150.0 | 1 | -1 | -1 | 5.0 | [0.0, 0.0, 50.0] |
| WF_127_CWSCROWS_HMG | 1 | 500.0 | 150 | 1 | -1 | 5.0 | [0.0, 0.0, 800.0] |
| WF_CWSCROWS_Spike | 4 | 150.0 | 1 | 10 | -1 | 5.0 | [0.0, 0.0, 50.0] |
| WF_CWS_AGL | 3 | 150.0 | 30 | 1 | -1 | 5.0 | [0.0, 1.2699999809265137, 100.0] |
| WF_Vehicles_Stationary_AntiAir | 2 | 720.0 | -1 | -1 | -1 | 8.0 | [0.0, 0.0, 1175.0] |
| WF_Vehicles_OpenGunner_HMG | 10 | 500.0 | 250 | 1 | -1 | 5.0 | [0.0, 0.0, 760.0] |
| WF_Vehicles_SAA_PrimaryWeapon_20mmRotaryCannon | 1 | 1200.0 | -1 | -1 | -1 | 20.0 | [0.0, 0.0, 1100.0] |
| WF_Vehicles_SSMBattery_SecondaryWeapon_AntiAirMissile | 1 | 120.0 | 1 | -1 | -1 | 10.0 | [0.0, 0.0, 20.0] |

Configured values do not establish units, loaded/reserve rounds, infinite ammunition, effective fire rate, active/default loadouts, projectile damage or radius. No gameplay recording was made. Projectile damage/radius remains unresolved where no exact same-owner name control was available.

## Configured armament, item 6 (L3029)

[L3029](../../reference-data/provenance/frosty-2026-09-30-L3029-vehicle-configured-stats.json) records 1 exact controlled firing profiles selected by helicopter/mh47, helicopter/uh60. The same-Head M4A1 own-wrapper control names these fields. Actual owner class/key and each nested/member descriptor match before labels transfer. This is explicit schema inference. The parent independently reread one RateOfFire operand and checked the worker scope, hashes and raw receipts.

| Selected WF | Firing object | RateOfFire | MagazineCapacity | NumberOfMagazines | InitialAmmo | AutoReplenishDelay | Shot.InitialSpeed |
|---|---|---|---|---|---|---|---|
| WF_Vehicles_TransportHeli_Gunner_Minigun | 5 | 1800.0 | 100 | 4 | 200 | 20.0 | [0.0, 0.0, 700.0] |

helicopter/mh47: selected profile retains an unmatched firing owner /; no name transfer or follow-up.

Configured values do not establish units, loaded/reserve rounds, infinite ammunition, effective fire rate, active/default loadouts, projectile damage or radius. No gameplay recording was made. Projectile damage/radius remains unresolved where no exact same-owner name control was available.

## Stage 2 coverage close-out (L3030)

[L3030](../../reference-data/provenance/frosty-2026-09-30-L3030-vehicle-stage2-closeout.json) pins the cumulative 38-family/46-root map. Exact controlled firing fields cover 27 families/34 root profiles with 69 deduplicated profiles and 552 scalar operands. All previous configured health and UI boundaries are retained.

MQ9 selects a deploy-time wrapper (Class_5b9b2235/key8bbd8fbf139b81bc58b352065eda425e); TRV150 selects its blueprint root (Class_b057bb60/key1d85d88a8e017d438f60302e5e3bad4b). Neither selected root matches the controlled ground WF root schema. No selected exact controlled ground weapon-owner join is proved on this route; no fields transferred and no follow-up tonight. This does not establish absent weapons.

The 1.4.3.5 update check decides carry-forward. No live stat, default loadout, availability or effective behavior follows from these configured source facts.

## MBT UI card join control (L3031)

[L3031](../../reference-data/provenance/frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json) tests one MAIN BATTLE TANK card against the selected MBT metadata route. The prior card text/import controls pass. One guarded shared-lock capture adds 28 unique missing target assets at 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. All 42 former external target references match an exact captured file/exported-object GUID pair. This resolves target availability, not family membership.

The card's selected external pointer is the tank icon. The selected Abrams/Leopard metadata image pointer targets the shared Abrams image, rather than either blueprint root. Field_1636b8bd lookup arrays retain their exact ids, but their gameplay consumer/domain is not proved. No end-to-end card-to-root chain passed on this selected route. No family receives seat counts, roles or tags from this result. This bounded finding does not establish that no other exact join exists.

The receipt keeps the original Head 4892087 identities for reused L3023 raw data and current Head 4909002 identities for the new targets. Prior cited bytes carry forward by the saved raw-hash comparison. Twelve unique worker reads and the parent image-import reread pass. Native UI selection and runtime vehicle behavior remain unresolved.

## Customization category join attempt (L3032)

[L3032](../../reference-data/provenance/frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json) checks the second MBT card-to-root route. The customization config pointer/import resolves exactly to DefaultCategorizationTags object 637, RemoteWeaponStation - Primary, with signed Field_c124c7d8 id `-30013352`. Source control and all 127 worker raw reads pass. The parent independently reads that id at offset 33668, bytes `580836fe`.

All fifteen selected imported category owners use the same local-key schema. Their retained fields are name, category id, local parent pointer and ordinal. Every selected parent pointer resolves to this categorization asset's object 0. These selected category targets supply no exact MBT card-to-Abrams/Leopard root edge. This is a bounded route result, not a global absence claim. The receipt records the initial pre-control decoded probe separately; conclusions use the post-control raw checks.

L3031 and L3032 both lack a complete card-to-root chain. UI join work stops at the operator's two-lead limit. All nine cards remain unlinked; no family seat counts, roles or tags are assigned. The capture gap is resolved for the 42 requested external references. The remaining gap is the exact metadata lookup consumer and root identity relation. No working UI-to-asset join method is claimed.

## Current APHEI owner attempt (L3033)

[L3033](../../reference-data/provenance/frosty-2026-09-30-L3033-vehicle-aphei-current-only.json) is current-only 1.4.3.5 evidence at Head 4909002. The known airplane cannon root selects local weapon object 3, then firing object 1, with the exact controlled owner keys. RateOfFire is 1200 at raw offset 784, bytes `00009644`; all three worker reads and the independent parent read pass. This controls the source reader and candidate owner, not the APHEI identity.

The current TSV contains APHEI Cannon ids `29F90E86` and `2A030C88`, plus 20mm APHEI Cannon id `E2912A70`. Four directly selected aircraft/AA vehicle metadata assets and two current cannon candidates did not establish an exact text-to-weapon owner chain. A targeted legacy Field_3d34898a id lookup supplied no additional route. Legacy bodies are used only to find routes. Full candidate decodes retain layout ambiguity; unknown imports retain unknown roles. These are bounded decoder/search observations, not global absence claims.

The [official patch notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-4-3-5) state the APHEI/carrier restriction. Its exact APHEI weapon, projectile and carrier-specific serialized rule remain unresolved. No small exact missing UI target was identified for capture. Work stops at the owner gate after the one permitted lead. No carrier capture, damage/radius naming hunt, old-raw comparison, before/after claim or native runtime test was made.
