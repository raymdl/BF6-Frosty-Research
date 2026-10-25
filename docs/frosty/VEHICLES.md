# Vehicle comparison source evidence

Vehicles are research for a possible future Analyzer section. Cosmetics, skins and artwork are excluded. Site implementation is not authorized. Gadgets are a separate game category with their own page, [Gadgets](GADGETS.md).

Evidence classes stay apart on this page: a stored source value (read by exact owner, member, offset and hash), an inherited declared default, an attributed UI statement, a dated EA statement, a hypothesis, and effective runtime behaviour, which nothing here reaches. **Registry defaults are not selected values**: a selected export's own value is never replaced by, or averaged with, the registry or leaf default. Foundation research for a future vehicles and gadgets version of the site, not tied to current site outputs.

**Season 5 (2.1.1.0).** Most values below were read at 1.4.3.5. Where a stated value changed in 2.1.1.0, the new value follows it as `(2.1.1.0: x)`; `registry` means the registry row changed and the file value did not. Derived columns (products, hit counts, EA comparisons) are not recomputed. Source: `builds\2.1.1.0\reports\registry-diff-2026-10-14\` and the 13 October update trace (`2026-10-13-update-2110-post\STAGE6-8-TRACE-RESULTS.md`).

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
| WF_Vehicles_RWS_HMG | 3 | 400.0 (2.1.1.0 registry: 450) | 250 | 1 | -1 | 5.0 | [0.0, 0.0, 760.0] |
| WF_Vehicles_IFV_SecondaryWeapon_HomingATGM | 4 | 150.0 | 1 | 6 | -1 | 20.0 | [0.0, 0.0, 80.0] |
| WF_Vehicles_IFV_PrimaryWeapon_Canister | 9 | 200.0 | 12 | 20 | -1 | 20.0 | [0.0, 0.0, 700.0] |
| WF_Vehicles_IFV_SecondaryWeapon_LightRockets | 6 | 300.0 | 2 | 4 | -1 | 20.0 | [0.0, 0.0, 120.0] |
| WF_Vehicles_IFV_PrimaryWeapon_APFSDST | 6 | 200.0 | 12 | 20 | -1 | 20.0 | [0.0, 0.0, 375.0] |
| WF_Vehicles_RWS_TargetDesignator | 1 | 550.0 | -1 | 1 | -1 | 5.0 | [0.0, 0.0, 350.0] |
| WF_Vehicles_IFV_SecondaryWeapon_TOW | 2 | 150.0 | 1 | 6 | -1 | 20.0 | [0.0, 0.0, 50.0] (2.1.1.0 registry: z 76) |
| WF_Vehicles_IFV_PrimaryWeapon_HEAB | 2 | 200.0 | 12 | 20 | -1 | 20.0 | [0.0, 0.0, 250.0] |

Tank/AAV7A1: Common/Hardware/Vehicles/_VehiclesCommon/WeaponData/RWS/WF_Vehicles_RWS_AGL-SP retains an unmatched firing owner 35259f6b/503dde81ed5cf4d154423f8a6d296a95; no name transfer or follow-up.

Tank/AAV7A1: Common/Hardware/Vehicles/_VehiclesCommon/WeaponData/RWS/WF_Vehicles_RWS_HMG-SP retains an unmatched firing owner 35259f6b/503dde81ed5cf4d154423f8a6d296a95; no name transfer or follow-up.

Configured values do not establish units, loaded/reserve rounds, infinite ammunition, effective fire rate, active/default loadouts, projectile damage or radius. No gameplay recording was made. Projectile damage/radius remains unresolved where no exact same-owner name control was available.

## Configured armament, item 3 (L3021)

[L3021](../../reference-data/provenance/frosty-2026-09-30-L3021-vehicle-configured-stats.json) records 6 exact controlled firing profiles selected by Tank/Gepard. The same-Head M4A1 own-wrapper control names these fields. Actual owner class/key and each nested/member descriptor match before labels transfer. This is explicit schema inference. The parent independently reread one RateOfFire operand and checked the worker scope, hashes and raw receipts.

| Selected WF | Firing object | RateOfFire | MagazineCapacity | NumberOfMagazines | InitialAmmo | AutoReplenishDelay | Shot.InitialSpeed |
|---|---|---|---|---|---|---|---|
| WF_Vehicles_AA_PrimaryWeapon_AAGP | 2 | 600.0 (2.1.1.0: 550) | 6 | 28 | -1 | 8.0 | [0.0, 0.0, 850.0] (2.1.1.0 registry: z 1,175) |
| WF_Vehicles_AA_PrimaryWeapon_AAAP | 6 | 240.0 (2.1.1.0: 480) | 8 (2.1.1.0 registry: 4) | 16 (2.1.1.0 registry: 32) | -1 | 8.0 | [0.0, 0.0, 560.0] (2.1.1.0 registry: z 900) |
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
| WF_Vehicles_RWS_HMG | 3 | 400.0 (2.1.1.0 registry: 450) | 250 | 1 | -1 | 5.0 | [0.0, 0.0, 760.0] |

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
| WF_Vehicles_Stationary_TOW | 3 | 150.0 | 1 | -1 | -1 | 5.0 | [0.0, 0.0, 50.0] (2.1.1.0 registry: z 76) |
| WF_127_CWSCROWS_HMG | 1 | 500.0 | 150 | 1 | -1 | 5.0 | [0.0, 0.0, 800.0] |
| WF_CWSCROWS_Spike | 4 | 150.0 | 1 | 10 | -1 | 5.0 | [0.0, 0.0, 50.0] |
| WF_CWS_AGL | 3 | 150.0 | 30 | 1 | -1 | 5.0 | [0.0, 1.2699999809265137, 100.0] |
| WF_Vehicles_Stationary_AntiAir | 2 | 720.0 (2.1.1.0 registry: 1,100) | -1 | -1 | -1 | 8.0 | [0.0, 0.0, 1175.0] |
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

The receipt keeps the original Head 4892087 identities for reused L3023 raw data and 1.4.3.5 Head 4909002 identities for the new targets. Prior cited bytes carry forward by the saved raw-hash comparison. Twelve unique worker reads and the parent image-import reread pass. Native UI selection and runtime vehicle behavior remain unresolved.

## Customization category join attempt (L3032)

[L3032](../../reference-data/provenance/frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json) checks the second MBT card-to-root route. The customization config pointer/import resolves exactly to DefaultCategorizationTags object 637, RemoteWeaponStation - Primary, with signed Field_c124c7d8 id `-30013352`. Source control and all 127 worker raw reads pass. The parent independently reads that id at offset 33668, bytes `580836fe`.

All fifteen selected imported category owners use the same local-key schema. Their retained fields are name, category id, local parent pointer and ordinal. Every selected parent pointer resolves to this categorization asset's object 0. These selected category targets supply no exact MBT card-to-Abrams/Leopard root edge. This is a bounded route result, not a global absence claim. The receipt records the initial pre-control decoded probe separately; conclusions use the post-control raw checks.

L3031 and L3032 both lack a complete card-to-root chain. UI join work stops at the operator's two-lead limit. All nine cards remain unlinked; no family seat counts, roles or tags are assigned. The capture gap is resolved for the 42 requested external references. The remaining gap is the exact metadata lookup consumer and root identity relation. No working UI-to-asset join method is claimed.

## Current APHEI owner attempt (L3033)

[L3033](../../reference-data/provenance/frosty-2026-09-30-L3033-vehicle-aphei-current-only.json) is current-only 1.4.3.5 evidence at Head 4909002. The known airplane cannon root selects local weapon object 3, then firing object 1, with the exact controlled owner keys. RateOfFire is 1200 at raw offset 784, bytes `00009644`; all three worker reads and the independent parent read pass. This controls the source reader and candidate owner, not the APHEI identity.

The current TSV contains APHEI Cannon ids `29F90E86` and `2A030C88`, plus 20mm APHEI Cannon id `E2912A70`. Four directly selected aircraft/AA vehicle metadata assets and two current cannon candidates did not establish an exact text-to-weapon owner chain. A targeted legacy Field_3d34898a id lookup supplied no additional route. Legacy bodies are used only to find routes. Full candidate decodes retain layout ambiguity; unknown imports retain unknown roles. These are bounded decoder/search observations, not global absence claims.

The [official patch notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-4-3-5) state the APHEI/carrier restriction. Its exact APHEI weapon, projectile and carrier-specific serialized rule remain unresolved. No small exact missing UI target was identified for capture. Work stops at the owner gate after the one permitted lead. No carrier capture, damage/radius naming hunt, old-raw comparison, before/after claim or native runtime test was made.

## Vehicle semantic transfer census (L640)

[L640](../../reference-data/provenance/frosty-2026-09-30-L640-transfer-census.json) inventories 17 shared vehicle comparison rows and the per-family L3018 stat map. Its 39 gadget comparison rows are on the [gadget page](GADGETS.md#transfer-census-gadget-side-l640-l645-l648). Exact class, descriptor key and field identity permit transfer of configured RateOfFire, MagazineCapacity, reload source fields and Shot.InitialSpeed components. Replenishment and reserve-count semantics remain unconfirmed on infantry and do not transfer. Gravity and drag transfer only for the exact infantry projectile schema consumed by `frosty-ballistics.py`. Other projectile owners retain their own field identities.

M4A1 and L115 extraction controls pass the established IEEE float32 precision contract for rate, capacity, reload, damage, velocity, gravity and drag. Literal float64 differences are listed in the run control file. Field meaning does not establish active/default loadouts, native timing selection, utility effects, target/material damage or guided flight. Season 5 durability and named AA/mine items are excluded. UI identity searches remain parked; unconfirmed; no recording planned.

## Configured weapon-shape profiles (L641-L645)

The 2026-09-30T234837-0400-gadget-vehicle-semantics run extracted 69 vehicle firing owners. M4A1 and L115 controls pass the established IEEE float32 source contract. Literal float64 differences remain explicit in the control result. Each selected firing owner and nested member has the same class key and field identity as its weapon control. The parent worker reviews and independent consequential raw reads pass.

The draft profiles preserve full source precision for configured RateOfFire, MagazineCapacity and the launch vector. Matching infantry projectile owners also retain gravity and drag. Effective reload totals remain null because selector and composition are unconfirmed. Tweakable and primary health curves remain separate; one cannot replace the other. Different projectile classes do not inherit infantry damage or ballistics meaning. Display names and active loadouts remain unset. These results confirm configured field meaning through weapons; they do not establish effective cadence, reserve resources, guided flight or native activation.

[Draft vehicle profiles](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-09-30T234837-0400-gadget-vehicle-semantics/vehicle-weapon-profiles.json) retain partial rows, exact selected joins and raw-check evidence. Vehicle batches are L641-L644 (15/15/15/12); gadget batch L645 has 11 owners. Original Head 4892087 and raw hashes are retained and carry forward to 1.4.3.5. No site data, simulation or UI changed. Unconfirmed fields: unconfirmed; no recording planned.

## EA and UI semantic statements and baseline limits (L646-L651)

All 23 official updates are read: 297 selected gadget/vehicle statements, including 221 numeric statements. The patch inventory retains all 68 `articles` entries. Verified rollout dates are separate from publication dates; two release dates remain unresolved. The 1.4.3.5 sentence has conflicting relative and explicit date wording. The ledger retains exact numeric fragments, quantities, mode, snapshot hash and line numbers.

L649 retains 17 UI mechanic quantities and separates 128 model/caliber/label tokens. The UI-to-gameplay joins remain unlinked. No exact version-matched EA/UI operand comparison is established, so no field meaning is promoted from these statements. The local build labels are 1.4.2.5, 1.4.3.0 and 1.4.3.5; most stated numeric updates predate the captured builds. Supporting later-source comparisons retain explicit version and selection limits. The launch and later ladder baselines differ; the mortar prompt says increased while its endpoints decrease. These are source-text issues, not native runtime findings.

The 73 selected vehicle WF routes include all 69 controlled firing owners and four saved routes without such a profile. All 12 AA/scout owners are retained by L650 as **changes in Season 5**. The gadget and underbarrel owners added by L648 are on the [gadget page](GADGETS.md#transfer-census-gadget-side-l640-l645-l648). Durability and named Season 5 validation exclusions stay separate from extraction.

L649 corrects three L644 array boundaries: `Field_2ad7e688` has three local curve references and three null pointers; the referenced `Field_5279388d` arrays use the valid empty-array sentinel and decode `[]`. `Field_6008eb31` is null on all six owners. An empty curve is not a zero-damage conclusion. L651 adds receipt-local owner identities, reload-phase limits and the selected weapon damage-curve identity to the transfer census.

The second community pass retains 29 mechanic leads. Titles and chapters are candidate topics, with no measured gadget/vehicle test promoted. Later patch changes limit older videos to their own version. [Statement ledger](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-09-30T234837-0400-gadget-vehicle-semantics/ea-stated-numbers.json), [UI statements](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-09-30T234837-0400-gadget-vehicle-semantics/L649/ui-statements-v2.json) and [handoff](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-09-30T234837-0400-gadget-vehicle-semantics/handoff.md) preserve the exact limits. Remaining effects: **unconfirmed; no recording planned**.

## Pre-Season 5 vehicle raw baseline (L3034)

[L3034](../../reference-data/provenance/frosty-2026-10-01-L3034-vehicle-baseline.json) extracts 1.4.3.5 raw (the build then open) for all 46 exact vehicle roots and their selected damage-zone/part chains. All values are **pre-Season 5 baseline; meaning unconfirmed**. The baseline retains 183 local descriptor families, 27,473 raw reads and 85 raw-file identities. Selected zone dependencies are present; no array read is left unsupported in this batch. Original semantic names are restricted to the controlled CB90 owner; other schemas stay hash-only.

The same-owner CB90 control passes: MaxHealth 1000, offset 440, bytes `00007a44`, SHA-256 `2d8e05398f8f3f2b79159a8db1ec5a87d3033ac7c2469d0cb5f3c6c3f6911ad3`. Parent review checks all 46 scoped rows and independently reads the control. Source tuple/array values do not establish regeneration timing, directional damage composition, weak spots, armor, effective health or disable behavior. Durability validation remains excluded. The [baseline](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T011608-0400-vehicles-open-frontier/L3034/baseline.json) preserves exact owners, field identities, offsets and hashes for a later update diff.

## Current vehicle firing and projectile frontier (L3035)

[L3035](../../reference-data/provenance/frosty-2026-10-01-L3035-vehicle-frontier.json) — All 73 selected WF routes have current raw. They contain 72 firing owners: 69 have the exact infantry control key. The three new CRAM/RWS firing owners have a different key; the flare route is an array-only owner. All 83 non-null Shot projectile selections have exact current file/exported-object joins. The 27 selections with the controlled infantry projectile key retain gravity/drag and separate curve channels. Other owners stay hash-only. The 43 tested infantry selections do not supply a matching owner control for those other classes. Empty tweakable arrays remain empty; primary-health curves never substitute for them. Effective damage, reload, guidance and firing behavior remain unconfirmed. All 12 AA/scout selections retain full source replenishment/reload/heat fields as changes in Season 5.

The parent independently reads the alternate CRAM Field_14c4a054 source operand as 1200 at offset 744, bytes `00009644`. This is hash-only source evidence, not an RPM claim for the alternate key. The M4A1 control and worker review pass; 32,293 unique raw reads pass. All source values are **pre-Season 5 baseline; meaning unconfirmed**. [Source atlas](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T011608-0400-vehicles-open-frontier/L3035/vehicle-weapon-profiles-v2.json). No site data, simulation, UI or recording changed.

## Vehicle motion, turret and station source atlas (L3036)

[L3036](../../reference-data/provenance/frosty-2026-10-01-L3036-vehicle-frontier.json) — All 46 roots have exact selected MM/MD coverage across 78 assets. The saved atlas retains 33,364 local owners, 7,195,338 raw operand reads and 64,863 source edges. Large raw payloads are compressed per asset; all payload hashes pass. All 218 selected descriptor schemas retain their exact keys and member types. There are no missing selected routes or traversal errors. 11,346 owners retain layoutAmbiguous markers; field-name transfer and absence claims are excluded for them. Speed units, acceleration/handling equations, turret rates and usable seats remain unconfirmed.

Current same-owner CB90 MM and AAV7A1 MD hash-only pointer controls pass. The parent independently rereads the CB90 MM pointer at offset 66264 as -3536, bytes `30f2ffff`. Pointer/source labels do not establish an operation or physical unit. All source values are **pre-Season 5 baseline; meaning unconfirmed**. [Source atlas](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T011608-0400-vehicles-open-frontier/L3036/field-atlas-motion.json). No site data, simulation, UI or recording changed.

## Vehicle Ability, lock and resupply source frontier (L3037)

[L3037](../../reference-data/provenance/frosty-2026-10-01-L3037-vehicle-frontier.json) — All 46 current roots have selected VB issuing consumers and forward Ability/U/WF/WMD, lock/guidance and repair/resupply source fields retained. The atlas covers 3,271 selected owners, 118,985 raw reads, 6,824 target identity joins and 2,612 array-count reads. The selected pass has zero named raw gaps. Twelve exported-owner identities and two channel imports remain unresolved. The two channel file GUIDs have no match in the current 467,208-asset catalog; this is a source boundary, not an absent mechanic. Loadout artifacts record explicit source selections; default loadouts and availability remain null.

The same-owner current smoke graph control passes. The parent independently reads a selected SP vehicle magazine modifier Float32 as 1 at offset 168, bytes `0000803f`; this does not establish an active modifier. Duration, charge/cooldown units, lock-break effects, repair/resupply composition and native receivers remain unconfirmed. Canonical full-precision numeric values are `rawChecks[].value`; the generic decoder `decodedValue` may be rounded display data. All source values are **pre-Season 5 baseline; meaning unconfirmed**. [Source atlas](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T011608-0400-vehicles-open-frontier/L3037/field-atlas-abilities.json). No site data, simulation, UI or recording changed.

## Ranked vehicle community source traces (L3039)

[L3039](../../reference-data/provenance/frosty-2026-10-01-L3039-vehicle-frontier.json) — All 22 vehicle community items are traced in rank order. Each item names current root candidates, exact issuing owners, reviewed controls and the selected firing/projectile, motion or Ability source proofs. Exact reachable graph owners remain separate from independent candidates. The source ledger does not establish active primary/secondary/gunner slots, equipment upgrades, team entry permission, Thermal Smoke duration/charges/cooldown/lock break, or vehicle supply composition. Dating and title/chapter ambiguity remain visible. No community value or validation claim is imported.

The parent independently rereads the controlled MBT primary firing scalar as 900 at offset 1104, bytes `00006144`. This is a serialized source operand; active cadence and slot identity remain unconfirmed. Twenty-two compact dead-end rows identify the missing field-specific control or native receiver and the evidence that would reopen each item. All source values are **pre-Season 5 baseline; meaning unconfirmed**. [Source atlas](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T011608-0400-vehicles-open-frontier/L3039/community-vehicle-traces.json). No site data, simulation, UI or recording changed.

## Complete vehicle typed field atlas (L3038)

[L3038](../../reference-data/provenance/frosty-2026-10-01-L3038-vehicle-frontier.json) — The frozen forward source frontier covers 1,607 current files, 983 schemas and 5,540 exact declaring-key/member families. Statuses are 9 in the stat map, 5,517 traced but not mapped and 14 known limits. All typed layouts were examined. The traced classification includes 2,915 families with layout inventory only; it does not mean that every family has a controlled value or native operation. Priority handling/boost/curves, countermeasure/lock/repair/resupply and turret/aiming source candidates have supplemental evidence across 171 files, 684 families and 46,399 raw reads. Dense MM/MD and reviewed Ability payloads are reused. No named eligible raw route remains missing.

The parent independently rereads a WingData Float32 operand as 1.2000000476837158 at offset 184, bytes `9a99993f`; the generic display value is 1.2. Canonical numeric values are `rawChecks[].value`. Three unresolved object imports on two Marauder ownership file GUIDs have no match in the current catalog. They remain exact source limits, not absent-mechanic claims. The atlas keeps previous and current examination states, exact evidence pointers, ambiguous layouts and reopen conditions. All source values are **pre-Season 5 baseline; meaning unconfirmed**. [Source atlas](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T011608-0400-vehicles-open-frontier/L3038/vehicle-field-atlas.json). No site data, simulation, UI or recording changed.

<!-- gadget-vehicle-display-2026-10-01-start -->
## Current run: displayable vehicle stats

Run: `2026-10-01T084100-0400-gadget-vehicle-display`. The gadget half of this run (L224-L228) is on the [gadget page](GADGETS.md#displayable-gadget-stats-l224-l228).

### L3041: high-impact vehicle meaning checks

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3041-display-stat-support.json). Ten named questions reuse L3034-L3039; no baseline is re-extracted. Current CB90 MaxHealth and smoke graph controls pass. Parent re-reads CB90 1000 (`00007a44`) and RepairRateModifier 1 (`0000803f`). These are configured values; neither is effective health or HP per second.

| Stat | Saved source and meaning basis | Remaining boundary and exact reopen condition |
|---|---|---|
| Damage from vehicles | L3035 exact selected WF to Shot/projectile and separate curve channels; saved baseline reused. Infantry control can name only Class_23637dce/key 664ff89c671d542411ab855346760f0a and matching selected curve representation. Missile Class_6a25e89d/key 31120380fad6ee70d05903053f9316b6 has no matching infantry control among the 43 saved controls. | No effective outgoing damage equation, material/zone composition or active slot established. Provide an exact same-owner projectile/payload wrapper contract plus selected damage consumer operation and units. |
| Damage to vehicles | L3034 damage-zone/armor owners and L3001 health channels remain separate from outgoing projectile curves. EA 1.3.1.0 distinguishes consistent lock-on damage from manually aimed zone/angle damage. Feedback chapter is only a lead. | No directional multiplier, weak-spot formula, armor-to-health composition or effective durability supported. Provide controlled selected zone/angle/material damage consumer connecting projectile and exact vehicle owner, with units and modifier order. |
| MaxHealth | CB90 own-wrapper receiving member retained and control reread. Exact own-wrapper association names Field_9040392c; same exact key/member schema can support source naming only. Different owner key  e39565c4c24306f97c377628132bba60 stays hash-only. | 1000 is configured MaxHealth; HP units and effective health remain unresolved. Provide selected native/compiled health normalization and modifier consumer; different owner keys require their own wrapper name join. |
| Repair | CB90 RepairRateModifier Field_8fc892f2 configured value 1, reread at 712. Own-wrapper association names modifier; EA repair reduction, regeneration and Emergency Repair describe separate named mechanics. | No repair health-per-second, duration, emergency-heal formula or supply composition derived from modifier 1. Provide matching receiver operation linking RepairRateModifier, repair tool/Emergency Repair inputs and named health channel, including units, pause and modifier order. |
| Countermeasure charges | Selected Ability/U/WF/WMD serialized ammunition/replenishment owners reused. NumberOfMagazines, InitialAmmo and AutoReplenishDelay source naming does not identify usable countermeasure charges. | No effective charges or replenishment count established. Provide exact source-selected countermeasure resource receiver and charge debit/replenishment contract; no numeric/route-name substitution. |
| Countermeasure duration | Smoke graph control pins Class_53d7404d/key 68be6a6ba6ab0bcbd19fd6d9bb5f89fb; u32 Field_42a48f69 is retained without a duration label. EA Thermal Smoke active-duration statement supports mechanic vocabulary at its stated version only. | No source member-to-duration or current effective duration established. Provide exact named timer/receiver contract for selected countermeasure graph with independent operation control and units. |
| Countermeasure cooldown | Source replenishment/delay inputs remain distinct from cooldown. EA names Smoke Screen cooldown in 1.3.1.0; name-matched text can support that historical mechanic, not field identity. | No current source-field cooldown equation or displayed cooldown established. Provide exact active Smoke Screen recharge timer receiver and units, then compare name-matched dated statement without equating numeric values. |
| Countermeasure lock breaks | L3014 direct smoke removal set and L3037 selected locking graphs preserved; SimEx_Smoke_FirePutOut compiled fields remain opaque. EA separately discusses countermeasures, Thermal Smoke mitigation/C-4 removal and later missile reaction. They are not interchangeable lock-break rules. | No active lock cancellation, immunity window, reacquisition or charge composition established. Provide controlled matching SerializedExpressionNodeGraph/native dispatch contract linking exact removal identities and locking state channels. |
| Lock range | L3037 exact lock/guidance selections and declaring schemas reused; no valid vehicle receiver role added. EA explicitly states laser designators affect locking range, including vehicle-mounted designators. Gadget-specific base ranges remain gadget-specific. | No current vehicle lock range or multiplier composition established. Provide same declaring-key/member own-wrapper name and controlled selected acquisition-range receiver, including base/laser/target modifier composition. |
| Lock time | DiceEx_TEMPLEGACYWriteLockingTargetStates selected channel pointer members remain a typed source boundary. EA named weapon/gadget locking time statements do not support a generic vehicle lock time; designator duration is separate. | No current acquisition time, delay units or reacquisition calculation established. Provide matching typed operation contract for exact selected locking-state receiver; resolve selected channel exported owners and distinguish acquisition time from designation duration. |

Dated EA statements are name-matched mechanic support and retain article versions. EclipseFPS Thermal Smoke (14:16), damage feedback (15:22) and Vehicle Ammo Crate (17:15) chapters rank first. Saved title/chapter metadata does not establish a test or a field meaning. No creator number is imported. UI-to-gameplay identity joins remain parked. The eligible saved consumer/member routes close at the listed boundaries. No recording is planned or proposed.

### L3040: complete vehicle candidate support matrix

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3040-display-stat-support.json). All 77 original document rows are mapped: 17 shared rows, ten role rows, three original proposals, 38 family rows and nine UI cards. The role rows expand to 47 named phrases. The final matrix separates configured fields, attributed UI/EA statements and effective mechanics. All 173 effective components remain unresolved and unset. The 124 statement components retain precise evidence, version and units, with no vehicle-family gameplay value.

| Candidate | Configured source components | Attributed statement support and effective boundary |
|---|---|---|
| S01 Configured MaxHealth | Configured MaxHealth: source value only | health (1.3.1.0) Effective mechanics unresolved (1). Exact support: matrix `/rows/0`. |
| S02 Effective health, zone damage and disable thresholds | No named source value; retained inventory is context. | zone_damage (1.3.1.0) Effective mechanics unresolved (3). Exact support: matrix `/rows/1`. |
| S03 Configured repair multiplier | Configured RepairRateModifier: source value only | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/2`. |
| S04 Effective repair rate and delay | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/3`. |
| S05 Armament alternatives | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/4`. |
| S06 Direct damage, blast damage and radius | No named source value; retained inventory is context. | blast radius (1.2.3.0); blast_radii (1.3.3.0); blast_radius (1.3.1.0); damage (1.3.1.0); damage (1.3.3.0); inner blast radius (1.2.3.0); inner_blast_radius (1.3.1.0); lethal blast radius (1.2.3.0); lethal_radius (1.3.1.0) Effective mechanics unresolved (3). Exact support: matrix `/rows/5`. |
| S07 Configured firing operand | Configured RateOfFire: confirmed meaning | fire rate (1.2.3.0); rate_of_fire (1.3.1.0); rate_of_fire (1.3.3.0) Effective mechanics unresolved (2). Exact support: matrix `/rows/6`. |
| S08 Observed fire rate and sustained fire | No named source value; retained inventory is context. | heat_per_bullet (1.3.3.0) Effective mechanics unresolved (2). Exact support: matrix `/rows/7`. |
| S09 Reload, cooldown, heat recovery and resupply | ReloadTime: confirmed meaning; ReloadTimeBulletsLeft: confirmed meaning; ReloadSpeed: confirmed meaning; ReloadDelay: source value only; PostReloadDelay: source value only | ammo regeneration (1.2.3.0); heat_per_bullet (1.3.3.0); reload (1.3.1.0) Effective mechanics unresolved (6). Exact support: matrix `/rows/8`. |
| S10 Configured ammo words | Configured MagazineCapacity: confirmed meaning; Configured NumberOfMagazines: source value only; Configured InitialAmmo: source value only; Configured AutoReplenishDelay: source value only | magazine_capacity (1.3.1.0) Effective mechanics unresolved (4). Exact support: matrix `/rows/9`. |
| S11 Loaded rounds, reserve rounds and ammo recovery | No named source value; retained inventory is context. | ammo regeneration (1.2.3.0); ammunition (1.2.3.0); mobile_AA_missile_supply (1.3.2.0); reserve ammunition (1.2.3.0) Effective mechanics unresolved (3). Exact support: matrix `/rows/10`. |
| S12 Countermeasure/passive alternatives | No named source value; retained inventory is context. | cooldown_acceleration (1.3.3.0); lock_resistance (1.3.1.0); received_damage_cap (1.3.3.0) Effective mechanics unresolved (2). Exact support: matrix `/rows/11`. |
| S13 Countermeasure charges, duration, cooldown and lock break | No named source value; retained inventory is context. | activation (1.3.1.0); activation (1.3.3.0); active_duration (1.3.1.0); cooldown_acceleration (1.3.3.0); deactivation (1.3.1.0); lock_resistance (1.3.1.0) Effective mechanics unresolved (4). Exact support: matrix `/rows/12`. |
| S14 Entry and station definitions | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/13`. |
| S15 Usable seats, switching and weapon access | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (3). Exact support: matrix `/rows/14`. |
| S16 Projectile speed, drop, lock range and guidance | initialSpeed.x: confirmed meaning; initialSpeed.y: confirmed meaning; bulletVel: confirmed meaning; Configured Gravity: confirmed meaning; Configured Drag: confirmed meaning | beam_offset (1.3.1.0); engine_lifetime (1.3.1.0); initial_speed (1.3.3.0); lifetime (1.3.1.0); post_engine_drag (1.3.1.0); turn_rate (1.3.1.0) Effective mechanics unresolved (7). Exact support: matrix `/rows/15`. |
| S17 Speed, acceleration, braking, turning and stability | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (6). Exact support: matrix `/rows/16`. |
| R01 Front/side/rear damage | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (3). Exact support: matrix `/rows/17`. |
| R02 turret traverse/elevation | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/18`. |
| R03 main/coax weapon access | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/19`. |
| R04 disable recovery | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/20`. |
| R05 Passenger access | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/21`. |
| R06 turret traverse/elevation | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/22`. |
| R07 autocannon/missile access | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/23`. |
| R08 amphibious behavior where supported | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/24`. |
| R09 Air-target damage | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/25`. |
| R10 lock range/acquisition time | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/26`. |
| R11 gun overheat | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/27`. |
| R12 anti-spotting and smoke effects | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/28`. |
| R13 Hill acceleration | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/29`. |
| R14 turn/brake response | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/30`. |
| R15 rollover | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/31`. |
| R16 passenger exposure | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/32`. |
| R17 station weapon access | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/33`. |
| R18 Climb rate | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/34`. |
| R19 yaw/pitch/roll response | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (3). Exact support: matrix `/rows/35`. |
| R20 pilot/gunner access | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/36`. |
| R21 missile lock time | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/37`. |
| R22 flare/other selected countermeasure timing | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/38`. |
| R23 Usable passenger/gunner stations | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/39`. |
| R24 climb rate | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/40`. |
| R25 flight response | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/41`. |
| R26 spawn behavior | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/42`. |
| R27 countermeasure timing | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/43`. |
| R28 Top/boost speed | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/44`. |
| R29 boost duration/recovery | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/45`. |
| R30 turn/climb response | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/46`. |
| R31 stall behavior | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/47`. |
| R32 lock and countermeasure timing | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/48`. |
| R33 Forward/reverse speed | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/49`. |
| R34 water turning | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/50`. |
| R35 shore transition | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/51`. |
| R36 passenger exposure | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/52`. |
| R37 station access | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/53`. |
| R38 Traverse/elevation limits | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/54`. |
| R39 firing/cooldown | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/55`. |
| R40 guidance/lock | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/56`. |
| R41 operator exposure | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/57`. |
| R42 Control range | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/58`. |
| R43 view/targeting | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/59`. |
| R44 deployment/recovery | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (2). Exact support: matrix `/rows/60`. |
| R45 flight response | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/61`. |
| R46 loss-of-link behavior | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/62`. |
| R47 selected payload access | No named source value; retained inventory is context. | No precise bounded statement support. Effective mechanics unresolved (1). Exact support: matrix `/rows/63`. |

The nine exact archetype cards provide stated seats: MBT 2, IFV 6, light transport 5, armored transport 4, AA 1, attack helicopter 2, transport helicopter 5, attack jet 1 and fighter jet 1. AA also states dual autocannons; transport helicopter states two side-mounted miniguns. These are attributed card statements. Family usable-seat/active-armament values remain unset. Name-matched associations do not prove gameplay identity.

The current M4A1/CB90/MBT source controls and selected operand re-reads pass. Values reuse L3034-L3039 with the pre-Season 5 label. Older sources retain their original Head and carry-forward evidence. Broad patch mechanic groups remain context. No effective timing, heat, damage, health, dynamics or default loadout is inferred.

### L3042: configured OverHeat field meanings

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3042-vehicle-heat-meaning.json). The M27IAR own-wrapper control joins GRX_Weapons anchor 5155 and class GUID `ba9d132f-45a0-4fe4-a266-d47c14ec5bfe`. Its actual nested declaring key is `837134b69fa37406929eea7d9dc25891` (Class_92d07f08). Exact member/type identity transfers five configured field names to 72 saved selected vehicle firing owners and 360 unchanged Float32 operands. Three firing root keys differ; the exact nested declaring-key/member contract still matches. Forward-import atlas owners without selected profiles are excluded. No vehicle value is re-extracted.

| Member | Confirmed configured meaning | AAHV stored value | Confidence and units |
|---|---|---|---|
| 72a2b562 | HeatPerBullet | 0.041999999433755875 | confirmed meaning for configured field name; source units unresolved |
| e6120d22 | HeatDropPerSecond | 0.5 | confirmed meaning for configured field name; source units unresolved |
| 3b078489 | OverHeatDropDelay | 0.0 | confirmed meaning for configured field name; source units unresolved |
| 3ad34fcc | OverHeatPenaltyTime | 0.5 | confirmed meaning for configured field name; source units unresolved |
| 37a30bd2 | OverHeatThreshold | 0.0 | confirmed meaning for configured field name; source units unresolved |

The parent re-reads all five AAHV operands. HeatPerBullet is `0.041999999433755875` at offset 1328, bytes `31082c3d`; HeatDropPerSecond is `0.5` at 1332, bytes `0000003f`. Zero fields do not prove no active heat gate. No percent scaling, effective cooldown, shots to overheat or sustained fire equation is established.

