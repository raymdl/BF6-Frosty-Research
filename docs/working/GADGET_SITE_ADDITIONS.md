# Gadget research and potential Analyzer additions

[Current-site research queue](FROSTY_RESEARCH_QUEUE.md) · [Gadget source findings](../frosty/DATA_GRAPH.md#gadget-routes-hotfix-head-4892087)

## Purpose

Keep gadget work separate from research for the current weapon Analyzer. The
operator plans to add gadgets to the site in the future. These proposals require
product review before implementation. Serialized values, inferred meanings and
unresolved runtime behavior must remain separate; a source profile is not a
validated gameplay stat.

The scope includes all gadget functions. Health and ammunition resupply, vehicle
repair, revives, ladder interaction, deployable protection, detection and other
utility effects have the same priority as damage. Resource fields alone do not
establish those functions; follow the selected effect, target and receiving
consumer. Record qualitative source evidence as well as mapped numeric fields.

Use `python scripts/frosty-records.py status` for live leads in both queues.
Close gadget leads with the same receipt, topic-page, build/check and local-commit
workflow. Remove completed rows here. Closed leads and past runs remain in
[the research archive](../archive/FROSTY_QUEUE_CLOSED.md).

## Review before resuming (Claude Opus, 29 September 2026)

Read this before launching new gadget leads.

- **Accuracy is sound.** 1,209 sampled raw byte checks across 48 receipts (L162–L209 and
  the vehicle run) had zero mismatches. An independent decode of `Minigun_WB` matched
  (magazine 250, fire rate about 1800). Controls, parent reviews and scope boundaries held.
- **The yield is low because of the approach.** This run inherited the narrow
  one-question-per-worker method from the weapons work and spawned 47 workers. That
  method suits weapons, where each lead checks a number the site already shows. Gadgets
  have no site data, so most leads end as "value stored; meaning unresolved". Each also
  carries the full per-lead overhead: brief, control, review, receipt and two commits.
- **Consolidate before adding leads.** Do a census-style pass like the vehicle run's:
  finish the coverage list (77 of 121 groups had no reviewed lead at the start), map each
  family's roots and connections, then choose leads. Use narrow leads only for specific
  stats the gadget section would show.
- **Every proposal needs a named validation step.** "Confirm units, availability,
  composition" is not actionable. Name the check that would settle it, such as an
  in-game measurement or a stat screen, or leave it as a finding.
- **Don't queue leads that can only record limits.** L183 and L190 documented dead
  ends. Units, effective amounts and activation sit behind compiled graphs and native
  code (L190). More tracing will not resolve them; in-game checks or outside references will.
- **Writing.** Repo docs have dropped spaces between words and numbers ("with400",
  "Head4892087"). Fix these when the docs are next edited, and keep the proposal text readable.

## Active source leads

### Paused goal: trace all gadgets - GPT-6.1 Sol

The operator asked us to continue exploration after each group of leads. The
all-gadgets goal is paused at the operator's request. Orchestrator: **GPT-6.1 Sol**; workers:
**GPT-6.1 Sol, Low effort**. Run: `2026-09-29T185409-0400-sol61-all-gadgets`.
The [coverage list](../../reference-data/frosty/gadget-coverage.json) contains
121 normalized category/family groups, including shared
systems and assets whose current multiplayer availability is unresolved. These
are coverage candidates, not a confirmed list of equippable gadgets. Reuse the
previous run's receipts; investigate the remaining groups and new consumer routes.

Checkpoint, 29 September 2026: L162-L209 are reviewed and locally committed.
No gadget worker remains active. The latest record check passed: 511 valid
records, zero errors and two existing warnings. Site data, simulation and UI were
not changed. The all-gadgets trace is incomplete; source findings remain partial.

Resume from the run folder's `orchestrator-progress.md`. First reuse the exact
Corpse Drop Ammo token/consumer evidence and trace its receiving semantics or an
incoming drop owner. Then assess the remaining shared or ambiguous catalog groups
for a selected utility consumer before launching a lead. Compiled expression
grammar, effective utility amounts and runtime activation remain unresolved;
L190 records the scoped reader/control limit. Do not repeat unnamed float scans.

| # | Lead | Established | Next source step |
|---|---|---|---|

## Proposed Analyzer changes

These are potential additions for the future gadget section. None is implemented.

| Proposal | Affected data/code | Evidence and remaining validation |
|---|---|---|
| **Operator review: MP NVG resource source profile (L182)** | Optional future gadget comparison data and UI | Mapped MagazineCapacity/NumberOfMagazines/InitialAmmo/AutoReplenishRounds are -1; AutoReplenishMagazine false. Exact Ability and client VE references resolve. Confirm resource meanings and active consumer before any battery/refill/vision stats or availability claim. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L182-nvg-resource-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Railgun firing / resource source profile (L180)** | Optional future gadget comparison data and UI | Selected ammo 1/11/-1, RateOfFire about 299.99, reload fields about 4.266/-1; selected direct StartDamage/EndDamage 150/150 and falloff fields 100/200. Confirm availability, units and effective composition. No charge time, penetration, effective cadence or damage formula is established. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L180-railgun-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Vehicle Supply Crate resource source profile (L177)** | Optional future gadget comparison data and UI | The checked deployment chain selects the captured VB/gameplay objects; selected ammo is 1/1/-1 and reload fields are 1000/1000. Confirm resource meanings, units, availability and active configuration. No typed refill/repair consumer, benefit, radius or cooldown is established. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L177-vehicle-supply-crate-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Utility throwable resource source profiles (L176)** | Optional future gadget comparison data and UI | Concussion/Flashbang/Smoke/Proximity NumberOfMagazines 1/1/2/1; ReloadTime about 0.1 and ReloadTimeBulletsLeft -1; Shot.InitialSpeed.z 25 in all. Confirm resource meanings, units, active configuration and launch behavior before gameplay stats. No nonlethal effect claim. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L176-utility-throwable-resource-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Minigun firing / resource source profile (L175)** | Optional future gadget comparison data and UI | MagazineCapacity 250, NumberOfMagazines 1, RateOfFire about 1799.999023 and reload fields about 6.7/5.83. Preserve selected health/armor curve sources separately. Confirm current availability, field units, fire-mode selection and effective composition before gameplay stats; no effective cadence or damage formula is established. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L175-minigun-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Repair Tool direct-damage source profile (L174)** | Optional future gadget comparison data and UI | The selected local projectile stores StartDamage/EndDamage 13/13 and falloff start/end 100/200. Confirm current availability, units, hit frequency and effective composition. These values do not establish repair rate or damage per second; healing selection remains unresolved. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L174-repair-tool-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Mobile Jammer resource source profile (L173)** | Optional future gadget comparison data and UI | Mapped ammo 1/1/-1, AutoReplenishMagazine true, AutoReplenishRounds -1 and AutoReplenishDelay 45, with checked forward effect references. Confirm units, resource semantics and current availability before gameplay stats; no 45-second refill, jamming radius or duration claim. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L173-mobile-jammer-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: EOD Bot demolition / mine source profiles (L172)** | Optional future gadget comparison data and UI | Checked deployment/weapon-feature/Shot paths select demolition and mine blasts with damage/radius 5/4 versus 150/2; deployment/demolition/mine ammo tuples 1/1/-1, 1/2/-1 and 1/3/-1. Confirm current availability, units, resource meanings and effective composition. Cluster submunition remains a connected candidate. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L172-eodbot-payload-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: MPAPS / EIDOS resource source profiles (L171)** | Optional future gadget comparison data and UI | Both selected WB owners store ammo 1/1/-1. ReloadTime differs 0/0.5; ReloadTimeBulletsLeft is 0/0. Confirm availability, resource meanings and timing units. This does not establish protection radius, interception capacity or effective recharge/deployment time. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L171-mpaps-eidos-resource-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Drone payload configuration source profile (L170)** | Optional future gadget comparison data and UI | A checked separate PayloadDrone branch selects bomb blast fields 1.5/100/5/1/7.5 (inner/damage/radius/shock damage/radius). Confirm current availability, branch activation, units and effective composition. Lancet explosion 25/4 remains a compiled-consumer candidate and is excluded from selected gameplay stats. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L170-drone-payload-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Deployable Mortar payload source profiles (L169)** | Optional future gadget comparison data and UI | Two checked VB firing chains select M720A1/M722 with ammo 1/-1/-1 versus 1/3/0, ReloadTime 4 in both and selected blast damage/radius 60/7.622 versus 0/5. Confirm availability, sentinel meanings, units and effective composition; no trajectory or unlimited-ammo claim. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L169-mortar-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Panzerfaust3 variant source profiles (L168)** | Optional future gadget comparison data and UI | Baseline and DM32 configured projectile blast damage 130/230, radius 5/5; WB ammo 1/3/-1 and reload fields 4.96. Confirm current availability, default/fallback selection, units and effective composition; DM12A1 baseline use remains conditional. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L168-panzerfaust3-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Javelin launcher source profile (L167)** | Optional future gadget comparison data and UI | Mapped MagazineCapacity 1, NumberOfMagazines 3, reload fields -1; selected PB_Javelin blast damage/radius 125/4. Laser-guided remains a candidate with unnamed blast fields. Confirm availability, resource meanings, units and effective composition before gameplay stats. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L167-javelin-source.json). Attribution: GPT-6.1 Sol; worker Low effort. |
| **Operator review: Throwable ammunition / launch source profiles (L166)** | Optional throwable gadget comparison data and UI | Frag/Mini V40/Anti-Tank/C4/Incendiary/Throwing Knife store NumberOfMagazines 1/2/2/3/1/5 and WB Shot.InitialSpeed.z 25/35/25/9.5/25/44.973999. Baseline reload fields are also retained. Confirm resource meanings, timing units and native launch behavior; do not calculate carried uses or label the z field as physical throw speed. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L166-throwable-ammo-launch-source.json). Attribution: GPT-6.1 Sol; workers Low effort. |
| **Operator review: Claymore blast source profile (L164)** | Optional mine gadget comparison data and UI | Selected blast object stores InnerBlastRadius 2.5, BlastDamage 1, BlastRadius 5, ShockwaveDamage 1 and ShockwaveRadius 7.5. Confirm units, fragment effects and effective composition before gameplay stats; these values do not describe effective mine damage. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L164-claymore-blast-source.json). Attribution: GPT-6.1 Sol; workers Low effort. |
| **Operator review: Airburst Incendiary primary source profile (L163)** | Optional launcher gadget comparison data and UI | MagazineCapacity 1, NumberOfMagazines 3, ReloadTime and ReloadTimeBulletsLeft 2.53; the selected blast stores BlastDamage 1 and BlastRadius 3. No selected lingering route was proved. Confirm units, resource meanings and effective composition; BlastRadius 3 is not established fire coverage. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L163-airburst-incendiary-source.json). Attribution: GPT-6.1 Sol; workers Low effort. |
| **Operator review: Stinger / IGLA source profiles (L162)** | Optional anti-air gadget comparison data and UI | Mapped MagazineCapacity 1/1, NumberOfMagazines 3/3, ReloadTime 3.4/3.4 and ReloadTimeBulletsLeft 3.66/2.33; selected blast objects both store BlastDamage 100 and BlastRadius 5. Other projectile scalars remain unnamed. Confirm resource meanings, units, reload phases and effective damage before gameplay stats. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L162-stinger-igla-source.json). Attribution: GPT-6.1 Sol; workers Low effort. |
| **Operator review: Breaching Dart blast source profile (L159)** | Optional gadget comparison data and UI beside launcher source profiles | The standard primary projectile stores mapped `BlastDamage` 40, `BlastRadius` 1, `InnerBlastRadius` 1, `ShockwaveDamage` 1 and `ShockwaveRadius` 7. A separate gas configuration path has the same serialized fields but is only a candidate. Confirm units, selected multiplayer configuration, and effective blast/direct-hit composition before displaying gameplay stats. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L159-breaching-dart-source.json). |
| **Operator review: Throwing Knife projectile source profile (L156)** | Optional gadget comparison data and UI | Selected v2 projectile stores mapped Start/EndDamage 50/50, falloff start/end 5/15, InitialSpeed 350 and TimeToLive 10. These are serialized source values. Confirm units, effective hit composition and trajectory before displaying gameplay stats. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L156-throwing-knife-source.json). |
| **Operator review: launcher blast source profile (L152)** | Extend optional launcher comparison data and UI from L137 | Three selected primary projectiles store mapped `BlastDamage` 70/80/70 and `BlastRadius` 6/4/5 for RPG-7, MBT-LAW and AT4. Other projectile floats lack verified speed/time labels. These are serialized source values; confirm units and effective composition before gameplay numbers. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L152-launcher-projectile-source.json). |
| **Operator review: Anti-Tank Grenade blast source profile (L150)** | Optional throwable comparison data and UI | The selected blast object stores mapped `BlastDamage` 50 and `BlastRadius` 1.5, beside Frag 100/5. Its linked four-row child has no verified falloff labels. Display only source scalars after review; confirm units and effective damage composition before gameplay numbers. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L150-antitank-blast-source.json). |
| **Operator review: C4 blast source profile (L151)** | Optional explosive-gadget comparison data and UI | The selected WB-to-projectile-to-blast chain stores mapped `BlastDamage` 100 and `BlastRadius` 3, with eight falloff points; Frag stores 100/5 with seven points. These are serialized source values. Confirm units, interpolation and effective composition before displaying gameplay numbers. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L151-c4-blast-source.json). |
| **Operator review: AT Mine and M4 SLAM blast source profile (L153)** | Optional explosive-gadget comparison data and UI | Directly selected blast objects store mapped `BlastDamage` 300/100 and `BlastRadius` 2/1, beside Frag 100/5. These are serialized source values, not effective game damage or physical coverage. Confirm units and effective composition before displaying gameplay numbers. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L153-mine-blast-source.json). |
| **Operator review: Frag versus Mini V40 blast profile (L148)** | Optional throwable comparison data and UI | Selected hotfix WB-to-PBNS-to-blast chains store mapped `BlastDamage` 100/40, mapped `BlastRadius` 5/5, and distinct seven-/five-point falloff lists. These are serialized source values, not established effective game damage or physical coverage. Confirm units, interpolation and composition before displaying gameplay numbers. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L148-frag-miniv40-blast-source.json). |
| **Operator review: launcher handling comparison (L137)** | Optional gadget comparison data and UI for RPG-7, MBT-LAW and M136 AT4 | Three hotfix WB roots store `MagazineCapacity` 1/1/1, `NumberOfMagazines` 3/3/2 and `ReloadTime` 3.4/3.4/3.66; directly imported zoomed movement arrays store 0.45/0.4/0.45. These are serialized source values. Confirm multiplayer selection, carried-ammo meaning and timing/movement labels from the game or stat screen before displaying them as gameplay stats. Do not calculate reserve rounds from `NumberOfMagazines` yet. [Receipt](../../reference-data/provenance/frosty-2026-09-29-L137-launcher-handling-ammunition.json). |
