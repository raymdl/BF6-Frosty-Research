# Review of result-Conquest.md (build 2.1.1.0, Season 5)

Reviewer: Sonnet 5.5 subagent. Method: Python (`python -I`) scripts in the session scratchpad (cqparse.py, t2.py to t23.py) re-parsed `extraction\Conquest-maps.txt` (18 map blocks, 1,837 lines; every instance line and every BOX/POLY line) and `existing-tweakables.txt` (the MUT_Conquest block). I regenerated, in the author's own line format, every flag line (position, t, off-axis, OutlineArea attribution), the pad totals, the per-anchor pad groups with distances, the forward/stationary/AutomaticAA/resupply groups, the Air pads lines, the HQ lines, the SpecialCombatArea polygon lists, the largest-polygon picks, the Battle_Pickup and PsyGasZone lines, the Other lines, the GEM counts, factionOverrides and asset lists, and all 18 cross-map table rows, then compared them to the result text. Result files and GAME_MODES were not edited.

## Header summary

- Tally: **ok 2** (Blackwell Fields, Hagental Base), **minor fixes 16**, **wrong 0**. The extraction holds 19 map ids (Gameplay-maps.txt) and 18 have a Conquest0 layer (Saints Quarter has none, confirmed). It does not contain 21 maps; if the brief's 21 is a count of playable maps, 2 are in no extraction file.
- Counts are right. All 18 sections' flag, HQ, pad (per class and per nearest anchor), forward, stationary, AutomaticAA, resupply, Air, Battle_Pickup, PsyGasZone, TelemetryArea, GEM-count, faction and asset lines reproduce exactly, and all 18 cross-map table rows reproduce. All 59 MUT_Conquest rows match the source values and ranges except one malformed row (below).
- **Single most important correction:** every "distance median" in the per-anchor pad lines is the upper-middle value for groups with an even number of pads (Python `median_high`), not the median. 38 of 100 groups differ after rounding, and for 2-pad groups the "median" simply equals the max. Examples: Eastwood flag B 134 m (true 99), Siege of Cairo HQ-E 52 m (true 36), Railway to Golmud flag B 123 m (true 81), Tsuru Reef flag D 104 m (true 74), Mirak Valley flag A 48 m (true 31). Corrected rows are in each map section.
- Other corrections worth applying: (1) the "Conquest_Team1/Conquest_Team2 exist as assets" boilerplate is false for Siege of Cairo, Iberian Offensive and Contaminated; (2) Empire State's unresolved third HQ can be resolved from Insertion data; (3) the "inferred play area" from the largest polygon contains neither HQ on Siege of Cairo, Wake Island and Hagental Base, so it is the objective area, not a play area; (4) the fixed-wing pads (AttackPlane, FighterPlane) counted under "near HQ" are 284 to 1188 m from the HQ and outside its spawn polygon on four maps; (5) Contaminated flag A is credited with 6 OutlineAreas that are not its own; (6) the CaptureSpeedMultipliers rule row is malformed.

## Evidence used repeatedly (computed, all maps)