The historical 1.3.3.0 EA statement changes Mobile AA High Velocity heat from 4.2% to 3.6%. This is a name-matched dated statement. The current source scalar is not converted to a percentage or treated as a contradiction. The selected Gepard EnhancedLoading modifier reaches Class_df8f40db/key `c28d6f25ab0d14d4c460ada3bc29d585`; the same member hash occurs on a different declaring key and four own-wrapper links are null. It lacks a same-owner receiving/operation control. U_VEH_AA_AAHV's selected CT_GLA channel is compiled-resource membership, not an execution contract. Reopen with that exact contract or authoritative item/unit identity. The bounded heat modifier frontier is closed; no active number is derived from the apparent difference.
<!-- gadget-vehicle-display-2026-10-01-end -->

<!-- native-semantics:L1001:start -->
### Exact descriptor enum reader (L1001)

Exact descriptor enum membership is available through the L1001 reader. Current atlas application adds no zeroing, stance/state, spotting or vehicle enum names. Hash members stay unnamed. See the [receipt](../../reference-data/provenance/frosty-2026-10-01-L1001-descriptor-enum-reader.json) for identity counts, controls and limits.
<!-- native-semantics:L1001:end -->

<!-- native-semantics:L1002:start -->
### Curve and table reader boundary (L1002)

The L1002 reader identifies exact controlled curve/table schemas in the current atlas. Site-model interpolation controls do not name physical axes or native interpolation in other owners. No atlas semantic meaning or site number changes. See the [receipt](../../reference-data/provenance/frosty-2026-10-01-L1002-curve-table-reader.json) for identity counts, controls and limits.
<!-- native-semantics:L1002:end -->

## Vehicle station controls (L3100)

[L3100](../../reference-data/provenance/frosty-2026-10-01-L3100-vehicle-station-controls.json) reproduces exact station component controls on 1.4.3.5, Head 4909002. UH60 has five entry definitions with indices 0-4. The two gunner component subtrees select the same exported transport minigun WF owner. CB90 has two entry definitions; the index 1 subtree selects five mortar WF owners. The join uses local component pointers and external file/object GUIDs. Weapon-name words do not assign the station. All 249 worker raw checks pass; independent parent pointer reads pass.

The route is VB root -> vehicle entity -> station component container -> entry and weapon component -> exact WF owner. The entry index remains a serialized index; role, canFire, exposure, default selection and native activation remain unresolved. Distinct passenger entry classes must be retained. The UH60 five-entry count agrees with the transport-helicopter card. Card checks on other families must include every selected entry class.

## Vehicle seat mapping (L3101)

[L3101](../../reference-data/provenance/frosty-2026-10-01-L3101-vehicle-seat-map.json) maps 20 serialized entries on 4 exact roots at 1.4.3.5, Head 4909002. Positive station controls pass. The map retains 32 WF selections and 114 U/WMD or other capability selections. Exact component containment and exported owner identities supply the joins. These selections are alternatives; default and active selection remain unset. The parent re-read a consequential operand on each root.

| Vehicle root | Serialized entries | Card count check | Seat equipment evidence |
|---|---|---|---|
| tank/abrams / VB_VEH_Tank_Abrams | 4 | 2; differs from source total | index 0: 3 WF, 19 capability identities, index 1: 3 WF, 11 capability identities, index 2: 0 WF, 0 capability identities, index 3: 0 WF, 0 capability identities |
| tank/bradley / VB_VEH_Tank_Bradley | 6 | 6; agrees | index 0: 6 WF, 15 capability identities, index 1: 4 WF, 12 capability identities, index 2: 0 WF, 0 capability identities, index 3: 0 WF, 0 capability identities, index 4: 0 WF, 0 capability identities, index 5: 0 WF, 0 capability identities |
| tank/cv90 / VB_VEH_Tank_CV90 | 6 | 6; agrees | index 0: 6 WF, 15 capability identities, index 1: 4 WF, 12 capability identities, index 2: 0 WF, 0 capability identities, index 3: 0 WF, 0 capability identities, index 4: 0 WF, 0 capability identities, index 5: 0 WF, 0 capability identities |
| tank/leopard / VB_VEH_Tank_Leopard | 4 | 2; differs from source total | index 0: 3 WF, 19 capability identities, index 1: 3 WF, 11 capability identities, index 2: 0 WF, 0 capability identities, index 3: 0 WF, 0 capability identities |

Role, canFire and exposure remain null where no exact semantic control applies. Ability, upgrade and countermeasure classification remains unresolved where the saved pointer selects only an unclassified U/WMD or a shared vehicle owner. An empty station weapon component list does not prove that its occupant cannot fire a personal weapon. The map keeps exact entry classes, local keys, source indices, pointer chains and raw checks. Card checks do not supply a missing card-to-root identity join.

[Seat map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/L3101/seat-map.json).

## Station graph control boundary (L3110)

[L3110](../../reference-data/provenance/frosty-2026-10-01-L3110-station-graph-control.json) tests a one-edge graph endpoint route against the known UH60 minigun and CB90 mortar station controls. That graph route fails its controls and stops. It supplies no MBT ability, upgrade or countermeasure absence result. The component containment controls in L3100 still pass. An available selected ModBuilder owner outside the saved atlas remains an untraced route; it is not a native limit. Reopen the graph route only with a passing exact station-to-equipment graph chain and controlled dispatch meaning.

## Vehicle seat mapping (L3102)

[L3102](../../reference-data/provenance/frosty-2026-10-01-L3102-vehicle-seat-map.json) maps 3 serialized entries on 2 exact roots at 1.4.3.5, Head 4909002. Positive station controls pass. The map retains 8 WF selections and 28 U/WMD or other capability selections. Exact component containment and exported owner identities supply the joins. These selections are alternatives; default and active selection remain unset. The parent re-read a consequential operand on each root.

| Vehicle root | Serialized entries | Card count check | Seat equipment evidence |
|---|---|---|---|
| tank/aav7a1 / VB_VEH_Tank_AAV7A1 | 2 | Unassigned | index 0: 0 WF, 0 capability identities, index 0: 2 WF, 4 capability identities |
| tank/gepard / VB_VEH_Tank_Gepard | 1 | 1; agrees | index 0: 6 WF, 24 capability identities |

Role, canFire and exposure remain null where no exact semantic control applies. Ability, upgrade and countermeasure classification remains unresolved where the saved pointer selects only an unclassified U/WMD or a shared vehicle owner. An empty station weapon component list does not prove that its occupant cannot fire a personal weapon. The map keeps exact entry classes, local keys, source indices, pointer chains and raw checks. Card checks do not supply a missing card-to-root identity join.

[Seat map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/L3102/seat-map.json).

## Vehicle seat mapping (L3103)

[L3103](../../reference-data/provenance/frosty-2026-10-01-L3103-vehicle-seat-map.json) maps 20 serialized entries on 6 exact roots at 1.4.3.5, Head 4909002. Positive station controls pass. The map retains 35 WF selections and 84 U/WMD or other capability selections. Exact component containment and exported owner identities supply the joins. These selections are alternatives; default and active selection remain unset. The parent re-read a consequential operand on each root.

| Vehicle root | Serialized entries | Card count check | Seat equipment evidence |
|---|---|---|---|
| helicopter/ah64e / VB_VEH_Helicopter_AH64E | 2 | Unassigned | index 0: 5 WF, 13 capability identities, index 1: 2 WF, 4 capability identities |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M | 4 | Unassigned | index 0: 7 WF, 18 capability identities, index 1: 3 WF, 6 capability identities, index 2: 0 WF, 0 capability identities, index 3: 0 WF, 0 capability identities |
| helicopter/ah6m / VB_VEH_Helicopter_AH6M_M05_SP_Cine | 4 | Unassigned | index 0: 2 WF, 5 capability identities, index 1: 0 WF, 0 capability identities, index 2: 0 WF, 0 capability identities, index 3: 0 WF, 0 capability identities |
| helicopter/ah6m / VB_VEH_Helicopter_SP_MH6M | 6 | Unassigned | index 0: 2 WF, 5 capability identities, index 1: 0 WF, 0 capability identities, index 2: 0 WF, 0 capability identities, index 3: 0 WF, 0 capability identities, index 4: 0 WF, 0 capability identities, index 5: 0 WF, 0 capability identities |
| helicopter/eurocopter / VB_VEH_Helicopter_Eurocopter | 2 | Unassigned | index 0: 5 WF, 12 capability identities, index 1: 2 WF, 4 capability identities |
| helicopter/eurocopter / VB_VEH_Helicopter_Eurocopter_SP | 2 | Unassigned | index 0: 5 WF, 13 capability identities, index 1: 2 WF, 4 capability identities |

Role, canFire and exposure remain null where no exact semantic control applies. Ability, upgrade and countermeasure classification remains unresolved where the saved pointer selects only an unclassified U/WMD or a shared vehicle owner. An empty station weapon component list does not prove that its occupant cannot fire a personal weapon. The map keeps exact entry classes, local keys, source indices, pointer chains and raw checks. Card checks do not supply a missing card-to-root identity join.

[Seat map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/L3103/seat-map.json).

## Vehicle seat mapping (L3104)

[L3104](../../reference-data/provenance/frosty-2026-10-01-L3104-vehicle-seat-map.json) maps 22 serialized entries on 3 exact roots at 1.4.3.5, Head 4909002. Positive station controls pass. The map retains 2 WF selections and 8 U/WMD or other capability selections. Exact component containment and exported owner identities supply the joins. These selections are alternatives; default and active selection remain unset. The parent re-read a consequential operand on each root.

| Vehicle root | Serialized entries | Card count check | Seat equipment evidence |
|---|---|---|---|
| helicopter/mh47 / VB_VEH_Helicopter_MH47_Insertion | 16 | Unassigned | index 1: 0 WF, 0 configuration identities, index 2: 0 WF, 0 configuration identities, index 3: 0 WF, 0 configuration identities, index 4: 0 WF, 0 configuration identities, index 5: 0 WF, 0 configuration identities, index 6: 0 WF, 0 configuration identities, index 7: 0 WF, 0 configuration identities, index 8: 0 WF, 0 configuration identities, index 9: 0 WF, 0 configuration identities, index 10: 0 WF, 0 configuration identities, index 11: 0 WF, 0 configuration identities, index 12: 0 WF, 0 configuration identities, index 13: 0 WF, 0 configuration identities, index 14: 0 WF, 0 configuration identities, index 15: 0 WF, 0 configuration identities, index 16: 0 WF, 0 configuration identities |
| helicopter/mh47 / VB_VEH_Helicopter_MH47_SP | 1 | Unassigned | index 0: 0 WF, 0 configuration identities |
| helicopter/uh60 / VB_VEH_Helicopter_UH60 | 5 | 5; agrees | index 0: 0 WF, 0 configuration identities, index 1: 1 WF, 4 configuration identities, index 2: 1 WF, 4 configuration identities, index 3: 0 WF, 0 configuration identities, index 4: 0 WF, 0 configuration identities |

Role, canFire and exposure remain null where no exact semantic control applies. Ability, upgrade and countermeasure classification remains unresolved where the saved pointer selects only an unclassified U/WMD or a shared vehicle owner. An empty station weapon component list does not prove that its occupant cannot fire a personal weapon. The map keeps exact entry classes, local keys, source indices, pointer chains and raw checks. Card checks do not supply a missing card-to-root identity join.

[Seat map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/L3104/seat-map.json).

## Vehicle seat mapping (L3105)

[L3105](../../reference-data/provenance/frosty-2026-10-01-L3105-vehicle-seat-map.json) maps 8 serialized entries on 3 exact roots at 1.4.3.5, Head 4909002. Positive station controls pass. The map retains 13 WF selections and 34 U/WMD or other capability selections. Exact component containment and exported owner identities supply the joins. These selections are alternatives; default and active selection remain unset. The parent re-read a consequential operand on each root.

| Vehicle root | Serialized entries | Card count check | Seat equipment evidence |
|---|---|---|---|
| boat/cb90 / VB_VEH_Boat_CB90 | 2 | Unassigned | index 0: 7 WF, 19 configuration identities, index 1: 5 WF, 10 configuration identities |
| boat/jetski / VB_VEH_Boat_JetSki | 2 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 0 WF, 0 configuration identities |
| boat/rhib / VB_VEH_Boat_RHIB | 4 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 1 WF, 5 configuration identities, index 2: 0 WF, 0 configuration identities, index 3: 0 WF, 0 configuration identities |

Role, canFire and exposure remain null where no exact semantic control applies. Ability, upgrade and countermeasure classification remains unresolved where the saved pointer selects only an unclassified U/WMD or a shared vehicle owner. An empty station weapon component list does not prove that its occupant cannot fire a personal weapon. The map keeps exact entry classes, local keys, source indices, pointer chains and raw checks. Card checks do not supply a missing card-to-root identity join.

[Seat map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/L3105/seat-map.json).

## Vehicle seat mapping (L3106)

[L3106](../../reference-data/provenance/frosty-2026-10-01-L3106-vehicle-seat-map.json) maps 26 serialized entries on 6 exact roots at 1.4.3.5, Head 4909002. Positive station controls pass. The map retains 12 WF selections and 62 U/WMD or other capability selections. Exact component containment and exported owner identities supply the joins. These selections are alternatives; default and active selection remain unset. The parent re-read a consequential operand on each root.

| Vehicle root | Serialized entries | Card count check | Seat equipment evidence |
|---|---|---|---|
| car/couch / VB_VEH_Car_Couch | 4 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 0 WF, 0 configuration identities, index 1: 0 WF, 0 configuration identities, index 1: 0 WF, 0 configuration identities |
| car/flyer60 / VB_VEH_Car_Flyer60 | 5 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 1 WF, 7 configuration identities, index 2: 0 WF, 0 configuration identities, index 3: 0 WF, 0 configuration identities, index 4: 0 WF, 0 configuration identities |
| car/flyer60 / VB_VEH_Car_Flyer60_SP | 5 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 1 WF, 6 configuration identities, index 2: 0 WF, 0 configuration identities, index 3: 0 WF, 0 configuration identities, index 4: 0 WF, 0 configuration identities |
| car/jltv / VB_VEH_Car_JLTV | 4 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 3 WF, 14 configuration identities, index 2: 1 WF, 5 configuration identities, index 3: 1 WF, 5 configuration identities |
| car/marauder / VB_VEH_Car_Marauder | 4 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 3 WF, 15 configuration identities, index 2: 1 WF, 5 configuration identities, index 3: 1 WF, 5 configuration identities |
| car/ptv / VB_VEH_Car_PTV | 4 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 0 WF, 0 configuration identities, index 2: 0 WF, 0 configuration identities, index 3: 0 WF, 0 configuration identities |

Role, canFire and exposure remain null where no exact semantic control applies. Ability, upgrade and countermeasure classification remains unresolved where the saved pointer selects only an unclassified U/WMD or a shared vehicle owner. An empty station weapon component list does not prove that its occupant cannot fire a personal weapon. The map keeps exact entry classes, local keys, source indices, pointer chains and raw checks. Card checks do not supply a missing card-to-root identity join.

[Seat map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/L3106/seat-map.json).

## Vehicle seat mapping (L3107)

[L3107](../../reference-data/provenance/frosty-2026-10-01-L3107-vehicle-seat-map.json) maps 20 serialized entries on 6 exact roots at 1.4.3.5, Head 4909002. Positive station controls pass. The map retains 2 WF selections and 10 U/WMD or other capability selections. Exact component containment and exported owner identities supply the joins. These selections are alternatives; default and active selection remain unset. The parent re-read a consequential operand on each root.

| Vehicle root | Serialized entries | Card count check | Seat equipment evidence |
|---|---|---|---|
| car/quadbike / VB_VEH_Car_QuadBike | 2 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 0 WF, 0 configuration identities |
| car/thebeast / VB_VEH_Car_TheBeast | 4 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 0 WF, 0 configuration identities, index 2: 0 WF, 0 configuration identities, index 3: 0 WF, 0 configuration identities |
| car/vector / VB_VEH_Car_Vector | 5 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 1 WF, 5 configuration identities, index 2: 0 WF, 0 configuration identities, index 3: 0 WF, 0 configuration identities, index 4: 0 WF, 0 configuration identities |
| car/vector / VB_VEH_Car_Vector_M05_CarChase | 5 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 1 WF, 5 configuration identities, index 2: 0 WF, 0 configuration identities, index 3: 0 WF, 0 configuration identities, index 4: 0 WF, 0 configuration identities |
| motorcycle/dirtbike01 / VB_VEH_Motorcycle_DirtBike01 | 2 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 0 WF, 0 configuration identities |
| motorcycle/dirtbike02 / VB_VEH_Motorcycle_DirtBike02 | 2 | Unassigned | index 0: 0 WF, 0 configuration identities, index 1: 0 WF, 0 configuration identities |

Role, canFire and exposure remain null where no exact semantic control applies. Ability, upgrade and countermeasure classification remains unresolved where the saved pointer selects only an unclassified U/WMD or a shared vehicle owner. An empty station weapon component list does not prove that its occupant cannot fire a personal weapon. The map keeps exact entry classes, local keys, source indices, pointer chains and raw checks. Card checks do not supply a missing card-to-root identity join.

[Seat map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/L3107/seat-map.json).

## Vehicle seat mapping (L3108)

[L3108](../../reference-data/provenance/frosty-2026-10-01-L3108-vehicle-seat-map.json) maps 9 serialized entries on 7 exact roots at 1.4.3.5, Head 4909002. Positive station controls pass. The map retains 30 WF selections and 64 U/WMD or other capability selections. Exact component containment and exported owner identities supply the joins. These selections are alternatives; default and active selection remain unset. The parent re-read a consequential operand on each root.

| Vehicle root | Serialized entries | Card count check | Seat equipment evidence |
|---|---|---|---|
| airplane/f14 / VB_VEH_Airplane_F14 | 2 | Unassigned | index 0: 2 WF, 4 configuration identities, index 1: 2 WF, 5 configuration identities |
| airplane/f16 / VB_VEH_Airplane_F16 | 1 | Unassigned | index 0: 4 WF, 9 configuration identities |
| airplane/f22 / VB_VEH_Airplane_F22 | 1 | Unassigned | index 0: 3 WF, 6 configuration identities |
| airplane/fa18f / VB_VEH_Airplane_FA18F | 2 | Unassigned | index 0: 6 WF, 12 configuration identities, index 1: 3 WF, 7 configuration identities |
| airplane/jas39 / VB_VEH_Airplane_JAS39 | 1 | Unassigned | index 0: 4 WF, 8 configuration identities |
| airplane/jas39 / VB_VEH_SP_Assault_Airplane_JAS39 | 1 | Unassigned | index 0: 3 WF, 7 configuration identities |
| airplane/su57 / VB_VEH_Airplane_SU57 | 1 | Unassigned | index 0: 3 WF, 6 configuration identities |

Role, canFire and exposure remain null where no exact semantic control applies. Ability, upgrade and countermeasure classification remains unresolved where the saved pointer selects only an unclassified U/WMD or a shared vehicle owner. An empty station weapon component list does not prove that its occupant cannot fire a personal weapon. The map keeps exact entry classes, local keys, source indices, pointer chains and raw checks. Card checks do not supply a missing card-to-root identity join.

[Seat map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/L3108/seat-map.json).

## Vehicle seat mapping (L3109)

[L3109](../../reference-data/provenance/frosty-2026-10-01-L3109-vehicle-seat-map.json) maps 7 serialized entries on 7 exact roots at 1.4.3.5, Head 4909002. Positive station controls pass. The map retains 9 WF selections and 20 U/WMD or other capability selections. Exact component containment and exported owner identities supply the joins. These selections are alternatives; default and active selection remain unset. The parent re-read a consequential operand on each root.

| Vehicle root | Serialized entries | Card count check | Seat equipment evidence |
|---|---|---|---|
| stationary/bgm71tow / VB_VEH_Stationary_BGM71TOW | 1 | Unassigned | index 0: 1 WF, 2 configuration identities |
| stationary/cws / VB_VEH_Stationary_Turret_CROWS | 1 | Unassigned | index 0: 3 WF, 6 configuration identities |
| stationary/gdf009 / VB_VEH_Stationary_GDF009 | 1 | Unassigned | index 0: 1 WF, 3 configuration identities |
| stationary/m2mg / VB_VEH_Stationary_M2MG | 1 | Unassigned | index 0: 1 WF, 4 configuration identities |
| stationary/phalanx / VB_VEH_Stationary_Phalanx | 1 | Unassigned | index 0: 1 WF, 2 configuration identities |
| stationary/phalanx / VB_VEH_Stationary_Phalanx_SP | 1 | Unassigned | index 0: 1 WF, 2 configuration identities |
| stationary/ssmbattery / VB_VEH_Stationary_SSMBattery | 1 | Unassigned | index 0: 1 WF, 1 configuration identities |

Role, canFire and exposure remain null where no exact semantic control applies. Ability, upgrade and countermeasure classification remains unresolved where the saved pointer selects only an unclassified U/WMD or a shared vehicle owner. An empty station weapon component list does not prove that its occupant cannot fire a personal weapon. The map keeps exact entry classes, local keys, source indices, pointer chains and raw checks. Card checks do not supply a missing card-to-root identity join.

[Seat map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/L3109/seat-map.json).

## Vehicle seat mapping (L3111)

[L3111](../../reference-data/provenance/frosty-2026-10-01-L3111-vehicle-seat-map.json) maps 2 serialized entries on 2 exact roots at 1.4.3.5, Head 4909002. Positive station controls pass. The map retains 0 WF selections and 2 U/WMD or other capability selections. Exact component containment and exported owner identities supply the joins. These selections are alternatives; default and active selection remain unset. The parent re-read a consequential operand on each root.

| Vehicle root | Serialized entries | Card count check | Seat equipment evidence |
|---|---|---|---|
| airplane/mq9 / VB_VEH_Airplane_MQ9 | 1 | Unassigned | index 0: 0 WF, 1 configuration identities |
| drone/trv150 / VB_VEH_Drone_TRV150 | 1 | Unassigned | index 0: 0 WF, 1 configuration identities |

Role, canFire and exposure remain null where no exact semantic control applies. Ability, upgrade and countermeasure classification remains unresolved where the saved pointer selects only an unclassified U/WMD or a shared vehicle owner. An empty station weapon component list does not prove that its occupant cannot fire a personal weapon. The map keeps exact entry classes, local keys, source indices, pointer chains and raw checks. Card checks do not supply a missing card-to-root identity join.

[Seat map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/L3111/seat-map.json).

## Complete source entry map (L3112)

[L3112](../../reference-data/provenance/frosty-2026-10-01-L3112-vehicle-seat-map-closeout.json) closes source coverage of all 46 exact roots and 38 families in the reused 1 Oct census. The map contains 137 serialized entry definitions, 143 station WF selections and 426 station equipment configuration references. Complete active player loadouts remain unresolved. No new extraction was made.

The positive UH60 minigun and CB90 mortar controls pass before each batch. The exact route is VB root `Field_9e113e77` to the vehicle entity, recursive `Field_5e00055a` component pointers to entry and equipment owners, then the raw import file/object GUIDs to exported WF, U, Ability or WMD identities. The source index is retained with the entry object, class and local key. A name containing Primary, Coax, Passenger or Gunner does not assign a role.

### Count consistency

The table compares all requested groups with the operator counts. Comparisons without a joined card identity remain provisional. MBT source total 4 differs from card 2; selecting only one entry class would hide two retained entries. IFV source total 6 agrees. Source counts for variants and shared containers do not prove usable seats.

| Exact root | Source entries | Operator card comparison | Identity limit |
|---|---|---|---|
| VB_VEH_Tank_Abrams | 4 | MBT 2: differs | operator group comparison |
| VB_VEH_Tank_Bradley | 6 | IFV 6: agrees numerically | operator group comparison |
| VB_VEH_Tank_CV90 | 6 | IFV 6: agrees numerically | operator group comparison |
| VB_VEH_Tank_Leopard | 4 | MBT 2: differs | operator group comparison |
| VB_VEH_Tank_AAV7A1 | 2 | armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Tank_Gepard | 1 | AA 1: agrees numerically | operator group comparison |
| VB_VEH_Helicopter_AH64E | 2 | attack helicopter 2: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_AH6M | 4 | attack helicopter 2: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_AH6M_M05_SP_Cine | 4 | attack helicopter 2: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_SP_MH6M | 6 | attack helicopter 2: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_Eurocopter | 2 | attack helicopter 2: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_Eurocopter_SP | 2 | attack helicopter 2: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 16 | transport helicopter 5: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_MH47_SP | 1 | transport helicopter 5: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Helicopter_UH60 | 5 | transport helicopter 5: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Boat_CB90 | 2 | No stated count | no stated card count |
| VB_VEH_Boat_JetSki | 2 | No stated count | no stated card count |
| VB_VEH_Boat_RHIB | 4 | No stated count | no stated card count |
| VB_VEH_Car_Couch | 4 | light transport 5: differs; armored transport 4: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Car_Flyer60 | 5 | light transport 5: agrees numerically; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Car_Flyer60_SP | 5 | light transport 5: agrees numerically; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Car_JLTV | 4 | light transport 5: differs; armored transport 4: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Car_Marauder | 4 | light transport 5: differs; armored transport 4: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Car_PTV | 4 | light transport 5: differs; armored transport 4: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Car_QuadBike | 2 | light transport 5: differs; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Car_TheBeast | 4 | light transport 5: differs; armored transport 4: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Car_Vector | 5 | light transport 5: agrees numerically; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Car_Vector_M05_CarChase | 5 | light transport 5: agrees numerically; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Motorcycle_DirtBike01 | 2 | light transport 5: differs; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Motorcycle_DirtBike02 | 2 | light transport 5: differs; armored transport 4: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_F14 | 2 | attack jet 1: differs; fighter jet 1: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_F16 | 1 | attack jet 1: agrees numerically; fighter jet 1: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_F22 | 1 | attack jet 1: agrees numerically; fighter jet 1: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_FA18F | 2 | attack jet 1: differs; fighter jet 1: differs | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_JAS39 | 1 | attack jet 1: agrees numerically; fighter jet 1: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_SP_Assault_Airplane_JAS39 | 1 | attack jet 1: agrees numerically; fighter jet 1: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Airplane_SU57 | 1 | attack jet 1: agrees numerically; fighter jet 1: agrees numerically | comparison only; exact archetype association unresolved |
| VB_VEH_Stationary_BGM71TOW | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_Turret_CROWS | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_GDF009 | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_M2MG | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_Phalanx | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_Phalanx_SP | 1 | No stated count | no stated card count |
| VB_VEH_Stationary_SSMBattery | 1 | No stated count | no stated card count |
| VB_VEH_Airplane_MQ9 | 1 | No stated count | no stated card count |
| VB_VEH_Drone_TRV150 | 1 | No stated count | no stated card count |

### Selected weapon owners by source entry

The labels below are exact WF route tails with only the common `WF_Vehicles_` prefix removed. They are configuration selections. Duplicated selections are retained when separate source components select the same WF. Defaults are null. Every row has the full VB, entry, component and import identity chains and raw checks in the [aggregate map](../../../BF6%20Datamining/reports/weapon-analyzer-research/2026-10-01T-vehicle-seats-L3100/seat-map.json).

| Exact root | Stored index / entry object | Selected WF route tails | Equipment references |
|---|---|---|---|
| VB_VEH_Tank_Abrams | 0 / 26 | MBT_PrimaryWeapon_120mm, MBT_SecondaryWeapon_CoaxLMG, MBT_SecondaryWeapon_CoaxHMG | 19 |
| VB_VEH_Tank_Abrams | 1 / 25 | RWS_HMG, RWS_AGL, RWS_LMG | 11 |
| VB_VEH_Tank_Abrams | 2 / 42 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_Abrams | 3 / 43 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_Bradley | 0 / 28 | IFV_PrimaryWeapon_APFSDST, IFV_PrimaryWeapon_HEAB, IFV_PrimaryWeapon_Canister, IFV_SecondaryWeapon_LightRockets, IFV_SecondaryWeapon_TOW, IFV_SecondaryWeapon_HomingATGM | 15 |
| VB_VEH_Tank_Bradley | 1 / 31 | RWS_HMG, RWS_AGL, RWS_LMG, RWS_TargetDesignator | 12 |
| VB_VEH_Tank_Bradley | 2 / 26 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_Bradley | 3 / 29 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_Bradley | 4 / 27 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_Bradley | 5 / 30 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_CV90 | 0 / 32 | IFV_PrimaryWeapon_APFSDST, IFV_PrimaryWeapon_HEAB, IFV_PrimaryWeapon_Canister, IFV_SecondaryWeapon_LightRockets, IFV_SecondaryWeapon_TOW, IFV_SecondaryWeapon_HomingATGM | 15 |
| VB_VEH_Tank_CV90 | 1 / 31 | RWS_HMG, RWS_AGL, RWS_LMG, RWS_TargetDesignator | 12 |
| VB_VEH_Tank_CV90 | 2 / 29 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_CV90 | 3 / 27 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_CV90 | 4 / 30 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_CV90 | 5 / 28 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_Leopard | 0 / 25 | MBT_PrimaryWeapon_120mm, MBT_SecondaryWeapon_CoaxLMG, MBT_SecondaryWeapon_CoaxHMG | 19 |
| VB_VEH_Tank_Leopard | 1 / 26 | RWS_HMG, RWS_AGL, RWS_LMG | 11 |
| VB_VEH_Tank_Leopard | 2 / 42 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_Leopard | 3 / 43 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_AAV7A1 | 0 / 15 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Tank_AAV7A1 | 0 / 14 | RWS_AGL-SP, RWS_HMG-SP | 4 |
| VB_VEH_Tank_Gepard | 0 / 19 | AA_PrimaryWeapon_AAGP, AA_PrimaryWeapon_AAAP, AA_PrimaryWeapon_AAHV, AA_SecondaryWeapon_AntiAirMissile, AA_SecondaryWeapon_HighVelocityMissile, AA_SecondaryWeapon_AimGuidedMissile | 24 |
| VB_VEH_Helicopter_AH64E | 0 / 21 | AttackHeli_PrimaryWeapon_LightRockets, AttackHeli_PrimaryWeapon_HeavyRockets, AttackHeli_PrimaryWeapon_SmartRockets, AttackHeli_SecondaryWeapon_AirToAirMissile, AttackHeli_SecondaryWeapon_TOW | 13 |
| VB_VEH_Helicopter_AH64E | 1 / 20 | AttackHeli_Passenger_PrimaryWeapon_Chaingun, AttackHeli_Passenger_SecondaryWeapon_LockingMissile | 4 |
| VB_VEH_Helicopter_AH6M | 0 / 23 | ScoutHeli_PrimaryWeapon_Minigun, ScoutHeli_PrimaryWeapon_GAU19, ScoutHeli_PrimaryWeapon_LR30, ScoutHeli_SecondaryWeapon_Hellfire, ScoutHeli_SecondaryWeapon_LightRockets, ScoutHeli_SecondaryWeapon_SmartRockets, ScoutHeli_SecondaryWeapon_AirToAirMissile | 18 |
| VB_VEH_Helicopter_AH6M | 1 / 24 | ScoutHeli_Passenger_PrimaryWeapon_ThermalScanner, ScoutHeli_Passenger_SecondaryWeapon_DirectionalJammer, RWS_TargetDesignator | 6 |
| VB_VEH_Helicopter_AH6M | 2 / 35 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_AH6M | 3 / 36 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_AH6M_M05_SP_Cine | 0 / 18 | TransportHeli_Gunner_Minigun, Airplane_SecondaryWeapon_LightRockets | 5 |
| VB_VEH_Helicopter_AH6M_M05_SP_Cine | 1 / 19 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_AH6M_M05_SP_Cine | 2 / 31 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_AH6M_M05_SP_Cine | 3 / 30 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_SP_MH6M | 0 / 21 | TransportHeli_Gunner_Minigun, Airplane_SecondaryWeapon_LightRockets | 5 |
| VB_VEH_Helicopter_SP_MH6M | 1 / 20 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_SP_MH6M | 2 / 29 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_SP_MH6M | 3 / 28 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_SP_MH6M | 4 / 30 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_SP_MH6M | 5 / 27 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_Eurocopter | 0 / 20 | AttackHeli_PrimaryWeapon_LightRockets, AttackHeli_PrimaryWeapon_HeavyRockets, AttackHeli_PrimaryWeapon_SmartRockets, AttackHeli_SecondaryWeapon_TOW, AttackHeli_SecondaryWeapon_AirToAirMissile | 12 |
| VB_VEH_Helicopter_Eurocopter | 1 / 21 | AttackHeli_Passenger_PrimaryWeapon_Chaingun, AttackHeli_Passenger_SecondaryWeapon_LockingMissile | 4 |
| VB_VEH_Helicopter_Eurocopter_SP | 0 / 21 | AttackHeli_PrimaryWeapon_LightRockets, AttackHeli_PrimaryWeapon_HeavyRockets, AttackHeli_PrimaryWeapon_SmartRockets, AttackHeli_SecondaryWeapon_TOW, AttackHeli_SecondaryWeapon_AirToAirMissile | 13 |
| VB_VEH_Helicopter_Eurocopter_SP | 1 / 22 | AttackHeli_Passenger_PrimaryWeapon_Chaingun, AttackHeli_Passenger_SecondaryWeapon_LockingMissile | 4 |
| VB_VEH_Helicopter_MH47_Insertion | 1 / 35 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 2 / 38 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 3 / 36 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 4 / 33 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 5 / 29 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 6 / 42 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 7 / 31 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 8 / 27 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 9 / 41 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 10 / 40 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 11 / 37 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 12 / 34 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 13 / 30 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 14 / 32 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 15 / 39 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_Insertion | 16 / 28 | Shared context; assignment unresolved | Shared context; assignment unresolved |
| VB_VEH_Helicopter_MH47_SP | 0 / 12 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_UH60 | 0 / 17 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_UH60 | 1 / 19 | TransportHeli_Gunner_Minigun | 4 |
| VB_VEH_Helicopter_UH60 | 2 / 18 | TransportHeli_Gunner_Minigun | 4 |
| VB_VEH_Helicopter_UH60 | 3 / 33 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Helicopter_UH60 | 4 / 32 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Boat_CB90 | 0 / 26 | PatrolBoat_PrimaryWeapon_M230LF, PatrolBoat_PrimaryWeapon_GAU19, PatrolBoat_SecondaryWeapon_RBS70, PatrolBoat_SecondaryWeapon_MistralMissile, MBT_SecondaryWeapon_CoaxLMG, PatrolBoat_Equipment_Torped47, PatrolBoat_Equipment_NavalMines | 19 |
| VB_VEH_Boat_CB90 | 1 / 25 | PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_HE, PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Smoke, PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Guided, PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Airburst, PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Illumination | 10 |
| VB_VEH_Boat_JetSki | 0 / 13 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Boat_JetSki | 1 / 21 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Boat_RHIB | 0 / 15 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Boat_RHIB | 1 / 16 | OpenGunner_HMG | 5 |
| VB_VEH_Boat_RHIB | 2 / 26 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Boat_RHIB | 3 / 25 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Couch | 0 / 13 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Couch | 1 / 19 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Couch | 1 / 18 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Couch | 1 / 17 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Flyer60 | 0 / 14 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Flyer60 | 1 / 15 | OpenGunner_HMG | 7 |
| VB_VEH_Car_Flyer60 | 2 / 29 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Flyer60 | 3 / 31 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Flyer60 | 4 / 30 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Flyer60_SP | 0 / 20 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Flyer60_SP | 1 / 19 | OpenGunner_HMG | 6 |
| VB_VEH_Car_Flyer60_SP | 2 / 31 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Flyer60_SP | 3 / 32 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Flyer60_SP | 4 / 30 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_JLTV | 0 / 20 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_JLTV | 1 / 23 | RWS_HMG, RWS_AGL, RWS_LMG | 14 |
| VB_VEH_Car_JLTV | 2 / 22 | RWS_LMG | 5 |
| VB_VEH_Car_JLTV | 3 / 21 | RWS_LMG | 5 |
| VB_VEH_Car_Marauder | 0 / 21 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Marauder | 1 / 19 | RWS_HMG, RWS_AGL, RWS_LMG | 15 |
| VB_VEH_Car_Marauder | 2 / 20 | RWS_LMG | 5 |
| VB_VEH_Car_Marauder | 3 / 22 | RWS_LMG | 5 |
| VB_VEH_Car_PTV | 0 / 14 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_PTV | 1 / 29 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_PTV | 2 / 28 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_PTV | 3 / 30 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_QuadBike | 0 / 14 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_QuadBike | 1 / 26 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_TheBeast | 0 / 14 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_TheBeast | 1 / 24 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_TheBeast | 2 / 25 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_TheBeast | 3 / 26 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Vector | 0 / 15 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Vector | 1 / 14 | OpenGunner_HMG | 5 |
| VB_VEH_Car_Vector | 2 / 30 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Vector | 3 / 29 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Vector | 4 / 31 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Vector_M05_CarChase | 0 / 21 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Vector_M05_CarChase | 1 / 20 | OpenGunner_HMG | 5 |
| VB_VEH_Car_Vector_M05_CarChase | 2 / 31 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Vector_M05_CarChase | 3 / 33 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Car_Vector_M05_CarChase | 4 / 32 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Motorcycle_DirtBike01 | 0 / 11 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Motorcycle_DirtBike01 | 1 / 18 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Motorcycle_DirtBike02 | 0 / 11 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Motorcycle_DirtBike02 | 1 / 18 | No WF selected in this entry subtree; fire permission unresolved | 0 |
| VB_VEH_Airplane_F14 | 0 / 19 | Airplane_PrimaryWeapon_Cannon, Airplane_SecondaryWeapon_AirToAirMissile | 4 |
| VB_VEH_Airplane_F14 | 1 / 20 | NavalFighter_PrimaryWeapon_AIM54, Airplane_Passenger_PrimaryWeapon_SemiActiveRadarMissile | 5 |
| VB_VEH_Airplane_F16 | 0 / 20 | Airplane_PrimaryWeapon_Cannon, Airplane_SecondaryWeapon_LightRockets, Airplane_SecondaryWeapon_AirToGroundMissile, Airplane_Bomb_Mk82AIR | 9 |
| VB_VEH_Airplane_F22 | 0 / 19 | Airplane_PrimaryWeapon_Cannon, Airplane_SecondaryWeapon_AirToAirMissile, Airplane_Bomb_GBU39 | 6 |
| VB_VEH_Airplane_FA18F | 0 / 26 | Airplane_PrimaryWeapon_Cannon, Airplane_PrimaryWeapon_Cannon, Airplane_SecondaryWeapon_AirToAirMissile, Airplane_SecondaryWeapon_AntiRadiationMissile, MultirolePlane_PrimaryWeapon_ZuniRockets, Airplane_Bomb_Rockeye | 12 |
| VB_VEH_Airplane_FA18F | 1 / 27 | Airplane_Passenger_PrimaryWeapon_SemiActiveRadarMissile, Airplane_Bomb_BunkerBuster, Airplane_TVMissile | 7 |
| VB_VEH_Airplane_JAS39 | 0 / 20 | Airplane_PrimaryWeapon_Cannon, Airplane_SecondaryWeapon_AirToGroundMissile, Airplane_SecondaryWeapon_LightRockets, Airplane_Bomb_Mk82AIR | 8 |
| VB_VEH_SP_Assault_Airplane_JAS39 | 0 / 22 | Airplane_SecondaryWeapon_AirToGroundMissile, Airplane_SecondaryWeapon_LightRockets, Airplane_Bomb_Mk82AIR | 7 |
| VB_VEH_Airplane_SU57 | 0 / 19 | Airplane_PrimaryWeapon_Cannon, Airplane_SecondaryWeapon_AirToAirMissile_R73, Airplane_Bomb_GBU39 | 6 |
| VB_VEH_Stationary_BGM71TOW | 0 / 14 | Stationary_TOW | 2 |
| VB_VEH_Stationary_Turret_CROWS | 0 / 14 | WF_127_CWSCROWS_HMG, WF_CWS_AGL, WF_CWSCROWS_Spike | 6 |
| VB_VEH_Stationary_GDF009 | 0 / 12 | Stationary_AntiAir | 3 |
| VB_VEH_Stationary_M2MG | 0 / 14 | OpenGunner_HMG | 4 |
| VB_VEH_Stationary_Phalanx | 0 / 10 | SAA_PrimaryWeapon_20mmRotaryCannon | 2 |
| VB_VEH_Stationary_Phalanx_SP | 0 / 10 | WF_SAA_CRAM | 2 |
| VB_VEH_Stationary_SSMBattery | 0 / 13 | SSMBattery_SecondaryWeapon_AntiAirMissile | 1 |
| VB_VEH_Airplane_MQ9 | 0 / 11 | No WF selected in this entry subtree; fire permission unresolved | 1 |
| VB_VEH_Drone_TRV150 | 0 / 14 | No WF selected in this entry subtree; fire permission unresolved | 1 |

