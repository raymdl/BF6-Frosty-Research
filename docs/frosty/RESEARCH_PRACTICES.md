# Research practices

[Research index](README.md) · [Research queue](../working/FROSTY_RESEARCH_QUEUE.md) · [Tools](TOOLS.md)

How Frosty research runs are planned, staffed, checked and recorded, and the lessons
behind each rule. This page is a summary for readers. The rules that agents actually
run under live in these files, and they win where this page differs:

- [Standing orchestrator rules](../working/frosty-orchestrator-standing.txt)
- [Worker brief preamble](../working/frosty-worker-brief.txt) and
  [worker conventions](../working/frosty-worker-conventions.txt)
- The research queue's [working rules](../working/FROSTY_RESEARCH_QUEUE.md#working-rules)
- The review skill, `.claude/skills/review-frosty-research/SKILL.md`
- The [capture plan](../working/BF6_CAPTURE_PRIORITIES.md) for the recording rule

Model and usage-budget choices change often and are set in each session prompt, so
they are not listed here.

## Core principles

- **Values come only from Frosty source.** Community guides rank leads, and creators'
  published in-game tests can confirm how a mechanic behaves. Neither supplies
  numbers. Datamined community stats confirm nothing, because they come from the same
  files.
- **Keep three things separate:** what the bytes say, what we infer they mean, and
  what the game does at runtime. A missed name search does not show absence. A byte or
  name match does not establish meaning. Source presence does not establish runtime
  use.
- **Model what the game does, not what it describes.** When an attachment's intended
  effect does not apply in game, the site emulates the in-game result and notes the
  intended effect as a bug. A source-only omission without in-game confirmation is a
  candidate, not grounds to change the site.
- **Store full source precision.** Site data keeps the decoded float32 value and the
  UI does the rounding. Rounded burst rates (830 stored against 830.769 in source)
  shifted burst gaps.
- **Pin evidence to a build.** Run the build guard before any Frosty use. New
  evidence carries its Head and descriptor hash. An older receipt carries forward
  only where its cited raw SHA-256 equals the current bytes, and it keeps its original
  Head.
- **Name matching is supporting evidence only.** An identity join needs an exact
  GUID, import, pointer or id chain that can be re-read from raw bytes.
- **Controls and field names do not transfer across types.** A control proven on one
  owner type applies to another item only when the typed owner, the selected export
  and the schema match. A different type key stops the transfer (the M4A1 and L115
  controls were refused for the C-RAM, 2 October).
- **Stored values are not an operation.** Two stored numbers do not give a rate, a
  percentage or a combined damage until the operation that consumes them is shown.
  Repair Tool's stored 40 and a vehicle's stored health of 1000 do not give a repair
  time.

## Lessons learned

