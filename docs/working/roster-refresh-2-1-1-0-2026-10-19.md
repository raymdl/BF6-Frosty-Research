# Roster refresh on build 2.1.1.0 (19 October 2026)

Research only. Re-run of the L3307 roster-values pass (`docs/working/ROSTER_VALUES.md`, build 1.4.3.5) on the Season 5 captures, to see which stored and registry values moved. Nothing here is an in-game reading, and no site data, simulation or UI change is authorized.

## Method

1. Same script, same hand tables: `python scripts/frosty-roster-values.py --build-dir builds/2.1.1.0/capture --descriptors builds/2.1.1.0/capture/toolchain/SharedTypeDescriptors.ebx --out-dir builds/2.1.1.0/reports/roster-refresh-2026-10-19 --names reference-data/frosty/roster-display-names.json --name-joins reference-data/frosty/roster-registry-name-joins.json`. Every route it needs was already in `capture/collection/raw` (31,432 files); nothing was captured. The 15 October hotfix changed no gadget or vehicle asset (BUILD.json: 3 changed routes, none of them gadget or vehicle), so the 13 October capture stands for the hotfix.
2. All 11,902 raw-offset checks pass (`frosty-raw-check.py --manifest raw-check-manifest.json`, output `raw-checks.json`), 0 decode failures (the 1.4.3.5 pass had three: the two `SP_SwitchbladeDrone` affectors and the crouched incendiary affector; they decode now).
3. Old side: `reference-data/frosty/roster-values.json` (1.4.3.5). New side: `roster-compact.json` of the run folder. Entries compared by stat id (167 on both sides, none added or removed). Registry rows were de-duplicated across entries and compared by (owner, row name) on the default value; own values by (file, property). Outputs `diff.json` (per entry) and `diff-dedup.json` (de-duplicated) are in the run folder.
4. Cross-checked against `builds/2.1.1.0/reports/registry-diff-2026-10-14/registry-diff.tsv` (all-rows diff) and EA's 2.1.1.0 notes (fetched through a page summarizer on 19 October; re-read the page before citing a figure).

Run folder: `C:\Users\royal\Documents\BF6 Datamining\builds\2.1.1.0\reports\roster-refresh-2026-10-19`.

## Source assets

Rosters: `Persistence/StatCategories/StatCategorization/Categorization_Vehicles`, `_Gadgets`, `_Vehicles_Equipment`. Registries: `Common/Hardware/Gadgets/GRX_Gadgets_Glacier`, `Common/GameSetup/Tweakables/GameRemixer/GRX_Vehicles`. Carrier and weapon files under `Common/Hardware/Gadgets`, `Common/Hardware/Vehicles`, `Common/Gameplay/Abilities`, `Common/Gameplay/Loadouts/Vehicles`. All read from `builds/2.1.1.0/capture/collection/raw`.

## Result

- Roster: `Categorization_Gadgets` changed hash (4beaf227… to 8ce12b95…); the other two are equal. Identity, category, archetype, group and GUID lists are unchanged for every entry except the GUID lists of `gad_ubl_gl_smoke`, `gad_ubl_gl_he` and `gad_ubl_gl_tb` (underbarrel launchers, which had no defining object and still have none). Still the same nine entries with no defining object.
- Coverage: with own values 31 / 60 / 42 (unchanged); with registry rows vehicles 30 (30), gadgets 45 (44), vehicle equipment 59 (60). The gadget gain is the IGLA below; the vehicle-equipment loss is the Field Maintenance rename below.
- Registry rows reached: 5,656 to 5,708. 66 rows changed default, 56 added, 4 removed. Own values: 3 changed, 7 newly reached, 0 removed.
- The registry moved far more than the assets: of the 17 properties that now differ between registry and own value and did not before, in every case the registry moved and the asset did not. That is the pattern L3314 named as its reopening condition.
- Registry-against-own differences, recomputed with an owner-name join over the roster rows: 94 before, 111 now. 17 new, 1 resolved (`PB_Missile_TOW2B` `InnerBlastRadius`: registry 1.75 to 2.0 and asset 1.0 to 2.0, now equal), 8 moved on the registry side only. The 73-property census of L3314 is not recomputed (its pairing method is not in a script); of its 73 pairs, 1 is now equal (the TOW2B row) and 72 still differ.

