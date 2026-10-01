# Vehicles and gadgets: Frosty research summary

Research snapshot: 1 October 2026. This document uses the approved description, field-value, interpretation, findings, and remaining-limits format.

## Scope and evidence

The vehicle list covers all 38 blueprint families, plus the five separately reviewed vehicle-role candidates. The gadget list covers all 121 research groups: 56 classified as multiplayer equipment under the approved text-based coverage rule, six shared systems, one single-player or mode item, and 58 unresolved groups. A coverage classification is not proof of an active multiplayer blueprint. Additional UI records that have no group association are listed separately so their descriptions are not lost.

These are saved source facts and stated game descriptions. They are not new in-game measurements. Most vehicle and gadget captures retain Head 4892087 (1.4.3.1), descriptor SHA-256 `99b49cfd8bdb5bb6f0181df8ac0d93a0396c1b7f07a1ba3ce8ca1cea45969640`. Later work uses 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. Profile carry-forward statements use the saved hash checks; an older receipt is not relabeled as a fresh measurement.

Historical M26/M320 underbarrel receipts retain release Head 4892017 and descriptor `91c9ea7c3dd830e34a78123c8bb7485e80eefdb18fc9c7ee41117971d23565c2`. Their ordinary M4A1 selections are separate from later hotfix gadget owners. A historical field name is not transferred to a different hotfix owner merely because the item name matches. The current APHEI wording also has no proved text-to-weapon owner join, so no APHEI damage or family assignment is added.

Readable field names below come from reviewed mappings or exact schema matches to known weapon controls. This remains schema inference when the target has no own naming wrapper. Values are rounded to eight significant digits for readability; the source register identifies the full-precision files. Negative values such as -1 retain their special-value meaning as unresolved. A stored zero or missing curve does not prove that the whole item has no effect.

A firing configuration can exist for a tool, scanner, designator, or deployable. Its RateOfFire and MagazineCapacity do not by themselves establish shots per minute or carried uses. Reload entries are listed separately; they are not summed into a gameplay reload time. Launch vectors, gravity, and drag do not establish guided flight or effective velocity. Blast and damage curves do not establish target-specific final damage. Season 5 durability and named AA/scout/mine changes remain version-sensitive.

Descriptions marked as saved game text are supporting UI associations. Exact UI-to-gameplay joins remain unproved. Descriptions based on source roles are labeled accordingly. Unknown descriptions and stats are stated explicitly.

Only this Markdown document is being published. Some cited receipts and detailed profiles are still local research files. Their names, local source locations, and SHA-256 hashes are retained in the source register; this document does not imply that those files are already available on GitHub.

## Contents

- [Vehicles](#vehicles)
- [Separate vehicle-role candidates](#separate-vehicle-role-candidates)
- [Gadgets classified as multiplayer equipment](#gadgets-classified-as-multiplayer-equipment)
- [Shared gadget systems](#shared-gadget-systems)
- [Single-player or mode-specific gadget groups](#single-player-or-mode-specific-gadget-groups)
- [Gadget groups with unresolved availability](#gadget-groups-with-unresolved-availability)
- [Additional UI records without a group association](#additional-ui-records-without-a-group-association)
- [Source register](#source-register)

## Vehicles

### F14 — vehicle

**Research identity:** `airplane/f14`. Exact root variants: `VB_VEH_Airplane_F14`.

**Description (source-role summary):** Aircraft source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_Airplane_Passenger_PrimaryWeapon_SemiActiveRadarMissile:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 0 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 7.5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_PrimaryWeapon_Cannon:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 1100 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 10 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_NavalFighter_PrimaryWeapon_AIM54:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 150 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 0 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Airplane_F14`; raw SHA-256 `68664b0e99e1944cd2c6df8bb1efefb97f49f715caac84173ac85853ed01b065`; profile `l3008-result-v2-authoritative.json` /rows/0/variants/0.
**Sources:** `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### F16 — vehicle

**Research identity:** `airplane/f16`. Exact root variants: `VB_VEH_Airplane_F16`.

**Description (source-role summary):** Aircraft source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_Airplane_PrimaryWeapon_Cannon:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 1100 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_Bomb_Mk82AIR:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 0 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 30 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_SecondaryWeapon_AirToGroundMissile:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 18 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 40 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 15 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_SecondaryWeapon_LightRockets:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 7 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 360 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 14 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Airplane_F16`; raw SHA-256 `7d99e0abbba5a58ecf7025cc33841e9662ae620fa1bfc02718ecfdb7145971c0`; profile `l3007-result-v2.json` /rows/1.
**Sources:** `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-09-29-L3007-vehicle-air-pilot-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### F22 — vehicle

**Research identity:** `airplane/f22`. Exact root variants: `VB_VEH_Airplane_F22`.

**Description (source-role summary):** Aircraft source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_Airplane_PrimaryWeapon_Cannon:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 1100 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 10 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_Bomb_GBU39:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 0 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Airplane_F22`; raw SHA-256 `52f193e63997466a8a55133b80d7dcecab52f6dcefc390cf1c5568cc0ac2097c`; profile `l3008-result-v2-authoritative.json` /rows/1/variants/0.
**Sources:** `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### FA18F — vehicle

**Research identity:** `airplane/fa18f`. Exact root variants: `VB_VEH_Airplane_FA18F`.

**Description (source-role summary):** Aircraft source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_Airplane_Passenger_PrimaryWeapon_SemiActiveRadarMissile:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 0 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 7.5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_PrimaryWeapon_Cannon:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 1100 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 10 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_Bomb_BunkerBuster:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 0 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 10 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_Bomb_Rockeye:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 0 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 30 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_SecondaryWeapon_AntiRadiationMissile:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 40 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 10 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_TVMissile:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 18 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 5 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_MultirolePlane_PrimaryWeapon_ZuniRockets:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 4 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 360 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 2 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Airplane_FA18F`; raw SHA-256 `5e6a8b69fedc76ca5515841122af7114febbff29148453bbfd9ef9c2bca757c4`; profile `l3008-result-v2-authoritative.json` /rows/2/variants/0.
**Sources:** `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-10-01-L643-weapon-shape-profiles.json`, `frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### JAS39 — vehicle

**Research identity:** `airplane/jas39`. Exact root variants: `VB_VEH_Airplane_JAS39`, `VB_VEH_SP_Assault_Airplane_JAS39`.

**Description (source-role summary):** Aircraft source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_Airplane_PrimaryWeapon_Cannon:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 1100 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_Bomb_Mk82AIR:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 0 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 30 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_SecondaryWeapon_AirToGroundMissile:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 18 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 40 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 15 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_SecondaryWeapon_LightRockets:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 7 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 360 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 14 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 2 exact blueprint roots have a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Airplane_JAS39`; raw SHA-256 `99328b8f81bb70ed0de0189f30c69812f2711dde710a40f6a600fef7c17c2787`; profile `l3008-result-v2-authoritative.json` /rows/3/variants/0.
**Root evidence:** `VB_VEH_SP_Assault_Airplane_JAS39`; raw SHA-256 `04f716566ec2020a0b12bf8a5b0186d2148737f12a06393ee3b498aaf903465b`; profile `l3008-result-v2-authoritative.json` /rows/3/variants/1.
**Sources:** `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### MQ9 — vehicle

**Research identity:** `airplane/mq9`. Exact root variants: `VB_VEH_Airplane_MQ9`.

**Description (source-role summary):** Drone aircraft source family. The selected weapon route stops at a deployment wrapper; an exact controlled weapon-owner join remains unresolved.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Airplane_MQ9`; raw SHA-256 `284031c4a199682d3b3a280a3b80edc12cac3560c89868d7eee0572ccd0bc8e9`; profile `l3008-result-v2-authoritative.json` /rows/4/variants/0.
**Sources:** `frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### SU57 — vehicle

**Research identity:** `airplane/su57`. Exact root variants: `VB_VEH_Airplane_SU57`.

**Description (source-role summary):** Aircraft source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_Airplane_PrimaryWeapon_Cannon:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 1100 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_Bomb_GBU39:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 0 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_Airplane_SecondaryWeapon_AirToAirMissile_R73:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 8 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 10 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Airplane_SU57`; raw SHA-256 `4621cb5729b75c4f4ac0af4671cfe6c2f829ff43ea5ecb3eca15e71c0171f044`; profile `l3008-result-v2-authoritative.json` /rows/5/variants/0.
**Sources:** `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-10-01-L643-weapon-shape-profiles.json`, `frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### CB90 — vehicle

**Research identity:** `boat/cb90`. Exact root variants: `VB_VEH_Boat_CB90`.

**Description (source-role summary):** Boat source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 700 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 600] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[20, 35.220001], [75, 20.67]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_Equipment_NavalMines:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 900 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 0 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 86400 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_Equipment_Torped47:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 900 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 10 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 0.5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Airburst:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 80 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 2.5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Guided:8`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 80 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 2.5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_HE:9`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 80 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 2.5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 8 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 7 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Illumination:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_Gunner_PrimaryWeapon_120mmMortar_Smoke:8`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_PrimaryWeapon_GAU19:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | 200 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 100 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_PrimaryWeapon_M230LF:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 8 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_SecondaryWeapon_MistralMissile:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_PatrolBoat_SecondaryWeapon_RBS70:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 6 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Boat_CB90`; raw SHA-256 `2d8e05398f8f3f2b79159a8db1ec5a87d3033ac7c2469d0cb5f3c6c3f6911ad3`; profile `l3009-result-v2.json` /rows/0.
**Sources:** `frosty-2026-10-01-L641-weapon-shape-profiles.json`, `frosty-2026-10-01-L643-weapon-shape-profiles.json`, `frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### JetSki — vehicle

**Research identity:** `boat/jetski`. Exact root variants: `VB_VEH_Boat_JetSki`.

**Description (source-role summary):** Boat source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth / RepairRateModifier` | Unresolved | The actual owner differs from the named control and its selected naming wrapper is null. This does not imply zero health or absent repair. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Boat_JetSki`; raw SHA-256 `8f911f6676c9a701c943e0e955fbfc0ca544ded800d6dc17b6039ed890632518`; profile `l3009-result-v2.json` /rows/1.
**Sources:** `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3024-health-own-wrapper-check.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### RHIB — vehicle

**Research identity:** `boat/rhib`. Exact root variants: `VB_VEH_Boat_RHIB`.

**Description (source-role summary):** Boat source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_OpenGunner_HMG:10`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 500 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 760 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Boat_RHIB`; raw SHA-256 `cc45dacb066f666293c5430404a3cad98321b1e03f20cb6d6ffd68214a27f806`; profile `l3009-result-v2.json` /rows/2.
**Sources:** `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### Couch — vehicle

**Research identity:** `car/couch`. Exact root variants: `VB_VEH_Car_Couch`.

**Description (source-role summary):** Ground vehicle source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Car_Couch`; raw SHA-256 `49d8ebca518738a5dbc801bf89a2d8b2d76e259410e66d8f5c64dd4458e89748`; profile `l3010-result.json` /rows/6.
**Sources:** `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### Flyer60 — vehicle

**Research identity:** `car/flyer60`. Exact root variants: `VB_VEH_Car_Flyer60`, `VB_VEH_Car_Flyer60_SP`.

**Description (source-role summary):** Ground vehicle source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_OpenGunner_HMG:10`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 500 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 760 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 2 exact blueprint roots have a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Car_Flyer60`; raw SHA-256 `afea4a935d8310ae3ee8abf907c7789b57690f7c898c936bcc3e100e6631edb2`; profile `l3010-result.json` /rows/7.
**Root evidence:** `VB_VEH_Car_Flyer60_SP`; raw SHA-256 `d7696533159f8e3e685a550e0c1a9059ebf18bb7f3e585d318930a0af1545a1f`; profile `l3010-result.json` /rows/7/functionalVariants/0.
**Sources:** `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### JLTV — vehicle

**Research identity:** `car/jltv`. Exact root variants: `VB_VEH_Car_JLTV`.

**Description (source-role summary):** Ground vehicle source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 800 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_RWS_AGL:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 325 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 5 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 1.27, 100] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.003 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 10 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_LMG:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 720 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 600] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[20, 35.220001], [75, 20.67]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_HMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 400 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 760] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[25, 52.400002], [75, 27.299999]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Car_JLTV`; raw SHA-256 `13f64f0252f34050910d1aedca17cf9a45c8ff1d621c878e6188dca7867ee729`; profile `l3010-result.json` /rows/8.
**Sources:** `frosty-2026-10-01-L641-weapon-shape-profiles.json`, `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### Marauder — vehicle

**Research identity:** `car/marauder`. Exact root variants: `VB_VEH_Car_Marauder`.

**Description (source-role summary):** Ground vehicle source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 800 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_RWS_AGL:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 325 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 5 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 1.27, 100] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.003 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 10 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_LMG:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 720 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 600] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[20, 35.220001], [75, 20.67]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_HMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 400 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 760] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[25, 52.400002], [75, 27.299999]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Car_Marauder`; raw SHA-256 `02231651f7cb25c9242e0bd1313355f60edeefe993be590276d0ca3f5bdc9804`; profile `l3010-result.json` /rows/9.
**Sources:** `frosty-2026-10-01-L641-weapon-shape-profiles.json`, `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### PTV — vehicle

**Research identity:** `car/ptv`. Exact root variants: `VB_VEH_Car_PTV`.

**Description (source-role summary):** Ground vehicle source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Car_PTV`; raw SHA-256 `3e49923df3ea6273002d468cbbaef3ffd76fd8012e616a977bb8473c5bfb9bd9`; profile `l3010-result.json` /rows/10.
**Sources:** `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### QuadBike — vehicle

**Research identity:** `car/quadbike`. Exact root variants: `VB_VEH_Car_QuadBike`.

**Description (source-role summary):** Ground vehicle source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Car_QuadBike`; raw SHA-256 `0124300b03c73bf58ba642ce7a0914d8471f71ab4d7ec896d2c7ab8db581873f`; profile `l3010-result.json` /rows/11.
**Sources:** `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### TheBeast — vehicle

**Research identity:** `car/thebeast`. Exact root variants: `VB_VEH_Car_TheBeast`.

**Description (source-role summary):** Ground vehicle source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth / RepairRateModifier` | Unresolved | The actual owner differs from the named control and its selected naming wrapper is null. This does not imply zero health or absent repair. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Car_TheBeast`; raw SHA-256 `6f344d9f8fd7f43adbbaffef62183d640e072addff58f58af86ecebd9838c8d7`; profile `l3010-result.json` /rows/12.
**Sources:** `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3024-health-own-wrapper-check.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### Vector — vehicle

**Research identity:** `car/vector`. Exact root variants: `VB_VEH_Car_Vector`, `VB_VEH_Car_Vector_M05_CarChase`.

**Description (source-role summary):** Ground vehicle source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_OpenGunner_HMG:10`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 500 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 760 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 2 exact blueprint roots have a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Car_Vector`; raw SHA-256 `f3a1dad4b5a20f602f6a3392a4a9397394c95c0aea18e62bf47e7bf86dffe665`; profile `l3010-result.json` /rows/13.
**Root evidence:** `VB_VEH_Car_Vector_M05_CarChase`; raw SHA-256 `450a2d938d471b03c42cb350a8f9ca86cfd28739a21533535c4c676a27e5cffa`; profile `l3010-result.json` /rows/13/functionalVariants/0.
**Sources:** `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### TRV150 — vehicle

**Research identity:** `drone/trv150`. Exact root variants: `VB_VEH_Drone_TRV150`.

**Description (source-role summary):** Drone source family. The separately reviewed spectator-support role must remain separate from player-controlled equipment.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 100 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Drone_TRV150`; raw SHA-256 `c5cad6cd88ff78aac29a187551acc38e29a94822f5e167b38980490f869bee76`; profile `l3009-result-v2.json` /rows/9.
**Sources:** `frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### AH64E — vehicle

**Research identity:** `helicopter/ah64e`. Exact root variants: `VB_VEH_Helicopter_AH64E`.

**Description (source-role summary):** Helicopter source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_AttackHeli_Passenger_PrimaryWeapon_Chaingun:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 625 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 805 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0024999999 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 1.2 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 8 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_Passenger_SecondaryWeapon_LockingMissile:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 18 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_PrimaryWeapon_HeavyRockets:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 4 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 360 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 2 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_PrimaryWeapon_LightRockets:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 360 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 2 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 18 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_PrimaryWeapon_SmartRockets:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 7 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 180 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 2 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 14 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_SecondaryWeapon_AirToAirMissile:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 8 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 10 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_SecondaryWeapon_TOW:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 18 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 50 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Helicopter_AH64E`; raw SHA-256 `371300af99eab2e9b4bef53cec964bdf7edbcb0ef55c6c426eb963c72c2fa555`; profile `l3007-result-v2.json` /rows/0.
**Sources:** `frosty-2026-10-01-L643-weapon-shape-profiles.json`, `frosty-2026-09-29-L3007-vehicle-air-pilot-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### AH6M — vehicle

**Research identity:** `helicopter/ah6m`. Exact root variants: `VB_VEH_Helicopter_AH6M`, `VB_VEH_Helicopter_AH6M_M05_SP_Cine`, `VB_VEH_Helicopter_SP_MH6M`.

**Description (source-role summary):** Helicopter source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 700 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_RWS_TargetDesignator:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 350] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_ScoutHeli_Passenger_PrimaryWeapon_ThermalScanner:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 3600 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 350 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_ScoutHeli_Passenger_SecondaryWeapon_DirectionalJammer:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 360 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 350 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_ScoutHeli_PrimaryWeapon_GAU19:9`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 800 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 100 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 860 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | 200 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_ScoutHeli_PrimaryWeapon_LR30:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 250 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 6 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 265 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0024999999 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_ScoutHeli_PrimaryWeapon_Minigun:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1800 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 100 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 700 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | 200 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_ScoutHeli_SecondaryWeapon_AirToAirMissile:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 10 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_ScoutHeli_SecondaryWeapon_Hellfire:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 18 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 40 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_ScoutHeli_SecondaryWeapon_LightRockets:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 7 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 360 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 21 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_ScoutHeli_SecondaryWeapon_SmartRockets:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 4 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 360 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 3 exact blueprint roots have a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Helicopter_AH6M`; raw SHA-256 `ed3c587a39bf7421e5479e85efb96c5df4dbcc588810d651a0b83e1b9375d098`; profile `l3008-result-v2-authoritative.json` /rows/6/variants/0.
**Root evidence:** `VB_VEH_Helicopter_AH6M_M05_SP_Cine`; raw SHA-256 `106354665d9d738edf5acaa14e37485bf0ffa0b24e01a7d3ccbb7eacdeb6c307`; profile `l3008-result-v2-authoritative.json` /rows/6/variants/1.
**Root evidence:** `VB_VEH_Helicopter_SP_MH6M`; raw SHA-256 `8f517ad3d4dfa294edb22a02407349899bc2da10d142ed0f1327ca2e52ddfac8`; profile `l3008-result-v2-authoritative.json` /rows/6/variants/2.
**Sources:** `frosty-2026-10-01-L641-weapon-shape-profiles.json`, `frosty-2026-10-01-L650-aa-scout-preupdate-baseline.json`, `frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### Eurocopter — vehicle

**Research identity:** `helicopter/eurocopter`. Exact root variants: `VB_VEH_Helicopter_Eurocopter`, `VB_VEH_Helicopter_Eurocopter_SP`.

**Description (source-role summary):** Helicopter source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_AttackHeli_Passenger_PrimaryWeapon_Chaingun:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 625 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 805 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0024999999 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 1.2 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 8 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_Passenger_SecondaryWeapon_LockingMissile:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 18 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_PrimaryWeapon_HeavyRockets:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 4 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 360 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 2 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_PrimaryWeapon_LightRockets:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 360 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 2 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 18 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_PrimaryWeapon_SmartRockets:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 7 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 180 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 2 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 14 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_SecondaryWeapon_AirToAirMissile:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 8 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 10 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AttackHeli_SecondaryWeapon_TOW:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 18 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 50 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `ReloadTime` | 5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 2 exact blueprint roots have a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Helicopter_Eurocopter`; raw SHA-256 `d4b4cc97f3d4c9fd9ddcea5a49cd10d177b0f1c840c8b947ef13d3cb6a010445`; profile `l3008-result-v2-authoritative.json` /rows/7/variants/0.
**Root evidence:** `VB_VEH_Helicopter_Eurocopter_SP`; raw SHA-256 `fa2fb8b5c69bd73ec748dd6328f2af256f6c556a6244ef0493022d65f71cf007`; profile `l3008-result-v2-authoritative.json` /rows/7/variants/1.
**Sources:** `frosty-2026-10-01-L643-weapon-shape-profiles.json`, `frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### MH47 — vehicle

**Research identity:** `helicopter/mh47`. Exact root variants: `VB_VEH_Helicopter_MH47_Insertion`, `VB_VEH_Helicopter_MH47_SP`.

**Description (source-role summary):** Transport-helicopter source family. Its polymorphic component layout does not prove absent weapons.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 2 exact blueprint roots have a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Helicopter_MH47_Insertion`; raw SHA-256 `2283aa479c1c9942788e2fbbef21e51412e97b21540db299921b857e5d1e9e4b`; profile `l3008-result-v2-authoritative.json` /rows/9/variants/0.
**Root evidence:** `VB_VEH_Helicopter_MH47_SP`; raw SHA-256 `d29abee576574ee192f2487f9101f1863a6cc6486496035ed9af316cf08dc240`; profile `l3008-result-v2-authoritative.json` /rows/9/variants/1.
**Sources:** `frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### UH60 — vehicle

**Research identity:** `helicopter/uh60`. Exact root variants: `VB_VEH_Helicopter_UH60`.

**Description (source-role summary):** Helicopter source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1500 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_TransportHeli_Gunner_Minigun:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | 200 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 100 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Helicopter_UH60`; raw SHA-256 `e82e813cba78d36ba89d859aae18f3bc34e0f0f727f2312d0e51fa0a30c54d97`; profile `l3008-result-v2-authoritative.json` /rows/8/variants/0.
**Sources:** `frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### DirtBike01 — vehicle

**Research identity:** `motorcycle/dirtbike01`. Exact root variants: `VB_VEH_Motorcycle_DirtBike01`.

**Description (source-role summary):** Motorcycle source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Motorcycle_DirtBike01`; raw SHA-256 `19ad25b50818a33f4effb26f4f1fa47c00727932f5f168f97e37866bbafbdfc2`; profile `l3010-result.json` /rows/14.
**Sources:** `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### DirtBike02 — vehicle

**Research identity:** `motorcycle/dirtbike02`. Exact root variants: `VB_VEH_Motorcycle_DirtBike02`.

**Description (source-role summary):** Motorcycle source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Motorcycle_DirtBike02`; raw SHA-256 `9d391833c249600fc40c5db6b863be7042e4d542e7f0468b08c8035ff2b87342`; profile `l3010-result.json` /rows/15.
**Sources:** `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### BGM71 TOW — vehicle

**Research identity:** `stationary/bgm71tow`. Exact root variants: `VB_VEH_Stationary_BGM71TOW`.

**Description (source-role summary):** Stationary weapon source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 150 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_Stationary_TOW:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Stationary_BGM71TOW`; raw SHA-256 `79a593c9ae9bee42fe3059b1faa29e424bff044f83fca552f6b4886b138727a2`; profile `l3009-result-v2.json` /rows/3.
**Sources:** `frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### CWS / CROWS — vehicle

**Research identity:** `stationary/cws`. Exact root variants: `VB_VEH_Stationary_Turret_CROWS`.

**Description (source-role summary):** Stationary weapon source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 300 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_127_CWSCROWS_HMG:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 150 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_CWSCROWS_Spike:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 10 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_CWS_AGL:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | 30 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Stationary_Turret_CROWS`; raw SHA-256 `995550c5c0ac690e9ddbab3a46cfb8c66591fcf22aa2739f7787f1675d240f8f`; profile `l3009-result-v2.json` /rows/4.
**Sources:** `frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### GDF009 — vehicle

**Research identity:** `stationary/gdf009`. Exact root variants: `VB_VEH_Stationary_GDF009`.

**Description (source-role summary):** Stationary weapon source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_Stationary_AntiAir:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 720 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 1175 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0024999999 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `AutoReplenishDelay` | 8 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Stationary_GDF009`; raw SHA-256 `97bc54bf61f1521b82b657c6b566bce74cb6155ed82702e30432158879c3f71f`; profile `l3009-result-v2.json` /rows/5.
**Sources:** `frosty-2026-10-01-L650-aa-scout-preupdate-baseline.json`, `frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### M2MG — vehicle

**Research identity:** `stationary/m2mg`. Exact root variants: `VB_VEH_Stationary_M2MG`.

**Description (source-role summary):** Stationary weapon source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 150 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_OpenGunner_HMG:10`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 500 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 760 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Stationary_M2MG`; raw SHA-256 `e902fe4daf0e42f2b925d644731812a47caede44e1f482e61fd92cb601634bdf`; profile `l3009-result-v2.json` /rows/6.
**Sources:** `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### Phalanx — vehicle

