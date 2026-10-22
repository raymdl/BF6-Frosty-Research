# Review of result-Escalation.md (Escalation, build 2.1.1.0)

Method: parsed extraction\Escalation-maps.txt and recomputed by script (python -I; scripts esc_review.py, esc_verify.py, esc_v2.py, esc_alt.py, esc_axis.py in the session scratchpad). The script re-derived, for all 11 maps: gem counts, initial HQ positions and separation, every capture point position, dW/dE distance, nearest Sector and distance, both removal orders, all "alternate HQ" orders, top-3 overlap, vehicle pad totals per class, the distance and nearest anchor of every listed Battle_Pickup, StationarySpawner, AutomaticAA, resupply station and Collection_Event, and the "flags with no outline within 15 m" lists. Tweakables were checked against existing-tweakables.txt (MUT_Escalation, lines 106-151). ui-text.txt, objective-table.json and map-names.json are not in the extraction folder, so the UI-text quotes in section 1.1 and the map names that README-modes.md does not list (Siege of Cairo, Liberation Peak, Manhattan Bridge, Eastwood, Operation Firestorm, New Sobek City, Mirak Valley) could not be verified here.

## Summary

Tally: ok 5, minor fixes 6, wrong 0.
- ok: Siege of Cairo, Liberation Peak, Eastwood, Operation Firestorm, Mirak Valley.
- minor fixes: Wake Island, Iberian Offensive, Contaminated, Manhattan Bridge, Tsuru Reef, New Sobek City.

No miscounted capture point, HQ, sector, pad class, distance or removal order was found. Every number in the 11 map sections and the cross-map table reproduces exactly (counts of CapturePoint 7/7/7/7/7/7/7/7/9/7/7, HQ 6 each, pad totals 24/59/8/36/38/32/53/54/47/39/62, all dW/dE values, all orders, all three "OVERLAP" verdicts). The faults are in how pad ownership and the HQ roles are described, not in the data.

Single most important correction: the pad-ownership rule in section 2 ("nearest of the 2 initial HQs and the 7 flags; HQ-W/HQ-E absorb their flag-side HQs") is not what the per-map tables do. The tables use the nearest of ALL 6 HQs plus the flags, and then merge into HQ-W/HQ-E only those HQs listed as "W-cluster/E-cluster". Consequences: the "flags" column of the cross-map table contains pads that sit at flag-side HQs (Wake Island 22 of 25, Tsuru Reef 14 of 23, Operation Firestorm 3 of 10, Liberation Peak 2 of 6, Manhattan Bridge 1 of 5), Tsuru Reef has 9 flags not 7, and Manhattan Bridge shows 14/13/5 where the stated rule gives 13/13/6. Second correction: in section 2 "the other 4 HQ instances sit at flags" is false for Iberian Offensive, where HQ@73, HQ@76 and HQ@102 are three HQs stacked at the same point [920.1, 74.8, 134.5].

## Siege of Cairo (MP_ABBASID)

Verdict: ok.
- All recounted values match: CapturePoint 7, HQ 6, Sector 7 (bijective with the flags, 3 to 26 m), pads 24 (IFV 4, LightTransport 8, PTV_QuadBike 8, Tank 4), HQ-W 10 / HQ-E 10 / flags 4. W order 132(75) > 243(124) > 30(140) > 45(217) > 81(316) > 217(334) > 151(400); E order 151(64) > 217(151) > 81(162) > 45(248) > 30(343) > 243(365) > 132(390). Overlap none confirmed. Alternate-HQ orders confirmed.
- Geometry: flags project onto the W-E axis at t = 0.16 to 0.86, lateral offsets 1 to 65 m, so the layout is a plain line between the bases and the dW order equals the axis order (132, 243, 30, 45, 81, 217, 151 within the lateral scatter). Consistent.
- Contradiction: "CapturePoint_OutlineArea: 7 for 7 flags (flags with no outline within 15 m: [132])". Seven outline instances exist but CP@132 has none within 15 m, so one outline is not on a flag. Reword to "7 outlines, 6 flags matched within 15 m".
- The nearest flags to the initial HQs are 75 m (W) and 64 m (E), which contradicts section 2 "no flag within about 100+ m" (see cross-map section).
- Low-confidence inference (initial pair, high stated): sound. The pair is 464 m apart, each has 8 Insertions and 10 pads, and the two alternate clusters (HQ@12, HQ@172 / HQ@115, HQ@124) give the same orders.