### Limits and reopening conditions

Source entry and equipment containment is mapped. Complete active player seat loadouts are not established.

seatIndex is the stored Field_c8750d4f candidate. UI numbering and role-to-entry identity remain unresolved.

The operator card consistency check fails for MBTs and some variants. No class filter was used to force agreement.

Exact U, WMD and Ability references remain equipment configuration identities unless their capability kind is controlled. They are not defaults or proof of availability.

Shared component contexts are retained once, with per-entry assignment null. An empty station WF list is not proof that its occupant cannot fire.

Role, defaults, canFire, exposed and activation remain null where no same-owner semantic control exists.

Unresolved imported GUID targets remain visible in the per-station component import lists. No name-only target join was used.

The one-edge graph route L3110 failed its positive control. It supplies no negative findings. Available ModBuilder source remains untraced.

EA text is corroboration only and its MBT/IFV counts differ from the operator cards. EclipseFPS video access was throttled; no chapter claims or numbers were imported.

No site proposal is made. Reopen only with the exact owner and a passing semantic control for the missing role, capability kind, default, card identity or permission. The failed L3110 graph control remains a dead end, not an absence result.

## Vehicle preset UI census (L3150)

[L3150](../../reference-data/provenance/frosty-2026-10-01-L3150-vehicle-default-ui-census.json) starts the default-loadout pass from four saved current UI roots at build 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. The MAIN BATTLE TANK text control passes its exact local owner, pointer, string id and raw read. The parent independently re-read ECD2AB78 at offset 2608.

The four roots contain 619 objects, 126 text rows and 115 import pairs. UIVehicleLoadoutPresetMetadata has 15 preset text records and no imports. Its MBT and IFV LOADOUT 1 descriptions state vehicle roles; they do not name selected equipment. No resolved text row contains "default" or "unlock". Literal array order is retained, with no default meaning assigned to the first entry or to LOADOUT 1. UIVehicleMetadata retains 25 exact selected UI target pairs for the equipment census.

The UI text control validates this census. It does not validate seat defaults. UH60 minigun, RHIB OpenGunner HMG and MBT seat 0 main gun controls still need an exact UI slot-to-gameplay owner chain plus default selection evidence. Previous card/icon/category/lookup-id routes are not repeated.

Full fields, text ids, slot/flag candidates, GUID pairs, local keys and raw checks stay in `2026-10-01T163631-0400-vehicle-seat-defaults/L3150/ui-census.json`, pinned by the receipt. Unknown hashed field roles remain unresolved. This is UI/source evidence, with no site change.

## Vehicle default UI control route (L3151)

[L3151](../../reference-data/provenance/frosty-2026-10-01-L3151-vehicle-default-ui-controls.json) checks the exact UI preset/slot default route at build 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. Functional default control status: unresolved; the exact owner/default gate failed. The reader/text control passed. The parent reviewed the fixed scope and re-read a consequential operand. UI/import controls and default controls are recorded separately.

25 selected UI targets retain 1111 objects, 170 resolved text rows and 456 import pairs. The UH60 minigun text control passes. The direct import route fails all three functional default controls; no seat default finding follows.

No role, default or active loadout follows from a route name, matching text, first array entry, LOADOUT 1 or an expected control answer. A failed route supplies no negative gameplay finding. The full UI census, exact attempted joins and raw checks remain in the run folder, pinned by this receipt. Excluded SP, cinematic, CarChase, MH47 and Couch roots receive no seat rows.

## Vehicle default UI control route (L3152)

[L3152](../../reference-data/provenance/frosty-2026-10-01-L3152-vehicle-default-ui-controls.json) checks the exact UI preset/slot default route at build 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. Functional default control status: fail. The parent reviewed the fixed scope and re-read a consequential operand. UI/import controls and default controls are recorded separately.

Four fresh UI definition assets declare VehicleSeat, SlotId, PackageId, VehicleEquipmentList and IsSelected/IsAvailable properties. Three imports select other UI definitions, with zero exact saved gameplay-owner matches. The UI dependency and literal string controls pass; the three functional default controls fail the owner/selection gate. Definitions describe data shape and do not prove a configured seat default. No gameplay absence follows.

No role, default or active loadout follows from a route name, matching text, first array entry, LOADOUT 1 or an expected control answer. A failed route supplies no negative gameplay finding. The full UI census, exact attempted joins and raw checks remain in the run folder, pinned by this receipt. Excluded SP, cinematic, CarChase, MH47 and Couch roots receive no seat rows.

## Vehicle seat default UI join coverage (L3154)

Build 1.4.3.5, Head 4909002, descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L3154-vehicle-seat-default-ui-join-coverage.json).

UI route census closed for all 28 catalog vehicle UI metadata assets; 36 exact source roots and 92 entry definitions have ordered seat rows. All 368 default fields remain unresolved because the three required functional default controls fail. The retained 126 weapon configuration selections and 379 equipment configuration references are not active/default loadouts.

The UI census covers 41 raw assets, 2092 objects, 348 text rows and 675 import pairs, including all 28 current vehicle UI metadata assets. The exact source map hash and 1785 distinct source entry/selector/target raw operands agree. UI reader controls pass; the separate factory-default route does not pass the three known answers. No name, category, image, lookup integer or first-element default is substituted.

[Ordered seat rows](../working/VEHICLE_SITE_ADDITIONS.md#vehicle-seat-defaults-current-run-l3150-l3199) record every included entry with separate weapon, ability, countermeasure and upgrade default/alternative fields. The full source identity and UI tables remain in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T163631-0400-vehicle-seat-defaults`, pinned by path/SHA-256 in the receipt. AAV7A1 duplicate stored index 0 and remote/drone assignment limits remain explicit. No defaults or active equipment are asserted; no site changes, recordings, generated build or push. Next evidence must provide a new exact UI producer/default selector that reproduces the three controls.

## Tank directional damage source pass (L3200-L3208)

Build 1.4.3.5, Head 4909002. Descriptor SHA-256: `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. Prior raw assets are reused. Source operands and exact selections are separate from effective damage and hits-to-kill.

### L3202: Five tank damage weapon source comparison

L3202 is partial. All five selected source routes were examined. Five prior same-owner firing scalar controls pass current raw hash, bytes and value reads. Four exported projectile joins and APFSDS override import pass raw checks.

M136 AT and MBT-LAW selected missile owners both retain Field_c30df0ef 500 and Field_58d24a64 0.75. IFV lock-guided missile retains 200 and 0.75. APFSDS selected projectile has 3500 and 0.75. These serialized values do not reproduce EA550,240,450,650 through a proved receiving operation. C4 has another owner key and inherited 0.75. No directional or bypass claim follows.

No site or repository changes. No capture, recording, generated build, commit or push. Native channel composition remains unresolved.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3202-tank-weak-spots.json). Full evidence stays in the run folder at `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\L3202`, with hashes in the receipt.

### L3203: Four vehicle exact damage-part comparison

L3203: Four vehicle source comparisons complete. Actual root health: Leopard 1200; Bradley, CV90 and AAV7A1 1000. Eight exact parts each. All 2137 baseline raw reads reproduce saved hashes and bytes.

CV90 selects three IFV angle curves. Leopard, Bradley and AAV7A1 have null part Field_d3605883 pointers. Leopard, Bradley and CV90 select the exact shared tank schematic. Hash-only part deltas and exact bone-definition child joins are retained in result and supporting files. No runtime multiplier or mesh collision claim is made. No site or repository edits occurred.

Source operation, angle convention, composed damage and exact mesh/collision identity remain unresolved.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3203-tank-weak-spots.json). Full evidence stays in the run folder at `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\L3203`, with hashes in the receipt.

### L3200: Selected RPG source damage and channel gate

L3200 partial: RPG-7V2 selected source owner and exact Damage name chain.

Extraction control passes all 19 archived L645 raw checks, carried forward by current WB raw hash equality. The selected Shot pointer resolves PB_NS_RPG object 1 by exact file and exported-instance GUID. Exact own GRX_Gadgets_Glacier wrapper names Field_91bb7b5f Damage; the receiving raw value is 135. Registry default 125 is separate.

Raw 500 and 0.75 candidates and the immediate explosion owner are retained without damage semantics. The front 188, side 375, rear 500 source mechanism gate remains unresolved. No vehicle-channel, material/grid consumer or effective composition is proven. No site proposal.

The first contract helper misaligned one primitive registry array read. Its result failed the raw expectation; the helper revision and failed reads were retained. Corrected array location passes all 12 contract checks. No negative mechanism conclusion uses that failed read.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3200-tank-weak-spots.json). Full evidence stays in the run folder at `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\L3200`, with hashes in the receipt.

### L3201: Abrams exact part and selected angle curve chain

L3201 is partial. Both corrected controls passed: Front part1000 and VB root1200. Eight exact GUID part labels and selected bone owners were joined. Four selected angle curves were raw checked. Class_1c26a81e carries an identity transform and selects PF_Vehicle_GameplayDamageZones_Tank. No exact source operation reproduces RPG188/375/500. Field_64b3e9cd remains unnamed. No repo or site changes. Large retained evidence is cited by path and SHA-256 in draft-receipt.json. No file exceeds50MB.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3201-tank-weak-spots.json). Full evidence stays in the run folder at `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\L3201`, with hashes in the receipt.

### L3204: Three selected missile Damage and material contracts

L3204 is partial. The RPG named Damage 135 and exact declaring key/member controls pass. Three selected source Damage fields are 125,100,250 for M136 AT, MBT-LAW and IFV lock missile. These are not effective tank damage.

The current controlled M4A1 material struct contract matches all three missiles. Material IDs are 430,651,651. IFV own registry Damage default 150 is separate from actual 250. Own IFV explosion wrapper names are retained, but immediate explosion bodies are layoutAmbiguous. No tank composition or bypass operation is established.

No repo/site change, capture, git command, recording, generated build or push.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3204-tank-weak-spots.json). Full evidence stays in the run folder at `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\L3204`, with hashes in the receipt.

### L3205: Selected launcher to vehicle material-grid relation

L3205: Both same-grid M4276 to Head24 controls passed, full array and slot11 about1.4. Six unique selected cells represent RPG125, M136430, MBT-LAW651 and IFV651 to target119 across Abbasid and Badlands. Each cell selects one exact Class_d4177d69 key88a8412a92f0990e0641d979bac74397. Field_674633de raw values are2,2.200000047683716,0,0 respectively, equal across both grids. No protection-array record occurs in these selected cells.

The complete map, row, cell, group, item and object chain is retained with raw array directory counts, pointers, descriptor keys, relation fields and source declarations. The native operation and damage composition remain unresolved. No damage target or flat bypass is established. No Frosty export, full-grid decode, site edit, repository edit or git operation occurred.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3205-tank-weak-spots.json). Full evidence stays in the run folder at `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\L3205`, with hashes in the receipt.

### L3206: APFSDS and C4 remaining source contracts

L3206 is partial. Both selected profiles were examined.

The current M4A1 source controls pass. APFSDS exact root key and field descriptors match: StartDamage 150, EndDamage 135. Four health/armor curve pointers are null. Its controlled material ID is 431.

C4 selected projectile material ID is 548; immediate explosion material ID is 95. The material struct key and UINT32 member match the controlled source. No positive own explosion semantic control was available for BlastDamage.

No effective tank damage, angle or bypass claim. No repo/site change, capture, git, recording, generated build or push.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3206-tank-weak-spots.json). Full evidence stays in the run folder at `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\L3206`, with hashes in the receipt.

### L3207: APFSDS and C4 selected vehicle material relations

L3207: Three exact new channels and six cells complete. Current grid hashes preserve both prior M4Head known-answer controls. All cells select exact Class_d4177d69 key88a8412a92f0990e0641d979bac74397. Field_674633de values match across Abbasid and Badlands: APFSDS431=2.5, C4projectile548=0, C4explosion95=3.5. C4projectile also has Field_8196a5df0; others have1. Source declaration bytes and exact Struct_1e8e7eef key were rechecked.

198 target-grid raw reads retain matrixmap, rows, cells, groups, items, EBXX count/flags and typed relation operands. No protection-array record occurs in these six selected cells. Field meanings, source operation, composed EA650/350 damage and bypass remain unresolved. No previous target batch, full grid scan, Frosty, capture, repository edit or site edit occurred.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3207-tank-weak-spots.json). Full evidence stays in the run folder at `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\L3207`, with hashes in the receipt.

### L3208: APFSDS and LAW exact selected Damage defaults

L3208 is partial. Two source controls and the prior RPG own registry default control pass.

APFSDS exact selected BulletEntityData wrapper names StartDamage. Its own current registry default is 130, separate from raw projectile value 150. Exact wrapper import, GUID, field hash, member pointer, name bytes and default were reread. No controlled active assignment was found.

MBT-LAW source Damage is 100. Its own MissileEntityData wrapper pointer is zero/null. No default 80 claim is supported by this route.

The EA target arithmetic remains a hypothesis. No repo/site/capture/git/recording/push/generated build.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3208-tank-weak-spots.json). Full evidence stays in the run folder at `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\L3208`, with hashes in the receipt.


### Angle-damage curves (reviewed addendum, 1 October 2026)

Decoded independently with `scripts/frosty-ebx-decode.py` at build 1.4.3.5, Head 4909002, from `builds\1.4.3.5\reports\vehicles-open-layer3-2026-10-01-0132\raw\Common\Hardware\Vehicles\_VehiclesCommon\AngleDamage\` (Class_afbfd124 points: Field_3901db14 angle in degrees, Field_42fc0f5e multiplier). All nine assets decoded, none failed.

| Curve | Points (angle, multiplier) |
|---|---|
| AngleDamageCurve_Tank_Front_Shared | (23, 1.0) (90, 1.1) (157, 1.0) |
| AngleDamageCurve_Tank_Side_Shared | (23, 1.0) (90, 1.9) (157, 1.0) |
| AngleDamageCurve_Tank_Turret_Side_Shared | (23, 1.0) (90, 1.9) (157, 1.0) |
| AngleDamageCurve_Tank_Rear_Shared | (23, 1.0) (76, 3.2) (104, 3.2) (157, 1.0) |
| AngleDamageCurve_IFV_Front_Shared | (23, 1.4) (90, 1.64) (157, 1.4) |
| AngleDamageCurve_IFV_Side_Shared | (23, 1.4) (90, 2.6) (157, 1.4) |
| AngleDamageCurve_IFV_Rear_Shared | (23, 1.4) (73, 3.2) (107, 3.2) (157, 1.4) |
| AngleDamageCurve_ArmoredTransport_Shared | (90, 1.0) |

HitTypeAngle_Small has no points. Abrams parts select the tank curves (L3201): Front to Front, Left and Right to Side, Special 1 and 2 to Turret Side, Rear to Rear. CV90 selects the IFV curves. Leopard, Bradley and AAV7A1 have null curve pointers in the selected part owners, so the curves are shown to apply to Abrams (and CV90) only; Leopard has the same 1200 root health and the same EA tank ranges.

What the curves support: a directional pattern in which rear is greater than side, side is greater than front, and rear is flat between 76 and 104 degrees, falling to the glancing value at 23 and 157 degrees. That fits the operator's answers from play (no recording): one RPG to the side plus one to the rear does not kill a tank, and maximum damage needs a straight-on hit from behind. Both answers are consistent with the curves, but the answer about side plus rear is not independent support, because the EA and creator numbers alone (375 + 500 = 875 of 1000) predict it too.

What they do not support: the EA ratio. Every EA tank range, including the pre-update values, has a maximum-to-minimum ratio of 2.66 to 2.67 (500/188, 550/207, 650/244, 320/120, 200/75; 460/173, 250/94, 750/282 before 1.3.3.0). The curves give a rear-to-glancing span of 3.2, not 2.667, and a common rescale (1000/1200) cancels out of a ratio. The match 3.2 / 1.2 = 2.667 applies the 1.2 to the maximum only, so it is a numeric fit, not a derivation. The RPG points 188 : 375 : 500 are 0.376 and 0.75 of rear; the curves give 0.344 (0.3125 at x1.0) and 0.594. No single scale fits all three. A factor of 1.2, the 1000 part health against the 1200 root health, Field_64b3e9cd (0.7 on most parts) and the angle convention (surface normal versus travel direction) are unexplained.

Open: the creator side value 375 against about 357 expected from x1.9 on an RPG base of 188; Leopard, Bradley and AAV7A1 inheritance or default curves. A discriminating play check, if wanted: three square RPG hits to the side of an Abrams. EA and creator numbers on a 1000 scale predict a kill (3 x 375 = 1125); the raw curve reading predicts none (3 x 357 = 1071 against 1200). The result depends on the hits being square.

Evidence: addendum `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\review-addendum-angle-curves.md`, SHA-256 `3fac68cf20ad7fadde42eb62705aeb43da2ad24881d5c042b0334a21e9b510fc`; review of it `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\review.md`, SHA-256 `7f637576e981c4ec6115cf9bead8ccf745b53203420bb30246619493a24cb605`.

### Direction and zone tables at close

The effective damage mechanism is unresolved. The tables below retain serialized source fields. Field values are not accepted as effective multipliers. Exact pointer chains, GUIDs, hashes and typed reads are in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T164935-0400-tank-weak-spots\direction-zone-table.json`. That file has SHA-256 `936078adfeed94f130e8336c5ba42438d46e66776fda67d71e17e147bc4b8bc3`.

#### tank/aav7a1

Root `Field_9040392c`: 1000. Effective health is unresolved.

| Exact identifier | Object | Part Field_9040392c | Field_64b3e9cd | Selected curve | Effective multiplier |
|---|---|---|---|---|---|
| Front | 3 | 100 | 0.7 | null pointer | unresolved |
| Left | 9 | 100 | 0.7 | null pointer | unresolved |
| Right | 8 | 100 | 0.7 | null pointer | unresolved |
| Rear | 7 | 100 | 0.7 | null pointer | unresolved |
| Special 1 | 2 | 100 | 0.7 | null pointer | unresolved |
| Special 4 | 6 | 100 | 0.7 | null pointer | unresolved |
| WreckLeft | 1 | 100 | 0 | null pointer | unresolved |
| WreckRight | 5 | 100 | 0 | null pointer | unresolved |

#### tank/abrams

Root `Field_9040392c`: 1200. Effective health is unresolved.

| Exact identifier | Object | Part Field_9040392c | Field_64b3e9cd | Selected curve | Effective multiplier |
|---|---|---|---|---|---|
| Front | 2 | 1000 | 0.7 | Tank_Front_Shared | unresolved |
| Right | 10 | 1000 | 0.7 | Tank_Side_Shared | unresolved |
| Left | 8 | 1000 | 0.7 | Tank_Side_Shared | unresolved |
| Rear | 5 | 1000 | 0.7 | Tank_Rear_Shared | unresolved |
| Special 2 | 3 | 1000 | 0 | Tank_Turret_Side_Shared | unresolved |
| Special 1 | 9 | 1000 | 0.7 | Tank_Turret_Side_Shared | unresolved |
| WreckRight | 6 | 100 | 0 | null pointer | unresolved |
| WreckLeft | 7 | 100 | 0 | null pointer | unresolved |

#### tank/bradley

Root `Field_9040392c`: 1000. Effective health is unresolved.

| Exact identifier | Object | Part Field_9040392c | Field_64b3e9cd | Selected curve | Effective multiplier |
|---|---|---|---|---|---|
| Front | 1 | 1000 | 0.7 | null pointer | unresolved |
| Rear | 10 | 1000 | 0.7 | null pointer | unresolved |
| Left | 5 | 1000 | 0.7 | null pointer | unresolved |
| Right | 2 | 1000 | 0.7 | null pointer | unresolved |
| Special 1 | 8 | 1000 | 0 | null pointer | unresolved |
| Special 2 | 3 | 1000 | 0 | null pointer | unresolved |
| WreckRight | 7 | 100 | 0 | null pointer | unresolved |
| WreckLeft | 6 | 100 | 0 | null pointer | unresolved |

#### tank/cv90

Root `Field_9040392c`: 1000. Effective health is unresolved.

| Exact identifier | Object | Part Field_9040392c | Field_64b3e9cd | Selected curve | Effective multiplier |
|---|---|---|---|---|---|
| Front | 5 | 1000 | 1 | IFV_Front_Shared | unresolved |
| Rear | 1 | 1000 | 1 | IFV_Rear_Shared | unresolved |
| Left | 8 | 1000 | 1 | IFV_Side_Shared | unresolved |
| Right | 4 | 1000 | 1 | IFV_Side_Shared | unresolved |
| Special 2 | 3 | 1000 | 1 | IFV_Side_Shared | unresolved |
| Special 1 | 6 | 1000 | 1 | IFV_Side_Shared | unresolved |
| WreckLeft | 2 | 100 | 0 | null pointer | unresolved |
| WreckRight | 10 | 100 | 0 | null pointer | unresolved |

#### tank/leopard

Root `Field_9040392c`: 1200. Effective health is unresolved.

| Exact identifier | Object | Part Field_9040392c | Field_64b3e9cd | Selected curve | Effective multiplier |
|---|---|---|---|---|---|
| Front | 3 | 1000 | 0.7 | null pointer | unresolved |
| Right | 9 | 1000 | 0.7 | null pointer | unresolved |
| Left | 2 | 1000 | 0.7 | null pointer | unresolved |
| Rear | 4 | 1000 | 0.7 | null pointer | unresolved |
| WreckLeft | 7 | 100 | 0 | null pointer | unresolved |
| Special 1 | 5 | 1000 | 0 | null pointer | unresolved |
| Special 2 | 8 | 1000 | 0 | null pointer | unresolved |
| WreckRight | 1 | 100 | 0 | null pointer | unresolved |

#### Known-answer arithmetic

These values use the operator health premise of 1000. They are attributed tank values and conditional arithmetic. The source pass does not establish their use for current IFVs or AAV7A1. Unknown side values remain unresolved.

| Weapon | Front damage / hits | Side damage / hits | Rear damage / hits | Basis |
|---|---|---|---|---|
| RPG-7V2 | 188 / 6 | 375 / 3 | 500 / 2 | EA1.3.3.0 min/max; side operator-supplied creator test |
| M136 AT | 207 / 5 | unresolved | 550 / 2 | EA1.3.1.0 |
| 120 mm APFSDS | 244 / 5 | unresolved | 650 / 2 | EA1.3.3.0 |
| MBT aim-guided shell | 244 / 5 | unresolved | 650 / 2 | EA1.3.3.0 |
| Attack helicopter heavy rockets | 120 / 9 | unresolved | 320 / 4 | EA1.3.3.0 |
| IFV light rockets | 75 / 14 | unresolved | 200 / 5 | EA1.3.1.0 |
| IFV lock-guided missile | 450 / 3 | 450 / 3 | 450 / 3 | EA1.3.3.0 |
| C-4 | 350 / 3 | 350 / 3 | 350 / 3 | EA1.3.1.0 |
| MBT-LAW | 240 / 5 | 240 / 5 | 240 / 5 | EA1.3.1.0 |

No proposal meets the required source multiplier and operation controls. Future `incomingDamageByDirection`, `incomingDamageByZone` and `hitsToKillByDirection` fields remain blocked. Validation targets remain RPG 188/375/500, M136 207-550, APFSDS 244-650 and the stated flat amounts. The RPG side target is operator-supplied creator corroboration. No recording is proposed.

[Close audit](../../reference-data/provenance/frosty-2026-10-01-tank-directional-damage-control-audit.json). The audit cites the full tables and controls by path and SHA-256.

## Vehicle gameplay loadout slots (L3250-L3257)

Build 1.4.3.5, Head 4909002, descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. Source configuration and runtime activation are separate.

### L3250: current slot census

All 688 gameplay loadout and archetype/context routes were captured through the shared lock and decoded with no failures. All 166 slot rows match the prior 1.4.3.0 CSV, including raw SHA-256, ordered options and the separate option reference. 47 rows have one option. In all 166 rows, Field_bf67ccc6 equals the first Field_0a2f2eab option. This does not prove default activation. Exact seat controls and preset selectors were checked in L3251 and L3252.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3250-vehicle-loadout-slots.json). Complete slot rows and raw pointer reads remain in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T-vehicle-loadout-slots-L3250\slot-rows-current.json`, SHA-256 `c46d39ec9982b558c8e3c6bfce224855dc35c695717e0e851b1f03dc6753ab50`.

### L3252: Vehicle preset and context selectors

Build 1.4.3.5; Head 4909002; descriptor SHA-256 4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1.

Control passed. The MBT first preset selects the exact coax slot. That slot selects Eq Coax LMG. All 1,366 independent raw checks passed.

Examined 98/98 scoped assets: 26 numbered presets, 25 archetype markers, and 47 gameplay contexts. See selectors.json for 173 ordered slot occurrences, exact selections, import identities, and raw checks.

All 47 context root pointers resolve. 0 context roots match the exclusion rules; 47 contexts pass the requested name exclusions. This source count does not prove playable coverage. The context records remain in the examined scope.

The 25 archetype marker bodies have no outgoing pointers. Default preset activation remains unconfirmed. No exact imports remain unresolved. No site changes or native runtime claims.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3252-vehicle-loadout-slots.json). Full output remains in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T-vehicle-loadout-slots-L3250\L3252`.

### L3251: Vehicle option and seat controls

Five option controls pass. The Eq U identity, or the Eq Ability U identity, equals the U import in the selected weapon component. That same component imports the exact WF owner in the prior seat map. UH60 Left is serialized seat 1 and Right is seat 2; AH64E Chaingun is seat 1; Abrams Coax LMG and HMG are seat 0. All retained pointer and owner checks pass.

RHIB seat 1 has exact U and WF imports in one component. No Eq option or EqSlot is established for RHIB. This limit does not establish absence. Preset/default activation and runtime use remain unresolved.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3251-vehicle-loadout-slots.json). Full output remains in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T-vehicle-loadout-slots-L3250\L3251`.

### L3253: Vehicle slot and seat source table

Status: partial. Build 1.4.3.5, Head 4909002.

Five same-owner option controls pass. The table has 36 included roots and 92 candidate stations. Two roots and stations are drone context only. The source census has 166 EqSlots, 151 Eq options and 173 ordered preset-slot occurrences.

Exact Eq U, or Eq -> Ability.Field_f86e0433 U, originally found 74 exact U joins, of which 72 had a companion WF. L3257 retains the two U-only seat components and adds five MBT ammo consumer joins. The L3253 table presentation is superseded by L3257. 49 stations have no configured weapon component in the source map. The table retains all stations and all 78 unresolved slots. RHIB candidate seat 1 retains its fixed context Ability/U/WF control.

Each slot retains ordered options, Field_bf67ccc6 selected reference, exact Field_3a640553 marker, and actual preset array references. All 166 selected references equal option 0. 47 slots have one option. These are source facts; initial game selection remains unresolved.

Shared markers group variants only after each slot has an exact option U association to the station. Shared Feature or WMD imports do not assign options. The rejected marker-only method and its AA/MBT collision are recorded in where-not-to-look.json.

4799 raw checks were read again; all match. No site, simulator or game-runtime change was made. No file above 50 MB was created. Earlier revisions of the lead-owned table were replaced by this final bounded method.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3253-vehicle-loadout-slots.json). Full output remains in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T-vehicle-loadout-slots-L3250\L3253`.

### L3255: Vehicle recipe applicability correction

Source pass: partial. This correction supplements L3253. Committed L3253 files remain unchanged.

88 unique recipe variants produce 125 station-variant option associations across 92 retained stations. 114 associations have all options matched to the same station; 11 have partial option matches. Seven selected references do not match the associated station and are not projected onto that station.

False selected cases: Bradley 0/CV90 0 TRV150 MortarDrop; Bradley 1/CV90 1 IFV Passenger Equipment1/3 SmokeLauncher; FA18F 1 Passenger Primary3 JammingPod. Matching alternate options remain exact source facts.

Every rootRecipeIdentityConfirmed flag is false. A recipe with all options matched is source-associated, but recipe applicability remains unresolved. First-preset selected references are conditional on recipe applicability. The corrected table separates partial candidates from all-options source associations. It retains 78 variants with no station association.

Validation checked all 125 associations, their partitions and all 7 removed selected projections. No new raw value, capture, runtime behavior or site change is claimed. Prior five Eq control checks remain the basis of the unchanged option U method; RHIB fixed configuration passes while EqSlot remains unresolved.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3255-vehicle-loadout-slots.json). Full output remains in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T-vehicle-loadout-slots-L3250\L3255`.

### L3254: MBT ammo option condition consumer

L3254: complete

Control: MBT Coax LMG; all 42 stored raw checks re-read and passed.

Five MBT ammo Eq options bind through exact PassiveAbility, DiceFeature, SimEx, Affector, and token U owner pointers. Each token root GUID equals the typed WMD condition GUID. The same five exact WMD owner pairs are direct imports on the Abrams serialized seat 0 component 15 and Leopard serialized seat 0 component 13. Each component imports the exact WF_Vehicles_MBT_PrimaryWeapon_120mm object 11. Component containment and each direct WMD and WF pointer are raw checked for each root.

Preset source selections: MPAT, MPAT, HEShell for Loadout 1, Loadout 2, Loadout 3. No runtime activation or composition claim. No site data or recordings changed. No output over 50 MB created.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3254-vehicle-loadout-slots.json). Full output remains in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T-vehicle-loadout-slots-L3250\L3254`.