**Research identity:** `stationary/phalanx`. Exact root variants: `VB_VEH_Stationary_Phalanx`, `VB_VEH_Stationary_Phalanx_SP`.

**Description (source-role summary):** Stationary weapon source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_SAA_PrimaryWeapon_20mmRotaryCannon:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 2 exact blueprint roots have a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Stationary_Phalanx`; raw SHA-256 `87704f8646870a651d66681d89949163277d6b6c0ccc424f0a4207761dcdf401`; profile `l3009-result-v2.json` /rows/7.
**Root evidence:** `VB_VEH_Stationary_Phalanx_SP`; raw SHA-256 `8d52dc854ca6ef63aef290271b981bcd4a9bba6342b09566149499a22fef36a5`; profile `l3009-result-v2.json` /rows/7/continuationSources/variants/0.
**Sources:** `frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### SSM Battery — vehicle

**Research identity:** `stationary/ssmbattery`. Exact root variants: `VB_VEH_Stationary_SSMBattery`.

**Description (source-role summary):** Stationary weapon source family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_SSMBattery_SecondaryWeapon_AntiAirMissile:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 10 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Stationary_SSMBattery`; raw SHA-256 `e1d2e74eab998ec75a6a58a74e5c4fb2d88339bc6fca529ffc402ef8907319ac`; profile `l3009-result-v2.json` /rows/8.
**Sources:** `frosty-2026-10-01-L650-aa-scout-preupdate-baseline.json`, `frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### AAV7A1 — vehicle

**Research identity:** `tank/aav7a1`. Exact root variants: `VB_VEH_Tank_AAV7A1`.

**Description (source-role summary):** Armored transport or fighting-vehicle source family with selected turret and secondary-weapon configurations.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth / RepairRateModifier` | Unresolved | The actual owner differs from the named control and its selected naming wrapper is null. This does not imply zero health or absent repair. |

**Weapon stats:** No exact controlled firing profile is assigned to this family in the saved profile list. This does not establish absent armament.

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Tank_AAV7A1`; raw SHA-256 `9912c341bb80f992e104cc364f737e3d7b64943d6c423509581e7d2e1a3b5c71`; profile `l3010-result.json` /rows/0.
**Sources:** `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3024-health-own-wrapper-check.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### Abrams — vehicle

**Research identity:** `tank/abrams`. Exact root variants: `VB_VEH_Tank_Abrams`.

**Description (source-role summary):** Main battle tank source family with selected cannon, coaxial machine-gun, and remote weapon-station configurations.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1200 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 700 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 600] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[20, 35.220001], [75, 20.67]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 360 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 760] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[25, 52.400002], [75, 27.299999]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_AGL:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 325 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 5 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 1.27, 100] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.003 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 10 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_LMG:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 720 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 600] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[20, 35.220001], [75, 20.67]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_HMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 400 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 760] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[25, 52.400002], [75, 27.299999]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_MBT_PrimaryWeapon_120mm:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 900 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 560] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 4.0999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 14 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 20 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Tank_Abrams`; raw SHA-256 `e65f368eb95aebd9ec21cbc6728830acaac54589324582dd9516d3f7a70ed672`; profile `l3010-result.json` /rows/1.
**Sources:** `frosty-2026-10-01-L641-weapon-shape-profiles.json`, `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### Bradley — vehicle

**Research identity:** `tank/bradley`. Exact root variants: `VB_VEH_Tank_Bradley`.

**Description (source-role summary):** Armored transport or fighting-vehicle source family with selected turret and secondary-weapon configurations.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_RWS_AGL:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 325 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 5 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 1.27, 100] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.003 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 10 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_LMG:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 720 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 600] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[20, 35.220001], [75, 20.67]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_HMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 400 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 760] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[25, 52.400002], [75, 27.299999]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_SecondaryWeapon_HomingATGM:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 150 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 80] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 9.5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 6 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_PrimaryWeapon_Canister:9`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 700] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.003 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 2.4000001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 20 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_SecondaryWeapon_LightRockets:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 120] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -4.9050002 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 0 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 2 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_PrimaryWeapon_APFSDST:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 375] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 2.4000001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 20 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_TargetDesignator:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 350] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_SecondaryWeapon_TOW:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 150 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 50] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 8.1999998 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 6 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_PrimaryWeapon_HEAB:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 250] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0020000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 2.4000001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 20 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Tank_Bradley`; raw SHA-256 `7d42a906aebe89d73fa0bb3ed1ab38df5c1dc5bbf8770fa230c88adf1a5a9d64`; profile `l3010-result.json` /rows/2.
**Sources:** `frosty-2026-10-01-L641-weapon-shape-profiles.json`, `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### CV90 — vehicle

**Research identity:** `tank/cv90`. Exact root variants: `VB_VEH_Tank_CV90`.

**Description (source-role summary):** Armored transport or fighting-vehicle source family with selected turret and secondary-weapon configurations.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_RWS_AGL:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 325 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 5 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 1.27, 100] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.003 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 10 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_LMG:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 720 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 600] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[20, 35.220001], [75, 20.67]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_HMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 400 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 760] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[25, 52.400002], [75, 27.299999]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_SecondaryWeapon_HomingATGM:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 150 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 80] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 9.5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 6 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_PrimaryWeapon_Canister:9`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 700] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.003 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 2.4000001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 20 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_SecondaryWeapon_LightRockets:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 120] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -4.9050002 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 0 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 2 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 4 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_PrimaryWeapon_APFSDST:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 375] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 2.4000001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 20 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_TargetDesignator:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 350] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_SecondaryWeapon_TOW:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 150 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 50] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 8.1999998 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 6 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_IFV_PrimaryWeapon_HEAB:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 200 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 12 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 250] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0020000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 2.4000001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 20 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 20 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Tank_CV90`; raw SHA-256 `a39ff8309493fb4e625c098809891a8f8fbfd950c329afa7b7079211e3e514a4`; profile `l3010-result.json` /rows/3.
**Sources:** `frosty-2026-10-01-L641-weapon-shape-profiles.json`, `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### Gepard — vehicle

**Research identity:** `tank/gepard`. Exact root variants: `VB_VEH_Tank_Gepard`.

**Description (source-role summary):** Anti-air vehicle source family. Cheetah is reviewed as a customization alias, rather than a separate blueprint family.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1000 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_AA_PrimaryWeapon_AAGP:2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 600 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 6 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 850] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0024999999 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 1.2 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 8 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 28 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AA_PrimaryWeapon_AAAP:6`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 240 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 8 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 560] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0024999999 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 2.4000001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 8 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 16 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AA_SecondaryWeapon_AimGuidedMissile:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 50 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AA_PrimaryWeapon_AAHV:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 720 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 1175 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0024999999 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `AutoReplenishDelay` | 8 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AA_SecondaryWeapon_HighVelocityMissile:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 60 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 4 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 117.5 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_AA_SecondaryWeapon_AntiAirMissile:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 120 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 2 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed.z` | 20 | Configured z component of the launch vector; this does not establish measured flight speed. |
| `AutoReplenishDelay` | 16 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Tank_Gepard`; raw SHA-256 `8cb03f795a1518a6a92a70a348e777b1e10eaca2603c99fd04d50552ec0c7f39`; profile `l3010-result.json` /rows/4.
**Sources:** `frosty-2026-10-01-L641-weapon-shape-profiles.json`, `frosty-2026-10-01-L642-weapon-shape-profiles.json`, `frosty-2026-10-01-L650-aa-scout-preupdate-baseline.json`, `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

### Leopard — vehicle

**Research identity:** `tank/leopard`. Exact root variants: `VB_VEH_Tank_Leopard`.

**Description (source-role summary):** Main battle tank source family with selected cannon, coaxial machine-gun, and remote weapon-station configurations.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MaxHealth` | 1200 | Configured base health; effective durability also depends on damage and armor rules. |
| `RepairRateModifier` | 1 | Repair-rate modifier. A value of 1 appears neutral; the underlying repair rate remains unconfirmed. |

