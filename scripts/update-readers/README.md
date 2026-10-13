# Update readers

Scripts that read a build's raw EBX captures directly and derive site-shaped data for new
weapons. Written for the 2.1.1.0 (Season 5) update; the build and working folder are settings.

## Settings

`settings.json` holds the build label and the working folder; `BF6_BUILD` and
`BF6_READER_WORK` override them for one run. Every raw capture of the build is read:
`capture\collection\raw` first, then each `reports\*\raw` folder in date order, so a later
capture overrides an earlier one. Each part keeps its files in `<work>\A`, `\B` or `\C`.

For a new build:

1. Set `build` and a new `work` folder in `settings.json`.
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
- The lists of new weapons inside the scripts (for example the four Season 5 internal names)
  and some report wording still name 2.1.1.0 content; change them for the next update.
- The remaining files are one-off looks kept for reference. Some read earlier trace outputs
  from the 2.1.1.0 run folder (`uncaptured\attgraph.json`, `raw-index-old.tsv`).
- `regnames.py` reads registries under `Tweakables` only; that covers the weapon names.

The generator scripts in `scripts/` (`frosty-*.py`, raw mode) are the maintained route for
regenerating site data.