### L3256: Remaining vehicle equipment producer chains

Build 1.4.3.5, Head 4909002, descriptor SHA-256 4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1.

All 72 remaining Eq options were traced through their selected producer roles. The MBT APFSDS producer-to-direct-WMD-condition control passed before this batch. No selected producer imports remain missing and no decode failed. The batch establishes no additional seat-consumer join in the controlled component scope. All 2265 distinct retained raw checks agree. Ten options have a raw null selected Ability reference; their exact U roots remain preserved. Vehicle-wide or other native consumers and root-to-recipe applicability remain unresolved. No absence of gameplay effects is claimed.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3256-vehicle-loadout-slots.json). Full output remains in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T-vehicle-loadout-slots-L3250\L3256`.

### L3257: final source table

All 1,124 capture routes passed. All 166 slot rows are byte-identical to the 1.4.3.0 probe and retain their ordered options and selected references. The final table has 151 captured Eq options, of which 149 occur in slot lists. 79 have exact seat-map owners; 77 have companion weapon consumers. 72 remain unresolved. JammingPod and MortarDrop have exact seat-component U owners without a companion WF. Five MBT ammo options join to both main weapon components through exact producer tokens and typed WMD conditions. The fixed 120 mm main weapon is not an EqSlot.

94 unique slot variants produce 138 station-variant associations: 129 have all options matched to the station, and nine are partial candidates. Six selected references do not match their candidate station and are not projected. All 92 source station definitions remain in the table, with the two remote/drone definitions marked separately. All rootRecipeIdentityConfirmed flags remain false. The three preset columns are conditional source recipe selections; Loadout 1 is first preset, default activation unconfirmed. L3257 supersedes L3253/L3255 table presentation. No native playability, recipe applicability or active-default claim is made.

Verification passed for all 166 rows, 389 option references and 173 preset references, plus 36 raw re-reads for the two U-only joins. No site proposal is ready.

[Receipt](../../reference-data/provenance/frosty-2026-10-01-L3257-vehicle-loadout-slots.json). Final table: `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T-vehicle-loadout-slots-L3250\vehicle-slot-table.json`, SHA-256 `7491470cbacff5d2ccb83c52b144fe5218d09d659b4fe05520bd152b879eadcc`. Readable tables: `vehicle-slot-table.md` and `vehicle-slot-table.csv` in the same run folder.

## Vehicle projectile and gun own-wrapper values (L3300, L3301)

[L3300](../../reference-data/provenance/frosty-2026-10-02-L3300-vehicle-projectile-own-values.json) and [L3301](../../reference-data/provenance/frosty-2026-10-02-L3301-vehicle-receiver-supplements.json), Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. The overnight vehicle and gadget program traced 55 selected projectile owners: 54 have scoped source review, CRAM has a method stop, and none has full functional coverage. A selected source path does not prove activation, default loadout, effective damage, units, enum labels or an equation.

Method: the exact vehicle, weapon, firing and projectile selection, plus the selected object's own registry wrapper, names its damage, blast and falloff fields. Where the own wrapper names a role it is an own value; where it does not, an exact current declaring-schema control can supply the name, and the value is then labelled a controlled schema name, not an own name. A control is transferred only when the exact owner key, member and type match; alternate declaring keys (CRAM, older IGLA) are refused.

| Owner | Class | Values |
|---|---|---|
| PB_Missile_TOW2B | Stored source value | Own Damage 150, Drag 0 (2.1.1.0 registry: 0.000454), MaxSpeed 150 (offsets 868, 800, 684; two `Field_` hashes hold 150.0); blast six values. |
| PB_Missile_TOW2B_AirVehicle | Stored source value | Own ten fields; the registry leaf 120 / 20 differs from the receiver 90 / 0 (the own receiver value is the one stored). |
| PRJ_Missile_Hydra70 | Stored source value | Own Damage 15 (2.1.1.0 registry: 12), Drag 0, MaxSpeed 740; local blast six values. |
| IFV APFSDS | Stored source value | Five own-wrapper values; StartDamage 150 against registry default 130. Other APFSDS variants and registry defaults are separate. |
| Guided missiles (MBT guided, stationary TOW, AA aim-guided) | Stored source value | Own nine fields each; own MinimumBlastDamage 0 / 0 (a serialized value only). EngineStrength 150 / 50 / 50, EngineTimeToLive 1 / 3.95 / 3.95, MaxTurnAngle 6 / 90 / 90, TurnAngleMultiplier 1 / 1.5 / 1.5. GuidanceMethod is numeric 3 with no readable label; UnderWaterDrag and FlightRegimeEnabled are own-name stops. |
| Bombs (Rockeye, GBU39, BunkerBuster, Mk82AIR) | Stored source value | 29 own fields on the first three, nine on Mk82AIR. Rockeye blast 0 is not total damage; GBU39 leaf 240 against receiver 200. |
| Rockets (Hellfire, APKWS, Zuni, reduced variants) | Stored source value | Own nine fields each on Hellfire, APKWS and Zuni, with own MinimumBlastDamage hash slots absent (no global absence claim); all 54 rocket receivers across the six rocket owners accepted. |
| Guns (Phalanx, AttackHeli chaingun, M230LF, helicopter guns, coax and RWS, Gepard, light rockets, HMG-SP) | Stored source value | Own seven direct roles each, M230LF seven blast. Chaingun receiver 50 / 50 against leaf 22 / 22. Gepard registry leaves differ from receivers; precedence is unproved. |
| CB90 mortars | Stored source value | Own three Missile roles each plus seven explosion roles on each selected Explosion object; Airburst has two explosion objects. 75 own-named typed receivers across the five owners. |

The parent typed own-wrapper bindings are kept inside the review packets; the supervisor re-read raw bytes and hashes but did not independently reproduce every typed derivation.

## Inherited InitialSpeed and TimeToLive (L3302)

[L3302](../../reference-data/provenance/frosty-2026-10-02-L3302-inherited-projectile-speed-lifetime.json), Head 4909002. The 31 existing exact Missile owners store two inherited Projectile roles, `Field_0bf4f62b` InitialSpeed and `Field_5ef7b9a1` TimeToLive, declared in Class_990616ac (key `2d4898813df1638f89a026d45a64c3be`) at member offsets 144 and 148 (flags 304, type 19); they sit at file offsets 336 and 340 in the selected objects (Class_6a25e89d). All values are Float32. The table lists the 30 vehicle owners; the TracerDart gadget projectile (350 / 20) is on the [gadget page](GADGETS.md#gadget-projectiles-and-explosions-l230), and AGM84 stores 350 / 10.

**Inherited declared default; not shown to be the effective launch speed/lifetime.** These are controlled current-schema source names, not each owner's own registry names; prior own-name stops remain.

| Owner | Selected asset | InitialSpeed | TimeToLive | Acceptance |
|---|---|---:|---:|---|
| owner-02 | PB_Bomb_Rockeye | 350 | 60 | reviewer re-read |
| owner-03 | PB_Bomb_GBU39 | 350 | 60 | reviewer re-read |
| owner-04 | PB_Bomb_Mk82AIR | 350 | 60 | reviewer re-read |
| owner-06 | PB_Bomb_BunkerBuster | 350 | 60 | reviewer re-read |
| owner-09 | PB_Missile_AGM88 | 350 | 15 | reviewer re-read |
| owner-10 | PBNS_Missile_AIM54 | 350 | 15 | reviewer re-read |
| owner-11 | PBNS_Missile_AIM7 | 350 | 15 | reviewer re-read |
| owner-12 | PBNS_Missile_AIM9X | 350 | 15 | reviewer re-read |
| owner-13 | PB_Missile_AGM114_Hellfire | 350 | 10 | reviewer re-read |
| owner-14 | PRJ_Missile_AGM65_Maverick | 350 | 10 | reviewer re-read |
| owner-15 | PBNS_Missile_R73 | 350 | 15 | reviewer re-read |
| owner-16 | PB_Missile_RBS70 | 350 | 6 | reviewer re-read |
| owner-17 | PB_ATGM_Homing_Spike | 350 | 15 | run supervisor |
| owner-18 | PB_Missile_Torped47 | 350 | 40 | reviewer re-read |
| owner-19 | PB_Missile_MBT_GuidedMunition | 350 | 4 | reviewer re-read |
| owner-20 | PB_Missile_TOW2B_AirVehicle | 350 | 11.5 | reviewer re-read |
| owner-21 | PB_Missile_TOW2B | 350 | 8 | reviewer re-read |
| owner-22 | PB_NS_Missile_AA_Secondary_AimGuided | 350 | 11.5 | reviewer re-read |
| owner-23 | PB_NS_Missile_AA_Secondary_HighVelocity | 350 | 11.5 | run supervisor |
| owner-24 | PB_120mmMortar_Airburst | 0 | 30 | run supervisor |
| owner-25 | PB_120mmMortar_Guided | 0 | 30 | run supervisor |
| owner-26 | PB_120mmMortar_HE | 0 | 30 | run supervisor |
| owner-27 | PB_120mmMortar_Illumination | 0 | 30 | run supervisor |
| owner-28 | PB_120mmMortar_Smoke | 0 | 30 | run supervisor |
| owner-29 | PBNS_Stinger_Vehicle | 350 | 15 | run supervisor |
| owner-30 | PRJ_Missile_APKWS-II_Reduced | 250 | 1.35000002 | reviewer re-read |
| owner-31 | PRJ_Missile_APKWS-II | 250 | 1.35000002 | run supervisor |
| owner-32 | PRJ_Missile_Hydra70_Reduced | 250 | 1.35000002 | reviewer re-read |
| owner-33 | PRJ_Missile_Hydra70 | 250 | 1.35000002 | reviewer re-read |
| owner-34 | PRJ_Missile_Zuni | 250 | 1.35000002 | reviewer re-read |

Contrasts with the own wrappers: TOW2B own MaxSpeed 150 against inherited InitialSpeed 350; Hydra70 own MaxSpeed 740 against inherited 250. The same 350 appears on every air-guided, ground-guided and Hellfire owner and 250 / 1.35 on every APKWS, Hydra and Zuni owner, so the pair looks like a base-class default. That is a hypothesis, not a finding: the inherited pair may not drive actual flight for these projectiles.

Acceptance: 18 of the 60 cells were supervisor-accepted in the run. The other 42 (air-guided 16, rockets 10, bombs and ground-guided 16) were parent-reviewed only; they were accepted as source values on a raw re-read of all 31 source files on 2 October 2026, and every stored value matched.

## Vehicle caller and lifecycle chains (L3303)

[L3303](../../reference-data/provenance/frosty-2026-10-02-L3303-vehicle-selection-and-caller-chains.json), Head 4909002. Exact current vehicle root, component and armament paths reach the selected WF weapon exports for the Gepard, for 26 coax and RWS paths (eight tank and car families) and for the five CB90 mortars. The CB90 paths below start at the accepted root 0 to 1 edge.

| Mortar owner | Local path | WF weapon object |
|---|---|---:|
| 24 Airburst | 1 -> 59 -> 37 -> 5 | 4 |
| 25 Guided | 1 -> 59 -> 37 -> 10 | 5 |
| 26 HE | 1 -> 59 -> 40 -> 13 | 6 |
| 27 Illumination | 1 -> 59 -> 37 -> 16 | 7 |
| 28 Smoke | 1 -> 59 -> 37 -> 7 | 6 |

The CB90 hull reaches its motion asset (exported root to object 17 through 1 / 60, then the MM export; labels Input Throttle and Speed exist, with no consumer or units), and the Vehicle Supply Crate reaches its feature (WB to VB root to object 26 through 1 / 24; the feature's local child holds an opaque ResourceRef RID). Own pointers on CRAM are null and its alternate declaring keys block the ordinary-bullet control, so CRAM has a method stop. These paths do not establish station names, availability, defaults, activation or runtime execution.

## RWS AGL damage and vehicle firing and utility findings (L3304)

[L3304](../../reference-data/provenance/frosty-2026-10-02-L3304-vehicle-stats-agl-firing-utility.json), Head 4909002 (a saved pre-Season 5 baseline; L3013 keeps its Head 4892087 label and its AGL raw hash equals the current copy).

Selected chains: Bradley serialized seat candidate 1 is `1 -> 89 -> 54 -> 14` and CV90 is `1 -> 84 -> 55 -> 16`; both select `U_VEH_IFV_RWS_AGL` object 0 and `WF_Vehicles_RWS_AGL` object 3, then firing object 1 and `PB_Vehicle_AGL_Grenade` object 1. RWS, stationary CWS and RWS-SP share that projectile import but remain separate firing owners.

| Channel | Named member | Value | Offset |
|---|---|---:|---:|
| Direct | DamageFalloffStartDistance / EndDistance | 15 / 350 | 700 / 704 |
| Direct | StartDamage / EndDamage | 32 / 32 | 692 / 696 |
| Direct | DamageMultiplier | 1 | 780 |
| Primary explosion | BlastDamage | 70 | 1344 |
| Primary explosion | InnerBlastRadius / BlastRadius | 1 / 4 | 1336 / 1360 |
| Primary explosion | MinimumBlastDamage / ShockwaveDamage / ShockwaveRadius | 0 / 1 / 7.5 | 1352 / 1376 / 1380 |
| Dud explosion | BlastDamage / BlastRadius / ShockwaveDamage | 0 / 5 / 0 | 1840 / 1856 / 1872 |

No composed 102 or 103 damage, radius units or falloff equation is established; registry defaults are separate. Other findings from the same run, all stored source values:

- RWS AGL and HMG reload discriminators MaxAmmoCountInWeapon, MinAmmoCountInWeapon and ReloadType (exact `Struct_b50f190f` key `f772f46b705664a5cadd2fc69f25df37`) all store -1 / -1 / 1. Enum labels, sentinel meaning and the reload operation are unresolved.
- CB90 own configured MaxHealth 1000 (offset 440) and RepairRateModifier 1; the operation linking repair input to the health owner is unresolved.
- Bradley IFV missile Damage 250 (control passes) against registry default 150, which stays separate.
- IFV Thermal Smoke, MBT active protection (Abrams is the representative source context) and AttackHeli flares have exact Eq, Ability and producer identities; AH64E has no exact seat join in L3257. Activation, timers, charges and lock effects are unresolved.

Serialized seat candidate indices are not usable seats, the operator gunner role is separate from the source entry index, the WF is a configured alternative, and active equipment, recipe applicability and default selection remain unresolved.

## Selected declarations and ability chains (L3305, 4 October 2026)

Eleven selected declaration bodies have retained source evidence ([L3305](../../reference-data/provenance/frosty-2026-10-04-L3305-vehicle-declaration-tuples.json)): six Medbay/Combat Awareness declarations and five MBT/IFV regeneration and IFV/AA antispotting declarations. Exact selected-parent imports, exported identities, owning `Field_0c59fa06` name pointers and same-schema three-field FLOAT32 tuples are verified. The physical fields at +64, +68 and +72 are `Field_3ff76ddb`, `Field_42c8b257` and `Field_c06d0cbb`; their roles, units, active/default selection and consuming operations are unknown. The IFV and MBT delay affectors import the same MBT-named export `1ef528cb-2cdb-4644-8f60-c0cdf8f7eff5`. This is source association and declaration evidence, not runtime behaviour. Original Head 4909002 is retained; the cited raw hashes match the current saved files.

Two ability chains ([mapping receipt](../../reference-data/provenance/frosty-2026-10-04-vehicle-passive-and-edc-chain-mappings.json)): the MBT Enhanced Loading ability's list entry [1] and the conditional-passive getter's binding 1 import the same DefaultCategorizationTags pair (file `b7212109-58ca-a203-bb87-d6d32dcc1cd0`, export `73625636-233e-4ba6-a83e-b6e3696c1212`, the tag named "Vehicle Conditional Passive Ability"), byte for byte. Getter binding 2 targets a different tag, "Vehicle Switchable Passive", which the ability does not list. The Car EmergencyDamageControl ability reaches a Helicopter-named DiceFeature, SimEx and ExtraHeal affector with file and export GUIDs matching at each join; the affector holds unlabelled scalars 70.0 and 2.0. The TRV150 movement owner's `Field_8ca2d991` is an unnamed hash-labelled PointerRef in the SDK, which gives no direction or provider. These are authored identities and ownership only. What the getter computes, its polarity, activation, the Enhanced Loading effect, the heal amount or health predicate and Car-versus-Helicopter applicability are unknown, and the MBT-versus-AA Enhanced Loading UI discrepancy is unchanged.

## From the gadget runs: Vehicle Supply Crate and cover health channels

Two gadget runs carry items that belong with vehicles. The rest of those runs is on the [gadget page](GADGETS.md).

- **Vehicle Supply Crate lifecycle** ([L233](../../reference-data/provenance/frosty-2026-10-02-L233-healing-resupply-functional-dossiers.json)): separate construction and pickup-restriction stages. Named current GRX inputs VSC_Enable Auto Construct true, VSC_Time To Construct raw Float32 0.6000000238418579 and VSC_Resupply Interval 5.0; units and effective behaviour are unresolved. UI: a pallet that resupplies ammunition for nearby friendly vehicles.
- **Vehicle health channels** ([L234](../../reference-data/provenance/frosty-2026-10-02-L234-protection-concealment-functional-report.json)): `ChannelBindings_Vehicle_Health` (key `ab89182cfe1957ed44a562cd880a91cf`) has seven pointers into `ChannelList_Vehicle_Common` naming Vehicle Current Health, Vehicle Health Normalized, Vehicle Max Health, VehicleArmor_CurrentArmor, VehicleArmor_MaxArmor, Vehicle Damage State and Vehicle Is Wreck. Deployable Cover's four 200.0 operands are not a health total.

## Operator vehicle loadout screenshots (3 October 2026)

The operator supplied 137 UI screenshots across 13 vehicle folders. The [working research plan](../working/VEHICLE_SITE_ADDITIONS.md#vehicle-screenshot-evidence-and-next-research-paths-3-october-2026) records category seat text, captured slot layouts, all selection-screen descriptions as summaries, and 58 proposed research directions. The local chat will orchestrate the next round; Dex received the reference handoff. The [image index](../../reference-data/frosty/vehicle-loadout-screenshots-2026-10-03.json) retains every path and SHA-256.

The screenshots narrow activation, slot and recipient questions. Key distinctions include MBT versus AA Enhanced Loading, IFV versus AA Systems Upgrade, and driver-selected Attack Helicopter Thermal Optics affecting the gunner. These are attributed UI statements, not new source mappings or runtime findings. The captured build and factory defaults remain unverified; all existing source identity, receiver, units and activation limits remain in force.

## Inherited projectile source review (4 October 2026)

The current mechanics program independently accepted 42 previously parent-reviewed `InitialSpeed` and `TimeToLive` fields across 21 air-guided, rocket and bomb/ground-guided owners. Current raw identity, the complete unique inherited declaration and all stored cells matched. Exact values and source evidence are in `C:/Users/royal/Documents/BF6 Datamining/reports/weapon-analyzer-research/2026-10-03-vehicle-screenshot-program/INHERITED_PROJECTILE_SUPERVISOR_REVIEW.json`. See the [working review](../working/VEHICLE_SITE_ADDITIONS.md#inherited-projectile-review-4-october-2026). These are stored source settings, with units, active selection, effective behavior and runtime composition unresolved. Earlier own-name limits and historical descriptor boundaries remain unchanged.

## Vehicle stat ids, archetypes and blueprints (L3306, 9 October 2026)

Build 1.4.3.5, client 1.0.443.60769, Head 4909067, descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. [Receipt](../../reference-data/provenance/frosty-2026-10-09-L3306-vehicle-stat-archetype-links.json).

`Persistence/StatCategories/StatCategorization/Categorization_Vehicles` holds 33 entries. Each entry stores a stat id string, import pointers to nodes in three category trees and a GUID list. 28 entries import a node in `Category_VehicleArchetypes`; all 33 import a node in `Category_Hardware`. For 30 entries one listed GUID occurs in a saved `VB_VEH_*` blueprint file. This is the first serialized vehicle-to-category link; L3031 and L3032 started from the UI card and found none.

The archetype tree has `archetype_all` with two children. `arch_mastery` holds 13 archetypes: antiair, carapc, fighterplane, heliattack, heliscout, helitrans, ifv, jetattack, jetfleet, jetmultirole, lighttrans, mbt and patrolboat. `arch_mastery_no` holds car, motorcycle and inflatableboat. The four stationary entries and `veh_air_mh47` import no archetype node. The mastery reading of the two parent names is an inference from the names.

All 539 raw checks pass through `frosty-raw-check.py`: entry GUIDs, name pointers and strings, category-array counts, import pointers (value 2 x import index + 1), the 32-byte import records, target node GUIDs and names, tree child pointers, and each blueprint GUID at its offset in both files. Control: `veh_sur_m1a2sepv3` imports `arch_mbt` and lists GUID `6bc50f3e-2272-490e-97ac-140ef69ee3dd`, which occurs in `VB_VEH_Tank_Abrams`.

| Stat id | Archetype | Hardware tree parents | Blueprint with the listed GUID | UI name (name-matched) | UI category text (name-matched) |
|---|---|---|---|---|---|
| `veh_air_m77efalchion` | arch_heliattack | veh_air_helis < veh_air < veh | VB_VEH_Helicopter_AH64E | M77E Falchion | Attack Helicopter |
| `veh_air_panthera` | arch_heliattack | veh_air_helis < veh_air < veh | VB_VEH_Helicopter_Eurocopter | Panthera KHT | Attack Helicopter |
| `veh_air_uh06` | arch_helitrans | veh_air_helis < veh_air < veh | VB_VEH_Helicopter_UH60 | UH-79  | Transport Helicopter |
| `veh_air_f61v` | arch_jetattack | veh_air_jets < veh_air < veh | VB_VEH_Airplane_F16 | F-61V | Attack Bomber |
| `veh_air_f39e` | arch_jetattack | veh_air_jets < veh_air < veh | VB_VEH_Airplane_JAS39 | F-39E | Attack Bomber |
| `veh_air_f97kes` | arch_fighterplane | veh_air_jets < veh_air < veh | VB_VEH_Airplane_F22 | F-97 Kestrel | Fighter Jet |
| `veh_air_su57` | arch_fighterplane | veh_air_jets < veh_air < veh | VB_VEH_Airplane_SU57 | Su-57 | Fighter Jet |
| `veh_sur_m1a2sepv3` | arch_mbt | veh_sur < veh | VB_VEH_Tank_Abrams | M1A2 SEPv3 | Main Battle Tank |
| `veh_sur_leoa4` | arch_mbt | veh_sur < veh | VB_VEH_Tank_Leopard | Leo A4 | Main Battle Tank |
| `veh_breacher` | arch_mbt | veh_sur < veh | none saved |  |  |
| `veh_sur_strf09a4` | arch_ifv | veh_sur < veh | VB_VEH_Tank_CV90 | Strf 09 A4 | Infantry Fighting Vehicle |
| `veh_sur_bradley` | arch_ifv | veh_sur < veh | VB_VEH_Tank_Bradley | M3A3 Bradley | Infantry Fighting Vehicle |
| `veh_sur_ge26pax` | arch_antiair | veh_sur < veh | none saved | GE-26 PAX | Mobile Anti-Air |
| `veh_sur_cheetah1a2` | arch_antiair | veh_sur < veh | VB_VEH_Tank_Gepard | Cheetah 1A2 | Mobile Anti-Air |
| `veh_sur_glider96` | arch_lighttrans | veh_sur < veh | VB_VEH_Car_Flyer60 | Glider 96 | Light Ground Transport |
| `veh_sur_vector` | arch_lighttrans | veh_sur < veh | VB_VEH_Car_Vector | VECTOR | Light Ground Transport |
| `veh_sur_rhib` | arch_inflatableboat | veh_nav < veh | VB_VEH_Boat_RHIB | 7.7m NSW RHIB | Light Transport Boat |
| `veh_sur_travmark2` | arch_carapc | veh_sur < veh | VB_VEH_Car_Marauder | Traverser Mark 2 | Armored Personnel Carrier |
| `veh_sur_ptv` | arch_car | veh_sur < veh | VB_VEH_Car_PTV | Turfpro PTV Royal | Golf Cart |
| `veh_sur_quadbike` | arch_car | veh_sur < veh | VB_VEH_Car_QuadBike | Rugged MV740 | Quad Bike |
| `station_aa_gdf009` | none | stationary_heavy < stationary | VB_VEH_Stationary_GDF009 |  |  |
| `station_at_m41a7tow` | none | stationary_light < stationary | VB_VEH_Stationary_BGM71TOW |  |  |
| `station_autoaa_legion` | none | stationary_heavy < stationary | VB_VEH_Stationary_Phalanx |  |  |
| `station_hmg_madeuce` | none | stationary_light < stationary | VB_VEH_Stationary_M2MG |  |  |
| `veh_air_mh47` | none | veh | VB_VEH_Helicopter_MH47_Insertion |  |  |
| `veh_air_ah6litbird` | arch_heliscout | veh_air_helis < veh_air < veh | VB_VEH_Helicopter_AH6M | AH-6 Little Bird |  |
| `veh_air_mh350` | arch_heliscout | veh_air_helis < veh_air < veh | none saved |  |  |
| `veh_sur_dirtbike01` | arch_motorcycle | veh_sur < veh | VB_VEH_Motorcycle_DirtBike01 | M1030-M1 | Dirt Bike |
| `veh_sur_dirtbike02` | arch_motorcycle | veh_sur < veh | VB_VEH_Motorcycle_DirtBike02 | TM/O 450 | Dirt Bike |
| `veh_sur_ltv` | arch_carapc | veh_sur < veh | VB_VEH_Car_JLTV | LTV | Armored Personnel Carrier |
| `veh_sur_CB90` | arch_patrolboat | veh_nav < veh | VB_VEH_Boat_CB90 | RCB-90 Patrol Boat | Patrol Boat |
| `veh_air_fa18f` | arch_jetmultirole | veh_air_jets < veh_air < veh | VB_VEH_Airplane_FA18F | F/A-81F SUPER SPECTRE | F/A-81F SUPER SPECTRE |
| `veh_air_f14tomcat` | arch_jetfleet | veh_air_jets < veh_air < veh | VB_VEH_Airplane_F14 | F-74A SEACAT | F-74A SEACAT |

The hardware-tree leaf names equal the stat ids except for the two dirt bikes, whose leaves are `veh_sur_moto_db01` and `veh_sur_moto_db02`. `veh_sur_cheetah1a2` lists the Gepard blueprint GUID; `veh_sur_ge26pax` has no blueprint match and its selected GUID occurs in the Tank/Cheetah customization files. `veh_breacher` and `veh_air_mh350` have no saved blueprint match.

The two UI columns are resolved text from the saved per-vehicle UI metadata records, joined by record internal name (for example "Abrams Vehicle"). No saved vehicle or gadget file contains any of those UI record GUIDs, so this join is name matching, not a source link. The F-14 and F/A-18F records carry INTERCEPTOR JET and MULTIROLE JET as short text. `UIVehicleArchetypeMetadata` is byte-identical to the 30 September capture and still has nine cards; no link from an archetype node to a card or display name was found. `Field_d10900b8` and the `Category_Misc` import on six entries are not interpreted. Runtime use of these categories is not established. No site change.

Full rows and raw checks: `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-09-vehicle-archetype-links\L3306`.

## L3307 - Stored values for every vehicle and vehicle equipment stat entry (9 October 2026)

`Categorization_Vehicles` holds 33 entries and `Categorization_Vehicles_Equipment` 66. `scripts/frosty-roster-values.py` traced each from its GUID list to its defining object and carrier files. A vehicle weapon's firing and projectile data is linked inside the vehicle blueprint: the blueprint object that imports the equipment's unlock also points at the `WF_Vehicles_*` weapon data, so the walk starts from those blueprint objects. Ammunition types, upgrades and abilities are carried by `Eq_Vehicle_*`, `PassiveAbility_*`, `Ability_*` and `WMD_Vehicle_*` files, and each `VehicleCustomizationContext_*` file imports one blueprint and the abilities offered on it.

Vehicles: 31 of 33 have a defining object and own values, 30 have `GRX_Vehicles` rows, 24 have a UI name. Equipment: 64 of 66 have a defining object, 42 have own values, 60 have registry rows, 58 have a UI name. No value of any kind: `veh_air_mh350`, `veh_breacher`, `vehec_wp_30revcan`, `veheq_eq_airrevive` (no saved file contains their GUIDs) and `veheq_upg_imparm` (its affector stores no plain number).

Registry default and own value agree for 1,394 owner-and-property pairs across the three rosters and differ for 73, most of them vehicle weapon damage and falloff (for example MBT APFSDS start damage 130 against 150 and falloff 100 to 300 against 50 to 400). Which one a live match uses is not settled by source data.

Evidence class: stored source values with raw-offset checks (11,854 checks over 470 files, all matched). Passive-upgrade and ability rows are joined by a hand-reviewed name table, and equipment UI names by a hand table on designation text; no asset reference links a vehicle UI record to an equipment entry. Units and runtime use are unconfirmed.

Per-entry tables, the unresolved list with what was searched, and the open questions with an in-game test for each are in `docs/working/ROSTER_VALUES.md`. Data: `reference-data/frosty/roster-values.json`. Receipt: `reference-data/provenance/frosty-2026-10-09-L3307-roster-values.json`.
## L3308 - Vehicle missile lock-on values (9 October 2026)

Vehicle missile locking controllers (lock time, release times, ray length, minimum range) are recorded with the gadget launchers in [Gadgets](GADGETS.md), section L3308, and in `reference-data/frosty/locking-controllers.json`. Registry rows and blueprint objects agree except for the ray length of air-to-air default controllers (registry 650 or 665, blueprint 800).

## L3312 - Vehicle ability timings, passive upgrades and radar rules (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3312-vehicle-abilities-passives.json). Dataset: `reference-data/frosty/registry-vehicle-abilities-passives.json` (185 rows, each default read back at its raw offset). Registry defaults from `GRX_Vehicles`; own asset values for the same abilities are in L3307. Meaning is read from row names; units, multiplier direction and use in a match are unconfirmed.

| Ability owner | Active time | Recharge time |
|---|---|---|
| `Ability_APC_ExplosivesDetectionDetonationSystem` | 0.4 | 20 |
| `Ability_APC_Passenger_SmokeLauncher` | 0.25 | 30 |
| `Ability_APC_ProximityDetectionSystem` | 12 | 20 |
| `Ability_AttackHeli_Countermeasure_Flares` | 1.8 | 15 |
| `Ability_AttackHeli_GroundTargetDetection` | 15 | 25 |
| `Ability_AttackPlane_Countermeasure_Flares` | 1.8 | 15 |
| `Ability_CV90_AdvancedThreatDetectionSystem` | 10 | 15 |
| `Ability_CV90_Passenger_SmokeLauncher` | 0.25 | 30 |
| `Ability_CV90_ProximityDetectionSystem` | 12 | 20 |
| `Ability_Car_EmergencyDamageControl` | 0.4 | 24 |
| `Ability_FighterPlane_Countermeasure_Flares` | 1.8 | 15 |
| `Ability_Helicopter_EmergencyDamageControl` | 0.4 | 24 |
| `Ability_MBT_ActiveProtectionSystem` | 5 | 32 |
| `Ability_MBT_ExplosivesDetectionDetonationSystem` | 0.4 | 20 |
| `Ability_MBT_SwitchAmmo` | 0 | 0.5 |
| `Ability_ScoutHeli_Countermeasure_Flares` | 1.8 | 15 |
| `Ability_UH60_Countermeasure_Flares` | 1.8 | 15 |
| `Ability_Vehicle_RWS_ActiveMissileWarningAndKillSystem` | 3.6 | 20 |
| `Ability_Vehicle_SmokeScreen` | 8.1 | 16 |
| `Ability_Vehicle_ThermalSmoke` | 10 | 16 |

| Row | Default |
|---|---|
| `Ability_ThermalSmoke_DestroyC4` | false |
| `Ability_ThermalSmoke_InfantryDamage_BR.DamageInterval` | 0.5 |
| `Ability_ThermalSmoke_InfantryDamage_BR.DamageToDealPerSecond` | 12 |
| `Ability_ThermalSmoke_InfantryDamage_BR.InitialDamage` | 25 |
| `Ability_ThermalSmoke_InfantryDamage_MP.DamageInterval` | 0.5 |
| `Ability_ThermalSmoke_InfantryDamage_MP.DamageToDealPerSecond` | 12 |
| `Ability_ThermalSmoke_InfantryDamage_MP.InitialDamage` | 25 |
| `Ability_Vehicle_SmokeScreen_BlockerDeployInterval` | 0.5 |
| `Ability_Vehicle_SmokeScreen_MinDistanceToDropNewSpotBlocker` | 1 |
| `Ability_Vehicle_SmokeScreen_TimeToExpand` | 1.35 |
| `Ability_Vehicle_SmokeScreen_maxRadius` | 7 |
| `Ability_Vehicle_SmokeScreen_minRadius` | 4.5 |
| `Air Radar In World Spotting Range` | 0.7 |
| `Air Radar Max Range` | 700 |
| `Air Radar Resistance Range Multiplier` | 0.6 |
| `Air Radar Tick Rate` | 1 |
| `Below Radar Activation Delay` | 0 |
| `Below Radar HeightHelicopter` | 25 |
| `BelowRadarHeightJet` | 50 |
| `Disable Below Radar` | false |
| `Disable Below Radar F2P` | false |
| `EmergencyDamageControl_ExtraHealingAmount` | 50 |
| `Ground Radar In World Spotting Range` | 0.4 |
| `Ground Radar Max Range` | 700 |
| `Ground Radar Resistance Range Multiplier` | 0.5 |
| `Ground Radar Tick Rate` | 1 |
| `Is Repair Exhaustion Enabled` | true |
| `MobilityHitDamageThreshold` | 0.5 |
| `MobilityHitDuration` | 5 |
| `MobilityHitTimeFrame` | 3 |
| `Passives_Vehicles_AA_Antispotting_SpotTimeMultiplier.RankData[0].AdditionalSpotTime` | 0 |
| `Passives_Vehicles_AA_Antispotting_SpotTimeMultiplier.RankData[0].IgnoreSelfSpot` | false |
| `Passives_Vehicles_AA_Antispotting_SpotTimeMultiplier.RankData[0].SpotTimeMultiplier` | 0.75 |
| `Passives_Vehicles_AA_Antispotting_TimeToReactivate` | 10 |
| `Passives_Vehicles_AA_EquipmentUpgrade_AirRadarRadiusMultiplier.RankData[0].Value` | 1.5 |
| `Passives_Vehicles_AttackHeli_AntiRadar_AccelerationToMaintain` | 17 |
| `Passives_Vehicles_AttackHeli_AntiRadar_LockOnTime.RankData[0].LockingTimeMultiplier` | 0.7 |
| `Passives_Vehicles_AttackHeli_AntiRadar_SpottingDuration.RankData[0].AdditionalSpotTime` | 0 |
| `Passives_Vehicles_AttackHeli_AntiRadar_SpottingDuration.RankData[0].IgnoreSelfSpot` | false |
| `Passives_Vehicles_AttackHeli_AntiRadar_SpottingDuration.RankData[0].SpotTimeMultiplier` | 0.75 |
| `Passives_Vehicles_AttackHeli_AntiRadar_VelocityToActivate` | 32 |
| `Passives_Vehicles_AttackHeli_AntiRadar_VelocityToMaintain` | 27.5 |
| `Passives_Vehicles_CaptureSpeed_Affector.RankData[0].Value` | 1.15 |
| `Passives_Vehicles_CombatAwareness_EffectRadius` | 20 |
| `Passives_Vehicles_CombatAwareness_SpottingDuration` | 5 |
| `Passives_Vehicles_FighterPlane_AntiRadar_LockOnTime.RankData[0].LockingTimeMultiplier` | 0.7 |
| `Passives_Vehicles_FighterPlane_AntiRadar_SpottingDuration.RankData[0].AdditionalSpotTime` | 0 |
| `Passives_Vehicles_FighterPlane_AntiRadar_SpottingDuration.RankData[0].IgnoreSelfSpot` | false |
| `Passives_Vehicles_FighterPlane_AntiRadar_SpottingDuration.RankData[0].SpotTimeMultiplier` | 0.75 |
| `Passives_Vehicles_IFV_Antispotting_LockOnTime.RankData[0].LockingTimeMultiplier` | 0.6 |
| `Passives_Vehicles_IFV_Antispotting_SpotTimeMultiplier.RankData[0].AdditionalSpotTime` | 0 |
| `Passives_Vehicles_IFV_Antispotting_SpotTimeMultiplier.RankData[0].IgnoreSelfSpot` | false |
| `Passives_Vehicles_IFV_Antispotting_SpotTimeMultiplier.RankData[0].SpotTimeMultiplier` | 0.75 |
| `Passives_Vehicles_IFV_Antispotting_TimeToReactivate` | 10 |
| `Passives_Vehicles_IFV_Durability_DamageRecievedMultiplier` | 0.85 |
| `Passives_Vehicles_IFV_EquipmentUpgrade_ProximityDetectionSystemRadiusMultiplier.RankData[0].Value` | 1.3 |
| `Passives_Vehicles_IFV_Regeneration_Rate` | 110 |
| `Passives_Vehicles_IFV_Regeneration_RegenDelay` | 9.5 |
| `Passives_Vehicles_MBT_Durability_DamageRecievedMultiplier` | 0.85 |
| `Passives_Vehicles_MBT_Regeneration_Rate` | 132 |
| `Passives_Vehicles_MBT_Regeneration_RegenDelay` | 9.5 |
| `Passives_Vehicles_Medbay_EffectInterval` | 0.9 |
| `Passives_Vehicles_Medbay_EffectRadius` | 12.5 |
| `Passives_Vehicles_Medbay_HealOverTime` | 20 |
| `Passives_Vehicles_Medbay_InitialHeal` | 5 |
| `Passives_Vehicles_MobileTrophy_CooldownPerCharge` | 10 |
| `Passives_Vehicles_MobileTrophy_ExcludeOccupantsFromNearbySoldierCheck` | false |
| `Passives_Vehicles_MobileTrophy_MaxCharges` | 3 |
| `Passives_Vehicles_MobileTrophy_NearbyFriendlySoldierRadius` | 13.5 |
| `Passives_Vehicles_ScoutHeli_AntiRadar_AccelerationToMaintain` | 10 |
| `Passives_Vehicles_ScoutHeli_AntiRadar_VelocityToActivate` | 27.5 |
| `Passives_Vehicles_ScoutHeli_AntiRadar_VelocityToMaintain` | 18.5 |
| `Passives_Vehicles_Shared_Durability_MassMultiplier.RankData[0].Value` | 1.04 |
| `Passives_Vehicles_Shared_Durability_ReduceRepairRate` | true |
| `Passives_Vehicles_Shared_EnhancedLoading_HealthThreshold` | 0.6 |
| `Passives_Vehicles_Shared_GunHandling_PitchMultiplier.RankData[0].Value` | 1.3 |
| `Passives_Vehicles_Shared_GunHandling_YawMultiplier.RankData[0].Value` | 1.3 |
| `Passives_Vehicles_Shared_Gunhandling_ImprovedSteeringRatio.RankData[0].Value` | 1.03 |
| `Repair Exhaustion Recovery Rate` | 6 |
| `Repaired Health Threshold Level 1` | 80 |
| `Repaired Health Threshold Level 2` | 295 |
| `Repaired Health Threshold Level 3` | 395 |
| `Repaired Health Threshold Level 4` | 495 |
| `SmokeDischarge_Radius` | 8.4 |
| `Vehicle_Ability_ActiveProtectionSystem_SaturationMechanic` | false |
| `Vehicle_Ability_AttackHeli_GroundTargetDetection_LockOnTimePenalty.RankData[0].LockingTimeMultiplier` | 1.1 |
| `Vehicle_Ability_ExplosivesDetectionDetonationSystem_DetectWhileRecharging` | true |
| `Vehicle_Ability_ExplosivesDetectionDetonationSystem_MaxDetonationDelay` | 0.11 |
| `Vehicle_Ability_ExplosivesDetectionDetonationSystem_PulseTimer` | 1.5 |
| `Vehicle_Ability_ExplosivesDetectionDetonationSystem_Radius` | 30 |
| `Vehicle_Ability_ExplosivesDetectionDetonationSystem_SupressExplosions` | true |
| `Vehicle_Ability_Flare_IsLockableTime` | 2.75 |
| `Vehicle_Ability_GroundTargetDetection_ConeLength` | 250 |
| `Vehicle_Ability_GroundTargetDetection_ConeRadius` | 70 |
| `Vehicle_Ability_GroundTargetDetection_ShouldDisableBelowRadar` | true |
| `Vehicle_Ability_GroundTarget_Detection_RadarRadiusIncrease.RankData[0].Value` | 1.5 |
| `Vehicle_Ability_ProximityDetectionSystem_Radius` | 30 |
| `Vehicle_Ability_SeismicDetector_GraniteMult` | 1 |
| `Vehicle_Ability_SeismicDetector_Radius` | 36 |
| `Vehicle_Ability_SeismicDetector_SpottingDuration` | 2 |
| `Vehicle_Ability_SeismicDetector_TimeBetweenPulses` | 3 |
| `Vehicle_Ability_ThermalScanner_BaseRadius` | 1 |
| `Vehicle_Ability_ThermalScanner_Range` | 135 |
| `Vehicle_Ability_ThermalScanner_SharedSpotDuration` | 1 |
| `Vehicle_Ability_ThermalScanner_TopRadius` | 20 |
| `Vehicle_Ability_ThreatDetectionSystem_ActiveSpotDuration` | 10 |
| `Vehicle_Ability_ThreatDetectionSystem_PassiveSpotDuration` | 4 |
| `Vehicle_Ability_ThreatDetectionSystem_PreActivationBufferTime` | 5 |
| `Vehicle_HUD_Locking_PainterPainterMaxDuration` | 9 |
| `Vehicles_Passives_AA_EnhancedLoading_Stance1.Modifiers[0].WeaponReloadSpeedModifier.ReloadSpeed` | -1 |
| `Vehicles_Passives_AA_EnhancedLoading_Stance1.Modifiers[0].WeaponReloadSpeedModifier.ReloadSpeedMultiplier` | 1.5 |
| `Vehicles_Passives_AA_EnhancedLoading_Stance2.Modifiers[0].WeaponReloadSpeedModifier.ReloadSpeed` | -1 |
| `Vehicles_Passives_AA_EnhancedLoading_Stance2.Modifiers[0].WeaponReloadSpeedModifier.ReloadSpeedMultiplier` | 1.25 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance1.Modifiers[0].WeaponReloadSpeedModifier.ReloadSpeed` | -1 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance1.Modifiers[0].WeaponReloadSpeedModifier.ReloadSpeedMultiplier` | 1.35 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance2.Modifiers[0].WeaponOverheatModifier.HeatDropPerSecond` | -1 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance2.Modifiers[0].WeaponOverheatModifier.HeatDropPerSecondMultiplier` | 1.3 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance2.Modifiers[0].WeaponOverheatModifier.HeatPerBullet` | -1 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance2.Modifiers[0].WeaponOverheatModifier.HeatPerBulletMultiplier` | 1 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance2.Modifiers[0].WeaponOverheatModifier.OverheatDropDelay` | -1 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance2.Modifiers[0].WeaponOverheatModifier.OverheatDropDelayMultiplier` | 1 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance2.Modifiers[0].WeaponOverheatModifier.OverheatThreshold` | -1 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance2.Modifiers[0].WeaponOverheatModifier.OverheatedDropMultiplier` | 1.1 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance2.Modifiers[0].WeaponOverheatModifier.OverheatedPenaltyTime` | -1 |
| `Vehicles_Passives_MBT_EnhancedLoading_Stance2.Modifiers[0].WeaponOverheatModifier.OverheatedPenaltyTimeMultiplier` | 1 |
| `Vehicles_Passives_ScoutHeli_SateliteUplink_SpotDurationMultiplier` | 1.35 |