**Reviewed weapon configurations:** These are source selections, not a default or simultaneous loadout.

**Profile:** `WF_Vehicles_MBT_SecondaryWeapon_CoaxLMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 700 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 600] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[20, 35.220001], [75, 20.67]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_MBT_SecondaryWeapon_CoaxHMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 360 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 760] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[25, 52.400002], [75, 27.299999]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_AGL:1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 325 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 5 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 1.27, 100] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.003 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 10 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_LMG:5`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 720 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 600] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[20, 35.220001], [75, 20.67]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_RWS_HMG:3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 400 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 760] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Field_edfc6df6 (damage-curve points)` | [[25, 52.400002], [75, 27.299999]] | Stored point pairs [first coordinate, second coordinate] on the selected damage curve. Native interpolation and effective damage remain unconfirmed. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**Profile:** `WF_Vehicles_MBT_PrimaryWeapon_120mm:4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 900 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 560] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 4.0999999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `AutoReplenishDelay` | 14 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 20 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |

**What we know:** 1 exact blueprint root has a reviewed source profile. The health names, where provided, are base-root values; different single-player or cinematic owners must be checked separately. Source entry definitions, equipment references, and motion/input graphs retain structural evidence.

**Still uncertain:** Effective durability and repair rate, target-specific damage, displayed ammunition, native firing/reload timing, countermeasure timing, usable seats, default loadout, speed, acceleration, and handling. UI cards have not been joined to exact family roots, so their seat counts and category descriptions are not assigned here.

**Root evidence:** `VB_VEH_Tank_Leopard`; raw SHA-256 `ca4d6b711fb9846d6239006347c46a8669aa8dbda3e7dd0de486d04f6fc2795c`; profile `l3010-result.json` /rows/5.
**Sources:** `frosty-2026-10-01-L641-weapon-shape-profiles.json`, `frosty-2026-09-29-L3010-vehicle-ground-continuation.json`, `frosty-2026-09-30-L3018-vehicle-stat-map.json`, `frosty-2026-09-30-L3030-vehicle-stage2-closeout.json`, `frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json`, `frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json`.

## Separate vehicle-role candidates

### C17 — reviewed role candidate

**Description (source-role summary):** visual object and associated physics branch.

**Known stats:** No separate player vehicle stat profile is assigned to this candidate.

**What we know:** Exclude inspected model/artwork branch from gameplay vehicle profiles. No blanket per-file cosmetic validation is claimed.

**Still uncertain:** This result applies to the inspected role or branch. It does not prove that every same-name asset is cosmetic or that no other gameplay route exists.

**Source:** `L3006`; identity `airplane/c17`.

### MD530 — reviewed role candidate

**Description (source-role summary):** model definition branch.

**Known stats:** No separate player vehicle stat profile is assigned to this candidate.

**What we know:** Exclude inspected model root and its visual descendants from independent gameplay vehicle profiles.

**Still uncertain:** This result applies to the inspected role or branch. It does not prove that every same-name asset is cosmetic or that no other gameplay route exists.

**Source:** `L3006`; identity `helicopter/md530`.

### Cheetah — reviewed role candidate

**Description (source-role summary):** functional Gepard customization alias with alternate model.

**Known stats:** No separate player vehicle stat profile is assigned to this candidate.

**What we know:** Retain independent functional customization/loadout routes with Gepard. Exclude only the inspected alternate model subtree; do not count a new independent vehicle chassis.

**Still uncertain:** This result applies to the inspected role or branch. It does not prove that every same-name asset is cosmetic or that no other gameplay route exists.

**Source:** `L3006`; identity `tank/cheetah`.

### SignalDecryption_Antenna — reviewed role candidate

**Description (source-role summary):** functional vehicle authored mission objective system.

**Known stats:** No separate player vehicle stat profile is assigned to this candidate.

**What we know:** Retain a separate objective-system coverage row; not artwork and not an ordinary combat-vehicle profile.

**Still uncertain:** This result applies to the inspected role or branch. It does not prove that every same-name asset is cosmetic or that no other gameplay route exists.

**Source:** `L3006`; identity `Game/GlacierGranite/Gamemodes/GM_BattleRoyale/Missions/Mission_DataUpload/VB_VEH_SignalDecryption_Antenna`.

### Abrams_ULR_Prop — reviewed role candidate

**Description (source-role summary):** visual object prop branch.

**Known stats:** No separate player vehicle stat profile is assigned to this candidate.

**What we know:** Exclude inspected prop/model branch from separate gameplay vehicle profiles.

**Still uncertain:** This result applies to the inspected role or branch. It does not prove that every same-name asset is cosmetic or that no other gameplay route exists.

**Source:** `L3006`; identity `Game/GlacierSP/Levels/DSUB_SP_Assault/_Art/VehicleProps/VB_VEH_Tank_Abrams_ULR_Prop`.

## Gadgets classified as multiplayer equipment

### Missile Strike (MISSILE STRIKE) — gadget group

**Research identity:** `callins/jagmstrike`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** STRIKE PACKAGE

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Air Strike and JAGM configurations share targeting equipment. Offered selector entries include both resource choices. Those entries do not establish active deployment or the selected strike payload.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L199-air-jagm-callin-selection.json`.

### VL-7 Strike — gadget group

**Research identity:** `callins/psygas`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** STRIKE PACKAGE

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`.

### Hardware Suppression System (DGMK4) — gadget group

**Research identity:** `intel/lancet`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** When equipped, the Hardware Suppression System spots all nearby electronic and explosive gadgets as well as targets in the middle of a locked-on process. Take aim and activate the device to intercept missiles and destroy electronic gadgets, up to a total of three combined.

**Configuration:** `pbns_lancetexplosion`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 25 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 4 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 7.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The recon weapon source reaches drone deployment and a separate payload-drone branch. A selected payload-bomb profile is distinct from a Lancet explosion candidate. The source also references targeting and state expressions; payload execution, flight, lifetime, and spotting remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L170-drone-payload-source.json`.

### Incendiary Airburst Launcher (Sich G1 WP) — gadget group

**Research identity:** `launchers/airburstincendiary`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Fires incendiary grenades a distance of 25m that explode mid-flight, producing an incendiary cloud that burns enemy targets. The cloud will block visibility and clear and prevent spotting.

**Configuration:** `wb_airburstincendiary`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `RateOfFire` | 100 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadTime` | 2.53 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 2.53 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `Shot.InitialSpeed` | [0, 1.6390001, 100] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 2.53 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 2.53 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |

**Configuration:** `pb_airburstincendiary`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 1 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 3 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 3.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The weapon source selects a projectile and a blast child. Its firing, ammunition, reload, and blast settings were read. Lingering-fire selection and effective burn behavior remain unresolved.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L163-airburst-incendiary-source.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### Active Locking Air-Defense Launcher (9K38 Igla) — gadget group

**Research identity:** `launchers/igla`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A man-portable air-defense system designed to target enemy aircraft. Requires lock-on before launch, after which the user must maintain target acquisition by tracking the aircraft with the weapon sight to preserve missile guidance. Missiles can reacquire targets mid-flight if tracking is lost or countermeasures are deployed.

**Configuration:** `wb_igla`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadTime` | 3.4 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 2.33 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**Configuration:** `pb_ns_igla`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 100 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 7.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The weapon source selects the scoped missile projectile. Stinger and IGLA share stored BlastDamage 100 and BlastRadius 5, but their alternate reload entries differ. Locking, guidance, and final target damage remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L162-stinger-igla-source.json`.

### Long-Range Launcher (MAS 148 Glaive) — gadget group

**Research identity:** `launchers/javelin`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A long-range anti-vehicle missile system. Requires lock-on before launch, after which the missile will engage automatic self-guidance. Capable of faster and longer range lock-ons for ground and air targets that have been marked with the Laser Designator or Tracer Dart.

**Configuration:** `wb_javelin`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadTime` | -1 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 3.5, 10] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadSpeed` | 1.1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |

**Configuration:** `pb_javelin`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 125 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 4 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 6.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The weapon source selects the Javelin projectile and its blast profile. A laser-guided alternative remains a separate candidate and does not inherit these values automatically.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L167-javelin-source.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### Aim-Guided Launcher (M136 AT) — gadget group

**Research identity:** `launchers/m136at4`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** An anti-vehicle launcher that allows the user to guide the missile to the target via the weaponâ€™s crosshairs. Inflicts greater damage on the sides, top, and rear of vehicles where the armor is thinner.

**Configuration:** `wb_at4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadTime` | 3.66 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 3.66 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 0, 30] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 3.6600001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 3.6600001 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |

**Configuration:** `pb_at4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 70 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 2 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 7.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The launcher weapon sources select distinct primary projectiles and blast owners. Ammunition, reload entries, and movement-array values were read. Stored counts and timing do not establish carried ammunition or actual reload time.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L137-launcher-handling-ammunition.json`, `frosty-2026-09-29-L152-launcher-projectile-source.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### Underbarrel Shotgun (M26 MASS) — gadget group

**Research identity:** `launchers/m26mass`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Chambered in 12-gauge buckshot rounds, the M26 is a bolt action close-range shotgun.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`.

### High Explosive Launcher (M320A1 HE) — gadget group

**Research identity:** `launchers/m320he`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Fires impact-triggered grenades designed for damaging structures and targeting infantry behind cover. Can be carried standalone or underslung on weapons with a Gadget Mount attachment for faster access.

**Configuration:** `pb_ns_m320he`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InitialSpeed` | 250 | Speed setting on this particular projectile owner; it is separate from the weapon launch vector. |
| `TimeToLive` | 15 | Projectile lifetime setting; units and actual expiry conditions remain unconfirmed. |
| `BlastDamage` | 120 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `DamageMultiplier` | 1 | Damage multiplier setting; active composition and target-specific final damage remain unconfirmed. |

**Configuration:** `primaryfire_m320`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 100 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 63] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 2.28 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 2.28 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The earlier ordinary underbarrel selection reaches HE and AT payload paths. HE direct blast names were controlled, but radius labels and the additional AT-specific effects remain unresolved.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-26-L71-m320-he-at-source-profile.json`, `frosty-2026-09-26-L75-m320-explosion-naming-limit.json`, `frosty-2026-09-26-L76-m320-he-firing-inputs.json`, `frosty-2026-09-26-L79-m320-explosion-name-limits.json`, `frosty-2026-09-26-L85-m320-shockwave-input.json`, `frosty-2026-09-26-L86-L87-secondary-spread-protection.json`, `frosty-2026-09-26-L86-L87-secondary-spread-protection.json`, `frosty-2026-09-26-L88-m26-m320-configured-ammo-counts.json`, `frosty-2026-09-29-L195-m320-smoke-selection.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Smoke Grenade Launcher (M320A1 SMK) — gadget group

**Research identity:** `launchers/m320smoke`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Fires impact-triggered grenades designed to create temporary smoke screens. Blocks ability to spot targets and clears spotted markers from all infantry inside the smoke radius. Can be carried standalone or underslung on weapons with a Gadget Mount attachment for faster access.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Equipment, ability, and customization sources reach the shared M320 weapon and smoke modifier. The weapon offers standard and temporary Hemostatic payload entries; active/default choice and smoke effects remain unresolved.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L195-m320-smoke-selection.json`.

### Thermobaric Grenade Launcher (M320A1 THRM) — gadget group

**Research identity:** `launchers/m320thermobaric`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Fires impact-triggered thermobaric grenades, ideal for targeting groups of hostiles. The blast delivers limited initial damage but stuns and burns enemies for a short duration. Can be carried standalone or underslung on weapons with a Gadget Mount attachment for faster access.

**Configuration:** `Historical selected TB Explosion (Head 4892017)`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 30 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `DamageMultiplier` | 1 | Damage multiplier setting; active composition and target-specific final damage remain unconfirmed. |

**Configuration:** `Historical associated TB registry (Head 4892017)`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 50 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `DamageMultiplier` | 1 | Damage multiplier setting; active composition and target-specific final damage remain unconfirmed. |

**What we know:**

- The earlier ordinary underbarrel selection reaches the thermobaric explosion owner. Its local BlastDamage is 30 while the associated registry value is 50; these are distinct source values, not interchangeable damage results.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-26-L78-m320tb-explosion-profile.json`, `frosty-2026-09-26-L79-m320-explosion-name-limits.json`, `frosty-2026-09-26-L85-m320-shockwave-input.json`.

### Auto-Guided Launcher (MBT-LAW) — gadget group

**Research identity:** `launchers/mbtlaw`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** An anti-tank missile system. Aim at the target and fire; the missile will then guide itself to the enemy vehicle and execute a top-down attack.

**Configuration:** `wb_mbtlaw`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadTime` | 3.4 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `RateOfFire` | 257 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 0, 30] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 3.4000001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |

**Configuration:** `pb_mbtlaw`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 80 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 4 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 6.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The launcher weapon sources select distinct primary projectiles and blast owners. Ammunition, reload entries, and movement-array values were read. Stored counts and timing do not establish carried ammunition or actual reload time.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L137-launcher-handling-ammunition.json`, `frosty-2026-09-29-L152-launcher-projectile-source.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### Panzerfaust 3 Simple (Panzerfaust3) — gadget group

**Research identity:** `launchers/panzerfaust3`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Anti-Vehicle Launcher

**Configuration:** `wb_panzerfaust3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadTime` | 4.96 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 4.96 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `RateOfFire` | 257 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1.6821553, 162] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |

**Configuration:** `dudexplosion_panzerfaust3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 56 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 4 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 2.0999999 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 7 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `pb_panzerfaust3`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 130 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 12 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `pb_panzerfaust3_dm32`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 230 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 12 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- Baseline and DM32 choices select different projectiles with different stored BlastDamage values. DM12A1 changes shot tuning; fallback, default selection, and effect composition remain unresolved.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L168-panzerfaust3-source.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### Unguided Rocket Launcher (RPG-7V2) — gadget group

**Research identity:** `launchers/rpg7`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A launcher that fires impact-triggered unguided rockets. Delivers effective damage against structures and vehicles. Inflicts greater damage on the sides, top, and rear of vehicles where the armor is thinner.

**Configuration:** `wb_rpg7v2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadTime` | 3.4 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `RateOfFire` | 150 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1.45, 117.99] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 3.4000001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |

**Configuration:** `pb_ns_rpg`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 70 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 6 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 2 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 8.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The launcher weapon sources select distinct primary projectiles and blast owners. Ammunition, reload entries, and movement-array values were read. Stored counts and timing do not establish carried ammunition or actual reload time.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L137-launcher-handling-ammunition.json`, `frosty-2026-09-29-L152-launcher-projectile-source.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### Air-Defense Launcher  (SLM-93A Spire) — gadget group

**Research identity:** `launchers/stinger`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A man-portable air-defense system designed to target enemy aircraft. Requires lock-on before launch, after which missiles will self-guide to the target unless intercepted by countermeasures. Designated targets can be locked-on from further away and lose below-radar protection.

**Configuration:** `wb_stinger`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadTime` | 3.4 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 3.66 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**Configuration:** `pb_ns_stinger`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 100 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 7.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The weapon source selects the scoped missile projectile. Stinger and IGLA share stored BlastDamage 100 and BlastRadius 5, but their alternate reload entries differ. Locking, guidance, and final target damage remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L162-stinger-igla-source.json`.

### Anti-Vehicle Mine (M15) — gadget group

**Research identity:** `mines/atmine`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** An anti-vehicle mine that detonates when armored vehicles pass over it. Place on the ground to arm. Cannot be stacked or positioned too close together.

**Configuration:** `pbns_atmine`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 1.99 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 300 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 2 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 4.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The source reaches projectile, simulation, and blast configurations. Blast values were checked; trigger distances, lifetimes, fragment composition, and effective damage remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L138-mine-trigger-source.json`, `frosty-2026-09-29-L153-mine-blast-source.json`.