## Wake Island (MP_ATOLL)

Verdict: minor fixes.
- Counts match: CapturePoint 7, HQ 6, Sector 5, pads 59 (PatrolBoat 21, Tank 6, LightTransport 6, MultirolePlane 4, NavalFighterPlane 4, TransportHelicopter 4, PTV_QuadBike 4, IFV 4, AttackHelicopter 2, MobileAA 2, RHIB 2). Orders and overlap {26} confirmed (W top3 28, 26, 137; E top3 26, 117, 59).
- "Capture points (ordered W to E)" is false for this map: the listed order 28, 137, 36, 59, 100, 26, 117 is neither by x nor by dW (604, 930, 1118, 939, 1202, 909, 1155). Say "in file order" or sort by dW.
- Geometry: the farthest-apart HQ pair (HQ@67, HQ@32, 1308 m) does not lie along the flags. Projected on the HQ@67 to HQ@32 axis, all 7 flags have a lateral offset of 295 to 889 m (t 0.39 to 0.79). The flags form one cluster in the east of the island, the "initial" HQs are far west and far south. This supports the low confidence the author states; it is more than "low", it is geometrically odd.
- Sector check: 5 sectors for 7 flags. Sector@44, @101, @114, @136, @138 pair with CP@28 (126 m), CP@117 (12 m), CP@137 (67 m), CP@26 (16 m), CP@100 (120 m). CP@36 (229 m) and CP@59 (164 m) have no sector of their own; Sector@138 is the nearest of three flags (100, 59, 36). Author's statement is correct.
- Inference test for the base question (O8). The two land groups are mirror images (11 pads each: IFV 2, LightTransport 3, MobileAA 1, PTV_QuadBike 2, Tank 3) at HQ@55 and HQ@2, and the air/boat groups are mirror images (17 pads each) at HQ@67 and HQ@32. Both pairs are symmetric, so the data cannot say which pair is the starting base. What the author left unsaid: the first removal is robust. With HQ@55 as W base the order is 28(22) > 59(355) > 26(373) > 137(426) > 117 > 36 > 100; with HQ@2 as E base it is 26(3) > 117(273) > 59(286) > 28(353) > 100 > 137 > 36. First removal is CP@28 (W) and CP@26 (E) under both hypotheses. Under the land-base hypothesis the top-3 overlap becomes {26, 59} (W 28, 59, 26; E 26, 117, 59), not {26}.
- The sentence in section 4 "Orders from nearby alternate HQ instances:  | " is empty for this map; the data does give HQ@2, @16, @40, @55 orders (above). Not stale, but the empty field should be dropped or filled.
- Corrected row (strict rule: 2 initial HQs + 7 flags): HQ-W 17 / HQ-E 17 / flags 25 (CP@26 11, CP@28 11, CP@59 3). Same numbers; the anchors are flags, not HQ@2 / HQ@55. CP@59's 3 pads are boats (PatrolBoat 1, RHIB 2).

## Iberian Offensive (MP_BATTERY)

Verdict: minor fixes.
- Counts match: CapturePoint 7, HQ 6, Sector 7 (bijective, 5 to 38 m), pads 8 (IFV 2, LightTransport 4, Tank 2), VehicleSpawner_Forward 3, no air. Orders W 43(111) > 58(130) > 101(160) > 52(198) > 30(208) > 62(287) > 39(311), E 62(85) > 39(89) > 30(143) > 52(165) > 101(202) > 58(217) > 43(288). Overlap none confirmed.
- Error in the HQ description: HQ@73, HQ@76 and HQ@102 share the identical position [920.1, 74.8, 134.5], so the E base has three HQ instances and the W base one (HQ@23) plus two flag-side HQs (HQ@48 40 m from CP@43, HQ@85 34 m from CP@43). The "Other HQ instances" line gives "HQ@76 near CP@62 (85 m)" and "HQ@102 near CP@62 (85 m)" as if they were flag-side; 85 m is simply the distance of the initial E HQ from CP@62. Correct text: HQ@76 and HQ@102 are duplicates of HQ@73; there is no flag-side HQ on the E side. O5 notes the stacking but section 2 ("the other 4 HQ instances sit at flags") and the cluster notation contradict it.
- The pads (4 and 4) and the 3 Forward spawners (all at the W base: 4, 9, 10 m from HQ@23) make the base asymmetric; the W base alone holds the Forward spawners. O5/O6 state this. Fine.
- Collection_Event "(HQ-W 587 m)" is correct but meaningless (object at 0,0,0). Leave.
- Initial pair confidence "high" is sound: 345 m apart, the only candidate with pads (4 each). The E initial HQ is 85 m from CP@62 and 89 m from CP@39 (section 2 says no flag within about 100+ m; wrong).
- Corrected row: unchanged (4 / 4 / 0, total 8).

