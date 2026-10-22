# Review brief

You are reviewing per-map Breakthrough analyses written by Sonnet subagents from decoded Battlefield 6 data.
Read first: README-for-agents.md (format of the MP_*.txt extraction files) and ../bt-hq-groups.txt (each
map's HQs with the pads nearest to each, plus nearest sector marker and capture point).

Model under review (current): each vehicle pad is assigned to an HQ and is live when that HQ is live. In
phase N (sector N under attack) attackers draw on the HQ on their side of sector N (the start HQ in phase
1), defenders on the HQ on their side (the final HQ in the last phase). Team 1 attacks. Chain direction
and HQ sides are spatial inferences; in-game samples are ground truth.

In-game samples (19 Oct 2026). Class names: Tank, IFV, APC (LTV / Traverser Mark 2), LT (Glider 96 /
VECTOR), Dirt (M1030-M1 / TM/O 450), Quad (Rugged MV740), TrHeli (UH-79), AtkHeli (M77E), ScoutHeli
(AH-6), AtkPlane (F-61V), RHIB, PatrolBoat (RCB-90).
- Area 51 (MP_DRYLAKE), 4 sectors, NATO attacks. Attackers S1: TrHeli 1, Tank 1, APC 1, LT 2, Dirt 2.
  Attackers later sector (logged 3): AtkHeli 1, Tank 1, IFV 1, LT 3, Dirt 2. Defenders S2: Dirt 4, LT 1,
  IFV 1, TrHeli 1.
- Manhattan Bridge (MP_DUMBO), 3 sectors, NATO attacks. S1: no vehicles either side.
- Vegas Strip (MP_PARADISE), 3 sectors, Pax attacks. Attackers S2: IFV 1, APC 1. Defenders S1: IFV 1.
  Defenders S2: APC 1 (LTV), IFV 1.
- Railway to Golmud (MP_GOLMUDRAILWAY), 4 sectors, NATO attacks. Attackers S2: AtkPlane 1, ScoutHeli 1,
  Tank 2, APC 2, LT 1, Dirt 2. Defenders S2: Dirt 2, LT 1, Tank 1, IFV 1.
- Wake Island (MP_ATOLL), 5 sectors, NATO attacks, start on the carrier. Attackers S1: TrHeli 2, RHIB 9,
  PatrolBoat 4. Attackers S3: Tank 1, RHIB 2, PatrolBoat 3, LT 3. Attackers S4: Quad 1, RHIB 1, LT 3,
  PatrolBoat 3, Tank 1, IFV 1.
- Contaminated (MP_CONTAMINATED), 5 sectors. Defenders (Pax) S2: Dirt 1, LT 2.
- Liberation Peak (MP_CAPSTONE), 5 sectors, NATO attacks. Attackers S1: Tank 1, IFV 1. Attackers S2:
  Tank 1, IFV 1.
- Cairo Bazaar (MP_PLAZA), 3 sectors, Pax attacks. Attackers S1: IFV 1. Attackers S2: none.
- Tsuru Reef (MP_ISOLATED), 4 sectors, Pax attacks. Attackers S1: APC 1, LT 1, RHIB 2, Quad 2, Dirt 2.
  Attackers S2: APC 1, LT 1, RHIB 2, Quad 2.
Sets smaller than an HQ group are expected (a random-enabler mechanism exists); sets larger than or
disjoint from the claimed group are errors.

For each map in your result file, check:
1. Every vehicle count in the HQ-group per-phase table against bt-hq-groups.txt (exact class counts per
   HQ). Flag any miscounted or invented entries.
2. That every HQ with pads appears exactly once (a phase row or the unassigned row), and no pad group is
   used for two phases without a stated reason.
3. Chain direction and sector order against the geometry in the MP_*.txt file and against any in-game
   sample for that map; state whether the sample fits the claimed HQ group as equal or subset.
4. Internal contradictions between the first (area-based) table or prose and the HQ-group table; list
   stale statements that a reader would be misled by.
5. Anything the author marked low confidence: say whether you agree, and if you can resolve it from the
   data, say how.

Write review-<group>.md in this folder: one section per map with Verdict (ok / minor fixes / wrong),
a bullet list of concrete findings with the numbers, and corrected table rows where you found errors.
Do not rewrite the result file. Reply with one line per map: map, verdict, the single most important
finding.