### Tripwire Sensor AV Mine (M4A1 SLAM) — gadget group

**Research identity:** `mines/m4slam`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** An anti-vehicle mine designed for ground and off-route placement. When nearby enemy vehicles trip the device's proximity sensor they are targeted with a high-velocity projectile.

**Configuration:** `pb_m4slam`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 0.99000001 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 100 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 1 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 3.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `m4slam_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 300 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 7] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 0.75 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The source reaches projectile, simulation, and blast configurations. Blast values were checked; trigger distances, lifetimes, fragment composition, and effective damage remain unconfirmed.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L138-mine-trigger-source.json`, `frosty-2026-09-29-L153-mine-blast-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Acoustic Sensor AV Mine (PTKM-1R) — gadget group

**Research identity:** `mines/ptkm1r`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** An anti-vehicle mine that locates targets in the immediate area via audio sensors. Once triggered, it launches an explosive payload and performs a top-down attack to strike armored vehicles where they are less protected.

**Configuration:** `ptkm1r_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `ReloadTime` | 0 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |

**What we know:**

- Deployment reaches a deployed vehicle source, but the inspected forward route does not select its CombatElement. The separate explosive projectile stores candidate BlastDamage 160 and BlastRadius 4; these are not confirmed active mine effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L161-gadget-handling-source.json`, `frosty-2026-09-29-L165-ptkm1r-projectile-source.json`.

### Adrenaline Injector (AJ-03 STIM) — gadget group

**Research identity:** `misc/adrenalineshot`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Temporarily boosts sprint speed while reducing explosive and incendiary damage. Also provides brief resistance to and clears the effects of Flash and Stun Grenades.

**Configuration:** `wb_adrenalineshot`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `ReloadTime` | 0 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |

**What we know:**

- A gameplay expression references three named effect assets. The inspected ability route does not prove when those effects execute or how their stored numbers should be used.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L147-adrenaline-shot-source.json`, `frosty-2026-09-29-L161-gadget-handling-source.json`.

### Upgraded Armor — gadget group

**Research identity:** `misc/ceramicarmor`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Standard small-arms issue tactical vest insert. Provides base-line ballistic protection.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The ability and effect sources select different resource owners and share state-channel references. The inspected routes do not establish active protection, damage reduction, or equipment selection.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L179-armor-resource-joins.json`.

### Defibrillator (PowerPulse) — gadget group

**Research identity:** `misc/defibrillator`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** This equipment can revive both squad members and teammates. Charge paddles for a short duration to revive a downed soldier with full health. Can also inflict damage on enemies.

**Configuration:** `defibrillators_equipped_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | 3 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |

**What we know:**

- The source includes revive-state and teammate-revive channels, charge-related interfaces, and a faster-recharge perk reference. These references do not establish restored health, charge time, or recharge time.
- Later resource work names the selected ammunition fields after a same-owner control. The counts and replenishment settings remain source configuration.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L139-defibrillator-source.json`, `frosty-2026-09-29-L187-defibrillator-revive-consumer.json`, `frosty-2026-09-29-L190-utility-compiled-reader-gate.json`, `frosty-2026-09-30-L217-support-resource-source.json`.

### Portable Mortar (LWCMS) — gadget group

**Research identity:** `misc/deployablemortar`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** This man-portable indirect-fire weapon launches high-explosive shells designed to strike defensive positions and disperse infantry, or smoke shells to conceal troop movement. Aim via the minimap or manually. Once fired, the mortar will be spotted, marking its position in-world and on the enemyâ€™s minimap. Weapon accuracy increases with continuous shots in the same location.

**Configuration:** `deployablemortar_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `ReloadTime` | 0 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `RateOfFire` | 399.89999 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 0, 0] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**Configuration:** `vb_veh_deployablemortar`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `ReloadTime` | 4 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | 0 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |

**Configuration:** `pbns_m720a1`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 2.444 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 60 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 7.6220002 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |

**Configuration:** `pbns_m722`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 0 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |

**What we know:**

- Deployment reaches two mortar firing configurations, M720A1 and M722. Their ammunition and blast settings differ. Native payload selection and effective damage remain unconfirmed.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L169-mortar-source.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### Recon Drone (XFGM-6D) — gadget group

**Research identity:** `misc/drone`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A combat drone armed with an electronics disruption weapon, able to target gadgets through walls and destroy them without line of sight. Can be left hovering to automatically spot hostiles, marking their position in-world and on the minimap. Equipped with thermal vision for enhanced spotting.

**Configuration:** `veh_drone`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 0 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 15 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The recon weapon source reaches drone deployment and a separate payload-drone branch. A selected payload-bomb profile is distinct from a Lancet explosion candidate. The source also references targeting and state expressions; payload execution, flight, lifetime, and spotting remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L170-drone-payload-source.json`, `frosty-2026-09-29-L204-recon-drone-tracking-source.json`, `frosty-2026-09-29-L205-drone-utility-source-consumers.json`.

### Protective Mask — gadget group

**Research identity:** `misc/gasmask`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A multi-filter respirator that, when equipped, protects the wearer from the disorienting effects of VL-7 smoke.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Gas-mask sources reference removal and duration effects. A separate blocking configuration references soldier channels, but the exact binding and effective protection rules remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L160-gas-mask-source.json`, `frosty-2026-09-29-L208-special-mask-duration-channel-source.json`.

### Handheld Jammer (MANET-DIS 5) — gadget group

**Research identity:** `misc/mobilejammer`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A portable electronic warfare device that, when active, temporarily disrupts the function of enemy equipment within its range. The device is audible when in use, and can be carried by the user or tossed as a diversion.

**Configuration:** `mobilejammer_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `AutoReplenishDelay` | 45 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |

**What we know:**

- The weapon configuration contains resource and replenishment settings. Its selected effect references reach jammer effects, but execution and the affected targets remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L173-mobile-jammer-source.json`.

### Night Vision Goggles — gadget group

**Research identity:** `misc/nvg`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** NVGs

**Configuration:** `WB_NVG_MP`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | false | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |

**What we know:**

- The multiplayer-named weapon configuration contains negative ammunition values and disables automatic magazine replenishment. Ability and client-expression references resolve; battery and vision behavior remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L182-nvg-resource-source.json`.

### Laser Designator (LTLM II) — gadget group

**Research identity:** `misc/pld`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** The designator functions as binoculars for enhanced spotting and allows users to mark designate both vehicles and locations. Designated targets can be locked-on from further away and lose below-radar protection. Users can set the device to function autonomously and remotely access the designator at any point, which can rotate to provide a 360 degree field of view.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The inspected designator and lock/spotting assets contain checked values and references. Their ranges, magnitudes, durations, and active selection are not established.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L149-pld-marking-source.json`.

### Soft  Armor Simple (Standard Armor) — gadget group

**Research identity:** `misc/softarmor`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Standard small-arms issue tactical vest insert. Provides base-line ballistic protection.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The ability and effect sources select different resource owners and share state-channel references. The inspected routes do not establish active protection, damage reduction, or equipment selection.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L179-armor-resource-joins.json`.

### Tracer Dart (TRCRv2) — gadget group

**Research identity:** `misc/tracerdart`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A gas-powered pistol that fires a magnetic dart which designates enemy vehicles or personnel. Designated targets can be locked-on from further away and lose below-radar protection.

**Configuration:** `wb_tracerdart`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 257 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 200] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 3.3800001 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 3.3800001 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The projectile references a gameplay expression that references the tracer-dart locking-signature effect. A stored float 11 and Boolean false were checked; neither establishes an 11-fold lock effect.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L144-tracer-dart-lock-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Anti-Personnel Mine (M18A1) — gadget group

**Research identity:** `placedexplosives/m18claymore`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A directional, anti-personnel fragmentation mine that is detonated via a tripwire firing system. Enemies moving past the mine at normal crouch or prone speed will not trigger the device.

**Configuration:** `m18claymore_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 60 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 0] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 0 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The source reaches projectile, simulation, and blast configurations. Blast values were checked; trigger distances, lifetimes, fragment composition, and effective damage remain unconfirmed.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L138-mine-trigger-source.json`, `frosty-2026-09-29-L164-claymore-blast-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### SP_Drone Simple (SURVEILLANCE DRONE) — gadget group

**Research identity:** `remotecontrollable/payloaddrone`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Can be placed for use by eliminated squadmates

**Configuration:** `vb_veh_drone_payload`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 0 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 15 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `psb_prj_bomb_dronepayload`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 1.5 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 100 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 7.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- The recon weapon source reaches drone deployment and a separate payload-drone branch. A selected payload-bomb profile is distinct from a Lancet explosion candidate. The source also references targeting and state expressions; payload execution, flight, lifetime, and spotting remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L170-drone-payload-source.json`, `frosty-2026-09-29-L206-sp-payload-drone-deployment-source.json`.

### Supply Pouch (Goliath Compact) — gadget group

**Research identity:** `supply/supplypouch`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A single-use pouch to replenish ammo and medical supplies for the owner or their teammates. Fully restocks ammo capacity of the primary and secondary weapons and restores a portion of health.

**Configuration:** `supplypouch_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |

**What we know:**

- The weapon and supply-sphere sources reference ammunition and healing effects. Their stored operands have not been mapped to an effective refill amount, healing rate, or cadence.
- Later resource work names the selected ammunition fields after a same-owner control. The counts and replenishment settings remain source configuration.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L157-supply-pouch-source.json`, `frosty-2026-09-30-L217-support-resource-source.json`.

### Anti-Vehicle Grenade (SCG-24) — gadget group

**Research identity:** `throwables/antitank`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A grenade primarily for use against vehicles but will inflict damage on enemies caught in the blast. When thrown, it follows the trajectory of a typical grenade before releasing a parachute and dropping rapidly for a top attack.

**Configuration:** `pbns_antitankgrenade`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 0.75 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 50 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 1.5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 4 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `antitankgrenade_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadTime` | 0.1 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1.4, 25] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The selected blast object has a smaller stored blast radius and lower stored blast damage than Frag. Its four-row child has no proved falloff meaning.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L150-antitank-blast-source.json`, `frosty-2026-09-29-L166-throwable-ammo-launch-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Demolition Charge (C-4 Explosives) — gadget group

**Research identity:** `throwables/c4`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A bundle of high explosive charges that can be remote detonated after placement. Can cause massive destruction to structures, vehicles, and infantry.

**Configuration:** `pns_c4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 100 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 3 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 0 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `wb_c4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadTime` | 0 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `RateOfFire` | 100 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1, 9.5] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**Configuration:** `blastcurve_c4`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `CurveDistance` | [0, 0.59900004, 0.60000002, 0.75797439, 0.76102567, 0.90256411, 0.90358973, 1] | Stored first coordinate of a falloff curve. Units and interpolation are unconfirmed. |
| `CurveDamage` | [1, 0.99578947, 0.80000001, 0.80000001, 0.4063158, 0.40210527, 0.2, 0.2] | Stored second coordinate of a falloff curve. Effective scaling and interpolation are unconfirmed. |

**What we know:**

- The weapon source selects a projectile, a blast object, and an eight-point blast-falloff curve. C4 stores BlastDamage 100 and BlastRadius 3; Frag stores 100 and 5. This is a source comparison, not an effective damage comparison.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L151-c4-blast-source.json`, `frosty-2026-09-29-L166-throwable-ammo-launch-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Stun Grenade (Mk 141 Mod 0) — gadget group

**Research identity:** `throwables/concussion`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** This grenade produces a concussive blast that disorients enemies, temporarily preventing ADS and sprint capabilities.

**Configuration:** `concussiongrenade_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadTime` | 0.1 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1.4, 25] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The projectile references a named concussion expression. Its radius interface has an unresolved type and a null boxed value, so no concussion radius or duration is assigned.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L142-concussion-effect-envelope.json`, `frosty-2026-09-29-L176-utility-throwable-resource-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Sniper Decoy (Field Dummy No.25) — gadget group

**Research identity:** `throwables/decoy`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A dummy designed to draw the enemy's attention while you fire from a safer location. Taking up position near a friendly Sniper Decoy will hide your scope glint with its own. Replicates the stance of the owner when placed and is immediately spotted, marking its position in-world and on the enemyâ€™s minimap.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The regular decoy source reaches a projectile and a sound-patch reference. The sniper decoy reaches deployment expressions. Sound range, glint selection, spotting benefits, and activation conditions remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L193-decoy-utility-consumer.json`.

### Flash Grenade (M84) — gadget group

**Research identity:** `throwables/flashbang`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** This grenade emits an intense blast that temporarily blinds nearby enemies. Impairment scales with proximity and line of sight to the blast.

**Configuration:** `flashbang_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadTime` | 0.1 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1.4, 25] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The weapon references two exports in the flashbang projectile file. The scoped effect route does not establish a selected effect owner or a flash duration.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L155-flashbang-effect-source.json`, `frosty-2026-09-29-L176-utility-throwable-resource-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Fragmentation Grenade (M67) — gadget group

**Research identity:** `throwables/frag`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Equipped with an impact-triggered time fuse, this grenade is ideal for targeting enemies behind cover. Deadly when close to blast radius.

**Configuration:** `pbns_fraggrenade`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `Gravity` | -9.8000002 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 100 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 7.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `fraggrenade_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadTime` | 0.1 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1.4, 25] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**Configuration:** `fraggrenade_blastdamagefalloff_curve`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `CurveDistance` | [0, 0.2, 0.60000002, 0.60100001, 0.79900002, 0.80000001, 1] | Stored first coordinate of a falloff curve. Units and interpolation are unconfirmed. |
| `CurveDamage` | [1, 1, 0.80000001, 0.60000002, 0.40000001, 0.2, 0.2] | Stored second coordinate of a falloff curve. Effective scaling and interpolation are unconfirmed. |

**What we know:**

- The selected projectile-to-blast chains store BlastDamage 100 for Frag and 40 for Mini V40, with BlastRadius 5 in both. Their seven-point and five-point falloff curves differ; effective damage is unconfirmed.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L148-frag-miniv40-blast-source.json`, `frosty-2026-09-29-L166-throwable-ammo-launch-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Incendiary Grenade (AN/M14) — gadget group

**Research identity:** `throwables/incendiary`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A grenade that produces a brief blast radius of intense heat. Affected enemies will continue to burn for a short duration. Fire damage can be reduced by going prone.

**Configuration:** `pbns_incendiarygrenade`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `Gravity` | -9.8000002 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 0 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 4 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 6.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `incendiarygrenade_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadTime` | 0.1 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1.4, 25] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The weapon selects a projectile and blast child. Separate fire expressions reference damage effects, but they do not establish the active lingering-fire equation. BlastDamage 0 is not proof of no fire damage.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L154-incendiary-source.json`, `frosty-2026-09-29-L166-throwable-ammo-launch-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Mini Frag Grenade (V40) — gadget group