Open, with the test that would settle each:

- Recharge start point: time each ability from activation to ready and from end of effect to ready.
- Direction of lock-time multipliers: time an enemy lock on an IFV with and without the antispotting upgrade (stored 0.6) and on a helicopter with and without anti-radar (stored 0.7).
- Regeneration: damage a tank with the upgrade, stay out of combat and record the delay (stored 9.5) and the gain per second (stored 132, unit unknown).
- Repair exhaustion: repair a tank through several damage cycles and record repair speed after each stored threshold (80, 295, 395, 495).
- Below-radar heights: fly a helicopter at 20 m and 30 m and a jet at 45 m and 55 m above ground and check whether a lock can start (stored 25 and 50).

## L3313 - Vehicle weapon heat, ammunition, reload and replenish rows (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3313-vehicle-weapon-heat-ammo.json). Dataset: `reference-data/frosty/registry-vehicle-weapon-heat-ammo.json` (701 rows, each default read back at its raw offset). Registry defaults from `GRX_Vehicles`; own asset values are in L3307. Units and use in a match are unconfirmed.

Heat rows. The last two columns are arithmetic on the stored defaults (inference): shots to overheat is 1 / heat per bullet, assuming heat runs 0 to 1 with no cooling while firing; full cool-down is 1 / heat drop per second.

| Owner | Heat per bullet | Heat drop per second | Overheat threshold | Penalty time | Drop delay | Rate of fire | Shots to overheat (inferred) | Full cool-down s (inferred) |
|---|---|---|---|---|---|---|---|---|
| `ALQ99 Jammer` | 0.025 | 0.2 | 0.05 | 0.5 | 1 | 360 | 40 | 5.0 |
| `WF_Vehicles_AA_PrimaryWeapon_AAHV` | 0.036 | 0.5 | - | - | - | 720 | 28 | 2.0 |
| `WF_Vehicles_APC_FiringPortWeapon` | 0.025 | 0.5 | 0.01 | 0 | 0.5 | 981 | 40 | 2.0 |
| `WF_Vehicles_Airplane_PrimaryWeapon_Cannon` | 0.02 | 0.25 | - | - | - | 1200 | 50 | 4.0 |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | 0.05 | 0.5 | 0.01 | 0 | 0.5 | 360 | 20 | 2.0 |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG` | 0.025 | 0.5 | 0.01 | 0 | 0.5 | 720 | 40 | 2.0 |
| `WF_Vehicles_OpenGunner_HMG` | 0.025 | 0.5 | 0.01 | 0 | 0.5 | 500 | 40 | 2.0 |
| `WF_Vehicles_RWS_HMG` | 0.033333 | 0.5 | 0.01 | 0 | 0.5 | 400 | 30 | 2.0 |
| `WF_Vehicles_RWS_HMG-SP` | 0.033333 | 0.5 | 0.01 | 0 | 0.5 | 400 | 30 | 2.0 |
| `WF_Vehicles_RWS_LMG` | 0.025 | 0.5 | 0.01 | 0 | 0.5 | 720 | 40 | 2.0 |
| `WF_Vehicles_SAA_PrimaryWeapon_20mmRotaryCannon` | 0 | 0 | - | - | - | 1200 | - | - |
| `WF_Vehicles_ScoutHeli_Passenger_PrimaryWeapon_ThermalScanner` | 0.025 | 0.2 | 0.05 | 0.5 | 1 | 300 | 40 | 5.0 |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_GAU19` | 0.03125 | 0.3 | 0.1 | 0 | 0.1 | 800 | 32 | 3.3 |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_Minigun` | 0.008889 | 0.3 | 0.1 | 0 | 0.1 | 1800 | 112 | 3.3 |
| `WF_Vehicles_Stationary_AntiAir` | 0.042 | 0.5 | - | - | - | 720 | 24 | 2.0 |
| `WF_Vehicles_TransportHeli_Gunner_Minigun` | 0.006667 | 0.3 | 0.1 | 0 | 0.1 | 1800 | 150 | 3.3 |

Ammunition, rate of fire and reload rows (`-1` is stored as written; its meaning is not established):

| Owner | Magazine capacity | Magazines | Auto replenish magazine | Auto replenish rounds | Auto replenish delay | Rate of fire | Reload time | Reload speed |
|---|---|---|---|---|---|---|---|---|
| `ALQ99 Jammer` | -1 | 1 | false | -1 | 5 | 360 | - | - |
| `WF_Vehicles_AA_PrimaryWeapon_AAAP` | 8 (2.1.1.0: 4) | 16 (2.1.1.0: 32) | true | -1 | 8 | 240 (2.1.1.0: 480) | 2.4 (2.1.1.0: 1.2) | 1 |
| `WF_Vehicles_AA_PrimaryWeapon_AAGP` | 6 | 28 | true | -1 | 8 | 600 (2.1.1.0: 550) | 1.2 | 1 |
| `WF_Vehicles_AA_PrimaryWeapon_AAHV` | 250 | 1 | false | 25 | 8 | 720 | 1.7 | 1 |
| `WF_Vehicles_AA_SecondaryWeapon_AimGuidedMissile` | 1 | 4 | true | -1 | 16 | 120 | 2 | 1 |
| `WF_Vehicles_AA_SecondaryWeapon_AntiAirMissile` | 2 | 2 | true | -1 | 16 | 120 | 8 | 1 |
| `WF_Vehicles_AA_SecondaryWeapon_HighVelocityMissile` | 4 | 2 | true | -1 | 16 | 60 | 8 | 1 |
| `WF_Vehicles_APC_FiringPortWeapon` | 250 | 1 | false | -1 | 5 | 981 | - | - |
| `WF_Vehicles_Airplane_Bomb_BunkerBuster` | 1 | 2 | true | -1 | 10 | 1200 | 5 | 1 |
| `WF_Vehicles_Airplane_Bomb_GBU39` | 1 | 4 | true | -1 | 20 | 120 | 0 | 1 |
| `WF_Vehicles_Airplane_Bomb_Mk82AIR` | 1 | 2 | true | -1 | 30 | 1200 | 0 | 1 |
| `WF_Vehicles_Airplane_Bomb_Rockeye` | 1 | 2 | true | -1 | 30 | 1200 | 0 | 1 |
| `WF_Vehicles_Airplane_Passenger_PrimaryWeapon_SemiActiveRadarMissile` | 2 | 1 | false | 1 | 7.5 | 120 | 8 | 1 |
| `WF_Vehicles_Airplane_PrimaryWeapon_Cannon` | -1 | -1 | false | -1 | 20 | 1200 | - | - |
| `WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile` | 2 | 1 | false | 1 | 10 | 120 | 8 | 1 |
| `WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile_R73` | 2 | 1 | false | 1 | 10 | 120 | 8 | 1 |
| `WF_Vehicles_Airplane_SecondaryWeapon_AirToGroundMissile` | 1 | 2 | true | -1 | 15 | 18 | 5 | 1 |
| `WF_Vehicles_Airplane_SecondaryWeapon_AntiRadiationMissile` | 2 | 1 | false | 1 | 10 | 120 | 8 | 1 |
| `WF_Vehicles_Airplane_SecondaryWeapon_LightRockets` | 7 | 2 | true | -1 | 14 | 300 | 2 | 1 |
| `WF_Vehicles_Airplane_TVMissile` | 1 | 2 | true | -1 | 16 | 18 | 5 | 1 |
| `WF_Vehicles_AttackHeli_Passenger_PrimaryWeapon_Chaingun` | 12 | -1 | true | -1 | 8 | 625 | 1.2 | 1 |
| `WF_Vehicles_AttackHeli_Passenger_SecondaryWeapon_LockingMissile` | 1 | 4 | true | -1 | 20 | 18 | 5 | 1 |
| `WF_Vehicles_AttackHeli_PrimaryWeapon_HeavyRockets` | 4 | 2 | true | -1 | 16 | 300 | 2 | 1 |
| `WF_Vehicles_AttackHeli_PrimaryWeapon_LightRockets` | 12 | 2 | true | -1 | 18 | 300 | 2 | 1 |
| `WF_Vehicles_AttackHeli_PrimaryWeapon_SmartRockets` | 7 | 2 | true | -1 | 14 | 300 | 2 | 1 |
| `WF_Vehicles_AttackHeli_SecondaryWeapon_AirToAirMissile` | 2 | 1 | false | 1 | 10 | 120 | 8 | 1 |
| `WF_Vehicles_AttackHeli_SecondaryWeapon_TOW` | 1 | 4 | true | -1 | 20 | 18 | 5 | 1 |
| `WF_Vehicles_IFV_PrimaryWeapon_APFSDST` | 10 | 20 | true | -1 | 20 | 160 | 2.75 | 1 |
| `WF_Vehicles_IFV_PrimaryWeapon_Canister` | 16 | 20 | true | -1 | 20 | 240 | 2.75 | 1 |
| `WF_Vehicles_IFV_PrimaryWeapon_HEAB` | 12 | 20 | true | -1 | 20 | 180 | 2.75 | 1 |
| `WF_Vehicles_IFV_SecondaryWeapon_HomingATGM` | 1 | 6 | true | -1 | 20 | 150 | 9.5 | 1 |
| `WF_Vehicles_IFV_SecondaryWeapon_LightRockets` | 2 | 4 | true | -1 | 20 | 300 | 0 | 1 |
| `WF_Vehicles_IFV_SecondaryWeapon_TOW` | 1 | 6 | true | -1 | 20 | 150 | 8.2 | 1 |
| `WF_Vehicles_MBT_PrimaryWeapon_120mm` | 1 | 20 | true | -1 | 14 | 900 | 4.1 | 1 |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | 250 | 1 | false | -1 | 5 | 360 | - | - |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG` | 250 | 1 | false | -1 | 5 | 720 | - | - |
| `WF_Vehicles_MultirolePlane_PrimaryWeapon_ZuniRockets` | 4 | 2 | true | -1 | 16 | 300 | 2 | 1 |
| `WF_Vehicles_OpenGunner_HMG` | 250 | 1 | false | -1 | 5 | 500 | - | - |
| `WF_Vehicles_RWS_AGL` | 5 | 10 | false | -1 | 5 | 325 | 2 | 1 |
| `WF_Vehicles_RWS_HMG` | 250 | 1 | false | -1 | 5 | 400 | - | - |
| `WF_Vehicles_RWS_HMG-SP` | 250 | 1 | false | -1 | 5 | 400 | - | - |
| `WF_Vehicles_RWS_LMG` | 250 | 1 | false | -1 | 5 | 720 | - | - |
| `WF_Vehicles_RWS_TargetDesignator` | -1 | 1 | false | -1 | 5 | - | - | - |
| `WF_Vehicles_SAA_PrimaryWeapon_20mmRotaryCannon` | -1 | -1 | false | -1 | 20 | 1200 | 0 | 1 |
| `WF_Vehicles_ScoutHeli_Passenger_PrimaryWeapon_ThermalScanner` | -1 | 1 | false | -1 | 5 | 300 | - | - |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_GAU19` | 100 | 4 | false | -1 | 20 | 800 | 0 | 1 |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_Minigun` | 100 | 4 | false | -1 | 20 | 1800 | 0 | 1 |
| `WF_Vehicles_ScoutHeli_SecondaryWeapon_AirToAirMissile` | 2 | 1 | false | 0 | 10 | 120 | 5 | 1 |
| `WF_Vehicles_Stationary_AntiAir` | -1 | -1 | false | 25 | 8 | 720 | 1.7 | 1 |
| `WF_Vehicles_Stationary_TOW` | 1 | -1 | false | -1 | 5 | 150 | 10.8 | 1 |
| `WF_Vehicles_TransportHeli_Gunner_Minigun` | 100 | 4 | false | -1 | 20 | 1800 | 0 | 1 |

Open, with the test that would settle each:

- Heat scale and the meaning of the overheat threshold: hold fire with the tank coaxial heavy machine gun, count shots to overheat, then time the lock-out and the return to zero heat.
- Replenish: empty a vehicle weapon's reserve and time each returning round or magazine against the stored delay.
- Rate of fire unit: count shots in a 5 s burst from a recording.
- Which side is live where the registry and the weapon asset differ (see L3314).

## L3321 - Mine damage against tanks is stored blast damage times the material-grid value (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3321-mine-tank-material-grid.json). Dataset: `reference-data/frosty/mine-tank-material-grid.json`. This extends L3205 and L3207, which read the same grid field without an official number to compare.

Each mine's explosion object stores a material ID. The level material grid cell for that material against target 119 (the tank target of L3205) holds `Field_674633de`. Multiplying the stored blast damage by it gives EA's [1.3.1.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) damage against tanks exactly. Values are equal in the Abbasid and Badlands grids. Official names are joined to owners by name only.

| Item | Owner | Explosion material | Stored blast damage | Grid value | Product | EA against tanks |
|---|---|---|---|---|---|---|
| EOD Bot mine | `PB_NS_EODBot_Mines` | 96 | 150 (asset own value, no registry row) | 2 | 300 | 300 |
| M15 AV Mine | `PBNS_ATMine` | 96 | 195 (registry default; asset own value 300) | 2 | 390 | 390 |
| PTKM-1R | `PB_PRJ_PTKM1R_EFP` | 650 | 160 (2.1.1.0: 142) (asset own value, no registry row) | 3 | 480 | 480 |

The M15 matches only with the registry default 195; its own 300 would give 600 (see L3320 in `docs/working/ROSTER_VALUES.md`). The PTKM-1R uses a different material and grid value, so it is an independent match. This is a correspondence on three items, not a proof of the game's operation.

All cells read against target 119:

| Source material | Used by | Grid value |
|---|---|---|
| 91 | SLAM body explosion | 1 |
| 94 | PTKM-1R combat element explosion | 0.4 |
| 95 | C4 explosion (control, L3207: 3.5) | 3.5 |
| 96 | mine explosion (M15, EOD Bot mine) | 2 |
| 99 | naval mine explosion | 0 |
| 125 | RPG projectile (control, L3205: 2) | 2 |
| 141 | mine projectile (M15, EOD Bot mine, SLAM body) | 0 |
| 164 | RPG explosion | 0 |
| 174 | SLAM EFP explosion | 0 |
| 208 | EFP projectile (PTKM-1R, SLAM) | 0.4375 |
| 650 | PTKM-1R EFP explosion | 3 |

Still open, with the test that would settle each:

- Target 119 is not named in stored data. One M15 under a main battle tank and one under an infantry fighting vehicle: equal readings of 390 would mean both use the same target material.
- Direct-hit weapons are not checked. One RPG hit square on a tank's side at close range, compared with registry Damage 125 times 2 and the side angle curve.
- The SLAM's cells (0.4375, 0 and 1) do not reproduce EA's 199 to 363. SLAM hits on the side, front and underside of a full-health tank.
- No reading on the current build. One PTKM-1R full hit on a full-health tank should read 480.

## L3322 - Anti-air damage against aircraft: the material grid stores half of each multiplier (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3322-anti-air-aircraft-material-grid.json). Dataset: `reference-data/frosty/anti-air-aircraft-material-grid.json`. This answers the open item of L3318 (multipliers 4, 5 and 10) as far as stored data goes, with the method of L3321.

| Ammunition | Owner | Projectile material | Registry StartDamage | Grid value | Product | EA number | EA / product |
|---|---|---|---|---|---|---|---|
| High velocity | `PD_Vehicles_AA_PrimaryWeapon_AAHV` | 642 | 13 (2.1.1.0: 25) | 2 (targets 121, 669) | 26 | 52 (helicopters) | 2 |
| High velocity | same | 642 | 13 | 2.5 (targets 120, 207, 233, 670) | 32.5 | 65 (jets) | 2 |
| Armour piercing | `PD_Vehicles_AA_PrimaryWeapon_AAAP` | 577 | 20 (2.1.1.0: 50) | 5 (all six targets) | 100 | 200 (aircraft) | 2 |
| General purpose | `PD_Vehicles_AA_PrimaryWeapon_AAGP` | 577 | 13 (2.1.1.0: 34) | 5 (all six targets) | 65 | 130 (aircraft) | 2 |

The grid reproduces the helicopter to jet ratio and the single aircraft number, and EA's figures are exactly twice the product every time. That last factor 2 is not traced. Each cell also stores `Field_7fa53094` = 2, but the mine cells of L3321 store the same 2 and need no extra factor. Which targets are helicopters and which are jets is inferred from EA's numbers only. Values are equal in the Abbasid and Badlands grids. Official names are joined to owners by name only.

The mine explosion material (96) reads 11 against the same six targets.

Still open, with the test that would settle each:

- The remaining factor 2. One high velocity rocket hit on a full-health helicopter: 52 confirms twice the product; 26 would mean EA counts a pair of hits.
- Target identities. The same single hit on a transport helicopter, an attack helicopter and a jet: 52, 52 and 65 would confirm the split.
- Mines against aircraft. Land a helicopter on an M15 mine: a grid value of 11 would destroy it outright.

## L3323 - EA's vehicle damage figures follow registry damage times the material-grid value (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3323-vehicle-damage-material-grid-rule.json). Dataset: `reference-data/frosty/vehicle-damage-material-grid-rule.json`. This builds on L3205, L3207, L3321 and L3322 and gives the first rule that reproduces EA's [1.3.1.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) figures from stored numbers.

The rule, with `Field_674633de` of the level material grid as the grid value:

- Tanks (target 119): registry direct damage x grid value x a hit-quality factor from 0.75 to 2. EA's low figure is the product x 0.75 rounded up; the high figure is the product x 2. Every cell read also stores `Field_7fa53094` = 2; that this is the top factor is an inference.
- Helicopters (target 121) and jets (target 120): registry direct damage x grid value, plus registry blast damage x the blast material's grid value. No hit-quality factor. EA caps jets at 1000.
- Mines (L3321): blast damage x grid value only.

All four EA figures reproduced exactly (24 numbers). Official names are joined to owners by name only; one grid (Abbasid) was read.

| EA item | Owner | Registry direct damage | Grid: tank / helicopter / jet | Registry blast damage (grid: helicopter / jet) | Tanks, rule | Tanks, EA | Helicopters, rule | Helicopters, EA | Jets, rule | Jets, EA |
|---|---|---|---|---|---|---|---|---|---|---|
| 120mm HEMP-T Rounds | `PD_Vehicles_MBT_AmmoTypes_HE` | 120 | 2 / 9 / 10 | 100 (1 / 2) | 180 to 480 | 180 to 480 | 1180 | 1180 | 1000 | 1000 |
| 120mm HEAT-MP-T Rounds | `PD_Vehicles_MBT_AmmoTypes_MPAT` | 140 | 2 / 9 / 10 | 100 (1 / 2) | 210 to 560 | 210 to 560 | 1360 | 1360 | 1000 | 1000 |
| IFV Light Rockets | `PD_Vehicles_IFV_SecondaryWeapon_LightRockets` | 50 | 2 / 9 / 10 | 100 (1 / 2) | 75 to 200 | 75 to 200 | 550 | 550 | 700 | 700 |
| Helicopter Light Rockets | `PRJ_Missile_Hydra70` | 15 (2.1.1.0: 12) | 2 / 9 / 10 | 90 (1 / 2) | 23 to 60 | 23 to 60 | 225 | 225 | 330 | 330 |
| Helicopter Aim-Guided Rockets | `PRJ_Missile_APKWS-II` | 30 | 2.2 / 8 / 10 | 80 (1 / 2) | 50 to 132 | 50 to 132 | 320 | 320 | 460 | 460 |
| IFV AP shells | `PD_Vehicles_IFV_PrimaryWeapon_APFSDS` | 100 | 0.3 / 1 / 1 | none | 23 to 60 | 23 to 60 | 100 | 100 | 100 | 100 |

Fit only with an earlier damage value (taken as changed after 1.3.1.0; earlier registry copies are not saved):

| EA item | Owner | Registry direct damage | Grid: tank / helicopter / jet | Registry blast damage (grid: helicopter / jet) | Tanks, rule | Tanks, EA | Helicopters, rule | Helicopters, EA | Jets, rule | Jets, EA |
|---|---|---|---|---|---|---|---|---|---|---|
| Helicopter Heavy Rockets | `PRJ_Missile_Zuni` | 64 | 2.5 / 4 / 5 | 100 (1 / 2) | 120 to 320 | 94 to 250 | 356 | 300 | 520 | 450 |
| 120mm APFSDS Rounds | `PD_Vehicles_MBT_AmmoTypes_APFSDS` | 130 | 2.5 / 4 / 5 | 0 (0 / 0) | 244 to 650 | 282 to 750 | 520 | 600 | 650 | 750 |
| RPG | `PB_NS_RPG` | 125 | 2 / 9 / 10 | 70 (0 / 0) | 188 to 500 | 173 to 460 | 1125 | 1035 | 1000 | 1000 |

Heavy Rockets fit with direct damage 50 (now 64), the RPG with 115 (now 125), tank APFSDS with 150 (now 130; 130 gives 650, the figure of a later note, see L3318). Update 1.3.3.0 restates all three (Heavy Rocket 120 to 320 / 356 / 520, RPG 188 to 500 / 1125, tank APFSDS 244 to 650 / 520 / 650), and today's registry values give exactly those figures; see L3324 in `docs/working/ROSTER_VALUES.md`.

Does not fit: the mobile anti-air figures of L3322 are twice what this rule gives for aircraft.

Still open, with the test that would settle each:

- The hit-quality factor is not tied to the stored angle curves. Tank HE at a tank's front, side and rear from 20 m: 180 and 480 are the stored extremes.
- The anti-air factor 2. One high velocity rocket hit on a full-health helicopter: 26 means EA counts a pair, 52 means a further multiplier.
- Current values. One RPG hit on a tank's rear should read 500; one tank APFSDS hit on a tank's rear should read 650.
- Other maps. One tank HE rear hit on a second map: 480 on both confirms the grid values are shared.

## L3325 - Dead end: which stored fields carry the hit-quality factor and the anti-air factor 2 (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3325-vehicle-damage-factor-candidates.json). Dataset: `reference-data/frosty/vehicle-damage-factor-candidates.json`. Recorded as a dead end for source-only research. It follows the two factors left untraced by L3322 and L3323.

Candidates found:

| Stored value | Where | Equals |
|---|---|---|
| `Field_58d24a64` = 0.75 | projectile object of all 24 weapon and mine files read | low end of EA's tank ranges |
| `Field_7fa53094` = 2 | every material-grid cell read with a non-zero damage value | high end of EA's tank ranges |
| `Field_84b71f89` = 1 | the three mobile anti-air rounds only (2 in every other round of that class) | the group whose figures are twice the rule |

What was searched:

- Every numeric field of the projectile object of 24 weapon and mine files was listed and compared between the weapons that fit the L3323 rule and the three mobile anti-air rounds that are twice the rule.
- Field_58d24a64 is 0.75 in all 24 projectile objects, equal to the low end of EA's tank ranges. It never varies, so no weapon can show whether changing it changes the low figure.
- Field_7fa53094 is 2 in every material-grid cell read with a non-zero damage value (tank, helicopter and jet targets, both grids where read), equal to the high end of EA's tank ranges. It never varies either, and aircraft cells hold the same 2 although aircraft figures show no range.
- Field_84b71f89 is 1 in the three mobile anti-air rounds and 2 in every other projectile of the same class. It is the only stored difference found that lines up with the anti-air figures being twice the rule. No registry row names it.
- Field_be8c8762 (2, 5 or 6) and Field_c30df0ef (35 to 5000) vary but do not line up with either factor.
- The registry rows of the anti-air rounds (damage, falloff, speed, gravity, drag, lifetime, DamageMultiplier 1) hold no 2.
- The stored angle curves of L3201 (side 1 to 1.9, front up to 1.1, rear 3.2) do not give 0.75 to 2.
- Game code is not in the saved data, so which field the game reads cannot be seen.

The damage rule of L3323 does not depend on which field carries the factors.

Open, with the test that would settle it:

- Tank HE at a tank from the front, the side and the rear at 20 m: three readings between 180 and 480 give the factor per direction.
- One high velocity anti-air round on a full-health helicopter (26 or 52), then one IFV AP shell on the same helicopter (100 expected).

## L3327 - The damage rule extended to launchers, C-4 and jet bombs (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3327-damage-rule-launchers-c4-bombs.json). Dataset: `reference-data/frosty/vehicle-damage-rule-extension.json`. This applies the rule of L3323 to the weapons EA quotes in its [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) that were not yet checked. Cells were read in the Abbasid and Badlands grids and are equal. EA item names are joined to owners by name only.

Seven further items reproduce every EA figure (26 numbers). Where the summed jet figure is 1000 or more, EA states 1000.

