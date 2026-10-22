# Review B
Checked against bt-hq-groups.txt. I did not reopen the MP_*.txt files beyond what the result and the HQ file give. Geometry is from the HQ, sector and CP positions.

## MP_EASTWOOD
Verdict: minor fixes
- HQ-group counts are correct: HQ@79 has APC1, Cart2, HMG1, AT2; HQ@100 has TrHeli1, Cart2; HQ@1 has IFV1, AT1; HQ@76 has Tank1; HQ@34 has IFV1, HMG1; HQ@164 has none.
- HQ@34 appears twice, in the phase 1 attackers cell ("if used") and in the Unassigned row. Pick one. HQ@34 sits 71 m from CP65 on the east side, so it belongs with the phase 1 attackers. Corrected row: `| 1 (S182) | HQ@164 none (start); HQ@34: IFV x1, HMG x1 | HQ@79: APC x1, Cart x2, HMG x1, AT x2 | |` and `| Unassigned | | | none |`.
- The area table is stale. Its S182 row gives GolfCart x3 (@142,@177,@187), but the HQ@79 group has Cart 2. Its S151 row gives GolfCart x1, but HQ@100 has Cart 2. The 2+2 split matches the stated total of 4.
- The geometry fits east to west: S182 x=70, then S151 x=15, then S191 x=-182, with HQ@164 at x=376 and HQ@76 at x=-335. There is no sample. I agree it is low-medium confidence, because both ends have one heavy vehicle (Tank west, IFV east).

## MP_FIRESTORM
Verdict: ok
- All counts match: HQ@158 (Quad2, Fwd1, IFV1, TrHeli1, Tank1, LT2), HQ@163 (IFV1, Tank1, Fwd1), HQ@54 (Tank1, IFV2), HQ@170 none, HQ@93 and HQ@8 (IFV1, Tank1 each).
- Each HQ appears once. HQ@54 and HQ@170 are paired, 6 m apart, which is fine.
- The order fits the x positions: S103 at 48.5, S196 at -103, S216 at -297. There is no sample, so direction stays a guess. The east base is much larger (8 pads), which supports east = attackers.

## MP_OUTSKIRTS
Verdict: minor fixes
- HQ-group counts are correct: HQ@56 (Fwd2, IFV1, LT1), HQ@46 (HMG2, APC1, AT1), HQ@73 (AT1, LT2), HQ@94 (IFV1), HQ@156 (Quad1), HQ@157 (HMG1, AT1), HQ@71 (LT1, IFV1), HQ@152 none.
- The area table is stale. Its S207 row gives HMG x2 with no AT, but HQ@46 also has AT1. Its S15 row gives AT x2, but HQ@73 has AT1. The total of AT3 is right (one each at HQ@46, HQ@73 and HQ@157).
- Phase 4: HQ@71 is 92 m from S175 and the nearest sector to it is S175, not S131 (HQ@152 is 85 m from S131). Placing HQ@71 as the final defenders' HQ is still the best fit for the last phase. I agree with low confidence. No sample.

## MP_PARADISE
Verdict: minor fixes
- HQ-group counts are correct: HQ@32 (APC1, Tank1, Dirt1, LT1), HQ@28 (IFV1, APC1), HQ@47 (LT1, APC1, Fwd1, IFV1), HQ@137 (APC2, IFV1), HQ@115 (IFV1). HQ@116, HQ@8, HQ@100 and HQ@144 have none.
- Samples (3 sectors, Pax attacks):
  - Defenders S1 IFV1 is a subset of HQ@28.
  - Attackers S2 IFV1 + APC1 equals HQ@28.
  - Defenders S2 is APC1 (LTV) + IFV1, a subset of HQ@47.
  - Dropping S59 is consistent with the sample's 3 sectors.
- Wrong note in phase 2: it says the sample defenders were "LT+IFV". The sample says APC (LTV) + IFV, and the LTV is the APC class. The conclusion still holds (subset of HQ@47: APC1, IFV1). Corrected note: `Sample: attackers IFV+APC = HQ@28; defenders APC(LTV)+IFV subset of HQ@47`.
- Side label: "Attackers = team1 (Coalition)" in the prose, while the sample says Pax attacks. Write the side as Pax/team1 so it does not contradict the sample.
- Stale area-table statements:
  - S59 is listed as phase 4.
  - The HQ@47 staging block is called "likely Atk", but the HQ table uses it for phase 2 defenders and phase 3 attackers.
  - HQ@100 is listed among the S51 HQs, but it has no pads.
  - The prose order is "S27 -> S23 -> S51 -> S59".

## MP_PLAZA
Verdict: minor fixes
- HQ-group counts are correct: HQ@147 (IFV1), HQ@52 none, HQ@158 (HMG2, IFV1, AT1), HQ@31 (HMG1, AT1), HQ@10 (AT1), HQ@113 none, HQ@50 none. The totals IFV2, HMG3, AT3 check out.
- Samples: attackers S1 IFV1 equals HQ@147, and attackers S2 none equals HQ@52. Both fit.
- The area table contradicts the HQ table. Its S182 row puts IFV x1 (@112), HMG x2 and AT x1 under HQ@52, but those are the HQ@158 group, and HQ@52 has no pads. Its S56 row says "HQ@158 none". A reader would think HQ@52 holds the IFV. Corrected rows: `| 1: S182 | CP177, CP40 | HQ@52 | none | Def | Med |` and `| 2: S56 | CP162, CP90 | HQ@158 | IFV x1 (@112), HMG x2, AT x1 | Def | Low |`.
- I agree S56 at (-182.4, -3.9) is a displaced marker. It is identical to Eastwood S191. HQ@158 (y=63) between S182 (y=0) and S143 (y=145) is the only middle-phase group, which supports the assignment. The south-to-north direction fits the sample.

## MP_SUBSURFACE
Verdict: ok
- No pads; all 9 HQs are listed.
- Minor: HQ@16 is listed under S145, but its nearest sector is S147 (40 m, against 63 m for HQ@92 to S145). This has no effect on vehicles.

## MP_TUNGSTEN
Verdict: ok
- All counts match: HQ@39 (LT1, Tank1, IFV1), HQ@218 (Tank1, IFV1), HQ@116 (LT2), HQ@312 (IFV1, Tank1), HQ@110 (Tank1, IFV1), HQ@199 (Tank1, IFV1).
- The order fits the x positions: S217 at -290, S75 at -54, S139 at 97, S32 at 246. No sample. I agree the direction is a guess, but the extra LT at HQ@39 slightly favours west = attackers.