**Research identity:** `throwables/miniv40`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A compact grenade that can be thrown further than the standard Frag but at the cost of less damage. Reduced weight means more can be carried.

**Configuration:** `pbns_miniv40`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `Gravity` | -9.8000002 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 40 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 5 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 7.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |
| `CurveDistance` | [0.29743591, 0.5, 0.69846153, 0.69946152, 0.90358973] | Stored first coordinate of a falloff curve. Units and interpolation are unconfirmed. |
| `CurveDamage` | [1, 0.83332998, 0.66659999, 0.5, 0.33329999] | Stored second coordinate of a falloff curve. Effective scaling and interpolation are unconfirmed. |

**Configuration:** `miniv40_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadTime` | 0.1 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1.6, 35] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The selected projectile-to-blast chains store BlastDamage 100 for Frag and 40 for Mini V40, with BlastRadius 5 in both. Their seven-point and five-point falloff curves differ; effective damage is unconfirmed.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L148-frag-miniv40-blast-source.json`, `frosty-2026-09-29-L166-throwable-ammo-launch-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Throwable Proximity Detector (MTN-55) — gadget group

**Research identity:** `throwables/proximity`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** This detector scans for enemies once per second within visible range of the device. Detected enemies will be spotted, marking their position in-world and on the minimap for a duration of two seconds.

**Configuration:** `proximity_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadTime` | 0.1 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `Shot.InitialSpeed.z` | 25 | Configured z component of the launch vector; this does not establish measured flight speed. |

**What we know:**

- A candidate detection expression stores 75, -1, and -1. Their roles and active selection are unresolved, so 75 is not assigned as a detection radius.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L158-proximity-source.json`, `frosty-2026-09-29-L176-utility-throwable-resource-source.json`.

### Smoke Grenade (M18) — gadget group

**Research identity:** `throwables/smoke`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A grenade designed to create temporary smoke screens. Blocks ability to spot targets and clears spotted markers from all infantry inside the smoke radius.

**Configuration:** `smokegrenade_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadTime` | 0.1 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1.4, 25] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The inspected smoke sources contain checked values and import links. They do not establish smoke coverage, duration, or active effect selection.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L146-smoke-grenade-source.json`, `frosty-2026-09-29-L176-utility-throwable-resource-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Supply Bag (Goliath 90L) — gadget group

**Research identity:** `throwables/supplycrate`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Once dropped, the bag resupplies all nearby infantry with ammo for gadgets and weapons and regenerates health more efficiently, even when under fire. Gadget resupply does not occur in Battle Royale.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The weapon-to-projectile-to-feature-to-expression route and ammunition-effect references resolve. Medic variants also reference a healing effect. Actual health/ammo amounts, cadence, and self-resupply conditions remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L143-supply-crate-ammunition-source.json`, `frosty-2026-09-29-L186-supply-utility-consumer.json`, `frosty-2026-09-29-L190-utility-compiled-reader-gate.json`, `frosty-2026-09-29-L194-medic-crate-healing-consumer.json`.

### Throwing Knife (Steel Wing) — gadget group

**Research identity:** `throwables/throwingknife`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A lightweight balanced blade that will fly in a small arc to the target. Headshots deliver instant kills while non-fatal strikes delay health regeneration for 10 seconds.

**Configuration:** `throwingknife_projectile_v2`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `StartDamage` | 50 | Damage at the beginning of the configured distance profile; effective hit damage is unconfirmed. |
| `EndDamage` | 50 | Damage at the end of the configured distance profile; effective hit damage is unconfirmed. |
| `DamageFalloffStartDistance` | 5 | Start of the configured damage-falloff interval; this does not establish tool reach. |
| `DamageFalloffEndDistance` | 15 | End of the configured damage-falloff interval; units and effective range are unconfirmed. |
| `InitialSpeed` | 350 | Speed setting on this particular projectile owner; it is separate from the weapon launch vector. |
| `TimeToLive` | 10 | Projectile lifetime setting; units and actual expiry conditions remain unconfirmed. |

**Configuration:** `throwingknife_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 5 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadTime` | 0.1 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `RateOfFire` | 550 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 1.527, 44.973999] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The earlier selected v2 projectile has direct-damage, falloff, lifetime, and speed settings. The weapon launch-vector setting is a separate value; the two speeds must not be substituted for each other.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L156-throwing-knife-source.json`, `frosty-2026-09-29-L166-throwable-ammo-launch-source.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### Deployable Cover (MaxGuard 900) — gadget group

**Research identity:** `tools/deployablecover`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A reinforced ballistic shield to protect from projectiles and explosive damage. The shield can degrade from damage, so work with Engineers who can repair it and keep you in the fight.

**Configuration:** `deployablecover_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |

**What we know:**

- The later deployment route reaches the deployed object, damage zones, shared health configuration, and gameplay expressions. This resolves source references, but it does not establish effective cover health or protection.
- Later resource work names the selected ammunition fields after a same-owner control. The counts and replenishment settings remain source configuration.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L141-cover-durability-source.json`, `frosty-2026-09-29-L189-deployable-cover-protection-consumer.json`, `frosty-2026-09-30-L216-deployment-resource-count-source.json`.

### Grenade Intercept System (GPDIS) — gadget group

**Research identity:** `tools/eidos`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Once set on the ground, the Grenade Intercept System tracks and destroys incoming projectiles such as hand-thrown and launched grenades. Can intercept up to three projectiles during a window of activation that begins after the initial detection.

**Configuration:** `eidos_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `ReloadTime` | 0.5 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The weapon source selects a deployed object and a controlled ammunition owner. EIDOS and MPAPS have distinct reload entries. The protection and interception rules remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L171-mpaps-eidos-resource-source.json`.

### Assault Ladder (Tarantula ALX) — gadget group

**Research identity:** `tools/ladder`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** This equipment provides access to higher vantage points. Depending on the angle of placement, it can act as a bridge between buildings, or a ramp to help traverse obstacles on the battlefield.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The deployment route reaches the ladder and its separate configuration, physics, and interaction sources. The interaction graph references action, climbing, melee, and stance channels. Placement limits, climb behavior, and activation conditions remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L178-ladder-deployment-source.json`, `frosty-2026-09-29-L188-assault-ladder-interaction.json`.

### Missile Intercept System (MP-APS) — gadget group

**Research identity:** `tools/mpaps`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Once set on the ground, this device tracks and destroys larger incoming projectiles such as missiles, mortar shells, and tank shells. Can intercept up to three projectiles during a window of activation that begins after the initial detection.

**Configuration:** `mpaps_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `ReloadTime` | 0 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 0 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The weapon source selects a deployed object and a controlled ammunition owner. EIDOS and MPAPS have distinct reload entries. The protection and interception rules remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L171-mpaps-eidos-resource-source.json`.

### Repair Tool (HOFF-1500) — gadget group

**Research identity:** `tools/repair`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A blow torch to repair friendly vehicles and equipment. Can also damage enemy assets. Extended use will temporarily overheat the tool. In Battle Royale, it has the additional ability to open locked safes.

**Configuration:** `wb_repairtool`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `StartDamage` | 13 | Damage at the beginning of the configured distance profile; effective hit damage is unconfirmed. |
| `EndDamage` | 13 | Damage at the end of the configured distance profile; effective hit damage is unconfirmed. |
| `DamageFalloffStartDistance` | 100 | Start of the configured damage-falloff interval; this does not establish tool reach. |
| `DamageFalloffEndDistance` | 200 | End of the configured damage-falloff interval; units and effective range are unconfirmed. |
| `RateOfFire` | 600 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | -1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 0, 80] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | 0 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.5899999 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**Configuration:** `RepairTool_Default_Repair Amount Per Second`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `Unnamed float members` | [40, 0, 250] | The owner is named as a repair amount per second. The three member roles and effective repair rate remain unresolved; 40 is not confirmed health per second. |

**What we know:**

- The selected projectile contains direct-damage settings. A repair expression references the vehicle-repair effect and the named repair-amount setting. Its three stored floats do not establish actual repair health per second.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Repair rate, actual damage ticks, tool reach, overheating, and cooling time remain unconfirmed.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L174-repair-tool-source.json`, `frosty-2026-09-29-L185-repair-utility-consumer.json`, `frosty-2026-09-29-L190-utility-compiled-reader-gate.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### Deploy Beacon (QLink 6) — gadget group

**Research identity:** `tools/spawnbeacon`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** The beacon provides a single-use deploy point for the operator and each squad member. The device emits a constant sound audible to hostiles and becomes inactive after the owner uses it to deploy. In Small Scale Battles, squad member deployment is disabled.

**Configuration:** `wb_spawnbeacon`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |

**What we know:**

- Beacon roots and their directly referenced children were checked. Vehicle-field candidates match between two variants, but the active multiplayer choice and spawning rules remain unconfirmed.
- Later resource work names the selected ammunition fields after a same-owner control. The counts and replenishment settings remain source configuration.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L145-spawn-beacon-source.json`, `frosty-2026-09-30-L217-support-resource-source.json`.

### Motion Sensor (T-UGS) — gadget group

**Research identity:** `tools/tugs`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** This device spots nearby moving enemies, vehicles, and gadgets, marking their position in-world and on the minimap for all team members. Enemy infantry can remain undetected while moving in crouch or prone. The device emits a sound audible to hostiles.

**Configuration:** `wb_tugs`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |

**What we know:**

- The source points to a detection expression containing -1, -1, and 75. Their meanings and execution remain unresolved; 75 is not a confirmed detection radius.
- Later resource work names the selected ammunition fields after a same-owner control. The counts and replenishment settings remain source configuration.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L140-tugs-detection-source.json`, `frosty-2026-09-30-L216-deployment-resource-count-source.json`.

### Underbarrels/M26Mass12gFrag — gadget group

**Research identity:** `underbarrels/m26mass12gfrag`. Classification: equippable multiplayer gadget.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The remaining M26 payload and state roots were checked, but ordinary parent selections reach the base and Dragon's Breath sources. Exact selection of this remaining payload is unproved, and its owner identity prevents automatic transfer of older field names.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L201-m26-remaining-payload-route-limit.json`.

### Underbarrels/M26Mass4Buck — gadget group

**Research identity:** `underbarrels/m26mass4buck`. Classification: equippable multiplayer gadget.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The remaining M26 payload and state roots were checked, but ordinary parent selections reach the base and Dragon's Breath sources. Exact selection of this remaining payload is unproved, and its owner identity prevents automatic transfer of older field names.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L201-m26-remaining-payload-route-limit.json`.

### Incendiary-Round Shotgun (SS26) — gadget group

**Research identity:** `underbarrels/m26massdragonbreath`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** A bolt action shotgun, chambered in 12-gauge incendiary buckshot rounds. Deals reduced impact damage but sets targets on fire and burns them for a short duration. Ground shots produce an area of fire that burns enemies for a short duration if entered.

**Configuration:** `pd_m26massdragonbreath`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `StartDamage` | 5 | Damage at the beginning of the configured distance profile; effective hit damage is unconfirmed. |
| `EndDamage` | 2.5 | Damage at the end of the configured distance profile; effective hit damage is unconfirmed. |
| `DamageFalloffStartDistance` | 5 | Start of the configured damage-falloff interval; this does not establish tool reach. |
| `DamageFalloffEndDistance` | 15 | End of the configured damage-falloff interval; units and effective range are unconfirmed. |
| `InitialSpeed` | 350 | Speed setting on this particular projectile owner; it is separate from the weapon launch vector. |
| `TimeToLive` | 0.1 | Projectile lifetime setting; units and actual expiry conditions remain unconfirmed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |

**What we know:**

- The earlier ordinary M26 source has a buckshot base projectile and a Dragon's Breath replacement projectile. Their direct-damage and falloff settings differ. They are not necessarily separate menu choices, and null direct-hit/second-curve pointers do not establish zero damage.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-26-L73-m26db-source-profile.json`, `frosty-2026-09-26-L80-m26db-trajectory-inputs.json`.

### Underbarrels/M26MassFlechette — gadget group

**Research identity:** `underbarrels/m26massflechette`. Classification: equippable multiplayer gadget.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The remaining M26 payload and state roots were checked, but ordinary parent selections reach the base and Dragon's Breath sources. Exact selection of this remaining payload is unproved, and its owner identity prevents automatic transfer of older field names.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L201-m26-remaining-payload-route-limit.json`.

### Underbarrel Shotgun (M26 MASS) — gadget group

**Research identity:** `underbarrels/m26massslug`. Classification: equippable multiplayer gadget.

**Description (saved game text; supporting association):** Chambered in 12-gauge buckshot rounds, the M26 is a bolt action close-range shotgun.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The remaining M26 payload and state roots were checked, but ordinary parent selections reach the base and Dragon's Breath sources. Exact selection of this remaining payload is unproved, and its owner identity prevents automatic transfer of older field names.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L201-m26-remaining-payload-route-limit.json`.

## Shared gadget systems

### CallIns/_Shared — gadget group

**Research identity:** `callins/_shared`. Classification: shared system.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Several call-ins share targeting equipment. Smoke, artillery, air-strike, and target-validation references were traced. Shared source equipment does not make their payloads or effects interchangeable.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L196-smoke-screen-callin-consumer.json`, `frosty-2026-09-29-L198-artillery-mortar-callin-selection.json`, `frosty-2026-09-29-L199-air-jagm-callin-selection.json`, `frosty-2026-09-29-L200-kinetic-gas-targeting-consumer.json`.

### Launchers/CB90TorpedoLauncher — gadget group

**Research identity:** `launchers/cb90torpedolauncher`. Classification: shared system.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Patrol-boat equipment references the torpedo and mine projectiles. Their features reference simulation, presentation, and water interaction. Guidance, trigger conditions, damage, and player availability remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L207-naval-gadget-dependency-source.json`.

### Mines/Naval_Mines — gadget group

**Research identity:** `mines/naval_mines`. Classification: shared system.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Patrol-boat equipment references the torpedo and mine projectiles. Their features reference simulation, presentation, and water interaction. Guidance, trigger conditions, damage, and player availability remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L207-naval-gadget-dependency-source.json`.

### RemoteControllable/ReconDrone — gadget group

**Research identity:** `remotecontrollable/recondrone`. Classification: shared system.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The drone source references abilities, targeting, lifetime, thermal, and boundary expressions. The inspected incoming selections do not establish effective control range, spotting, lifetime, or target-state rules.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L204-recon-drone-tracking-source.json`.

### RemoteControllable/Shared — gadget group

**Research identity:** `remotecontrollable/shared`. Classification: shared system.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The drone source references abilities, targeting, lifetime, thermal, and boundary expressions. The inspected incoming selections do not establish effective control range, spotting, lifetime, or target-state rules.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L205-drone-utility-source-consumers.json`.

### Medic Crate Simple (Medical Crate) — gadget group

**Research identity:** `throwables/mediccrate`. Classification: shared system.

**Description (saved game text; supporting association):** Restores health to all nearby friendlies, healing any sustained damage.  Powerful squad survivability booster.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Supply-crate variants and the medic graph reference the exact healing effect. The configuration token named Ignore_Damage does not establish the healing amount or prove immunity.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L194-medic-crate-healing-consumer.json`.

## Single-player or mode-specific gadget groups

### SP_Drone Simple (Payload Drone Grenade) — gadget group

**Research identity:** `remotecontrollable/sp_payloaddrone`. Classification: single player or mode item.

**Description (saved game text; supporting association):** Payload Drone Grenade

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The single-player drone owner references unit, deployment, ability, and state configuration. Stored members do not establish native deployment or multiplayer availability.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L206-sp-payload-drone-deployment-source.json`.

## Gadget groups with unresolved availability

### BattlePickups/ArtilleryStrikeMP — gadget group

**Research identity:** `battlepickups/artillerystrikemp`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Customization variants reference shared targeting equipment with different modifier contexts. Targeting interfaces and resource choices are sourced; selected payloads, target eligibility, and execution remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L198-artillery-mortar-callin-selection.json`.

