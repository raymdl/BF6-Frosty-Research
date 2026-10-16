# Ranked in-game capture plan

Rescoped 28 September 2026 by the operator: captures are for mechanics that change a
displayed number and cannot be settled from source, the in-game stat screen (which
is treated as accurate) or the screenshot audit. Everything else was removed; see
[Removed captures](#removed-captures-28-september-2026). Source questions remain in
[open questions](../frosty/OPEN_QUESTIONS.md).

**Capture rule (operator, 28 September 2026).** Request a recording only when all
four hold: (1) its result would change a displayed site number or decide a pending
enhancement proposal; (2) the source, the in-game stat screen (treated as accurate),
the screenshot audit, official EA text, Sym and the operator's own in-game knowledge
cannot answer it (ask the operator before requesting a recording); (3) the predicted
difference is large enough to see in a recording; (4) it is the smallest test: one
weapon and loadout, a stated prediction, and what changes on the site for each
outcome. Otherwise record the limit as unresolved; do not add a capture.

| # | Capture | Why | People / format |
|---|---|---|---|
| 1 | Match Trigger semi vs auto (M433; L17) | Site shows no effect; source binds about 16% less recoil and faster recovery on 24 weapons, probably semi-only | Solo; video, repeated groups |
| 2 | Optional: hit-capsule boundary (M433; L99) | Target-view chest/abdomen split; M433 chest aim 4 → 5 hits if the source capsules hold. Target view is already labelled approximate | Enemy helper standing still; damage numbers **Done 10 Oct (L4010): chest zone confirmed as the site draws it; no further capture needed.** |
| 3 | Recoil recovery by impacts (AK-205, Standard and Lightened Suppressor) | Every spray on the site uses an assumed recovery law. The 14 October replay of the September recordings rejects two alternatives but leaves the M4A1 15-round climb 20% above the model and a 33 ms post-shot dead time as the one-parameter explanation; AK-205 15-round groups differ by 13 cm at 20 m between the two laws | Solo; video with audio and HUD, screenshots of each group; about 840 rounds (plus 500 optional M4A1) |

## Record once per session

- Show the game version and date. Record the mode, map and platform. Save custom
  server settings, including damage, health, regeneration and spotting changes.
  A custom-mode result does not by itself establish standard multiplayer behavior.
- Show the full loadout, class and specialization. Use exact attachment labels.
  Keep these fixed within each comparison except for the tested item.
- Show resolution, FOV, ADS FOV option, PiP option, input device and relevant HUD
  options. The earlier 1.4.2.5 / FOV 103 captures are historical; confirm current
  settings rather than carrying them forward silently.
- Keep the original video with audio and full HUD. Prefer 120 fps for short timing
  tests when practical; 60 fps is still useful. State the actual recording rate.
  Avoid interpolation, slow-motion exports, frame blending and cropped-only copies.
- Include a loadout card before each set. Keep each trial identifiable, for example
  `01_spotting_SG553R_standard_observer_trial01`. Five repetitions are a useful first
  timing set; threshold tests use three repeats on each side of the boundary.
- Report missing or hidden indicators as unavailable. Do not treat them as zero.
  Record failed or ambiguous trials as well as successful ones.

## 1. Match Trigger in semi-auto and automatic modes (L17)

**Why it matters.** Match Trigger can be selected on 24 weapons, and the site shows it
with no effect. On all 24, source binds recoil tier +3 (M433 per-shot recoil
×0.844, about 16% less), recovery ×1.728 (factor 72 → 124.4) and spread increase ×0
([L24](../../reference-data/provenance/frosty-2026-09-24-L24-match-trigger-family.json)).
The effects sit behind the same fire-mode condition class as the burst modifiers
(mask 1 = semi, [L31](../../reference-data/provenance/frosty-2026-09-24-L31-fire-mode-mask-candidate.json)),
so they are probably semi-only, which the stat screen does not reflect. If they
act, the site understates one of the stronger ergonomic choices; if they are
semi-only, they matter once the single-fire mode proposal (L14) exists. Only a
semi/auto recoil comparison answers both.

**Bloom done 25 September:** no bloom in semi with or without Match Trigger, so the
bloom operand cannot be isolated. Recoil and recovery comparisons are still open.

Use M433, matching the HK433 source trace. Compare the bare baseline with Match
Trigger, with all other choices fixed. Show the selected fire mode and attachment.
Run manually selected semi-auto first, then automatic as a condition control;
tapping an automatic trigger is not proof of selecting semi-auto. Record repeated
isolated shots and equal-cadence groups in ADS and hip, stationary first.

Measure initial aim displacement separately from weapon animation, recoil return
at matched displacement/time, and the spread indicator or repeated impact groups.
Use a cadence high enough that the baseline shows measurable bloom; full recovery
between taps cannot distinguish the zero-increase candidate. Match shot intervals
between paired trials. A missing/censored indicator is unavailable, not zero.

If all source operands act under the current model, the M433 candidate predicts
a per-shot recoil ratio of 0.843908625, a recovery factor of 124.416 instead of 72,
and zero added bloom with unchanged minimum spread. `GS_HK433` also binds the
semi-mode no-bloom modifier ([L63](../../reference-data/provenance/frosty-2026-09-25-L63-vssm-semi-bloom.json)),
so the bare semi baseline may already show no bloom. In that case the bloom
comparison cannot isolate Match Trigger; the recoil and recovery comparisons still can. If the attachment acts only
in semi-auto, the automatic control should lack those changes. If no differences
are resolved, the result is inconclusive about activation and global absence.
A different direction or magnitude can reject this simple composition. There is
no sourced cadence prediction; record timing to control the experiment. Native
operator order and broader weapon coverage remain separate questions. See
[L17 evidence](../../reference-data/provenance/frosty-2026-09-24-L17-match-trigger-indirect-effects.json).

## 2. Optional: hit-capsule boundary (L99)

M433 single shots up the centre line of a standing helper in MP at 10 m. Record
loadout, target orientation, aim position and per-shot damage. Damage numbers
(26 versus about 22) decide the chest/abdomen boundary before any target-view
change. Shots above the helmet are exploratory only, and the range dummy is not a
validation target (different head length and materials). Keep site geometry
unchanged pending the result. See the
[L99 receipt](../../reference-data/provenance/frosty-2026-09-27-L99-soldier-hit-capsules.json).

## 3. Recoil recovery by impacts (AK-205)

**Brief:** Datamining `reports\review-2026-10-14\CAPTURE_BRIEF_recoil_recovery.md`, with
predictions in `recovery-variants\capture-predictions.json` (`predict-capture.mjs`).

**Four-part rule.** (1) The recovery law feeds every recoil path the site draws; the
September M4A1 impact screenshots sit 20% above the model at 15 rounds and the camera
fits need a different factor scale per weapon (M4A1 0.77, TR7 and AK4D 0.91). A fixed
dead time of about 33 ms after each shot fits all three with one parameter; if it holds,
sustained-fire climb changes on every automatic weapon (AK-205 15-round group 69 → 82 cm
at 20 m). (2) Source gives the recovery operands but not the equation, the stat screen
shows only the per-shot amount, the screenshot audit has no sustained-fire measurement,
and the Sym pages describe the law without its constants; the 14 October replay used every
existing recording. (3) Predicted differences are 9 to 13 cm on 10- and 15-round group
height against 2.4 cm burst-to-burst scatter on the AK-205 (variation 7.4°), and 4 to 10 cm
of remaining recoil at 133 to 200 ms in single-fire pairs against 1.2 cm scatter.
(4) One weapon, two muzzles, the default loadout otherwise; the brief states the prediction
for each band and what changes on the site for each outcome.

**What it tests.** Part A, single-fire pairs at 133 to 400 ms gaps: the production law says
the AK-205 is back on the aim point by 300 ms (9.5 cm remaining at 133 ms, 4.0 at 200);
a nonzero mean at 300 ms falsifies the factor or time exponent with no camera model.
Standard against Lightened at 133 and 200 ms tests the ×1.2 recovery operand (about 1 cm
difference, three standard errors with 15 pairs per band). Part B, automatic bursts of 5,
10 and 15 rounds, 10 each: the 15-round Standard mean decides between 69 cm (production
law) and 82 cm (33 ms dead time); between the two gives the implied dead time. Part C,
optional M4A1 10- and 15-round bursts, ties the result to the September screenshots
(230 cm observed at 15 rounds against 192 and 222 cm predicted).

**First attempt, 14 October.** Ten Part A clips were recorded (120 fps, audio, Mini Flex, the range's grey door beyond 20 m). Timing is usable (130 to 140 ms at the trigger cap); impacts are not, because every shot merged into one light decal smear. The no-bloom condition for single fire was confirmed on the spread indicator. The brief now requires the highest-magnification optic with PiP off (sights carry no recoil or spread effect in site data), about 40 m so decals separate, and a side-step then a 2 s pause between pairs; the retake is pending.

**Result, 14 October ([L4040](../../reference-data/provenance/frosty-2026-10-14-L4040-ak205-recoil-recovery-capture.json)).** Retake recorded and analysed the same day (run folder `2026-10-14-ak205-recovery-capture`, `ANALYSIS.md`). Lens magnification measured at 5.00 over 1x in every clip. Pairs: 0.331 / 0.302 deg (Standard / Lightened) at 133 ms and 0.264 / 0.225 at 167 ms against 0.271 / 0.244 and 0.190 / 0.145 from the production law; bursts 1.36 / 2.13 / 2.41 deg (Standard 5/10/15) against 1.17 / 1.74 / 1.97. A factor scale of 0.8 fits all ten; the 33 ms dead time fits bursts only and is rejected by the pairs; the x1.2 Lightened operand is supported. The 1x FOV was confirmed by the operator as 103 (14 October). Open: a second weapon profile. Proposal in the queue.

**Follow-up capture: LMR27 pairs.** Brief in Datamining `reports\review-2026-10-14\CAPTURE_BRIEF_lmr27_pairs.md`: four bands (133, 233, 300, 400 ms), 15/15/15/10 pairs per suppressor, same setup as the AK-205 retake. Predictions under the stored factor and x0.8 differ by 5 to 8 px at 233 ms and beyond (300 ms Standard: 17 px stored, 24 px x0.8) against about 1 px of band error, so one session decides whether the 0.8 transfers to the slow recovery profile (factor 13.7, time exponent 0.56). **Recorded and analysed 14 October ([L4041](../../reference-data/provenance/frosty-2026-10-14-L4041-lmr27-pairs-second-profile.json)):** at 233 ms, 0.384 / 0.322 deg (Standard / Lightened) against 0.319 / 0.271 stored and 0.403 / 0.349 at x0.8; effective scale 0.85 to 0.9, so the constant transfers. The 133 ms band was unusable (shot 2 lands under the reticle's top arc) and the 300 and 400 ms bands are below the 25 px resolution floor; a 180 to 200 ms band would tighten the value. **Applied 14 October:** the operator approved the proposal and the site now scales every recovery factor by 0.8 (`RECOIL_RECOVERY_SCALE` in `sim/core.js`); L4040 closed as site-fixed.

**Revisits** the 28 September removal of "idle recovery and recoil return" (reason: a video
cannot pin the recovery equation). It cannot pin it from an open fit; it can choose
between stated laws when each has a prediction, which is what the brief gives. Results go
to the Analyzer `docs/RECOIL_SPREAD_MODEL.md` ("The recovery law against the BF1
community formula") and a dated receipt; no site change without the operator's approval.

**Follow-up capture, 15 October: the recovery tail and a third profile (TR-7).** Overnight re-analysis of the 14 October pairs with a template fit that resolves marks down to 6 px ([L4042](../../reference-data/provenance/frosty-2026-10-15-L4042-recovery-tail-template-fit.json)) measured every band: the factor scale 0.8 to 0.9 holds on both profiles, but the AK-205 keeps 0.10 deg at 292 ms and 0.08 at 333 ms where the x0.8 law is at zero, and the LMR27 Lightened at 350 ms (0.191 deg) recovers no faster than the Standard. Brief in Datamining `reports\review-2026-10-14\CAPTURE_BRIEF_tail_and_tr7.md`: TR-7 pairs at 167, 233, 300, 450 and 600 ms plus 5/10/15 bursts, both suppressors (third profile, factor 104 / exponent 1.459, and the tail test on a 1.16 deg kick); LMR27 pairs at 200, 300 and 600 ms, both suppressors (Lightened replicate, scale clear of the arc); optional AK-205 at 450 and 600 ms. Hold still 1 s after shot 2 before the side-step. **Recorded and analysed 15 October ([L4043](../../reference-data/provenance/frosty-2026-10-15-L4043-tr7-lmr27-tail-capture.json)):** the 0.8 scale holds on the TR-7 (267 ms: 0.214 / 0.158 deg against 0.226 / 0.161 at x0.8; 5 and 10-round bursts match), the LMR27 reproduces 14 October to 0.001 deg with the Lightened tail anomaly intact, every band from 480 ms is at the estimator floor (no residual), and the 15-round TR-7 bursts climb to 11.2 deg against 8.7 predicted. The TR-7 167 ms Standard band was lost to the reticle arc. Next capture: brief in Datamining `reports\review-2026-10-14\CAPTURE_BRIEF_m433_and_long_bursts.md` (16 October): M433 pairs at 167 / 233 / 300 ms and 5 / 10 / 15-round bursts, both suppressors (the 72 / 1.2 profile, fifteen weapons), recorded 16 October; the long-burst sets in that brief were withdrawn after L4045 and L4046. No further capture is requested; remaining questions are worked from existing footage. **Offline shape study, 16 October ([L4044](../../reference-data/provenance/frosty-2026-10-16-L4044-recovery-law-shape.json)):** no two-term, rate-capped or time-capped recovery reproduces the tail, the Lightened tail and the TR-7 late climb together (best combination chi2 329.8 against 476.7 applied), and the 15-round close-ups show the climb accelerating through the burst, which no recovery-only law can do. The next capture should record per-shot impact positions (the burst video at 1x resolves 0.9 deg steps) rather than extents. **Camera track of the 15-round videos, later on 16 October ([L4045](../../reference-data/provenance/frosty-2026-10-16-L4045-tr7-burst-camera-track.json)):** the pre-shot aim follows the x0.8 law to within 0.4 deg through all 15 shots on both suppressors (8.51 against 8.32 deg at shot 15 Standard, 7.61 against 7.62 Lightened), so the convex-climb reading is withdrawn; the extent excess is impact deviation 1.0 to 1.5 deg above the aim at the top of the spray, and the recovery after the last shot is rate-limited near 30 deg/s where the law runs at 37 falling to 10. Captures that would settle these: long bursts followed by a held aim on two profiles (the recovery rate limit), and a mark-per-shot measurement of impact against aim. **Extents re-measured on the 1x screenshots ([L4046](../../reference-data/provenance/frosty-2026-10-16-L4046-tr7-burst-extents-1x.json)):** 15 rounds 8.62 / 7.59 deg (law 8.67 / 8.03), 10 rounds 6.38 / 6.04, 5 rounds 3.58 / 2.97; the close-up method had counted the panel frame and the weapon as marks, and the spray top in L4045 was the dust cloud. Every TR-7 burst sits on the x0.8 law; the mark-per-shot capture is no longer needed for this weapon. Future burst captures: measure at 1x from the firing position (the close-up adds nothing). **M433 set recorded and analysed ([L4047](../../reference-data/provenance/frosty-2026-10-16-L4047-m433-profile-capture.json)):** Standard pairs 0.279 / 0.101 / 0.056 deg at 200 / 267 / 333 ms against 0.284 / 0.115 / 0.013 at x0.8 (no tail at 333 ms); Lightened 0.246 / 0.101 at 200 / 267 ms; 1x bursts 5 / 10 / 15 rounds 2.55 / 4.05 / 5.66 Standard (x0.8 2.23 / 4.31 / 5.72) and 2.29 / 3.85 / 4.71 Lightened (x0.8 2.17 / 4.08 / 5.31). The spread indicator (on for the first time) never appears in semi-auto pairs and opens from the first automatic shot; it is masked in the detectors. Sets 2 to 4 of the brief (TR-7 20-round bursts, TR-7 300 ms pairs, AK-205 long bursts) were not recorded. **Camera track of the pair videos ([L4048](../../reference-data/provenance/frosty-2026-10-16-L4048-pair-camera-track.json)):** 356 of 377 pairs tracked; the recovery clock resets at every shot (the no-reset variant is excluded on all 36 bands); every kick rings for 7 to 10 frames with a fixed period; after a single shot the camera is above the x0.8 law by +0.12 deg (AK-205) and +0.25 to +0.33 (TR-7) from 200 to 330 ms, within 0.06 on the LMR27, and reaches zero at 408 to 458 ms with a 0.04 undershoot on the TR-7: the law stretched in time by x1.35 to 1.40 (AK-205, TR-7) or x1.05 to 1.10 (LMR27), descending at a near-constant 1.3 to 1.8 / 3.2 to 3.9 deg/s (the burst signature scaled down), not a slow pool. At shot 2 the camera sits 0.07 to 0.36 deg above the holes at 167 to 300 ms, growing with the kick, and equals them at 333 to 350 ms on the AK-205 and LMR27 Lightened; the LMR27 camera shows the Lightened advantage the holes lack. A capture that places the bullets against the camera on one shot would separate a stretched aim from a camera offset. **Stretched-time recovery laws fitted offline ([L4049](../../reference-data/provenance/frosty-2026-10-17-L4049-stretched-time-fit.json)):** a hard cap on the time term at 0.2 s scores 294.9 on the 56 hole observations against 359.2 applied (two-pool 241.8) but is worse on the AK-205; a smooth saturation, a lower exponent and a descent that holds its early rate are all worse than the applied law (367.9, 341.3, 698.9); none removes the camera's x1.35 stretch at its hole-fitted C, and the scale the camera wants (0.45 on the AK-205 and TR-7, 0.7 on the LMR27) scores 5959.4 on the holes. The x0.8 law stands; no change proposed. Offset 0 with C 0.87 (270.6) is noted as a separate source-operand question. **Spread indicator against the site's spread law ([L4050](../../reference-data/provenance/frosty-2026-10-15-L4050-m433-spread-indicator-law.json)):** on every frame of the 12 M433 burst clips the indicator follows the site law: between-shot recovery 2.68 / 2.97 / 3.62 / 4.42 deg/s at 0.42 / 0.70 / 0.98 / 1.26 deg against 2.80 / 3.11 / 3.70 / 4.63 from 2.7 + 1.2 x delta^2.5, not-firing 7.13 against 7.2 deg/s starting one shot interval after the last shot, and peaks within 0.045 deg of the law at all 15 shots. The indicator draws the spread radius at the lens scale (179 px/deg, fixed by the 0.32 moving and 0.05 standing minima). The spread law is confirmed as implemented; nothing changes on the site.

## Removed captures (28 September 2026)

Full text of the removed sections is in git history (`git show ab9ca9c:docs/working/BF6_CAPTURE_PRIORITIES.md`).

| Former item | Decision and reason |
|---|---|
| Burst cadence and recoil (kept briefly on 28 Sep) | Closed without a recording: source BPM plus operator recordings support the site model (no delay on the six BPM-0 weapons, ~33 ms on M16A4/GRT-BC); the recoil part only served the cadence question. [Receipt](../../reference-data/provenance/frosty-2026-09-28-burst-cadence.json). |
| 1 Spot-on-fire ranges; 2 health regeneration | Not necessary (operator). |
| 3 VSSM barrel ADS; Interdictor grips | Stat screen is accurate and the site matches it (Mobility checker agrees on all captured panels, including 43 VSSM panels). The extra GS index likely feeds ADS-entry spread settling, which is not displayed. |
| 4 Idle recovery and recoil return | The site already uses Sym's firing/not-firing spread model and continuous recoil recovery; the missing Idle state (A16) only acts after long pauses. A video cannot pin the recovery equation. |
| 5 Bipod/mounted; 7 zeroing; 8 optic framing and SGX sway; 12 underbarrel traits | Not necessary (operator). |
| 6 Reload commit and bolt cadence | Ammo-commit timing is not displayed. Recon rechambering is the class trait (EA: "rechamber more quickly") and joins the trait proposal from source. |
| 10 Controller recoil | Not needed; the source vertical-recovery operand (L19) can be proposed directly if wanted. |
| 11 Menus, MagFlare, optic mobility, laser visibility, damage regression | Covered by the screenshot audit; optic mobility confirmed in game by the operator. |
| L14 single-fire cadence | Source `RateOfFireForSingleFire` (Sym SingleRoF) already supplies the rate; now a site enhancement proposal, no capture. |
| L18, L22, L25 | Not necessary (operator). |
| L20 pellet pattern; L32 strafe velocity | Pellet statistics stay unavailable; inherited strafe velocity is a few m/s against 300–900 m/s. |
| L27 Compact Handstop | Confirmed by the operator: it allows firing while sprinting (the site shows this chip). |
| L35 DRS-IAR heat | Heat build-up is visual only (operator). |
| L63 VSSM semi bloom | Done 25 September; rejected. |
| L103 sniper sway by class | Operator confirms snipers sway more on non-Recon classes. |
| Subsonic velocity precision | Differences of 0.3–0.6 m/s are below what recordings can resolve. |

## Maintenance

Keep the ranks current as source work proceeds. After receiving files, record which
capture IDs are received, usable, inconclusive or resolved. Link the measured report
and update the topic page. Remove resolved work from the active list without losing
its dated evidence. Do not request repeats of a usable existing control without a
specific new uncertainty.