- E1 Insertions: every map has 16 Insertion instances, and nearest-HQ assignment gives exactly 8 to each HQ on all 18 maps (Empire State: 8 to @162, 8 to @97, 0 to @154; max Insertion to HQ distance 19 to 89 m). Strong evidence that the two HQs are the two spawn sides and that a 3rd HQ is not a spawn.
- E2 Spawn polygons: for every pad that lies inside an HQ-private polygon (a polygon in that HQ's polys list but not in the other's), the nearest-HQ rule assigns it to that same HQ. 0 disagreements across 478 pads (agreements per map: Siege of Cairo 4, Wake Island 22, Blackwell Fields 22, Iberian Offensive 6, Liberation Peak 16, Contaminated 20, Area 51 26, Manhattan Bridge 12, Eastwood 20, Operation Firestorm 30, Railway to Golmud 40, Tsuru Reef 16, New Sobek City 18, Vegas Strip 22, Cairo Bazaar 4, Mirak Valley 32). So the mirrored-HQ-pad inference is better than MEDIUM for pads inside the HQ polygon (HIGH), and the only weak part is the far fixed-wing pads (E3).
- E3 Pads assigned to an HQ by distance but outside every HQ-private polygon: only AttackPlane/FighterPlane pads. Liberation Peak 4 (495 to 547 m), Area 51 6 (820 to 844 m), Railway to Golmud 2 (1136, 1188 m), Tsuru Reef 4 (284 to 438 m). No flag-assigned pad lies inside an HQ polygon.
- E4 Flag order robustness: ordering flags by projection t (the author's method) and by (distance to HQ-W minus distance to HQ-E) agree on 17 of 18 maps. They differ only on Wake Island (E and F swap). A third ordering (distance to HQ-W alone) differs on Wake Island, Liberation Peak (C/D), Area 51 (D after F), Railway to Golmud (E/F), New Sobek City (A/B), Cairo Bazaar, Mirak Valley (C/D swap), so those are the maps where letters depend on the metric. Letters are never stored, so "consistent with geometry" can only mean this.
- E5 Sector marker: position (-8.3, 64.3, 61.0) on Wake Island, Liberation Peak, Contaminated, Eastwood, Operation Firestorm, Hagental Base (and (-8.2, 64.3, 61.0) on Cairo Bazaar, (-8.3, 77.7, 61.0) on Blackwell Fields), so it is a default placement with no geometry on 8 maps. Collection_Event is (0,0,0) on all 11 (confirmed). Only 10 maps have a unique Sector position.

## Per-map sections

Format per map: Verdict, findings with numbers, corrected rows. "Recount" means regenerated by script; where nothing is listed as wrong, the author's number equals mine.

### Siege of Cairo (MP_ABBASID)
- Verdict: minor fixes.
- Recount: 5 flags, 2 HQs, 4 pads (IFV 2, Tank 2), HQ-W 2 / HQ-E 2 / flags 0; forward 4 (W 2, E 2); resupply 4 (HQ-W, HQ-E, flag B, flag E); 6 OutlineAreas; Battle_Pickup 2. All match.
- Flag order: t A .29, B .30, C .51, D .72, E .73. A/B and D/E are ties (0.01 apart; dW 122 vs 142, dE 124 vs 122), so A/B and D/E letters are arbitrary; C is the bisector flag (214 m to HQ-W, 207 m to HQ-E). Projection and hyperbolic orders agree (ABCDE). Consistent, MEDIUM is fair for the C-centred three-tier structure {A,B} / C / {D,E}.
- Wrong: "Conquest_Team1/Conquest_Team2 exist as assets" - the asset list has neither.
- Inferred play area @169 [-253,-128,88,130] holds 0 of 2 HQs and 0 of 4 pads (HQ-W x=-276, HQ-E x=122); it is the flag area. Keep LOW, but do not call it a play area.
- Forward spawners are 47 to 53 m from HQ-W and 21 to 33 m from HQ-E. Sector (-237,-59) is 67 m from flag B, meaningless as a chain.
- Corrected rows: `near HQ-W: 2 pads (IFV 1, Tank 1); distance median 27 m, max 28 m` and `near HQ-E: 2 pads (IFV 1, Tank 1); distance median 36 m, max 52 m`.

### Empire State (MP_AFTERMATH)
- Verdict: minor fixes.
- Recount: 5 flags, 3 HQs, 0 pads, 6 HMG (HQ-1 2, HQ-3 1, flag C 2, flag E 1), 8 TelemetryAreas, 1 OutlineArea (flag E). All match.
- Open question 2 can be resolved: E1 shows 8 Insertions at @162 (polygon 94) and 8 at @97 (polygon 142), none at @154 or in its polygon 170 (the main area polygon). @154 (-555,-142) is 16 m from flag A (@23), 120 m from @162, and has no HMG assigned by nearest anchor. Treat @162 and @97 as the live spawn HQs (MEDIUM-HIGH) and @154 as a non-spawn marker (possibly a stand-in for the Winter_Conquest0 layout; that asset is undecoded). The axis is unchanged because @162 and @97 are also the lowest- and highest-x HQs, so every t value stays valid.
- Flag order: ABCDE by both metrics; B is the bisector flag (133/145). Off-axis E 113 m is 0.46 of the 246 m axis, so the HQ-line projection is the weakest here among small maps; A (t .29) sits 16 m from the spare HQ, so do not use A as "first flag of the HQ-1 side" without the caveat.
- "HQ-1(lowest x)/HQ-2/HQ-3" labels in the by-anchor line are fine but HQ-2 can be dropped from anchors once it is declared a marker (no pad or emplacement changes: nothing was assigned to it).
- Corrected cross-map row: `Empire State | 5 | 3 (2 live spawns + 1 non-spawn marker) | 0 / 0 / 0 | 0 | 1200 | no`.

### Wake Island (MP_ATOLL)
- Verdict: minor fixes.
- Recount: 7 flags, 2 HQs, 40 pads (RHIB 13, PatrolBoat 10, AttackHelicopter 3, LightTransport 3, PTV_QuadBike 3, Tank 3, MultirolePlane 2, TransportHelicopter 2, NavalFighterPlane 1), 11/11/18; stationary 10 (AntiTank 5, AntiAircraft 3, HMG 2); resupply 6; AutomaticAA 2. All match.
- Flag order is the only LOW case that holds: projection ABCDEFG, hyperbolic ABCDFEG (E/F swap), distance-to-HQ-W AEBDCGF. Off-axis 257 to 854 m on a 1286 m axis (0.20 to 0.66). Only A and C are nearer HQ-W than HQ-E (split W2/E5). The letters are not supported; keep LOW and say the order is unknown.
- The largest polygon @183 [-509,-452,823,730] holds 0 of 2 HQs and 18 of 40 pads. It is the island's objective area, not a play area.
- Pads: 22 pads are inside HQ-private polygons (11/11, E2) and 18 are the neutral ones (near flags). Four of those 18 are over 100 m from their flag (PatrolBoat at D and E, AttackHelicopter at C, PTV_QuadBike at B).
- Corrected rows: `near flag A: 2 pads (LightTransport 1, PatrolBoat 1); distance median 37 m, max 46 m`; `near flag B: 2 pads (PTV_QuadBike 1, Tank 1); distance median 77 m, max 101 m`; `near flag D: 4 pads (PatrolBoat 3, RHIB 1); distance median 33 m, max 133 m`; `near flag E: 2 pads (LightTransport 1, PatrolBoat 1); distance median 96 m, max 133 m`.

### Blackwell Fields (MP_BADLANDS)
- Verdict: ok.
- Recount: 6 flags, 2 HQs, 28 pads (LightTransport 8, APC 4, Tank 4, AttackHelicopter 2, AttackPlane 2, FighterPlane 2, IFV 2, MobileAA 2, PTV_DirtBike 2), 11/11/6; stationary 5; AutomaticAA 2; resupply 5; 0 Collection_Event. All match; no even-sized group differs.
- Flag order ABCDEF by both metrics; C and E are 152 and 153 m off-axis (0.21), no ties. MEDIUM is fair.
- SpecialCombatArea @129 [-1097,-1315,1182,849] holds both HQs, all 6 flags and all 28 pads: sound as the play boundary (MEDIUM). Planes are inside HQ polygons here (no far fixed-wing pads).
- No corrected rows.

### Iberian Offensive (MP_BATTERY)
- Verdict: minor fixes.
- Recount: 5 flags, 2 HQs, 8 pads (LightTransport 6, IFV 2), 3/3/2; forward 3; resupply 4; Battle_Pickup 3 (base variant @84 included). All match; no median issues (odd or single groups).
- Wrong: "Conquest_Team1/Conquest_Team2 exist as assets" - the asset list is only the Conquest0 path.
- Missed asymmetry: all 3 forward spawners lie within 5 to 12 m of HQ-W (579,118) and none near HQ-E (924,134). Siege of Cairo (2/2) and Operation Firestorm (3/3) are symmetric, so this is the one map where the forward set is one-sided. The mode rules note that "HQ sets are mirrored" (cross-map notes) is true for pads and Insertions (8/8) but not for forward spawners here. State it; reason unknown.
- Resupply: HQ-W 19 m, HQ-E 11 m, and two at flag C (33 m and 71 m).
- Flag order ABCDE by both metrics, no ties. Off-axis A 80, D 73, E 77 of 346 (0.23). OK.
- Inferred play area @107 [569,3,943,292] holds both HQs, all 5 flags and all 8 pads: sound at LOW to MEDIUM.

### Liberation Peak (MP_CAPSTONE)
- Verdict: minor fixes.
- Recount: 6 flags, 2 HQs, 26 pads, 10/10/6; 5 OutlineAreas (flag F's is 7 m away, flag A has none); Battle_Pickup 4 (2 base variant). All match.
- The HQ rows (10/10) include 4 fixed-wing pads (AttackPlane 1 + FighterPlane 1 per side) at 495 to 547 m from the HQ and outside its polygon (E3). Inside HQ polygons there are 8/8. Suggested row: `Liberation Peak | 6 | 2 | 8 / 8 / 6 (+4 fixed-wing pads 495-547 m from the nearest HQ, outside the HQ polygons) | 26 | 1200 | yes`.
- SpecialCombatArea instances @90 and @143 are both at (0,0,0), so their "containing polygons" are just the polygons containing the world origin, not a spatial link. @115 (2599 x 2644) holds both HQs, all flags and all pads; @211 (486 x 440) holds 0 of 2 HQs and 6 of 26 pads. The outer one is the boundary candidate; the pair is unresolved as the author says.
- Flag order: C/D tie (t .52/.53, off-axis 228 and 83); C is 421 m from HQ-W and 401 m from HQ-E; distance-to-HQ-W order is ABDCEF. Treat C/D letters as arbitrary. B, C, E are 153 to 228 m off-axis (0.33 max): MEDIUM falls to LOW for the middle flags.
- Corrected row: `near HQ-W: 10 pads (LightTransport 2, PTV_DirtBike 2, AttackHelicopter 1, AttackPlane 1, FighterPlane 1, IFV 1, PTV_QuadBike 1, Tank 1); distance median 19 m, max 547 m`.

### Contaminated (MP_CONTAMINATED)
- Verdict: minor fixes.
- Recount: 6 flags, 2 HQs, 24 pads, 10/10/4; stationary 11; resupply 8; PsyGasZone 6 (positions match). All match.
- Wrong: the "Conquest_Team1/Team2 exist as assets" boilerplate (neither is in the asset list).
- Flag A is credited with `OutlineArea x6 (dist 284/274/277/282/275/280 m)`. Those six are not flag A's. They are stacked within 10.5 m of each other at about (-282, -78) with y=464 (flags are at y 297 to 340, HQ-W at 331), 203 m from HQ-W, inside polygon 279 only. Flag A has no OutlineArea of its own. Flags C and E have two OutlineAreas each, stacked at the same point (about 1 m apart), so duplicates are normal. Item 7 "reason unknown" can be refined: 6 stacked outlines at one elevated off-flag point; 2 stacked at flags C and E; 0 at B, D, F.
- SpecialCombatArea @16 at (141,101): its polygons @43 (571 x 443; 1 of 2 HQs), @142 (45 x 39 m; bbox [125,79,170,118] is the flag C capture polygon, flag C is at (146,101)), @279 (944 x 844; both HQs, 6 of 6 flags, 24 of 24 pads). Drop @142 from the list (it is a flag polygon, not a combat area); @279 is the boundary candidate.
- Flag order ABCDEF by both metrics; C/D tie (.51/.52); D off-axis 160 (0.26). MEDIUM, with C/D arbitrary.
- Corrected rows: `near HQ-W: 10 pads (PTV_DirtBike 3, LightTransport 2, Tank 2, AttackHelicopter 1, IFV 1, ScoutHelicopter 1); distance median 31 m, max 58 m`; `near HQ-E: ... distance median 12 m, max 49 m`; `near flag D: 2 pads (PTV_QuadBike 2); distance median 26 m, max 27 m`.

### Area 51 (MP_DRYLAKE)
- Verdict: minor fixes.
- Recount: 9 flags + 1 CapturePoint_Proxy, 2 HQs, 61 pads (LightTransport 17, PTV_QuadBike 17, PTV_DirtBike 6, AttackPlane 4, Tank 4, AttackHelicopter 3, APC 2, FighterPlane 2, IFV 2, MobileAA 2, TransportHelicopter 2), 16/16/29. All match.
- Proxy @145 is 18 m from flag D (@64) in the same 56 x 57 m polygon (@23). The inference "stand-in, 9 playable flags" (MEDIUM) is sound; flag D also has the most pads (8 within 36 m), consistent with a hub objective.
- HQ rows (16/16) include 6 fixed-wing pads (AttackPlane 2 + FighterPlane 1 per side) 820 to 844 m from the HQ and outside its polygon (E3). Inside HQ polygons there are 13/13. Suggested row: `Area 51 | 9 | 2 | 13 / 13 / 29 (+6 fixed-wing pads about 830 m from the nearest HQ) | 61 | 1200 | yes`.
- Flag order: ABCDEFGHI by both metrics; D, E, F are within 0.02 of each other (t .47, .48, .49; E off-axis 6 m, D 338 m) and C/D .03, A/B .03, so letters C to F are arbitrary; distance-to-HQ-W order puts D after F. Keep MEDIUM/LOW as stated.
- SpecialCombatArea @190 holds both HQs, all flags and all 61 pads; @203 [-355,722,888,1314] holds 0 of 2 HQs. Sector (1515,236) is 736 m from HQ-E, not informative.
- Corrected rows: `near HQ-W: ... distance median 34 m, max 837 m`; `near HQ-E: ... distance median 35 m, max 844 m`; `near flag A: 2 pads (LightTransport 1, PTV_QuadBike 1); distance median 17 m, max 29 m`; `near flag D: 8 pads (LightTransport 4, PTV_QuadBike 4); distance median 33 m, max 36 m`; `near flag E: 6 pads (PTV_DirtBike 2, PTV_QuadBike 2, AttackHelicopter 1, LightTransport 1); distance median 24 m, max 76 m`; `near flag I: 2 pads (LightTransport 1, PTV_QuadBike 1); distance median 38 m, max 40 m`.

### Manhattan Bridge (MP_DUMBO)
- Verdict: minor fixes.
- Recount: 5 flags, 2 HQs, 14 pads (LightTransport 6, IFV 2, PTV_QuadBike 2, ScoutHelicopter 2, Tank 2), 6/6/2; stationary 2 (flags A and E); 2 OutlineAreas (flag D). All match.
- SpecialCombatArea @1 at (-42,-344) lists four polygons: @45 (763 x 684) and @115 (411 x 372) are plausible boundaries (@45 holds both HQs and all 14 pads; @115 holds 0 HQs and 2 pads), but @243 (29 x 26) and @285 (68 x 70) are small flag C capture polygons (flag C is at (-41,-345), 1 m from the SCA and the Sector). Drop those two.
- The Sector sits on flag C (0 m), the only map where it coincides with a flag.
- Flag order: ABCDE by both metrics, no ties, B off-axis 104 (0.21); C is the bisector (241 vs 243). OK.
- Corrected rows: `near HQ-W: 6 pads (LightTransport 3, IFV 1, ScoutHelicopter 1, Tank 1); distance median 19 m, max 32 m`; `near HQ-E: ... distance median 15 m, max 26 m`.

### Eastwood (MP_EASTWOOD)
- Verdict: minor fixes.
- Recount: 5 flags, 2 HQs, 34 pads (PTV_GolfCart 10, LightTransport 8, APC 4, Tank 4, AttackHelicopter 2, IFV 2, MobileAA 2, TransportHelicopter 2), 10/10/14. All match.
- The 10 golf carts are the weakly assigned group: flag B gets 3 (median 99 m, max 144 m) and flag C gets 5 (median 100 m, max 137 m); five flag pads are over 100 m from their flag. Suggest wording "golf carts form their own cluster; assignment to B/C is by distance only".
- Flag order: A/B tie (.29/.32) and D/E tie (.79/.81); C is nearer HQ-E (480 vs 358). Same ordering by both metrics. OK with ties noted.
- Corrected rows: `near HQ-E: 10 pads (APC 2, LightTransport 2, Tank 2, AttackHelicopter 1, IFV 1, MobileAA 1, TransportHelicopter 1); distance median 13 m, max 46 m`; `near flag B: 4 pads (PTV_GolfCart 3, LightTransport 1); distance median 99 m, max 144 m`.
- Faction overrides (team1 Alliance/NATO, team2 Coalition/Pax Armata) match the file.

### Operation Firestorm (MP_FIRESTORM)
- Verdict: minor fixes.
- Recount: 5 flags, 2 HQs, 37 pads, 15/15/7; forward 6 (3 per HQ, 64 to 96 m out); 17 OutlineAreas. All match.
- Open question 7: the 17 outlines are not unrelated to flags. They belong to only three flags: A 3 (6 to 34 m), B 7 (24 to 29 m), D 7 (20 to 37 m); C and E have none. All are within 37 m of a flag. State that, drop "reason unknown" to "multi-part outlines on flags A, B, D".
- Flag order ABCDE by both metrics; D/E tie (.68/.70, E off-axis 147 of 839); C is the bisector (427 vs 431). OK.
- Corrected rows: `near flag B: 2 pads (LightTransport 1, Tank 1); distance median 50 m, max 78 m`; `near flag E: 2 pads (LightTransport 1, Tank 1); distance median 50 m, max 69 m`.

### Railway to Golmud (MP_GOLMUDRAILWAY)
- Verdict: minor fixes.
- Recount: 7 flags, 2 HQs, 61 pads, 21/21/19; stationary 18; resupply 11; Battle_Pickup 7 (ArtilleryStrike 5, SmokeScreen 2); 1 OutlineArea (flag F). All match.
- HQ rows (21/21) include one FighterPlane per side at 1136 and 1188 m, outside the HQ polygon (E3). Inside HQ polygons: 20/20.
- Flag order: by both metrics ABCDEFG; E and F tie (t .53/.53, E off-axis 426 = 0.30 of the 1443 m axis); C/D/E within 0.04; distance-to-HQ-W order is ABCDFEG. Only G is clearly on the HQ-E side (1182 vs 398). MEDIUM to LOW as the author states, and the E/F letter is arbitrary.
- Corrected rows: `near flag A: 4 pads (PTV_DirtBike 2, IFV 1, LightTransport 1); distance median 25 m, max 127 m`; `near flag B: 2 pads (PTV_DirtBike 1, PTV_GolfCart 1); distance median 81 m, max 123 m`; `near flag E: 4 pads (PTV_DirtBike 2, LightTransport 1, MobileAA 1); distance median 31 m, max 47 m`; `near flag F: 2 pads (LightTransport 1, PTV_DirtBike 1); distance median 18 m, max 26 m`; `near flag G: 4 pads (PTV_DirtBike 2, LightTransport 1, Tank 1); distance median 26 m, max 203 m`.

### Tsuru Reef (MP_ISOLATED)
- Verdict: minor fixes.
- Recount: 9 flags, 2 HQs, 40 pads, 10/10/20; stationary 3; 8 OutlineAreas (all flags except E). All match.
- HQ rows (10/10) include 2 fixed-wing pads per side at 284 to 438 m, outside the HQ polygon (E3). Inside HQ polygons: 8/8.
- Flag order: ABCDEFGHI by both metrics, B/C tie (.33/.35) and G/H tie (.66/.69). Off-axis is at most 285 m of 1687 (0.17), the smallest ratio of the four maps the author calls weak; with the two orderings agreeing, MEDIUM is justified except for the ties. The map's HQ axis is mostly north-south (HQ-W z=843, HQ-E z=-680); W/E names are an x-only label.
- Corrected rows: `near HQ-W: 10 pads (RHIB 4, PatrolBoat 2, TransportHelicopter 2, AttackPlane 1, FighterPlane 1); distance median 50 m, max 289 m`; `near flag A: 2 pads (APC 1, PTV_DirtBike 1); distance median 23 m, max 30 m`; `near flag D: 4 pads (PTV_QuadBike 3, APC 1); distance median 74 m, max 146 m`; `near flag E: 2 pads (PTV_QuadBike 1, ScoutHelicopter 1); distance median 51 m, max 60 m`.

### New Sobek City (MP_OUTSKIRTS)
- Verdict: minor fixes (confidence wording only).
- Recount: 5 flags, 2 HQs, 21 pads, 9/9/3; stationary 9; 4 OutlineAreas (flags B, D). All match; no group is even-sized with a median difference.
- Flag order: ABCDE by projection and by hyperbolic metric. All five flags lie south of the HQ line (z -162 to -52 against HQs at z 0 and 12), giving off-axis 60 to 163 m (0.44 of the 374 m axis), yet the along-axis order is robust (it equals plain x order). Distance to HQ-W alone would put B (144) before A (165). This map is a clear case where "off-axis distance" overstates the uncertainty; MEDIUM is fine, and the convention line that lists only four off-axis maps is inconsistent with the printed distances.
- SpecialCombatArea @39 (36,-142): @37 (884 x 787) holds both HQs and all pads; @110 (469 x 230) holds 1 of 2 HQs and 13 of 21 pads.

### Vegas Strip (MP_PARADISE)
- Verdict: minor fixes.
- Recount: 5 flags, 2 HQs, 34 pads, 11/11/12; stationary 3; resupply 2; no Collection_Event, TelemetryArea 0. All match.
- SpecialCombatArea @114 and @173 both fall in @145 (406 x 476; 0 of 2 HQs, 15 of 34 pads) and @147 (831 x 966; both HQs, all 34 pads); @147 is the boundary candidate.
- Flag order ABCDE by both metrics; B (164) and E (155) are 0.25 off-axis. OK.
- Corrected rows: `near flag D: 2 pads (LightTransport 2); distance median 50 m, max 51 m`; `near flag E: 2 pads (PTV_DirtBike 1, PTV_QuadBike 1); distance median 46 m, max 49 m`. (Small differences, but the same method error.)

### Cairo Bazaar (MP_PLAZA)
- Verdict: minor fixes.
- Recount: 5 flags, 2 HQs, 4 pads (IFV 2, LightTransport 2), 2/2/0; stationary 4 (AntiTank at HQ-W, flags B, D, E); 5 OutlineAreas (flag B 1, flag C 4; A, D, E none). All match.
- SpecialCombatArea @114 at (20,93): @42 (24 x 57) is the flag C capture polygon (C is at (22,97)); remove it. @95 (246 x 291) holds HQ-E but not HQ-W (HQ-W z=-48 against bbox z min -38) and 1 of 4 pads, so neither listed polygon is a clean boundary; say so.
- Flag order ABCDE by both metrics; C is the bisector (167/165); D is 141 m off the 330 m axis (0.43), E and D close (t .64/.69). Distance-to-HQ-W order ACBED differs, so B/D letters are weaker than MEDIUM.
- Corrected rows: `near HQ-W: 2 pads (IFV 1, LightTransport 1); distance median 41 m, max 42 m`; `near HQ-E: 2 pads (IFV 1, LightTransport 1); distance median 21 m, max 27 m`.

### Hagental Base (MP_SUBSURFACE)
- Verdict: ok.
- Recount: 5 flags, 2 HQs, 0 pads, 0 resupply, 2 HMG (flags B and D), 5 TelemetryAreas, 2 Battle_Pickup (Minigun). All match.
- Flag order ABCDE by every metric, off-axis at most 50 m, C is the bisector (289/288). Strongest geometry of all maps; MEDIUM to HIGH.
- The "inferred play area" @48 [-232,-118,257,95] holds all 5 flags but neither HQ (HQ-W (-254,102) and HQ-E (275,-128) are 7 to 22 m outside). Already labelled LOW; add "objective area, HQs just outside".

### Mirak Valley (MP_TUNGSTEN)
- Verdict: minor fixes.
- Recount: 5 flags, 2 HQs, 42 pads, 16/16/10; stationary 15; resupply 7; Battle_Pickup 3 (Railgun 2, Minigun 1). All match.
- Flag @152 (C) is 233 m off-axis (0.23) and sits at the bisector (548 vs 555); C/D tie (.50/.53). Orders: projection and hyperbolic ABCDE, distance-to-HQ-W ABDCE. Letters C/D arbitrary, as the author says for C.
- SpecialCombatArea @53 (36,-329): @42 (2458 x 2048) holds everything; @171 (722 x 638) holds 0 of 2 HQs and 10 of 42 pads.
- Corrected rows: `near flag A: 2 pads (LightTransport 1, PTV_QuadBike 1); distance median 31 m, max 48 m`; `near flag C: 4 pads (AttackHelicopter 1, MobileAA 1, PTV_QuadBike 1, Tank 1); distance median 33 m, max 52 m`; `near flag E: 2 pads (LightTransport 1, PTV_QuadBike 1); distance median 25 m, max 30 m`.

### Saints Quarter (MP_LIMESTONE)
- Verdict: ok. Confirmed: Gameplay-maps.txt lists no Conquest layer for MP_LIMESTONE (only Gameplay, Gameplay_Global, Narrative and Telemetry layers); MUT_Limestone has 0 tweakables.

## Cross-map table and rules corrections

Cross-map table: all 18 rows (flags, HQs, W/E/flags, total, Air) reproduce exactly. Suggested edits:
- Empire State HQs cell: `3 (2 live + 1 marker)`.
- Pads cell on Liberation Peak, Area 51, Railway to Golmud, Tsuru Reef: add the far fixed-wing pad count (`8 / 8 / 6 +4 far`, `13 / 13 / 29 +6 far`, `20 / 20 / 19 +2 far`, `8 / 8 / 20 +4 far`), per E3. The totals (26, 61, 61, 40) do not change.
- Note on HQ-mirroring (line "Every map with data has an equal pad count at the two HQs"): confirmed, class mixes identical on all 16 maps with pads (computed), and strengthened by E1 and E2 (mark HIGH for pads inside HQ polygons). Add the exception that forward spawners on Iberian Offensive are all at HQ-W (3/0).
- Flags note (line "Flags: ..."): correct; it is listed in two batches (first capture, then the four added maps). Merge into one list.
- Notes line "Empire State has 3 HQs and 0 pads; Hagental Base ... infantry-only layouts": both true (Empire State has HMGs, Hagental HMGs); keep.

Rules section (59 rows): values and ranges equal `existing-tweakables.txt` for 58 rows. Corrections:
- Malformed row `CQ_f[]CaptureSpeedMultipliers`. Correct row: value `{"Field_ffba60f0": [0.0, 1.0, 1.333, 1.666, 2.0]}`, range `unbounded/not set` ([0.0..0.0]). The current row splits the array across the value and range cells.
- Source line 3 says the tweakables come from "Conquest-tweakables.txt"; that file holds only 4 round-logic graphs (all null). The 59 MUT_Conquest rows are in `existing-tweakables.txt` lines 1 to 60. Fix the source list.
- `CQ_bUseDynamicBleedFrequency` row says the interval "scales with the flag lead", but the next row (`CQ_iBleedFrequencyScoreRange`, 100) says the range is in lives. The name pair points to the lives (score) lead, so change to "scales with the lives lead (inferred, MEDIUM)".
- `CQ_fDeathRatioMultiplier = 2.0`: "scale of life loss per kill/death" is a guess; the name could also be a death-to-kill ratio factor. Mark LOW.
- `CQ_FullMajority_iFlagThresholdHigh` (6) and `Low` (3): the flag-count cutoff between High, Low and Default is not stored. With 5-flag maps requiring 3 and a 9-flag map requiring 6 the pairing is plausible but unverified; keep as inference (LOW).
- "The shared GEM logic graphs ... list only null runtime variables, no numbers": `SimEx_SectorSpotting` holds an undecoded boxed array (`SpottingSharingRules`), so say "no decoded numbers".
- UI-text quotes and the "Hardcore Conquest" title string cannot be checked: `ui-text.txt` and `map-names.json` are not in the extraction folder given to this review. Leave the quotes as is, but mark as unverified here.
- Per-map table: all 12 MUT blocks match (Abbasid, Aftermath, Badlands, Battery, Capstone, Dumbo, Eastwood, FireStorm, Golmud, Limestone, Outskirts, Tungsten). Seven maps (Wake Island, Contaminated, Area 51, Tsuru Reef, Vegas Strip, Cairo Bazaar, Hagental Base) have no MUT in the file. The sentence that per-map keys "suggest they override the mode default" is fine at MEDIUM.
- Vehicle class names in the tables are internal variant tokens (LightTransport, PTV_QuadBike, MobileAA, PTV_GolfCart). Map them to in-game vehicle names (UI metadata) before they go into GAME_MODES. The resupply labels `Ground` and `Ground_Air` are the author's wording for the default and the `_Air` variant (GMPF_VehicleResupplyStation_Air); say so.

## Stale statements

1. Header lines 9 and 10 and item 1 of section 4 narrate the capture history ("second capture", "Resolved by the second capture", "in either capture", line 803). The data now stands alone: 18 maps have Conquest0, Saints Quarter has none. Remove the history, and move the Iberian Offensive sentence (MUT_Battery values) out of "Conventions" into the per-map table.
2. "Layout variants: ... `Conquest_Team1`/`Conquest_Team2` exist as assets" is copy-pasted into all 18 maps and is false for Siege of Cairo, Iberian Offensive and Contaminated. Also "hold no gameplay instances" should read "no instances in this extraction" (only Conquest0 contributes instances; Conquest_Global and Conquest_Telemetry contribute polygons).
3. Conventions and open question 4 name four weak-axis maps (Wake Island, Tsuru Reef, Area 51, Railway to Golmud). By the printed off-axis ratio the weakest are Wake Island (0.66), Empire State (0.46), New Sobek City (0.44), Cairo Bazaar (0.43), Liberation Peak (0.33), Railway to Golmud (0.30); Tsuru Reef (0.17) and Area 51 (0.23) are among the better ones. By the two-ordering agreement test (E4) only Wake Island is unstable. Replace the list with the E4 result plus the tie list (Siege of Cairo A/B and D/E, Liberation Peak C/D, Contaminated C/D, Area 51 D/E/F, Golmud E/F, Eastwood A/B and D/E, Tsuru Reef B/C and G/H, Mirak Valley C/D).
4. Open question 2 (Empire State "which two HQs are live") is answerable; see the Empire State section.
5. Open question 7 (outline counts "reason unknown") is partly explained; see Contaminated and Operation Firestorm.
6. Flag lists in section 3 notes ("Flags: ..." and the HQ-mirroring list) are two-batch lists with the four added maps appended at the end; the table itself is in mixed order (first-capture maps, then Mirak Valley last). Cosmetic, but it shows the merge.
7. Open question 8 lists SpecialCombatArea "containing polygons" including tiny flag capture polygons (Manhattan Bridge @243 and @285, Contaminated @142, Cairo Bazaar @42) and a (0,0,0) instance (Liberation Peak). Remove the flag polygons; note that @90 and @143 are at the world origin.
8. The "inferred play area from the largest polygon" lines are wrong in kind on Siege of Cairo, Wake Island and Hagental Base (no HQ inside): label them "objective area".
9. Line 5, "MEDIUM on maps with a clear HQ axis": add that for pads inside the HQ spawn polygons the nearest-HQ rule is confirmed with 0 exceptions (E2), so "MEDIUM" for HQ ownership of those pads can be raised; ownership by team (which HQ is team 1) remains unknown.