## Liberation Peak (MP_CAPSTONE)

Verdict: ok.
- All counts match: CapturePoint 7, HQ 6, Sector 7 (6 to 25 m, bijective), TelemetryArea 13, outlines 3, pads 36 (LightTransport 14, AttackHelicopter 2, AttackPlane 2, FighterPlane 2, IFV 4, PTV_DirtBike 4, PTV_QuadBike 4, Tank 4). Orders and overlap none confirmed. No Insertion instances on this map.
- The cross-map "flags 6" counts CP@28, CP@137, CP@149, CP@155 (1 LightTransport each) plus HQ@39 and HQ@103 (1 LightTransport each). Under the stated rule these two pads belong to CP@9 (41 m from HQ@39) and CP@124 (6 m from HQ@103): six flags, same total, so the number is right, the per-anchor list is not (see cross-map section).
- Geometry: axis t 0.25 to 0.75, lateral up to 271 m (CP@29, CP@28 at -187 to -271). Consistent with a wide map; dW order matches.
- Inference (initial pair high): sound; 684 m apart, air pads present at both, 15 pads each.

## Contaminated (MP_CONTAMINATED)

Verdict: minor fixes.
- Counts match: CapturePoint 7, HQ 6, Sector 7, pads 38 (PTV_DirtBike 12, LightTransport 6, ScoutHelicopter 4, Tank 4, IFV 4, AttackHelicopter 2, AttackPlane 2, FighterPlane 2, MobileAA 2), HQ-W 16 / HQ-E 17 / flags 5. Orders and overlap none confirmed; W-cluster HQ@91 order confirmed.
- Listing order "ordered W to E" is not monotone (dW 151, 248, 298, 507, 448, 533, 564). Cosmetic.
- Error: StationarySpawner @238 is labelled "(HQ-W 19 m)". It is 19 m from HQ@91 [-103.7, -150.0] (a W-cluster HQ), and 103 m from the initial W HQ@114. Label it HQ@91, or use 103 m. (The other labelled distances all reproduce.)
- Sector note is sound but incomplete. Six of the 7 sectors sit at y = 64.3 while flags are at y = 300 to 334; Sector@6 [193.3, 342, 37] is the only one at flag height and is 78 m from CP@231, 110 m from CP@111, which the author never uses (the author picks Sector@101 13 m from CP@231 in 2D). Three flags (89, 212, 41, nearest Sector@220 at 153, 182, 31 m) share one sector in 2D. The author's call that distance matching is unreliable here is correct.
- SpecialCombatArea POLY@43 bbox [-383, -396, 604, 523] contains all 7 flags (43 appears in every flag's polys): this one does look like the play-area bound. Unlike Eastwood, Firestorm and New Sobek City (below).
- Corrected row: unchanged (16 / 17 / 5, total 38).

## Manhattan Bridge (MP_DUMBO)

Verdict: minor fixes.
- Counts match: CapturePoint 7, HQ 6, Sector 7 (0 to 5 m, bijective), pads 32. Orders W 49(136) > 62(141) > 167(235) > 111(239) > 15(294) > 19(355) > 165(373), E 165(136) > 19(142) > 15(218) > 111(243) > 167(292) > 62(345) > 49(375). Overlap none confirmed. The initial pair is symmetric (136 m to the nearest flag on both sides).
- Pad split inconsistent with the stated rule. The table gives HQ-W 14 / HQ-E 13 / flags 5. HQ-W 14 includes HQ@153's LightTransport (HQ@153 is 96 m from HQ@12 and is listed as a W-cluster HQ), while HQ@110's PTV_QuadBike (a flag-side HQ at CP@19) is kept separate, and HQ@145's pad is shown under CP@62. Under the rule of section 2 (2 initial HQs + 7 flags): HQ-W 13 / HQ-E 13 / flags 6 (CP@111 2 PTV_QuadBike, CP@165 1 LightTransport, CP@19 1 PTV_QuadBike, CP@49 1 LightTransport, CP@62 1 PTV_QuadBike). Both bases identical: AttackHelicopter 1, IFV 2, LightTransport 4, MobileAA 1, PTV_QuadBike 2, ScoutHelicopter 1, Tank 2 (13 each). The table row should be 13 / 13 / 6; the asymmetric 14 / 13 comes from the cluster merge, not from the map.
- Geometry: the layout is a double loop (lateral +86 to -107 m) rather than a line; dW order still matches distance order. The vehicle OOB note (MP_Dumbo_VehicleOOBtime = 10 [1..15]) is correct.
- Inference (initial pair high): sound; 482 m apart, 13 pads each, 8 Insertions each.

## Eastwood (MP_EASTWOOD)

Verdict: ok.
- All counts match: CapturePoint 7, HQ 6, Sector 7 (4 to 55 m, bijective), pads 53 (LightTransport 14, PTV_QuadBike 8, PTV_GolfCart 7, Tank 6, APC 4, IFV 4, MobileAA 4, AttackHelicopter 2, ScoutHelicopter 2, TransportHelicopter 2), HQ-W 20 / HQ-E 20 / flags 13 (CP@152 4 PTV_GolfCart, CP@168 3, CP@103 2, four CPs with 1 LightTransport). Orders and overlap none confirmed; E-cluster HQ@186 order confirmed.
- factionOverrides team1 = NATO, team2 = Pax Armata: confirmed, the only layer with this reversal.
- SpecialCombatArea@199: POLY@22 bbox [-66, -160, 279, 326] contains only CP@282, CP@152, CP@302 (22 in their polys); the other 4 flags, both initial HQs and the 8-Insertion clusters are outside. It cannot be the play-area limit, so it should not be described under "Combat area" without saying so. O13 does not claim it is, but a reader will assume it.
- Inference (initial pair high): sound (829 m).

## Operation Firestorm (MP_FIRESTORM)

Verdict: ok.
- All counts match: CapturePoint 7, HQ 6, Sector 7 (5 to 15 m, bijective), VehicleResupplyStation 10, AutomaticAA 4, pads 54 (PTV_DirtBike 14, LightTransport 12, IFV 8, Tank 6, MobileAA 4, six other classes 2 each), HQ-W 22 / HQ-E 22 / flags 10. Orders and overlap none confirmed.
- "flags 10" includes 3 pads sitting at HQ@106, HQ@255 and HQ@318 (flag-side HQs, 37 to 39 m from CP@222 and CP@64). Under the rule of section 2 the flags hold: CP@222 2, CP@23 2, CP@300 2, CP@64 2, CP@266 1, CP@36 1 = 10. Same total.
- Resupply stations: the listing shows @220 VehicleResupplyStation_Air "(HQ-W 174 m)" and @250 "(HQ-E 139 m)". Distances reproduce.
- SpecialCombatArea@229 at [0, 0, 0] with POLY@89 bbox [-375, -350, 197, 289]: only CP@36, CP@103, CP@266 carry polygon 89. Four flags (222, 300, 23, 64) and both initial HQs are outside, so this is a partial zone, not the map boundary. Same remark as Eastwood.
- Inference (initial pair high): sound (1389 m apart, 22 pads each).

## Tsuru Reef (MP_ISOLATED)

Verdict: minor fixes.
- Counts match: CapturePoint 9, HQ 6, Sector 5, pads 47 (RHIB 12, PTV_QuadBike 6, PatrolBoat 6, IFV 4, Tank 4, TransportHelicopter 4, PTV_DirtBike 4, LightTransport 2, AttackPlane 2, FighterPlane 2, APC 1), no insertions, no Battle_Pickup, no outlines. Removal orders W 55 > 56 > 22 > 24 > 27 > 26 > 87(1164) > 16(1166) > 74; E 74 > 87 > 16 > 26 > 27 > 24 > 56 > 22 > 55. Overlap none confirmed.
- Wording errors: section 2 says pads go to "the 7 flags"; here there are 9. The cross-map "flags 23" is not 23 pads at flags: only 9 are (CP@16 1, CP@24 3, CP@26 2, CP@27 1, CP@56 1, CP@74 1) at flags in the author's table, and 14 sit at flag-side HQs (HQ@96 6, HQ@75 4, HQ@54 2, HQ@9 2). Under the stated rule (flags only): CP@55 6, CP@74 5, CP@24 3, CP@22 2, CP@26 2, CP@87 2, CP@16 1, CP@27 1, CP@56 1 = 23. Total correct, the labelled breakdown is not.
- Sector check: 5 sectors, 9 flags. Sector@101 (-917, 66) is the nearest of CP@26, CP@27 and CP@24 (137, 157, 179 m); Sector@98 is nearest for CP@55 (27 m) and CP@56 (167 m); Sector@5 for CP@74 and CP@16 (31, 238 m). No sector within 100 m of CP@16, CP@24, CP@26, CP@27, CP@56. Author's "some sectors cover several flags" is correct.
- Inference test for the base question (O9): the alternative base pair HQ@96 (on CP@55) and HQ@75 gives W order 55 > 56 > 22 and E order 74 > 87 > 16, identical top-3 to the author's, so the removal prediction is robust whichever HQs are the real bases. The land hubs are not symmetric (HQ@96: APC 1, IFV 2, Tank 2, PTV_DirtBike 1; HQ@75: IFV 2, Tank 2), whereas the air/boat hubs at HQ@94 and HQ@21 are exact mirrors (12 each). Flags lie 20 to 287 m off the HQ@94-HQ@21 axis, so this map is consistent with the pair.
- With 9 flags, 3 + 2 removals leave 4, not 2 (section 1.1 states "2 flags always remain" for 7 flags only; add the Tsuru exception).

## New Sobek City (MP_OUTSKIRTS)

Verdict: minor fixes.
- Counts match: CapturePoint 7, HQ 6, Sector 7 (0 to 36 m, bijective), pads 39 (LightTransport 11, IFV 6, PTV_QuadBike 6, Tank 4, PTV_DirtBike 4, six singles/doubles), HQ-W 17 / HQ-E 17 / flags 5 (LightTransport at CP@54, 93, 148, 199, 200). Orders confirmed. Overlap {165} confirmed for HQ@191 and HQ@140.
- The overlap verdict depends on which HQ of the base pair is the initial one. With W-cluster HQ@167 (which the author lists) W top3 becomes 54 > 200 > 127 and the overlap with E top3 (93, 199, 165) is empty; with HQ@44 it is 54, 165, 200. The result states this in O7 but section 4 and the cross-map text give only "OVERLAP {165}". Also a refinement for all maps: with a 3 + 2 split, the loser removes only 2 flags. {165} can only be contested if E wins 3 (E top3 93, 199, 165 against W top2 54, 165); if W wins 3 (54, 165, 200) against E top2 (93, 199) there is no clash. Same for Wake Island: the loser's top 2 (E: 26, 117 or W: 28, 26) still contains 26 in both directions, so Wake's clash is real either way.
- Two HQs per base (HQ@191 / HQ@44 on W, 50 m apart; HQ@140 / HQ@201 on E, 61 m apart) is correctly flagged as medium confidence.
- SpecialCombatArea@212: POLY@56 bbox [-113, -221, 65, -3] contains CP@127, CP@165, CP@148 only; CP@54, CP@200, CP@93, CP@199 and both HQ pairs are outside (O13 statement confirmed). It is again a partial zone.
- Corrected row: unchanged (17 / 17 / 5, total 39). Medium confidence on the initial pair is sound.

## Mirak Valley (MP_TUNGSTEN)

Verdict: ok.
- All counts match: CapturePoint 7, HQ 6, Sector 7 (17 to 48 m, bijective), pads 62 (LightTransport 16, IFV 8, Tank 8, AttackHelicopter 4, AttackPlane 4, FighterPlane 4, MobileAA 4, PTV_DirtBike 4, PTV_QuadBike 4, TransportHelicopter 4, ScoutHelicopter 2), HQ-W 27 / HQ-E 27 / flags 8 (CP@237 2, six CPs 1 each; one LightTransport each). Orders and overlap none confirmed.
- Two SpecialCombatArea polygons: POLY@219 bbox [-1229, -1434, 1229, 614] contains all 7 flags and both HQs (it is the only one that looks like the real bound); POLY@145 bbox [-149, -582, 241, 37] covers the centre flags only. O13 lists the layer but not that these are different.
- Inference (initial pair high): sound (1000 m, 27 pads each, all classes mirrored).

## Railway to Golmud, Area 51, Vegas Strip (non-full layers)

- Golmud: confirmed, 1 CapturePoint @4 at [-64.5, 738.6, 852.8] in `Escalation_Global` (gem counts CapturePoint 1). The text mentions only BOX@1; the file lists seven boxes (BOX@1, 2, 3, 5, 6, 7, 8), none of which contains the point (all contains=[]). Add this. factionOverrides team1 = Pax Armata confirmed. Golmud_Escalation_EnableMovingTrain = true confirmed.
- Area 51 and Vegas Strip: empty gem counts confirmed (both also carry the same team1 = Pax Armata override, which the result does not mention; irrelevant).
- Empire State, Blackwell Fields, Saints Quarter, Cairo Bazaar, Hagental Base absent from the file: confirmed (14 map blocks: 11 full, Golmud stub, 2 empty).

## Cross-map table and rules corrections

1. Table column "Pads per side (nearest anchor)": rename the third value from "flags N" to "other anchors N" or recompute strictly. Strict values (2 initial HQs + all flags, no merging): Siege 10/10/4, Wake 17/17/25, Iberian 4/4/0, Liberation Peak 15/15/6, Contaminated 16/17/5, Manhattan Bridge 13/13/6 (author 14/13/5), Eastwood 20/20/13, Firestorm 22/22/10, Tsuru Reef 12/12/23, New Sobek City 17/17/5, Mirak Valley 27/27/8. Only Manhattan Bridge changes. All totals unchanged.
2. Section 2 pad rule, replace with what the tables do: "nearest of all 6 HQs and the flags (7, or 9 on Tsuru Reef); HQs within about 110 m of an initial HQ that are listed as W-/E-cluster are merged into it." The per-map anchor lists of Liberation Peak (HQ@39, HQ@103), Operation Firestorm (HQ@106, HQ@255, HQ@318), Manhattan Bridge (HQ@110), Wake Island (HQ@2, HQ@55) and Tsuru Reef (HQ@9, @54, @75, @96) show non-merged flag-side HQs, which is consistent with that rule and not with the current text. Tie handling: where a flag-side HQ sits on a flag (Manhattan HQ@145 on CP@62, 0 m; Wake HQ@2 on CP@26, 3 m), the flag wins.
3. Section 2: "each has a cluster of 8 Insertions" holds on 7 maps only (Siege, Contaminated, Manhattan, Eastwood, Firestorm, New Sobek City, Mirak). There are no Insertion instances on Wake Island, Iberian Offensive, Liberation Peak or Tsuru Reef. "4-27 vehicle pads" is correct (Iberian 4, Mirak 27, on the initial HQs).
4. Section 2: "no flag within about 100+ m" is false. Nearest flag to the initial HQs: Siege 75 / 64 m, Iberian 111 / 85 m, New Sobek City 122 / 103 m, Manhattan 136 / 136 m, Contaminated 151 / 193 m, Mirak 166 / 182 m, Liberation Peak 172 / 169 m, Eastwood 250 / 181 m, Firestorm 330 / 259 m, Tsuru 437 / 430 m, Wake 604 / 537 m. Replace with "64 m to 604 m (Siege of Cairo is the closest at 64 / 75 m)".
5. Section 2: "The other 4 HQ instances sit at flags" is false for Iberian Offensive (two are duplicates of the E initial HQ) and loose for Tsuru Reef HQ@75 (194 m from any flag, as O9 says) and Eastwood HQ@186 (85 m). Rephrase as "near flags (0 to 86 m, except Tsuru Reef HQ@75 194 m)" and note the Iberian duplicates.
6. "Capture points (ordered W to E)" (all map sections): the list is approximately dW order, not x order and not exactly dW order on Wake Island, Contaminated, Mirak Valley, Eastwood, Firestorm, Tsuru Reef. Rename to "in order of distance from HQ W (approx.)" or sort.
7. Overlap check: top-3 of both sides is a conservative stand-in. Max 5 removals come as 3 (winner) + 2 (loser), so compare winner top-3 with loser top-2; refine per direction. Verdicts stay: Wake clash on CP@26 in both directions (and CP@59 as well under the land-base hypothesis); New Sobek City clash on CP@165 only if E wins; all others no clash.
8. Section 1.1: "2 flags always remain" holds for 7 flags; Tsuru Reef (9 flags) leaves 4. The statement "(confirmed: the team that takes territory loses the flag nearest ITS OWN initial HQ...)" overstates: the UI sentence is quoted as "closest to your initial HQ" and the round graph that selects the flag is unreadable (O3); the reading "taker's own HQ" is an inference, medium confidence.
9. Sources: section 1.2 attributes the ESC_ values to Escalation-tweakables.txt, but that file only holds the null-valued logic variables (LaunchParameters, stalemate provider, GemCollectionFilter, Leadership_ViewModel). All 41 ESC_ values and the 4 class flags are in existing-tweakables.txt (MUT_Escalation, 45 tweakables). I checked every value quoted in the result against it: all match, including ESC_f[]PhaseLengths = [90.0, 162.0, 252.0, 3600.0], ESC_f[]CaptureSpeedMultipliers = [0.0, 1.0, 1.333, 1.666, 2.0], ESC_iPhaseAmount = 5 [0..9], ESC_fProgressResetDelayOnTerritoryTaken = 6.0 [0.0..10.0], ESC_AwardSuccessfulRetreat = true. Per-map MUT values (MP_Dumbo_VehicleOOBtime = 10 [1..15], SpawnPreventionRadius_Small = 40 for Abbasid, SpawnPreventionRadius_LargeModes_Battery = 45, Golmud flags) match maps-tweakables.txt; the "may apply" for the spawn radii is correctly hedged.
10. Combat area (O13): add that SpecialCombatArea on Eastwood (3 of 7 flags inside), Operation Firestorm (3 of 7) and New Sobek City (3 of 7) is a partial zone, while Contaminated POLY@43 and Mirak Valley POLY@219 contain all 7 flags and look like the map bound.
11. Inference of which team is where (factionOverrides): confirmed per layer. team1 = Pax Armata on Siege of Cairo, Iberian Offensive, Operation Firestorm, Tsuru Reef, Golmud stub, Area 51, Vegas Strip; team1 = NATO on Eastwood; default (empty) on Wake Island, Liberation Peak, Contaminated, Manhattan Bridge, New Sobek City, Mirak Valley.

## Stale statements

- Section 4, Wake Island and Tsuru Reef: "Orders from nearby alternate HQ instances:  | " is an empty field; the data has alternates (Wake HQ@2, @16, @40, @55; Tsuru HQ@9, @54, @75, @96) and the text elsewhere (O8, O9) already discusses them. Fill or delete.
- Section 2 pad rule ("the 7 flags") and the "8 Insertions" and "100+ m" statements date from the first capture (8 maps, mostly mainland layouts); the island layers added by the second capture (Wake Island, Tsuru Reef) and Contaminated break them (9 flags, no Insertions, base-to-flag distances up to 604 m).
- Section 3 note and the "flags" column header: written for the first-capture maps where flag-side HQs had no pads; the second-capture islands put up to 22 land pads at flag-side HQs, so "flags" no longer means flags.
- Section 0 mentions "BOX@1" for Golmud only; the file has seven boxes.
- Section 1.1 "With 7 flags ... 2 flags always remain" has not been updated for Tsuru Reef's 9 flags.
- No stale map counts remain: the 11-map scope, the 8 + 3 split, the empty Area 51 / Vegas Strip blocks, the O14 outline counts (7, 5, 4, 3, 3, 2, 1, 1, none on Wake Island, Tsuru Reef, Mirak Valley) and the Collection_Event list (8 maps) all match the file. No "Armada" and no em-dash occurs in the result.
