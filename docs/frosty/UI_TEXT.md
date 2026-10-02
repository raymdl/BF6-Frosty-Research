# UI text: names, descriptions and labels

[Frosty docs](README.md) · [Field map](FIELD_MAP.md) · [Tools](TOOLS.md) · [Data sources](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/DATA_SOURCES.md)

How the site resolves English weapon names, attachment and optic names, labels and
descriptions from BF6 game data, and what the current site mapping contains.
The gadget section records captured 1.4.3.1 text separately from site data.
Snapshot: 1.4.2.5 export (13–14 September 2026), strings rechecked on 1.4.3.0.

Results:

- [frosty-weapon-display-names-2026-09-13.json](../../reference-data/provenance/frosty-weapon-display-names-2026-09-13.json)
- [frosty-attachment-descriptions-2026-09-13.json](../../reference-data/provenance/frosty-attachment-descriptions-2026-09-13.json)
- [frosty-optic-render-fov-2026-09-16.json](../../reference-data/provenance/frosty-optic-render-fov-2026-09-16.json) `opticNames` (in-game names of 42 optics)
- [weapon-descriptions-2026-09-13.json](../../reference-data/provenance/weapon-descriptions-2026-09-13.json)

## 1.4.3.5 text check (30 September 2026)

The 109,195-row current English strings export is byte-identical to the recorded
1.4.3.1 table: SHA-256
`1ec449fa2a12bc3d307bfa5878ee7d8c56af14fae65ea1f6c6286e85d98e7392`.
Current label and description roles were decoded for 1,004 AD metadata assets and
resolved against that table. Their raw bytes are unchanged. All AD metadata has
layout ambiguity, so unchanged decoded fields alone are not the stability proof.
No generated old tooltip file was used to verify new wording. Evidence and limits:
[update receipt](../../reference-data/provenance/frosty-update-1.4.3.5-2026-09-30.json).

## Why the XML export is not enough

