# Game update: Haiku worker briefs

Ready briefs for the worker plan in the
[game update guide](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/GAME_UPDATE_GUIDE.md#haiku-workers).
First used on 12 October 2026 for the 2.1.1.0 patch-note pre-trace
(`BF6 Datamining/reports/weapon-analyzer-research/2026-10-12-update-2110-pretrace/`).

## How to launch

- Agent type `haiku-worker` (shell and scripts) or `haiku-reader` (reading and searching only),
  `model: haiku`, `effort: medium`. Never an all-tools agent type.
- One run folder per update under `BF6 Datamining/reports/weapon-analyzer-research/`, one
  subfolder per worker. Workers write nowhere else.
- Save the common brief below as `brief-common.txt` in the run folder and start every task
  prompt with "First read `<run>/brief-common.txt` in full and follow it. Your output folder is
  `<run>/<worker>`." This keeps each prompt short.
- Build the two shared inputs once, in the main session, before launching:
  - `raw-index.tsv`: asset route, tab, absolute path of every raw `.ebx` held for the build.
  - `roster-flat.tsv`: `reference-data/frosty/roster-values.json` flattened to
    source, stat id, owner asset, value name, value.
- Launch independent workers in one message so they run in parallel. Workers never run Frosty;
  only one Frosty process may run at a time and captures stay in the main session.
- Check every result against the files before recording it. In the 7 October tests about one
  run in four had a disclosed rule slip, and Medium effort never volunteered a control the brief
  did not ask for: name every required output.
- Workers do not edit either repo, `BUILD.json`, or anything under `builds\`. The hotfix or
  new-build decision, sealing, decoder changes and site changes stay in the main session.

## Common brief

Replace `<RUN>`, `<BUILD>` and the goal paragraph.

```text
COMMON BRIEF - read fully before starting. Start your final report by quoting your model ID.

Goal of the run: <one paragraph: which update, what is being compared, what the worker's
answers will be used for>. You are tracing stored values in decoded game files. You are NOT
explaining game mechanics: report what is stored and where.

Folders (Windows, use forward slashes in Git Bash, quote paths with spaces):
  RUN  = <RUN>
  DOCS = C:/Users/royal/Documents/BF6 Frosty Research/docs/frosty
  DATA = C:/Users/royal/Documents/BF6 Frosty Research/reference-data/frosty

Inputs (all read-only):
  RUN/raw-index.tsv   <asset route><TAB><absolute path of the raw .ebx file>. Every raw game
                      file we hold. Search it with grep for names.
  RUN/roster-flat.tsv Values already read and named. Columns: source (own|reg), stat id,
                      owner asset, value name, value. Use it as anchors: a known named value
                      tells you which object you are looking at.
  DOCS/FIELD_MAP.md   Known meanings of Field_xxxxxxxx hashes. grep it for any hash you report.
  DOCS/*.md           Earlier findings. grep only; do not read whole files.

Decoder (turns raw .ebx into JSON). Put the .ebx paths, one per line, in a list file:
  python "C:/Users/royal/Documents/BF6 Frosty Research/scripts/frosty-ebx-decode.py" \
    --descriptors "C:/Users/royal/Documents/BF6 Datamining/builds/<BUILD>/capture/toolchain/SharedTypeDescriptors.ebx" \
    --ebx-list <list file> --out <output json>
Use the descriptors file of the client the raw files came from. A few hundred files per call is fine.

Decoded JSON shape: {"assets": {"<file path>": {"file","sha256","fileGuid","objects":[...]}}}.
Each object: {"$class":"Class_xxxxxxxx","$guid":...,"Field_xxxxxxxx": value, ...}.
{"$ref": n} points at objects[n] in the same file. {"$import":{"fileGuid","classGuid"}} points at
another file; match fileGuid against the "fileGuid" of other decoded files to follow it.
Field and class names are hashes. Numbers are 32-bit floats: 0.85 is stored as 0.8500000238,
so compare with a tolerance of 1e-4. Angles may be degrees or radians, times seconds,
percentages fractions (3.6% = 0.036): check each plausible encoding.

Method for every target value:
  1. Decode the named files. Search every numeric leaf for the target value (with tolerance).
  2. For each hit record: file, object index, object $class, full field path, value.
  3. A hit counts as "located" only if the same field path holds the matching value in the
     sibling files too. One isolated hit of a common number is "candidate", not "located".
  4. If the value is not in the named files, follow their $import links one step, decode those
     files and search again. Stop after two steps and report "not found" with what you searched.

Rules:
  - Write only inside your own output folder. Save every script you run there. No temp files
    elsewhere. Do not modify anything outside it.
  - Do not use the browser or the network. Do not run Frosty.
  - Never decode or open a material grid file (route contains materialgrid): it is too large.
    Read grid values from DOCS or DATA instead.
  - Never invent a value or a field meaning. "Not found" and "candidate" are valid answers.
  - Keep printed output small: write big results to files, print summaries.

Required outputs in your output folder:
  result.json  one entry per target: status (located|candidate|not found), file route, object
               class, field path, value(s), and the sibling check.
  summary.txt  under 80 lines: a table of the targets, then the extension table the task asks
               for, then anything that contradicts the patch notes or the anchors.
  files.txt    every file you decoded (route and sha256 from the decoder output).
Final reply to the orchestrator: under 50 lines, the same tables in compact form, plus any rule
you broke or shell call that was denied.
```

## Task briefs

Each is appended after the "First read ..." line. Fill the angle-bracket parts.

### A. Patch-note checklist (while the Stage 1 capture runs; `haiku-reader`)

```text
TASK - patch-note checklist. Input: <RUN>/patch-notes.txt (the notes as plain text).
Write checklist.tsv with one row per line of the notes that states or implies a stored value:
section, item (weapon / vehicle / gadget name as EA writes it), stat, from value, to value,
unit, and "asset home" taken from the table "Stage 7 - Map patch notes to assets" in
C:/Users/royal/Documents/BF6 Weapon Analyzer/docs/GAME_UPDATE_GUIDE.md (leave blank if the
table has no row for it). Put fixes with no number in a second file fixes.tsv: section, item,
EA wording. Skip the sections the orchestrator lists here: <sections to skip>.
Do not interpret or merge lines; one EA line can produce several rows.
```

### B. Pre-update "from" trace (the day before; `haiku-worker`, one per patch-note section)

```text
TASK - locate the pre-update values for <section>.
Named files: <routes or route fragments to grep in raw-index.tsv>.
Anchors already known: <named values from roster-flat.tsv for these files>.
Targets (EA's "from" values): <T1..Tn, each with the item, the value and the unit>.
EXTENSION (required): once a target field path is located, decode <the wider file set> and
write extension.tsv with that field's value for every file. In summary.txt list the items with
non-default values.
```

### C. Signal cross-check (after Stage 3 has the three lists; `haiku-worker`)

```text
TASK - cross-check the three change signals. Inputs: <patch summary file>, <comparison.json
from frosty-capture-compare.py>. Write signals.tsv: one row per asset route that appears in
any signal, with columns in_patch_summary, catalog_sha1_changed, raw_sha256_changed, added,
removed, guid_same_path_changed. In summary.txt give the count for each combination and list
every route where the signals disagree. Do not judge which signal is right.
```

### D. Diff triage (Stage 5; `haiku-worker`, split the changed list into batches of about 40 files)

```text
TASK - diff triage for batch <n>. Inputs: <RUN>/batch-<n>.tsv with route, old raw path, new
raw path. Decode old with <old descriptors> and new with <new descriptors>.
For each file match objects by $guid and $class. For objects with a null $guid, pair by class
and position only as a candidate, then confirm the pair: both objects must be referenced from
the same field path of an already matched object, or be the only object of that class in both
files. Give every row a match column: guid, confirmed or uncertain. Report field differences
on uncertain pairs with category "uncertain"; they are not changes until the orchestrator has
checked them. Compare field paths inside matched objects, keeping array order.
Write changes.tsv: route, object class, match, field path, old value, new value, category.
Category rules, in this order:
  uncertain      the object pair is not confirmed (above)
  string-id      field is Field_8cf424e7 or Field_fefe9de1
  expression     field is Field_0c18a620, Field_aa4fa860 or Field_c7ffe639
  fx-reference   field is Field_0679f638
  cosmetic       route contains /Art/Skins/, _Textures/Decals/ or _Charms/
  reordered      object identities, values, references and array order all agree
  other          everything else (do not classify further)
In summary.txt: per file, the count per category, and the full list of "other" changes for
files with fewer than 30 of them. List files where objects could not be matched, and every
uncertain pair.
Also list "control" files: in the batch but with zero changes.
```

### E. Consistency scan (Stage 6; `haiku-worker`, one scan per worker)

```text
TASK - consistency scan "<scan name>". Read the section "<scan heading>" of
C:/Users/royal/Documents/BF6 Weapon Analyzer/docs/GAME_UPDATE_GUIDE.md and run exactly that
scan over <file set / script named in the section>. Output scan.tsv with one row per item
checked and a pass/fail column, and in summary.txt every failing row with the stored values.
Then compare with the previous build's result at <path>: list rows that are new failures,
rows that no longer fail, and unchanged failures. Do not explain causes.
```

### F. Known-issue list recheck (Stage 8; `haiku-worker`, one list per worker)

```text
TASK - recheck the list <list file>. Inputs: <RUN>/changed-routes.txt (raw routes whose
SHA-256 changed), <RUN>/fixes.tsv and <RUN>/checklist.tsv (from task A).
For each entry of the list write a row in recheck.tsv: entry id or heading, the asset routes
the entry cites, which of them are in changed-routes.txt, and any patch-note line whose item
name matches the entry (quote the line). Then the mechanical status only:
  asset-changed        at least one cited route changed
  note-only            a patch-note line matches but no cited route changed
  untouched            neither
Do not mark anything resolved: that decision is made in the main session from the
asset-changed and note-only rows.
```

### G. Post-update "to" confirmation (after the new capture; `haiku-worker`)

```text
TASK - confirm the post-update values. Inputs: <previous run>/W*/result.json (located field
paths for the "from" values) and <RUN>/checklist.tsv. For every located field path, decode the
new raw file with the new descriptors and write confirm.tsv: item, field path, old value,
new value, EA from, EA to, and match (yes / no / field missing). In summary.txt list every
"no" and "field missing", and every checklist row that had no located field path.
```

### H. Availability census (Stage 7, new content; `haiku-worker`)

```text
TASK - availability census. Input: <RUN>/new-assets.tsv (catalog-added routes) and the new
build's raw files. For every added Attachment_* record, ammunition record, weapon and gadget
write census.tsv: item (file name), weapon, has_attachment_record, has_ability_branch
(<weapon>_ability branch list Field_d7605aab binds it), in_modifier_list (<weapon>_WB
Field_0cd9f20f holds its package), kill_switch_value (the stored value of its KST_* row, or
"no row"), in_weapon_aam (the weapon's AAM_* map lists it), in_game_name (from the AAM record
or name metadata, or "not found").
Report the stored kill-switch value as it is: true or false. Do not translate it to
"enabled" or "disabled", and do not classify items as live or not live; the main session
does that. In summary.txt list every item that lacks one of the columns.
```

### I. New-weapon part (Stage 9; one `haiku-worker` per part, or a larger model for part C)

```text
TASK - site data for the new weapons, part <A weapon records | B ammunition and ballistics |
C attachments>. Read "Adding a new weapon" in
C:/Users/royal/Documents/BF6 Weapon Analyzer/docs/GAME_UPDATE_GUIDE.md.
Site fields in this part: <list of data files and keys>.
STEP 1 (required before step 2): write an extractor that reads these fields from the new
build's raw files, run it for every existing site weapon, and write validation.json: per
field, how many weapons match the site, and every mismatch with both values. Do not adjust
the extractor to hide a mismatch; name its cause or mark it "cause not found".
STEP 2: run the same extractor on <new weapons>. Write proposed.json: fragments keyed by
target file and JSON path, each with the route and field it came from.
Write "not found" for any value the files do not give; do not fill it from another weapon.
In summary.txt: the validation table, every mismatch, every "not found", and values that
look like game data errors. Do not write to the site repo.
```
