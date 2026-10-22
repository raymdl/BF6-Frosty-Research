# Review of result-A.md

Source of truth for counts: ../bt-hq-groups.txt. "Group" = pads nearest that HQ.

## MP_ABBASID
Verdict: ok

- HQ-group table counts all match: HQ313 APC1 IFV1, HQ33 IFV1, HQ8 IFV1, HQ63 APC1, HQ283 IFV1, HQ74 0, HQ198 0, HQ151 IFV1. Totals APC2 IFV5 = 7 pads, as stated.
- Every pad-bearing HQ (313, 33, 8, 63, 283, 151) appears; reuse across phases is only the model's flip (defender in N, attacker in N+1) or the stated "the one not used by defenders" for coincident pairs.
- Sector order along x: @187 (x -182), @311 (-82), @221 (15), @95 (129); HQ313 at x -256 is beyond @187. Direction west to east is consistent. No in-game sample.
- The coincident pairs are HQ8/HQ63 (2.5 m apart) and HQ283/HQ74 (3 m). The data cannot say which one goes to which side. Under the brief's model, both could also be defender HQs for that sector. Leaving them unresolved is correct.
- Minor wording: anomaly line "Spawner classes total 2" means 2 classes, which is easy to misread as 2 spawners.

## MP_AFTERMATH
Verdict: minor fixes

- HQ-group counts match: HQ114 HMG1 (maxdist 73), HQ135 HMG1, HQ176 HMG1, HQ89 HMG1; HQ154/172/157/29 none. Total HMG4, no vehicles.
- Contradiction: prose and first table say the start base HQ114 has "no spawner" / "none", but the HQ-group table (correctly) gives HQ114 HMG x1 (its HMG is 73 m away; it is likely HMG69 or 151, which the first table assigns to S1). One of the two must go; the HQ-group table is the one to keep.
- First table S1 cell "HMG x3 (69, 151, plus 88 is middle, see S2) = 2 (69, 151)" is garbled and makes S1 hold 2 HMGs. The HQ-group view gives HQ135 1.
- Markers: Sector@20 (z 43.5) and @95 (z 31.4) are 12 m apart; only @83 (z -70.5) is south. The author's 3 sectors are CP clusters (north CP22/87/171, middle CP5/50/161, south CP129), not markers. The data does not settle this, so low confidence is right.
- Direction: no sample, and nothing in the data decides it. I agree with low confidence. The HMG-only content makes the per-phase table matter little.
- Pad use is correct: each of 114/135/176/89 is used once, plus the 135 flip.

## MP_BADLANDS
Verdict: minor fixes

- HQ-group table counts match: HQ109 Tank1 AT1, HQ107 APC1 AT1, HQ98 Tank1 AT2 HMG1, HQ135 APC1, HQ48 0, HQ64 0. Totals Tank2 APC2 AT4 HMG1 = 9, as stated.
- Contradiction with the first table: the start base row lists Tank x1 only and the S1 row gives AntiTank x2 (58, 75). The HQ groups put one AT at HQ109 (attackers) and one at HQ107 (defenders). A reader of the first table would think S1 defenders get both ATs. Corrected rows:
  - Start base: HQ109 | Tank x1, AT x1
  - S1: HQ107 | APC x1, AT x1
- The first table lists HQ64 under S3 and again under Final base, so it appears twice. The HQ-group table lists it once.
- Sector order @116 (316,-60), @139 (140,-206), @28 (-92,-323), with HQ109 (336,35) beyond @116, so the direction is consistent. No sample.
- Low-to-medium S3 confidence: I agree. HQ135 (x -21) is nearer @28 (96 m) than HQ48 is, and HQ48's nearest sector is @139 (117 m). HQ48 has no pads, so this does not change any vehicle set. The HQ107 and HQ109 groups have maxdist 96-97 m, so those two pad assignments are the loosest on the map.

## MP_CAPSTONE
Verdict: minor fixes (the HQ-group table is right; the top half is stale)

- In-game sample: attackers S1 Tank1 IFV1 equals HQ184 {IFV1, Tank1}. Attackers S2 Tank1 IFV1 equals HQ205 {IFV1, Tank1}. Both are equal sets, so the reversed direction is confirmed. The original direction would give S1 attackers HQ2 {IFV1, LT1, Quad2}, which the sample contradicts.
- HQ-group counts all match: HQ184 IFV1 Tank1, HQ205 IFV1 Tank1, HQ213 IFV1 Tank1, HQ263 0, HQ189 IFV1, HQ272 0, HQ246 IFV1, HQ266 Quad2, HQ188 IFV1 Quad1 LT1, HQ2 IFV1 LT1 Quad2. Totals IFV7 Tank3 Quad5 LT2 = 17, as stated. Every pad HQ appears.
- Stale statements a reader would be misled by, all above the CORRECTION line: "Attackers start at POLY34@215 (HQ2)", "defenders' final base is POLY31@73 (HQ184)", "Direction confidence: high", and the whole first table (S1..S5 labels, the "Attackers during S1" row on HQ2, "Final base" on HQ184). The correction note fixes these in words but does not replace them.
- Missed stray marker: Sector@103 is at (15.4, -11.5), the same as Abbasid Sector@221, and boxes=[] in bt-hq-groups. So three markers are copies (@46 = Abbasid @95, @94 = Abbasid @311, @103 = Abbasid @221), and only @48 and @75 are real. The claim that "Sector@103 sits in POLY35@116", and the S4 row that uses it, should be dropped.
- Phase 4 note "one per side unresolved": HQ246 and HQ266 are 35 m apart, both nearest CP155, so they are not a coincident pair. Both being defenders' HQs in phase 4 fits the model just as well. The phase 3 pair HQ189/HQ272 is 12 m apart and has the same ambiguity.

## MP_DUMBO
Verdict: ok

- HQ-group counts all match: HQ17 IFV1 LT1 Quad1, HQ111 IFV1, HQ93 IFV1 Quad2, HQ194 AT1, HQ24 IFV1 Quad2 HMG1, HQ123 0. Totals IFV4 Quad5 LT1 AT1 HMG1 = 12 (10 vehicle + 2 stationary), as stated.
- In-game sample: S1 had no vehicles on either side. This is formally a subset (empty) of claimed attackers HQ17 {IFV1, LT1, Quad1} and defenders HQ111 {IFV1}. It does not confirm the HQ groups. Both sides empty points to a phase-1 or random-enabler effect, not a wrong group, and it is worth flagging.
- Direction: HQ17 (211,-243), then @189 (-65,-287), @73 (-80,-352), @243 (-130,-458), then HQ123 (-230,-499). The chain mostly runs along z (north to south) as well as east to west. The order is consistent.
- Phase 2 "one per side unresolved": HQ93 and HQ194 are 55 m apart, not coincident. Both being defenders (IFV1 Quad2 AT1) fits the model equally. The data cannot resolve this.
- No contradictions between the tables.