1. **The text is not in EBX.** `Common/Localization/Languages/fs_us_loc` is a small EBX
   record with two chunk GUIDs. The strings are in those binary chunks, which the XML
   export does not include. Export them with `FrostyCmd export-strings`
   ([Tools](TOOLS.md#frostycmd)).
2. **The weapon name links are not in the blanket XML tree.** They are in
   `UIWeaponAbilityMetaData` assets, which must be exported separately.
3. **Field names are hashed.** Tools that look up fields by name (`StringId`,
   `StringHash`, `LocalizedStringReference`) find nothing in BF6. Read fields by type
   and structure.

## The strings table

`export-strings` writes about 109,000 lines of `XXXXXXXX<TAB>text`. Tabs, carriage
returns, line feeds and backslashes in text are written as `\t`, `\r`, `\n` and `\\`.
This is English only; other languages use other `fs_*_loc` assets.

How the asset is decoded (same logic as `FsLocalizationPlugin.AddResource`):

1. Load every `Guid` property of the language asset's root object as a chunk. The two
   field names are hashed, so find them by type.
2. The chunk that starts with magic `0x00039000` is the string chunk. The other chunk is
   the histogram.
3. Histogram chunk: skip a `uint`, read `size` (`uint`), skip a `uint`, then read
   `size / 2` values of type `ushort`.
4. String chunk: read magic, size, one skipped `uint`, `dataOffset` and `stringsOffset`.
   From `dataOffset + 8` to `stringsOffset + 8`, read pairs of `uint` id and `uint` offset.
5. For each pair, read a null-terminated byte string at `stringsOffset + offset + 8`.
   A byte below `0x80` is the character. For a byte `b` of `0x80` or above, read
   `tmp = histogram[b]`. If `tmp` is `0x80` or above, it is the character. Otherwise read
   the next byte `b2`; the character is `histogram[(b2 − 0x80) + (tmp << 7)]`.

### String id hash

String ids are hashes of text keys: djb2 with seed `0xFFFFFFFF`, on 32-bit unsigned
values, `result = char + 33 × result` for each character.

```js
const hash = key => {
  let r = 0xFFFFFFFF;
  for (const ch of key) r = (ch.charCodeAt(0) + Math.imul(33, r)) >>> 0;
  return r.toString(16).toUpperCase().padStart(8, '0');
};
```

Of the 1,231 `ID_…` keys in the XML export, 1,157 hash to ids in the table. Weapon name
keys: `ID_ABILITY_<internal name>` (53 weapons), `ID_ABILITY_MP5` (PW5A3),
`ID_ABILITY_MSBSGROT` (GRT-BC), `ID_WEAPON_<internal name>` (EF88, VSSM, BROD 3) and
`ID_WEAPON_HTI` (Interdictor). Key guessing does not find L115A3, MSBSGROTCPS,
RagingHunter or RPK74M, so use the metadata links below; key patterns are supporting
evidence only.

Other hashes: delegate argument names use djb2-xor (seed 5381, case-sensitive; all 14
named arguments agree). `Field_`/`Class_` names use a different, unknown hash
([Field map](FIELD_MAP.md)).

## Weapon names

### Export the weapon UI metadata

```text
Common/UI/MetaData/UIWeaponAbilityMetaData
Common/UI/Static/Metadata/S1/UIWeaponAbilityMetaData_S1B1
Common/UI/Static/Metadata/S1/UIWeaponAbilityMetaData_S1B2
Common/UI/Static/Metadata/S2/UIWeaponAbilityMetaData_S2B1
Common/UI/Static/Metadata/S2/UIWeaponAbilityMetaData_S2B2
Common/UI/Static/Metadata/S3/UIWeaponAbilityMetaData_S3B1
Common/UI/Static/Metadata/S3/UIWeaponAbilityMetaData_S3B2
Common/UI/Static/Metadata/S3/UIWeaponAbilityMetaData_S3B3
Common/UI/Static/Metadata/S4/UIWeaponAbilityMetaData_S4B1
```

Newer seasons can add assets; check the manifest for more `UIWeaponAbilityMetaData_*`
names. `S3B2` is an empty container in 1.4.2.5.

To find the assets again after a large update, run `scan-string-usage` with the ids of
the strings whose text equals each site weapon name, plus a control id (for example the
hash of `ID_OPTIONS_HITSOUND_LABEL`, used in
`Common/GameSetup/Options/Audio/OptionHitIndicatorSound`). The scan walks public
properties, lists and structs to depth 8 without following pointers, and records a hit
when a `CString` hashes to a target id or an integer field equals it. On 13 September:
70,678 assets, 536 unreadable, about 3.5 GB and 7 minutes; 63 of 64 name ids were found,
all in `UIWeaponAbilityMetaData`.

### Parse the links

1. Every `Class_593f6146` object is one weapon record.
   - `Field_55aded8d`: a text label. It is **not always** the internal name (`SCAR-L`,
     `Tavor 7`, `ACE 32`, `DP-12`, `Mini Fix`, `GrotC`).
   - `Field_ebe3976f`, `Field_53078b86`: package image links such as
     `T_UI_SVCh_PKG_Factory`. The part between `T_UI_` and `_PKG` is the internal name.
   - `Field_fd698f51`: pointer to a `Class_fbe1d3bc` object.
2. That object's `Field_3d34898a` holds the name string id (for example `0xa77ee5e5`).
3. Look up the id (uppercase, 8 digits) in the strings table.
4. Link the record to a site weapon: match the image internal name to `internalId` in
   [frosty-weapon-identities.json](../../reference-data/provenance/frosty-weapon-identities.json),
   ignoring case. Without an image link, match the label with punctuation and spaces
   removed (`DP-12` → `DP12`).
5. Check that each site weapon has exactly one game name.

After an SDK change, find the same structure again: a record with a text label, package
image links and a pointer to an object that holds one 32-bit id.

### Apply and check

1. Update `name` in `data/weapons.json` and `siteName` in the identity map together;
   `scripts/frosty-configuration.py` requires them to be equal.
2. Do not rename screenshot folders. The audit scripts compare names without case and
   punctuation.
3. Run `node scripts/validate-data.mjs` and the tests.
4. Write a dated provenance record with the ids, names, source assets and hashes.

### Result

- All 63 site weapons link to their in-game name (for example `HK433` → M433).
- Three site names were corrected to the game spelling: **TR-7**, **SOR-556 Mk2**,
  **vz. 61**.
- `KSG` is the **KSG-12** and is not on the site.

| Case | Handling |
|---|---|
| GRT-CPS (`MSBSGROTCPS`) | Label `GrotC`, no image link, in `S2B1`. Id `A7711B37` resolves to GRT-CPS. |
| AK4D | Two strings read AK4D (`8F929007`, `B77F06A7`); the metadata uses `B77F06A7`. |
| `SCAR-SC .300 BLK`, `MP7A2 SP SUPPRESSED` | Variant records of SOR-300SC and PW7A2, not separate weapons. |
| Mini Scout, DB-12, GGH-22, M357 Trait | Two records each. |
| Sym and Companion names | They use old spellings. Recorded Sym `displayname` values stay unchanged. |

## Gadget names and descriptions

### Export the gadget UI metadata

```text
Common/UI/Static/Metadata/UIGadgetAbilityMetadata
Common/UI/Static/Metadata/UIGadgetAbilityMetadata_S2
Common/UI/Static/Metadata/S3/UIGadgetAbilityMetaData_S3
Common/UI/Static/Metadata/UISoldierLoadoutPresetMetadata
Common/UI/MetaData/UIPlayerAbilityDescriptionMetadata
```

The operator captured these assets on 1.4.3.1, Head 4892087. The parent folder
is named `1.4.3.0`; that name does not identify the captured client. Use the
capture identity and descriptor hash. L219 uses descriptor SHA-256
`99b49cfd8bdb5bb6f0181df8ac0d93a0396c1b7f07a1ba3ce8ca1cea45969640`
and the `pre-update-1.4.3.1-2026-09-29/fs_us_loc.strings.tsv` capture.

### Parse the links

1. Decode the three gadget metadata files with the pinned descriptor. Keep all
   78 records, including SP, EOD sub-tool, mode, placeholder and missing-text
   records. L219 identifies the main owner as `Class_8680e440`, with exact
   type key `3b1ec1ab4a3bfb39a85b2dbf937536cc`.
2. Read `Field_55aded8d` as the internal text label. Resolve local text pointers:
   `Field_33a358a7` (short name), `Field_70b5525f` (display name),
   `Field_490f0dd0` (description), `Field_f8c63ce7` (short description/category)
   and `Field_fd698f51` (alternate in-game name). Keep each field separately.
3. The selected `Class_fbe1d3bc` object has the string id in `Field_3d34898a`.
   Look up its uppercase eight-digit id in the pinned TSV. Preserve the exact
   escaped TSV text, its line and id; do not silently repair encoding.
4. Raw-check the pointer, selected object and string id. For example, AT Mine
   resolves to AV Mine, Anti-Vehicle Mine and M15 in the respective fields.
5. Record asset links separately from text. `Field_53078b86` and
   `Field_ebe3976f` are image imports. In this descriptor,
   `Field_1636b8bd` is a `UINT32[]` field. It is not an import pointer.
   Name matches and image names are supporting evidence only. A blueprint or
   ability join requires an exact source identity edge.

### Apply and check

1. Resolve the table independently before use. Do not run the supplied
   `gadget_table.py` in its source folder: it overwrites decoded outputs and
   the candidate table. Write independent outputs in a new lead folder.
2. Compare all 78 records, field by field, against the candidate table. Record
   missing ids and exact text differences. Keep unlinked records visible.
3. For coverage, record class loadout preset presence or verified player-facing
   metadata presence under the operator's approved rule. SP, EOD sub-tools,
   Portal and placeholders do not establish multiplayer availability by
   themselves. Preserve the evidence basis and unresolved identity joins.
4. Add a concrete check and prediction for a description's number or rule.
   Compare it to the selected source value only after the gadget identity is
   established. A description is a documentation claim; it is not a measured
   mechanic. Do not start in-game tests as part of this source pass.
5. Write a receipt with source hashes, raw offsets/bytes, exact ids and text,
   then run the receipt and records checks. Keep site data unchanged until
   the operator approves implementation.

### Result

[L219](../../reference-data/provenance/frosty-2026-09-30-L219-gadget-ui-metadata-linkage.json)
independently checks all 78 records with 4,164 raw checks. There are 75 exact
candidate-table matches and three description encoding differences: Sniper
Decoy, TOW and Mortar. Seventy-five description ids resolve; three are missing.
Excluding 12 stated label/stub texts reproduces the supplied count of 63
descriptive texts. This text criterion does not classify gadgets.

The outward direct-import and selected local-owner route leaves all 78 records
unlinked to a blueprint/ability: 451 imports are images and seven are UI movie
or configuration assets. Other inbound identity routes remain open. The
[verified metadata table](../../reference-data/frosty/gadget-ui-metadata.json)
keeps every record and its text fields. The
[L220 preset/ability-description pass](../../reference-data/provenance/frosty-2026-09-30-L220-gadget-preset-coverage.json)
decodes 24 MP preset rows and 102 ability descriptions. Preset descriptions
name Defibrillator, Deployable Cover, C4 and Ladder. Their numeric identifiers
have no overlap with the gadget metadata arrays, and all 194 ability-description
imports are images. Under the accepted text-presence rule, coverage records
56 multiplayer gadget groups, six shared systems, one SP/mode item and
58 unresolved groups. Every group states its text evidence basis separately
from the unresolved exact blueprint link.

[L221](../../reference-data/provenance/frosty-2026-09-30-L221-gadget-ui-text-and-checks.json) adds
UI text records to all 121 coverage groups and a 39-row stat companion. Sixty
groups show exact UI-owner text under a disclosed supporting association. The
63 substantive descriptions have concrete check steps and predictions; 12
stubs and three missing descriptions remain explicit exclusions. No game
tests were performed. M26 Slug versus buckshot text is recorded as a source
contradiction, without repair.

### Gadget reverse identity search (L222)

[L222](../../reference-data/provenance/frosty-2026-09-30-L222-gadget-reverse-ui-identity.json)
checks the reverse route from named gameplay WB, Ability, CUST, U_ and loadout
roots to the exact file and exported-object GUIDs of all 78 UI records. The
known Supply Drop Ability → CUST → WB chain passes before the search, and the
independent import reader recovers its exact CUST-to-WB pair.

The inventory retains all 121 groups and 320 named routes. It inspects 274
captured revisions and 4,712 imports with no exact metadata GUID reference,
encoded GUID candidate or reader error. Of these, 146 revisions and 3,358
imports have directly verified 1.4.3.5 raw bytes; 128 revisions and 1,354
imports remain historical-only evidence. There are 46 missing routes. The
negative applies to these inspected bytes, not to all gameplay assets.
Historical captures retain their original Head; equal current hashes prove
carry-forward only for the explicitly verified revisions.

No UI-to-gameplay join method follows from this route. All 78 records remain
unlinked. The numeric preset route is a separate check.

[L223](../../reference-data/provenance/frosty-2026-09-30-L223-gadget-preset-numeric-identity.json)
tests all 24 MP preset identifier arrays against typed integer fields in
named gadget Ability, WB, CUST, U_ and loadout roots. The exact Supply Drop
chain, its typed identity field and one preset UINT32 pass the controls.
All 24 preset values are distinct. None equals an inspected gameplay field.
The current scope is 145 directly verified roots with 761 integer operands;
128 historical-only roots have 833 further operands. Forty-six named routes
remain uncaptured. This scan covers typed root integer fields, integer arrays
and value structs; it skips pointers and other array types. No equality,
exact join or native selection rule follows from this scope.

The two unsuccessful identity leads close this run under the operator's stop
rule. Coverage and the stat-list statuses remain unchanged. No reusable
UI-to-asset join method was established. Reopen only with a new authoritative
identity route or a specific essential capture that can settle a named join.

## Weapon descriptions and role tags

Each weapon record has a description pointer (`Field_490f0dd0`), a category pointer
(`Field_f8c63ce7`), three role tags (`Field_8c7f991f`) and a numerical stat block.

**Descriptions.** 61 of 63 resolve. Two ids are missing from the English table; the
game panels (13 September) show text that exists under other ids:

| Weapon | Record pointer | Text id | Text | Site sweet spot |
|---|---|---|---|---|
| M2010 ESR | `2DB86D4C` | `5E0EAEEC` | 75m-100m, "relatively low base magazine capacity" | 75-100 m |
| SV-98 | `E8EA1B59` | `97529B79` | 54m-75m, "legacy 7.62x54mmR" | 54-75 m |

No metadata record uses either text id; the match comes from the caliber, magazine note
and range. The other sniper descriptions agree with `deriveSweetSpot`: PSR 90m-120m
(`84FCD536`), L115 100m-133m (`7A9C24A9`), Interdictor 120m-150m (`A89AE617`).

All 63 records in `data/weapons.json` include `description`, shown in weapon button and
comparison heading tooltips. Keep the source distinction (61 Frosty, 2 screenshot
transcriptions) when refreshing.

**Role tags.** [data/weapon-role-tags.json](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/data/weapon-role-tags.json) keeps
style, range and firing tags; reference data only. A record with a package image is
primary. PW7A2's base record says Mid Range (the panel agrees); its SP Suppressed record
says Close Range. Mini Scout: `UIWeaponAbilityMetaData` says Mid Range and `S1B1` says
Long Range; the panel shows Long Range, so the file uses `5852C245` with
`panelEvidence`.

### Numerical stat block — do not use

`BFUINumericalWeaponStatManagerWeaponConfigAsset` lists Firepower, Accuracy, Range and
Handling. The values are archetype templates, not per-weapon data: every SMG has
24/38/38/66, KSG-12 has SMG values, M123K and M121 A2 have shotgun values with "Pump
Action" and magazine 8, and SV-98 shows fire rate 25. Nine records have no block.

## Attachment labels and descriptions

`AD_*` assets under `Common/UI/Static/Metadata/Attachments/` hold two pointers to
`Class_fbe1d3bc` objects: `Field_33a358a7` (label) and `Field_490f0dd0` (description).
[frosty-descriptions.py](../../scripts/frosty-descriptions.py) resolves both against
the strings table.

- 1,003 assets exported without error: 990 labels and 997 descriptions resolve (984
  both); 131 distinct labels, 211 distinct descriptions.
- 13 assets have a null label pointer. Six descriptions use five ids missing from the
  table: `1C029CC8`, `BC1F219E`, `A70D89F6`, `2897A9DF`, `FC443C65`.
- Two assets can share a label and differ in description. Keep the asset path and ids
  when matching one to a site attachment.
- These are UI texts, not proof of mechanics or availability.

Optic `AD_*` labels are generic ("Sight 1.25x"). The optic model name comes from the AAM
record (below).

To repeat after an update: refresh the manifest and strings, batch-export
`Common/UI/Static/Metadata/Attachments/**/AD_*`, run the resolver and inspect its error
count. In 1.4.3.0 Frosty could not read these assets; use `scripts/frosty-ebx-decode.py`
([Tools](TOOLS.md#sdk-and-decoding)).

## Attachment and optic names (AAM records)

Each weapon's `AAM_<weapon>` asset holds one `Class_ccf7da47` record per attachment:

- `Field_55aded8d`: internal label (`RPK74M - RMR`).
- `Field_fd698f51` → `Class_fbe1d3bc.Field_3d34898a`: in-game name id
  (`0xadd3ecaf` = "R-MR 1.00x").
- `Field_85b318a1`: the AD asset (label and description).

Optic names include the magnification. Frosty record name → in-game name:

| Frosty | In-game | Frosty | In-game |
|---|---|---|---|
| 1P86 | 1P86 LPVO | NF ATACR | R-VPS 10.00x |
| 1P885 | 1p88 Variable | NX8-1 | S-VPS 6.00x |
| ACRO P2 | A-P2 1.75x | NX8-4 | NFX 8.00x |
| ANPAS35 | PAS-35 3.00x | Offset Red Dot | Piggyback Reflex |
| Bravo3 | Baker 3.00x | OPK7 | Osa-7 1.00x |
| CantedReflex | Canted Reflex | PG350 | 1p87 1.50x |
| COD2M | BF-2M 2.50x | QMK171A | QMK 3.00x |
| CompM5b | CCO 2.00x | RMR (also "Deltapoint") | R-MR 1.00x |
| EFLX Mini | Mini Flex 1.00x | Romeo4T | R4T 2.00x |
| ELCAN DR | SU-230 LPVO | RomeoX | ROX 1.50x |
| ELCAN LDS | LDS 4.50x | SB PMII | SSDS 6.00x |
| HISSHD | TS-HD 6.00x | Shield CQS | CQ RDS 1.25x |
| Holosun DRS TH | TH-RDS 1.00x | Spitfire | SF-G2 5.00x |
| M145MGO | MGO 3.50x | Steiner T536 | ST Prism 5.00x |
| M157 | NGFC LPVO | Tango6T | DVO LPVO |
| M7Xi | SM Rifle Variable | Trijicon MRO | RO-M 1.75x |
| March FFP Shorty | Mars-F LPVO | Trijicon RCO | PVQ-31 4.00x |
| Mark4M5A2 / M2 | LERT 8.00x | Trijicon REAPIR | GRIM 1.50x |
| Mepro M22 | 2Pro 1.25x | Trijicon SDO | SDO 3.50x |
| VZOR3 | 3VZR 1.75x | Trijicon SCO / VCOG | MC-CO LPVO |
| XPS3 | SU-123 1.50x | Trijicon SRO | RO-S 1.25x |

The M27IAR "NX8-4" record resolves to "S-VPS 6.00x". Some AD assets also hold stat
labels ("Aiming Down Sight Speed", "Zoom Level") and ids missing from the table.

## Current site mapping

All 3,011 non-optic site choices have reviewed Frosty source identities. The runtime
tooltip file describes 2,966 of them: 2,948 with Frosty English text and 18 with
approved game-panel text. The other 45 are deferred and carry
`description-review-required` in the mapping report.

All 350 generic optic choices map to 1,927 Frosty sight records for the 63 weapons.
Fixed scopes are Standard Optic; Variable Low and Variable High group the 20- and
25-point variable optics (not a magnification threshold). Iron Sights has a tooltip on
all 63 weapons (3,030 tooltips in total). The site shows the iron-sight name as
"Iron Sights (1.50x)" ([Attachments](ATTACHMENTS.md#optic-render-fov-and-zoom)).

- **Iron-sight defaults.** M16A4 (Classic) and UMG-40 (basic aperture) are user-selected.
  L115 and Interdictor use their no-scope-glint description. In game, M2010 ESR,
  SV-98, PSR and Mini Scout show the same no-glint text (operator check, 25 September),
  but their source `AD_*` descriptors link `0BB6AC0B` (reduced sway); the site still
  shows the linked text pending approved panel captures. Four missing iron UI links
  use the weapon's `AD_<weapon>_Sight`. M121 A2 uses
  `Common/Hardware/Weapons/MG/MG5/AD_MG5_IronSights` (description `0BB6AC0B`).
- **Panel text.** 18 approved panels supply tooltips. 15 replace missing strings; three
  (AK4D 20 Rnd fast, SV-98 Lightened Suppressor, SCW-10 Extended) replace linked text
  that differs from the live panel (`status: linked-text-differs-from-panel`). Evidence:
  `panelLinkageInvestigation` in the identity follow-up report.

| Captured selection | Weapons receiving panel text |
|---|---|
| Taclight - Hipfire | M433, B36A4, M277, M417 A2 |
| Taclight - Aimed | VCR-2, GRT-BC, BROD 3, EF88, ES 5.7, M45A1 |
| 50 MW Violet | GRT-BC, L110, DRS-IAR, DB-12 |
| 30 Fast magazine | RPKM |
| 20 Fast magazine (linked text differs) | AK4D |
| Lightened Suppressor (linked text differs) | SV-98 |
| Extended barrel, 200MM Custom (linked text is `[REDACTED]`) | SCW-10 |

RPKM's AAM title resolves to "30rnd Fast Mag", matching its panel. DRS-IAR and DB-12
have TOP hardware and panels but RGT names in their ANPEQ16B AAM records; DB-12 also has
a separate RGT record, so the AAM name is not simply a typo.

### Files

- `data/attachment-tooltips.json`: runtime descriptions and per-weapon links.
- `reference-data/provenance/frosty-site-attachment-mapping-2026-09-13.json`: every site
  choice with hardware paths, progression and attachment GUIDs, ability branches,
  selectors, UI links, review flags and input hashes.
- `reference-data/provenance/frosty-optic-category-mapping-2026-09-15.json`: optic
  category members, labels, descriptions and hashes (the 2026-09-13 file is the 1.4.2.5
  baseline).
- `reference-data/provenance/frosty-attachment-identity-followup-2026-09-13.json`:
  further identities and screenshot reviews with image hashes.

### Resolution rules

- The mapper starts with the reviewed site-to-hardware identities and checks them against
  the source graph. Then it tries the full AAM name, the name without the slot code,
  rail-side variants and exact weapon descriptor names (case-insensitive). Scoped
  prefixes such as `MZL_FlashComp` can be removed while the exact hardware model stays.
- Shared UI records need the exact hardware model and the same English text across rail
  variants. A peer description needs the same model and the same bound selector set, so
  recoil and non-recoil subsonic variants stay separate.
- Screenshot reviews can resolve missing or conflicting links. Regeneration checks the
  screenshot hash, the original candidates and the expected text.
- The panel-text pass needs an unresolved (or `linked-text-differs-from-panel`)
  description, one matching hardware source, the unchanged UI link and the saved image
  hash. It writes `screenshot:<weapon>:<slot>:<attachment>` keys (not localization ids)
  and marks the choice `screenshot-verified`. Panel text is never copied to other
  weapons.

### Corrections from this audit

- `ImprvdSuppressor01` is CQB and `ImprvdSuppressor02` is Lightened (the old audit
  reversed them).
- P18, ES 5.7, M45A1, GGH-22 and vz. 61 show Single-Port Brake at 10 points; the source
  brake is `Brake2_W10`. The site uses 10 points and no generic sway penalty.
- QBZ-192 ergonomics are None, Match Trigger and Rail Cover; the unsupported Aftermarket
  Buffer was removed.
- GRT-BC shows Burst Mode with 3-round bursts; SL9 uses the 2-round description.
- SGX Classic Vertical uses "Greatly reduces recoil" (`AD_KABroomstick`).
- The M4A1 hipfire taclight uses `AD_SF300_LeftRail`.
- VSSM ASM text ("Alternate barrel") and M1014 compensator text differ from saved panels;
  the site uses the current Frosty text and the review keeps both.

### Regeneration and verification

Copy the newest dated mapping files to a new date first, because the generator writes
back into them ([Tools](TOOLS.md#safety-rules)).

```powershell
python scripts/frosty-attachment-tooltips.py outputs/frosty-description-probe/aam data/attachment-tooltips.json --frosty-root '<Frosty export root>' --mapping-json reference-data/provenance/frosty-site-attachment-mapping-<date>.json --optic-mapping-json reference-data/provenance/frosty-optic-category-mapping-<date>.json
python scripts/frosty-attachment-tooltips.test.py
node --test scripts/attachment-effects.test.mjs scripts/optic-costs.test.mjs
node scripts/validate-data.mjs
node scripts/validate-ship-surface.mjs
```

The coverage check compares the report with the menu availability functions, every
runtime description reference and deferred choice, current hashes and all optic
members. Totals: 2,967 described non-optic choices, 63 iron-sight tooltips, 45 deferred
choices, 350 optic categories.

## Weapon Attributes UI

The game names this system **Weapon Attributes**. The four bars are Hipfire,
Precision, Control and Mobility. Calculation assets use `WeaponAttributesConfig_*`;
UI assets include `WeaponAttributes`, `WeaponAttributesCell` and
`WeaponAttributeProgressBar`. The current [model guide](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/WEAPON_ATTRIBUTES_MODEL.md)
separates source facts from inferred rules. Historical research is covered in
[composite stats findings](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/archive/COMPOSITE_STATS_FINDINGS.md). The UI side:

| Asset | Content |
|---|---|
| `NumericalStatsDBD` | `Name`, `Value`, `Delta` |
| `IconizedAttributesDBD` | `Label`, `Value`, `Delta`, localized value/delta/suffix, `Icon`, `IsDeltaPositve`, visibility flags |
| `AttachmentAttributeDBD` | `Text` |
| `WeaponAttributeProgressBar`, `CL_StatsBar_WeaponStats` | Bar layout and colors |
| `WeaponAttributesDelta`, `WeaponAttributesDeltaValue` | Delta layout, fonts, `{0:s}` format |
| `WeaponAttributesIconizedCell`, `WeaponAttributesIconizedValue`, `WeaponExtendedAttributesCell` | Cell layout; `IconizedAttributesColorLogic` |
| `MetaCustomization_AbilityStatsDBD`, `MetaCustomization_AbilityStatsView` | Visibility flags |
| `PlayerAbilityStateDBD`, `MP_QuickCustomization_ViewStateGraph` | Ability state; no stat fields |

The bindings receive a finished name, value and delta, with no weights or inputs. The
labels `PRECISION` (`2581C0EB`), `HIPFIRE` (`4B1DA1C6`), `MOBILITY` (`F9880148`) and
`CONTROL` (`D81D0800`) are not referenced in the XML export. The values probably come
from native code.

### Setting labels

[frosty-weapon-setting-labels-2026-09-13.json](../../reference-data/provenance/frosty-weapon-setting-labels-2026-09-13.json)
lists 104 English labels for weapon, aim, recoil, spread and handling settings (names
only). No label, in PascalCase, lowercase or camelCase, matches a `GRX_Weapons` hash or a
cited `Field_` hash. Three labels match delegate argument names as text:
`RECOIL AMOUNT` → `RecoilAmount` (`030aea17`), `RECOIL VARIATION` → `RecoilVariation`
(`890dbeaa`), `DEPLOY TIME` → `WeaponDeployTimeIndex` (`f407a9c7`).

### String usage scan

`scan-string-usage` searched `Game/GlacierPortal`, `Common/UI`, `Common/GameSetup`,
`Game/GlacierMP/GameSetup` and `Game/GlacierGranite` for 107 ids (the 104 labels,
`5E0EAEEC`, `2DB86D4C`, `E8EA1B59`): 161 hits for 35 ids. EBX values only, not native
code.

- `HIPFIRE`, `MOBILITY`, `CONTROL`, `RECOIL SMOOTHNESS`, `SWAY FREQUENCY` and the other
  Portal tuning labels have no hit.
- `PRECISION` has one hit, a gadget label in `UIGadgetAbilityMetadata`.
- `ACCURACY`, `FIREPOWER` and `HANDLING` hit only their `NumericalStatKey` assets.
- `2DB86D4C` and `E8EA1B59` hit only the M2010 ESR and SV-98 records. `5E0EAEEC` has no
  hit; `97529B79` was not in the scan.

### Companion Battlefield composite models

Third-party evidence, read 13 September 2026 from the `statModels` bundle in
`companionbattlefield.com/assets/app-DZxSgVe7.js`. Their site had data errors before;
use it only as a research lead.

- **Labels.** Panel labels (`ADS Time In`, `Sprint Recovery`, `Recoil Amount`,
  `2D Spot-On-Fire Range`) are the game's English UI labels. Modifier names
  (`recoilAmountTier`, `hipDispersionTier`, `adsZoomTier`, `precisionMinAngleMult`) and
  raw fields (`HIPRecoilAmount`, `ADSStandBaseMin`) are their own. No Frosty hash or
  delegate argument name appears.
- **Base panels** (`panelBases`) store the four stats per weapon; attachments carry
  `ratings` deltas.
- **Hipfire:** one 18-value table by hip dispersion row, capped at 100, with a per-weapon
  base index. Rows 1-15 equal the site candidate
  `10*sqrt(0.425/tan(1.25*H)*83.333/40.924)` on `HIP_SPREAD_TABLE.hipStand`; row 0
  differs (22.109 against 23.052). The light gate multiplies by 1.0954 (sqrt 1.2).
- **Control:** 2,276 cells by recoil amount and variation tier sums; all agree with the
  site formula within 0.0001.
- **Precision:** 4,833 rows for 41 automatic weapons, keyed by amount sum, variation sum,
  duration, decrease factor, ADS `minAngle` and RPM (G36: `minAngle` 0.36 → 0.24 raises
  26.951 to 31.025). The 22 weapons with `minAngle` 0 or 0.001 have no rows (snipers 100
  except Interdictor 1, DMRs 55-80, sidearms 24-57, shotguns 6-14).
- **ADS:** per-weapon milliseconds by tier sum. ADS move speed ladder: 0.325, 0.325, 0.37,
  0.42, 0.475, 0.535, 0.6, 0.67, 0.745, 0.825, 0.91, 1.

## Limits

- English only.
- The string scan skipped 536 unreadable assets; none of the missing links needed them.
- Name and description links establish UI text and source identity. They do not prove
  live availability or engine behavior.
- Open questions are in [Open questions](OPEN_QUESTIONS.md).

## Vehicle archetype, loadout and customization text (L3023)

[L3023](../../reference-data/provenance/frosty-2026-09-30-L3023-vehicle-ui-metadata.json) uses the operator capture at Head 4892087 (1.4.3.1), without Frosty. Four raw hashes, the descriptor and the localization TSV are pinned. Nine archetype cards and fifteen presets are retained.

Archetype Class_02be5e85 has actual key `9b9c42a5efc21f07060d23aa9918083c`. Field_8a9d7d7b selects role name, Field_f9aca425 short name, Field_490f0dd0 description and Field_ccfb8048 text tags. These semantic labels are inferred from the resolved text. Selected Class_fbe1d3bc targets contain ids in Field_3d34898a. Keep exact ids, TSV lines and escaped text. Field_1636b8bd is UINT32[] lookup keys. Hash-name layout ambiguity is retained; actual local keys and raw offsets control these reads. The independent parent control resolves ECD2AB78 to MAIN BATTLE TANK.

| Card / role name | Description | Seat text | Tags | Exact family/root link |
|---|---|---|---|---|
| MAIN BATTLE TANK (MBT) | Built for engaging enemy land vehicles but can also effectively combat enemy infantry. | 2 Seats | 2 Seats, Anti-Vehicle, Hard Target | Unlinked |
| INFANTRY FIGHTING VEHICLE (IFV) | Effectively counters hostile infantry but has limited capability against heavy enemy armor. | 6 Seats | 6 Seats, Anti-Soldier | Unlinked |
| LIGHT GROUND TRANSPORT (LIGHT TRANSPORT) | Designed for rapid battlefield traversal. Equipped with firepower to combat hostiles.  | 5 Seats | 5 Seats, Open Seats, Transport | Unlinked |
| ARMORED TRANSPORT (ATP) | Primarily for use in urban areas. Mine blast protection ensures optimal navigation through hostile territory. | 4 Seats | 4 Seats, Shielded Seats | Unlinked |
| MOBILE ANTI-AIR (ANTI-AIR) | Capable of using dual autocannons and homing missiles to combat enemy aircraft. | 1 Seat | 1 Seat, Shielded Seats | Unlinked |
| Attack Helicopter (ATTACK HELI) | Highly effective at engaging all ground targets, especially when both crew positions are manned. | 2 Seats | 2 Seats, Anti-Vehicle, Anti-Soldier | Unlinked |
| TRANSPORT HELICOPTER (TRANSPORT HELI) | This transport helicopter serves as a vital component in air assaults. Two side-mounted miniguns aid in self-defense. | 5 Seats | 5 Seats, Transport | Unlinked |
| ATTACK JET (ATTACK JET) | A fast multirole attack aircraft specialized in engaging all ground targets, including vehicles and infantry. | 1 Seat | 1 Seat, Anti-Vehicle, Anti-Soldier, Soft Target | Unlinked |
| FIGHTER JET (FIGHTER JET) | A stealth fighter that specializes in combating other air vehicles, with limited air-to-ground combat capabilities. | 1 Seat | 1 Seat, Anti-Vehicle, Soft Target | Unlinked |

Each stated numeric seat count is sourced as an in-game statement for usable seats. Validation: after establishing the exact vehicle/card join, count every enterable seat through spawn, enter and switch. Prediction: the count equals the card number. No test was run. Open Seats and Shielded Seats are descriptive tags, not extra seats. All nine cards remain explicitly unlinked after one saved-root selector pass; family seat values remain unset.

UIVehicleArchetypeMetadata selects nine local records and nine unresolved icon imports. UIVehicleLoadoutPresetMetadata selects fifteen local records: AA, AH, APC, IFV and MBT each have three numbered loadouts. Field_fd698f51 resolves LOADOUT 1/2/3; Field_490f0dd0 resolves descriptions, retained separately per preset in the receipt. Preset internal-name bytes are decoder/hash-pinned without separate string-byte checks.

UIVehicleMetadata links 25 external vehicle UI metadata GUID pairs; the registry routes are retained, but exact same-Head target objects are not captured in the bounded check. BFUIVehicleCustomizationsViewManagerConfig retains 21 local and 35 external pointer records: 18 have exact saved target GUID matches and 17 remain unresolved. The receipt pins every source field/index, offset and target GUID pair in links.json. These are customization and metadata selections, not default or active loadouts.

Worker review passed 292 unique raw checks. Parent rereads confirm one text id and one customization import pair. No family join was invented from a route label.

## Class, training-path and perk metadata

Client **1.4.3.1, Head 4892087**, descriptor `99b49cfd8bdb5bb6f0181df8ac0d93a0396c1b7f07a1ba3ce8ca1cea45969640`.
The retained `builds/1.4.3.0` folder name does not identify the client version.
[Table and source links (L400)](../../reference-data/provenance/frosty-2026-09-30-L400-class-trait-ui.json)
contain 17 class records, 12 training paths, 102 perk records and 24 presets.
The receipt keeps explicit columns for class, description, signature trait,
proficiency, path, perk, text numbers and exact record references. Missing fields
and all unverified activation links remain explicit.

Text resolves through local pointers to `Field_3d34898a`, then the captured English
TSV. The exact Support LMG control passes. There are 832 raw pointer/string reads.
Support and Recon signature string IDs are absent from this TSV; no substitute
names or descriptions are supplied. Decoder layout ambiguity markers remain in
the table. `Field_890a772b` path imports resolve to ClassSpecs **images**, which do
not establish class or perk selection. Duplicate internal names also need the
record GUID: `Ability_ActiveFlak` includes both RALLY SQUAD and HEAVY FLAK.

| Class | Captured proficiency text | Cross-check with existing release evidence |
|---|---|---|
| Assault | Faster draw times and fire sooner when exiting a sprint with Assault Rifles. | Agrees with draw/sprint-recovery +1 steps. |
| Engineer | Improved hip-fire control when using SMGs. | Agrees with hip minimum row +1. |
| Support | Faster transition to aim down sights (ADS) and no sprint speed penalty when carrying LMGs. | ADS agrees; sprint exemption has no sourced operand in L100-L104. |
| Recon | Reduced weapon sway, faster rechambering, and improved breath control with Sniper Rifles. | Sway agrees; rechambering remains conditional and breath control lacks an operand. |

The comparison uses L100-L104 and the existing timing receipt; it does not retrace
those release operands or establish their behavior on a new client build.
Eight captured multiplayer source paths have 32 raw-checked ordered
`Field_ba52a009` Ability imports. Their `U_FieldUpgradePath` wrapper tokens do not
establish a match to the UI table. Source paths and array positions are serialized
facts; UI display-name associations, unlock levels and class selection remain
unresolved. The readable table and run handoff are retained in
`BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T0112-0400-class-traits/`.

See [class/perk stat findings](WEAPONS.md#class-path-and-perk-source-cross-check).

<!-- L900-weapon-ui:start -->
## Weapon UI census (L900, corrected by L905)

[L900 receipt](../../reference-data/provenance/frosty-2026-10-01-L900-weapon-ui-census.json) uses current 1.4.3.5 bytes, Head 4909002 and the current English table. Nine weapon metadata containers plus the description container contain 1,183 localized text objects, 70 weapon UI records and 1,607 exact pointer/import edges. The M433 pointer and string-ID control passes after correcting signed string-ID lookup. Mixed ability/perk/gadget text stays separate from the weapon scope.

All 63 site names match available UI names. [L905](../../reference-data/provenance/frosty-2026-10-01-L905-weapon-ui-statements.json) corrects L900's description comparison to 61 of 63. M4A1 and KTS100 match; L900 read the UTF-8 site file through the default Windows encoding and produced two false apostrophe differences. The census's localized text objects were correct. M2010 ESR and SV-98 still have missing localization IDs and archived screenshot wording. The old receipt is retained as evidence of the original comparison.

Every selected UI source-owner link remains explicitly unresolved; image names and equal strings do not supply identity. The census retains raw text IDs, offsets, bytes and hashes, non-site variants and empty containers. L905's exact reused gameplay source associations support separate curve/capacity comparisons, with original Heads and current raw-hash equality retained. The atlas is not rebuilt.
<!-- L900-weapon-ui:end -->

<!-- L901-attachment-ui:start -->
## Attachment, ammo and optic metadata census (L901)

[L901](../../reference-data/provenance/frosty-2026-10-01-L901-attachment-ui-census.json) decodes all 1,003 AD owners under the requested UI metadata roots on 1.4.3.5 / Head 4909002. The current iron-sight description control passes. The result retains 2,317 text pointer occurrences, 57 missing string IDs, 233 nonempty metadata arrays and 2,195 import edges. The full census and raw-check lists stay in the run folder and are cited by hash.

Every asset retains the decoder's layout ambiguity. Raw pointer, GUID and string-ID reads support the exact text edges; they do not assign effect-chip or pros/cons roles to unnamed fields. Stated numbers are retained with text and units, while gameplay ownership and native effects remain unresolved. Image imports remain presentation edges. Underbarrel meaning is excluded. Exact selection joins and the stat-screen receiver determine which text can support a source comparison.
<!-- L901-attachment-ui:end -->

<!-- L903-selection-edges:start -->
## Exact selection and metadata boundary (L903)

[L903](../../reference-data/provenance/frosty-2026-10-01-L903-ui-selection-edges.json) independently verifies the M433 AAM-to-AD pointer/import and description-ID control. Its 63 source entries cover 189 current GS/WB/Ability roots, 64 AAM candidates (including extra KSG) and six metadata containers. The ledger retains 5,303 exact AAM-to-AD edges. Path correspondence selects AAM candidates; it does not establish gameplay ownership. The bounded direct-root check has no source-to-UI selection join and makes no transitive absence claim.

The numeric key/property receiver that connects a selected attachment to an AAM record remains unresolved. Current source roots, metadata arrays and AAM lookup keys retain raw identities. Name-based historical UI matching cannot replace that receiver. The run-folder dead-end batch states the precise route, attempted fields and reopen condition. New player-facing quantities use exact localization-ID references and independently confirmed source meanings; they retain this activation boundary.
<!-- L903-selection-edges:end -->

<!-- L906-statement-comparisons:start -->
## Numeric statement coverage (L906)

[L906](../../reference-data/provenance/frosty-2026-10-01-L906-attachment-ui-statements.json) retains every one of the 2,317 AD text occurrences. The 415 numerical tokens have explicit classifications: 13 match exact site tooltip text and 402 are unmapped. Labels state nominal capacity, zoom, angle, burst count or length, or contain model/shot-size identifiers. No percentage or timing effect quantity is present in this bounded string corpus. Text-reference equality is not a source-selection or native-effect join. The qualitative statement and reviewed-bug indexes retain those separate evidence levels.
<!-- L906-statement-comparisons:end -->

<!-- L905-weapon-statements:start -->
## Weapon description quantities and current text corrections (L905)

[L905](../../reference-data/provenance/frosty-2026-10-01-L905-weapon-ui-statements.json) classifies all 41 numeric token occurrences in the 63 weapon descriptions. Eleven are sourced effect/count values: ten endpoints of five peak-damage intervals and the eight-shot M357 cylinder. Thirty are cartridge/shell designations, model identifiers or historical ordinals, retained as unmapped context rather than gameplay modifiers. All 528 independent metadata, curve and capacity raw reads pass.

The current TSV entry `A89AE617`, selected by the raw Interdictor metadata pointer, states 120 m to 160 m. It is in the pinned current table with SHA-256 `1ec449fa2a12bc3d307bfa5878ee7d8c56af14fae65ea1f6c6286e85d98e7392`. L740's assertion that the current localization still ended at 150 m was stale; its receipt supplied no exact localization-ID/raw-text proof for that assertion. L905 retains the older receipt and the historical 150 m description separately. The implemented site wording and selected curve already use 160 m, so no new site edit is proposed.
<!-- L905-weapon-statements:end -->

<!-- L904-metadata-closure:start -->
## UI root coverage, stat descriptions and scope (L904)

[L904](../../reference-data/provenance/frosty-2026-10-01-L904-ui-metadata-closure.json) gives one scope disposition for all 1,319 catalog entries under the two requested metadata roots. All 39 fixed metadata containers and three exact extensions are examined; no fixed container or extra AD target is missing. The extensions are `Stats/UIStatDescriptionMetadata`, the mode-specific Granite shared-ammo metadata and the exact AAM import to `Common/Hardware/Weapons/MG/MG5/AD_MG5_IronSights`.

The 1,260 raw-checked text pointers comprise 827 package cosmetic texts, 20 slot labels, 370 mixed stat labels, 41 mode-specific ammo labels and two extra iron-sight strings. Cosmetic, soldier/perk, gadget, vehicle and unrelated UI contexts have explicit scope dispositions and remain separate from 63-weapon claims. Mixed stat descriptions and Granite ammo text are context until an exact selected weapon/stat receiver establishes their use. Twelve package owners retain layout ambiguity. All 663 inspected metadata objects have raw local class/key/current-descriptor qualifications. The independent Carrion pointer/string control and parent reread pass. No text or container membership supplies native stat normalization.
<!-- L904-metadata-closure:end -->

<!-- L902-weapon-attributes:start -->
## Current Weapon Attributes source and UI normalization (L902)

[L902](../../reference-data/provenance/frosty-2026-10-01-L902-weapon-attributes-ui.json) verifies the Control same-owner constant/input control on 1.4.3.5 / Head 4909002. All seven current compiled delegate bodies equal the reviewed bytes. The exact Precision settings raw hash also carries forward 63 tables and 4,946 rows; representative typed reads pass, including Boolean flags.

| Bar | Current source-supported site method | Remaining interpretation |
|---|---|---|
| Hipfire | Nonlinear delegate-specific 18-row dispersion lookup and separate angle input | Fraction branch and native operator meanings retain reviewed inference |
| Precision | Exact per-weapon source lookup tables | Active native table provider/selection unresolved |
| Control | `96 / (1.1 * R * sin(v) / v + 0.75)^2.25 + 4`, with `v = V * pi / 180` | Sine/native operator meaning and execution retain reviewed inference |
| Mobility | Reviewed weighted source indices | Native input/provider selection unresolved |

All four classify as matches site for the retained source-supported model candidates. This is not a claim that every game panel or native loadout uses that candidate. Extended RateOfFire, HeadshotMultiplier and CollateralMultiplier delegates have exact current input/resource identities but retain unresolved numeric operator/provider interpretation in this pass.

The current wrapper passes connected values 100 and 1 through `CL_StatsBar_WeaponStats` into local nodes 28/29 of `CL_StatsBar`. Exact value, label and delta property edges are retained. Anonymous type/operator/property semantics do not prove division, final bounds or a universal 0-100 clamp. No unvisited exact arithmetic source import remains; the remaining nested prefab is rendering context.

Exact atlas qualification checks 25 candidate families and 41 contexts. Their owners differ from the current bar delegates. Newly meaningful known-limit families: 0; contexts: 0. Matching class/field hashes or parameter names cannot transfer bar meaning to those owners. The atlas is reused without a rebuild or classification edits.
<!-- L902-weapon-attributes:end -->

<!-- L907-census-summary:start -->
## Integrated weapons UI census (L907)

[L907](../../reference-data/provenance/frosty-2026-10-01-L907-weapons-ui-frontier-census.json) retains the integrated `ui-census.json`, comparison ledger, scope audit and excluded-context ledger in the run folder, each with a SHA-256 citation. All 1,319 metadata catalog paths have scope dispositions. The census has 3,557 text/interface rows: 775 weapon-local text items, 2,317 AD occurrences, 433 slot/extra-AD/mixed-stat/mode-context occurrences and 32 stat-interface rows. The count includes available/contextual text, not a claim that every row is displayed for a selected multiplayer weapon. Another 1,235 mixed ability and package cosmetic rows remain separate.

Every one of the 627 lexical numeric occurrences has a four-way disposition: 25 matches site and 602 unmapped; no new source-only or conflict quantity is qualified. The 11 unique weapon-description effect/count tokens and 13 AD text-reference matches have separate source and text scopes; the integrated count retains a repeated UI occurrence. Identifier, historical, mixed career/stat and mode-specific numbers do not become physical gameplay quantities. The 233 nonempty AD arrays remain indexed with unresolved effect-chip/pro-con roles.

All four reviewed bar candidates retain current source support. Exact native provider selection, final renderer arithmetic and the selected attachment-to-metadata scalar receiver remain unresolved. Zero known-limit atlas families or contexts receive new meaning. The compact dead-end ledger uses route, fields, tried method, stop reason and reopen condition, with one receipt per batch. No currently available exact metadata or arithmetic import target remains unvisited.

The final L904 revision is also checked here: 1,260 text pointers agree with the shared helper, zero mismatches; 16 Granite array text indices and 663 metadata objects have current raw type/index qualifications. Fourteen examined owners retain layout ambiguity, including 12 package owners. Mixed mode/stat roles remain context. This final verification supplements L904's earlier committed census receipt without modifying it.
<!-- L907-census-summary:end -->

## Vehicle preset UI census for seat defaults (L3150)

[L3150](../../reference-data/provenance/frosty-2026-10-01-L3150-vehicle-default-ui-census.json) starts the default-loadout pass from four saved current UI roots at build 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. The MAIN BATTLE TANK text control passes its exact local owner, pointer, string id and raw read. The parent independently re-read ECD2AB78 at offset 2608.

The four roots contain 619 objects, 126 text rows and 115 import pairs. UIVehicleLoadoutPresetMetadata has 15 preset text records and no imports. Its MBT and IFV LOADOUT 1 descriptions state vehicle roles; they do not name selected equipment. No resolved text row contains "default" or "unlock". Literal array order is retained, with no default meaning assigned to the first entry or to LOADOUT 1. UIVehicleMetadata retains 25 exact selected UI target pairs for the equipment census.

The UI text control validates this census. It does not validate seat defaults. UH60 minigun, RHIB OpenGunner HMG and MBT seat 0 main gun controls still need an exact UI slot-to-gameplay owner chain plus default selection evidence. Previous card/icon/category/lookup-id routes are not repeated.

Full fields, text ids, slot/flag candidates, GUID pairs, local keys and raw checks stay in `2026-10-01T163631-0400-vehicle-seat-defaults/L3150/ui-census.json`, pinned by the receipt. Unknown hashed field roles remain unresolved. This is UI/source evidence, with no site change.

## Vehicle seat default UI census (L3150)

Build 1.4.3.5, Head 4909002, descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L3150-vehicle-ui-preset-census.json).

Four current raw UI roots contain 619 objects, 126 text-bearing records and 115 import pairs. The exact MAIN BATTLE TANK pointer/string control passes. UIVehicleLoadoutPresetMetadata contains 15 LOADOUT 1/2/3 records and no imports. The census retains every decoded field, literal array order, text pointer and import pair. Slot, seat, unlock and default semantics remain unresolved. This text control does not establish a seat default.

The census and full raw checks stay in `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T163631-0400-vehicle-seat-defaults\L3150`; their paths and SHA-256 are in the receipt. The selected equipment targets and UI definition assets are checked separately. No gameplay identity is assigned from a name, image or lookup integer.

## Selected vehicle equipment UI and default controls (L3151)

Build 1.4.3.5, Head 4909002, descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L3151-vehicle-ui-equipment-default-controls.json).

25 selected UI targets retain 1111 objects, 170 resolved text rows and 456 import pairs. The UH60 minigun text control passes. The direct import route fails all three functional default controls; no seat default finding follows.

The census retains literal array order, localized names/descriptions, pointer operands, exported identities and hash-only Boolean candidates. These candidates are not assigned unlock/default meanings. Exact registry-to-MBT-UI and UH60 minigun text controls pass. Imports resolve to images/icon atlases and numerical-stat configuration context, not the retained selected gameplay owners. Names and repeated integers are not used as joins.

The failed functional controls remain explicit for both UH60 door-gunner entries, RHIB OpenGunner and both MBT seat 0 main guns. A matching displayed label cannot repair the missing owner identity. This failed route produces no default or negative seat findings. All full census/raw-check files stay in the run folder; the receipt pins path and SHA-256.

## Vehicle seat and equipment UI definitions (L3152)

Build 1.4.3.5, Head 4909002, descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L3152-vehicle-ui-seat-equipment-definitions.json).

Six UI definition/customization siblings decode to 74 objects, 39 import pairs and 11 text rows. Exact schema/import reader control passes. Named seat, slot and selection properties are definitions, with no controlled per-seat default assignment.

VehicleLoadoutDBD declares CurrentItem and ItemCollection. VehicleLoadoutItemDBD declares AbilityId, AbilityCategory, IsWeapon, IsAvailable and IsSelected. VehicleLoadoutSeatDBD declares VehicleSeat, VehicleSeatName and VehicleEquipmentList. VehicleLoadoutEquipmentsDBD declares SlotId, LoadoutPositionOffset, UIAbilityCategory, EquipmentName and EquipmentDescription. The raw property-name bytes and exact DBD import control are retained.

These are property declarations. Their live values and producer are not in these definitions. IsSelected does not state the factory default, and no stored slot value is joined to seat-map.json. Shared UIWeaponCustomizationSlotMetaData resolves infantry customization labels. The saved BFUIVehicleCustomizationsViewManagerConfig is retained as UI configuration context; prior card/category/image routes are not repeated. Functional default controls remain failed, so no default or negative seat finding is made.

All six selected raws, declared properties, pointer operands and hash-only Boolean candidates are retained in the run census. The two captures passed guard and reported 5/5 routes with Head 4909002. Full output paths and SHA-256 are in the receipt.

## Supplemental vehicle UI metadata census (L3153)

Build 1.4.3.5, Head 4909002, descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L3153-additional-vehicle-ui-metadata.json).

All six remaining current vehicle UI metadata assets are decoded: 288 objects, 41 text rows and 65 exact import pairs. CB90 mortar text reader control passes. No complete default chain passes the required functional controls.

The six exact catalog assets are DirtBike, MissileBattery, Automatic AA, NavalFighterPlane, MultirolePlane and CB90 UI metadata. They complete 28/28 Common/Hardware/Vehicles UI metadata assets in the current catalog. The six captures passed guard and reported zero failures. Names, descriptions, literal array order, pointer operands and hash-only Boolean candidates are retained. The CB90 IR Smoke Shell pointer/string ID was read again from raw bytes.

Imports remain UI image/icon context. The required gameplay seat/default identity is not supplied by this direct route, which was already rejected by the default controls. No numeric, image, name or category join is substituted. UI equipment wording remains UI-stated and unassigned to exact gameplay seats. Full outputs stay in the run folder with receipt path/SHA-256 pins.

## Vehicle seat default receipt reconciliation (L3155)

Build 1.4.3.5, Head 4909002, descriptor SHA-256 `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. [Decision receipt](../../reference-data/provenance/frosty-2026-10-01-L3155-vehicle-seat-default-receipt-reconciliation.json).

Two parallel closeouts used L3151 and L3152 during this run. Their receipts remain committed. The final L3151 `vehicle-ui-equipment-default-controls` receipt retains the same 25 exact asset/hash identities as the parallel closeout. The final L3152 `vehicle-ui-seat-equipment-definitions` receipt extends the parallel four-definition scope to six UI definition/customization siblings. The decision explicitly supersedes the two parallel `vehicle-default-ui-controls` receipts and identifies the final evidence for each lead.

The exact source/UI reader controls pass. All three functional default controls remain unpassed. No gameplay/default claim changes and no existing commit or receipt is rewritten or removed.