### BattlePickups/Minigun — gadget group

**Research identity:** `battlepickups/minigun`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Configuration:** `minigun_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1799.999 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadTime` | 6.7 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 5.83 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `MagazineCapacity` | 250 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `RateOfFire` | 1799.999 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `Shot.InitialSpeed` | [0, 0, 990] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0.0035000001 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 6.6999998 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 5.8299999 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |

**Configuration:** `Minigun selected projectile`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `Field_5279388d (selected health-curve pairs)` | [[0, 26.049999], [21, 26.049999], [21, 20.67], [75, 20.67], [75, 17.129999]] | Stored pairs [first coordinate, second coordinate] on the selected health-associated projectile curve. Keep the armor curve separate; interpolation and effective damage remain unconfirmed. |

**What we know:**

- The weapon source selects a captured bullet projectile. Its magazine, firing-rate, reload, and damage-profile settings were read. These do not establish its current multiplayer availability.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L175-minigun-source.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### BattlePickups/Railgun — gadget group

**Research identity:** `battlepickups/railgun`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Configuration:** `railgun_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 299.98999 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadTime` | 4.2659998 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | -1 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 11 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `Shot.InitialSpeed` | [0, 0, 1029] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |

**Configuration:** `pd_railgun`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `StartDamage` | 150 | Damage at the beginning of the configured distance profile; effective hit damage is unconfirmed. |
| `EndDamage` | 150 | Damage at the end of the configured distance profile; effective hit damage is unconfirmed. |
| `DamageFalloffStartDistance` | 100 | Start of the configured damage-falloff interval; this does not establish tool reach. |
| `DamageFalloffEndDistance` | 200 | End of the configured damage-falloff interval; units and effective range are unconfirmed. |

**What we know:**

- The weapon source selects the Railgun projectile. Ammunition, reload, and direct-damage settings were read; actual firing and damage behavior remain unconfirmed.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L180-railgun-source.json`, `frosty-2026-10-01-L645-weapon-shape-profiles.json`; `gadget-weapon-profiles.json`.

### BattlePickups/SmokeScreenMP — gadget group

**Research identity:** `battlepickups/smokescreenmp`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Normal and multiplayer-named smoke-screen abilities use distinct configuration resources and a shared feature. Marker candidates reach a smoke expression; their active choice and concealment behavior remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L196-smoke-screen-callin-consumer.json`.

### BattlePickups/SystemManager — gadget group

**Research identity:** `battlepickups/systemmanager`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### CallIns/_SpawnerPrefabs — gadget group

**Research identity:** `callins/_spawnerprefabs`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### CallIns/AirDrop — gadget group

**Research identity:** `callins/airdrop`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Configuration:** `supplydrop_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | 1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | false | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |
| `AutoReplenishDelay` | 5 | Delay setting for ammunition replenishment; effective cooldown and units are unconfirmed. |

**What we know:**

- The Supply Drop weapon source selects deployment-marker and vehicle expressions. Later work proves the Ability-to-configuration-to-weapon binding. Actual supply delivery and refill conditions remain unconfirmed.
- Later L218 completes the exact Supply Drop Ability → customization configuration → weapon blueprint source binding. Its resource settings do not establish native uses or refill behavior.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L192-logistics-utility-consumer.json`, `frosty-2026-09-30-L218-supplydrop-resource-binding.json`.

### CallIns/AirStrike — gadget group

**Research identity:** `callins/airstrike`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Air Strike and JAGM configurations share targeting equipment. Offered selector entries include both resource choices. Those entries do not establish active deployment or the selected strike payload.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L199-air-jagm-callin-selection.json`.

### CallIns/ArtilleryGasStrike — gadget group

**Research identity:** `callins/artillerygasstrike`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Kinetic and PsyGas configurations reach weapon and marker contexts. Shared target-validation expressions reference target and zone dependencies; eligibility, execution, and gas-effect rules remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L200-kinetic-gas-targeting-consumer.json`.

### CallIns/ArtilleryStrike — gadget group

**Research identity:** `callins/artillerystrike`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Customization variants reference shared targeting equipment with different modifier contexts. Targeting interfaces and resource choices are sourced; selected payloads, target eligibility, and execution remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L198-artillery-mortar-callin-selection.json`.

### CallIns/KineticStrike — gadget group

**Research identity:** `callins/kineticstrike`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Kinetic and PsyGas configurations reach weapon and marker contexts. Shared target-validation expressions reference target and zone dependencies; eligibility, execution, and gas-effect rules remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L200-kinetic-gas-targeting-consumer.json`.

### CallIns/MobileRespawn — gadget group

**Research identity:** `callins/mobilerespawn`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The weapon source selects marker and vehicle expressions for Mobile Respawn. The conditions for deployment, spawning, and continued availability remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L192-logistics-utility-consumer.json`.

### CallIns/MortarStrike — gadget group

**Research identity:** `callins/mortarstrike`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Customization variants reference shared targeting equipment with different modifier contexts. Targeting interfaces and resource choices are sourced; selected payloads, target eligibility, and execution remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L198-artillery-mortar-callin-selection.json`.

### CallIns/SmokeScreen — gadget group

**Research identity:** `callins/smokescreen`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Normal and multiplayer-named smoke-screen abilities use distinct configuration resources and a shared feature. Marker candidates reach a smoke expression; their active choice and concealment behavior remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L196-smoke-screen-callin-consumer.json`.

### CallIns/UAVOverwatch — gadget group

**Research identity:** `callins/uavoverwatch`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The ability references a resource and a gameplay expression. MQ9 and spotting configuration are candidates; the route does not prove deployment selection or spotting behavior.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L191-uav-overwatch-utility-consumer.json`.

### Intel/DataDrive — gadget group

**Research identity:** `intel/datadrive`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Intel/DataExtractionTablet — gadget group

**Research identity:** `intel/dataextractiontablet`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The tablet modifier references the exact resource token. This proves configuration identity, but the inspected route does not establish the intelligence-gathering effect.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L203-data-extraction-tablet-configuration.json`.

### Intel/SurveillanceCameraDome — gadget group

**Research identity:** `intel/surveillancecameradome`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Intel/SurveillanceCameraSecurity — gadget group

**Research identity:** `intel/surveillancecamerasecurity`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Launchers/Airburst — gadget group

**Research identity:** `launchers/airburst`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### M320 Ballistic Dart Simple (M320 Ballistic Dart) — gadget group

**Research identity:** `launchers/breachingdart`. Classification: unresolved.

**Description (saved game text; supporting association):** M320 Ballistic Dart Description

**Configuration:** `pb_40x46mmlvg_drill`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 40 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 1 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 7 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `pb_40x46mmlvg_drill_gas`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `BlastDamage` | 40 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 1 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `InnerBlastRadius` | 1 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 7 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `drillgl_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 100 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 1.6, 72] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `ReloadTime` | 2.53 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 2.53 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The weapon source selects the standard breaching-dart projectile and its blast child. A gas path is a separate candidate. The stored blast values do not establish breaching strength or gas behavior.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L159-breaching-dart-source.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

### Launchers/CZ805G1 — gadget group

**Research identity:** `launchers/cz805g1`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Launchers/M224Mortar — gadget group

**Research identity:** `launchers/m224mortar`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Launchers/M320 — gadget group

**Research identity:** `launchers/m320`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Configuration:** `M26DB selected (historical Head 4892017)`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `hip.RecoilAmount` | 3 | Configured recoil amount for this aim state; effective native recoil remains unconfirmed. |
| `hip.RecoilAmountMultiplier` | 1 | Multiplier setting for this recoil component; native composition remains unconfirmed. |
| `hip.RecoilAmountMultiplierExponent` | 0 | Exponent setting for this recoil multiplier; native composition remains unconfirmed. |
| `hip.RecoilDirection` | -10 | Configured recoil direction for this aim state; coordinate convention and native behavior remain unconfirmed. |
| `hip.RecoilDirectionVariation` | 12 | Configured recoil-direction variation for this aim state; the effective distribution is unconfirmed. |
| `hip.RecoilDirectionVariationMultiplier` | 1 | Multiplier setting for this recoil component; native composition remains unconfirmed. |
| `hip.RecoilDirectionVariationMultiplierExponent` | 0 | Exponent setting for this recoil multiplier; native composition remains unconfirmed. |
| `ads.RecoilAmount` | 3 | Configured recoil amount for this aim state; effective native recoil remains unconfirmed. |
| `ads.RecoilAmountMultiplier` | 1 | Multiplier setting for this recoil component; native composition remains unconfirmed. |
| `ads.RecoilAmountMultiplierExponent` | 0 | Exponent setting for this recoil multiplier; native composition remains unconfirmed. |
| `ads.RecoilDirection` | -10 | Configured recoil direction for this aim state; coordinate convention and native behavior remain unconfirmed. |
| `ads.RecoilDirectionVariation` | 12 | Configured recoil-direction variation for this aim state; the effective distribution is unconfirmed. |
| `ads.RecoilDirectionVariationMultiplier` | 1 | Multiplier setting for this recoil component; native composition remains unconfirmed. |
| `ads.RecoilDirectionVariationMultiplierExponent` | 0 | Exponent setting for this recoil multiplier; native composition remains unconfirmed. |

**Configuration:** `M320 HE selected (historical Head 4892017)`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `hip.RecoilAmount` | 5 | Configured recoil amount for this aim state; effective native recoil remains unconfirmed. |
| `hip.RecoilAmountMultiplier` | 1 | Multiplier setting for this recoil component; native composition remains unconfirmed. |
| `hip.RecoilAmountMultiplierExponent` | 0 | Exponent setting for this recoil multiplier; native composition remains unconfirmed. |
| `hip.RecoilDirection` | 0 | Configured recoil direction for this aim state; coordinate convention and native behavior remain unconfirmed. |
| `hip.RecoilDirectionVariation` | 0 | Configured recoil-direction variation for this aim state; the effective distribution is unconfirmed. |
| `hip.RecoilDirectionVariationMultiplier` | 1 | Multiplier setting for this recoil component; native composition remains unconfirmed. |
| `hip.RecoilDirectionVariationMultiplierExponent` | 0 | Exponent setting for this recoil multiplier; native composition remains unconfirmed. |
| `ads.RecoilAmount` | 2 | Configured recoil amount for this aim state; effective native recoil remains unconfirmed. |
| `ads.RecoilAmountMultiplier` | 1 | Multiplier setting for this recoil component; native composition remains unconfirmed. |
| `ads.RecoilAmountMultiplierExponent` | 0 | Exponent setting for this recoil multiplier; native composition remains unconfirmed. |
| `ads.RecoilDirection` | 0 | Configured recoil direction for this aim state; coordinate convention and native behavior remain unconfirmed. |
| `ads.RecoilDirectionVariation` | 0 | Configured recoil-direction variation for this aim state; the effective distribution is unconfirmed. |
| `ads.RecoilDirectionVariationMultiplier` | 1 | Multiplier setting for this recoil component; native composition remains unconfirmed. |
| `ads.RecoilDirectionVariationMultiplierExponent` | 0 | Exponent setting for this recoil multiplier; native composition remains unconfirmed. |

**What we know:**

- The earlier ordinary M4A1 underbarrel paths reach separate M26 and M320 HE recoil owners. Recoil inputs are sourced; spread, timing, and active firing behavior retain separate limits.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-26-L81-secondary-recoil-inputs.json`, `frosty-2026-09-26-L82-L84-secondary-spread-inputs.json`, `frosty-2026-09-26-L83-secondary-recoil-recovery.json`, `frosty-2026-09-26-L82-L84-secondary-spread-inputs.json`, `frosty-2026-09-26-L86-L87-secondary-spread-protection.json`, `frosty-2026-09-26-L86-L87-secondary-spread-protection.json`.

### Launchers/Zipline — gadget group

**Research identity:** `launchers/zipline`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/Beacon — gadget group

**Research identity:** `misc/beacon`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/CacheGrabCase — gadget group

**Research identity:** `misc/cachegrabcase`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/DataExtractionCase_01 — gadget group

**Research identity:** `misc/dataextractioncase_01`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/DogTags — gadget group

**Research identity:** `misc/dogtags`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/DualPrimary — gadget group

**Research identity:** `misc/dualprimary`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The ability and modifier reference the same resource token and configuration child. The route does not reach a proved weapon-slot consumer.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L202-dual-primary-configuration-loop.json`.

### EOD Bot (CSB IV) — gadget group

**Research identity:** `misc/eodbot`. Classification: unresolved.

**Description (saved game text; supporting association):** Remotely controllable robot with various capabilities, including repairing vehicles and equipment, arming and disarming M-COM explosives, remote M-COM explosive arming where the robot will self-destruct on completion of task, launching cluster munitions to clear an area of enemy gadgets, and placing Anti-Vehicle Mines.

**Configuration:** `wb_eodbot`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |

**Configuration:** `wf_eodbot_primary_deminingcharge`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 2 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |

**Configuration:** `pb_ns_eodbot_clustercharge_mainmunition`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 4.9899998 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 5 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 4 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 11.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `pb_ns_eodbot_clustercharge_submunition`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 2 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 20 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 4 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 6 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**Configuration:** `wf_eodbot_equipment_atmine`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | 3 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | -1 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |

**Configuration:** `pb_ns_eodbot_mines`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `InnerBlastRadius` | 1.99 | Inner blast-region setting; exact composition with the falloff curve is unresolved. |
| `BlastDamage` | 150 | Base blast-damage setting; target modifiers, material effects, and final damage are unconfirmed. |
| `BlastRadius` | 2 | Outer blast-radius setting; physical units and effective damage coverage are unconfirmed. |
| `ShockwaveDamage` | 1 | Damage setting for a separate shockwave component; its active contribution is unconfirmed. |
| `ShockwaveRadius` | 4.5 | Radius setting for the shockwave component; units and effective coverage are unconfirmed. |

**What we know:**

- Deployment reaches demolition and mine weapon features with distinct blast profiles. Their effective damage and cluster behavior remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `gadget-ui-metadata.json`; `frosty-2026-09-29-L172-eodbot-payload-source.json`.

### Misc/IntelDroneController — gadget group

**Research identity:** `misc/inteldronecontroller`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/KeyCardDevice — gadget group

**Research identity:** `misc/keycarddevice`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/RespawnCallin — gadget group

**Research identity:** `misc/respawncallin`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/RevivePen — gadget group

**Research identity:** `misc/revivepen`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Configuration:** `squadrevive_wb`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `MagazineCapacity` | 1 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `NumberOfMagazines` | -1 | Ammunition resource-count setting; do not calculate reserve rounds or carried uses from it. |
| `InitialAmmo` | 10 | Initial ammunition setting. Negative values are special values with unresolved gameplay meaning. |
| `AutoReplenishMagazine` | true | Automatic magazine-replenishment switch; refill conditions and actual behavior are unconfirmed. |
| `AutoReplenishRounds` | -1 | Replenishment count setting; negative values do not establish infinite resources. |

**What we know:**

- The Squad Revive ability and value expressions reference six named revive channels. Actual restored health, timing, reach, and execution remain unconfirmed.
- Later resource work names the selected ammunition fields after a same-owner control. The counts and replenishment settings remain source configuration.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L181-squad-revive-channel-joins.json`, `frosty-2026-09-30-L217-support-resource-source.json`.

### Misc/SeismicDetector — gadget group

**Research identity:** `misc/seismicdetector`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/SOFLAM — gadget group

**Research identity:** `misc/soflam`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/SpecialMask — gadget group

**Research identity:** `misc/specialmask`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Gas-mask sources reference removal and duration effects. A separate blocking configuration references soldier channels, but the exact binding and effective protection rules remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L208-special-mask-duration-channel-source.json`.

### Misc/SprayCan — gadget group

**Research identity:** `misc/spraycan`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/SwitchbladeLauncher — gadget group

**Research identity:** `misc/switchbladelauncher`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/TrackingAntenna — gadget group

