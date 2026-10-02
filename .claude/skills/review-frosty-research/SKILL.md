---
name: review-frosty-research
description: Review a finished Frosty research run (Codex/Sol orchestrator handoff) — verify commits, records, raw bytes, headline values, controls, proposals and cleanup, then write review.md. Use when the operator asks to review a research run, handoff or overnight session. Intended for Sonnet 5.5 High; escalates approach problems to Opus.
---

# Review a research run

You are the reviewer, not the researcher: verify, do not redo the work. Keep reads targeted: use
scripts that print counts and samples, and never read large JSON files whole. Change nothing
except the review.md you write at the end; no commits, no pushes.

Run every command from `C:\Users\royal\Documents\BF6 Frosty Research` ("this repo" below); relative
paths assume it, even when the session started in another repo.

## Inputs

Ask the operator for anything missing (usually one path is enough to find the rest):
- the handoff (`handoff.md` / `HANDOFF.md`) and its run folder under
  `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\`;
- the saved prompt, `orchestrator-prompt.txt` in the run folder;
- the run's receipts in `reference-data/provenance/` (from the lead ids in the handoff).

## Checks

Report each as pass or flag, with the evidence in one line.

1. **Scope and rules.** Compare the handoff with the saved prompt. Did the run stay in its
   stages and stop where the prompt said (for example at an approval gate)? List skipped or
   added stages.
2. **Commits.** In this repo and `C:\Users\royal\Documents\BF6 Weapon Analyzer`, run `git log` and
   `git show --stat` for the commits the handoff names. Flag commits touching site `data/`,
   `sim/`, `ui/`, `index.html` or `assets/`; files outside the run's topic; or anything pushed
   (the branch must still be ahead of origin).
3. **Records.** `python scripts/frosty-records.py check` must pass. Known warnings:
   ledger-stale, the L107 value-changed warning and the two L604 warnings. Flag any other.
   Runs no longer commit generated files, so "[generated] out of date" is expected. Once
   every parallel run has closed and the repos are clean, the operator may approve one
   `build`, a re-check and a single generated-files commit in each repo; otherwise flag it.
4. **Raw bytes.** `python .claude/skills/review-frosty-research/review-rawcheck.py "<receipts glob>"`.
   Any byte or value mismatch or missing file is a flag.
5. **Headline values.** Take the 3-5 numbers the handoff leads with. Decode each cited raw file
   independently: `python scripts/frosty-ebx-decode.py --descriptors <descriptor for that Head,
   from builds\1.4.3.0\BUILD.json clients> --ebx <raw file> --out <scratch json>`, find the
   field by its hash (receipt or `docs/frosty/FIELD_MAP.md`) and compare. Note headline values
   that no receipt raw-checks.
6. **Controls and scope.** Each lead's known-answer control passed before findings, and the
   examined counts match the brief's scope.
7. **Proposals.** Each names its site data/code, the sourced value, how it activates, and a
   validation step with a prediction. Flag proposals that only say "confirm units/meaning".
8. **Evidence version.** New evidence carries its Head and descriptor; Heads are not mixed.
9. **Cleanup.** The run folder has `cleanup.json`, no junctions or symbolic links, no
   `asset-catalog.json` from targeted captures, and no uncited files over 50 MB.

## Escalate to Opus

Say so at the top of the review when:
- most results are "unresolved" or "limit" rather than values — the method may be wrong, not
  the leads (for example, classifying multiplayer availability from source when the game's UI
  metadata or loadout presets would answer it);
- leads were rerun (v2/v3) repeatedly, or scope grew without approval;
- a result contradicts an earlier receipt or a site value;
- a proposal would change site data, simulation or UI;
- check 2, 4 or 5 fails.

## Output

Write `review.md` in the run folder: verdict (accept / accept with flags / escalate), a table of
the nine checks, flags with evidence, and decisions for the operator. Then give the operator a
summary of at most 10 lines.