## Matches with EA's 2.1.1.0 notes

The notes name figures that equal the registry change and not the asset's own value, where both exist:

- Anti-Armor AA shell (`PD_Vehicles_AA_PrimaryWeapon_AAAP`): damage to infantry 20 to 50 (registry; asset own value 57 unchanged), rate of fire 240 to 480, magazine 8 to 4, reload 2.4 to 1.2, velocity 560 to 900, projectile life 2 to 1.73.
- Multi-Purpose AA shell (AAGP): infantry 13 to 34 (registry; asset 32 unchanged), velocity 850 to 1,175, life 1.6 to 1.32.
- 35mm High Velocity AA (AAHV): infantry 13 to 25 (registry; asset 12 unchanged), heat per shot 3.6% to 13%, heat recovery 0.5 to 0.833, velocity 1,175 to 1,250, life 1.2 to 1.24.
- GDF-009 Cannon (`Stationary_AntiAir`): rate of fire 720 to 1,100, heat 4.2% to 8.4%, recovery 0.5 to 1, life 1.2 to 1.32; registry infantry damage is now 34 for start and end, the notes say 34.
- RWS .50 cal: rate of fire 400 to 450 and life 1.5 to 4; drag 0.0035 to 0.002 sits on the coaxial row.
- Scout helicopter rocket pod resupply 28 to 38 s (`AutoReplenishDelay`); MBT and IFV passive regeneration delay 12 s reapplied when firing (new `Base_RegenDelay` 12 and `ResetHealthRegenOnFire` true).
- No matching figure in the notes for the MBT HE and coaxial heat rows, the TOW2B flight rows, the AGM-88 turn angle or Hydra damage 15 to 12 (the notes state only a 30% cut of 70mm splash damage; 12 / 15 is 20%).

Reading: for the AA ammunition rows EA's infantry damage figure equals the registry default and differs from the asset's own number (50 against 57, 34 against 32, 25 against 12), the same direction as L3317 and L3324. This is a statement matched to a stored value, not an in-game control.

## Changes by group

- **Field Maintenance regeneration (`veheq_upg_fieldmain`).** The four rows `Passives_Vehicles_{IFV,MBT}_Regeneration_{Rate,RegenDelay}` (IFV 110 / 9.5, MBT 132 / 9.5) are gone. New rows: `Base_RegenRate` IFV 87.5 and MBT 100, `Base_RegenDelay` 12 for both, `MaintenanceRegeneration_Rate` IFV 96.25 and MBT 110, `MaintenanceRegeneration_RegenDelay` 9.5, and `Passive_Vehicles_ResetHealthRegenOnFire` true. The pass lost the entry's four registry rows because the name table `roster-registry-name-joins.json` names the old owners; the table was not edited.
- **IGLA (`gad_rl_autoguide`).** In 1.4.3.5 its `WB_IGLA*` / `PB_NS_IGLA*` rows sat in `MutatorDatabase_CH1_S02` (REDSEC). 2.1.1.0 removed them there and `GRX_Gadgets_Glacier` now holds 56 owner-named rows (`WB_IGLA`, `PB_NS_IGLA`), so the owner-name join finds them. Examples: missile `MaxSpeed` 480, `MaxTurnAngle` 420, `LockTime` 0, reload 3.4, three magazines, resupply 18 s. Whether the new rows replace the removed mutator rows value for value was not compared.
- **Supply Pouch (`gad_sup_pouch`).** Registry: magazine capacity 1 to 3, number of magazines 3 to 1, auto-replenish rounds -1 to 1, auto-replenish magazine true to false, reload time 0 to 1. The notes state new per-use ammunition amounts for the pouch; no row here carries those amounts.
- **Frag grenade (`gad_gren_frag`).** `Detonation Delay After Bounce` 1.4 to 1.1 (L3310 recorded the fuse 1.1 and 1.4 after a bounce).
- **Own values.** `PB_Missile_TOW2B` and `PB_Missile_TOW2B_SP` `InnerBlastRadius` 1 to 2; `PB_PRJ_PTKM1R_EFP` `BlastDamage` 160 to 142 (no registry row, no figure in the notes). `WF_Vehicles_Stationary_TOW` explosion values and `Gadget_SupplyCrate_WB` speed 350 / life 30 are newly reached by shared-file reach, not changed numbers.
- **Unnamed carrier numbers.** 85 (entry, field hash, file) groups differ (41 removed, 30 added, 14 changed). They come from changed reach (new shared users such as `SimEx_KillCam` and `SimEx_DamageReceived`, changed M320 and sniper decoy carrier sets) and changed carrier files; listed in `diff.json`, not interpreted.
- **Registry rows beyond the roster pass.** The all-rows diff also shows `AssaultLadderConfig.RampAngle` 52 to 45 (in the table) and a row named `Range` 3 to 15 in `GRX_Gadgets_Glacier` (not joined to any entry), 113 gadget rows added in total (IGLA 56 plus 16 sublocking rows, PTKM1R civilian-vehicle rows, `ATMine_TransportDetectionInterval`). The 2,150 added `GRX_Weapons` rows belong to the Season 5 attachment and weapon work and were not touched.

