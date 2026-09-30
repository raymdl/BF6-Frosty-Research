# Vehicle research and potential Analyzer additions

## Purpose

Record vehicle source findings for possible future site additions. Vehicles are outside the current weapon and attachment scope. Cosmetics, skins and artwork are excluded. Keep serialized facts, inferred meanings and unresolved runtime behavior separate.

## Review before resuming (Claude Opus, 29 September 2026)

Read this before resuming vehicle work.

- **The census-first approach was right for a new domain.** Census, then identity for all
  46 roots, then family stages gave a complete map with only 6 workers. Keep that shape,
  and reuse it for gadgets.
- **Accuracy is sound.** Sampled raw byte checks across this run and the gadget run had
  zero mismatches, and parent reviews held.
- **Keep stages moderately sized.** L3007–L3009, L3014 and L3017 needed v2/v3 reruns,
  and L3014's receipt runs to about 1,000 lines. Split large family stages so each
  result can be reviewed in one pass.
- **Few usable numbers yet.** Apart from CB90 `MaxHealth` 1000 and the antenna's 150,
  the findings are structural: owners, entries, consumers and connections. Units,
  effective amounts and activation sit behind compiled graphs and native code (L3012,
  L190). More tracing will not resolve them. After finishing the coverage merge, choose
  the specific comparison stats a vehicle section would show, and name a validation step
  (such as an in-game test) for each before tracing further.
- **Use a vehicle-specific orchestrator prompt.** This run used the weapons-era prompt,
  which parks vehicles and tells the orchestrator not to trace itself. It worked around
  both; a prompt written for this domain would make the scope explicit.
- **Writing.** This doc has dropped spaces between words and numbers ("and37",
  "verifies46", "Head4892087"). Fix them during the coverage rewrite.

## Active research

The operator requested tracing of all vehicles on 29 September 2026. Workers use GPT-6.1 Sol at Low effort. Evidence is separated by Head and descriptor. The run folder is `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-09-29T2025-0400-vehicles`.

The operator requested a pause checkpoint. All 46 exact blueprint roots have checked identities and source profiles. Reviewed stage findings are saved below. The final coverage merge and current-understanding write-up remain for the next session. No source-pass completion or native runtime claim is made from the root count alone.

| Lead | Question | State |
|---|---|---|
| L3011 | Exact root coverage and available-source gap review | Reviewed audit; coverage proposal merge deferred for resume |

## Source findings

L3000 census review passed. The catalog contains 6,847 entries under `Common/Hardware/Vehicles`. The [coverage list](../../reference-data/frosty/vehicle-coverage.json) has 41 family/candidate rows: 38 families with 46 exact blueprint roots, plus C17, MD530 and Cheetah role candidates. Two additional roots outside that namespace require role review: a signal-decryption antenna and an Abrams ULR prop. A BattleRoyale, SP or Art path token does not establish an exclusion.

The census found two release capture rows and 3,344 hotfix capture rows. Functional profiles use exact Head/descriptor pairs. The [census receipt](../../reference-data/provenance/frosty-2026-09-29-L3000-vehicle-census.json) records the catalog scope, controls and source paths. The root identity review now verifies all 46 blueprint roots. Functional tracing is still active; identity coverage does not mean that all branches are complete.

L3001 completes seven same-hotfix health-channel name joins. The CB90 actual owner maps to configured `MaxHealth` f32 `1000` and `RepairRateModifier` f32 `1`; raw offsets are 440 and 712. The actual owner type/key and the separate registry wrapper/child/hash pairs were checked. These are named source fields; units, damage equations, repair composition and activation remain unresolved. See the [shared-health receipt](../../reference-data/provenance/frosty-2026-09-29-L3001-vehicle-health.json).

| Reviewed stage | Established source route | Remaining work |
|---|---|---|
| L3002: AH64E/F16 | Seven AH64E and four F16 weapon owners select exact same-hotfix WF/Ability targets; 256 profile raw reads | L3007 follows damage, movement, seats, slots, projectiles and variants |
| L3003: remaining aircraft | Nine captured base-family roots and selected local component/armament routes; MH47 was a capture gap | L3008 uses fresh MH47 roots and follows functional consumers |
| L3004: ground | Fourteen captured bases select 50 weapon-owner alternatives and 34 entry-owner instances; 400 profile raw reads | L3010 uses fresh AAV7A1/TheBeast/functional variant roots and follows consumers |
| L3005: watercraft/stationary/drone | Ten roots and 22 reachable weapon-owner branches; 400 raw reads; CWS root is CROWS | L3009 follows functional consumers and variants |

The dated receipts contain the reviewed record and hashes of the full external worker results. A selected owner or entry count does not establish a default loadout or usable seat count. L3002-L3005 are partial source profiles. Their reviewed continuations are recorded below. Cosmetics, skins and artwork are excluded by the operator; no cosmetic absence claim follows from this scope exclusion.