| EA item | Owner | Direct damage | Grid: tank / helicopter / jet | Blast damage | Grid: tank / helicopter / jet | Tanks, rule | Tanks, EA | Helicopters, rule | Helicopters, EA | Jets, rule | Jets, EA |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M136 AT | `PB_AT4` | 125 (own, no registry row) | 2.2 / 8 / 10 | 70 (own, no registry row) | 0 / 0 / 0 | 207 to 550 | 207 to 550 | 1000 | 1000 | 1250 | 1000 |
| MBT-LAW | `PB_MBTLAW` | 100 (own, no registry row) | 0 / 0 / 0 | 80 (own, no registry row) | 3 / 6.5 / 10 | 240 | 240 | 520 | 520 | 800 | 800 |
| SLM-93A | `PB_NS_Stinger` | 100 (own, no registry row) | 0 / 6.5 / 6.5 | 100 (own, no registry row) | 2 / 0 / 0 | 200 | 200 | 650 | 650 | 650 | 650 |
| 9K93 IGLA | `PB_NS_IGLA` | 100 (own, no registry row) | 0 / 6.5 / 6.5 | 100 (own, no registry row) | 2 / 0 / 0 | 200 | 200 | 650 | 650 | 650 | 650 |
| C-4 packs | `PNS_C4` | none | none | 100 (own, no registry row) | 3.5 / 3.5 / 15 | 350 | 350 | 350 | 350 | 1500 | 1000 |
| Attack Jet Mk82 High Drag Bombs | `PB_Bomb_GBU39` | 40 (registry; own 40) | 2 / 9 / 10 | 240 (registry; own 200) | 1 / 3 / 4 | 300 to 400 | 300 to 400 | 1080 | 1080 | 1360 | 1000 |
| Fighter Jet GBU-39/B Small Diameter Bombs | `PB_Bomb_Mk82AIR` | 50 (registry; own 50) | 2 / 9 / 10 | 335 (registry; own 335) | 1 / 3 / 4 | 410 to 535 | 410 to 535 | 1455 | 1455 | 1840 | 1000 |

What this adds to the rule:

- **Blast against tanks.** The MBT-LAW, the SLM-93A, the IGLA and C-4 deal no direct damage to tanks (grid value 0 or no direct damage field); their whole tank figure is blast damage times the blast material's grid value, with no range. For the bombs the tank range is the direct part times 0.75 to 2 plus a fixed blast part (GBU-39 file: 60 to 160 plus 240).
- **Asset values where no registry row exists.** The M136 AT, MBT-LAW, SLM-93A, IGLA and C-4 projectiles have no registry damage row; their own stored values give EA's figures.
- **One more disputed property follows the registry.** `PB_Bomb_GBU39` BlastDamage is 240 in the registry and 200 in the asset. 240 gives 300 to 400 / 1080; 200 would give 260 to 360 / 960. That makes 26 of 73 (see L3324 in `docs/working/ROSTER_VALUES.md`).
- **The factor steps are EA's own.** The same notes state that turret hits deal 75%, the body at least 100%, a favourable side angle 150% and a favourable rear angle 200%. The rule's range 0.75 to 2 is these steps; the in-game RPG rear reading of L3326 (500) is the 200% step.

Three things do not fit or are not settled:

- **Bomb names are crossed.** The file `PB_Bomb_GBU39` gives the figures EA lists for the attack jet's Mk82 (300 to 400 / 1080), and `PB_Bomb_Mk82AIR` gives the figures EA lists for the fighter jet's GBU-39 (410 to 535 / 1455). Read by file name, neither matches. Either the notes swap the two lines or the files are used the other way round; stored data does not say which.
- **IFV HEI-T low figure.** EA states 10 to 30 against tanks. The rule gives 12 to 30 (registry StartDamage 50 x 0.3). Helicopters (100) and jets (150) match. L3324 recorded EA's low figure as absent; the notes do state 10.
- **M4A1 SLAM.** EA states 199 to 363. The EFP gives 43 to 113.75 (StartDamage 130 x 0.4375) and 143 to 213.75 with the body explosion (100 x 1) added. A direct product of 131.25 plus the body's 100 would give 199 to 362.5, but no stored damage value gives 131.25. This remains a dead end for stored data, as in L3321.

A registry row `PB_C4...BlastDamage` stores 180. No saved file has that name and no stored link to the C-4 projectile `PNS_C4` (own value 100) was found. 100 x 3.5 is EA's 350; 180 x 3.5 would be 630.

Still open, with the test that would settle each:

- Bomb identity. Drop one bomb from the fighter jet on a full-health tank's body: about 320 means the GBU-39 file's values, about 435 the Mk82 file's.
- C-4 value. One C-4 pack on a full-health tank: 350 (asset 100) or 630 (registry row 180).
- HEI-T low figure. One IFV HEI-T hit on a tank's turret: 10 or 12.
- SLAM. One SLAM against a full-health tank's side, front and underside, three readings.
- Current values. EA's figures are from update 1.3.1.0. One M136 AT hit on a tank's rear should read 550; one MBT-LAW hit 240.

## L3328 - Target materials of all vehicles, and grid values against light vehicles (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3328-vehicle-target-materials.json). Dataset: `reference-data/frosty/vehicle-target-materials.json`. This answers the open item of L3321 (whether the IFV uses target 119) from stored data. Each vehicle's `_DamageZones` file stores a material ID on its parts, read the same way as the Abrams parts in L3201. All 37 saved files were read.

| Target material | Vehicles (file names) |
|---|---|
| 116 | `Stationary_GDF009` |
| 119 | `Car_JLTV`, `Car_Marauder`, `Stationary_Turret_CROWS`, `Tank_AAV7A1`, `Tank_Abrams`, `Tank_Bradley`, `Tank_CV90`, `Tank_Gepard`, `Tank_Leopard` |
| 120 | `Airplane_F16`, `Airplane_F22`, `Airplane_JAS39`, `SP_Assault_Airplane_JAS39`, `Airplane_SU57` |
| 121 | `Helicopter_AH64E`, `Helicopter_AH6M`, `Helicopter_AH6M_M05_SP_Cine`, `Helicopter_Eurocopter`, `Helicopter_Eurocopter_SP`, `Helicopter_MH47_SP`, `Helicopter_UH60` |
| 122 | `Boat_RHIB`, `Car_Flyer60`, `Car_Flyer60_SP`, `Car_Vector`, `Car_Vector_M05_CarChase` |
| 123 | `Car_TheBeast`, `Stationary_Phalanx`, `Stationary_Phalanx_SP` |
| 187 | `Car_PTV`, `Car_QuadBike`, `Motorcycle_DirtBike01`, `Motorcycle_DirtBike02` |
| 233 | `Airplane_MQ9` |
| 313 | `Boat_CB90` |
| none stored (material 0 only) | `Stationary_M2MG` |

Material 0 also appears on two parts of each tracked vehicle and one part of several helicopters. Files with `SP`, `M05` or `Cine` in the name are campaign or cinematic variants.

So the IFVs (Bradley, CV90), the AAV7A1, the Gepard and the two armoured cars use the same target material as the tanks, and every grid value read for target 119 applies to them. Light vehicles use three other materials, and the grid values against those are different. Selected rows (all weapons are in the dataset; values are equal in the Abbasid and Badlands grids):

| Weapon | Part | Material | 119 | 121 | 120 | 122 | 187 | 123 | 116 | 233 |
|---|---|---|---|---|---|---|---|---|---|---|
| 120mm HEMP-T Rounds | direct | 125 | 2 | 9 | 10 | 5.5 | 5 | 5.5 | 5.5 | 10 |
| 120mm HEMP-T Rounds | blast | 130 | 0 | 1 | 2 | 3 | 4 | 3 | 1.5 | 2 |
| MBT 120mm APFSDS Rounds | direct | 431 | 2.5 | 4 | 5 | 5.5 | 5 | 5.5 | 5.5 | 5 |
| MBT 120mm APFSDS Rounds | blast | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| IFV AP shells | direct | 460 | 0.3 | 1 | 1 | 1.25 | 2.6 | 1 | 1 | 1 |
| IFV HEI-T Rounds | direct | 459 | 0.3 | 2 | 3 | 1.25 | 2.6 | 1.7 | 1 | 3 |
| IFV HEI-T Rounds | blast | 129 | 0 | 0 | 0 | 1 | 1 | 1 | 0.5 | 0 |
| Mobile AA High Velocity | direct | 642 | 0.35 | 2 | 2.5 | 1.25 | 2.6 | 1.25 | 1 | 2.5 |
| MAS 148 Glaive | direct | 651 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| MAS 148 Glaive | blast | 650 | 3 | 6.5 | 10 | 7 | 7 | 3 | 3.5 | 10 |
| RPG-7V2 | direct | 125 | 2 | 9 | 10 | 5.5 | 5 | 5.5 | 5.5 | 10 |
| RPG-7V2 | blast | 164 | 0 | 0 | 0 | 0.3 | 8.5 | 0.3 | 0.15 | 0 |
| M136 AT | direct | 430 | 2.2 | 8 | 10 | 6.5 | 5 | 6.5 | 5.5 | 10 |
| M136 AT | blast | 655 | 0 | 0 | 0 | 0.3 | 8.5 | 0.3 | 0.15 | 0 |
| MBT-LAW | direct | 651 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| MBT-LAW | blast | 650 | 3 | 6.5 | 10 | 7 | 7 | 3 | 3.5 | 10 |
| SLM-93A | direct | 184 | 0 | 6.5 | 6.5 | 4.5 | 11 | 4.5 | 1 | 6.5 |
| SLM-93A | blast | 185 | 2 | 0 | 0 | 2 | 8.5 | 2 | 1 | 0 |
| C-4 | blast | 95 | 3.5 | 3.5 | 15 | 4.5 | 8.5 | 4.5 | 3.34 | 15 |
| M15 AV Mine | blast | 96 | 2 | 11 | 11 | 2 | 2 | 2 | 1 | 11 |

Against the light materials, blast damage counts much more than against armour: the RPG's explosion (material 164) reads 0 against 119 but 8.5 against 187 and 0.3 against 122.

Limits: the material shows which grid column a vehicle uses. It does not show that the 0.75 to 2 hit-quality steps, which EA describes for tanks, apply to the other vehicles on material 119. No value could be read for target 313 (CB90).

Still open, with the test that would settle each:

- IFV and armoured car. One M15 mine under a Bradley and one under a JLTV: 390 on both would confirm the shared material.
- Hit-quality steps on an IFV. One RPG on a Bradley's rear: 500 if the steps apply as on a tank.
- Light vehicles. One RPG on a Vector (122): 708.5 by the rule (125 x 5.5 + 70 x 0.3). One on a quad bike (187): 1220, a kill.
- CB90. One RPG hit on a full-health CB90, to give a first value for target 313.

## L3330 - Hits to destroy each vehicle, by the damage rule and stored health (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3330-vehicle-hits-to-kill.json). Dataset: `reference-data/frosty/vehicle-hits-to-kill.json` (928 rows: 32 weapons against 29 vehicles). This is a research dataset, not site data. Every number is the rule of L3323 and L3327 applied to stored values; none is a measured result.

How each number is formed:

- Damage per hit is stored direct damage times the grid value, plus stored blast damage times the blast material's grid value, at close range with the full blast.
- Health is the stored root value (`Class_f2a56983.Field_9040392c`), shown in the column heads. Effective health is not established. The Abrams and Leopard store 1200, while EA's and creators' figures treat a tank as 1000; the dataset gives both counts for those two.
- For vehicles on target material 119 the four counts are turret (75%) / body (100%) / side (150%) / rear (200%). One count means the angle makes no difference. That these steps apply to the Bradley and JLTV as they do to tanks is an assumption (L3328).
- Mobile anti-air rounds against aircraft are doubled to agree with EA's figures (L3322).
- Not included: repair, active protection, upgrades, range falloff, partial blast.

Selected rows:

| Weapon | Abrams (1200) | Bradley (1000) | JLTV (800) | Vector (1000) | PTV (1000) | AH-64E (1000) | AH-6M (700) | UH-60 (1500) | F-16 (1000) |
|---|---|---|---|---|---|---|---|---|---|
| RPG-7V2 | 7 / 5 / 4 / 3 | 6 / 4 / 3 / 2 | 5 / 4 / 3 / 2 | 2 | 1 | 1 | 1 | 2 | 1 |
| M136 AT | 6 / 5 / 3 / 3 | 5 / 4 / 3 / 2 | 4 / 3 / 2 / 2 | 2 | 1 | 1 | 1 | 2 | 1 |
| MBT-LAW | 5 | 5 | 4 | 2 | 2 | 2 | 2 | 3 | 2 |
| MAS 148 Glaive | 3 | 3 | 2 | 1 | 1 | 1 | 1 | 2 | 1 |
| SLM-93A | 6 | 5 | 4 | 2 | 1 | 2 | 2 | 3 | 2 |
| C-4 | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 5 | 1 |
| M15 AV Mine | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| PTKM-1R | 3 | 3 | 2 | 1 | 1 | 1 | 1 | 2 | 1 |
| MBT 120mm APFSDS Rounds | 5 / 4 / 3 / 2 | 5 / 4 / 3 / 2 | 4 / 3 / 2 / 2 | 2 | 2 | 2 | 2 | 3 | 2 |
| 120mm HEAT-MP-T Rounds | 6 / 5 / 3 / 3 | 5 / 4 / 3 / 2 | 4 / 3 / 2 / 2 | 1 | 1 | 1 | 1 | 2 | 1 |
| 120mm HEMP-T Rounds | 7 / 5 / 4 / 3 | 6 / 5 / 3 / 3 | 5 / 4 / 3 / 2 | 2 | 1 | 1 | 1 | 2 | 1 |
| IFV Aim-Guided Missile | 6 / 5 / 3 / 3 | 5 / 4 / 3 / 2 | 4 / 3 / 2 / 2 | 1 | 1 | 1 | 1 | 2 | 1 |
| IFV Lock-Guided Missile | 3 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 |
| IFV AP shells | 54 / 40 / 27 / 20 | 45 / 34 / 23 / 17 | 36 / 27 / 18 / 14 | 8 | 4 | 10 | 7 | 15 | 10 |
| Air-to-Ground Missiles | 3 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | 1 |
| Attack Helicopter Heavy Rocket | 10 / 8 / 5 / 4 | 9 / 7 / 5 / 4 | 7 / 5 / 4 / 3 | 2 | 2 | 3 | 2 | 5 | 2 |
| Mobile AA High Velocity | 352 / 264 / 176 / 132 | 294 / 220 / 147 / 110 | 235 / 176 / 118 / 88 | 62 | 30 | 20 | 14 | 29 | 16 |

Checks against what is known: EA's and the creator figures for the RPG against a tank (188, 375, 500) are the turret, side and rear damage behind the first row, and the user-reported rear reading of L3326 is 500.

Still open, with the test that would settle each:

- Tank health. Count RPG rear hits (500 each) needed to destroy a full-health Abrams with no repair: 2 means 1000, 3 means 1200.
- Light vehicles. One RPG on a full-health PTV should destroy it (1220); two on a Vector.
- Helicopters. One M136 AT hit on an AH-64E should destroy it (1000 against 1000); one on a UH-60 should leave 500.
- IFV steps. Count M136 AT rear hits on a Bradley: 2 if the 200% step applies.

## L3331 - Which jet carries which bomb (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3331-jet-bomb-identity.json). This settles the crossed bomb names of L3327 as far as stored data can. The links below are stored imports resolved by file GUID, not name matches.

| Jet (file) | Class in the vehicle list | Weapon file imported | Projectile file it imports |
|---|---|---|---|
| F-61V (`VB_VEH_Airplane_F16`) | arch_jetattack | `WF_Vehicles_Airplane_Bomb_Mk82AIR` | `PB_Bomb_Mk82AIR` |
| F-39E (`VB_VEH_Airplane_JAS39`) | arch_jetattack | `WF_Vehicles_Airplane_Bomb_Mk82AIR` | `PB_Bomb_Mk82AIR` |
| F-97 Kestrel (`VB_VEH_Airplane_F22`) | arch_fighterplane | `WF_Vehicles_Airplane_Bomb_GBU39` | `PB_Bomb_GBU39` |
| Su-57 (`VB_VEH_Airplane_SU57`) | arch_fighterplane | `WF_Vehicles_Airplane_Bomb_GBU39` | `PB_Bomb_GBU39` |

So the file names are the right way round: attack jets carry the Mk82 file and fighter jets the GBU-39 file. By the damage rule the figures are:

| Bomb file | Carried by | Tanks | Helicopters | EA 1.3.1.0 lists these figures under |
|---|---|---|---|---|
| `PB_Bomb_Mk82AIR` | attack jets | 410 to 535 | 1455 | Fighter Jet GBU-39/B |
| `PB_Bomb_GBU39` | fighter jets | 300 to 400 | 1080 | Attack Jet Mk82 |

EA's two lines are crossed relative to stored data, or the two bombs' values were exchanged after that update; stored data cannot tell which. On today's values the attack jet's bomb is the stronger one. 12 raw-offset checks matched.

Still open, with the test that would settle each:

- Drop one bomb from the attack jet on a full-health tank's body: about 435 confirms the stored link and values.
- The same from the fighter jet: about 320.

## L3334 - EA states tank health 1200 and armoured transport health 800 (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3334-armoured-vehicle-health-official.json). EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) say: "Weapons no longer deal different damage values to IFV, MBT, APT & AA Vehicles. Instead, MBT health has been increased to 1200 and APT health has been reduced to 800."

| Group | Vehicle file | Stored root health | EA 1.3.1.0 | Target material |
|---|---|---|---|---|
| Main battle tanks | `VB_VEH_Tank_Abrams` | 1200 | 1200 | 119 |
| Main battle tanks | `VB_VEH_Tank_Leopard` | 1200 | 1200 | 119 |
| Armoured transports (EA: APT) | `VB_VEH_Car_JLTV` | 800 | 800 | 119 |
| Armoured transports (EA: APT) | `VB_VEH_Car_Marauder` | 800 | 800 | 119 |
| Infantry fighting vehicles | `VB_VEH_Tank_Bradley` | 1000 | not stated | 119 |
| Infantry fighting vehicles | `VB_VEH_Tank_CV90` | 1000 | not stated | 119 |
| Anti-air | `VB_VEH_Tank_Gepard` | 1000 | not stated | 119 |

This settles two open items from stored data plus an official statement:

- **Health (L3330).** The stored root health is the health in use; tanks have 1200, not the 1000 that EA's damage ranges seemed to imply. In the hits-to-kill dataset the counts for stored health are the ones to read; the `hitsIfHealth1000` figures for the two tanks no longer apply.
- **Shared damage (L3328).** The vehicles EA names all store target material 119, so one hit deals the same damage to each and removes a larger share of an IFV (1000) or an armoured transport (800) than of a tank (1200).

IFV and anti-air health (1000) is stored but not stated by EA. 65 raw-offset checks matched.

Still open, with the test that would settle each:

- Angle steps on other vehicles. One RPG on a Bradley's rear: 500 if the 200% step applies as on a tank.
- IFV health. Two M136 AT rear hits on a full-health Bradley (2 x 550) should destroy it.
- Current build. Three RPG rear hits should destroy a full-health tank; two should not.

## L3335 - EA's reload, rate of fire, magazine and speed figures against registry rows (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3335-official-non-damage-figures.json). Dataset: `reference-data/frosty/official-non-damage-figures.json`. EA's [1.3.1.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) and [1.3.3.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-3-0) notes state many numbers that are not damage. Each was compared with one registry row chosen by exact owner and property; item names are joined to owners by name only. A Haiku worker proposed the candidates; every row below was re-selected and re-read here.

Equal (22 rows):

| EA statement | Registry row | Registry default | EA number |
|---|---|---|---|
| IFV cannon reload time 2.4 to 2.75 s | `WF_Vehicles_IFV_PrimaryWeapon_HEAB.PrimaryFire.FireLogic.ReloadInfoArray[0].ReloadTime` | 2.75 | 2.75 |
| IFV cannon reload time 2.4 to 2.75 s | `WF_Vehicles_IFV_PrimaryWeapon_APFSDST.PrimaryFire.FireLogic.ReloadInfoArray[0].ReloadTime` | 2.75 | 2.75 |
| IFV cannon reload time 2.4 to 2.75 s | `WF_Vehicles_IFV_PrimaryWeapon_Canister.PrimaryFire.FireLogic.ReloadInfoArray[0].ReloadTime` | 2.75 | 2.75 |
| IFV HE rounds rate of fire 200 to 180 RPM | `WF_Vehicles_IFV_PrimaryWeapon_HEAB.PrimaryFire.FireLogic.RateOfFire` | 180 | 180 |
| APDS rounds magazine capacity 12 to 10 | `WF_Vehicles_IFV_PrimaryWeapon_APFSDST.PrimaryFire.Ammo.MagazineCapacity` | 10 | 10 |
| IFV AP shells rate of fire 120 to 160 RPM | `WF_Vehicles_IFV_PrimaryWeapon_APFSDST.PrimaryFire.FireLogic.RateOfFire` | 160 | 160 |
| IFV AP shell initial velocity 375 to 445 m/s | `WF_Vehicles_IFV_PrimaryWeapon_APFSDST.PrimaryFire.Shot.InitialSpeed.z` | 445 | 445 |
| IFV canister rounds magazine capacity 12 to 16 | `WF_Vehicles_IFV_PrimaryWeapon_Canister.PrimaryFire.Ammo.MagazineCapacity` | 16 | 16 |
| IFV canister rounds rate of fire 200 to 240 RPM | `WF_Vehicles_IFV_PrimaryWeapon_Canister.PrimaryFire.FireLogic.RateOfFire` | 240 | 240 |
| RWS and coaxial LMG minimum damage 21 to 19 | `PD_Vehicles_RWS_LMG.BulletEntityData.EndDamage` | 19 | 19 |
| RWS and coaxial LMG falloff start 20 to 25 m | `PD_Vehicles_RWS_LMG.BulletEntityData.DamageFalloffStartDistance` | 25 | 25 |
| RWS and coaxial LMG falloff end 75 to 60 m | `PD_Vehicles_RWS_LMG.BulletEntityData.DamageFalloffEndDistance` | 60 | 60 |
| RWS and coaxial HMG minimum damage (75+ m) 30 to 24 | `PD_Vehicles_RWS_HMG.BulletEntityData.EndDamage` | 24 | 24 |
| RWS and coaxial HMG minimum damage at 75+ m | `PD_Vehicles_RWS_HMG.BulletEntityData.DamageFalloffEndDistance` | 75 | 75 |
| Automatic grenade launcher RWS reload 3 to 2 s | `WF_Vehicles_RWS_AGL.PrimaryFire.FireLogic.ReloadInfoArray[0].ReloadTime` | 2 | 2 |
| Attack helicopter TOW2 maximum speed 90 to 120 m/s | `PB_Missile_TOW2B_AirVehicle.MissileEntityData.MaxSpeed` | 120 | 120 |
| Ground vehicle TOW missiles remain at 90 m/s | `PB_Missile_TOW2B.MissileEntityData.MaxSpeed` | 90 | 90 |
| MBT-LAW initial missile speed 30 to 100 m/s | `MBTLAW_Weapon Blueprint.WeaponEntityData.WeaponFiring.PrimaryFire.Shot.InitialSpeed.z` | 100 | 100 |
| MAS 148 Glaive maximum missile speed 60 to 70 m/s | `PB_Javelin.MissileEntityData.MaxSpeed` | 70 | 70 |
| High Velocity anti-air heat per bullet 4.2% to 3.6% | `WF_Vehicles_AA_PrimaryWeapon_AAHV.PrimaryFire.OverHeat.HeatPerBullet` | 0.036 (x 100 = 3.6) (2.1.1.0: 0.13) | 3.6 |
| Armoured vehicle regeneration delay 6 to 12 s (only the CB90 has a row) | `VB_VEH_Boat_CB90.RegenerationDelay` | 12 | 12 |
| Regeneration rate about 5% to 10% per second (CB90 row, health 1000) | `VB_VEH_Boat_CB90.RegenerationRate` | 100 (x 0.1 = 10) | 10 |

Not equal:

| EA statement | Registry row | Registry default | EA number |
|---|---|---|---|
| RWS and coaxial LMG muzzle velocity 850 to 670 m/s | `WF_Vehicles_RWS_LMG.PrimaryFire.Shot.InitialSpeed.z` | 737 | 670 |
| RWS and coaxial LMG muzzle velocity 850 to 670 m/s | `WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG.PrimaryFire.Shot.InitialSpeed.z` | 737 | 670 |
| RWS and coaxial HMG muzzle velocity 890 to 760 m/s | `WF_Vehicles_RWS_HMG.PrimaryFire.Shot.InitialSpeed.z` | 890 | 760 |
| RWS and coaxial HMG muzzle velocity 890 to 760 m/s | `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG.PrimaryFire.Shot.InitialSpeed.z` | 890 | 760 |

What this gives: the units of these rows (seconds, rounds per minute, metres per second, heat as a fraction of 1), and that `EndDamage` is the minimum damage reached at `DamageFalloffEndDistance`. The machine gun velocity rows hold EA's older value (890) or a different one (737); the cause is not decided. 26 raw-offset checks matched.

Still open, with the test that would settle each:

- Machine gun velocity. Fire the coaxial HMG at a wall 380 m away and time the flight: 0.5 s means 760 m/s, 0.43 s means 890 m/s.
- Current values. Count IFV HE shots in 10 s of held fire (30 at 180 RPM) and time one cannon reload (2.75 s).

## L3336 - Dead end: CB90 damage and the low HEI-T figure (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3336-cb90-cell-and-heit-low-dead-end.json). Two open items of L3327 and L3328 that stored data cannot settle.

- **CB90 (target material 313).** All 785 target columns of the material grid were read for source materials 125 and 96. Column 313 is empty for both, as is every material from 312 to 325 (339 of 785 columns are empty for source 125). The control cell, 125 against 119, reads 2.0. The grid stores no fallback for an empty cell.
- **HEI-T low figure.** EA gives 10 to 30 against tanks. The registry holds `StartDamage` 50 and `EndDamage` 40 (falloff from 70 m to 120 m) and the grid value is 0.3. Full damage gives 12 on the turret and 30 on the rear; minimum damage gives 9 and 24. Neither gives 10.

8685 raw-offset checks matched.

Tests that would settle them:

- One RPG on a full-health CB90; read the health removed.
- One HEI-T round on a tank turret within 70 m; 12 by the rule, 10 by EA's notes.

## L3337 - MinimumBlastDamage is EA's minimum explosive damage of 20% (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3337-minimum-blast-damage-share.json). Dataset: `reference-data/frosty/minimum-blast-damage.json`. EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0): "Most land vehicle explosive weapons now have a minimum explosive damage of 20%. This does not increase lethal or total radius, but increases damage at the edges of explosive radius." The vehicle registry has a `MinimumBlastDamage` row beside `BlastDamage`. Owners with a value above zero:

| Registry owner | BlastDamage | MinimumBlastDamage | Share | Inner radius | Blast radius |
|---|---|---|---|---|---|
| `PB_Missile_TOW2B` | 100 | 20 | 20% | 1.75 (2.1.1.0: 2.0) | 4 |
| `PB_Missile_TOW2B_AirVehicle` | 100 | 20 | 20% | 1.75 | 4 |
| `PB_NS_Missile_AA_Secondary_AimGuided` | 75 | 20 | 26.7% | 1.75 | 3 |
| `PB_NS_Missile_AA_Secondary_HighVelocity` | 75 | 20 | 26.7% | 1.75 | 3 |
| `PB_Vehicle_AGL_Grenade` | 70 | 20 | 28.6% | 1 | 4 |
| `PD_Vehicles_IFV_PrimaryWeapon_HEAB` | 50 | 15 | 30% | 1 | 4.25 |
| `PD_Vehicles_IFV_SecondaryWeapon_LightRockets` | 100 | 20 | 20% | 1 | 4 |
| `PD_Vehicles_MBT_AmmoTypes_HE` | 100 | 20 (2.1.1.0: 17.13) | 20% | 2.25 (2.1.1.0: 2.3) | 5 (2.1.1.0: 6) |
| `PD_Vehicles_MBT_AmmoTypes_MPAT` | 100 | 20 | 20% | 1 | 5 |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_LR30` | 30 | 30 | 100% | 1.75 | 1.76 |

Five owners store exactly one fifth. Owners that store 0: `PBNS_Missile_AIM54`, `PBNS_Missile_AIM54_Pitbull`, `PBNS_Missile_AIM7`, `PB_120mmMortar_Airburst`, `PB_120mmMortar_Airburst`, `PB_120mmMortar_Guided`, `PB_120mmMortar_HE`, `PB_Bomb_BunkerBuster`, `PB_Bomb_BunkerBuster_Passthrough`, `PB_Bomblet_Rockeye`, `PB_Missile_AGM84`, `PB_Missile_AGM88`, `PB_Missile_MBT_GuidedMunition`, `PB_Missile_RBS70`, `PB_Missile_RBS70_TerminalHoming`, `PB_Missile_Torped47`, `PB_NavalMine`, `VB_VEH_Boat_CB90`, `Vulcan_CombatMix_HE_Ammo`, `WF_Vehicles_PatrolBoat_PrimaryWeapon_M230LF - ProjectileData`.

So for the weapons in the table the blast falls from `BlastDamage` inside the inner radius to `MinimumBlastDamage` at the blast radius, not to zero. The shape of the fall between the radii is not in these rows.

Radii against EA's notes (shell names joined by name only):

| EA statement | Row | Stored | EA |
|---|---|---|---|
| HEMP-T inner blast radius 2 to 2.25 m (1.3.1.0) | `PD_Vehicles_MBT_AmmoTypes_HE` InnerBlastRadius | 2.25 (2.1.1.0: 2.3) | 2.25 |
| HEAT-MP-T total blast radius 4 to 5 m ([1.3.3.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-3-0)) | `PD_Vehicles_MBT_AmmoTypes_MPAT` BlastRadius | 5 | 5 |
| HEAT-MP-T lethal radius 1 to 1.25 m (1.3.3.0) | `PD_Vehicles_MBT_AmmoTypes_MPAT` InnerBlastRadius | 1 | 1.25 |

120 raw-offset checks matched.

Still open, with the test that would settle each:

- HEAT-MP-T lethal radius. A shell landing 1.2 m from a full-health soldier: a kill means 1.25.
- Edge damage. A HEMP-T shell landing 4.9 m from a full-health soldier without flak: 20 damage means the minimum applies at the edge.
- Whether the minimum is scaled by the target material value: not tested.

## L3338 - Vehicle machine guns against soldiers and vehicles (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3338-vehicle-machine-gun-damage.json). Dataset: `reference-data/frosty/vehicle-machine-gun-damage.json`. Registry and own damage are equal for all seven bullet files. Soldier figures assume 100 health and no armour.

| Weapon | Bullet file | Close damage | Far damage | Falloff (m) | Head | Body shots to kill (close / far) |
|---|---|---|---|---|---|---|
| Tank coaxial HMG | `PD_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | 50 | 30 | 25 to 75 | x1.34 | 2 / 4 |
| Tank coaxial LMG | `PD_Vehicles_MBT_SecondaryWeapon_CoaxLMG` | 35 | 21 | 20 to 75 | x1.34 | 3 / 5 |
| Remote weapon station HMG | `PD_Vehicles_RWS_HMG` | 50 | 24 | 25 to 75 | x1.34 | 2 / 5 |
| Remote weapon station LMG | `PD_Vehicles_RWS_LMG` | 36 | 19 | 25 to 60 | x1.34 | 3 / 6 |
| Scout helicopter minigun | `WF_Vehicles_ScoutHeli_PrimaryWeapon_Minigun` | 34 | 18 | 40 to 120 | x1.34 | 3 / 6 |
| Transport helicopter minigun | `WF_Vehicles_TransportHeli_Gunner_Minigun` | 34 | 20 | 200 to 500 | x1.34 | 3 / 5 |
| Scout helicopter GAU-19 | `WF_Vehicles_ScoutHeli_PrimaryWeapon_GAU19` | 50 | 24 | 45 to 135 | x1.34 | 2 / 5 |

Grid value by target material (damage is stored damage times this):

| Weapon | Material | Tanks, IFVs (119) | Helicopters (121) | Jets (120) | Flyer, Vector, RHIB (122) | Quad, bikes (187) |
|---|---|---|---|---|---|---|
| Tank coaxial HMG | 289 | 0 | 0.6 | 0.8 | 0.5 | 1.5 |
| Tank coaxial LMG | 288 | 0 | 0.8 | 0.7 | 0.25 | 1.2 |
| Remote weapon station HMG | 289 | 0 | 0.6 | 0.8 | 0.5 | 1.5 |
| Remote weapon station LMG | 288 | 0 | 0.8 | 0.7 | 0.25 | 1.2 |
| Scout helicopter minigun | 621 | 0 | 0.4 | 0.7 | 0.25 | 1.2 |
| Transport helicopter minigun | 621 | 0 | 0.4 | 0.7 | 0.25 | 1.2 |
| Scout helicopter GAU-19 | 289 | 0 | 0.6 | 0.8 | 0.5 | 1.5 |

- None of these guns damages tanks, IFVs, armoured transports or the anti-air vehicle (grid value 0).
- Head hits multiply by 1.34; abdomen and limbs by 1.
- **Coaxial files differ from the remote weapon station files.** `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` and `CoaxLMG` import their own bullet files, which hold minimum damage 30 and 21 and LMG falloff 20 to 75 m. EA's 1.3.1.0 notes changed "RWS & Coaxial" guns to 24 and 19 (LMG falloff 25 to 60 m); only the `PD_Vehicles_RWS_*` files hold those (L3335). The RWS weapon files are imported by both tanks, both IFVs, the JLTV and the Marauder.

5633 raw-offset checks matched.

Still open, with the test that would settle each:

- Coaxial minimum damage. Coaxial LMG body shots on a full-health soldier beyond 75 m: 5 to kill means 21, 6 means 19.
- Headshot value. One close coaxial HMG headshot on a full-health soldier should deal 67.

## L3339 - Aim-Guided Shell and MAS 148 Glaive under the damage rule (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3339-guided-shell-and-glaive-rule.json). Two items EA gives figures for ([1.3.1.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0), [1.3.3.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-3-0)) that had not been run through the rule of L3323. Files: `PB_Missile_MBT_GuidedMunition` (direct material 431: 2.5 / 4 / 5; blast material 130: 0 / 1 / 2) and `PB_Javelin` (direct material 651: 0 / 0 / 0; blast material 650: 3 / 6.5 / 10). Names are joined by name only.

| Item | Values used | Rule: tanks / helicopters / jets | EA | Notes |
|---|---|---|---|---|
| MBT Aim-Guided Shell | own Damage 125, BlastDamage 200 | 235 to 625 / 700 / 1000 | 235 to 625 / 700 / 1000 | 1.3.1.0 |
| MBT Aim-Guided Shell | registry Damage 130, BlastDamage 200 | 244 to 650 / 720 / 1000 | 244 to 650 / 720 / not stated | 1.3.3.0 |
| MAS 148 Glaive | registry Damage 140 (grid value 0), BlastDamage 155 | 465 / 1007.5 / 1000 | 465 / 1007.5 / 1000 | 1.3.1.0 |
| MAS 148 Glaive | own Damage 150 (grid value 0), BlastDamage 125 | 375 / 812.5 / 1000 | not stated | not EA: own values |