## Table: registry defaults that changed (66 rows)

Values are the registry default. A row is shown once even when several roster entries reach it.

| Asset (registry owner) | Property | Old (1.4.3.5) | New (2.1.1.0) | Roster entries |
| --- | --- | --- | --- | --- |
| `AssaultLadderConfig` | `RampAngle` | 52.0 | 45.0 | gad_ladder |
| `FragGrenade` | `FragGrenade_Detonation Delay After Bounce` | 1.4 | 1.1 | gad_gren_frag |
| `PB_Missile_AGM88` | `MissileEntityData.MaxTurnAngle` | 30.0 | 15.0 | veh_air_f97kes, veh_air_fa18f, veh_air_su57 |
| `PB_Missile_TOW2B` | `MissileEntityData.Drag` | 0.0 | 0.000454 | gad_surv_crows, station_at_m41a7tow, veh_sur_bradley… |
| `PB_Missile_TOW2B` | `MissileEntityData.EngineTimeToIgnition` | 0.14 | 0.1 | gad_surv_crows, station_at_m41a7tow, veh_sur_bradley… |
| `PB_Missile_TOW2B` | `MissileEntityData.EngineTimeToLive` | 3.95 | 1.6 | gad_surv_crows, station_at_m41a7tow, veh_sur_bradley… |
| `PB_Missile_TOW2B` | `…Explosion.ExplosionEntityData.InnerBlastRadius` | 1.75 | 2.0 | gad_surv_crows, station_at_m41a7tow, veh_sur_bradley… |
| `PB_Missile_TOW2B` | `…TimeToLive` | 11.5 | 18.0 | gad_surv_crows, station_at_m41a7tow, veh_sur_bradley… |
| `PB_Missile_TOW2B` | `MissileEntityData.MaxTurnAngle` | 90.0 | 60.0 | gad_surv_crows, station_at_m41a7tow, veh_sur_bradley… |
| `PB_Missile_TOW2B` | `MissileEntityData.MinTurnAngle` | 25.0 | 15.0 | gad_surv_crows, station_at_m41a7tow, veh_sur_bradley… |
| `PB_Missile_TOW2B` | `MissileEntityData.TimeToActivateGuidingSystem` | 0.165 | 0.1 | gad_surv_crows, station_at_m41a7tow, veh_sur_bradley… |
| `PD_Vehicles_AA_PrimaryWeapon_AAAP` | `BulletEntityData.Drag` | 0.0025 | 0.0015 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `PD_Vehicles_AA_PrimaryWeapon_AAAP` | `BulletEntityData.EndDamage` | 20.0 | 50.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `PD_Vehicles_AA_PrimaryWeapon_AAAP` | `…TimeToLive` | 2.0 | 1.73 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `PD_Vehicles_AA_PrimaryWeapon_AAAP` | `BulletEntityData.StartDamage` | 20.0 | 50.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `PD_Vehicles_AA_PrimaryWeapon_AAGP` | `BulletEntityData.Drag` | 0.0025 | 0.0015 | veh_sur_cheetah1a2, vehec_wp_rnd_35aaap |
| `PD_Vehicles_AA_PrimaryWeapon_AAGP` | `BulletEntityData.EndDamage` | 13.0 | 34.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aaap |
| `PD_Vehicles_AA_PrimaryWeapon_AAGP` | `…TimeToLive` | 1.6 | 1.32 | veh_sur_cheetah1a2, vehec_wp_rnd_35aaap |
| `PD_Vehicles_AA_PrimaryWeapon_AAGP` | `BulletEntityData.StartDamage` | 13.0 | 34.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aaap |
| `PD_Vehicles_AA_PrimaryWeapon_AAHV` | `BulletEntityData.Drag` | 0.0025 | 0.0015 | veh_sur_cheetah1a2, vehec_wp_rnd_35aahv |
| `PD_Vehicles_AA_PrimaryWeapon_AAHV` | `BulletEntityData.EndDamage` | 13.0 | 25.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aahv |
| `PD_Vehicles_AA_PrimaryWeapon_AAHV` | `…TimeToLive` | 1.2 | 1.24 | veh_sur_cheetah1a2, vehec_wp_rnd_35aahv |
| `PD_Vehicles_AA_PrimaryWeapon_AAHV` | `BulletEntityData.StartDamage` | 13.0 | 25.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aahv |
| `PD_Vehicles_MBT_AmmoTypes_APFSDS` | `BulletEntityData.Drag` | 0.002 | 0.0025 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_rnd_120apfsds |
| `PD_Vehicles_MBT_AmmoTypes_HE` | `BulletEntityData.Drag` | 0.004 | 0.0043 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_rnd_120hemp |
| `PD_Vehicles_MBT_AmmoTypes_HE` | `…Explosion.ExplosionEntityData.BlastRadius` | 5.0 | 6.0 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_rnd_120hemp |
| `PD_Vehicles_MBT_AmmoTypes_HE` | `…Explosion.ExplosionEntityData.InnerBlastRadius` | 2.25 | 2.3 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_rnd_120hemp |
| `PD_Vehicles_MBT_AmmoTypes_HE` | `…Explosion.ExplosionEntityData.MinimumBlastDamage` | 20.0 | 17.129999 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_rnd_120hemp |
| `PD_Vehicles_MBT_AmmoTypes_MPAT` | `BulletEntityData.Drag` | 0.004 | 0.00425 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_rnd_120heat |
| `PD_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | `BulletEntityData.Drag` | 0.0035 | 0.002 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_coaxhmg |
| `PD_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | `…TimeToLive` | 1.5 | 4.0 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_coaxhmg |
| `PD_Vehicles_RWS_LMG` | `…TimeToLive` | 1.5 | 4.0 | veh_sur_bradley, veh_sur_leoa4, veh_sur_ltv… |
| `PD_Vehicles_Stationary_AntiAir` | `BulletEntityData.EndDamage` | 22.0 | 34.0 | station_aa_gdf009 |
| `PD_Vehicles_Stationary_AntiAir` | `…TimeToLive` | 1.2 | 1.32 | station_aa_gdf009 |
| `PD_Vehicles_Stationary_AntiAir` | `BulletEntityData.StartDamage` | 30.0 | 34.0 | station_aa_gdf009 |
| `PRJ_Missile_Hydra70` | `MissileEntityData.Damage` | 15.0 | 12.0 | gad_callin_airstrike, veh_air_f39e, veh_air_f61v… |
| `SupplyPouch_WB` | `WeaponEntityData.WeaponFiring.PrimaryFire.Ammo.AutoReplenishMagazine` | True | False | gad_sup_pouch |
| `SupplyPouch_WB` | `WeaponEntityData.WeaponFiring.PrimaryFire.Ammo.AutoReplenishRounds` | -1 | 1 | gad_sup_pouch |
| `SupplyPouch_WB` | `WeaponEntityData.WeaponFiring.PrimaryFire.Ammo.MagazineCapacity` | 1 | 3 | gad_sup_pouch |
| `SupplyPouch_WB` | `WeaponEntityData.WeaponFiring.PrimaryFire.Ammo.NumberOfMagazines` | 3 | 1 | gad_sup_pouch |
| `SupplyPouch_WB` | `WeaponEntityData.WeaponFiring.PrimaryFire.FireLogic.ReloadInfoArray[0].ReloadTime` | 0.0 | 1.0 | gad_sup_pouch |
| `WF_Vehicles_AA_PrimaryWeapon_AAAP` | `PrimaryFire.Ammo.MagazineCapacity` | 8 | 4 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `WF_Vehicles_AA_PrimaryWeapon_AAAP` | `PrimaryFire.Ammo.NumberOfMagazines` | 16 | 32 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `WF_Vehicles_AA_PrimaryWeapon_AAAP` | `PrimaryFire.FireLogic.BurstsPerMinute` | 90.0 | 0.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `WF_Vehicles_AA_PrimaryWeapon_AAAP` | `PrimaryFire.FireLogic.RateOfFire` | 240.0 | 480.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `WF_Vehicles_AA_PrimaryWeapon_AAAP` | `PrimaryFire.FireLogic.RateOfFireForBurst` | 240.0 | 480.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `WF_Vehicles_AA_PrimaryWeapon_AAAP` | `PrimaryFire.FireLogic.ReloadInfoArray[0].ReloadTime` | 2.4 | 1.2 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `WF_Vehicles_AA_PrimaryWeapon_AAAP` | `PrimaryFire.Shot.InitialSpeed.z` | 560.0 | 900.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aamp |
| `WF_Vehicles_AA_PrimaryWeapon_AAGP` | `PrimaryFire.Shot.InitialSpeed.z` | 850.0 | 1175.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aaap |
| `WF_Vehicles_AA_PrimaryWeapon_AAHV` | `PrimaryFire.OverHeat.HeatDropPerSecond` | 0.5 | 0.833333 | veh_sur_cheetah1a2, vehec_wp_rnd_35aahv |
| `WF_Vehicles_AA_PrimaryWeapon_AAHV` | `PrimaryFire.OverHeat.HeatPerBullet` | 0.036 | 0.13 | veh_sur_cheetah1a2, vehec_wp_rnd_35aahv |
| `WF_Vehicles_AA_PrimaryWeapon_AAHV` | `PrimaryFire.Shot.InitialSpeed.z` | 1175.0 | 1250.0 | veh_sur_cheetah1a2, vehec_wp_rnd_35aahv |
| `WF_Vehicles_IFV_SecondaryWeapon_TOW` | `PrimaryFire.Shot.InitialSpeed.z` | 50.0 | 76.0 | veh_sur_bradley, veh_sur_strf09a4, vehec_wp_m41a7tow |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | `PrimaryFire.FireLogic.RateOfFire` | 360.0 | 449.998993 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_coaxhmg |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | `PrimaryFire.FireLogic.RateOfFireForBurst` | 360.0 | 449.998993 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_coaxhmg |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | `PrimaryFire.OverHeat.HeatPerBullet` | 0.05 | 0.0392 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_coaxhmg |
| `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG` | `PrimaryFire.Shot.DamagePenetrationMultiplierIndex` | 6 | 8 | veh_sur_leoa4, veh_sur_m1a2sepv3, vehec_wp_coaxhmg |
| `WF_Vehicles_RWS_HMG` | `PrimaryFire.FireLogic.RateOfFire` | 400.0 | 449.998993 | veh_sur_bradley, veh_sur_leoa4, veh_sur_ltv… |
| `WF_Vehicles_RWS_HMG` | `PrimaryFire.FireLogic.RateOfFireForBurst` | 400.0 | 449.998993 | veh_sur_bradley, veh_sur_leoa4, veh_sur_ltv… |
| `WF_Vehicles_RWS_HMG` | `PrimaryFire.Shot.DamagePenetrationMultiplierIndex` | 6 | 8 | veh_sur_bradley, veh_sur_leoa4, veh_sur_ltv… |
| `WF_Vehicles_ScoutHeli_SecondaryWeapon_LightRockets` | `Ammo.AutoReplenishDelay` | 28.0 | 38.0 | veh_air_ah6litbird, vehec_wp_70ffar |
| `WF_Vehicles_Stationary_AntiAir` | `PrimaryFire.FireLogic.RateOfFire` | 720.0 | 1100.0 | station_aa_gdf009 |
| `WF_Vehicles_Stationary_AntiAir` | `PrimaryFire.FireLogic.RateOfFireForBurst` | 720.0 | 1100.0 | station_aa_gdf009 |
| `WF_Vehicles_Stationary_AntiAir` | `PrimaryFire.OverHeat.HeatDropPerSecond` | 0.5 | 1.0 | station_aa_gdf009 |
| `WF_Vehicles_Stationary_AntiAir` | `PrimaryFire.OverHeat.HeatPerBullet` | 0.042 | 0.084 | station_aa_gdf009 |
| `WF_Vehicles_Stationary_TOW` | `PrimaryFire.Shot.InitialSpeed.z` | 50.0 | 76.0 | station_at_m41a7tow, vehec_wp_m41a7tow |

