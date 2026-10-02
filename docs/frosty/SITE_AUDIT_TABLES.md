# Remaining site data audit, 1.4.3.5

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T2359-0400-site-audit-tables/`. Reserved leads: L700-L739. Current build: 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`.

The [L700 census](../../reference-data/provenance/frosty-2026-10-01-L700-tables-audit-census.json) covers seven files. The orchestrator completed Stage 1 without workers. It records 69 numeric or Boolean field families in the four CUR files, including 35,832 numeric leaves. Existing September field reviews cover their values. The three Precision RPM leaves changed since that review are accepted L107 precision edits. The source-backed table operands carry forward by raw hash with their original Head 4892017 retained. The external census lists every family, owner, prior receipt, exclusion and raw-reuse group.

`balance_tables.json` covers ordered ADS, deploy/undeploy, sprint recovery, movement and spread rows, hip base selectors, recoil multipliers, reload and velocity factors, health regeneration and collateral overrides. L125 supplies the later FZT General_01 comparison for the ADS-in ladder. L107 declined the older AZTT-plus-two-frames precision route and all 66 draw/sprint conversion edits. Source row values do not prove native composition or activation.

`weapon_attributes.json` has 39,946 reviewed Precision values, four reviewed shotgun dispersion inputs, two reviewed L115 base coordinates and two panel/model grip zero overrides. The zero overrides retain their unresolved native receiver. `reload-exceptions.json` retains five animation override entries, the documented PP-19 Fast Mag game bug and the operator's composed-loadout observation. L107 left the integer millisecond override contract unchanged. `recoil_decay.json` retains 134 reviewed map values; current `sim/core.js` declares the maps but does not read them. These maps have no displayed effect.

ADS/deploy/sprint base coordinates are stored in `attachments.json` under `WEAPON_MAG`, not in `balance_tables.json`. They have earlier source selector reviews and belong to the attachment audit. This audit covers the tables and the Mobility extras in `weapon_attributes.json`.

Three GEN hash-only leads are complete: L701 ballistics, L702 hit zones and L703 tooltips. Seven recorded Killswitch input hashes differ, and some graph input routes have no current raw file. These are input-hash findings, not displayed-value proposals. No generator was rerun. No site data, simulation or UI was changed. No in-game test or push was run.

## L701 ballistics.json generator inputs

[L701 receipt](../../reference-data/provenance/frosty-2026-10-01-L701-ballistics-input-hashes.json). 4276/4286 recorded raw inputs equal 1.4.3.5; seven Killswitch hashes differ and 3 historical hashes are unavailable. No displayed-value proposal. Hash controls passed; worker scope 10/10 passed mechanical review. The parent independently reread one consequential changed raw hash.

Historical raw hashes for the three blacklight graph routes are unavailable. One current WPM capture was found by L703 in the concurrent ammo run, but it cannot replace the missing historical hash. No generator was rerun or capture started.

## L702 hit_zones.json generator inputs

[L702 receipt](../../reference-data/provenance/frosty-2026-10-01-L702-hit-zones-input-hashes.json). 4278/4288 recorded raw inputs equal 1.4.3.5; seven Killswitch hashes differ and 3 historical hashes are unavailable. No displayed-value proposal. Both original grid streams match; descriptor raw hashes differ. Hash controls passed; worker scope 10/10 passed mechanical review. The parent independently reread one consequential changed raw hash.

The original Abbasid and Badlands raw grids carry forward exactly. The descriptor changes from `91c9ea7c...565c2` to `4c28ad65...16a1`. The old receipt remains an old descriptor decode; equal grid bytes do not verify a new descriptor decode.

Historical raw hashes for the three blacklight graph routes are unavailable. One current WPM capture was found by L703 in the concurrent ammo run, but it cannot replace the missing historical hash. No generator was rerun or capture started.

## L703 attachment-tooltips.json generator inputs

[L703 receipt](../../reference-data/provenance/frosty-2026-10-01-L703-tooltips-input-hashes.json). 7614/7628 recorded raw inputs equal 1.4.3.5; seven Killswitch hashes differ and 7 historical hashes are unavailable. No displayed-value proposal. Localization TSV differs; all 1067 supplemental AAM/descriptor raw inputs match. Hash controls passed; worker scope 14/14 passed mechanical review. The parent independently reread one consequential changed raw hash.

The first Stage 1 generic collector omitted 64 AAM and 1003 description-descriptor inputs. The supplemental check found all 1067 raw inputs equal. The original census and its raw artifact remain immutable; this receipt records the expanded 7,628-input scope. The original and current English TSV hashes differ. No text difference or semantic consequence was inferred from that hash.

The three blacklight graph routes lack historical raw hashes. One current `WPM_RGT_Blacklight_W10` capture was found in the concurrent ammo run; the other current raw files were not found in the bounded search. Tooltip-only scope inputs add four recorded RagingHunter/TRR8 sight routes with no historical raw hashes. No generator was rerun and no capture was started.

## L704 used tooltip localization text

[L704 receipt](../../reference-data/provenance/frosty-2026-10-01-L704-used-tooltip-text.json). Clean family: all **413 used localization IDs** have exactly equal text in the old generator TSV and 1.4.3.5. All 413 IDs exist in both files. There are **zero changed texts and zero missing IDs**. The other 18 description keys begin with `screenshot:` and are reviewed panel overrides. They are not localization IDs.

The receipt records each `data/attachment-tooltips.json:/descriptions/<ID>` path, old/current TSV lines and all site selection paths that use that key. The known September field-review control `0099DD29` passes and equals the current site text. The global TSV hash difference does not make any of these tooltip texts stale. No text correction or new proposal is supported. Only the requested used IDs were retained from the TSV scans.

## Run close

L700-L704 are complete. L705-L739 are unused. The original census remains immutable; `census-final.json` includes the supplemental tooltip inputs and L704 follow-up. No class (a) difference or new Analyzer proposal was established. GEN hash equality is not complete for every recorded input: seven Killswitch raw hashes differ, seven routes lack historical raw hashes, and localization/descriptor inputs differ. The 413 used localized tooltip texts remain exactly equal. All seven site data files retain their run-start hashes. No generator, site data/sim/UI edit, in-game test, capture or push was run.
