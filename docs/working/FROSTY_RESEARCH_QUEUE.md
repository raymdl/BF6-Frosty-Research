# Frosty research queue

[Research index](../frosty/README.md) · [Open questions](../frosty/OPEN_QUESTIONS.md) · [Capture plan](BF6_CAPTURE_PRIORITIES.md)

## Objective

Vehicle research runs separately in [Vehicle research and potential Analyzer additions](VEHICLE_SITE_ADDITIONS.md). The operator authorized all-vehicle tracing on 29 September 2026; vehicle lead IDs start at L3000.

On 3 October, the operator authorized a continuing [mechanics research program](VEHICLE_SITE_ADDITIONS.md#orchestration-and-evidence-rules) across vehicles, gadgets, weapons and attachments. The vehicle screenshot worklist is its first stage. Subsequent assignments must identify a potential site benefit and new evidence or method, reuse completed findings, and preserve unresolved source/runtime boundaries. The local orchestrator maintains the active roster and 20-minute supervision schedule.

On 9 October 2026 the operator set this broad goal for vehicle and gadget research: **understand, from the game data, how every multiplayer vehicle, vehicle weapon, vehicle upgrade and gadget works, well enough that a future version of the site could show and compare them the way it does weapons and attachments.** For each item that means its identity and category (stat id, archetype, in-game name), what mounts or carries it, the stored values behind its damage, blast, projectile, ammunition, reload, cooldown, range, duration and durability, and which of those values a live match uses. The roster to cover is the game's own: the stat-category entries of L3306 (33 vehicles, 68 gadgets, 66 vehicle equipment items). Site implementation still needs separate authorization.

Keep tracing Frosty source to find information that changes or explains Analyzer
values. Priority order:

1. Site values that are wrong, assumed or based only on screenshots.
2. Mechanics the site does not model that could change displayed stats, and
   weapon/attachment/soldier stats it does not show yet but that matter for
   comparing weapons and loadouts (enhancement proposals, e.g. class traits).
3. Source evidence that narrows a question the capture plan would otherwise have
   to answer in game.

Scope is multiplayer weapons, attachments, optics and soldier mechanics. Check maps
and modes only for overrides of those mechanics. Exclude only supported cosmetic,
single-player-only and battle-royale-only content.
Gadget research and proposals for future site functionality are maintained in
[potential gadget additions](GADGET_SITE_ADDITIONS.md).

**This queue has no completion condition.** Classifying an item as "blocked" does
not end its tracing. After each lead, record the result in the owning topic page,
add any new leads it exposes, and move on to the next one. Mark a lead exhausted
only with a list of what was searched: fields, value searches, catalog scope and
callers. "Needs a native consumer" is a reason to look for one, not a stopping point.

## Working rules

- Research only: tools, evidence and docs. Production data changes need the
  operator's approval first. Do not push.
- Use float32/int32 value searches, then decoded-field and raw-byte checks. A missed
  name search does not show that something is absent. A byte match alone does not
  establish meaning. Source presence does not establish runtime use.
- Follow a dependency only when it can affect an Analyzer value. Broad catalog
  expansion (tasks E1–E4 in the [23 September snapshot](#history)) stays deferred.
- Closing a lead has three steps: (1) a new dated receipt in
  `reference-data/provenance/` with a `record` (lead status, assets, site pointers;
  `python scripts/frosty-records.py schema` prints the fields), (2) the `docs/frosty/`
  topic page, edited in place (current understanding only; history lives in
  receipts), (3) delete the lead's row from this queue. Then
  `python scripts/frosty-records.py build && python scripts/frosty-records.py check`
  must pass before committing. `asset-findings.json`, `lead-index.json`,
  `site-evidence.json` and the archive's Closed leads table are generated; do not
  hand-edit them. Do not create per-investigation Markdown docs or append progress
  narrative to this queue.
- Start every run with `python scripts/frosty-records.py status` instead of reading
  this queue and the archive whole.
- Captures: follow the four-part rule at the top of the
  [capture plan](BF6_CAPTURE_PRIORITIES.md). Ask the operator before requesting a
  recording; an unresolved runtime question is recorded as a limit, not a capture.
- Keep 1.4.3.0 (Head 4892017, descriptor `91c9ea7c…`) and 1.4.3.1 (Head 4892087,
  descriptor `99b49cfd…`) evidence separate. Use hashes, not file versions. The
  `builds/1.4.3.0` folder name is the retained identifier for both. New work uses
  the open build 2.1.1.0 (13 October; Head 5382784, descriptor `c477622c…`,
  `builds/2.1.1.0`; hotfix clients of 15 and 22 October share its type layouts, see the
  [update ladder](../updates/README.md)). 1.4.3.5 (Head 4909002, descriptor `4c28ad65…`) is
  sealed. An earlier receipt carries forward only where the cited raw SHA-256 equals the
  current bytes. On 30 September (1.4.3.5), 1,070 of 1,073 cited raw assets were
  equal; the other 3 citations are `GRX_Vehicles`, which differs only by the
  reviewed string-id renumbering (`builds/1.4.3.5/reports/carry-forward-2026-09-30/carry-forward-result.json`).
- Start a new exploration area from the game's UI metadata (`Common/UI/Static/Metadata`,
  `Common/UI/MetaData`): in-game names, descriptions and the numbers they state. They
  say what each item does and which source values to trace; tracing without them
  produced source profiles with unknown meaning (gadget run, 29 September). Resolve
  strings as in [UI text](../frosty/UI_TEXT.md).

### Awaiting operator

- Captures ([capture plan](BF6_CAPTURE_PRIORITIES.md)): Match Trigger semi vs auto
  (L17; final brief `2026-10-30-review-gaps/L4073/capture-brief.md`: M433 200 ms pairs, semi then
  auto, AK4D control; the site already applies the block in semi since 24 Oct, so the capture
  validates it). The L99 hit-capsule capture was settled by L4010 (10 Oct); burst cadence closed
  without a recording.
- Review the class-trait, single-fire rate (L14) and RPK-74M reload proposals, plus
  the ADS-out time (L114) and stance-change penalty (L120) proposals (burst-rate
  precision closed 30 Oct: implemented).
- Mounted-state recoil (L108) and reserve-rounds / chambered-round (L110) proposals:
  deferred by the operator (28 Sep); keep them in the proposal table.
- Recovery-scale capture (L4062, 30 Oct): one M87A1 pump-pair set (12 pairs at the 633 ms
  cycle, 6 null pairs over 1 s; prediction 1.57 degrees at x0.8 against 1.21 at x1.0). Brief in
  `BF6 Datamining/reports/weapon-analyzer-research/2026-10-30-review-gaps/L4062/capture-brief.md`.
  Bolt-action pairs are not justified (the scales differ by under 0.012 degrees at 300 ms).
- Capture-rule review (L4066, 30 Oct): a draft revised rule that keeps the four parts and adds a
  one-minute glance class with a stated prediction, plus the blocked-items table (L110, L120/L124,
  L22/L25 and L69 glance-eligible; L114, L17, L19, L105 need recordings).
  `.../2026-10-30-review-gaps/L4066/capture-rule-review.md`, for the operator's decision.
- Registry precedence check (L4058, 30 Oct): M136 AT standing, aimed, five rockets at a wall about
  100 m away; file spread 0.0 predicts every impact on the crosshair, registry 0.35 degrees predicts
  scatter up to about 0.6 m. No site number depends on the answer today. `L4058/operator-check.md`.
- Three one-minute glances (30 Oct): reserve rounds on the M4A1 20 Rnd (L4068), M433 Sprint Recovery
  on an Assault against a Support soldier (L4070); and one recording for ADS-out (L4067, M4A1 vs M240L).
- Tooling for the operator's OK (L4058, L4059): the registry-against-file assertion in
  `frosty-configuration.py` (design in `L4058/assertion-proposal.md`) and the Stage 0/1 guide text
  (`L4059/guide-text.md`; `scripts/frosty-hotfix-check.py` is installed).

<!-- review-gaps-2026-10-30:start -->
## Review-gaps run (closed 30 October 2026)

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-10-30-review-gaps/`, L4057-L4082 (L4064 opened as a lead, L4065 split A/B), build 2.1.1.0 (guard OK; captures `expression-graph-bodies-2026-10-30`, `-b-2026-10-30`, `missing-attachments-2026-10-30`, `roster-refresh-2026-10-30`). Orchestrator Claude Fable 5.1; 22 workers (Opus 5.5 for L4057-L4059, L4071, L4076-L4078; Sonnet 5.5 for the rest). No site data, sim or UI change; one docs-only site commit (`48da623`, update guide Stages 0, 1 and 5). No push. Seventeen receipts for the 17-26 October measurements and the 19 October recheck rows (L4051-L4054) were written so the record system sees them (L4063).

| Lead | Status | Result | Commit |
|---|---|---|---|
| L4057 | finding | Expression-graph diff 1.4.3.5 to 2.1.1.0: 304 graphs, 188 ids unchanged (bodies byte-equal), 116 re-baked, 17 changed in substance (Spooky Rush contracts, ArmorGrant gate, man-down PVE branch, XP graphs); re-bake is not noise. Stage 5 rule applied to the Analyzer guide; resource-id file beside `raw-routes.txt`. | `05bb686` |
| L4058 | finding | Registry precedence: 0 of 15,879 site-weapon pairs differ on 2.1.1.0; no attachment-effect file has a registry row; 98 differing pairs are gadget, launcher and vehicle rows. AAHV heat cannot decide precedence (8 shots either way); proposed check is the M136 AT aimed spread (0.0 vs 0.35). Generator table and the `frosty-configuration.py` assertion design in the run folder. | `bead0f9` |
| L4059 | finding | Gameplay-shape route list (41,196 routes; holds all 283 changed-not-captured assets); `scripts/frosty-hotfix-check.py` installed, flags only the REDSEC graph on the two hotfixes and the XP caps plus 6,651 registry rows on the update. Stage 0/1 guide text applied. 18 registries never captured. | `bead0f9` |
| L4060 | finding | Strings census: 303 number-bearing rows, 56 traced, 3 conflicts (Quick Plating 25% vs 1.5; CDX40 Single Shot 30-60 m vs curve 42-68 m; Low-Zoom 2x/3x resolve to "4x"); M2010 ESR and SV-98 description ids are djb2 of unhashed names in no table; E6 strings located. | `cde0ce0` |
| L4061 | finding | Re-screen of 116 negative closures: 46 "stored, no consumer"; 30 stand, 14 unscreenable, L3380 (armor) reopened; L7 control detected. | `6cfa65b` |
| L4062 | finding | Recovery scale 0.8 is measured on AK-205, TR-7, M433 and LMR27 (a DMR); 63 weapons are transfer; bolt-action pairs cannot test it; the smallest capture is M87A1 pump pairs (1.57 vs 1.21 degrees). | `5799671` |
| L4063 | finding | 17 receipts drafted and recorded for the October measurements and L4051-L4054. | `bead0f9` |
| L4064 | open | Standing grip-pod recoil ratio 0.80 measured vs 0.890 predicted: new lead in the Active table. | `bead0f9` |
| L4065 | finding | ELR-40 mag 8 = 7 Rnd package capacity (nominal +1; closes L4055); Mk 24 index 12 -> head 1.57 confirmed; Season 5 heat, class-trait and limb reads; Stage 8 items done (ReloadSpeed divisor reproduces all 67 reloads; selector graph from 2.1.1.0 raw; optic FOV unchanged); roster-values.json refreshed with corrected joins; 2.1.1.0 patch-notes entry; burst-rate row removed (8h). | `6cfa65b`, `b0d71fd`, `91d0c50` |
| L4066 | finding | Capture-rule review draft (glance class) for the operator. | `5799671` |
| L4067 | proposal | ADS-out on 67 of 67 (General_10 by the ADS index; no attachment shift found); Mobility row proposal; validation recording M4A1 vs M240L. | `bead0f9` |
| L4068 | proposal | Reserve rounds: 302 of 303 magazine choices read (+1 on 277, +0 on 24, +2 DB-12); "20+1 / 189" card line; one spawn-HUD glance decides reading A or B. | `bead0f9` |
| L4069 | proposal | Stance-change penalties unchanged on 63 of 63, four profiles; posture minima columns unread by sim; posture selector proposal with the drop-prone glance. | `18c7bc3` |
| L4070 | proposal | Class-trait chip: on-class and off-class values for 41 of 67 weapons; Season 5 membership confirmed; stat-screen glance (M433 Sprint Recovery, Assault vs Support). | `bead0f9` |
| L4071 | finding | GCR ladder: 14 steps, override of two GS camera fields, no unit, unchanged on 2.1.1.0; SU-230 fix acted in the shared Elcan part, not the ladder. No chip. | `b0d71fd` |
| L4072 | proposal | 54 singleton zeros (100/60/75 m) read on 2.1.1.0; ELR-40 CustomZeroing true (only one); default-zero proposal for the Soldier Target view, M4A1 100 m glance (-5 vs -18 cm). | `18c7bc3` |
| L4073 | finding | Match Trigger: site semi-only block (24 Oct) equals the source; 26 site weapons bind the same effects; M433 package replaces the local selector; final capture brief (200 ms pairs, AK4D control). L17/L24 re-recorded site-supported. | `a256bed` |
| L4074 | finding | Projectile lifetime: TimeToLive on all 94 PD files; all 353 ammo selections reach 3.5x or more of their damage curve (shortest 151.6 m for buckshot against 34 m), so no Range card note applies. The brief's PD InitialSpeed control clause was wrong (PD stores 350 or 0; the muzzle velocity is WB Shot.InitialSpeed.z). | close-out |
| L4075 | proposal | Movement speed m/s: walk 3.5, sprint 6.05, LMG x0.95 on exactly the 11 LMGs, ADS-move index equals the site on 67; Mobility row proposal with a timed 50 m test. | `18c7bc3` |
| L4076 | finding | Armor plates are REDSEC and Gauntlet content by every source route (ArmorGrantSpawnPlate feeds the loot grant; SpawnWithArmor 0; no 2.1.1.0 importer of Ability_ArmorGrant); unplated BTK unchanged. Answers the L3380 reopen. | `fd73086` |
| L4077 | finding | Census: 94 bullets x 29 vehicle, emplacement and deployable materials, 812 pairs; tanks 0, deployables 1; L3364 cells unchanged. No narrow lead. | `b0d71fd` |
| L4078 | exhausted | Ricochet: 0 string hits, no named field, no consumer; penetration text is the collateral the site models. | `91d0c50` |
| L4079 | finding | H1 and ZDA column 4 are the hip and ADS jump/sprint minima by position (one label); the site holds H1 in HIP_SPREAD_TABLE; one jump glance can tell table (2.5x) from GS leaf (1.75x). | `b0d71fd` |
| L4080 | finding | Downed damage: no stored 0.8; the man-down graph applies affectors x0 / x2 and crawling x0.05 / x0.45; EA's 20% line is 1.3.1.0. | `5981993` |
| L4081 | exhausted | No stance-gated recoil modifier, condition asset or GS field on 2.1.1.0. | `b0d71fd` |
| L4082 | finding | Swap = holster(A) + draw(B) from the shared DTA row (300 to 1,167 ms); sprint-to-fire input is the Sprint Recovery the site shows. | `5981993` |

- **Awaiting the operator:** the capture-rule review (L4066), the M87A1 pump capture (L4062), the Match Trigger capture (L4073), the ADS-out recording (L4067), the registry precedence check (L4058), four one-minute glances (L4068 reserve rounds, L4070 class trait, L4069 drop-prone, L4072 zero), the tooling OKs (registry assertion, L4058; guide text applied as docs-only, L4059), and three OPEN_QUESTIONS rows from the strings census (L4060).
- **Site proposals (not implemented):** ADS-out row, reserve-rounds card line, posture dimension, class-trait chip, default zero, movement speed row (L4067-L4070, L4072, L4075). Each has a validation step in its receipt.
- **Needs capture (source only):** `SimEx_BR_ApplyProgressionWeapon` body and `WPM_MAG_100Cpt1_PKM_W05` are not in the catalog; `SimEx_CeramicArmor` / `SimEx_SoftArmor` bodies, `Ability_ArmorGrant` and the `FieldUpgradePath_BR_*_Y2` paths, the renumbered movement resource `0550f387167b0bdd`, and the 18 registries of the new route list.
<!-- review-gaps-2026-10-30:end -->

<!-- weapons-registry-2026-10-10:start -->
## Weapons and attachments run (closed 10 October 2026)

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-10-10-weapons-registry/`, L4000-L4009, build 1.4.3.5. Read from saved raw files only; no capture, no push. One site edit, approved by the operator during the run (L4008). The run applied the 9 October vehicle and gadget methods (registry default against own value, registry row names, EA patch-note figures) to weapons, bullets and attachments.

| Lead | Status | Result | Commit |
|---|---|---|---|
| L4000 | finding | Registry default equals the own value on every compared row of the 63 site weapons, their firing data and their bullets. The registry-or-own question of L3356 does not arise for weapons. **Rechecked on 2.1.1.0 (19 Oct): still 0 differing over 14,838 values (279 row names); six defaults moved (M39 EMR and SVDM recoil), the own value moved with each ([L4051](#current-weapons-registry-recheck-19-october-2026)).** | `5279418` |
| L4001 | finding | EA 1.3.3.0 recoil variation equals the site on 39 of 39 weapons. EA states the M45A1 and vz. 61 are subsonic by default; their stored spotting ranges are 27 / 64.29 against 54 / 150 on the other 61 weapons. | `5279418` |
| L4002 | exhausted | Registry rows name 102 weapon fields; 101 were already in FIELD_MAP.md. No hash cited by 116 earlier negative closures gains a name. `Field_440ed7fa` has no registry row. **Rechecked on 2.1.1.0: row suffixes unchanged (332), no new name; 1,836 value rows added, all on the new weapons, five new bullets and M240L stance rows (L4053).** | `5279418` |
| L4003 | finding | Site velocity, magazine, drag and limb values equal the stored rows on all 63 weapons; the eight rate-of-fire differences are the single-fire VSSM and seven manually cycled weapons. **Rechecked on 2.1.1.0: all 441 records identical; site equals source on every existing weapon (L4051).** | `5279418` |
| L4004 | finding | Bullet damage curves are equal between registry, own files and the site; the M45A1 keeps its reviewed step. **Rechecked on 2.1.1.0: health curves unchanged; 13 armor curves changed, registry and own together (L4052).** | `5279418` |
| L4005 | finding | Weapon and attachment figures in EA notes 1.1.3.0 to 1.4.3.0 agree with the site or were superseded. | `5279418` |
| L4006 | exhausted | Parked questions W1-W9, O1-O3, M1-M3 and G1 screened against the three methods; none is reopened. | `5279418` |
| L4007 | finding | Head-table index equal on 63 of 63; seven manually cycled rates reproduced from stored bolt fields; reload sums equal on 48 tactical and 45 of 58 empty values, the rest are reviewed capture values. EA: Interdictor limb damage matches chest; Match Trigger must not affect automatic fire. | `5279418` |
| L4008 | site-fixed | The operator's stat-screen screenshots show 27 / 64 m for the M45A1 and vz. 61 (0 / 9 m suppressed). Source, EA and the stat screen agree; the site's 54 / 150 was wrong for these two. | `5279418` |
| L4009 | finding | Audit of 116 earlier negative closures: 16,432 recorded byte checks all match the current files; ten claims from the 45 leads without byte checks were re-tested by a second route and none is contradicted. | `5279418` |

- **One site change, approved by the operator:** spot-on-fire base 27 / 64.285713 for `m45a1` and `vz61` (site commit `b6da447`, on origin/main).
- **Audit of earlier closures (L4002, L4009).** Registry names recover nothing the earlier runs missed; all recorded bytes are intact; re-tested claims hold. The one wrong outcome was the consequence drawn from L7 (one spot base for all weapons). Closures of the form "stored but no consumer found" should be checked against the screenshot audit or EA notes before they are accepted.
- **Dead ends.** Attachment effect files (`WME_`, `WPM_`, `GDM_`, `GID_`, `AAM_`) have no registry rows, so none of the three methods reaches attachment effects. Weapon rows under `WeaponModifierDataAssets` carry only a Priority value.
- **Outside this run's scope.** The L4000 pass lists 74 registry-against-own differences on gadget, launcher and vehicle owners, 40 of them not in the L3314 census (for example `GS_AT4`, `GS_MBTLAW` and `GS_RPG7v2` zoomed dispersion). They are in `reference-data/frosty/weapon-registry-own-comparison.json` for the vehicle and gadget work.
- **Tests for the operator:** none new. The L4001 spotting test is withdrawn (L4008). The Match Trigger capture (L17) remains optional: all 24 Match Trigger stat panels equal the site's display, so it would only decide whether to model a single-fire effect the game does not show.
<!-- weapons-registry-2026-10-10:end -->

<!-- weapons-registry-recheck-2026-10-19:start -->
## Current weapons registry recheck (19 October 2026)

Run: `BF6 Datamining/builds/2.1.1.0/reports/weapon-registry-recheck-2026-10-19/`, note [WEAPON_REGISTRY_RECHECK_2026-10-19.md](WEAPON_REGISTRY_RECHECK_2026-10-19.md), build 2.1.1.0 (hotfix capture). Read from saved raw files only; no capture, no site edit, no commit, no push. Re-run of L4000, L4002, L4003, L4004 and L604. The brief asked for rows from L4020; L4020 to L4050 are closed leads with receipts, so these rows are L4051 onward. They still had no receipts on 25 October, so the lead index does not list them; L4055 is open.

| Lead | Status | Result | Commit |
|---|---|---|---|
| L4051 | finding | L4000 and L4003 repeated: 14,838 registry-against-own values (279 row names, 63 weapons) equal on both builds; 6 defaults moved (M39 EMR, SVDM recoil), own value with them. Site equals the source on every existing weapon (441 records identical to 10 October); the SVDM and M39 EMR edits of 13 October match. Own leaves: 2,006 differences over 74 files, all in six classes (priority index shifts, recoil, spot-on-fire 54 to 75, class profile, array entries, armor curves). | - |
| L4052 | finding | L4004 repeated: health curves unchanged on all bullet files; 13 armor curves changed (own and registry together, equal); site `dmg` lists unchanged. | - |
| L4053 | exhausted | L4002 repeated: 1,836 value rows added (tsv: 2,150 in `GRX_Weapons`; the 1,846 figure does not reproduce); row suffixes unchanged (332); 106 value-matched names, all in FIELD_MAP.md; none for the open-question or negative-closure hashes. | - |
| L4054 | finding | L604 repeated: mode lists and rates unchanged on 63 of 63, 12 branch files byte-identical. SGX and L110 lost the `_Ergo/CMU_SemiAuto` import; M433 gained a Match Trigger W15 import. | - |
| L4055 | finding | Closed 30 Oct ([L4065A](../../reference-data/provenance/frosty-2026-10-30-L4065A-season5-loose-ends-elr40-mk24.json)): ELR-40 site `mag` 8 is the 7 Rnd package capacity (nominal 7 + 1, as on the six other bolt-actions); `CDX40_WB` 1 is the bare receiver. The `M16A3_WB - InitialSpeed.z` 720 row, the M433 Match Trigger import and the 13 armor curves are taken up by L4058, L4073 and L4076 of the 30 Oct run. | `5799671`+ |

- **Operator action:** none. The ELR-40 magazine question is settled (L4055, 30 Oct): no site change.
<!-- weapons-registry-recheck-2026-10-19:end -->


<!-- gunfight-mechanics:start -->
## Current gunfight mechanics run (closed 1 October 2026)

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-10-01T084200-0400-gunfight-mechanics/`. Area gunfight-mechanics. Owned L741-L748 and L1100-L1199. Build 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. The available controlled frontier is exhausted within the named routes. L1105-L1199 remain unused; no placeholder leads were created.

| Stage / lead | Completed result | Remaining condition |
| --- | --- | --- |
| Stage 1, L741-L748 | All eight ranked questions have routes and control dispositions. Exact package text and structural identities are retained. Five guarded shared-lock batches captured 12 owners, zero failed routes. | Water damage, fatal precision, attachment weight, functional packages, melee, destructible cover, ping timing and sneaking audio lack the requested semantic controls. No new mechanic quantity follows. |
| L1100, creator map | Six primary-author controls; 21 dated public metadata items; 11 ranked mechanic groups. Patch inventory remains read-only and unchanged. | No spoken/numeric test result. Direct velocity/drop, sprint-to-fire, swap and hit-registration topics remain gaps; ADS timing and flinch also lack verified results. |
| L1101, damage/ballistics | Four groups, three base examples; 79 worker raw checks. Selected damage, multipliers, base velocity, cadence, gravity and drag agree with current site operators. Parent velocity re-read passed. | Native curve precedence, lethal precision, bolt readiness and trajectory execution remain open. The initial wrong velocity owner was stopped and corrected; no negative conclusion used it. |
| L1102, spread/recoil | M433, two groups; 93 fresh reads and 69 site input comparisons. Source selectors and inputs agree. Parent IncreasePerShot re-read passed. | Native sampler, recovery, state selection, random delivery and input/camera composition remain open. |
| L1103, handling/movement | M433 bare/30Rnd/20Rnd, four groups; 69 helper checks and 70 source reads. Selected table values support software outputs. Parent sprint setting re-read passed. | Native ADS composition, sprint firing readiness, total swap, movement units and jump accuracy remain open. |
| L1104, final route audit | Three named route dispositions; current owner/site hashes match. Zero mechanic operands read. | Hit acceptance/health commit, gameplay suppression and flinch need exact native consumers and same-owner effect controls. The missing-control review flag is retained; no absence claim follows. |

No new source/site correction or proposal was established. Existing proposals are unchanged; no duplicate holster or idle-recovery proposal was added. Community numbers never became source values. Controls, serialized facts, software policy and unresolved native behavior remain separate.

Method switches are recorded in `orchestrator-progress.md`: exact caller bodies and reverse input/config recipients replaced widening unresolved routes; primary author metadata replaced failed public discovery; actual site operators and exact declaring fields replaced repeated limit batches. `where-not-to-look.json` has 24 compact dead ends, each with route, fields, tried, stop reason and reopen condition. Eight receipts cover the batches. Original failed review/owner nominations are preserved beside corrected immutable results.

Reopen only when the exact consumer/control named in a dead end becomes available, or when accessible creator test text supplies a dated, testable meaning to corroborate. For new source/site disagreements, require a sourced operand and a concrete stat-screen, EA-text or cited-creator validation prediction before proposing a change. No site data/simulation/UI edit, recording, generated build or push occurred. Run handoff, review and cleanup receipts are in the run folder.

Local lead commits:
- `8414ed2e6fe600a4d29842162dbb34f137bc9847` - ranked-damage
- `8414ed2e6fe600a4d29842162dbb34f137bc9847` - ranked-soldier
- `8414ed2e6fe600a4d29842162dbb34f137bc9847` - ranked-equipment
- `8414ed2e6fe600a4d29842162dbb34f137bc9847` - L1100-map
- `8414ed2e6fe600a4d29842162dbb34f137bc9847` - L1101-source
- `8414ed2e6fe600a4d29842162dbb34f137bc9847` - L1102-source
- `8414ed2e6fe600a4d29842162dbb34f137bc9847` - L1103-source
- `8414ed2e6fe600a4d29842162dbb34f137bc9847` - L1104-audit
<!-- gunfight-mechanics:end -->

<!-- soldier-frontier:start -->
## Current soldier frontier run (1 October 2026)

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-10-01T001825-0400-soldier-frontier/`, L840–L867, 1.4.3.5 / Head 4909002. Controlled source frontier exhausted: no unvisited in-scope target with an available exact current body and passing control remains. Native mechanics are partly unresolved. [Soldier findings](../frosty/SOLDIER.md).

Final core atlas: 132 inspected owners, 1,899 typed families, 25,243 numeric observations and 36,622 physical reads; four initial UI owners give 136 core/UI owners. Selected presentation supplements have separate counts. All 32 class slots and 28 Ability targets have exact source dispositions. All 14 captured-only body gaps closed. The 34 mechanic groups are 8 modeled, 8 traced not on site and 18 known limits. The immutable initial atlas (29 owners/423 families/155 UI rows) and intermediate snapshots remain unchanged. L866 holds the final versioned atlas and second compact dead-end batch.

Top unknowns: compiled movement/state equations; regeneration units, sentinel/stacking/reset behavior; revive/fall timing; numeric perk roles and Evasion/Heavy Flak UI identity; native detection/flinch; MP armor gates and mode assignments. Three exact OverlayPicker file GUIDs remain catalog index limits. Each dead-end entry states what would reopen it. Six proposals in the table have concrete validation predictions; no implementation is authorized by this research run. Season 5 training changes are stated for BR; shared MP source overlap remains a recheck risk.

Finished leads are locally committed through a separate index with own paths/hunks only. Commit ids, checks and cleanup are in the run handoff. Shared generated snapshots were validated without writing site mirrors. No site edits, recordings or push.
<!-- soldier-frontier:end -->

## Current class-trait run (30 September 2026)

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T2021-0400-class-traits/`, L404-L405, on 1.4.3.5 / Head 4909002. [Findings](../frosty/WEAPONS.md#class-path-and-perk-source-cross-check): L405 establishes FasterRegen source field-role associations (rate/delay/amount 30/2.5/0 against 10/5/0). Native composition and the UI 1.5x comparison remain conditional. L404 did not establish an end-to-end activation control; no activation worker was launched. Agile Shooter, Evasion Training and Heavy Flak were skipped without qualified route/control pairs. Reopen only with an exact selection consumer or a named same-owner operand control. Earlier L400-L403 raw evidence carries forward by hash with original Heads retained. Proposed implementation still awaits the operator; the L108 deferral remains in force. No site implementation or in-game tests were included. Handoff, verification and cleanup are in the run folder. Local source commit: `dc7aa6c`; site evidence index: `b4e6074`. The handoff also records the research index commit.

Independent sample check (1 October): [L520 receipt](../../reference-data/provenance/frosty-2026-10-01-L520-weapons-sample-check.json), L520-L528, seed `20261001520`. Workers reread **1,172 current raw values** across all 74 displayed numeric field families and eight weapon classes, with two weapons per class/family where available (ten sparse exceptions). Parent join: **1,129 matches, 43 L107 precision-only differences, zero intentional deviations in the sample and zero mismatches**. The L500 review base is confirmed by sample, not by full re-extraction; no follow-up family or site change is required. Extraction leads were committed promptly through separate indexes. Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-10-01T0001-0400-weapons-sample-check/`.

## Current site audit run (attachments)

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T2100-0400-site-audit-attachments/`.
Build: **1.4.3.5 / Head 4909002**, descriptor `4c28ad65...`. A01 records the mixed
site baseline. [Findings and family receipts](../frosty/ATTACHMENTS.md#current-site-value-audit-30-september1-october-2026).

The orchestrator census covered **113 numeric families / 7,578 leaves**, with
7,248 generator/prior-field exclusions and 251 retained no-source-field contracts
or observations. All **79 candidate leaves in 12 ranked families** are reconciled:
18 prior field matches, one new raw match, five precision-only reload aliases,
one intentional grip override, six inactive velocity fallbacks, one None cost
contract and 47 no-source-route leaves. `census.json` retains the original census;
`census-reconciled.json` records each current pointer, value, selection and disposition.

L540: all six offered AG Coating owner costs match **10 points**, offset 128 u32.
The 185KSK 5-point control passed first, worker review passed, and the parent raw
reread passed. Twelve family receipts are published. Earlier field receipts retain
their original Head; 90 reused raw bodies match current hashes. No new class (a)
proposal was found; the Proposed Analyzer changes table needs no new row. The five
class (b) cases follow L107 and receive no proposal. Class (c) observations retain
the reviewed bugs. Class (d) is a bounded no-route result with no lead or source-zero
claim. Existing four SP spotting candidates remain conditional L47/L49 evidence.

The ranked scope is closed. L541-L579 were not launched because no qualifying new
route remained after prior-work reconciliation. The operator removed the usage
stop condition. Handoff records local commit IDs and cleanup. No site data/simulation/UI
edit, generator rerun, underbarrel audit, in-game test or push was included.
Commits use a private index and an atomic ref update; the shared index is untouched.

Local commits: `8414ed2` (family receipts, findings and research indexes), `63e6ff6`
(site indexes), and `dc7aa6c` (original census). Cleanup found no links or delete
candidates; all evidence was kept. The final documentation commit is in the handoff.

<!-- attachments-sample-check-2026-10-01:begin -->
Independent sample check (1 October): [L541 receipt](../../reference-data/provenance/frosty-2026-10-01-L541-attachments-sample-check.json), L541-L552, seed `20261001541`.
The sample covers 1,100 leaves in 109 slot/field strata: **456 matches, 66 L107
precision-only differences, 564 documented deviation or model/default cases,
14 unresolved leaves and zero new proven mismatches**. Model/default cases are
not newly measured native scalars. The separate 47-leaf residual pass found five
exact routes (weapon overrides or excluded deployed-bipod state); 42 still lack
a qualified scalar route. No new proposal, family escalation or site edit was
required. L553-L560 are unused. Generated indexes were not rebuilt. Slot evidence
was committed through private indexes. Run handoff and cleanup: `BF6 Datamining/reports/weapon-analyzer-research/2026-10-01T1918-0400-attachments-sample-check/`.
<!-- attachments-sample-check-2026-10-01:end -->



## Current site audit run (30 September 2026)

Weapons audit: `BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T2322-0400-site-audit-weapons/`, reserved L500–L539, on 1.4.3.5 / Head 4909002. [L500 receipt](../../reference-data/provenance/frosty-2026-09-30-L500-weapons-audit-census.json). The orchestrator completed the census without workers: 84 numeric field families and 5,416 values across 63 weapons. A01 is recorded; source labels alone were not used as verification. The census remains outside Git.

No family remains after the requested exclusions. Existing field-level reviews cover the displayed values; all 169 relevant GS/WB/base-projectile raw assets carry forward by hash with their original Head retained. All 34 numeric changes since the 23 September ledger have later evidence: 32 applied L107 precision edits and two reviewed burst-cadence values. Nine numeric provenance families and unused `reloadSpeed` do not supply displayed values. ADS/deploy/sprint base indices are in `balance_tables.json`, outside this file audit. No Stage 2 worker or new per-family extraction receipt was needed. Existing receipts are retained, including the 13 September damage review, the M45A1 in-game step, L107 precision decisions and L123 reload totals. No new class (a) proposal; the Proposed Analyzer changes table needs no new row. This is a reuse and exclusion result, not a new measurement of every value or proof of native runtime behavior.

The weapons run is closed. Attachments (L540–L579), ammo (L580–L599) and fire modes (L600 upward) remain separate sessions. No capture, site data/simulation/UI edit, generator rerun, in-game test or push was included. Run handoff and cleanup receipts are in the run folder. Local commits: `dc7aa6c` (receipt), `b4e6074` (site index). A concurrent commit, `dc7aa6c`, included this run's already-staged documentation and research index hunks; its history was preserved.


## Current site audit run (ammo)

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T232233-0400-site-audit-ammo/`.
Build: **1.4.3.5 / Head 4909002**, descriptor `4c28ad65...`. L580-L590 used;
L591-L599 unused. A01 applies: the site baseline has mixed source versions and
reviewed evidence. Stage 1 was completed by the orchestrator without workers;
`census.json` ranks seven families across 63 weapons, 15 ammo types and 328 choices.
The operator removed the usage stop condition. The audit is now closed because
all ranked families are compared or have a stated route/consumer limit.

Eleven extraction leads returned and were reviewed. [Weapon findings](../frosty/WEAPONS.md#current-ammo-site-value-audit-30-september-2026)
and [modifier findings](../frosty/ATTACHMENTS.md#current-ammo-modifier-and-point-audit-1-october-2026)
link one current receipt per family. Curves: 328 comparisons, 20 exact,
293 precision-only rows and 15 reviewed deviations. Pellets: 16/16 exact.
Velocity: 31 precision-only comparisons; no proposal. Recoil/spread:
186 selected operand comparisons match over 74 stored leaves.
Type modifiers: 120 exact selected operand comparisons and 31 precision-only
spotting comparisons. Points: 328/328 exact, with decoder ambiguity retained.
All 77 per-class collateral leaves are inactive fallbacks.

L589-L590 completed the current selected modifier graph for all 328 choices.
The previously partial Frangible/spotting joins and Flechette +2 are resolved.
137 choices have bounded configured absence of the named modeled owners;
no native runtime zero is inferred. The single missing Blacklight import was
captured under the shared lock on Head 4909002; one route succeeded, none failed,
and build manifest verification found no changed or missing files.

Remaining source limits: Slugs ADS increment 0.05 and current game defaults/menu
availability have no qualified source receiver/control; no new lead.
Native activation/composition remains unresolved. Earlier receipts retain their
original Head; matching current raw hashes support carry-forward. L107 precision
and reviewed panel/runtime differences do not become proposals. There is **no
new class (a) mismatch**, so the Proposed Analyzer changes table has no new row.
Displayed damage, BTK and TTK therefore remain unchanged.

Local first-pass commits: research `dc7aa6c`, site evidence `b4e6074`, and
close-out `dc7aa6c`. Continuation commit IDs are in the run's `handoff.md`.
All continuation commits use a private index and an atomic ref update; the shared
index is untouched. No site data, simulation or UI edits, site generator reruns,
underbarrel work, in-game tests or pushes were performed.

## Current fire-modes run (30 September 2026)

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T2323-0400-fire-modes/`, L600-L604, on 1.4.3.5 / Head 4909002. All 63 weapons are covered in `fire-modes.json`: 110 source mode rows and 12 mode-changing branches, including 10 site choices. All controls and worker reviews passed. The four XML-missing modifier imports were resolved from existing raw; no capture was needed. Generic unmatched graph joins remain explicit and do not supply runtime negatives. Count predictions, named toggle validation and conditional L63/L17 effects are in the proposal row and [findings](../frosty/WEAPONS.md#fire-mode-selector-source-data-1435-l600-l604). No site implementation or in-game tests were included. Local source commit: `dc7aa6c`; site evidence index: `b4e6074`. The run handoff records verification, limits and cleanup. No push. **L604 rechecked on 2.1.1.0 (19 Oct): mode lists and rates unchanged on all 63 weapons, the 12 branch files byte-identical; SGX and L110 lost the `CMU_SemiAuto` import (L4054).**

## Current site audit run (tables)

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T2359-0400-site-audit-tables/`, reserved L700-L739. Build: 1.4.3.5 / Head 4909002. [L700 census](../../reference-data/provenance/frosty-2026-10-01-L700-tables-audit-census.json), [findings](../frosty/SITE_AUDIT_TABLES.md). A01 applies: the site baseline has dated source, panel and game observations. Stage 1 was completed by the orchestrator without workers. The four CUR files have 69 numeric or Boolean families and 35,832 numeric leaves. Existing field-level reviews exclude all their families; three changed Precision RPM leaves are accepted L107 edits. Ordered ladders, hip/recoil base maps and geometric factors have matching current raw hashes. L125 resolves the later ADS ladder numeric comparison. Intentional reload observations, integer overrides and the two Mobility grip interpretations remain reviewed deviations. Legacy recoil maps have no displayed reader.

Stage 2 completed three GEN input raw-hash checks: L701 ballistics, L702 hit zones and L703 tooltips. Seven recorded Killswitch hashes differ; three graph raw routes are absent for ballistics/hit zones, seven for tooltips. No displayed-value mismatch or new class (a) proposal is established. ADS/deploy/sprint base coordinates are in attachments.json and belong to its separate audit. No capture, generator rerun, site data/sim/UI edit, in-game test or push was run. Census and resumable progress remain in the external run folder.

L701: [receipt](../../reference-data/provenance/frosty-2026-10-01-L701-ballistics-input-hashes.json). 4276/4286 recorded raw inputs equal 1.4.3.5; seven Killswitch hashes differ and 3 historical hashes are unavailable. No displayed-value proposal. Worker control, fixed scope and parent hash reread passed. No new Proposed Analyzer changes row.

L702: [receipt](../../reference-data/provenance/frosty-2026-10-01-L702-hit-zones-input-hashes.json). 4278/4288 recorded raw inputs equal 1.4.3.5; seven Killswitch hashes differ and 3 historical hashes are unavailable. No displayed-value proposal. Both original grid streams match; descriptor raw hashes differ. Worker control, fixed scope and parent hash reread passed. No new Proposed Analyzer changes row.

L703: [receipt](../../reference-data/provenance/frosty-2026-10-01-L703-tooltips-input-hashes.json). 7614/7628 recorded raw inputs equal 1.4.3.5; seven Killswitch hashes differ and 7 historical hashes are unavailable. No displayed-value proposal. Localization TSV differs; all 1067 supplemental AAM/descriptor raw inputs match. Worker control, fixed scope and parent hash reread passed. No new Proposed Analyzer changes row.

L704: [used tooltip text receipt](../../reference-data/provenance/frosty-2026-10-01-L704-used-tooltip-text.json). All 413 localization IDs used by attachment-tooltips.json have identical old/current text; zero changed or missing IDs. The 18 screenshot override keys are not localization IDs. Exact used-ID comparison resolves the text question raised by L703's global TSV hash difference. No likely stale tooltip text or new proposal was found.

The tables run is closed. L700-L704 are complete; L705-L739 are unused. Three workers returned, all controls and fixed-scope reviews passed; L704 was completed by the orchestrator. No class (a) mismatch or new proposal is supported. One current blacklight raw was reused from the concurrent ammo run; seven original input raw hashes remain unavailable. No capture or generator rerun was started. All seven data files retain their run-start hashes. `census-final.json`, handoff and cleanup receipts are in the run folder. Each finished lead was committed through a separate index; no push. Local commits: L700 `8414ed2` research / `63e6ff6` site, L701 `8414ed2` research / `63e6ff6` site, L702 `8414ed2` research / `63e6ff6` site, L703 `8414ed2` research / `63e6ff6` site, L704 `8414ed2` research / `63e6ff6` site.

## Prior weapon source frontier run (1 October 2026)

Build 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. Leads L780-L839. The source-route pass is complete. [L829](../../reference-data/provenance/frosty-2026-10-01-L829-late-context-actual-joins.json) has completed actual site, prior-receipt and September 30 census joins for all 481 added contexts. The full requirement audit passed. The run is closed: the available source frontier is exhausted, with native behavior limits retained. L828 audited all 133 ranked identities and their 347 exact source contexts; every remaining source route has a stated control, consumer or native-meaning gap. All 63 site weapons and all seven requested owner groups are covered. [L819](../../reference-data/provenance/frosty-2026-10-01-L819-current-weapon-field-atlas.json) publishes the [current atlas](../../reference-data/frosty/weapon-frontier/field-atlas.json): 5,351 field identities, 12,168 contexts and 458 declaring class hashes. This includes 5,212 real fields and 139 structural markers. The baseline and lossless source archive are preserved.

| Requested owner group | Distinct families | Source contexts |
|---|---:|---:|
| WB | 1,326 | 2,585 |
| GS | 610 | 1,144 |
| projectile | 170 | 170 |
| attachment/modifier | 1,289 | 2,175 |
| ammo | 49 | 55 |
| optic | 749 | 1,574 |
| weapon-balance | 1,268 | 1,269 |

Groups retain exact source scopes and may overlap. Registry, Ability, wrappers and extra linked owners remain separate graph contexts. [All owner group counts](../../reference-data/frosty/weapon-frontier/user-group-and-class-counts.json), [all 458 current class family counts](../../reference-data/frosty/weapon-frontier/current-declaring-class-counts.json) and [current context classifications by class](../../reference-data/frosty/weapon-frontier/final-current-counts.json) retain the complete census. The largest declaring classes are below; counts include structural markers.

| Declaring class hash | Families |
|---|---:|
| `b1f8b400` | 630 |
| `cb53a662` | 342 |
| `9bc51bd0` | 166 |
| `b216dfe5` | 90 |
| `45468e55` | 77 |
| `a6120457` | 72 |
| `4a238d8d` | 72 |
| `3ee1d169` | 72 |
| `bcfafb0d` | 68 |
| `0d3ca2f4` | 61 |
| `3205ef37` | 61 |
| `26e24b34` | 60 |
| `0fffd6b1` | 59 |
| `4e834289` | 59 |
| `ed5bf24c` | 57 |
| `7cb2b703` | 56 |

There are 11,895 known-limit, 166 modeled and 165 traced-not-site context memberships; 49 contexts have overlapping labels. No typed context remains never examined in the bounded inventory. L810 corrects 299 actual scalar variation summaries, including 298 all-63 weapon summaries. Source profiles and occurrence counts do not establish selected weapon values.

The [current ranked frontier](../../reference-data/frosty/weapon-frontier/current-ranked-frontier-draft.json) retains 133 source candidates. [L828](../../reference-data/provenance/frosty-2026-10-01-L828-ranked-source-route-audit.json) resolves their actual proof links, attempts and positive target routes. No unchased qualified source target remains. The [current join index](../../reference-data/frosty/weapon-frontier/current-join-disposition-index.json) binds exact site/prior/census evidence for the original 11,687 contexts. The [L829 late join index](../../reference-data/frosty/weapon-frontier/late-context-join-index-L829.json) adds actual attempts and precise bridge limits for the 481 added contexts. All 12,168 atlas contexts have join evidence; baseline joins are not transferred. W1-W9 and O1-O3 remain known gaps, not the exploration boundary.

Top remaining unknowns are native optical composition and selected FOV/PiP precedence; zeroing enum meanings and the firing receiver; compiled breath/NVG graph grammar; AtlasTexture and MeshSet current semantic controls; and weapon firing, recoil, movement and handling activation or units. [where-not-to-look.json](../../reference-data/frosty/weapon-frontier/where-not-to-look.json) retains 9,322 compact limits, with exact attempts and reopen conditions. Known limits do not establish no effect. No new numeric comparison meets the meaning, displayed-effect and validation-prediction rule. Existing conditional and qualitative proposals remain applicable.

Controls precede findings. Consequential operands and parent samples pass raw checks. Eleven captures use the shared lock. The current build manifest verifies 27,251 files, with zero new, changed or missing files. Private-index commits preserve parallel work. No site edits, recordings or push.

## Active source leads

Only open leads are listed here. Closed leads, past run blocks and applied proposals are in
[FROSTY_QUEUE_CLOSED.md](../archive/FROSTY_QUEUE_CLOSED.md); search them with
`python scripts/frosty-worker.py prior-work --terms ...` rather than reading the archive.
When a run closes a lead, delete its row here; `frosty-records.py build` adds it to the
archive's generated Closed leads table from its record.

Work these from source before handing them to the capture plan. The capture plan was rescoped on 28 September; "capture rank N" in older rows refers to the previous plan and most of those captures were [removed](BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026). Results from the
23 September pass are in the [receipt](../../reference-data/provenance/frosty-source-leads-2026-09-23.json). Each row says what is established and what is next.

| # | Lead | Established | Next source step |
|---|---|---|---|
| L4064 | **Standing grip-pod recoil ratio - measured 0.80 against predicted 0.890 (23 Oct)** | The M277 deployed-recoil measurement ([receipt](../../reference-data/provenance/frosty-2026-10-23-deployed-recoil.json)) reproduces the deployed bipod and grip-pod ratios within the clip spread, but a fitted, undeployed grip pod reads 0.80 of the no-grip climb against 0.890 from the +2 tiers (`0.9433^2`); the site applies +2. | Check whether a standing grip pod binds a further operand (the L61 `Field_b574fa40` dispersion steps do not apply when merely fitted; look for a recoil counterpart in the PTT, QD and Classic grip-pod packages and `GRM_Grippod*`), then re-measure on a second weapon before any site change. |

## Proposed Analyzer changes

These proposals come from completed source work. They need product review and
operator approval; none is implemented unless stated.

| Proposal | Affected data/code | Evidence and remaining validation |
|---|---|---|
| **Hold until released: DD Vertical grip (Season 5, U44)** | `data/attachments.json` GRIPS (new id) and the grip lists of 49 weapons | Source: GS `GRM_Recoil_BTM_P30` (+3 amount exponent, both aim branches) and WB `WME_DynamicPivot_M10`; no moving-ADS or ADS-move effect; cost 30. By the vertical-grip family mapping: ADS recoil 3, hip recoil 3, moving ADS 0. Not in the game at 2.1.1.0 (kill switch `KST_CH2_S1_Weapons`, later Season 5 phase); add when it appears, and read the display name from the loadout screen then. [Working note](SEASON5_ATTACHMENTS_2026-10-19.md). |
| **Hold until released: FML 1.00x thermal on seven sidearms (Season 5, U44)** | `data/attachments.json` SIGHTS and the sidearm sight lists; `optic_category` rule in `scripts/frosty-attachment-tooltips.py` | 1.00x thermal (ES 5.7, GGH-22, P18, M45A1, M44, vz. 61, M357 Trait), 25 points. Unlike every rifle thermal it does not import `WME_ADSMoveSpeed_M05`, so the Thermal category's ADS-move shift must not apply to it. Not in the game at 2.1.1.0 (same kill switch, later Season 5 phase); add when it appears. [Working note](SEASON5_ATTACHMENTS_2026-10-19.md). |
| **ELR-40 custom zeroing without the FN Elity (operator report, 19 Oct)** | Game-bugs document candidate; no site data | `CDX40_WB` zeroing block CustomZeroing (`Field_4449ee55`, now named from the registry hash pairing) true, the only weapon; registry row agrees. The FN Elity package sets RangeFinder and CustomZeroing; the ELR-40 has the second built in. Not in the game's text. [Working note](SEASON5_ATTACHMENTS_2026-10-19.md). |
| **Soldier frontier (L861): Holster setting** | Add the existing resolved `_undeployTimeMs` setting to loadout comparison. | L849: M433 default 30 Rnd model rounds to 200 ms; 20 Rnd rounds to 167 ms. Existing model/formatter check predicts ADS 0.75×, sprint 133 ms and deploy 467 ms for 20 Rnd. Re-run that exact model/formatter check before implementation. This is a handling setting; total swap/readiness remains unresolved. |
| **Soldier frontier (L861): Quicker Recovery description — parked, research only (operator, 1 Oct; the site has no class/perk surface)** | Show the Frontliner perk's stated recovery benefit. | [EA Assault guide](https://www.ea.com/games/battlefield/battlefield-6/news/assault-class): passive healing starts sooner and recovers faster. Validation prediction: the guide's Frontliner level 2 states both effects. L846 has source role settings 30/2.5/0 versus baseline 10/5/0; native units/composition remain unresolved, so display qualitative guide text. |
| **Soldier frontier (L861): Soft Landing description — parked, research only (operator, 1 Oct; the site has no class/perk surface)** | Show reduced falling/jumping impact for the Frontliner perk. | [EA Assault guide](https://www.ea.com/games/battlefield/battlefield-6/news/assault-class): reduced impact. Validation prediction: Frontliner level 1 states falling and jumping. L850/L854 trace Featherweight source selection and CT addresses; they do not establish damage thresholds or exact UI identity. Confirm the current UI selection before binding this guide description. |
| **Soldier frontier (L861): Revive Recovery description — parked, research only (operator, 1 Oct; the site has no class/perk surface)** | Show healing during revival and the incoming-damage interruption condition. | [EA Support guide](https://www.ea.com/games/battlefield/battlefield-6/news/support-class): Combat Medic level 1 gives both conditions. Validation prediction: the guide retains the heal-during-revive and damage-interruption clauses. L857/L860 retain exact ReviveHealthRegen source selection; no heal rate or duration is qualified. Confirm current UI selection before binding. |
| **Soldier frontier (L861): Explosives Resistant description — parked, research only (operator, 1 Oct; the site has no class/perk surface)** | Show the guide-stated 25% splash reduction while prone or mounted. | [EA Support guide](https://www.ea.com/games/battlefield/battlefield-6/news/support-class): Fire Support level 1. Validation prediction: the guide states 25% and both stance conditions. L847/L852 trace current StanceFlak source0.75, whose numeric role remains unresolved. Verify current UI identity; do not treat the raw0.75 as an independent damage-role proof. |
| **Soldier frontier (L861): Low Profile description — parked, research only (operator, 1 Oct; the site has no class/perk surface)** | Show the stated prone benefit: leave combat sooner and remain spotted for less time. | [EA Recon guide](https://www.ea.com/games/battlefield/battlefield-6/news/recon-class): Spec Ops level 2. Validation prediction: both benefits are conditional on prone. L856 traces exact LowProfile spotting and regen receivers; sentinel/operation roles prevent a numeric timer display. Confirm current UI selection before binding. |
| **L740: Interdictor peak-range description** | `data/weapons.json` description | [Receipt](../../reference-data/provenance/frosty-2026-10-01-L740-interdictor-range-description.json): current raw/site curve and EA 1.4.3.0 agree on 120–160 m; the site and game description said 120–150 m. Control and 20 operands passed. **Implemented 1 Oct** in site commit `4200945`: the operator chose the game data, so the description now ends at 160 m. The curve is unchanged (100 damage through 160 m). |
| **Operator review: class weapon traits (L100–L104; L400–L403; L4070 re-read on 2.1.1.0, 30 Oct: on-class and off-class values for 41 of 67 weapons, validation glance M433 Sprint Recovery on Assault vs Support, [receipt](../../reference-data/provenance/frosty-2026-10-30-L4070-class-trait-chip-proposal.json))** | New "class trait" toggle (off by default); `data/` trait table; `sim/applyAttachments.js` ADS, hip-spread and draw/sprint indices | Sourced for Assault/Support/Engineer on exactly the site weapons of each class; matches EA's class guide. Conditional values in the [receipt](../../reference-data/provenance/frosty-2026-09-28-L100-L104-class-traits.json): AR deploy 633 → 533 ms and sprint recovery 200 → 167 ms; LMG ADS one step faster; SMG hip minimum 1.804° → 1.352°. Recon: sniper sway ×2.25 without the trait, ×1.0 with it (the site's current value; operator confirms non-Recon sway is higher), plus the Recon rechamber block (e.g. Mini Scout 47.1 → 51.4 RPM; [timing receipt](../../reference-data/provenance/frosty-site-timing-2026-09-23.json)). Activation is class + signature weapon per EA; native composition unverified. Extension: [L400-L403](../frosty/WEAPONS.md#class-path-and-perk-source-cross-check) source perk text and spotting 1.33/1.10/+3 s; WeaponSwap +1 and MountedPlus +3/-2 are hotfix-verified, with L108 deferral retained. Perk metadata would use a new `data/` trait table and `ui/app.js`; numeric composition stays conditional. Validation predicts exact text equality first, then matched active/inactive range/angle/duration and handling changes. Recovery source 30/2.5 versus baseline 10/5 is a conditional text discrepancy, not a verified gameplay defect. Class/path/unlock and UI-to-source identity limits remain explicit. |
| **Operator review: ADS-out time per weapon (L114; L4067 re-read on 2.1.1.0, 30 Oct: 67 of 67 indices, Season 5 included, no attachment shift found, validation recording M4A1 200 ms vs M240L 333 ms, [receipt](../../reference-data/provenance/frosty-2026-10-30-L4067-ads-out-2110-proposal.json))** | New per-weapon ADS-out time in `data/` (with a UI stat); the sustained fully-ADS sniper cadence model | Sourced conditionally: all 63 weapon bodies select an `FZT_Weapons` `General_10` tier through the same `WeaponZoomTransitionIndex` as the site ADS-in index (`defAds` matches 63/63), giving 400/333.334/266.667/233.334/200/166.667/133.334/100 ms by index (e.g. 233.334 ms at index 3, the M4A1's 4 gives 200 ms). General_10 differs from General_01 at every index; the paired General_01 values match the site's ADS-in ladder within 1.2e-5 ms, supporting candidate transition roles ([L125](../../reference-data/provenance/frosty-2026-09-29-L125-fzt-general01-ads-in.json)). Whether the selector drives ADS-out, and whether ADS-time attachments shift it (no traced modifier references FZT directly and the receiving field of their steps is unnamed, [L121](../../reference-data/provenance/frosty-2026-09-29-L121-ads-time-modifier-targets.json)), is unresolved; do not apply ADS-in shifts to ADS-out. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L114-ads-out-transition.json). |
| **Movement speed in m/s (L4075, 30 Oct)** | Mobility card row beside Strafe Spd; `data/balance_tables.json` soldier movement constants | Walk 3.5 m/s, sprint 6.05, LMG sprint 5.7475 (x0.95 on the 11 LMGs), firing walk 2.8 (x0.8), ADS walk 3.5 x the shown ADS-move ratio (composition assumed). Sourced on 2.1.1.0 from `Glacier_Soldier`; validation a timed 50 m sprint (8.26 s; 8.70 s with an LMG) and walk (14.29 s). [Receipt](../../reference-data/provenance/frosty-2026-10-30-L4075-movement-speed-ms-proposal.json). |
| **Operator review: stance-change spread penalty (L120; L4069, 30 Oct)** | Optional per-weapon stance-change context beside the static spread minima in `data/`, `sim/core.js` spread and the stance control (see the crouch/prone posture row) | Sourced, activation unresolved: every weapon body stores `StanceChangePenalties` (Zoomed/Unzoomed x six stance transitions x `MinAngleOffset` degrees and `Duration` seconds; 1,512 raw reads over 63 weapons): prone transitions are 6 degrees over 0.9 s on 54 weapons, with class outliers, and the crouch/stand leaves are 0.2-1 degree over 0.3 s (all 24 slot joins exact, L124). No site choice or verified modifier targets them. If a capture confirms a transient spread floor after changing stance, show angle and duration beside the static minima; do not add them to spread until composition is known. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L120-stance-change-penalties.json). |
| **Deferred (operator, 28 Sep): mounted-state recoil (L108)** | New "mounted / MountedPlus" state toggle (off by default); `data/` state table; `sim/applyAttachments.js` recoil tiers | Source adds exponent +3/-2 for MountedPlus on all 63 weapons (amount x0.800-0.855, variation x1.161-1.223, conditional), and +10/-4 (amount x0.475-0.594) or +30/-5 (Bolt bipod, amount x0.107-0.209) when a bipod is deployed. The operator decided on 13 September to document mounted/bipod recoil without model changes; the MountedPlus operands were not known then. Activation, composition and the Vertical/Horizontal flags are unresolved. [Receipt](../../reference-data/provenance/frosty-2026-09-28-L106-L111-orchestrator-trial.json). **Measured 23 Oct** ([WEAPONS.md](../frosty/WEAPONS.md#mounted-and-deployed-recoil-2110-23-october-2026)): M277 deployed climb ratio 0.52 to 0.53 against predicted 0.558 (+10, bipod and grip pods alike); PSR settled ratio 0.163 against 0.156 (+30); mounting without a bipod gives no reduction; grip pod deployed recoil operand is +8 (`GRM_GrippodDeployed_BTM_P30`). The amount ladder composes natively; the variation sign is open (PSR horizontal spread fell when deployed). **Implemented 23 Oct** as the Mounted stance (Analyzer `data/attachments.json` grip `deployed` blocks, `sim/applyAttachments.js` `applyDeployedState`): tiers +10 / +8 / +30 (bolt), ADS bloom × 1/3, hip −2 steps, per-weapon exceptions; variation tiers not applied. |
| **Deferred (operator, 28 Sep): reserve rounds and chambered round (L110; L4068 re-read on 2.1.1.0, 30 Oct: 302 of 303 magazine choices, card line "20+1 / 189", one spawn-HUD glance decides reading A or B, [receipt](../../reference-data/provenance/frosty-2026-10-30-L4068-reserve-rounds-2110-proposal.json))** | `data/attachments.json` WEAPON_MAG, `data/weapons.json`; loadout stat row; `sim/core.js` mag-dump length | (1) Show carried rounds per magazine choice (capacity x `NumberOfMagazines`, e.g. M4A1 20 Rnd 210, 36 Rnd 222, 40 Rnd 246). (2) Treat the source +1 as a chambered round on tactical reloads for closed-bolt weapons (nominal for belt LMGs and revolvers). Runtime meaning of both is unresolved; the operator can confirm from the in-game HUD without a capture. [Receipt](../../reference-data/provenance/frosty-2026-09-28-L106-L111-orchestrator-trial.json). |
| **Operator review: RPK-74M empty reload (L105)** | `data/weapons.json` rpk74m `emptyRld` | 3.100 → 3.184 s if PostReloadDelay counts as the shotgun formula counts it. [Receipt](../../reference-data/provenance/frosty-2026-09-28-L105-reload-delays.json). Low value; a reload capture would settle it. |
| Optional underbarrel secondary profiles (L71/L75/L76/L76B/L78) | `data/attachments.json`; `sim/attachments.js`, `sim/damage.js`, `sim/ballistics.js` | **Operator review: optional feature only.** The current model has no underbarrel selector; primary damage uses the weapon curve and pellet count, and projectile overrides use the base weapon/ammo. L71/L75/L76/L78 source values do not establish underbarrel runtime behavior or show a defect in primary values. L76B gives a conditional capture-feasibility calculation, not a measurement. L78 records thermobaric Explosion fields but does not establish value precedence or runtime behavior. Consider a separate profile only after firing and owner semantics are established. [L71](../../reference-data/provenance/frosty-2026-09-26-L71-m320-he-at-source-profile.json); [L75](../../reference-data/provenance/frosty-2026-09-26-L75-m320-explosion-naming-limit.json); [L76](../../reference-data/provenance/frosty-2026-09-26-L76-m320-he-firing-inputs.json); [L76B](../../reference-data/provenance/frosty-2026-09-26-L76B-m320-he-capture-feasibility.json); [L78](../../reference-data/provenance/frosty-2026-09-26-L78-m320tb-explosion-profile.json). Parent code review: `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-09-26-astra\astra-underbarrel-site-review.json` (SHA-256 `330ba41287d436932254ad3fbf8d00d01b8f27948a263799d78bd240a9f5ea5a`). No numeric implementation proposed. |
| VSSM semi-auto hip bloom (L63) | `data/weapons.json` vssm `spreadDyn.hip.inc`, or a semi-mode rule in `sim/applyAttachments.js` | **Rejected by capture 25 September:** the bare VSSM hip reticle widens 68 → 121 px over 10 shots, so the semi condition is not active in its default mode; keep 0.398. The bare M433 in manually selected semi shows no bloom, so the condition does act after a mode switch, which matters for any future selectable single-fire mode (L14) on the 39 other bound weapons. [Source](../../reference-data/provenance/frosty-2026-09-25-L63-vssm-semi-bloom.json); [capture](../../reference-data/provenance/frosty-2026-09-25-L63-L17-semi-bloom-captures.json). |
| **Operator review: source caliber wording (L54/L55)** | `data/weapons.json` caliber metadata | Exact text supplies vz. 61 `.32 ACP`, M39 `7.62x51mm`, SVK `8.6x70mm`, and Interdictor `10.4x83mm`. These are wording options, not proof that stored aliases are wrong; no current direct consumer was found in L50. |
| **Operator review: M87A1 caliber metadata** | `data/weapons.json` M87A1 `cal` | L50 supports removing fixed `(00 Buck)` from the stored label; selectable #01/#00 names are distinct. No direct current consumer found; remaining gauge text and other weapons need separate source support. |
| Neutral shooting decay field (L15; lead rejected, field cleanup only) - operator review | `data/weapons.json` `recoil.{ads,hip}.shootingDecScale`; `sim/core.js` | All 126 stored values are 1 and core has no reader, consistent with [L15](../../reference-data/provenance/frosty-2026-09-24-L15-neutral-shooting-recoil-scale.json). Either remove the unused field or retain it as documented-neutral; no numeric change proposed and no site edit made. |
| Non-polar cleanup check (L33; lead rejected, code cleanup only) - operator review | `data/`, `sim/`, `ui/`; `sim/core.js:genRecoilPts` | No polar/non-polar flag or alternate branch found by scoped search and recoil-path inspection; core already resolves direction/magnitude through sine/cosine. [L33](../../reference-data/provenance/frosty-2026-09-24-L33-polar-recoil-build-separated.json) supports no current outlier, but does not prove the native equation; no removable site branch identified or changed. |
| Source hit capsules for target zones (L99) | `sim/target.js` zone partitions and alpha mask; `ui/target-stats.js` | **Closed: head zone applied, torso proposal withdrawn (L99 site-fixed; notes at the end of this row).** Proposed: replace the artwork partitions with the source capsule front view: larger head, and abdomen (limb multiplier) up to about 136-148 cm on the centre line. Chest 1.0 is now sourced (material 115). [Evidence](../../reference-data/provenance/frosty-2026-09-27-L99-soldier-hit-capsules.json). Arms need an in-game pose. **L4010 (10 Oct): operator video, M433 at 5 m against bots - mid-chest and upper-chest hits do 26, belly and limbs 22, head 36. The rest-pose capsule prediction for the chest aim point is not supported; the site's chest zone is kept and this proposal is withdrawn.** **Head zone implemented 10 Oct (site commits `99ed8f6`, `c54b33f`, on origin/main), approved and placed by the operator: the stored head capsule (radius 14 cm, length 6 cm) from 147.25 to 181.25 cm on the unchanged artwork, counted where it overhangs the figure (L4011). Torso zones unchanged.** |
| Crouch/prone spread posture (L69; L4069 re-read on 2.1.1.0, 30 Oct: posture minima and stance-change leaves on 67 of 67, proposal with the drop-prone glance, [receipt](../../reference-data/provenance/frosty-2026-10-30-L4069-stance-penalty-posture-2110-proposal.json)) | `ui/app.js` stance control; `sim/core.js` `spreadBounds`; per-weapon spread inputs | **Operator review: optional posture dimension.** The selected source rows contain crouch/prone minima outside the current standing/moving choice for M433, M39 EMR and DB-12. Keep current standing values. Posture labels use the named Sym crosswalk; native activation, composition, posture maxima and stationary ADS inputs remain unresolved. Needs operator review and native state evidence before implementation. [Evidence](../../reference-data/provenance/frosty-2026-09-26-L69-posture-spread.json). |
| Projectile lifetime and reachability (L22; L4074, 30 Oct: no site ammo selection reaches less than its damage curve, no lifetime note needed) | `data/ballistics.json` projectile fields; `sim/ballistics.js`; dependent travel/damage display | Current integration guard is not source lifetime. Selected buck/Slug TimeToLive 0.5/2.0 could affect reach within supported range. [Evidence](../../reference-data/provenance/frosty-2026-09-24-L22-projectile-lifetime.json). [L25](../../reference-data/provenance/frosty-2026-09-24-L25-selected-projectile-lifetimes.json) adds subsonic candidates using actual ammo velocity. Needs capture before implementation; show unreachable separately from conditional damage, do not assume zero damage. |
| Match Trigger in an explicit tested mode (L17) | `ERGOS[id=match_trigger]`, `sim/applyAttachments.js`, recoil/spread calculations | Current choice has no modeled effects. HK433 source selects amount-exponent +3, recovery operand 1.728 and bloom multiplier 0. Candidate M433 model predicts recoil ratio 0.843908625 and recovery factor 124.416 from current inputs; conditional only. [Evidence](../../reference-data/provenance/frosty-2026-09-24-L17-match-trigger-indirect-effects.json). [L24](../../reference-data/provenance/frosty-2026-09-24-L24-match-trigger-family.json) confirms shared source targets on all 24 selections, with differing priorities. L70 shows the existing M433 pair has insufficient capture observability; the conditional prediction remains open. [L70 capture limit](../../reference-data/provenance/frosty-2026-09-26-L70-match-trigger-capture-limit.json). Needs semi/auto capture and operator/activation validation; no blanket runtime change. |
| Controller vertical recovery (L19) | `ui/app.js` platform factor; `sim/core.js` `genRecoilPts` | Current factor changes amount only. Candidate separate vertical recovery control follows source 0.8836 multiplier; horizontal source operands are neutral. [Evidence](../../reference-data/provenance/frosty-2026-09-24-L19-controller-recovery-operand.json). Needs capture10/native equation before implementation; not a common decay-factor correction. |
| **Implemented fire-mode data, simulation and shares; selector UI hidden (L14, L600-L604)** | `data/weapons.json` per-weapon fire modes and rates; `sim/core.js` shot spacing; `sim/applyAttachments.js` mode selection | **Implementation present:** source-backed modes, cadence application and share-state handling landed in [ab5a0d2](https://github.com/raymdl/BF6-Weapon-Analyzer/commit/ab5a0d265b692a0960957c78c71c5f4a8e1af5c4). [7a23b8c](https://github.com/raymdl/BF6-Weapon-Analyzer/commit/7a23b8cc21a34872526662d6eea8636cf72f5571) hid the selector row pending UI placement while retaining that implementation. New loadouts use the weapon/loadout default unless a valid explicit mode is supplied. This status does not resolve conditional source effects or native-runtime assumptions. Data: `BF6 Datamining/reports/weapon-analyzer-research/2026-09-30T2323-0400-fire-modes/fire-modes.json`, 63 weapons / 110 source mode rows, full precision with paths, offsets, hashes and Head 4909002. [Per-weapon mode lists and selectable-mode count predictions](../frosty/WEAPONS.md#fire-mode-selector-source-data-1435-l600-l604): 26 weapons have one mode, 28 have two and nine have three across WB lists and site-offered mode choices; per-loadout counts can differ. Ten site mode branches and two source-only branches are retained; GRT-CPS burst is excluded from player prediction by the prior operator unavailable note. L63 semi no-bloom and L17 Match Trigger remain conditional. **Validation: confirmed by the operator on 1 October, all 11 match ([decision](../../reference-data/provenance/frosty-2026-10-01-decision-L604-toggle-check.json)):** M4A1 bare auto/single (2); M16A4 bare burst/single (2), A3 Receiver auto/single (2); KORD 6P67 Burst Training burst/auto/single (3); GRT-BC and SL9 Burst Mode burst/single (2); VSSM bare single (1), Folding Stock auto/single (2); GRT-CPS bare single (1); vz. 61 bare auto/single (2); M2010 ESR bare bolt single (1). [Receipt](../../reference-data/provenance/frosty-2026-09-30-L604-fire-mode-selector-data.json). |
| Model sustained fully-ADS bolt-rifle cadence | Sniper RPM, shot spacing, TTK | ADS-out (`Aout`) now has a conditional source (L114 row above). DLC Bolt and Mini Scout keep ADS through rechambering (L1); other snipers add ADS exit and entry. Separate next accepted shot from next fully-ADS shot. [Candidate table](../frosty/WEAPONS.md#ads-bolt-and-scoped-shot-cadence-23-september-2026). Overlap remains unresolved. Former capture rank 6 was removed ([operator removal decision, 28 September 2026](BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)); retain the exact readiness/overlap source question without a renewed recording request. |
| Generate per-weapon spot bases from WB (L4008 applied) | `sim/applyAttachments.js`, spotting display | M45A1 and Skorpion would differ from the current 54/150. Needs L7 source/application evidence. Former capture rank 1 was removed as unnecessary ([operator removal decision, 28 September 2026](BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)); this is not a renewed recording request. [Official 1.2.1.0 context](../../reference-data/provenance/frosty-spotting-patch-context-2026-09-23.json) corroborates 54 m and 21 m. **L4001 (10 Oct):** EA's 1.3.3.0 notes say the M45A1 and vz. 61 use subsonic ammunition by default; all 63 site weapon files were read and only these two differ from 54 / 150 (27 / 64.29). **L4008 (10 Oct):** the operator's stat-screen screenshots show 27 m / 64 m on every non-muzzle panel of the M45A1 (15) and vz. 61 (18), and 0 / 9 m suppressed (64.29 x 0.14, so the factors multiply); the P18 shows 54 / 150 and 0 / 21. Source, EA and the stat screen agree; no in-game test is needed and the L4001 test is withdrawn. **Approved by the operator and implemented 10 October 2026** (site commit `b6da447`, on origin/main): base 27 / 64.285713 for `m45a1` and `vz61`; existing attachment-effects test passes 37 of 37. |
| Test whether the idle-duration table controls ADS-entry spread timing | Not idle recovery in `sim/core.js` | The first eight values match the ADS ladder minus one 60 Hz frame; indices follow the ADS animation index on 62 of 64 weapons. Use the VSSM capture first. |
| Per-weapon deployed comparison using actual bipod operands | `sim/attachments.js`, `sim/core.js` | Deployment conditions and stacking unresolved; no mounted recoil reduction established. |
| Keep GS ADS tier and WB timing as separate coordinates | Handling data | Prevents VSSM double counting. |
| Exact optic identity and PiP/FOV context | Attachment/display data | Resolve local/shared precedence first. PiP changes magnification distribution only (official). |
| Zeroing/Rangefinder aim-point correction (L4072, 30 Oct: 54 singleton zeros read on 2.1.1.0, proposal to apply them as the default zero in the Soldier Target view, validation one M4A1 100 m firing-range shot, [receipt](../../reference-data/provenance/frosty-2026-10-30-L4072-zeroing-singletons-2110-proposal.json)) | `sim/ballistics.js` | Needs L9 effective selection/units/activation/correction evidence. Former capture rank 7 was removed as unnecessary ([operator removal decision, 28 September 2026](BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)); do not reinstate the recording request. |
| Keep class and mode context in damage/regen comparisons | Provenance, scenario controls | Shared defaults are not universal match rules. |

Also applied: SOR-300SC and GRT-CPS empty reloads are 3.2 s and 3.034 s,
from the [23 September capture](../../reference-data/provenance/frosty-empty-reload-capture-2026-09-23.json).

## Parked questions

These need new source or consumer evidence before they are reopened. Reopen one
when an asset changes, a new target body becomes available, exact class/mode
selection is found, or a compiled/native consumer is identified. An unresolved
runtime question is not evidence that the source asset is unused.

- **Closed path (operator, 1 Oct 2026): unmapped EA patch-note mentions.** The 1,944 unmapped
  mentions from the patch-notes coverage run are not a research path: mostly gadget, vehicle or
  mode text, previews, or qualitative guide wording, and the older fixes (1.2.3.0 and earlier,
  1.3.3.0 armored chest) have no current value. L741-L748 cover the current questions. Reopen
  only when a new patch states a weapon or soldier number.

| ID | Question | Status and blocker |
|---|---|---|
| W1 | Bipod/mounted modifiers and [idle table](../../reference-data/provenance/frosty-idle-duration-2026-09-23.json); [deployed review](../../reference-data/provenance/frosty-weapon-states-reviewed-2026-09-23.json) | Idle table associated across 63 GS blocks (BREN3 null). Values match the ADS ladder minus one frame; exceptions are VSSM and Interdictor. Need native use and stacking. No mounted recoil reduction established. |
| W2 | VSSM GS ADS +1 versus WB timing; [review](../../reference-data/provenance/frosty-vssm-ads-reviewed-2026-09-23.json) | GS +1 is separate from zero WB contribution. L62 found the same GS-only `GID_ADSTime_BRL` on EF88 and BROD3 Extended; EF88 panel Mobility follows the WB index. Need controlled ADS timing or a GS consumer. |
| W3 | M4A1 Magwell, BROD3 Cryo, SubsonicFrangible; [review](../../reference-data/provenance/frosty-attachment-branches-reviewed-2026-09-23.json) | Plain Magwell selects an empty default; BROD3 = BREN3. All 15 ammo branch defaults are true; no live-menu evidence. |
| W4 | Reload threshold/delays and WB frame duration (`Field_440ed7fa`) | 63 raw WB extracts. Need a timing consumer or commit/next-shot capture (rank 6). |
| W6 | Burst recoil, controller activation, lights, modifier order, unused recoil bounds, class traits, Slim Angled double ADS | Need native execution or controlled gameplay. Do not repeat exhausted operands. |
| W7 | Weapon Attributes native provider, sine/conditional rules, `Field_b30a73ed`; [model](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/WEAPON_ATTRIBUTES_MODEL.md) | No native provider evidence. |
| W8 | Grid surface and velocity candidates (L128/L130) | Two bounded leads yielded no site correction or useful comparison proposal; close the grid-inventory line. Six primary-material joins, 132 pair/map cells and nine speed-labeled objects are recorded. Reopen only for an authoritative field association and concrete primary-projectile consumer route; do not repeat numeric-ID or neutral-field scans. |
| W9 | Jump and landing numeric inventory (L132/L134) | Two bounded leads yielded no correction or useful enhancement proposal. Exact imports and seven named GRX tuples are recorded. Reopen for independent field-role/unit evidence and a validated consumer equation/activation route; do not repeat tuple or channel-name scans. |
| O1 | Ambiguous PiP layouts; [decoder limits](../frosty/TOOLS.md#sdk-and-decoding) | One pair reproduced; added import targets OptionEnablePiPZoom. Need independent field/consumer evidence. |
| O2 | Riser fields, inline/shared model precedence, render FOV | M2010 inline 55/59 and shared 34/20 are distinct paths. RMR riser 1.3 versus 1.0 needs consumer/precedence evidence. The former optic-framing recording was removed as unnecessary ([operator removal decision, 28 September 2026](BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)); no renewed capture request. |
| O3 | Optic glint and breath control; [discovery](../../reference-data/provenance/frosty-optic-discovery-2026-09-23.json) | Source links documented; visibility and duration need native or controlled evidence. |
| M1 | Regen/spotting activation and base values | Base 5 s, ammo 4/2 chains verified. All 13 Subsonic packages link both spotting effects. Native composition and reset remain unresolved. Former captures 1-2 were removed as unnecessary ([operator removal decision, 28 September 2026](BF6_CAPTURE_PRIORITIES.md#removed-captures-28-september-2026)); retain the source/application gates. |
| M2 | Soldier settings, abilities, LowProfile, suppression, movement ([settings](../../reference-data/provenance/frosty-soldier-settings-reviewed-2026-09-23.json), [abilities](../../reference-data/provenance/frosty-multiplayer-ability-candidates-reviewed-2026-09-23.json), [movement](../../reference-data/provenance/frosty-movement-reviewed-2026-09-23.json)) | Named configuration only; activation and native equations unverified. Registry defaults are not active mode values. |
| M3 | Four soldier file GUIDs; [trace](../../reference-data/provenance/frosty-1.4.3.0-unresolved-guid-trace-2026-09-16.json) | Need target body or consumer evidence. |
| G1 | Standard MP mode/map overrides; [review](../frosty/WEAPONS.md#mode-and-map-context) | Breakthrough has retreater-specific spotting defaults. No general combat override established; need effective server settings. |

## Where things are

- **Records.** `python scripts/frosty-records.py status` summarises live leads,
  what awaits the operator, the latest closed leads, ledger drift and stale
  pointers. The [lead index](../../reference-data/frosty/lead-index.json) lists every
  recorded lead with its status, receipts and what would reopen it;
  [site evidence](../../reference-data/frosty/site-evidence.json) maps site pointers
  to the receipts that bear on them; the [asset findings](../../reference-data/frosty/asset-findings.json)
  are generated from the frozen base plus each record's assets.
- **Site-input ledger.** The [input inventory](../../reference-data/provenance/frosty-site-input-inventory-v3-2026-09-23.json)
  covers every `data/*.json` leaf and `sim/*.js` line as of 23 September; [inventory v4 and its delta ledger](../../reference-data/provenance/frosty-site-input-inventory-v4-2026-09-28.json)
  (28 September) classify the 1,739 data leaves that changed since (sim drift is reported by `frosty-records.py ledger-drift`, not re-reviewed). The
  [final review](../../reference-data/provenance/frosty-site-input-review-final-v2-2026-09-23.json)
  classifies each one, and its [validation](../../reference-data/provenance/frosty-site-input-review-validation-2026-09-23.json)
  checks it. Use the review's blocker and next-step fields for L11.
- **Patch notes.** The [patch-notes inventory](../../reference-data/patch-notes/patch-notes-inventory.json)
  dates the EA game updates from 1.0.1.0 to 1.4.3.5 with their links and local builds
  (collected 30 September; it has no 2.1.1.0 entry yet, and lists Season 5 as upcoming). Use it to
  date creator videos, guides and EA statements: content from date D reflects the latest
  update released on or before D.
- **Topic results.** Spread, recoil, precision, timing, ADS, zeroing, projectiles and
  spotting results are in [weapons](../frosty/WEAPONS.md) and
  [attachments](../frosty/ATTACHMENTS.md). Receipts are in
  `reference-data/provenance/`; the lead index above links each lead to its receipts.
- **Catalog audit ledger.** `../BF6 Datamining/builds/1.4.3.0/reports/exhaustive-audit-2026-09-23/coverage-decoder-v5.sqlite`,
  used by `scripts/frosty-audit-coverage.py`. See [tools](../frosty/TOOLS.md#exhaustive-audit-coverage-ledger).
  Capture and decode coverage are not semantic review.
- **Capture work.** The [ranked capture plan](BF6_CAPTURE_PRIORITIES.md).

## History

The full 23 September handoff, with catalog-audit checkpoint counts, the per-topic
site comparison narrative and the E1–E4 catalog tasks, is in commit `b3040e7`
(`git show b3040e7:docs/working/FROSTY_RESEARCH_QUEUE.md`). Those counts describe
coverage, not findings. They were removed here so the queue lists work rather than
progress.

<!-- native-semantics:current-run:start -->
## Native semantics current run (1 October 2026)

Run CLOSED: `2026-10-01T0840-0400-native-semantics`, L1000-L1008. L1009-L1099 are unused. The available control-qualified static reader frontier is exhausted; recovering new native meanings remains incomplete. Build 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`.

Two installed readers pass known-answer controls: `scripts/frosty-enum-meaning-reader.py` qualifies 244 weapon, 638 soldier and 438 vehicle enum field identities; `scripts/frosty-curve-table-reader.py` matches 4 weapon, 14 soldier and 5 vehicle entries under six controlled schemas. Both applications are in the run folder. Exact descriptor membership and software-model controls are separate from native meaning. Entries changed from limit to new meaning: weapon 0, soldier 0, vehicle 0. No new site-number proposal is justified.

Compiled expression and resource grammars, field/type hashing, zeroing/stance/spotting labels, native interpolation and axis units remain unresolved. Controls pass for source identities and the two structural readers. The unique local-state ID route failed its semantic control and was rejected. No finding about native absence follows from a failed or unavailable semantic control.

Required method changes are recorded in orchestrator-progress.md: forward hash/source tests to inverse-seed algebra and authored state joins; size correlations to emitter input-schema controls; then exact retained UI choice/value bindings. No repeated forward inventory or capture was used. The 85-row where-not-to-look.json index records compact routes, attempts, limits and reopen conditions. Reopen with a static grammar/consumer contract and confirmed input/output control, a held-out field/type hash control, or a raw typed same-owner UI choice/value mapping.

Nine receipts pass check-receipt. Parent reviews and independent raw samples pass. All finished leads are committed through private indexes seeded from HEAD with only owned paths and hunks. Final-verification.json checks exact commit paths and sizes. No file over 10 MB was committed. No generated build/file commit, site data/simulation/UI edit, recording, game process/memory operation, new capture or push. Other sessions' work is preserved. Shared records have 6 expected generated-file errors and zero non-generated errors at close; no rebuild was run.

The handoff, progress, reader overlays, final verification and cleanup.json are in `C:/Users/royal/Documents/BF6 Datamining/reports/weapon-analyzer-research/2026-10-01T0840-0400-native-semantics`. Shared cleanup verified this closed folder: zero links or files removed. Resume only from a recorded reopen condition.

- L1000: `8414ed2e6fe600a4d29842162dbb34f137bc9847`.
- L1003: `8414ed2e6fe600a4d29842162dbb34f137bc9847`.
- L1004: `8414ed2e6fe600a4d29842162dbb34f137bc9847`.
- L1001: `8414ed2e6fe600a4d29842162dbb34f137bc9847`.
- L1002: `8414ed2e6fe600a4d29842162dbb34f137bc9847`.
- L1005: `8414ed2e6fe600a4d29842162dbb34f137bc9847`.
- L1006: `8414ed2e6fe600a4d29842162dbb34f137bc9847`.
- L1007: `8414ed2e6fe600a4d29842162dbb34f137bc9847`.
- L1008: `8414ed2e6fe600a4d29842162dbb34f137bc9847`.
<!-- native-semantics:current-run:end -->

<!-- weapons-ui-frontier:start -->
## Current weapons UI frontier run (1 October 2026)

Run: `BF6 Datamining/reports/weapon-analyzer-research/2026-10-01T0950-0400-weapons-ui-frontier/`, L900-L907, build 1.4.3.5 / Head 4909002. The available UI/source-comparison frontier is exhausted; native behavior remains partly unresolved. All 1,319 metadata catalog paths have scope dispositions. The integrated census has 3,557 text/interface rows, 627 lexical numeric occurrences and 233 uninterpreted effect/pro-con arrays. Twenty-five numeric occurrences match site text or established source comparisons; 602 remain unmapped or contextual. The four retained bar model candidates match current source evidence within existing operator/provider limits.

Five peak-damage intervals and the eight-shot cylinder statement match selected source values and site models. Current description wording matches 61 of 63: M2010 ESR and SV-98 have missing string IDs and archived screenshot text. L905 corrects two L900 Windows decoding comparison errors and L740's stale current 150 m assertion; current Interdictor text says 120-160 m. Earlier receipts remain unchanged. Existing reviewed attachment bug boundaries and proposals remain applicable. No new scalar implementation proposal is qualified; concrete validation predictions for the matched intervals/count are retained in L905.

The prior atlas is reused without a rebuild. Exact candidate lookup adds 0 meaningful known-limit families and 0 contexts. Top unknowns: effect-chip/pro-con roles; selected attachment-to-AAM scalar receiver; native bar arithmetic/provider selection; contextual stat/mode-ammo selection; optic nominal zoom versus selected FOV/PiP precedence. `where-not-to-look.json` gives route, fields, tried method, stop reason and reopen condition. Method switched after two mostly-limit census batches to current bar controls, exact localization-ID references and confirmed source meanings.

Eight leads are reviewed and committed through a separate index seeded from HEAD, own paths/hunks only. Seven shared-lock capture batches verified exact metadata/resource bytes. No generated-file build or commit, site edit, recording or push. Handoff and final audit are complete. The run is CLOSED for available source evidence. Final guard and manifest verify pass: 27,372 files, 0 new, 0 changed, 0 missing. The shared cleanup report and apply removed 0 links and 0 files; cleanup.json is verified. Commit IDs are in run-local-commits.json and handoff.md. Exact reopen conditions are recorded there.


Local lead commits: `8414ed2e6fe6`, `8414ed2e6fe6`, `8414ed2e6fe6`, `8414ed2e6fe6`, `8414ed2e6fe6`, `8414ed2e6fe6`, `8414ed2e6fe6`, `8414ed2e6fe6`.
<!-- weapons-ui-frontier:end -->