| Reviewed continuation | Source findings | Limit |
|---|---|---|
| [L3006 roles](../../reference-data/provenance/frosty-2026-09-29-L3006-vehicle-roles.json) | Cheetah customization selects Gepard and five functional armament/passive targets. The signal-decryption antenna is a separate vehicle-authored mission objective with configured MaxHealth150 and RepairRateModifier1. C17, MD530 and the Abrams ULR prop resolve to inspected model/object roles. | Keep the antenna as a separate objective profile. Exclude inspected visual branches. Names and path tokens alone do not establish roles. |
| [L3007 AH64E/F16](../../reference-data/provenance/frosty-2026-09-29-L3007-vehicle-air-pilot-continuation.json) | Selected damage zones, entry and slot definitions, projectile/warhead consumers, modifiers and AI constraints. Flight configuration reaches an exact local owner. | Hash-only receiving fields, units, flight equations and native selection remain unresolved. |
| [L3008 other aircraft](../../reference-data/provenance/frosty-2026-09-29-L3008-vehicle-aircraft-continuation.json) | Ten families and fifteen exact roots, including four added SP/Cine variants and MH47 input owners. | Different SP owner keys cannot inherit CB90 health names. MH47 polymorphic components are retained; no known weapon-owner match does not prove absent armament. |
| [L3009 water/stationary/drone](../../reference-data/provenance/frosty-2026-09-29-L3009-vehicle-water-stationary-continuation.json) | Ten families, Phalanx SP and the distinct TRV150 spectator role. Selected structured MM state/input graphs, entry/slot definitions, weapons, projectiles, modifiers and mode consumers. | MM roots are probable motion-machine graphs, not model-only exclusions. Graph labels do not establish equations or physical units. The spectator root has a different actual class/key from the base drone. |
| [L3010 ground](../../reference-data/provenance/frosty-2026-09-29-L3010-vehicle-ground-continuation.json) | Sixteen bases and functional Flyer60 SP/Vector CarChase variants; 52 base weapon-owner alternatives and37 entry owners. Typed firing owners, selected projectile data, three input targets and health names with exact schema limits. | Available projectile, movement, modifier and damage-consumer branches remain active source work. |
| [L3012 compiled resources](../../reference-data/provenance/frosty-2026-09-29-L3012-vehicle-resource-reader-gate.json) | Five selected SerializedExpressionNodeGraph bodies match typed source references, hashes, lengths and hotfix Head. All41 cited SDK/plugin/editor source hashes remain unchanged. | Raw retrieval is established. The checked route does not establish a registered semantic reader and independent operation control. Graph operations and native execution remain unknown. |
| [L3013 ground projectiles](../../reference-data/provenance/frosty-2026-09-29-L3013-vehicle-ground-projectile-curves.json) | Thirteen PD profiles, seven projectile blueprints and one selected MBT local payload. Six PD profiles select curve pairs; seven have exact null curve members. Both selected InnerRadius25/50 blast-curve point arrays are retained. | Point order does not establish units, interpolation or effective damage composition. No functional capture gap remains. |
| [L3015 IFV/AAV/APC targets](../../reference-data/provenance/frosty-2026-09-29-L3015-vehicle-ifv-aav-apc-tag-consumers.json) | Seventeen selected U targets resolve local tag owners. Sixteen select three exact Explosion_Damage, Bullet_Damage and SmallExplosion_Damage tag children; TargetDesignator has an empty selected array. Parent membership is checked. | These are identity and membership selections. No gameplay modifier/ammo/firing operand was established by this schema; native tag dispatch and mode admission remain unresolved. |
| [L3016 selected MD roles](../../reference-data/provenance/frosty-2026-09-29-L3016-vehicle-ground-md-roles.json) | All sixteen previously decoded MD selectors are raw checked and their exact exported targets resolved. Slot, bone and default-identity associations are established from actual selected schema. AAV7A1/TheBeast owner keys differ. Flyer60 SP/Vector CarChase reuse base target pairs through distinct source component keys. | No whole MD is classified as visual-only. Unnamed grammar and receiver roles remain exact schema limits; no movement statistic or native physics absence is inferred. |
| [L3014 AA/MBT equipment](../../reference-data/provenance/frosty-2026-09-29-L3014-vehicle-aa-mbt-equipment.json) | Twelve AA/MBT targets plus five Cheetah selections; exact reverse Ability joins, passive/thermal-smoke graphs, selected compiled body and direct removal set. 398 conservative operand reads checked. | Receiver names, compiled operations and native execution remain unresolved. Seven selected global membership/config bodies remain deferred; their identities do not establish gameplay admission or defaults. |
| [L3017 ground damage/entry/AI](../../reference-data/provenance/frosty-2026-09-29-L3017-vehicle-ground-damage-entry-ai.json) | Sixteen families and two functional variants. Selected root connection consumers, eight AAV damage-zone owners, AI aiming owners, repair interaction and ModBuilder graphs. 389 meaningful operands checked. Two selected compiled bodies are pinned. | Hash-only receiver meanings, units, equations and native graph execution remain unresolved. Entry and slot source data do not establish usable seats or multiplayer admission. View/global category/player-option dispatch are explicit scope endpoints. |

Most functional profiles use hotfix Head4892087 and descriptor SHA-256 `99b49cfd8bdb5bb6f0181df8ac0d93a0396c1b7f07a1ba3ce8ca1cea45969640`. Release control evidence uses Head4892017 and descriptor SHA-256 `91c9ea7c3dd830e34a78123c8bb7485e80eefdb18fc9c7ee41117971d23565c2`. These evidence sets remain separate.

## Potential future site additions

Candidate additions are vehicle source profiles, configured health/repair fields, selected armament alternatives, projectile profiles, seat/entry configuration, equipment/passives and movement/damage-zone comparisons. Each addition needs its typed selected consumer evidence and a clear confidence limit. No site implementation is authorized by this research.

## Coverage limits

A catalog entry or raw capture does not prove runtime use or current multiplayer availability. A family is complete only when its functional routes have a recorded result or a precise unresolved limit.

The [reviewed coverage audit](../../reference-data/provenance/frosty-2026-09-29-L3011-vehicle-coverage-gate.json) verifies46 exact root profiles and retains five separate role candidates. Seven global membership/config routes remain deferred through32 exact selected references. The full result and proposed compact coverage update are saved in L3011. The audit is complete; the all-vehicle research goal is paused before those deferred branches and the final repository coverage merge are settled. Restart steps are in the run folder's PAUSE_CHECKPOINT.md.