**Research identity:** `misc/trackingantenna`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/VehicleKeyCard — gadget group

**Research identity:** `misc/vehiclekeycard`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Misc/VestArmor — gadget group

**Research identity:** `misc/vestarmor`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### PlacedExplosives/DemolitionCharge — gadget group

**Research identity:** `placedexplosives/demolitioncharge`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### PlacedExplosives/ThermiteCharge — gadget group

**Research identity:** `placedexplosives/thermitecharge`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Supply/CorpseDropAmmo — gadget group

**Research identity:** `supply/corpsedropammo`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The projectile references a gameplay expression, an ammunition effect, and a resource token. The incoming drop owner, recipient rules, and actual refill behavior remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L209-corpse-drop-ammo-utility-source.json`.

### Supply/LootAmmo — gadget group

**Research identity:** `supply/lootammo`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Supply/VehicleSupplyCrate — gadget group

**Research identity:** `supply/vehiclesupplycrate`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Configuration:** `wb_vehiclesupplycrate`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `Field_14c4a054` | 1000 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |
| `Field_5bd8006c` | 1000 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |
| `Field_be31b12d` | -1 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |
| `Field_7f22bfb4` | 1 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |
| `Field_4614adfe` | 1 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |
| `Field_80a58418` | -1 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |

**What we know:**

- The weapon deployment selects a vehicle blueprint and a gameplay chain. Its ammunition and reload settings were read, but the refill and repair receiver remain unresolved.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L177-vehicle-supply-crate-source.json`.

### Throwables/RFJammer — gadget group

**Research identity:** `throwables/rfjammer`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Throwables/VehicleSupplyCrate — gadget group

**Research identity:** `throwables/vehiclesupplycrate`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Configuration:** `wb_vehiclesupplycrate`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `Field_14c4a054` | 1000 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |
| `Field_5bd8006c` | 1000 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |
| `Field_be31b12d` | -1 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |
| `Field_7f22bfb4` | 1 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |
| `Field_4614adfe` | 1 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |
| `Field_80a58418` | -1 | Stored raw field. Its role and units are unresolved; no player-facing stat name is assigned. |

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L177-vehicle-supply-crate-source.json`.

### Tools/BoltCutters — gadget group

**Research identity:** `tools/boltcutters`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Tools/GunsmithToolkit — gadget group

**Research identity:** `tools/gunsmithtoolkit`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Tools/HandheldRadio — gadget group

**Research identity:** `tools/handheldradio`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Tools/LaserDesignator — gadget group

**Research identity:** `tools/laserdesignator`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- Customization variants reference shared targeting equipment with different modifier contexts. Targeting interfaces and resource choices are sourced; selected payloads, target eligibility, and execution remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L197-laser-designator-configuration-joins.json`, `frosty-2026-09-29-L198-artillery-mortar-callin-selection.json`, `frosty-2026-09-29-L200-kinetic-gas-targeting-consumer.json`.

### Tools/MilitaryTablet — gadget group

**Research identity:** `tools/militarytablet`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Tools/RFRadio — gadget group

**Research identity:** `tools/rfradio`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

The group is retained in the catalog coverage list. Its gameplay routes have not produced a reviewed numeric stat or completed mechanic trace.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`.

### Tools/SniperDecoy — gadget group

**Research identity:** `tools/sniperdecoy`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Known stats:** No reviewed named numeric gameplay-stat field is available for this group in the retained evidence. Unnamed operands and source references, where present, do not justify an invented stat.

**What we know:**

- The regular decoy source reaches a projectile and a sound-patch reference. The sniper decoy reaches deployment expressions. Sound range, glint selection, spotting benefits, and activation conditions remain unconfirmed.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-29-L193-decoy-utility-consumer.json`.

### Underbarrels/M26Mass00Buck — gadget group

**Research identity:** `underbarrels/m26mass00buck`. Classification: unresolved.

**Description:** No verified descriptive text is assigned to this research group. The name identifies a research candidate; it does not establish its gameplay function.

**Configuration:** `pd_m26mass`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `StartDamage` | 8.3999996 | Damage at the beginning of the configured distance profile; effective hit damage is unconfirmed. |
| `EndDamage` | 2 | Damage at the end of the configured distance profile; effective hit damage is unconfirmed. |
| `DamageFalloffStartDistance` | 6 | Start of the configured damage-falloff interval; this does not establish tool reach. |
| `DamageFalloffEndDistance` | 25 | End of the configured damage-falloff interval; units and effective range are unconfirmed. |
| `InitialSpeed` | 350 | Speed setting on this particular projectile owner; it is separate from the weapon launch vector. |
| `TimeToLive` | 0.5 | Projectile lifetime setting; units and actual expiry conditions remain unconfirmed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |

**Configuration:** `wb_m26mass`.

| Field or setting | Value | What we think it represents |
|---|---|---|
| `RateOfFire` | 1799.999 | Configured firing or deployment cadence. Actual shot, tick, or placement rate is unconfirmed. |
| `MagazineCapacity` | 5 | Capacity setting in this firing owner; displayed loaded rounds or charges are not established. |
| `Shot.InitialSpeed` | [0, 1, 400] | Configured launch vector [x, y, z]. It is not a measured flight or throw speed. |
| `Gravity` | -9.8100004 | Gravity operand on a matched projectile schema; active flight behavior still requires validation. |
| `Drag` | 0 | Drag operand on a matched projectile schema; guided motion and other effects can remain separate. |
| `ReloadTime` | 3.53 | Stored reload-time entry; native selector, phase overlap, and effective total are unresolved. |
| `ReloadTimeBulletsLeft` | 3 | Alternate stored reload-time entry when ammunition remains; effective timing is unresolved. |
| `ReloadDelay` | 0 | Stored delay in a reload entry; its contribution to the effective reload is unresolved. |
| `ReloadSpeed` | 1 | Stored reload-speed setting; the active scaling rule is unconfirmed. |
| `PostReloadDelay` | 0 | Stored delay after a reload phase; native timing and overlap are unresolved. |

**What we know:**

- The earlier ordinary M26 source has a buckshot base projectile and a Dragon's Breath replacement projectile. Their direct-damage and falloff settings differ. They are not necessarily separate menu choices, and null direct-hit/second-curve pointers do not establish zero damage.
- The later configured weapon-shape pass matches the selected firing fields to weapon controls. It does not establish active equipment selection or utility effects.

**Still uncertain:** Exact UI-to-gameplay identity, current mode/loadout availability, native activation, units, and effective amounts or timing. Description claims remain untested unless a separate source finding above addresses them.

**Sources:** `gadget-coverage.json`; `frosty-2026-09-26-L73-m26db-source-profile.json`, `frosty-2026-09-26-L80-m26db-trajectory-inputs.json`, `frosty-2026-09-26-L81-secondary-recoil-inputs.json`, `frosty-2026-09-26-L82-L84-secondary-spread-inputs.json`, `frosty-2026-09-26-L83-secondary-recoil-recovery.json`, `frosty-2026-09-26-L82-L84-secondary-spread-inputs.json`, `frosty-2026-09-26-L86-L87-secondary-spread-protection.json`, `frosty-2026-09-26-L86-L87-secondary-spread-protection.json`, `frosty-2026-09-29-L201-m26-remaining-payload-route-limit.json`, `frosty-2026-10-01-L648-supplemental-gadget-profiles.json`; `gadget-weapon-profiles.json`.

## Additional UI records without a group association

### M320 Flash Grenade — unassigned UI record

**Research identity:** UI object 96; internal name `M320 Flash`.

**Description (saved UI text only):** A grenade launcher firing rounds that burrow through surfaces and eject a flashbang on the other side.

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `fa292429-4c80-49a9-b1ce-09e96b508918`.

### Thermite Sabotage — unassigned UI record

**Research identity:** UI object 110; internal name `F2P Thermite Sabotage`.

**Description (saved UI text only):** Improvised sabotage device which slowly damages a tank and its crew.

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `ef2c2f2e-5449-49e8-89e7-bde9ecddc7a2`.

### Goliath 90L — unassigned UI record

**Research identity:** UI object 145; internal name `Ammo Bag`.

**Description (saved UI text only):** A deployable bag that provides ammunition and medical supplies.

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `cbd4b73c-1eff-48f4-9989-de26443103d6`.

### Night Vision Goggles — unassigned UI record

**Research identity:** UI object 269; internal name `SP NVGs`.

**Description (saved UI text only):** NVGs

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `26bbc16f-be4e-4964-a0f4-4218e9d1fe9d`.

### EOD ATMine — unassigned UI record

**Research identity:** UI object 285; internal name `EOD ATMine`.

**Description (saved UI text only):** EOD ATMine Description

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `c3359d77-6974-4d36-bdb2-13b93d9a456d`.

### Non Line of Sight UAV — unassigned UI record

**Research identity:** UI object 293; internal name `nonLOS UAV Callin`.

**Description (saved UI text only):** UAV drone which spots enemy soldiers towards the direction you are looking at

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `92f5297b-a258-4dff-a440-8a8329289c3f`.

### EOD Demining Charge — unassigned UI record

**Research identity:** UI object 295; internal name `EOD Demining Charge`.

**Description (saved UI text only):** EOD Demining Charge Description

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `926fa67b-9c0c-4a3e-ad6e-1b4acb622439`.

### M320 LVG — unassigned UI record

**Research identity:** UI object 298; internal name `M320 LVG`.

**Description (saved UI text only):** Chambered in 40mm high explosive grenades, this weapon is ideal for taking out infantry. Can be carried standalone or underslung.

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `a55d5c7c-8b1d-41e7-ad43-a770cf3c0cbd`.

### Precision Airstrike — unassigned UI record

**Research identity:** UI object 403; internal name `Precision Strike`.

**Description (saved UI text only):** A fully automated indirect-fire Weapon System. It can target, direct and adjust firing solutions for 120mm mortars. It's a force multiplier for small units that do not have heavy weapon or close air support.

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `169cc9a5-428c-4f22-8dd6-fa5fbfba885a`.

### EOD PTKM — unassigned UI record

**Research identity:** UI object 406; internal name `EOD PTKM`.

**Description (saved UI text only):** EOD PTKM Description

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `971eaaa7-42b6-4d1a-9a4f-52c64cb3de09`.

### SURVEILLANCE DRONE — unassigned UI record

**Research identity:** UI object 459; internal name `SP_Drone`.

**Description (saved UI text only):** Can be placed for use by eliminated squadmates

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `c21e2fbd-e0bc-47ca-a688-cdc12e96b3d2`.

### X95 BRE — unassigned UI record

**Research identity:** UI object 463; internal name `Drill Launcher`.

**Description (saved UI text only):** A handheld launcher that fires breaching rounds which attach, and after a short delay, penetrate most destructible surfaces to deliver a blinding explosion on the other side. If the breaching round hits an enemy soldier, it will cause limited impact damage before triggering the same blinding explosion.

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `4a6322c0-86ad-4fb2-acf6-7239331b10fb`.

### EOD Repair Tool — unassigned UI record

**Research identity:** UI object 466; internal name `EOD Repair Tool`.

**Description (saved UI text only):** EOD Repair Tool Description

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `e3165dc1-69ee-45f3-9221-167554a02ff2`.

### LTLM II — unassigned UI record

**Research identity:** UI object 477; internal name `SP PLD`.

**Description (saved UI text only):** SP Target Designator.  Paints the target with a laser.

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `73820dc6-95b0-4eb4-b014-0a5718761282`.

### EOD Mini Lancet — unassigned UI record

**Research identity:** UI object 511; internal name `EOD Mini Lancet`.

**Description (saved UI text only):** EOD Mini Lancet Description

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `96c4bfd5-abfb-4c16-8473-99b2c6cb4867`.

### Protective Mask — unassigned UI record

**Research identity:** UI object 24; internal name `GasMask Class Gadget`.

**Description (saved UI text only):** A multi-filter respirator that, when equipped, protects the wearer from the disorienting effects of VL-7 smoke.

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `8688745a-6920-4586-b7fb-e988709a2020`.

### Portal Gadget — unassigned UI record

**Research identity:** UI object 51; internal name `Portal Gadget`.

**Description (saved UI text only):** Gadget that allows events to be raised from inputs, allowing Portal Creators to create custom gadget actions in script.

**Known stats:** No gameplay field values are assigned to this UI record.

**What we know:** The UI owner and its text identity were checked. The record remains in the fixed 78-record metadata scope.

**Still uncertain:** Exact blueprint identity, group assignment, multiplayer availability, and every effective mechanic. Label or placeholder text is not a mechanic description.

**Source:** `gadget-ui-metadata.json`; metadata GUID `76a409f1-55a8-47da-8200-f899f01d066c`.

## Source register

Source paths below are relative to the local research repositories. SHA-256 identifies the source file used for this document. Receipt files retain their own asset paths, hashes, offsets, bytes, build identities, controls, and review limits. Those details are not replaced by this summary.

