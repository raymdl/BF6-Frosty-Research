# Review D: MP_ATOLL and MP_DRYLAKE

## MP_ATOLL (Wake Island)

Verdict: wrong (chain from phase 2 on; the counts are right)

Counts (check 1):
- Every per-phase HQ-group row matches bt-hq-groups.txt: @198 {PB 6, RHIB 9, TrHeli 2}, @347 {LT 5, RHIB 1, PB 5, IFV 1, AT 1, HMG 1}, @185, @506, @255, @120+@49 (LT 9 = 8+1, Tank 2, Quad 1, PB 3, RHIB 4, IFV 1, AA 1, AT 1), and the unassigned rows @207, @267, @38, @246/@344 (0 pads). No invented entries.

Coverage (check 2):
- All 12 HQs appear once as a group. @347, @506 and @255 each serve two phases (defenders, then attackers), which is the model. Gap: phase 2 has no defenders' HQ at all, and the model needs one.

Chain (check 3):
- Phase 1 at @198 is sound. @198 is the only group that holds sample 1 (TrHeli 2, RHIB 9, PB 4 inside PB 6, RHIB 9, TrHeli 2), and its nearest sector is @404 (686 m). Phase 1 = Sector@404 with defenders @347 (10 m from it) fits. Sample 1 is a subset (PB 4 of 6).
- Phase 3 breaks the model. The author's attackers at Sector@7 are @185 at (-327, 41). Sector@7 is at (-103, 209), and in this chain the attackers come from Sector@30 at (129, -22) in the east. That puts @185 about 230 m beyond the sector on the far (west) side, the defenders' side. @185 is also never a defenders' HQ in any earlier phase, so the attackers would gain an HQ they never captured.
- Sample 4 does not fit the claimed group. Sample 4 is Quad 1, RHIB 1, LT 3, PB 3, Tank 1, IFV 1, and @506 has no RHIB. No single HQ holds sample 4: @185 has no IFV, @255 has no boats, and @207 has no Quad or IFV. Under the brief, a set larger than the claimed group is an error, not a "matches except".
- Merge choice: Sector@30 and @404 are 95 m apart, and CP@82 (Sector@30) is 104 m from @347, so @30 and @404 are the natural merge. The chosen merge, @157 with @178, is 269 m apart. The author's own Sector@30 phase has no HQ and no pads, which also points to it being part of @404.
- A chain that fits all three samples as subsets under the model, with the same geometry inputs (still an inference, not verified in game):
  @198 -> Sector@404+@30 merged (defenders @347) -> Sector@7 (defenders @506+@185, both nearest Sector@7) -> Sector@178 (defenders @255+@207+@267, all within 46 m of Sector@178) -> Sector@157 (no HQ) -> Sector@137 (defenders @120/@49/@38).
  - Sample 3 (Tank 1, RHIB 2, PB 3, LT 3) is a subset of @506+@185 (LT 7, Tank 2, PB 10, RHIB 2, Quad 2, IFV 1). Those are the phase 3 attackers once Sector@7 has fallen.
  - Sample 4 is a subset of @255+@207+@267 (LT 9, IFV 1, Quad 1, Tank 2, RHIB 5, PB 7). Those are the phase 4 attackers once Sector@178 has fallen.
  - Weak point: going from Sector@7 (west) to Sector@178 (south-east) is a leg of about 620 m. It needs a sample from phase 2 or phase 5 to confirm.

