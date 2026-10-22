# Review of result-Rush.md (build 2.1.1.0)

Method: all counts were recomputed by script (python -I; scripts in the session scratchpad: rr.py, r2.py to r5.py) from `extraction/Rush-maps.txt`. Rules were checked against `extraction/existing-tweakables.txt` (MUT_Rush, shared MCOM/Plant/Reinforcement logic) because `extraction/rush-tweakables.txt` holds only two near-empty objects (GM_Rush_LaunchFunction, GME_Pres_Rush_Round). SpookyRush files were not needed (the result cites only the `AD_Objective_SpookyRush` name, which is in `ad-tables-by-mode.json`).

## Summary

- Tally: 11 ok, 6 minor fixes, 1 wrong (18 maps).
- ok: Siege of Cairo, Blackwell Fields, Liberation Peak, Manhattan Bridge, Eastwood, Operation Firestorm, Railway to Golmud, Tsuru Reef, New Sobek City, Cairo Bazaar, Hagental Base.
- minor fixes: Empire State, Wake Island, Iberian Offensive, Area 51, Vegas Strip, Mirak Valley.
- wrong: Contaminated.
- Every instance count, every per-HQ pad count and every cross-map pad split (attackers/contested/defenders by the author's own rule) reproduced exactly on all 18 maps. No invented instances. All "N gameplay instances" totals match (40, 30, 116, 40, 28, 50, 36, 86, 39, 52, 41, 98, 50, 43, 46, 43, 38, 60). Saints Quarter is correctly absent.
- Most important correction: Contaminated. The cross-map row says 4 sectors but lists five per-sector entries ("1/1/1/1/1"), the per-map section builds a 5-station chain (S1 to S5), the file has 4 Sector markers and 6 M-COMs, and the exclusion of M-COM @21 rests on a weak argument (see section). The honest row is "4 markers, 6 M-COMs, no containers, station grouping unresolved", not "Sectors 4".
- Second most important: the cross-map column "Sectors" is really "M-COM stations (pairs)", not GEM_Sector markers. Markers differ from stations on Empire State (4 vs 3), Manhattan Bridge (5 vs 4), New Sobek City (6 vs 4) and Contaminated (4 vs 5/6). Rename the column and add a marker column.
- Third: the mode-rules section cites sources that are not in the work folder (`ui-text.txt`, `map-names.json`, `objective-table.json`, `Rush-tweakables.txt` with values, and the scripts `parse_rush.py`, `final.py`, `build.py`). The numbers themselves are right (checked against `existing-tweakables.txt`), but the UI quotes in 1.9 cannot be verified from the folder.

## Counts recomputed (all maps)

Columns: Sector markers (GEM_Sector), M-COM instances, M-COM stations used by the author with M-COMs per station, HQ instances (stray/default ones in brackets), pads (all VehicleSpawner variants, plus VehicleSpawner_Forward where stated).

| Map | Markers | M-COM inst. | Stations (M-COMs each) | HQ inst. | Pads | Author agrees? |
|---|---|---|---|---|---|---|
| Siege of Cairo | 4 | 8 | 4 (2/2/2/2) | 10 (2 stray at 39,40) | 3 IFV | yes |
| Empire State | 4 | 6 | 3 (2/2/2) | 8 | 0 | yes (marker @6 has no pair) |
| Wake Island | 5 | 10 | 5 (2 each) | 10 | 58 | yes |
| Blackwell Fields | 4 | 8 | 4 (2/2/2/2) | 8 | 6 | yes |
| Iberian Offensive | 3 | 6 | 3 (2/2/2) | 7 | 1 | yes |
| Liberation Peak | 4 | 8 | 4 (2/2/2/2) | 8 | 12 | yes |
| Contaminated | 4 | 6 | unresolved (5 singles + @21, or other) | 10 (1 stray) | 0 | table row wrong |
| Area 51 | 5 | 10 | 5 (2 each) | 10 | 46 + 2 Forward = 48 | yes |
| Manhattan Bridge | 5 | 8 | 4 (2/2/2/2) | 8 | 0 | yes |
| Eastwood | 4 | 8 | 4 (2/2/2/2) | 8 | 5 | yes |
| Operation Firestorm | 3 | 6 | 3 (2/2/2) | 6 | 4 | yes |
| Railway to Golmud | 5 | 10 | 5 (2 each) | 10 | 41 | yes |
| Tsuru Reef | 3 | 6 | 3 (2/2/2) | 6 | 13 | yes |
| New Sobek City | 6 | 9 (1 stray) | 4 (2/2/2/2) | 9 | 0 | yes |
| Vegas Strip | 4 | 8 | 4 (2/2/2/2) | 11 (1 stray, 2 outliers) | 6 | yes |
| Cairo Bazaar | 4 | 8 | 4 (2/2/2/2) | 8 | 4 | yes |
| Hagental Base | 5 | 10 | 5 (2 each) | 10 | 0 | yes |
| Mirak Valley | 4 | 15 (6 stray) | 4 (2/3/2/2 = 9) | 10 (2 stray) | 9 | yes |

Pad class totals per map were identical to the author's on all 18 maps (Wake 26 Light Transport, 17 Patrol Boat, 8 RHIB, 5 Quad Bike, 2 IFV; Area 51 14 Dirt Bike, 12 Light Transport, 8 Quad Bike, 8 Tank, 2 Attack Helicopter, 2 Forward, 1 APC, 1 IFV; Golmud 10 Dirt Bike, 10 Tank, 7 IFV, 7 Light Transport, 5 APC, 2 Scout Helicopter; and so on).

## Per-map sections

### Siege of Cairo (MP_ABBASID)
Verdict: ok.
- Counts reproduce: 4 markers, 8 M-COMs (2/2/2/2), 10 HQ (8 real + 2 at 39.1, 40.2), 3 IFV pads (HQ @85, @31, @26), 2 Anti-Tank, 2 Minigun pickups, 6 insertions.
- Chain S1 (91,-56) to S4 (-174,-18) is monotonic in x; shortest-path order equals the given order (283 m). Insertions (x 49 to 173) all at the S1 end. Consistent.
- Nit: "Every sector has two HQs" is loose. By containers S1 has one sector HQ (@85) and S4 has one (@94); @31 and @99 are the base HQs.
- The DeployCam (-65.3, 740.5, 271.6) is a shared default position (Outskirts has two at the same x/z), so "nearest S4" is meaningless. The author flags the position but still lists it as nearest S4.
- Pad split 3/0/0 reproduces.

### Empire State (MP_AFTERMATH)
Verdict: minor fixes.
- Counts reproduce (4 markers, 6 M-COMs in 3 pairs, 8 HQ, 6 insertions, 0 pads).
- Error: "Marker @6 ... with HQ @52, Battle_Pickup Minigun @13 and all 6 insertions around it" is wrong. Only 3 insertions (@57, @59, @71 at z 76 to 101) lie near HQ @52. The other 3 (@5, @19, @75 at x -634 to -659, z 0 to 4) sit on the S1 M-COMs, 200 m from marker @6.
- Chain S1 (-643,29) to S3 (-593,-129) is monotonic in z; consistent. Direction (insertions at the S1 end) is consistent; the 4th marker as a "start zone" is a plausible but unproven reading (Manhattan Bridge and New Sobek City also have extra markers). Low confidence is the right label.
- Faction override (team 1 Pax Armata, team 2 NATO) matches the file and differs from the default; fine.
- Corrected sentence: "insertions form two groups of 3: one near HQ @52 / marker @6 (z 76 to 101), one on the S1 M-COMs (z 0 to 4)."

### Wake Island (MP_ATOLL)
Verdict: minor fixes.
- Counts, per-HQ pad lists, class totals and the 32/5/21 split reproduce exactly.
- Chain S1 (225,373), S2 (424,373), S3 (470,151), S4 (376,-89), S5 (126,-136): shortest path equals given order (939 m). Consistent.
- Error: "Both [insertion groups] lie on the S1 side". The second group (x 337 to 364, z 322 to 391) is 75 m from S2 and about 125 m from S1; the author's own count "S1:8, S2:8" says so. The quoted centroid (181,306) and "81 m from S1" is an average of two groups 190 m apart and falls in empty ground. The orientation still holds (all 16 are 400+ m from S5), but the text should say "west group at the start base side, east group between S1 and S2 (nearest S2)".
- Method sensitivity: pad-to-HQ assignment is weak here (median pad to nearest HQ distance 93 m, up to 228 m). With nearest-station-centre assignment the split would be 30 attackers / 7 contested / 21 defenders instead of 32 / 5 / 21. Worth a footnote; the table is correct under the stated rule.
- HQ @139 (468,34) is assigned to S3 by distance (117 m) but sits in S4's own containers (P44, P62, P143). No pads, no effect on numbers.

### Blackwell Fields (MP_BADLANDS)
Verdict: ok.
- Counts reproduce. Markers are all on the shared default positions; grouping by shared Rush0 polygons is a sound workaround. Chain monotonic in x and z (480 m). Pad split 6/0/0 reproduces (4 Quad Bike at @43, APC at @84 and @23).
- Faction override: team 1 Pax Armata, team 2 NATO; correctly noted as an inference caveat.
- Minor: HQ @83 (301,-83) is called S4 (65 m), but its containers are S3's (P24, P36). No pads.

### Iberian Offensive (MP_BATTERY)
Verdict: minor fixes.
- Counts reproduce (3 markers, 6 M-COMs, 7 HQ, 1 pad). Chain monotonic (131 m); insertions at the S1 end (all 6). Consistent.
- Error: "TelemetryArea: 3 (S1:2, S2:1)". Each telemetry area sits within 20 m of a Sector marker (@4, @28, @15), so it is 1/1/1 by marker. The 2/1/0 comes from nearest M-COM centre, which is the wrong anchor on this map because the markers lie 114 to 132 m from their pairs.
- The marker order (640,207), (708,192), (798,154) agrees with the M-COM chain order, which supports the S1 to S3 order.

### Liberation Peak (MP_CAPSTONE)
Verdict: ok.
- Counts reproduce; per-HQ pads match; 10/0/2 split reproduces (start HQ @106 4, S1 @19 4, S2 @113 2; S3 @3 2).
- Chain monotonic (447 m); insertions at S1 and the start base. Consistent. Markers all default positions; polygon grouping sound.
- HQs @16 and @113 each sit in both S2 and S3 containers; assigning them to S3 and S2 respectively by distance is acceptable. No effect on the table (@16 has no pads).

### Contaminated (MP_CONTAMINATED)
Verdict: wrong (cross-map row and station reading; the per-map caveats are honest).
- Counts: 4 Sector markers (all on shared defaults), 6 M-COMs, 10 HQ (@26 at 39.1, 40.2 stray), 16 insertions (all key -1), 0 pads, 0 containers (no BOX or POLY lines at all). The author's counts match.
- Contradiction: per-map table has 5 stations (S1 to S5, one M-COM each); the cross-map row says "Sectors 4, 1/1/1/1/1 (4 markers, 6 M-COMs, unresolved)". Five entries cannot be four sectors. The row also lists "Attacker start (-185,-48) -> (146,-76)", which is the 5-station chain.
- The exclusion of M-COM @21 (-8.5, 65.0, 31.2) is unsound. Its x/z equals Outskirts @35, but Outskirts @35 is itself the stray on that map (y 108.6 there, 65.0 here), and Mirak Valley shows the same leftover pattern. Equal x/z shows a shared template position; it does not show @21 is unused on Contaminated. Its y (65) matches the other Contaminated M-COMs (60 to 67), unlike the Mirak strays (y 96 to 97) or Outskirts @35 (y 108.6).
- A 3-station reading (3 pairs: @45+@43 111 m, @20+@21 86 m, @12+@5 149 m) is as consistent with 6 M-COMs as the 5-single reading; neither is provable without containers. Normal Rush layout elsewhere is 2 M-COMs per station on 17 of 18 maps, which argues for pairs rather than singles.
- HQs line up one per M-COM (@32 with @45, @15 and @30 with @20, @17 with @12, @4 with @5, @44 near @21), which weakly favours singles or an HQ per M-COM. Insertions form three clusters (8 at the start HQ @14, 4 near @43, 4 near @45).
- Direction: ordering stations by x gives a monotonic chain (465 m, also the shortest path), but with only insertions as evidence and a clustered insertion set, "low" confidence is right.
- Corrected cross-map row: Contaminated | 4 markers | 6 M-COMs, station grouping unresolved (5 singles by x or 3 pairs) | HQ 9 real + 1 stray | pads 0/0/0 | no air.

### Area 51 (MP_DRYLAKE)
Verdict: minor fixes.
- Counts, 48 pads (46 VehicleSpawner + 2 VehicleSpawner_Forward), per-HQ lists and the 27/11/10 split reproduce. The pad total 48 mixes the Forward spawners in; say so in the table ("46 + 2 Forward").
- Error: HQ @137 (499,973) is called "start base (beyond S1)" and listed as an attacker start base with @57. @137 lies in the S1 polygons P90 and P114 (the same two that hold the S1 M-COMs @85 and @126 and four insertions), 48 m from the M-COM centre. @57 (971,768) is the only HQ in the start polygon P17 (with 4 insertions and the 2 Forward spawners). So: start base = @57; S1 sector HQ = @137. Pad split is unchanged (both are attacker side).
- Error: "8 insertions (key 3 OnSpot) sit at the S1 end around x 690". The 8 form two clusters (4 near x 900, z 860 to 880 in the start polygon; 4 near x 450 to 500, z 1045 to 1058 in S1). The centroid (690,961) is 236 m from S1 and in empty ground. Orientation still holds.
- Chain S1 (457,996), S2 (396,1123), S3 (202,1194), S4 (30,1207), S5 (-8,946): shortest path equals given order (783 m). S5 curves back south, plausible for a final base at (2,820). Consistent.
- Pad assignment is weak in places (pads up to 258 m from the assigned HQ). The 27/11/10 split is stable under nearest-station assignment (also 27/11/10).
- Sector marker y values (113 to 305) are far above the M-COMs (56 to 87); not mentioned, harmless.

### Manhattan Bridge (MP_DUMBO)
Verdict: ok.
- Counts reproduce (5 markers, 4 pairs, 8 HQ, 0 pads). Chain monotonic (371 m). Two markers (@63 and @84) in the S2 area is correctly noted. HQ pair @21/@70 4.5 m. Faction override equals the default.
- Telemetry 2/1/1/2 reproduces.

### Eastwood (MP_EASTWOOD)
Verdict: ok.
- Counts reproduce; 5 pads, split 5/0/0. Chain monotonic (462 m); all 16 insertions at the S1 end in two clusters (8 near x -220 at the start HQ, 8 near x -30). Marker y values (341 to 348) confirmed. Open question 2 (only Rush0 listed) is consistent with the file.

### Operation Firestorm (MP_FIRESTORM)
Verdict: ok.
- Counts reproduce; 3 Tank + 1 IFV; split 2/0/2; 5 resupply stations (2 S1, 1 S2, 2 S3) reproduce; Railgun is the only Railgun pickup in Rush. Chain monotonic (334 m). Faction override equals the default.

### Railway to Golmud (MP_GOLMUDRAILWAY)
Verdict: ok.
- Counts and 24/5/12 split reproduce under the stated rule. Chain strictly north to south (473 m). Insertions: 4 at the start HQ @119, 3 on S1, 1 toward S2.
- Notes: resupply station @158 has the variant name "Air" (the other two are the standard variant); the result lists it without the class. Under nearest-station assignment the split would be 26/5/10; footnote only.
- HQ pairs @58/@155 and @127/@169 at identical positions reproduce.

### Tsuru Reef (MP_ISOLATED)
Verdict: ok.
- Counts reproduce; split 8/4/1; insertion keys reproduce (1 Arrival, 5 OnSpot v1, 1 v2, 5 v3, 2 Chaotic Arrival v1, 2 v2). Chain strictly westward (497 m). HQ @34 is in S1 and S2 containers; assigned to S1 by distance; no pads.

### New Sobek City (MP_OUTSKIRTS)
Verdict: ok.
- Counts reproduce (6 markers, 9 M-COMs of which @35 is stray, 9 HQ, 2 DeployCams at the Siege of Cairo default). Chain monotonic (243 m). Duplicated markers @100/@105 and @29/@107, HQ cluster at S3 (three instances), all reproduce. The stray M-COM exclusion is well founded here (y 108.6 vs 92 to 97, no containers, 100+ m away).

### Vegas Strip (MP_PARADISE)
Verdict: minor fixes.
- Counts reproduce; split 5/0/1 reproduces.
- Error: HQ @48 (-119,171) and @52 (0,143) are assigned S3 and S2 by distance, but their containers say the opposite. @48 sits in P19, P38 and P58 (the S2 polygons, z 156 to 239) and outside P46 (z 63 to 165); @52 sits in P46 (an S3 polygon). Corrected: S2 = @14, @48; S3 = @24, @52. No pads at either, no table effect.
- Open question 8 / "shared default (39,40)" for HQ @12: the actual position is (38.4, 38.4), not (39.1, 40.2) as on Siege of Cairo and Contaminated. Sector markers @20 (128.0,-25.6) and @73 (12.8,-12.8) are also grid-like values, not the (129,-22) / (15,-12) defaults. Say "near-default grid position", not "shared default".
- Chain monotonic in z (270 m). Insertions all key 3: 8 at the start HQ @65 (z 370 to 376), 8 on S1 and S2 (z 218 to 239). Consistent.
- HQ @6 (-117,-46) shares containers P21 and P56 with the S4 M-COM @63; calling it "final base (beyond S4)" is a distance rule, not a container fact. @11 (-82,-156, alone in B79) is the stronger final-base candidate.

### Cairo Bazaar (MP_PLAZA)
Verdict: ok.
- Counts reproduce (4 pads: 3 Dirt Bike at @27, APC at @24); split 1/0/3. Chain monotonic in x (371 m). All markers on defaults; polygon grouping sound. All 16 insertions at the S1 end.

### Hagental Base (MP_SUBSURFACE)
Verdict: ok.
- Counts reproduce (5 markers, 10 M-COMs, 10 HQ, 0 pads). Chain monotonic in x (373 m). Co-located HQ pairs: @21/@66 are 1.8 m apart, @56/@62 are 10.6 m apart. The pair text says 2 m and 11 m; open question 7 says "1 m". Harmless rounding, but use one value.
- Marker @65 (124,38) is 80 m from the S4 centre and 127 m from S5; the author's S5 assignment is by order of the markers; it could equally be an extra S4 marker. Not provable; low consequence.

### Mirak Valley (MP_TUNGSTEN)
Verdict: minor fixes.
- Counts reproduce (15 M-COMs: 9 real, 2/3/2/2, plus 6 strays; 10 HQ: 8 real + 2 stray). The 6 containers claim is correct. Pad split 8/0/1 reproduces. Chain monotonic (692 m). Containers support the base readings: P46 holds the start HQ @117 plus insertions, P122 holds only the final HQ @10.
- Unsupported claim: "HQ @16 and @100 look like the same stray set" as the Outskirts M-COMs. Their positions (-166,-188) and (-23,-180) match no Outskirts HQ (Outskirts HQs: -205,-100; -132,-98; -67,-68; -69,-77; -10,-83; -5,-77; 76,-60; 148,-21). Only the y (96 to 97) matches Outskirts height. Say "same height as the strays, no container; probably unplaced", not "same set".
- The M-COM strays do match Outskirts: (-15,-100) x2, (-8,-64) x2, (84,-24), (97,-81).
- S2 with three M-COMs (@6, @34, @53 in P8): sound as counted, but weak. Marker @11 is 6 m from @34, and @6 and @53 are 62 m apart. Possible alternative: @6 and @53 are the S2 pair and @34 is an extra. Keep "2/3/2/2" with "medium-low" confidence.
- HQ @52 (167,-378) is assigned to S1 (140 m); it sits in P8, the S2 polygon (S2 centre 168 m away). No pads at @52.

## Cross-map table and rules corrections

1. Rename the "Sectors" column to "M-COM stations" and add "Sector markers". Corrected rows for the maps where they differ:

| Map | Sector markers | M-COM stations | M-COMs per station | HQ (real) |
|---|---|---|---|---|
| Empire State | 4 | 3 | 2/2/2 | 8 |
| Manhattan Bridge | 5 | 4 | 2/2/2/2 | 8 |
| New Sobek City | 6 | 4 | 2/2/2/2 (+1 stray M-COM) | 9 |
| Contaminated | 4 | unresolved (5 singles or 3 pairs) | 6 M-COMs, no containers | 9 (+1 stray) |
| Mirak Valley | 4 | 4 | 2/3/2/2 (+6 stray M-COMs) | 8 (+2 stray) |

All other rows: markers equal stations, 2 M-COMs per station, HQ counts as in the table above.

2. Contaminated row: replace "4 | 1/1/1/1/1 (4 markers, 6 M-COMs, unresolved)" with "unresolved: 4 markers, 6 M-COMs, no containers".
3. Area 51 pad total: write "46 + 2 Forward".
4. Pad-split footnote: the split is by nearest HQ. Wake Island (32/5/21 vs 30/7/21) and Railway to Golmud (24/5/12 vs 26/5/10) change by 2 pads if assigned to the nearest M-COM station centre instead. Other maps are unchanged.
5. Empire State direction line: keep, but the start-zone explanation (marker @6) is an inference (low).
6. Mode-rules section (1.0 to 1.8): every number checked against `existing-tweakables.txt` is correct (110 tweakables; R_iInitialTickets 75; thresholds 50 and 25 with no threshold 2; arm 2.0/1.6, defuse 5.0/4.0, fuse 30.0, urgency fuse 45.0; sector time 15; respawn 10 global and 12 per team array of 15; XP values; SimEx variable lists; OwningTeamInt = 1). The tweakable `R_AttackerAdvanceReminderIncrementDelay` is written as `R_AttackerAdvanceInitialReminderDelay / IncrementDelay`; use the real name. The file has no `R_Win_ThirdSpanMinutes`, correctly not claimed.
7. Section 1.0 and the source line cite files not in this folder: `Rush-tweakables.txt` (in the folder it has only 2 objects, the values are in `existing-tweakables.txt`), `ui-text.txt`, `map-names.json`, `objective-table.json` (the content is in `ad-tables-by-mode.json` as `AD_Objective_Rush`), and the scripts. The 1.9 UI quotes and the "HARDCORE RUSH" label cannot be verified here.
8. Section 1.6: per-map tweakables list matches `maps-tweakables.txt` (including empty `MUT_Limestone`, `MP_Dumbo_VehicleOOBtime` 10 [1..15]). Correct.
9. Insertion variant names in the objective table: key 6 and 7 are `Chaotic_Arrival_v1` and `_v2`; keys 15 and 16 are the `NOT_FOR_REVEAL` OnSpot v4 and v5 (used on Wake Island and Cairo Bazaar). The result does not name them; consider saying so when it lists keys.

## Stale statements

- "Rush-maps.txt (second capture, layers also found directly under _Layers_Gameplay)": fine, but Section 2 "Unusual" lines on Empire State ("Layer assets live directly under _Layers_Gameplay") duplicate that; no conflict.
- Cross-map table row Contaminated says "4" sectors while Section 2 shows five stations (first-capture count against the second-capture grouping); fix as above.
- Open question 15 (second-capture maps) repeats facts already in the per-map sections and in Questions 6 and 11; it is consistent but redundant.
- Open question 5 lists the default-marker maps but not Hagental's @55 and @65 as non-default; fine. It does say Paradise (@73, @20) are "near-default"; that is correct (12.8-grid values).
- Open question 7 says "Subsurface (@21/@66 at 1 m)" while the map section says 2 m; actual 1.8 m. Contaminated is "1 m" in Unusual and "2 m" in the HQ pair line; actual 1.5 m.
- Open question 8 lists Paradise @12 as sitting on (39,40); actual (38.4, 38.4).
- Open question 4 still treats Contaminated @21 as a probable stray ("whether @21 is live"); keep it open, do not state it as excluded in the cross-map row.
- Scope text says "all 18 carry Rush gameplay instances"; true. No map in this result is still described as lacking a layer, and no first-capture count survives in the per-map sections other than the Contaminated row.
- Open question 1 (attacker side) remains the dominant uncertainty: nothing in the data labels teams. The insertion-end reading is consistent on all 18 maps (every insertion set lies within the first one or two stations and the start base, none near the last station), which is the best available evidence; the SimEx_CheckMCOMStatus default (OwningTeamInt = 1) is a graph default and does not contradict it.