## Table: asset (own) values that changed or were newly reached

| Asset | Property | Old | New | Roster entries |
| --- | --- | --- | --- | --- |
| `PB_Missile_TOW2B` | InnerBlastRadius | 1.0 | 2.0 | gad_surv_crows, station_at_m41a7tow, veh_sur_bradley |
| `PB_Missile_TOW2B_SP` | InnerBlastRadius | 1.0 | 2.0 | station_at_m41a7tow, vehec_wp_m41a7tow |
| `PB_PRJ_PTKM1R_EFP` | BlastDamage | 160.0 | 142.0 | gad_mine_mosen |
| `WF_Vehicles_Stationary_TOW` | BlastDamage | (not reached) | 0.0 | station_at_m41a7tow, vehec_wp_m41a7tow |
| `WF_Vehicles_Stationary_TOW` | BlastRadius | (not reached) | 5.0 | station_at_m41a7tow, vehec_wp_m41a7tow |
| `WF_Vehicles_Stationary_TOW` | InnerBlastRadius | (not reached) | 1.0 | station_at_m41a7tow, vehec_wp_m41a7tow |
| `WF_Vehicles_Stationary_TOW` | ShockwaveDamage | (not reached) | 0.0 | station_at_m41a7tow, vehec_wp_m41a7tow |
| `WF_Vehicles_Stationary_TOW` | ShockwaveRadius | (not reached) | 7.0 | station_at_m41a7tow, vehec_wp_m41a7tow |
| `Gadget_SupplyCrate_WB` | InitialSpeed | (not reached) | 350.0 | gad_sup_bag |
| `Gadget_SupplyCrate_WB` | TimeToLive | (not reached) | 30.0 | gad_sup_bag |

Removed registry rows: the four `Passives_Vehicles_*_Regeneration_*` rows above. Added registry rows (56 owner-named IGLA rows) are in `diff-dedup.json` (`regAdded`).

## Not examined

- The three underbarrel launcher GUID lists changed; they have no defining object, so the pass records nothing for them. Not followed up.
- The hand tables `roster-registry-name-joins.json` and `roster-display-names.json` were not edited. The Field Maintenance join and the new IGLA owner names need review before this run is treated as the new baseline.
- No in-game test was run; units and runtime use are unchanged from L3307's open questions 1 to 12. Question 1 (registry or own value) gains the matches above; question 5 (passive upgrade sizes) gains the regeneration rows.
- `reference-data/frosty/roster-values.json`, `ROSTER_VALUES.md` and the topic pages are not regenerated; the new output stays in the run folder.