Corrected rows (proposed):

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (Sector@404+@30) | @198: PB 6, RHIB 9, TrHeli 2 | @347: LT 5, IFV 1, PB 5, RHIB 1, AT 1, HMG 1 | sample 1 subset |
| 2 (Sector@7) | @347 | @506+@185: LT 7, Quad 2, Tank 2, IFV 1, PB 10, RHIB 2 | no sample |
| 3 (Sector@178) | @506+@185 | @255+@207+@267: LT 9, Tank 2, IFV 1, Quad 1, PB 7, RHIB 5, AT 1, HMG 1 | sample 3 subset |
| 4 (Sector@157) | @255+@207+@267 | none at Sector@157; @49 nearest on the defenders' side (low) | sample 4 subset |
| 5 (Sector@137) | @255 group (or @49 if captured) | @120+@49+@38: LT 13, Tank 2, Quad 1, IFV 1, PB 3, RHIB 4, AA 1, AT 1 | final |
| Unassigned | @246, @344 (0 pads) | | |

Stale or contradictory text (check 4):
- Lines 7, 21 and 22 still describe the west base @185 as the attackers' start, and the area table runs the chain the other way (@7 first). The HQ-group section contradicts both.
- Line 24 lists 6 PB IDs under "PB x5". The line 30 note says PB 6 + RHIB 1 = 13, but the @347 group is PB 5 + RHIB 1 + LT 5 + IFV 1 (12 vehicles). The note is area-based, it is stale, and it confuses the phase 1 defenders' count.
- Line 28 calls @198 "Unclear ... not tied to a sector", which contradicts the carrier anchor on line 36.
- Line 36 says @506 is the phase 4 match. That is false (RHIB).

Low confidence (check 5):
- The author marked the 404/30 -> 7 leg as weak. I agree, and the samples do not force it: the chain above meets all three samples without it.
- Phase 1 on @198 and the carrier reading are supported. The TrHeli pads are at y=115 against sea level 98, and @198 is the only group with TrHeli and 9 RHIB.

## MP_DRYLAKE (Area 51)

Verdict: minor fixes

- Counts (check 1): every HQ row matches bt-hq-groups.txt: @96, @46, @118, @232, @112, @42, @236, @173 and @190. All 9 HQs appear exactly once.
- Sample 1 attackers (TrHeli 1, Tank 1, APC 1, LT 2, Dirt 2) are equal to @96 minus its 4 Fwd. The east-to-west chain is forced by this sample, and the geometry agrees: @96 is at x=1088 and the HQs step west through @46 (538), @118 (352), @232 (291), @112/@173 (149-159), @42 (-23) and @236 (-261).
- Sample defenders S2 (Dirt 4, LT 1, IFV 1, TrHeli 1) are a subset of @118 (Dirt 5). They are not a subset of @173 (Dirt 3), as the author says.
- The "later sector, logged 3" sample (AtkHeli 1, Tank 1, IFV 1, LT 3, Dirt 2) is equal to @42 minus its HMG/AT emplacements. @42 at x=-23 sits west of every S3 capture point (@39 at x=60, @168 at x=53, @193 at x=178), so under the model it can only be the attackers' HQ in phase 4. The log label "3" stays unresolved. The author's reading ("3 sectors captured") is plausible, but it is an assumption that should be stated in the table note, not only in the prose.
- Phase 3 attackers: @232 (Tank 1, LT 1) sits 25 m from CP@126, which is an S2 capture point. That is consistent with it being taken at S2. But @118, the phase 2 defenders' HQ, is not carried into phase 3 attackers, though the model gives attackers the captured S2 HQs. Suggested row: phase 3 attackers @118+@232 (LT 4, AtkHeli 1, Dirt 5, TrHeli 1, IFV 1, Tank 1), low confidence, no sample.
- Stale text (check 4): line 51 (west-to-east, "attackers start at the west base"), the area table's "Likely side" column (W base = attackers, S1 = Area A at CP@66) and the line 56 anomaly are all reversed by the HQ section. A reader of the first table gets the opposite sides.
- Low confidence (check 5): the B+C merge is not needed for the HQ table, which uses its own 4 sectors from the CP clusters, so that caveat is stale. The remaining low item is @190 at z=1152, off the axis. I agree it fits no phase. Its nearest CP is @126 at 140 m, so it may be a second S2 defenders' group, but no sample tests it.