| Lesson | What happened | Rule now |
|---|---|---|
| Runs drift without steering | Standalone runs chased self-consistency checks, empty catalog screens and about 20 underbarrel leads that changed no site value (22-26 September). | A lead needs a plausible route to change a displayed number, expose a site calculation defect, or source a stat that matters for comparing loadouts. Stop a category after two consecutive leads produce nothing sourced. |
| Start new areas from UI metadata | 48 gadget leads traced from source alone mostly ended "value stored, meaning unresolved". One metadata pass then gave a function description for 63 of 78 gadgets (29-30 September). | A new area begins with a census of the game's UI metadata and strings, then traces the values it points to. See [UI text](UI_TEXT.md). |
| Census first in a new domain | The vehicle run worked census, then identity, then family stages, and used 6 workers. The gadget run inherited narrow one-question leads and spawned 47. | With no site data to compare against, map the whole area before launching narrow leads. |
| A control must exist | L103 spent a run on a control that was not in site data. | Every lead names a known-answer control from the same owner. If none can be named, skip the lead. A failed control means the route is wrong, and no negatives are recorded from it. |
| A control must test the operation | Vehicle and gadget runs read many stored values correctly but could not say which one the game uses (CB90 mortar launch speed: 80 in one place, 0 in another; 2 October). | Before briefing, ask which same-owner known-answer control can distinguish the operation that consumes the values. If there is none, record the values as source facts and stop. Do not repeat a broad scan in the hope that it settles meaning. |
| A negative result is narrow | After several paths reached a limit, the orchestrator told every lane to stop, and the operator had to restart four useful ones (2 October). | A "no useful lead" result closes that question by that method. It does not close the area or the other lanes. Reopen it only for a distinct question or method, and record what evidence would reopen it. The two-empty-leads stop applies to one category, not to the run. |
| Run-folder status goes stale | 42 cells were accepted after the pause checkpoint and review were written, so those files still say "pending" while the receipt and summary say "accepted" (2 October). | The receipt is the record of acceptance. Checkpoints and reviews are dated snapshots and say so. A summary that reports a later acceptance cites the receipt, not the snapshot. Before a run closes, the handoff, summary and receipts must agree. |
| Workers overrun | Raw walks ran 77-107 minutes even at 100 items or fewer. Whole-slot sweeps ran 40-100 minutes. | Size each worker for 30-60 minutes: about 30 items and a few hundred values. Split by weapon class or route group. Separate scanning from site arithmetic. |
| Long runs lose the brief | Workers in one wave compacted 4-6 times each and drifted. | Keep briefs compact and pass files by path. Keep a progress file and re-read the brief and that file after every compaction. |
| Briefs must carry their own conventions | A worker misclassified results because the brief left out a site convention, and a lead-only note leaked into six briefs. | Assemble each brief from the shared preamble plus only the convention sections that lead needs. Do not rely on workers reading reference docs. |
| Docs scattered | A new doc was written for each investigation. | Edit topic pages in place. Receipts hold the history. Generated indexes are never hand-edited. See [Where to record new work](README.md#where-to-record-new-work). |
| Parallel sessions collide | A commit swept in another session's staged hunks, and parallel record builds overwrote each other's entries (30 September, 1 October). | Stage only your own paths and hunks, through a separate git index while other sessions run. Runs do not build or commit generated files. The reviewer rebuilds once after all parallel runs close. |
| Proposals without a test have low yield | Many results said only "confirm units or availability". | Each proposal names its stat, the sourced value and a concrete validation step with a prediction. Without one it stays a finding. |
| Recordings are expensive | Over 100 hours went into weapon and attachment recordings, and most later requests asked for things the stat screen already showed. | Request a recording only when it passes the four-part rule in the capture plan, and ask the operator first. Gadgets and vehicles are not recorded; their meanings come from fields confirmed on infantry weapons, EA patch notes and UI text, and the rest is labelled "source value, effect unconfirmed". |
| Bounded overnight audits finish early | An attachments audit ended with no mismatches and left the session idle. | Unattended runs get a broad frontier and no early stop. Dead ends are recorded compactly in one "where not to look" map instead of one receipt each. |
| Large files bloat the repo and the disk | Run folders kept catalogs, junctions and superseded dumps. | Commit no file over 10 MB. Close each run with the cleanup step and a `cleanup.json`. |

## Where files go

The default answer to "should I create a new document?" is no. A finding belongs in
a page that already exists. Standalone documents in new places are the most common
cleanup cost after a run, and each one hides its content from the next run's
prior-work search and from the reader who looks in the topic page.

### The three places

| Place | Holds | Does not hold |
|---|---|---|
| The research repo (`BF6 Frosty Research`) | Current understanding, compact evidence receipts, research scripts. | Run narrative, bulk data, drafts, anything over 10 MB. |
| The run folder (`BF6 Datamining\reports\weapon-analyzer-research\<timestamp>-<area>\`, one subfolder per lead) | Everything a run produces while working: prompts, briefs, progress files, worker results, decodes, dumps, comparison tables, helper scripts, handoff, review, cleanup record. | Anything a later reader needs to find without knowing the run existed. That goes in the repo. |
| The site repo (`BF6 Weapon Analyzer`) | Site data, simulation, UI, and its copies of site-bound receipts and shared scripts. | Research output. Research runs do not write here. |

### What goes where in the research repo

| What you have | Where it goes | How |
|---|---|---|
| A finding about weapons, attachments, soldier mechanics, vehicles, gadgets or UI text | The matching topic page in `docs/frosty/` | Edit the existing section in place, or add a section to that page. Current understanding only. |
| A field or class meaning | A row in [Field map](FIELD_MAP.md) | With its confidence. |
| A link between assets | [Data graph](DATA_GRAPH.md) | |
| A tool, command, reproduction method or safety rule | [Tools](TOOLS.md) | |
| An unanswered question | A row in [Open questions](OPEN_QUESTIONS.md) | Delete it when answered. |
| The values, hashes and commands behind a result | One new dated JSON receipt in `reference-data/provenance/` with a `record` | `frosty-<yyyy-mm-dd>-L<id>-<short-topic>.json`. Never edited after commit; a correction is a new receipt that supersedes it. |
| A live lead, a proposal, or something waiting on the operator | The [research queue](../working/FROSTY_RESEARCH_QUEUE.md), or the area's working doc for gadgets and vehicles | A row or the current-run block. No progress narrative. |
| A stat list, coverage table or proposal for a future site area | The area's existing working doc ([gadgets](../working/GADGET_SITE_ADDITIONS.md), [vehicles](../working/VEHICLE_SITE_ADDITIONS.md)) | |
| Structured reference data a script or page reads | `reference-data/frosty/` | Only when a repo script or topic page uses it. Otherwise it stays in the run folder. |
| A research script others will rerun | `scripts/`, with a line in [Tools](TOOLS.md) | One-off helpers stay in the run folder, cited by path and SHA-256. |
| A run's results, limits and next steps | `handoff.md` in the run folder, plus the current-run block in the working doc | Replace the previous current-run block; do not stack them. |
| A dead end | The lead's record (status, what was searched, reopen condition) | For open-ended runs, one "where not to look" map, not one receipt per dead end. |
| A plain-English snapshot for the operator | Only when the operator asks for one | It is a dated reader aid, not evidence, and is not folded into topic pages. |

### Do not create

- A Markdown file per investigation, lead, run, family or date, anywhere in the
  repo, other than the dated working notes allowed below. This includes `*_SUMMARY.md`, `*_REVIEW.md`, `*_FINDINGS.md`, `*_NOTES.md`,
  `*_PLAN.md` and `HANDOFF*.md`.
- A new file in `docs/frosty/`. The set of topic pages is fixed. A new topic page
  needs the operator's approval first, and must be added to the [index](README.md)
  in the same commit.
- A new file in `docs/working/` without the operator's approval. An approved working
  note for a multi-day topic may carry its date in the name (for example
  `GAME_MODES_2026-10-21.md`, with its per-item files in a matching dated folder);
  link it from the index's research-status lines in the same commit. Whether it is
  later folded into a topic page or archived is decided at cleanup.
- A new folder at the repo root, under `docs/` or under `reference-data/`.
- Anything in `docs/archive/`. Archiving is done at cleanup, by the operator's
  session, not by a run.
- Review, schema-check or candidate JSON files in the repo, or loose at the top of a
  run or program folder. They belong in the lead's subfolder.
- Copies of a file under a new name (`-v2`, `-final`, `-fixed`). In the run folder,
  keep the version the result cites and note the superseded ones. In the repo,
  edit the page in place or supersede the receipt.
- Hand edits to generated files: `asset-findings.json`, `lead-index.json`,
  `site-evidence.json` and the Closed leads table in `FROSTY_QUEUE_CLOSED.md`.
- Junctions or symbolic links, in the repo or the run folder.

### When nothing seems to fit

1. Search first: `python scripts/frosty-worker.py prior-work --terms <names>`. The
   topic has usually been written up already, and the new result belongs beside it.
2. Pick the topic page by subject, not by run. A new section in an existing page is
   always allowed.
3. If it is still unclear, leave the material in the run folder, say so in the
   handoff under "placement needed", and let the operator decide. Do not invent a
   location.

### Check before each commit

- `git status` shows no new `.md` or `.txt` file, and no new folder.
- Every new file is a receipt in `reference-data/provenance/`, or a file the session
  prompt named.
- No file is over 10 MB, and no generated file is staged.
- Only your own paths and hunks are staged.

The handoff lists every file the run created in the repo. The reviewer flags any new
file outside the places above.

## Roles

Most runs use two tiers: an orchestrator and its workers. The 2 October
vehicle and gadget program added a researcher tier between them. A reviewer checks
every finished run.

### Orchestrator

- Chooses leads, writes briefs, verifies results and writes the repo docs.
- Starts with `python scripts/frosty-records.py status` and the previous run's handoff
  and review, not by reading the queue and archive whole.
- Writes each lead's question, route, fixed scope, reuse pointers and control before
  launching it.
- Answers small questions directly instead of briefing a worker.
- Never relaunches a worker until the original has stopped.
- Runs `frosty-worker.py review` on each result before reading it, re-reads at least
  one consequential operand from raw bytes with `frosty-raw-check.py`, and checks the
  examined counts against the brief. The worker's summary is not trusted on its own.
- Keeps a progress file in the run folder and re-reads the prompt and that file after
  any compaction.
- Closes each lead with a receipt that has a `record`, the topic-page edit, a passing
  `check-receipt`, and a local commit.
- Never changes site data, simulation or UI, and never pushes.
- When several lanes run, gives each one functional area, assigns each shared
  blocker to one owner, and keeps the other lanes running when one reaches a limit.
- Is the only role that writes to the repo, and follows [Where files go](#where-files-go):
  no new documents or folders without the operator's approval.
- Ends with a handoff, the current-run block in the area's working doc, and
  run-folder cleanup.

### Researcher

Used when one orchestrator supervises several research paths at once.

- Owns one assigned research path covering one functional area (for example repair
  and revive, sensing, or vehicle weapons) and may use workers for specific, bounded
  checks.
- Works from a brief with a concrete question, an owned output folder, a control and
  a stop condition.
- Does not work on a blocker shared between lanes unless it is the one owner the
  orchestrator assigned to it.
- Reviews its workers' evidence and prepares the source packets and handoff for that
  path.
- Its review is not acceptance. The orchestrator makes its own targeted checks
  against source evidence before a finding enters the program summary.
- Starts from existing evidence and exact selected assets, and checks prior coverage
  before tracing.
- Applies a proven tracing method to other items only after separate coverage and
  schema checks for those items.
- Records each unresolved path with its limit and the condition for resuming it, and
  checkpoints unfinished work.

### Worker

- Answers one question with a fixed item count. Read-only: it writes only under its
  lead folder and never runs git write commands.
- Reports the control first and stops if the control is not reproduced.
- Raw-verifies every consequential value: file path, raw SHA-256, byte offset, bytes
  and decoded value.
- Searches prior work and reuses earlier decodes before decoding again.
- Stays inside the brief. Anything else it notices goes under `outOfScopeNotes`,
  uninvestigated.
- Inspects large files through scripts that print counts and samples, never whole
  files, and builds results with scripts that write files so findings survive
  compaction.
- Delivers a result JSON, a short summary and a draft receipt that passes
  `check-receipt`.
- Does not delegate further.

### Reviewer

- Verifies; does not redo the work. Writes only `review.md` in the run folder.
- Runs nine checks: scope and rules, commits, records, raw bytes, headline values,
  controls and scope counts, proposals, evidence version, cleanup.
- Escalates approach questions when most results are "unresolved" or "limit", leads
  were rerun repeatedly, a result contradicts an earlier receipt or a site value, a
  proposal would change the site, or a commit, raw-byte or headline-value check fails.
- After all parallel runs close, rebuilds the generated record files once, with the
  operator's approval.

## Judging a run

- Weapon, attachment and soldier runs are judged on site outcomes: a corrected value,
  an exposed defect, or a proposal with a validation step.
- Vehicle and gadget foundation runs are judged on readiness for a future site
  version: identities, which values the game actually uses against inherited
  defaults, units, labels and validation routes.
- A run whose results are mostly limits points to a wrong method, not unlucky leads.