- **The shell shows registry over own again.** Own Damage 125 reproduces the older update, registry 130 the newer one. The registry default is current.
- **The Glaive damages vehicles by blast only.** Its direct material has grid value 0, so there is no angle step: 155 x 3 = 465 on any part of a tank. With tank health 1200 (L3334) that is three hits.
- EA prints 1007.5 against helicopters, so only its jet figures are capped at 1000.

834 raw-offset checks matched.

Tests that would confirm the current build:

- One Glaive hit on a full-health tank: 465 removed; the third hit destroys it.
- Two Aim-Guided Shell rear hits destroy a full-health tank (2 x 650).

## L3341 - Where the 75 / 100 / 150 / 200% hit steps are stored (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3341-simplified-tank-angle-steps.json). Dataset: `reference-data/frosty/simplified-tank-angle-steps.json`. The rule of L3323 took its four factors from EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0). They are stored. Six curve files named `AngleDamageCurve_SimplifiedTank_*` hold them, and one schematic, `PF_Vehicle_GameplayDamageZones_Tank`, assigns a curve to each face of a body zone and three turret zones (all target material 119).

| Curve file | Points (angle in degrees, multiplier) | Used for |
|---|---|---|
| `AngleDamageCurve_SimplifiedTank_Turret` | (90, 0.75) | turret zones: four side faces and the bottom |
| `AngleDamageCurve_SimplifiedTank_Top` | (90, 1) (2.1.1.0: first angle 50) | top face of body and turret |
| `AngleDamageCurve_SimplifiedTank_Front` | no curve object (null) | body front face |
| `AngleDamageCurve_SimplifiedTank_Sides` | (70, 1) (70.001, 1.5) (109.999, 1.5) (110, 1) | body left and right faces |
| `AngleDamageCurve_SimplifiedTank_Rear` | (55, 1) (55.001, 2) (124.999, 2) (125, 1) | body rear face |
| `AngleDamageCurve_SimplifiedTank_Bottom` | (90, 2) | body bottom face |

- **Side and rear are gated by angle.** Rear gives 2.0 only between 55 and 125 degrees and sides 1.5 only between 70 and 110 degrees; outside the window the factor is 1.0. Reading 90 as square-on, that is up to 35 degrees off square at the rear and 20 at the side.
- **Check against known numbers.** RPG direct product 250 x 0.75 / 1.5 / 2 = 188 / 375 / 500: EA's range ends and the 375 side reading recorded earlier on this page.
- **Which vehicles.** A byte search of all 31,503 saved files finds the schematic's file GUID in the damage-zone files of the Abrams, Leopard, Bradley, CV90 and Gepard. So the same steps are selected for both tanks, both IFVs and the anti-air vehicle (the open item of L3334).
- **Armoured transports have no step.** The JLTV and Marauder import `AngleDamageCurve_ArmoredTransport_Shared`, one point (90, 1.0).
- The older `Tank_*_Shared` and `IFV_*_Shared` curves (1.0 to 3.2, L3201) are still imported by the Abrams and CV90 files but do not reproduce EA's figures.
- The body zone carries two face lists; the second names the front file for every face. What chooses between them is not decoded.

86 raw-offset checks matched.

Still open, with the test that would settle each:

- Face sets. An RPG square on a tank's side: 375 if the first list applies, 250 if the second.
- Angle window. An RPG on a tank's rear about 45 degrees off square: 250, not 500.
- IFVs. One RPG square on a Bradley's rear: 500 of 1000.

## L3344 - Helicopter rocket radii, Aim-Guided Shell timers and smoke cooldown against registry rows (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3344-rocket-radius-guided-shell-smoke-rows.json). Seven more statements from EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0), each compared with one registry row chosen by exact owner and property. Names are joined to owners by name only (Light Rocket = Hydra70, Smart Rocket = APKWS-II, Heavy Rocket = Zuni).

| EA statement | Registry row | Registry default | EA number | Equal |
|---|---|---|---|---|
| Helicopter Light Rocket area of effect 5 to 4.75 m | `PRJ_Missile_Hydra70 ... ExplosionEntityData.BlastRadius` | 4.75 | 4.75 | yes |
| Helicopter Smart Rocket area of effect 5 to 4.75 m | `PRJ_Missile_APKWS-II ... ExplosionEntityData.BlastRadius` | 4.75 | 4.75 | yes |
| Helicopter Heavy Rocket area of effect 5.5 to 5.25 m | `PRJ_Missile_Zuni ... ExplosionEntityData.BlastRadius` | 5.25 | 5.25 | yes |
| Aim-Guided Shell time to live 6 to 4 s | `PB_Missile_MBT_GuidedMunition ... ProjectileEntityData.TimeToLive` | 4 | 4 | yes |
| Aim-Guided Shell engine time to live 1.25 to 1 s | `PB_Missile_MBT_GuidedMunition.MissileEntityData.EngineTimeToLive` | 1 | 1 | yes |
| Aim-Guided Shell turning rate 12.5 to 6 degrees per second | `PB_Missile_MBT_GuidedMunition.MissileEntityData.MaxTurnAngle` | 7.5 | 6 | no |
| Smoke Screen cooldown 20 to 16 s | `Ability_Vehicle_SmokeScreen.RechargeTime` | 16 | 16 | yes |

- EA's rocket "area of effect" is the explosion's `BlastRadius`.
- The shell's `MaxTurnAngle` is 7.5; EA's turning rate is 6 (12.5 before). Not resolved.
- The smoke screen's `ActiveTime` row holds 8.1.

10 raw-offset checks matched.

## L3345 - Per-part multipliers in the damage-zone files are flat (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3345-damage-zone-multipliers-flat.json). After L3341 found the tank steps in a shared schematic, the 38 saved `*_DamageZones` files were checked for per-part multipliers of their own. Each zone object (`Class_6f785351`) has five multiplier-like fields; their meaning is not decoded.

| Field | Values across all zone objects |
|---|---|
| `Field_52bf99dc` | 1 (212) |
| `Field_4ee6e3a6` | 1 (210), 3 (1), 2 (1) |
| `Field_8c2ac57f` | 1 (212) |
| `Field_25714eef` | 1 (212) |
| `Field_c73fcda4` | 1 (212) |
| `Field_64b3e9cd` | 0.7 (141), 1 (36), 0 (31), 0.75 (2), 0.8 (2) |

- Every helicopter and jet zone holds 1.0 in the five fields: no stored weak-spot multiplier for rotor, cockpit or engine. EA gives one figure per weapon against helicopters and one against jets.
- The MQ-9 is the one exception (3.0 and 2.0 on two zones).
- `Field_64b3e9cd` varies and is still unnamed.

1272 raw-offset checks matched.

Test that would check this: the same RPG hit on a helicopter's body and on its tail should remove the same health.

## L3346 - Vehicle health regeneration: delay and rate (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3346-vehicle-regeneration-values.json). Dataset: `reference-data/frosty/vehicle-regeneration.json`. EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0): regeneration delay 6 to 12 seconds, rate about 5% to 10% per second. Both are stored on the vehicle root object (`Class_f2a56983`, beside root health): `Field_5c9d2d82` is the delay and `Field_3233bcbf` the rate in health per second. The CB90's registry rows `RegenerationDelay` 12 and `RegenerationRate` 100 hold the same numbers as its two fields, which names them.

Multiplayer vehicle files (single-player variants are in the receipt):

| Vehicle file | Root health | Delay (s) | Rate (health/s) | Share of health per second | Seconds from 0 to full once started |
|---|---|---|---|---|---|
| `VB_VEH_Airplane_F16` | 1000 | 17.5 | 100 | 10% | 10 |
| `VB_VEH_Airplane_F22` | 1000 | 17.5 | 100 | 10% | 10 |
| `VB_VEH_Airplane_JAS39` | 1000 | 17.5 | 100 | 10% | 10 |
| `VB_VEH_Airplane_MQ9` | 1000 | 40 | 0 | 0% | no regeneration |
| `VB_VEH_Airplane_SU57` | 1000 | 17.5 | 100 | 10% | 10 |
| `VB_VEH_Boat_CB90` | 1000 | 12 | 100 | 10% | 10 |
| `VB_VEH_Boat_RHIB` | 1000 | 12 | 100 | 10% | 10 |
| `VB_VEH_Car_Flyer60` | 1000 | 12 | 100 | 10% | 10 |
| `VB_VEH_Car_JLTV` | 800 | 12 | 80 | 10% | 10 |
| `VB_VEH_Car_Marauder` | 800 | 12 | 80 | 10% | 10 |
| `VB_VEH_Car_PTV` | 1000 | 12 | 100 | 10% | 10 |
| `VB_VEH_Car_QuadBike` | 1000 | 12 | 100 | 10% | 10 |
| `VB_VEH_Car_TheBeast` | 1000 | 5 | 0 | 0% | no regeneration |
| `VB_VEH_Car_Vector` | 1000 | 12 | 100 | 10% | 10 |
| `VB_VEH_Helicopter_AH64E` | 1000 | 17.5 | 100 | 10% | 10 |
| `VB_VEH_Helicopter_AH6M` | 700 | 17.5 | 70 | 10% | 10 |
| `VB_VEH_Helicopter_Eurocopter` | 1000 | 17.5 | 100 | 10% | 10 |
| `VB_VEH_Helicopter_UH60` | 1500 | 17.5 | 150 | 10% | 10 |
| `VB_VEH_Motorcycle_DirtBike01` | 1000 | 10 | 100 | 10% | 10 |
| `VB_VEH_Motorcycle_DirtBike02` | 1000 | 10 | 100 | 10% | 10 |
| `VB_VEH_Stationary_GDF009` | 1000 | 10 | 50 | 5% | 20 |
| `VB_VEH_Stationary_M2MG` | 150 | 10 | 7.5 | 5% | 20 |
| `VB_VEH_Stationary_Phalanx` | 1000 | 5 | 50 | 5% | 20 |
| `VB_VEH_Stationary_Turret_CROWS` | 300 | 10 | 15 | 5% | 20 |
| `VB_VEH_Tank_AAV7A1` | 1000 | 6 | 50 | 5% | 20 |
| `VB_VEH_Tank_Abrams` | 1200 | 12 | 120 | 10% | 10 |
| `VB_VEH_Tank_Bradley` | 1000 | 12 | 100 | 10% | 10 |
| `VB_VEH_Tank_CV90` | 1000 | 12 | 100 | 10% | 10 |
| `VB_VEH_Tank_Gepard` | 1000 | 12 | 100 | 10% | 10 |
| `VB_VEH_Tank_Leopard` | 1200 | 12 | 120 | 10% | 10 |

- Tanks, IFVs, the Gepard, the JLTV and the Marauder: 12 s and exactly 10% of health per second, EA's new values.
- The AAV7A1 holds 6 s and 5%, EA's old values.
- Helicopters and jets: 17.5 s, 10%. EA's statement does not cover them.
- Registry rows `Passives_Vehicles_MBT_Regeneration_*` (9.5 s, 132) and `IFV` (9.5 s, 110) belong to the regeneration passive EA says was replaced in 1.3.1.0.
- EA's 80% slowdown at critical health was not found as a stored value.

117 raw-offset checks matched.

Still open, with the test that would settle each:

- Where regeneration stops: damage a tank to half and watch.
- Critical slowdown: time regeneration from 10% health (24 per second on a tank if slowed by 80%).
- Aircraft delay: time from last damage to first tick on a helicopter (17.5 s).

## L3347 - Vehicle disabled (critical health) thresholds (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3347-vehicle-disabled-thresholds.json). Dataset: `reference-data/frosty/vehicle-disabled-thresholds.json`. EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) slow regeneration by 80% "while in critical health". The CB90's registry rows `DisabledDamageThreshold` and `ClearDisabledDamageThreshold` are both 400, and its root object holds 400 in exactly two fields. Those two fields on every multiplayer vehicle root:

| Vehicle file | Root health | `Field_1a7c18f1` | `Field_6497ebc7` | As share of health |
|---|---|---|---|---|
| `VB_VEH_Airplane_F16` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Airplane_F22` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Airplane_JAS39` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Airplane_MQ9` | 1000 | 140 | 70 | 7% / 14% |
| `VB_VEH_Airplane_SU57` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Boat_CB90` | 1000 | 400 | 400 | 40% / 40% |
| `VB_VEH_Boat_RHIB` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Car_Flyer60` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Car_JLTV` | 800 | 200 | 300 | 25% / 37.5% |
| `VB_VEH_Car_Marauder` | 800 | 200 | 300 | 25% / 37.5% |
| `VB_VEH_Car_PTV` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Car_QuadBike` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Car_TheBeast` | 1000 | 0 | 50 | 0% / 5% |
| `VB_VEH_Car_Vector` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Helicopter_AH64E` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Helicopter_AH6M` | 700 | 300 | 300 | 42.86% / 42.86% |
| `VB_VEH_Helicopter_Eurocopter` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Helicopter_UH60` | 1500 | 250 | 500 | 16.67% / 33.33% |
| `VB_VEH_Motorcycle_DirtBike01` | 1000 | 300 | 300 | 30% / 30% |
| `VB_VEH_Motorcycle_DirtBike02` | 1000 | 300 | 300 | 30% / 30% |
| `VB_VEH_Stationary_GDF009` | 1000 | 0 | 50 | 0% / 5% |
| `VB_VEH_Stationary_M2MG` | 150 | 0 | 50 | 0% / 33.33% |
| `VB_VEH_Stationary_Phalanx` | 1000 | 0 | 50 | 0% / 5% |
| `VB_VEH_Stationary_Turret_CROWS` | 300 | 75 | 50 | 16.67% / 25% |
| `VB_VEH_Tank_AAV7A1` | 1000 | 200 | 200 | 20% / 20% |
| `VB_VEH_Tank_Abrams` | 1200 | 200 | 400 | 16.67% / 33.33% |
| `VB_VEH_Tank_Bradley` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Tank_CV90` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Tank_Gepard` | 1000 | 200 | 300 | 20% / 30% |
| `VB_VEH_Tank_Leopard` | 1200 | 200 | 400 | 16.67% / 33.33% |

- Which field is which is not stored: both are 400 on the CB90. `Field_1a7c18f1` is the smaller or equal value on most vehicles but the larger on the MQ-9 and the CROWS turret, so the order cannot be read from the values.
- If a vehicle turns critical at the lower number and recovers at the higher, a tank turns critical below 200 of 1200 and recovers above 400. That reading is an inference.
- That the row name "disabled" is EA's "critical health" is a join by meaning.

114 raw-offset checks matched.

Test that would settle the order: damage a tank in steps and note the health at which the critical state starts (200 or 400) and, while it regenerates, where it ends.

## L3348 - Registry rows give one critical-health threshold per vehicle (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3348-vehicle-disabled-threshold-registry-rows.json). Dataset: `reference-data/frosty/vehicle-disabled-threshold-registry.json`. L3347 looked only at the CB90's registry rows. 23 vehicles have the same two rows, `DisabledDamageThreshold` and `ClearDisabledDamageThreshold`, and on every one they hold the same number, which is also the own `Field_6497ebc7`.

| Vehicle | Root health | Registry Disabled = ClearDisabled | Share of health | Own `Field_6497ebc7` | Own `Field_1a7c18f1` |
|---|---|---|---|---|---|
| `VB_VEH_Airplane_F16` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Airplane_F22` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Airplane_JAS39` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Airplane_SU57` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Boat_CB90` | 1000 | 400 | 40% | 400 | 400 |
| `VB_VEH_Boat_RHIB` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Car_Flyer60` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Car_JLTV` | 800 | 300 | 37.5% | 300 | 200 |
| `VB_VEH_Car_Marauder` | 800 | 300 | 37.5% | 300 | 200 |
| `VB_VEH_Car_PTV` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Car_QuadBike` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Car_Vector` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Helicopter_AH64E` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Helicopter_Eurocopter` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Helicopter_UH60` | 1500 | 500 | 33.33% | 500 | 250 |
| `VB_VEH_Motorcycle_DirtBike01` | 1000 | 300 | 30% | 300 | 300 |
| `VB_VEH_Motorcycle_DirtBike02` | 1000 | 300 | 30% | 300 | 300 |
| `VB_VEH_Tank_Abrams` | 1200 | 400 | 33.33% | 400 | 200 |
| `VB_VEH_Tank_Bradley` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Tank_CV90` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Tank_Gepard` | 1000 | 300 | 30% | 300 | 200 |
| `VB_VEH_Tank_Leopard` | 1200 | 400 | 33.33% | 400 | 200 |

- With registry defaults in use there is a single threshold: 400 for tanks (one third of 1200), 500 for the UH60, 300 for the others. **This replaces the reading offered in L3347** (critical below 200, recover above 400).
- The own `Field_1a7c18f1` is lower than the registry number on 19 vehicles: another own-versus-registry dispute.
- `RepairRateModifier` is 1.0 on every vehicle with a row.

135 raw-offset checks matched.

Test that would settle it: damage a tank in steps and note the health at which the critical warning and slowed regeneration start (400 by registry, 200 by the own field).

## L3349 - Vehicle passive rows in the registry (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3349-vehicle-passive-registry-rows.json). Dataset: `reference-data/frosty/vehicle-passive-rows.json`. The registry holds 66 rows for vehicle passives. Four statements in EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) can be compared (Antispotting is taken to be the Targeting Jammer, by name):

| EA statement | Registry row | Default | Reading |
|---|---|---|---|
| Targeting Jammers for the IFV & Mobile AA: locking resistance 30% to 40% | `IFV_Antispotting_LockOnTime.LockingTimeMultiplier` | 0.6 | 1 - 0.4 |
| Targeting Jammers for IFV & Mobile AA deactivation time 4.5 to 10 s (IFV) | `IFV_Antispotting_TimeToReactivate` | 10 | 10 |
| Targeting Jammers for IFV & Mobile AA deactivation time 4.5 to 10 s (anti-air) | `AA_Antispotting_TimeToReactivate` | 10 | 10 |
| Mine Sweeping highlights mines in a 30 m area | `Mine Sweep Radius` | 30 | 30 |

- Aircraft anti-radar passives hold a lock multiplier of 0.7 (30%), which EA did not change.
- How the multiplier is applied is not in the row. If it scales lock speed, a 1.4 s Glaive lock takes 2.33 s against a jammer.
- The Regeneration passive rows are still present although EA replaced the passive.

All numeric rows that are not 0, -1 or a multiplier of 1:

| Row (prefix `Passives_Vehicles_` or `Vehicles_Passives_` removed) | Default |
|---|---|
| `AA_Antispotting_SpotTimeMultiplier.SpotTimeMultiplier` | 0.75 |
| `AA_Antispotting_TimeToReactivate` | 10 |
| `AA_EnhancedLoading_Stance1.WeaponReloadSpeedModifier.ReloadSpeedMultiplier` | 1.5 |
| `AA_EnhancedLoading_Stance2.WeaponReloadSpeedModifier.ReloadSpeedMultiplier` | 1.25 |
| `AA_EquipmentUpgrade_AirRadarRadiusMultiplier.Value` | 1.5 |
| `AttackHeli_AntiRadar_AccelerationToMaintain` | 17 |
| `AttackHeli_AntiRadar_LockOnTime.LockingTimeMultiplier` | 0.7 |
| `AttackHeli_AntiRadar_SpottingDuration.SpotTimeMultiplier` | 0.75 |
| `AttackHeli_AntiRadar_VelocityToActivate` | 32 |
| `AttackHeli_AntiRadar_VelocityToMaintain` | 27.5 |
| `CaptureSpeed_Affector.Value` | 1.15 |
| `CombatAwareness_EffectRadius` | 20 |
| `CombatAwareness_SpottingDuration` | 5 |
| `FighterPlane_AntiRadar_LockOnTime.LockingTimeMultiplier` | 0.7 |
| `FighterPlane_AntiRadar_SpottingDuration.SpotTimeMultiplier` | 0.75 |
| `IFV_Antispotting_LockOnTime.LockingTimeMultiplier` | 0.6 |
| `IFV_Antispotting_SpotTimeMultiplier.SpotTimeMultiplier` | 0.75 |
| `IFV_Antispotting_TimeToReactivate` | 10 |
| `IFV_Durability_DamageRecievedMultiplier` | 0.85 |
| `IFV_EquipmentUpgrade_ProximityDetectionSystemRadiusMultiplier.Value` | 1.3 |
| `IFV_Regeneration_Rate` | 110 |
| `IFV_Regeneration_RegenDelay` | 9.5 |
| `MBT_Durability_DamageRecievedMultiplier` | 0.85 |
| `MBT_EnhancedLoading_Stance1.WeaponReloadSpeedModifier.ReloadSpeedMultiplier` | 1.35 |
| `MBT_EnhancedLoading_Stance2.WeaponOverheatModifier.HeatDropPerSecondMultiplier` | 1.3 |
| `MBT_EnhancedLoading_Stance2.WeaponOverheatModifier.OverheatedDropMultiplier` | 1.1 |
| `MBT_Regeneration_Rate` | 132 |
| `MBT_Regeneration_RegenDelay` | 9.5 |
| `Medbay_EffectInterval` | 0.9 |
| `Medbay_EffectRadius` | 12.5 |
| `Medbay_HealOverTime` | 20 |
| `Medbay_InitialHeal` | 5 |
| `Mine Sweep Radius` | 30 |
| `MobileTrophy_CooldownPerCharge` | 10 |
| `MobileTrophy_MaxCharges` | 3 |
| `MobileTrophy_NearbyFriendlySoldierRadius` | 13.5 |
| `ScoutHeli_AntiRadar_AccelerationToMaintain` | 10 |
| `ScoutHeli_AntiRadar_VelocityToActivate` | 27.5 |
| `ScoutHeli_AntiRadar_VelocityToMaintain` | 18.5 |
| `ScoutHeli_SateliteUplink_SpotDurationMultiplier` | 1.35 |
| `Shared_Durability_MassMultiplier.Value` | 1.04 |
| `Shared_EnhancedLoading_HealthThreshold` | 0.6 |
| `Shared_GunHandling_PitchMultiplier.Value` | 1.3 |
| `Shared_GunHandling_YawMultiplier.Value` | 1.3 |
| `Shared_Gunhandling_ImprovedSteeringRatio.Value` | 1.03 |

61 raw-offset checks matched.

Test: time a Glaive lock on an IFV with and without the Targeting Jammer (1.4 s against 2.33 s).

## L3351 - Vehicle registry rows not recorded before (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3351-vehicle-registry-global-rows.json). Dataset: `reference-data/frosty/vehicle-registry-global-rows.json`. `GRX_Vehicles` has 142 rows without an owner prefix; 62 of them were not named anywhere in the docs. All are in the dataset with default, minimum and maximum. These are registry defaults: the row name is the only description, units are implied by the name, and nothing here shows which mode reads a row.

Rows matching `Radius / Duration / Damage / Time / Speed / Health / Range / Multiplier / Delay` (31 of 62):

| Row | Default | Min | Max |
|---|---|---|---|
| `120mmILL_Radius` | 36 | 0 | 0 |
| `120mmILL_SpotDuration` | 7 | 0 | 0 |
| `APC_RetainOwnership_Radius` | 25 | 10 | 40 |
| `BoatRampSpeedCheckDeploy` | 9 | 0 | 0 |
| `BoatRampSpeedCheckUndeploy` | 12 | 0 | 0 |
| `BoatUnoccupiedCheckTimeInterval` | 2 | 1 | 5 |
| `HUD_RangeFinder_HelicopterRange` | 2000 | 0 | 2000 |
| `HUD_RangeFinder_TanksRange` | 1000 | 0 | 2000 |
| `HUD_RangeFinderAbsoluteMaximumRange` | 2000 | 0 | 2000 |
| `JetAimAssistMaxRange` | 500 | 0 | 1000 |
| `JetAimAssistMinRange` | 50 | 0 | 200 |
| `PhalanxAimEscalationTime` | 13 | 0.01 | 30 |
| `PhalanxAimRotationSpeed` | 270 | 30 | 720 |
| `PhalanxBurstDuration` | 3 | 0 | 5 |
| `TurretSpeedVisualMax` | 360 | 0 | 1800 |
| `TurretSpeedVisualMin` | 45 | 0 | 1800 |
| `TVmissileRollBlendTime` | 1.5 | 0.2 | 5 |
| `UnoccupiedBoatRadius` | 10 | 0 | 0 |
| `Vehicle_AirCombat_KeepAliveRadius` | 75 | 0 | 0 |
| `Vehicle_AirCombat_TimeUntilAbandonned` | 10 | 0 | 0 |
| `Vehicle_Combat_KeepAliveRadius` | 20 | 0 | 0 |
| `Vehicle_Combat_KeepAliveSpawnerRadius` | 110 | 0 | 0 |
| `Vehicle_Combat_TimeUntilAbandonned` | 5 | 0 | 0 |
| `Vehicle_Combat_TimeUntilAbandonned_TeamSpawners` | 120 | 0 | 0 |
| `Vehicle_Combat_TimeUntilAbandonnedIsDestroyed` | 15 | 0 | 0 |
| `Vehicle_InWorld_DefaultRespawnDelay` | 5 | 1 | 0 |
| `Vehicle_InWorld_Enemy_LocalSpottingRadius` | 10 | 0 | 0 |
| `Vehicle_InWorld_KeepAliveRadius` | 125 | 0 | 0 |
| `Vehicle_InWorld_KeepAliveSpawnerRadius` | 20 | 0 | 0 |
| `Vehicle_InWorld_TimeUntilAbandonned` | 5 | 0 | 0 |
| `Vehicle_InWorld_TimeUntilAbandonnedIsDestroyed` | 15 | 0 | 0 |

62 raw-offset checks matched.

## L3354 - Vehicle ability active and recharge times (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3354-vehicle-ability-times.json). Dataset: `reference-data/frosty/vehicle-ability-times.json`. Registry rows `Ability_*.ActiveTime` and `Ability_*.RechargeTime`. The own value is shown where the ability file is saved and differs. On the ability object (`Class_4918a771`), `Field_143f8e7a` is ActiveTime and `Field_bcfe8c70` is RechargeTime, named by the abilities where both sources agree.

| Ability | Active time (s) | Recharge time (s) |
|---|---|---|
| `Ability_APC_ExplosivesDetectionDetonationSystem` | 0.4 (own 0.1) | 20 |
| `Ability_APC_Passenger_SmokeLauncher` | 0.25 | 30 |
| `Ability_APC_ProximityDetectionSystem` | 12 | 20 |
| `Ability_AttackHeli_Countermeasure_Flares` | 1.8 | 15 |
| `Ability_AttackHeli_GroundTargetDetection` | 15 | 25 |
| `Ability_AttackPlane_Countermeasure_Flares` | 1.8 | 15 |
| `Ability_CV90_AdvancedThreatDetectionSystem` | 10 (own 20) | 15 (own 20) |
| `Ability_CV90_Passenger_SmokeLauncher` | 0.25 | 30 |
| `Ability_CV90_ProximityDetectionSystem` | 12 (own 20) | 20 |
| `Ability_Car_EmergencyDamageControl` | 0.4 | 24 (own 30) |
| `Ability_FighterPlane_Countermeasure_Flares` | 1.8 | 15 |
| `Ability_Helicopter_EmergencyDamageControl` | 0.4 | 24 (own 30) |
| `Ability_MBT_ActiveProtectionSystem` | 5 (own 4) | 32 |
| `Ability_MBT_ExplosivesDetectionDetonationSystem` | 0.4 | 20 |
| `Ability_MBT_SwitchAmmo` | 0 | 0.5 |
| `Ability_ScoutHeli_Countermeasure_Flares` | 1.8 | 15 |
| `Ability_UH60_Countermeasure_Flares` | 1.8 | 15 |
| `Ability_Vehicle_RWS_ActiveMissileWarningAndKillSystem` | 3.6 | 20 |
| `Ability_Vehicle_SmokeScreen` | 8.1 | 16 (own 20) |
| `Ability_Vehicle_ThermalSmoke` | 10 (own 7) | 16 (own 20) |

- Flares: 1.8 s active, 15 s recharge on every aircraft.
- Disputed pairs are marked "(own ...)"; the registry default is the likely value in use (L3327, L3339) but that is not verified for abilities.
- Thermal smoke damage to infantry (multiplayer rows): DamageInterval 0.5, DamageToDealPerSecond 12, InitialDamage 25.
- EA's smoke screen cooldown of 16 s is the `RechargeTime` row (L3344).

119 raw-offset checks matched.

Tests: time the tank's active protection window (5 s or 4 s) and the emergency repair cooldown (24 s or 30 s).

## L3355 - Registry over own holds for vehicle abilities (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3355-ability-registry-over-own-confirmed.json). L3354 left open which value applies when an ability's own time differs from its registry default. EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) state two of those changes:

| EA statement | Ability | Own value | Registry default |
|---|---|---|---|
| Smoke Screen cooldown 20 to 16 s | `Ability_Vehicle_SmokeScreen` RechargeTime | 20 | 16 |
| Thermal Smoke active duration increased by 3 s | `Ability_Vehicle_ThermalSmoke` ActiveTime | 7 | 10 |

The own value is the number before the change and the registry default the number after it, as with weapon damage (L3327, L3339) and missile speed (L3343). So thermal smoke lasts 10 s, and the other disputed abilities of L3354 most likely use their registry defaults too (tank active protection 5 s, emergency repair recharge 24 s); that extension is an inference. 6 raw-offset checks matched.

## L3357 - Vehicle cannons, canister rounds and the grenade launcher station (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3357-vehicle-cannon-damage.json). Dataset: `reference-data/frosty/vehicle-cannon-damage.json`. Damage per hit = registry damage (close range) x grid value; a blast, where the file has one, follows the plus sign. Own values are shown where they differ. Names are joined to files by name only and none has an EA figure.

| Weapon | File | Close / far damage | Blast | Soldier body | Tanks, IFVs (119) | Helicopters (121) | Jets (120) | Flyer, Vector, RHIB (122) | Quad, bikes (187) |
|---|---|---|---|---|---|---|---|---|---|
| Tank canister shell (per pellet) | `PD_Vehicles_MBT_AmmoTypes_Canister` | 50 / 30 | - | 50 | 0 | 30 | 40 | 25 | 75 |
| IFV canister round (per pellet) | `PD_Vehicles_IFV_PrimaryWeapon_Canister` | 15 / 5 | - | 15 | 0 | 13.5 | 25.5 | 7.5 | 15 |
| Grenade launcher station (AGL) | `PB_Vehicle_AGL_Grenade` | 32 / 32 | 70 | 32 + 70 | 9.6 | 64 + 210 | 96 + 189 | 40 + 105 | 83.2 + 175 |
| Attack helicopter gunner chaingun | `WF_Vehicles_AttackHeli_Passenger_PrimaryWeapon_Chaingun` | 22 (own 50) / 22 (own 50) | 30 | 22 + 30 | 22 | 88 | 110 | 27.5 + 30 | 57.2 + 30 |
| Jet cannon | `WF_Vehicles_Airplane_PrimaryWeapon_Cannon` | 34 / 34 | - | 51 | 10.2 | 36.04 | 73.1 | 42.5 | 88.4 |
| Stationary anti-air gun | `PD_Vehicles_Stationary_AntiAir` | 30 / 22 (2.1.1.0: 34 / 34) | - | 30 | 10.5 | 60 | 75 | 37.5 | 78 |
| Stationary 20 mm rotary cannon | `WF_Vehicles_SAA_PrimaryWeapon_20mmRotaryCannon` | 10 / 10 | - | 10 | 10 | 40 | 50 | 12.5 | 26 |

- Canister pellets do nothing to armour (grid value 0). Pellets per shot were not read.
- The jet cannon multiplies by 1.5 against soldiers.
- The gunner chaingun's registry damage is 22, own 50; the registry value applies by L3356.

5625 raw-offset checks matched.

Tests: gunner chaingun hits to destroy a hovering attack helicopter (88 or 200 per hit); one point-blank canister shot on a soldier-sized target to count pellets.

## L3358 - EA's Battle Royale vehicle lines (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3358-ea-battle-royale-vehicle-lines.json). From the [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0):

| EA 1.3.1.0 Battle Royale line | Stored value | Value | Result |
|---|---|---|---|
| Tanks now autospot on the enemy minimap from up to 300m away. | `GraniteBR_TankAutoSpotRadius` | 300.0 | equal |
| UH-79 was using the Multiplayer health value of 1500 instead of the Battle Royale value of 1250. | `VB_VEH_Helicopter_UH60 root health (Field_9040392c)` | 1500 | multiplayer value equal; no stored 1250 found |
| UH-79 minigun bullets are now affected by armour and deal a flat 20 damage. | `WF_Vehicles_TransportHeli_Gunner_Minigun StartDamage / EndDamage` | 34 / 20 | multiplayer row only; its far damage is 20 |
| UH-79 miniguns ... overheat penalty is now three times longer. | `OverHeatPenaltyTime, HeatDropPerSecond` | 0, 0.3 | multiplayer row only; penalty 0, so 'three times' cannot be read from it |
| Increased UH-79 minigun dispersion from 1.2 to 2.4 degrees. | `none for the vehicle minigun` | - | no row |
| Increased the XFGM-6D Recon Drone cooldown from 120 seconds to 240 seconds. | `none` | - | no row with 240 or 120 for the drone |

- EA confirms 1500 as the UH-79's multiplayer health (stored root health; with the tank 1200 and armoured transport 800 of L3334 that is three official health values).
- The Battle Royale overrides have no registry row; they are not needed for multiplayer pages.
- The `GS_Minigun` dispersion rows belong to a soldier weapon and are not evidence for the vehicle minigun.

6 raw-offset checks matched.

## L3363 - Earlier soldier figures rechecked under the array rule (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3363-soldier-figures-array-recheck.json). Dataset: `reference-data/frosty/soldier-figures-array-recheck.json`. L3362 (WEAPONS.md) showed that a soldier body-part cell uses its multiplier array where it has one. The 43 materials used for soldier figures in L3329, L3338, L3342 and L3357 were re-read:

- 38 have no array against the abdomen (all explosions, cannon shells, grenades, missiles): those figures stand.
- Materials 288, 289 and 621 have 0.84 for abdomen and limb against a scalar of 1.0. The 'soldier body' figures recorded for them are chest values:

| File | Bullet material | Close / far damage (registry) | Chest | Stomach and limbs (x0.84) |
|---|---|---|---|---|
| `PD_Vehicles_MBT_SecondaryWeapon_CoaxLMG` | 288 | 35 / 21 | 35 / 21 | 29.4 / 17.64 |
| `PD_Vehicles_RWS_LMG` | 288 | 36 / 19 | 36 / 19 | 30.24 / 15.96 |
| `PD_Vehicles_MBT_AmmoTypes_Canister` | 289 | 50 / 30 | 50 / 30 | 42 / 25.2 |
| `PD_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | 289 | 50 / 30 | 50 / 30 | 42 / 25.2 |
| `PD_Vehicles_RWS_HMG` | 289 | 50 / 24 | 50 / 24 | 42 / 20.16 |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_GAU19` | 289 | 50 / 24 | 50 / 24 | 42 / 20.16 |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_Minigun` | 621 | 34 / 18 | 34 / 18 | 28.56 / 15.12 |
| `WF_Vehicles_TransportHeli_Gunner_Minigun` | 621 | 34 / 20 | 34 / 20 | 28.56 / 16.8 |

- Headshots for these bullets: scalar 1.34 (L3338); the head table also holds 1.4 and the index used by vehicle weapons is not read.

50 raw-offset checks matched.

Test: one coax machine gun headshot on a full-health soldier at close range.

## L3364 - Small-arms bullets against vehicles and the Improved Armor material (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3364-small-arms-vs-vehicles.json). Dataset: `reference-data/frosty/small-arms-vs-vehicles.json`. Grid scalar (`Field_674633de`) per bullet material and vehicle target material; both level grids agree. Vehicle cells have no multiplier array.

| Bullet material | Bullet files | Helicopters (121), key 0 / key 2 | Jets (120) | Armour (119) | Flyer, Vector, RHIB (122) | Quad, bikes (187) | Material 508 |
|---|---|---|---|---|---|---|---|
| 275 | .40SW, .45ACP, 57x28mm +1 | 0.16 / 0.56 | 0.3 | 0 | 0 | 0.13 | 0.55 |
| 276 | .300BLK_Carbine, 545x39mm_Carbine, 556x45mmNATO_Carbine +4 | 0.25 / 0.65 | 0.5 | 0 | 0 | 0.175 | 0.5 |
| 277 | 545x39mm, 556x45mmNATO, 762x39mm | 0.4 / 0.8 | 0.7 | 0 | 0.25 | 0.35 | 0.5 |
| 278 | 545x39mm_MG, 556x45mmNATO_MG, 762x39mm_MG | 0.6 / 1 | 0.8 | 0 | 0.5 | 0.7 | 0.5 |
| 279 | 12gaNo00Buck275_Pump, 12gaNo00Buck275_Semi, 12gaNo00Buck300_Pump +5 | 0 | 0 | 0 | 0.25 | 0.5 | 0.5 |
| 286 | 12gaSlug275_Pump, 12gaSlug275_Semi, 12gaSlug300_Pump +1 | 0 | 0 | 0 | 0.25 | 0.5 | 0.5 |
| 288 | Vehicles_MBT_SecondaryWeapon_CoaxLMG, Vehicles_RWS_LMG | 0.8 / 0.8 | 0.7 | 0 | 0.25 | 1.2 | 1 |
| 289 | Vehicles_MBT_SecondaryWeapon_CoaxHMG, Vehicles_RWS_HMG, Vehicles_MBT_AmmoTypes_Canister | 0.6 / 1 | 0.8 | 0 | 0.5 | 1.5 | 1 |
| 290 | .300WinMag, .300WinMag_Match, .338LapuaMagnum2 +5 | 0.4 / 0.8 | 0.7 | 0 | 0.55 | 0.6 | 0.5 |
| 291 | 556x45mmNATO_Semi | 0.4 / 0.8 | 0.7 | 0 | 0.5 | 0.65 | 0.5 |
| 340 | Vehicles_IFV_PrimaryWeapon_Canister | 0.9 | 1.7 | 0 | 0.5 | 1 | 1 |
| 351 | 556x45mmNATO_Bolt | 0.4 / 0.8 | 0.7 | 0 | 0.55 | 0.6 | 0.5 |
| 491 | .357Magnum, .44Magnum | 0.16 / 0.56 | 0.3 | 0 | 0 | 0.13 | 0.55 |
| 492 | 46x30_PDW, 57x28mm_PDW | 0.16 / 0.56 | 0.3 | 0 | 0.4 | 0.25 | 0.5 |
| 493 | .40SW_PDW, 10x25mm_PDW, 32ACP_PDW +1 | 0.16 / 0.56 | 0.3 | 0 | 0.4 | 0.25 | 0.5 |
| 494 | 68x51mm_Carbine, 762x51mmNATO_Carbine | 0.25 / 0.65 | 0.5 | 0 | 0 | 0.175 | 0.5 |
| 496 | 762x51mmNATO, 762x51mmNATO_MG | 0.4 / 0.8 | 0.7 | 0 | 0.25 | 0.35 | 0.5 |
| 497 | 68x51mm_MG | 0.6 / 1 | 0.8 | 0 | 0.5 | 0.7 | 0.5 |
| 498 | .338LapuaMagnum_Semi, .338LapuaMagnum_Semi_Match, 762x51mmNATO_Semi +3 | 0.4 / 0.8 | 0.7 | 0 | 0.5 | 0.65 | 0.5 |
| 499 | 12gaFlechette275_Pump, 12gaFlechette275_Semi, 12gaFlechette300_Pump +1 | 0 | 0 | 0 | 0.25 | 0.5 | 0.5 |
| 606 | Vehicles_Airplane_PrimaryWeapon_Cannon | 1.06 | 2.15 | 0.3 | 1.25 | 2.6 | none |
| 621 | 556x45mmNATO_Minigun | 0.4 / 0.8 | 0.7 | 0 | 0.25 | 1.2 | 1 |
| 784 | .416Barrett, .416Barrett_Match | 0.4 / 0.8 | 0.7 | 0 | 0.55 | 0.6 | 0.5 |

- Armour (119): 0 for every infantry bullet.
- Helicopters (121): two records with keys 0 and 2 for rifle and pistol calibres; the selector is not read. L3338 and L3357 recorded the key 0 value.
- `Affector_Vehicle_Passive_AttackHeli_ImprovedArmor` holds packed material 532676736 (ID 508). The last column is each bullet against 508: 0.5 for infantry bullets, 1.0 for vehicle machine guns. The UI says the passive gives resistance against most infantry weapons, and EA's [1.3.1.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) say it reduces small arms damage. How 508 combines with the helicopter value is not read.

116 raw-offset checks matched.

Test: one assault rifle bullet on a Scout Helicopter and on an Attack Helicopter with Improved Armor, reading health lost.

## L3368 - Keyed grid records exist only against helicopters (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3368-keyed-records-helicopters-only.json). A scan of every source material against 14 target materials (12,838 cells) finds a second record with key 2 only against the helicopter material 121:

| Key 0 value | Key 2 value | Difference | Projectile materials |
|---|---|---|---|
| 0.16 | 0.56 | 0.4 | 275, 426, 491, 492, 493, 495, 500 |
| 0.25 | 0.65 | 0.4 | 276, 413, 494, 757 |
| 0.4 | 0.8 | 0.4 | 277, 290, 291, 351, 410, 486, 490, 496, 498, 501, 621, 631, 660, 784 |
| 0.6 | 1 | 0.4 | 278, 289, 497, 589, 630 |
| 0.8 | 0.8 | 0 | 288 |

- No tank, jet, light vehicle, boat or soldier cell has a keyed record.
- The step is 0.4 except for material 288 (vehicle light machine gun, 0.8 both).
- All helicopters use material 121, so the switch is something on the helicopter. Candidate: the Improved Armor passive. Not traced; see L3364 for the second candidate (material 508).

84 raw-offset checks matched.

## L3369 - Vehicle machine gun headshots use index 11, so 1.4 (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3369-vehicle-weapon-head-index.json). Dataset: `reference-data/frosty/vehicle-weapon-head-index.json`. Registry rows `<weapon>.PrimaryFire.Shot.DamageProtectionMultiplierIndex` pick the entry of the head table `[1, 1.34, 1.5, 1.75, 1.8, 1, 1, 1, 1, 1, 1, 1.4, 1.57, 1.8, 1.8]`. All nine vehicle weapon rows hold 11:

| Weapon row | Index | Projectile material | Close / far damage | Headshot close / far (x1.4) | Close headshot at the old 1.34 |
|---|---|---|---|---|---|
| `WF_Vehicles_APC_FiringPortWeapon` | 11 | not read | - | - | - |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | 11 | 289 | 50 / 30 | 70 / 42 | 67 |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG` | 11 | 288 | 35 / 21 | 49 / 29.4 | 46.9 |
| `WF_Vehicles_OpenGunner_HMG` | 11 | not read | - | - | - |
| `WF_Vehicles_RWS_HMG` | 11 | 289 | 50 / 24 | 70 / 33.6 | 67 |
| `WF_Vehicles_RWS_LMG` | 11 | 288 | 36 / 19 | 50.4 / 26.6 | 48.24 |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_GAU19` | 11 | 289 | 50 / 24 | 70 / 33.6 | 67 |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_Minigun` | 11 | 621 | 34 / 18 | 47.6 / 25.2 | 45.56 |
| `WF_Vehicles_TransportHeli_Gunner_Minigun` | 11 | 621 | 34 / 20 | 47.6 / 28 | 45.56 |

- Replaces the head value 1.34 in L3338, which was the cell scalar.
- Soldier multipliers for these guns: head 1.4, chest 1.0, stomach and limbs 0.84 (L3363).
- The own value of the index in the vehicle files is not read.

13 raw-offset checks matched.

Test: one coax machine gun headshot on a full-health soldier at close range.

## L3371 - Vehicle machine gun velocity: own 760 is EA's figure, registry 890 is the old one (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3371-vehicle-mg-velocity-own-vs-registry.json). Dataset: `reference-data/frosty/vehicle-mg-velocity.json`. L3335 found the registry velocity rows unequal to EA's [1.3.1.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) figures. The files' own values:

| Firing file | Own value | Registry default | EA 1.3.1.0 old to new |
|---|---|---|---|
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | 760 | 890 | 890 to 760 |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG` | 600 | 737 | 850 to 670 |
| `WF_Vehicles_PatrolBoat_PrimaryWeapon_GAU19` | 890 | - | - |
| `WF_Vehicles_RWS_HMG` | 760 | 890 | 890 to 760 |
| `WF_Vehicles_RWS_HMG-SP` | 890 | 890 | - |
| `WF_Vehicles_RWS_LMG` | 600 | 737 | 850 to 670 |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_GAU19` | 860 | 860 | - |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_Minigun` | 700 | 700 | - |
| `WF_Vehicles_OpenGunner_HMG` | 760 | 890 | - |
| `WF_Vehicles_TransportHeli_Gunner_Minigun` | 700 | 700 | - |

- Heavy machine guns: own 760 equals EA's new figure; the registry default 890 is EA's old one. This is an exception to the registry-first rule of L3356 (ROSTER_VALUES.md).
- Light machine guns: neither 600 nor 737 equals EA's 670 (737 = 670 x 1.1, arithmetic only).
- Miniguns and the Scout Helicopter GAU-19 agree in both places.

19 raw-offset checks matched.

Test: time a coaxial HMG bullet to a wall 380 m away (0.5 s for 760, 0.43 s for 890).

## L3372 - Launch speed in file and registry, all vehicle weapons (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3372-vehicle-weapon-velocity-own-vs-registry-survey.json). Dataset: `reference-data/frosty/vehicle-weapon-launch-speed.json`. 59 firing files: 36 have a registry row equal to the file's value, 16 have no row, seven differ:

| Firing file | Own value | Registry default | EA |
|---|---|---|---|
| `WF_Vehicles_AttackHeli_PrimaryWeapon_SmartRockets` | 180 | 360 | no EA line on file |
| `WF_Vehicles_IFV_PrimaryWeapon_APFSDST` | 375 | 445 | EA 1.3.3.0: 375 to 445 |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | 760 | 890 | EA 1.3.1.0: 890 to 760 |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG` | 600 | 737 | EA 1.3.1.0: 850 to 670 |
| `WF_Vehicles_OpenGunner_HMG` | 760 | 890 | no line for this gun (EA names RWS and coaxial) |
| `WF_Vehicles_RWS_HMG` | 760 | 890 | EA 1.3.1.0: 890 to 760 |
| `WF_Vehicles_RWS_LMG` | 600 | 737 | EA 1.3.1.0: 850 to 670 |

- IFV AP shell: the usual direction (registry new, file old).
- Machine guns: see L3371; the open-gunner HMG behaves like the other heavy machine guns.
- Attack Helicopter Smart Rockets: 180 in the file, 360 in the registry and in the Scout Helicopter's file. No EA line.

18 raw-offset checks matched. Full list: `reference-data/frosty/vehicle-weapon-launch-speed.json`.

Test: time an Attack Helicopter Smart Rocket to a target 360 m away (1 s for 360, 2 s for 180).

## L3373 - Rate of fire, magazine and heat in file and registry, all vehicle weapons (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3373-vehicle-weapon-own-vs-registry-rate-magazine-heat.json). Dataset: `reference-data/frosty/vehicle-weapon-own-vs-registry.json`. | Property | Equal | Different | No registry row |
|---|---|---|---|
| RateOfFire | 42 | 6 | 20 |
| MagazineCapacity | 46 | 3 | 19 |
| HeatPerBullet | 12 | 2 | 54 |

The 11 differences:

| Firing file | Property | Own value | Registry default | EA |
|---|---|---|---|---|
| `WF_Vehicles_AA_PrimaryWeapon_AAHV` | HeatPerBullet | 0.042 (2.1.1.0: 0.125) | 0.036 (2.1.1.0: 0.13) | 1.3.3.0: heat per bullet 4.2% to 3.6% |
| `WF_Vehicles_AA_SecondaryWeapon_AimGuidedMissile` | MagazineCapacity | 2 | 1 | no line on file |
| `WF_Vehicles_Airplane_Bomb_Mk82AIR` | RateOfFire | 300 | 1200 | no line on file |
| `WF_Vehicles_IFV_PrimaryWeapon_APFSDST` | RateOfFire | 200 | 160 | 1.3.1.0: 200 to 120; 1.3.3.0: 120 to 160 |
| `WF_Vehicles_IFV_PrimaryWeapon_APFSDST` | MagazineCapacity | 12 | 10 | 1.3.1.0: 12 to 10 |
| `WF_Vehicles_IFV_PrimaryWeapon_Canister` | RateOfFire | 200 | 240 | 1.3.1.0: 200 to 240 |
| `WF_Vehicles_IFV_PrimaryWeapon_Canister` | MagazineCapacity | 12 | 16 | 1.3.1.0: 12 to 16 |
| `WF_Vehicles_IFV_PrimaryWeapon_HEAB` | RateOfFire | 200 | 180 | 1.3.1.0: 200 to 180 |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG` | RateOfFire | 700 | 720 | no line on file |
| `WF_Vehicles_ScoutHeli_Passenger_PrimaryWeapon_ThermalScanner` | RateOfFire | 3600 | 300 | no line on file |
| `WF_Vehicles_ScoutHeli_PrimaryWeapon_Minigun` | HeatPerBullet | 0.006667 | 0.008889 | no line on file |

- All six with an EA figure: registry = EA's new number, file = EA's old number. The registry-first rule (L3356) holds here.
- Five have no EA line; the registry value is taken as current by that rule, unconfirmed.
- The machine gun velocity (L3371) remains the only case where the file is newer.

22 raw-offset checks matched.

Test: count Scout Helicopter minigun shots to overheat (112 or 150).

## L3382 - Vehicle health override affectors (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3382-vehicle-health-override-affectors.json). Dataset: `reference-data/frosty/vehicle-health-override-affectors.json`. Class `Class_15cfe943`; `Field_9040392c` is the health hash of vehicle bodies. Multiplayer and Battle Royale:

| Affector file | Health (`9040392c`) | `6f28bf9c` | `cbf2ad7c` | `8e30ee56` |
|---|---|---|---|---|
| `Affector_Vehicles_MP_DisabledStateHealthRegeneration` | 0 | 0 | 0.25 (2.1.1.0: 0.3) | 1 |
| `Affector_UH60VehicleHealthOverride_F2P` | 1250 | 200 | 0 | 1 |
| `Affector_IFVVehicleHealthOverride_F2P` | 750 | 200 | 0 | 1 |
| `Affector_TankVehicleHealthOverride_F2P` | 800 | 200 | 0 | 1 |

- UH-79 override 1250 equals EA's [1.3.1.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-1-0) Battle Royale value; L3358 had found no stored 1250.
- `6f28bf9c` (200) fits a critical-health threshold; `cbf2ad7c` 0.25 on the multiplayer disabled-state affector is near EA's 'slowed by 80 percent' (which would be 0.2) and is not recorded as that figure.

Single-player modifiers (not for multiplayer pages):

| Affector file | Health (`9040392c`) | `6f28bf9c` | `cbf2ad7c` | `8e30ee56` |
|---|---|---|---|---|
| `Affector_VehicleHealthMod_Eurocopter_Enemy_NightRaid_SP` | 4000 | 800 | - | - |
| `Affector_VehicleHealthMod_AAV7A1_Player_SP` | 2500 | 500 | - | - |
| `Affector_VehicleHealthMod_Abrams_Player_SP` | 1000 | 200 | - | - |
| `Affector_VehicleHealthMod_Abrams_Squad_SP` | 1000 | 200 | - | - |
| `Affector_VehicleHealthMod_Bradley_M03_Escort_SP` | 1500 | 300 | - | - |
| `Affector_VehicleHealthMod_CV90_Enemy_SP` | 500 | 100 | - | - |
| `Affector_VehicleHealthMod_Cheetah_Enemy_SP` | 320 | 100 | - | - |
| `Affector_VehicleHealthMod_Leopard_Enemy_SP` | 450 | 120 | - | - |
| `Affector_VehicleHealthMod_Oerlikon_Enemy_SP` | 300 | 100 | - | - |
| `Affector_VehicleHealthMod_UH60_Enemy_SP` | 600 | 150 | - | - |
| `Affector_VehicleHealthMod_Marauder_Enemy_SP` | 400 | 100 | - | - |
| `Affector_VehicleHealthMod_Quadbike_Enemy_SP` | 400 | 100 | - | - |
| `Affector_VehicleHealthMod_Vector_Enemy_SP` | 400 | 100 | - | - |

42 raw-offset checks matched.

## L3383 - Vehicle upgrade multiplier affectors against registry rank rows (9 October 2026) - Replaced by L3384 (counts corrected)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3383-vehicle-upgrade-multiplier-affectors.json). Dataset: `reference-data/frosty/vehicle-upgrade-multiplier-affectors.json`. One multiplier per affector file (`Field_8cf424e7`, lock-on time `Field_e2280e0b`, spot time `Field_f95f67f4`). Registry pairing is by name only. Rows that differ come first, then rows that agree, then file-only values:

| Affector file | File value | Registry row (name-only join) | Registry default |
|---|---|---|---|
| `Affector_Vehicles_Abilities_IFV_Antispotting_LockOnTime` | 0.8 | `Passives_Vehicles_IFV_Antispotting_LockOnTime.RankData[0].LockingTimeMultiplier` | 0.6 |
| `Affector_Vehicles_Abilities_AttackHeli_AntiRadar_LockOnTime` | 0.8 | `Passives_Vehicles_AttackHeli_AntiRadar_LockOnTime.RankData[0].LockingTimeMultiplier` | 0.7 |
| `Affector_VEH_PassiveAbility_CaptureSpeed` | 1.1 | `Passives_Vehicles_CaptureSpeed_Affector.RankData[0].Value` | 1.15 |
| `Affector_Vehicles_6Wheels_ImprovedSteeringRatio` | 1.02 | `Passives_Vehicles_Shared_Gunhandling_ImprovedSteeringRatio.RankData[0].Value` | 1.03 |
| `Affector_VEH_Tank_TurretVelocity_YawMultiplier` | 1.2 | `Passives_Vehicles_Shared_GunHandling_YawMultiplier.RankData[0].Value` | 1.3 |
| `Affector_VEH_Tank_TurretVelocity_PitchMultiplier` | 1.2 | `Passives_Vehicles_Shared_GunHandling_PitchMultiplier.RankData[0].Value` | 1.3 |
| `Affector_Vehicles_Abilities_IFV_Antispotting_SpotTimeMultiplier` | 0.75 | `Passives_Vehicles_IFV_Antispotting_SpotTimeMultiplier.RankData[0].SpotTimeMultiplier` | 0.75 |
| `Affector_Vehicles_Abilities_AA_Antispotting_SpotTimeMultiplier` | 0.75 | `Passives_Vehicles_AA_Antispotting_SpotTimeMultiplier.RankData[0].SpotTimeMultiplier` | 0.75 |
| `Affector_Vehicles_Abilities_AttackHeli_AntiRadar_SpottingDuration` | 0.75 | `Passives_Vehicles_AttackHeli_AntiRadar_SpottingDuration.RankData[0].SpotTimeMultiplier` | 0.75 |
| `Affector_Vehicles_Abilities_AttackHeli_GroundTargetDetection_LockOnTime` | 1.1 | `Vehicle_Ability_AttackHeli_GroundTargetDetection_LockOnTimePenalty.RankData[0].LockingTimeMultiplier` | 1.1 |
| `Affector_VEH_Ability_ProximityDetectionSystem_RangeIncreaseModifier` | 1.3 | `Passives_Vehicles_IFV_EquipmentUpgrade_ProximityDetectionSystemRadiusMultiplier.RankData[0].Value` | 1.3 |
| `Affector_Vehicles_6Wheels_MassMultiplier` | 1.04 | `Passives_Vehicles_Shared_Durability_MassMultiplier.RankData[0].Value` | 1.04 |
| `Affector_VEH_AirRadarRangeIncreaseMultiplier` | 1.5 | `Passives_Vehicles_AA_EquipmentUpgrade_AirRadarRadiusMultiplier.RankData[0].Value` | 1.5 |
| `Affector_Vehicles_Abilities_AA_Antispotting_LockOnTime` | 0.8 | none | - |
| `Affector_VEH_GroundRadarRangeIncreaseMultiplier` | 1.5 | none | - |
| `Affector_Vehicles_Boost_ConsumptionRate` | 1.15 | none | - |
| `Affector_Vehicles_Boost_RecoveryReduction` | 0.5 | none | - |
| `Affector_Vehicles_CruiseSpeedReductionModifier` | 0.84 | none | - |
| `Affector_Vehicles_IFV_CruiseSpeedModifier` | 0.92 | none | - |
| `Affector_Vehicles_MBT_CruiseSpeedModifier` | 0.92 | none | - |
| `Affector_Vehicles_Rotor_EngineUpgradeMultiplier` | 1.15 | none | - |
| `Affector_Vehicles_Rotor_MassMultiplier` | 0.85 | none | - |
| `Affector_Vehicles_TailRotor_StabilizerMultiplier` | 0.5 | none | - |

- Registry and file values are recorded separately. By L3356 and L3373 the registry is the likelier live value where they differ; that rule was shown for weapon rows only.
- File-only values can be stale (L3343).

36 raw-offset checks matched.

Tests: time a full turret turn with and without the gun handling upgrade; lock-on time against an IFV with the anti-spotting upgrade.

## L3384 - Vehicle upgrade multiplier affectors, corrected counts (replaces L3383) (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3384-vehicle-upgrade-multiplier-affectors-corrected.json). Dataset: `reference-data/frosty/vehicle-upgrade-multiplier-affectors-corrected.json`. L3383 stated 14 pairs, eight agreeing and nine file-only; the table it printed was right and the counts are 13, seven and ten. One multiplier per affector file (`Field_8cf424e7`, lock-on time `Field_e2280e0b`, spot time `Field_f95f67f4`). Registry pairing is by name only. Rows that differ come first, then rows that agree, then file-only values:

| Affector file | File value | Registry row (name-only join) | Registry default |
|---|---|---|---|
| `Affector_Vehicles_Abilities_IFV_Antispotting_LockOnTime` | 0.8 | `Passives_Vehicles_IFV_Antispotting_LockOnTime.RankData[0].LockingTimeMultiplier` | 0.6 |
| `Affector_Vehicles_Abilities_AttackHeli_AntiRadar_LockOnTime` | 0.8 | `Passives_Vehicles_AttackHeli_AntiRadar_LockOnTime.RankData[0].LockingTimeMultiplier` | 0.7 |
| `Affector_VEH_PassiveAbility_CaptureSpeed` | 1.1 | `Passives_Vehicles_CaptureSpeed_Affector.RankData[0].Value` | 1.15 |
| `Affector_Vehicles_6Wheels_ImprovedSteeringRatio` | 1.02 | `Passives_Vehicles_Shared_Gunhandling_ImprovedSteeringRatio.RankData[0].Value` | 1.03 |
| `Affector_VEH_Tank_TurretVelocity_YawMultiplier` | 1.2 | `Passives_Vehicles_Shared_GunHandling_YawMultiplier.RankData[0].Value` | 1.3 |
| `Affector_VEH_Tank_TurretVelocity_PitchMultiplier` | 1.2 | `Passives_Vehicles_Shared_GunHandling_PitchMultiplier.RankData[0].Value` | 1.3 |
| `Affector_Vehicles_Abilities_IFV_Antispotting_SpotTimeMultiplier` | 0.75 | `Passives_Vehicles_IFV_Antispotting_SpotTimeMultiplier.RankData[0].SpotTimeMultiplier` | 0.75 |
| `Affector_Vehicles_Abilities_AA_Antispotting_SpotTimeMultiplier` | 0.75 | `Passives_Vehicles_AA_Antispotting_SpotTimeMultiplier.RankData[0].SpotTimeMultiplier` | 0.75 |
| `Affector_Vehicles_Abilities_AttackHeli_AntiRadar_SpottingDuration` | 0.75 | `Passives_Vehicles_AttackHeli_AntiRadar_SpottingDuration.RankData[0].SpotTimeMultiplier` | 0.75 |
| `Affector_Vehicles_Abilities_AttackHeli_GroundTargetDetection_LockOnTime` | 1.1 | `Vehicle_Ability_AttackHeli_GroundTargetDetection_LockOnTimePenalty.RankData[0].LockingTimeMultiplier` | 1.1 |
| `Affector_VEH_Ability_ProximityDetectionSystem_RangeIncreaseModifier` | 1.3 | `Passives_Vehicles_IFV_EquipmentUpgrade_ProximityDetectionSystemRadiusMultiplier.RankData[0].Value` | 1.3 |
| `Affector_Vehicles_6Wheels_MassMultiplier` | 1.04 | `Passives_Vehicles_Shared_Durability_MassMultiplier.RankData[0].Value` | 1.04 |
| `Affector_VEH_AirRadarRangeIncreaseMultiplier` | 1.5 | `Passives_Vehicles_AA_EquipmentUpgrade_AirRadarRadiusMultiplier.RankData[0].Value` | 1.5 |
| `Affector_Vehicles_Abilities_AA_Antispotting_LockOnTime` | 0.8 | none | - |
| `Affector_VEH_GroundRadarRangeIncreaseMultiplier` | 1.5 | none | - |
| `Affector_Vehicles_Boost_ConsumptionRate` | 1.15 | none | - |
| `Affector_Vehicles_Boost_RecoveryReduction` | 0.5 | none | - |
| `Affector_Vehicles_CruiseSpeedReductionModifier` | 0.84 | none | - |
| `Affector_Vehicles_IFV_CruiseSpeedModifier` | 0.92 | none | - |
| `Affector_Vehicles_MBT_CruiseSpeedModifier` | 0.92 | none | - |
| `Affector_Vehicles_Rotor_EngineUpgradeMultiplier` | 1.15 | none | - |
| `Affector_Vehicles_Rotor_MassMultiplier` | 0.85 | none | - |
| `Affector_Vehicles_TailRotor_StabilizerMultiplier` | 0.5 | none | - |

- Registry and file values are recorded separately. By L3356 and L3373 the registry is the likelier live value where they differ; that rule was shown for weapon rows only.
- File-only values can be stale (L3343).

36 raw-offset checks matched.

Tests: time a full turret turn with and without the gun handling upgrade; lock-on time against an IFV with the anti-spotting upgrade.

## L4031 - Vehicle driving graphs (car, tank, aircraft, helicopter) (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4031-vehicle-driving-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/vehicles-tank.md`).

- Car (JLTV): boost meter 0..1 drains at 0.27 per second x the boost consumption effect and refills at 0.15 per second x the recovery effect; boost can start above 0.03 x 1.1; drive input fades to zero near 120 forward and 30 in the second case (reverse or crawl, inferred), speeds in km/h; drag = min(speed, 110)^2 x 0.8 x frame time; maximum steer 45 (quad bike 35).
- Dirt bike: no mobility or engine damage inputs; reports wheelie time to persistence.
- Tank (Abrams): speed cap 43 x `CruiseSpeedReductionModifier`, alternative cap 42, reverse 12 (km/h); throttle fades over the last 0.25 below the cap; mobility damage sets the cap target to 0 and zeroes turning; boost drains 0.14 per second and refills 0.115 (0.175 fast); a damaged track side drives at 0.45 (inferred). Bradley caps 45 and 43; Gepard 43 and 48 with no cruise import.
- Aircraft (F-16): grounded becomes airborne at 280 or more with pitch at or above 0 and a clear 20 m forward probe; airborne becomes grounded below 270 with pitch under 20 and a 50 m probe hit. Boost needs the meter above 0.3333, drains 0.0333 per second and refills 0.0667. Mobility damage adds 0.75 random-sign roll and -0.5 pitch. The Su-57 matches; the MQ-9 has no ground switch.
- F-16 airstrike: bombs release every 60 / 1200 = 0.05 s, alternating two bomb types, then 7 flares. MQ-9 overwatch leaves when health is under 0.3 or its time ends; a 40 constant is read as the upgraded leave timer.
- Helicopter (AH-64): engine target is 1 only with a driver and no damage state; spool up 3 s, down 16 s (10 s when damaged); mobility damage halves two flight parameters and adds a yaw bias of 1.1 x `TailRotor_StabilizerMultiplier`; yaw input smoothing 0.3 s (UH-60 0.5 s).
- Helicopter flares (UH-60 ability graph): 12 flares at 400 per minute, then the remove-signature effect for `IsLockableTime` minus current lock progress; no cooldown in this graph.

41 raw-offset checks matched.

## L4032 - Shared vehicle ability, expression and projectile graphs (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4032-shared-vehicle-ability-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/vehicles-common.md`).

- Weapon-slot cycling: 16 small graphs (Hellfire, Stinger, Maverick, Mk 82, AIM-9X, GBU-39 and others) increment the active launcher index and wrap to 1 past the launcher count.
- Smoke (`SimEx_SmokeMechanics`): each cloud applies `HideFromLockOn` for the Hide Duration tunable to entities inside, optionally with missile-jammer, laser-paint removal, cloud-volume and force-minimum-angle-damage effects; tracer-dart interaction is behind a kill switch. The smokescreen ability graph holds 6.5 and 5.0 constants; the passenger smoke launcher 21 and 2.4 (roles not established).
- Flares: 400 per minute (one every 0.15 s); then `Flares_RemoveSignature` for `IsLockableTime` minus the best active lock's progress.
- Radar: effective range = maximum range x max(range-increase effect, 1); a target with the jam-locking-weapon effect gets range 0; spots last one tick.
- Explosives detection: detonations staggered by 10 fixed fractions of `MaxDetonationDelay`; a 0.15 constant is present.
- Cluster bomb (Rockeye): rings of 1, 4 and 8 bomblets (13 in all, inferred), 2 degrees per ring, random speed 0.85 to 1.15.
- Passive anti-spotting and anti-lock abilities apply their effect while active and drop when laser-painted, damaged or slowed, with a reactivation timer.
- Mortar illumination descent uses 58, 70 and 80 m/s by charge; the 120 mm airburst graph holds 225; bunker buster 0.525 and 0.75; thermal smoke damage 2.5; vehicle thermal signature 0.9 (roles in the findings file, several inferred).

13 raw-offset checks matched.

## L4033 - Boat and stationary weapon graphs (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4033-boat-and-stationary-weapon-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/vehicles-boat-stationary.md`).

- Boats: while `Affector_Vehicles_MobilityDamage` is active, throttle to thrust is 0 (CB90 0x428c, jet ski 0x1d54; RHIB imports the same effect).
- CB90 and RHIB boost (0x4694 to 0x5348): meter 0..1; needs sprint input, a driver, throttle above 0, brake 0 and no crawl mode; starts only above the configured threshold x 1.1; drain and recharge are scaled by the consumption and recovery effects; rates come from a vehicle configuration table.
- CB90 capsize (inferred): thrust cut at 80 degrees tilt or more; self-righting torque 18 between 80 and 181 degrees when speed is under 5 with a driver seated.
- Throttle response time: CB90 0.1 s; RHIB 0.375 / 0.4 s; jet ski 0.7 / 0.85 s.
- Phalanx: slew limited to frame time x `PhalanxAimRotationSpeed`; pitch 0 to 90; aim point = position + velocity x T + 0.5 x acceleration x T^2 with T from a distance curve; a sweep offset decays toward `AimStrafeMinimum` over `AimEscalationTime`, 4 x faster against fast targets; bursts alternate `BurstDuration` and `BurstCooldown`; a target is dropped after burst duration + curve x 1.35.
- Missile battery: launch speed = sqrt(9.8 x r^2 / (r - dz)), a 45 degree lob; reload from `CS_fSSMBattery_ReloadTime`; six tubes cycle; fires only once the turret has stopped; an owner change resets the reload timer.

11 raw-offset checks matched.

## L4037 - Vehicle mobility hit rule (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4037-vehicle-mobility-hit-rule.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/vehicle-mobility-hit.md`).

- Trigger (0x214 to 0x414): for each new damage event with damage above 0, sum = damage + stored sum; if sum >= scale x `MobilityHitDamageThreshold`, apply `Affector_Vehicles_MobilityDamage` for `MobilityHitDuration` and set the sum to 0; otherwise store the sum.
- Window (0x55c to 0x678): the sum is set to 0 when ticks since the recorded hit exceed `MobilityHitTimeFrame` / max(frame time, 1/240).
- Removal (0x438 to 0x4ec): `Affector_Vehicles_RemoveMobilityDamge` is applied when `Vehicle Health Normalized` equals 1 and a stored flag is set.
- Defaults (already recorded): threshold 0.5, duration 5 s, time frame 3 s.
- Effect of a mobility hit by class (L4031, L4033): tanks lose speed and turning, boats lose thrust, helicopters have two flight parameters halved, jets get random roll and nose-down pitch.
- Vehicle health and critical-health thresholds are not in expression graphs; they remain as recorded in L3347 and L3348.

2 raw-offset checks matched.
