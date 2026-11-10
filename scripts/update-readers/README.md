# Update readers

Scripts that read a build's raw EBX captures directly and derive site-shaped data for new
weapons. Written for the 2.1.1.0 (Season 5) update; the build and working folder are settings.

## Settings

`settings.json` holds the build label, the working folder and the update's new weapons
(`newWeapons`); `BF6_BUILD` and `BF6_READER_WORK` override the first two for one run. Every raw
capture of the build is read: `capture\collection\raw` first, then
`capture\collection-fresh-cache\raw`, then each `reports\*\raw` folder in date order, so a later
capture overrides an earlier one. Each part keeps its files in `<work>\A`, `\B` or `\C`.

To run the same readers on the pre-update baseline as a control (a sealed build, or a
`pre-update-*` capture), set `BF6_RAWINDEX` to a run raw index for that capture, and
`BF6_DESCRIPTORS`, `BF6_CATALOG` and `BF6_STRINGS` to its files (see `settings.py`).

For a new build:

1. Set `build`, a new `work` folder and `newWeapons` in `settings.json`.
2. Run `python regnames.py` (field names from the build's tweakable registries, needed by part A).
3. Run the parts' main scripts from their own folder, in the order below.

Do not point `work` at an old run's folder: the scripts overwrite their outputs, and site data
cites the 2.1.1.0 outputs under `2026-10-13-update-2110-post\stage9\`.

## Parts

| Part | Loader | Main scripts, in order |
|---|---|---|
| A, base weapon records | `lib.py` | `extract.py` (per-weapon fields, registry override), `uimeta.py` (names, descriptions, role tags), `precision.py` (Precision tables), `reloadscan.py`, `build.py` (assembles the proposal) |
| B, projectiles and ammunition | `common.py` | `derive.py` (projectile and ammo side), `compare.py` (validates against the weapons already on the site, then proposes the new ones) |
| C, attachments | `rawlib.py` | `graph.py` (attachment graph for one weapon), `ui.py` (AD descriptors and AAM maps), `identity.py`, `derive.py`, `structure.py`, `validate.py` (regenerates existing weapons and diffs against the site), `propose.py`, `report.py` |

A weapon that is already on the site is validated, not proposed.

## Limits

- Checked on 2.1.1.0 only: parts A and B were re-run through `settings.py` and gave the same
  values as the original run, apart from counts that follow the site now holding 67 weapons.
  Part C's main scripts were not re-run after the change.
- The main scripts take the new weapons from `settings.json`. Still season-specific: the
  `UIWeaponAbilityMetaData_S5B1` route in `A/build.py`, some report wording, and the one-off
  look scripts.
- 2.1.2.0 moved the `Equipment_*` preset id list (`Field_6bf3cb97` to
  `Field_3538f6ad[].Field_5bed6412`); `B/derive.py` reads both. Without it, "default ammo"
  matched 0 of 67 weapons.
- The remaining files are one-off looks kept for reference. Some read earlier trace outputs
  from the 2.1.1.0 run folder (`uncaptured\attgraph.json`, `raw-index-old.tsv`).
- `regnames.py` reads registries under `Tweakables` only; that covers the weapon names.
- Part C's identity truth is the reviewed mapping `frosty-site-attachment-mapping-2026-10-24.json`
  (67 weapons, the site after 2.1.1.0; switched from the 2026-09-15 file on 10 Nov 2026). On
  2.1.2.0 against the updated site that cut the validation rows from 479 to 397. **Open:** the
  mapping has no rows for attachments added at the 2.1.2.0 integration (the Rubberized
  Vertical, `BTM_DDVertical`, on 52 weapons, rail covers, Synthetic Tip, new magazines) or for
  the NSW4, so those show as "record not on site" (116 rows) and "site only" availability
  (73 rows), and the NSW4's attachments are not validated. Closing it takes a 2.1.2.0 mapping:
  `scripts/frosty-attachment-tooltips.py` reads the XML export, so it needs a raw mode (or
  the integration's reviewed identity decisions written out as mapping rows), then a re-run of
  part C to show the remaining rows are the known stale ones.
- Part C identifies a record by its selector set when the stem is new to the mapping. Where a
  record now selects another attachment's package, it resolves to that attachment's id: in
  2.1.2.0 the SV-98 Flash Compensator and Suppressor (checklist T6 and T7) resolve to
  `flash_hider` and `std_supp`, while the site rightly keeps the in-game names. These were
  the two "cause not found" rows of the post-integration run.

The generator scripts in `scripts/` (`frosty-*.py`, raw mode) are the maintained route for
regenerating site data.