| Source file | SHA-256 |
|---|---|
| `BF6 Datamining/reports/weapon-analyzer-research/2026-09-29T2025-0400-vehicles/L3007/l3007-result-v2.json` | `e3e00591787221ce1700a0db73fb2e179a09940098f5742b2d4d5815b6dafd01` |
| `BF6 Datamining/reports/weapon-analyzer-research/2026-09-29T2025-0400-vehicles/L3008/l3008-result-v2-authoritative.json` | `5aeb4f77d3e70a36184a8833b902ac43722a2861c421f9d226788fca65083b07` |
| `BF6 Datamining/reports/weapon-analyzer-research/2026-09-29T2025-0400-vehicles/L3009/l3009-result-v2.json` | `4ae34f0529807eb8e0545eed503cc49c7763b640778d4721427e5b4a6fe3eedd` |
| `BF6 Datamining/reports/weapon-analyzer-research/2026-09-29T2025-0400-vehicles/L3010/l3010-result.json` | `e7870ad1f176c4e196ef66cc224d1e355c59d83fad6c6ee22dd03cfaaf14de73` |
| `BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T234837-0400-gadget-vehicle-semantics/gadget-weapon-profiles.json` | `41115a110443ee8fb5dbf5cd1f47bafca0d12829fbf2e5787041d53e493ebe93` |
| `BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T234837-0400-gadget-vehicle-semantics/vehicle-weapon-profiles.json` | `2934c1cb9ffaf17bf101cada3e44669d6ed47ac055d674932df0c5d5ad79d0b0` |
| `BF6 Frosty Research/docs/working/VEHICLE_SITE_ADDITIONS.md` | `ec9d0a90535098e2aab0ced5c17f58c5b323d28c2b745de712560b8ca2a7ee37` |
| `BF6 Frosty Research/reference-data/frosty/gadget-coverage.json` | `0fb9700fa0052351a344b340b5ffeb433f343bf79a8281b2cb0263a72a6c4e4b` |
| `BF6 Frosty Research/reference-data/frosty/gadget-ui-metadata.json` | `df460ff16c074d725710a8c749e5e4928878b77f7e20aa61635812d52b50f2eb` |
| `BF6 Frosty Research/reference-data/frosty/vehicle-coverage.json` | `2e58fcb2ed8f596795d5cec592d5bf68e5d16f94ccfb770d566bfe8ccc372df1` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L71-m320-he-at-source-profile.json` | `836ce4ce54f504ed6a43e3a76fd52c75532ff4c2db0abe9c72199414de20aa56` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L73-m26db-source-profile.json` | `32c0c62b3becf8cbff176505af4517cb3cf59b191b8eca1fa2e2258bee580d62` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L75-m320-explosion-naming-limit.json` | `5a472bcf994ea7425d0c3bd58c7e7e75b1c028e6c9a9b5ad1c9aaf158d2db395` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L76-m320-he-firing-inputs.json` | `b6828e22c4375c0d304cc52fb565baf585f9ea8c59fa9f0df1a8f1421449c7a0` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L78-m320tb-explosion-profile.json` | `116f9ca4fc3b36948d8c69e82ff1dbbb6ec17fa7ae88aa0b33e8b3dc07e0b049` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L79-m320-explosion-name-limits.json` | `40693a4b87d9dd96ef2378e0e70e52024d38a41f7c40a775844e5010ae59274e` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L80-m26db-trajectory-inputs.json` | `c9d0c96bab6dedbec7cae7e3290cca7ade548648f39c1567e4e3ec67fe7357cc` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L81-secondary-recoil-inputs.json` | `b12f79bbc8191c4e21bbd815a9debc6032cf99ccd35d937934d1950df658b633` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L82-L84-secondary-spread-inputs.json` | `77106a894bc982f7664a092fbb14a18ae905c80b4222d1019a5fe03f0983699f` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L83-secondary-recoil-recovery.json` | `df2223c8789aab1a882c24530192a60ba226cf5fa1b5ee85cb4a758a7a87bcd8` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L85-m320-shockwave-input.json` | `c9287a3e6d3197d7214b955996060deac1eddf15a05e1d616cf78b1af702476d` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L86-L87-secondary-spread-protection.json` | `f5efc185a1d85b398944bfb447cede10f3f5365a6635e18c4762f45158f3cf9c` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-26-L88-m26-m320-configured-ammo-counts.json` | `677b4d51280d26c0d769bffdbfeb46b95ef2e51cb47b41a5f547ae4bc8ed8a56` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L137-launcher-handling-ammunition.json` | `ba6823bcbbf2e998b3dcfac8a57468e98d3c91729a580814f7155550ac5dc65a` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L138-mine-trigger-source.json` | `f49647932b0bfa8c742910efe41f95a3c21f73d09434e96ed213310abb040f74` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L139-defibrillator-source.json` | `5d3a9decbbcba97bb9e19042b3c2d54a93db60cdfa44383aff9b04e60d95d11e` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L140-tugs-detection-source.json` | `d895b8814100a23f6e6bf427b4af0fe7f25fd6e89cdd325ce50bd273e3edb166` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L141-cover-durability-source.json` | `34bdbb54599144c077507b04668d57f4a3ab683120e37a5cd686d2ed2fdc1267` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L142-concussion-effect-envelope.json` | `14be1d7430aeddd52a5c753931107e2c3c6af27012647a1d47eaaa4efdfaba1e` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L143-supply-crate-ammunition-source.json` | `9ef0e07cae5a2137d1c670890f019548f90335571cb77968729efb8d37761dc3` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L144-tracer-dart-lock-source.json` | `bf5299d7532c33aa993735c51c27b6382b1b39ade1a6e51b87d5f1b601391901` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L145-spawn-beacon-source.json` | `d43a642e4daeedf0d3a513d3477b973692d4db323555e182aab8ccd1408c20e0` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L146-smoke-grenade-source.json` | `5e86cac8d9108cc8a2373902cf829588bdcfeb25a7c8589992be2484a1fffae1` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L147-adrenaline-shot-source.json` | `db0aafab7cb72cc54a46b3b1fedf687217b075994c513b383702d6f350c96319` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L148-frag-miniv40-blast-source.json` | `90bd591bf7658aef387e9e36e1a2d0840821585447e37df8d7d8e9f8198219c0` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L149-pld-marking-source.json` | `08e184d4fc8f6972408b8fc15d4ed22fda9a0fdf30c50562f50b02037f785a78` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L150-antitank-blast-source.json` | `60e41a8b69c0a5b4475c334ec63742e3f9fb084a1143598765250e7f6030fddf` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L151-c4-blast-source.json` | `4b82be3df8a6edd3b9f41033492fdef02f71ba839c6a12b44cfe33467f8f0487` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L152-launcher-projectile-source.json` | `e6f8b71c242de31f2607cacf15c729a0af8bab34895efcf4b9ac85ea471efc35` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L153-mine-blast-source.json` | `9f9f9ebd6153d67fdc27a7c565bd11bb25790a6bbe9f1f91ee743527a6f80f51` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L154-incendiary-source.json` | `3f5cc19948b4db2ae2a777821957820be949db76c367a0862dcdee7f079098ab` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L155-flashbang-effect-source.json` | `89710837526c423eaba29697e9ede2a860c3f2542709667037b7ff277649b2c4` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L156-throwing-knife-source.json` | `67e0d5742bd508808735f021bc53817c6bdb63a54001ffcdac47ed6c74abf393` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L157-supply-pouch-source.json` | `fe35b7105bebb47c0836920405b5c84c469bc6f657f6005db2c49b88c7569634` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L158-proximity-source.json` | `cca2265ad39788329a146c494fa7073aa72e9dc1566c4abdd030622878032a2d` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L159-breaching-dart-source.json` | `1f99b5ee2f33dab9e9e9b3f351b57f44e37c0cf13ff4b2d4447101210cd6e1f2` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L160-gas-mask-source.json` | `02650707ad30f7bd3c04c1986665b9d24bae06c0e5dd3cfdf9ffd78c276b3720` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L161-gadget-handling-source.json` | `62e5315a1c0829a22857967a6925350c22d9463daa58cb13d78dea048b5a818e` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L162-stinger-igla-source.json` | `b6a7a2a7263bd9a25c29f2757838cdc14baefa5768731c13776e39acef8a44a5` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L163-airburst-incendiary-source.json` | `1860536fcad1d20c9b9919fbf8e53e1f1ff0c529bce295967e427f6bda4a4da4` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L164-claymore-blast-source.json` | `f48f8919338f01417d6c2ffd1846af777aac2e3add73cdbbc578ad7cbfa85dd0` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L165-ptkm1r-projectile-source.json` | `91abe4ee790450af49b4cbda177ab614daab3158491ce8c9a195de261e805fb1` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L166-throwable-ammo-launch-source.json` | `dbb44328cdfac5c5a59cca8966fcb64172bb16019a4c578dff85f95699a8868a` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L167-javelin-source.json` | `4621e15b911293d26f9abf10f2b79f3131060f5e269525fca8b31ebcf9b478e8` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L168-panzerfaust3-source.json` | `18f941264aca26dcaa18f992dd68a2826b0c2a01883586706de4cb3160d55fe0` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L169-mortar-source.json` | `a9f0894cd39acc5b176ffc1ddcec39fabf25737360f480a864a17ff4374660c0` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L170-drone-payload-source.json` | `d0102543b28cdfcd436b401b5b57aa983b9855c0604a2a62d7bb173b278ac9e1` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L171-mpaps-eidos-resource-source.json` | `13111a75c8222af1ad2dd7dd273037b4276016325a0a1399c8be27202c244089` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L172-eodbot-payload-source.json` | `cc365976416d91caf73b9f145441e29f7286060a133a8720e7eedc28f8a2432b` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L173-mobile-jammer-source.json` | `8c3ef1382212c71e03af8ee3a778a0c9821a9e14b0499b098b161bea342c046e` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L174-repair-tool-source.json` | `0fdf6ae32d2f2418e53f4a4bb463f4d752028d474e8a70eeb6b5c1e24434e8f0` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L175-minigun-source.json` | `d3c61768b3357dd2aef36b1de628ff683e4b5313fcefbf3dc901554f3b7cd16d` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L176-utility-throwable-resource-source.json` | `fa77d47f112ae5ae1fd5c4d5e56c28a7481b4e323010945d4f5ae16b0d92fbd4` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L177-vehicle-supply-crate-source.json` | `90f1f5133380953f8d6d8c14ee7115b4eebf206ad8bc5a39d80519feb15e117f` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L178-ladder-deployment-source.json` | `28c2c093ec422db4f1596bd19b7c61109d28226fefcd109270d83e090e63f355` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L179-armor-resource-joins.json` | `4f9521b0cdc3c4e48cce33a0dd936d79f1f2f06338bba27056f4bfd4d0c43f17` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L180-railgun-source.json` | `60c486baac85ab6b6ef1599caf5017fc6cbd6ac2ac22e3393f3c1c3c78f9041e` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L181-squad-revive-channel-joins.json` | `bf339d229ea7778ec8c39be7167c626eed538579c526f130b82dcd3aa116c017` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L182-nvg-resource-source.json` | `b1c7895bd2abf6f88861bd6bae9821fab8d0d73a3dbc257709f7232fb543b05b` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L185-repair-utility-consumer.json` | `4ba3350b4bc711494c54135d03eb1458191731dc8e38ab7bcce486e75706d665` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L186-supply-utility-consumer.json` | `f24789018fb0f2dd70c66420a80584ed80ddbe08adac799db7a7995d8ab88ca2` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L187-defibrillator-revive-consumer.json` | `65f0a2191aafe31936f42841b40a76bbbebd671701706a4e8305d74af644e3cc` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L188-assault-ladder-interaction.json` | `d3d59b5263726072a61ba02946d6ee8a893dda236ad1b57f4f299366cbc92341` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L189-deployable-cover-protection-consumer.json` | `8be8b2113923c45d3533ae43ae547206ae7373172bf50b60faf61c6ac9163204` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L190-utility-compiled-reader-gate.json` | `b8b91e6481ff6e158603352d50d798bbeeea0757c84d0e219d8f7044bef9c324` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L191-uav-overwatch-utility-consumer.json` | `4ec265bb33d1898ac4cf3c7ef8f73c232b64683a4db11e998a226508551cda45` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L192-logistics-utility-consumer.json` | `00ca9c750a953db80aac59fafc878cae0a51b86aca9392ad5b99affe0e91fa54` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L193-decoy-utility-consumer.json` | `74f4c5c8c78fbb23ee30c1677c2de88550f88f44aa7ef98e6b3ce13dcc2b8414` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L194-medic-crate-healing-consumer.json` | `20f1b6e71cd14a5608204c69a97f2d4f949af0a924a5b839b10821239d18dd5c` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L195-m320-smoke-selection.json` | `42357397e3a8278b1d3e78a0e7d2d09f2efb5ef9baf13830e9aa220397928a18` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L196-smoke-screen-callin-consumer.json` | `19c3d513135d21ead5a50f1e1bf4ca3ac69c51989a2dba113a47e075076141be` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L197-laser-designator-configuration-joins.json` | `07d888748436bd1dbea707fc910bdce70d9e5fd158e236fdaba3743aab5af485` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L198-artillery-mortar-callin-selection.json` | `59ff5f24414471da327e186d2b49063b4f0a4318fe33752392f911970384aa4a` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L199-air-jagm-callin-selection.json` | `3a489907eebfe9b4710c06f91faf3ce68b3dc52546619070d1c173afe09e6708` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L200-kinetic-gas-targeting-consumer.json` | `43ddafdeb76940883be5d9f29111e5ca5b15623a43253d4c9e4c8dff782b30f5` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L201-m26-remaining-payload-route-limit.json` | `a0e06c6d78f46888b048c22a29059d883fd70bd45f1bdc984921ac8537e5c5b1` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L202-dual-primary-configuration-loop.json` | `1b35f0fc1e2e3ac3a525d3ff8f8c86967ef072317c780b01fc71e8628f5f18fe` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L203-data-extraction-tablet-configuration.json` | `7364cb6a05efee3e9b3585ee1b42aec75eb94e2ef4403cec2f197bff0b43eb9b` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L204-recon-drone-tracking-source.json` | `8e4f5d8cce8b8a387cb0f24dc3e9ee0cd9524e3b6c32ab27c8e1e89b9efb23e0` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L205-drone-utility-source-consumers.json` | `f5dcc499be91594e2ace007f2b91ff00778a318f211622d59078520a9d893f4e` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L206-sp-payload-drone-deployment-source.json` | `378364658ef99677b6b0ef0d13e667826dbce5abe64a5f7a8be9cd7af548d683` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L207-naval-gadget-dependency-source.json` | `6cc507648ef8571d64eca0a8d10f7f0a8eb1e370952cd52d2726e01432e5b0c9` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L208-special-mask-duration-channel-source.json` | `f99099ec8dfed1db50cb9aaed1fd65e1b031ef2cfcb9f81f4e830413f478b156` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L209-corpse-drop-ammo-utility-source.json` | `b64acd8530c90acdd5919188b405d957a9e61f270aabadd4bab82fe964ef90ad` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L3007-vehicle-air-pilot-continuation.json` | `25e4f2e683bb34b5b9d249c64ec0d435ce1ae6ddc56a7899f10ccf45d2ad1e24` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json` | `e936fc12a88b727dc1f5016cf48fbc5182035783af59884b7bbc6c28f2894e69` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json` | `1e70621f19f5a35da85db42d783dbfaf9dfffe3545b241d16e3c4e7b8244c491` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-29-L3010-vehicle-ground-continuation.json` | `60f230c9d8cce7a2caa91202202703aef869ef33172a9371e2697132ac5d4ef5` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L216-deployment-resource-count-source.json` | `18a1cc62adfed3948d6af63a8e9ff49a71709a585b3c02ba141fdd1811123822` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L217-support-resource-source.json` | `adceb5a468cc132ec7d6816df15b38362749e75650c9cace280f1c6c18fc1969` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L218-supplydrop-resource-binding.json` | `789be967c825400942d4f710a0d9fa3ace7f7aff97ab40e952460aa55881e132` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3018-vehicle-stat-map.json` | `b36c3433f8436b06753fa780e7a69facf68894ad49b8d64f0d2d0540cf62c629` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3019-vehicle-configured-stats.json` | `f27e6f1b47b32b01e52d1dede855af04fc5e76a9e6b01b696298847ee5fcddfa` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3020-vehicle-configured-stats.json` | `400d62117928113e12069256f07ae6c38ab890904e6f9e880fc8b92b869744da` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3021-vehicle-configured-stats.json` | `091879a579bba4122b96dc2fca3ab6b43400be3ebe56727527b5f456c073dafc` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3022-vehicle-configured-stats.json` | `92f919d9ccfdda37f3a33d239ab490a6eeee4af8554b9916706375abbc9b57c2` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3024-health-own-wrapper-check.json` | `2428c43bd37fdf66538ad8b92b00b5dbeb333f6d15c8b731bed0bb3b9fa3c7f0` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3025-vehicle-configured-stats.json` | `0a7972ed5da9bac65bc9d2718eab3b8d12148080e6503f3deefe4ed10ffd3a98` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3026-vehicle-configured-stats.json` | `3f226aa84c804169ef946c463039074d58e3225945d3584d337ceb1b2e57f387` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3027-vehicle-configured-stats.json` | `501db7d7e1e12dfb9d6fd38ccfe67f59ee6c5594b6080252f7da97aa0135f021` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3028-vehicle-configured-stats.json` | `f90d98cb85084d0e632893be216345a69a38dbf101004c62b01d373693fe464d` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3029-vehicle-configured-stats.json` | `d6dfe1e813d9d31e2771ccbc1fd418d163b9cd1ac2fd36db63063ae79d7bcc41` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3030-vehicle-stage2-closeout.json` | `1dca45d15c0a5a91312ffb8c062e51c5b2fde63305aa40cdc4376f54583a0dda` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3031-vehicle-mbt-ui-root-join.json` | `a920c7612a12ba1209462fe7928cb803654f9a0491f1bdb6fd7bf6eac23c3f5a` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-09-30-L3032-vehicle-ui-category-root-join.json` | `9c933800b9f0c6cfd537ca4b3145c7d6c873698dfdbd0cd065a6cfb528de7af5` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-10-01-L641-weapon-shape-profiles.json` | `6517b549ff989447e0097eb23634d71fc84e8c4c70580929cb320dd07f6ff9da` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-10-01-L642-weapon-shape-profiles.json` | `4c4d953408275999b12fb6167dcfd8624f231221d85d8025aa3bdf58e1d16f26` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-10-01-L643-weapon-shape-profiles.json` | `f9eb8cb2f76ac6f45f13093440735d01c6691c49f588b78e2e450543722593a5` |
| `BF6 Frosty Research/reference-data/provenance/frosty-2026-10-01-L650-aa-scout-preupdate-baseline.json` | `566dae15b2a3c523328f4d54b922d13a90e1aab141444d36ee3bf4a55844b4cb` |
