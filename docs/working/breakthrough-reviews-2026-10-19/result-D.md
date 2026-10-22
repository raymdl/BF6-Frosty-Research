# Result D: MP_ATOLL and MP_DRYLAKE

Class abbreviations: LT = LightTransport, PB = PatrolBoat, RHIB, Quad = PTV_QuadBike, Dirt = PTV_DirtBike, Tank, IFV, APC, AtkHeli, TrHeli, MobAA, Fwd = VehicleSpawner_Forward. Indices are the `@` instance indices.

## MP_ATOLL

Chain direction (inferred, low-medium confidence, 5 sectors, adopted from review-D.md and checked against the three in-game samples): attackers start on the carrier (HQ@198) -> Sector@404+@30 merged (defenders @347) -> Sector@7 (HQs @506+@185) -> Sector@178 (HQs @255+@207+@267) -> Sector@157 (no HQ) -> Sector@137 (final, HQs @120/@49/@38). Sector@30 is merged into @404 (95 m apart, CP@82 is 104 m from @347, no HQ or pads of its own). Weak point: the Sector@7 -> Sector@178 leg (about 620 m) is untested by any sample.

Anomalies:
- No Sector marker has a BOX (boxes=[] for all 6). Sector areas were taken from POLYs: 7=POLY@5/45/285/511, 30=POLY@9, 404=POLY@6/28, 178=POLY@2/8 + BOX@395, 157=POLY@3/474, 137=POLY@4/20/7.
- Sector 157 has no HQ (only 2 LT, 1 HMG, 1 AT). Sector 30 has no HQ and only one AntiTank.
- Sector 178 is split: BOX@395 (CP@33, HQ@207/267) and POLY@8 (CP@394, HQ@255).
- Water spawners in shared polys (121/234/257/271) are assigned by nearest sector; low confidence.
- No carrier-jet pads exist in this file; @198 is the carrier (HQ and TrHeli pads at y=115 against sea level 98).
- Totals: 102 VehicleSpawner + 6 StationarySpawner accounted for in the area table below.

Area table (pads grouped by area; use the HQ-group table further down for sides and phase sets):

| Area | Capture points | HQs | Vehicle spawners (class x count) | Likely side | Confidence |
|---|---|---|---|---|---|
| West base (BOX@392, poly 285) | none | @185 | LT x4, Quad x1, Tank x1, PB x4, RHIB x2 = 12 | Defenders of Sector@7 (with @506); attackers in phase 3 once @7 falls | Medium |
| Sector@7 (POLY@5/45/511) | @262, @59 | @506 | LT x3, Quad x1, Tank x1, IFV x1, PB x6 = 12 | Defenders phase 2; attackers phase 3 | Medium |
| Sector@30 (POLY@9) | @82 | none | none; AT x1 (@379) | Merged into @404 (phase 1) | Low |
| Sector@404 (POLY@6/28/121) | @324 | @347 | LT x5, IFV x1, PB x5, RHIB x1 = 12 (area count with pool boats is 13); HMG x1 (@424) | Defenders phase 1; attackers phase 2 | Medium |
| Sector@178 (BOX@395 + POLY@8/2) | @33, @394 | @207, @267, @255 | LT x9, Tank x2, IFV x1, Quad x1, PB x6, RHIB x5 = 24 | Defenders phase 3; attackers phase 4 | Medium |
| Sector@157 (POLY@3/474, BOX@52) | @326, @369 | none | LT x2; HMG x1, AT x1 | Defenders phase 4 (no HQ; pads unclear) | Low |
| Sector@137 (POLY@4/20/7, final) | @367, @220, @441 | @38, @49, @120, @246, @344 | LT x11, Quad x1, Tank x2, IFV x1, PB x3, RHIB x4 = 22; AA x1, AT x1 | Defenders phase 5 | Medium |
| Carrier / naval (BOX@479/483, outside sectors) | none | @198 | PB x6, RHIB x9, TrHeli x2 = 17 | Attackers phase 1 (start) | High (sample 1) |

Area counts and HQ-group counts differ slightly (areas use polys, HQ groups use the nearest HQ); the per-phase sets below use HQ groups.

### Per-phase vehicles (attack vs defense)

Sample check on the adopted chain (all subsets):
- Sample 1 (TrHeli x2, RHIB x9, PB x4) is a subset of @198 only (PB 4 of 6): phase 1 attackers.
- Sample 3 (Tank x1, RHIB x2, PB x3, LT x3) is a subset of @506+@185 (LT 7, Tank 2, PB 10, RHIB 2): phase 3 attackers, so @185 and @506 land at phase 3 as attackers (after Sector@7 falls) and at phase 2 as defenders.
- Sample 4 (Quad x1, RHIB x1, LT x3, PB x3, Tank x1, IFV x1) is a subset of @255+@207+@267 (LT 9, Tank 2, IFV 1, Quad 1, PB 7, RHIB 5): phase 4 attackers. No single HQ holds it (@506 lacks RHIB), so the earlier "@506 at phase 4" claim was wrong.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (Sector@404+@30) | @198 (carrier): PB x6, RHIB x9, TrHeli x2 | @347: LT x5, IFV x1, PB x5, RHIB x1, AT x1, HMG x1 | Sample 1 subset |
| 2 (Sector@7) | @347: LT x5, IFV x1, PB x5, RHIB x1, AT x1, HMG x1 | @506+@185: LT x7, Quad x2, Tank x2, IFV x1, PB x10, RHIB x2 | No sample |
| 3 (Sector@178) | @506+@185: LT x7, Quad x2, Tank x2, IFV x1, PB x10, RHIB x2 | @255+@207+@267: LT x9, Tank x2, IFV x1, Quad x1, PB x7, RHIB x5, AT x1, HMG x1 | Sample 3 subset (attackers) |
| 4 (Sector@157) | @255+@207+@267: LT x9, Tank x2, IFV x1, Quad x1, PB x7, RHIB x5, AT x1, HMG x1 | none at Sector@157; @49 (LT x8, Tank x2, Quad x1) is the nearest on the defenders' side, low confidence | Sample 4 subset (attackers) |
| 5 (Sector@137, last) | @255 group (or @49 if captured earlier) | @120+@49+@38: LT x13, Tank x2, Quad x1, IFV x1, PB x3, RHIB x4, AA x1, AT x1 | Final; no sample |
| Unassigned | @246, @344 (0 pads) | | |

## MP_DRYLAKE

Chain direction (inferred, east to west, forced by the in-game attackers' sample 1 = HQ@96 exactly): attackers start at the east base (HQ@96, BOX@141, with the only usable Sector marker @166); the final defenders' HQ is @236 at the far west (with 2 AutomaticAA).

Anomalies:
- Sector@82, @89, @149 sit at about (-82..128, z 0..-38), far from the map (z 800-1200), in no box or poly. Positions unusable, so sectors were derived from the CP/HQ clusters.
- The east box BOX@141 holds Sector@166 plus the start base (HQ, 4 Fwd spawners) and no capture point.
- Spawners: 70 VehicleSpawner = W 8 + A 8 + B 20 + C 17 + D 10 + E 7; plus 4 Fwd, 5 StationarySpawner, 2 AutomaticAA.

Area table (by polygon; sides follow the east-to-west chain):

| Phase/Sector | Capture points | HQs | Vehicle spawners (class x count) | Likely side | Confidence |
|---|---|---|---|---|---|
| East base BOX@141 (Sector@166) | none | @96 | LT x2, Dirt x2, APC x1, Tank x1, TrHeli x1 = 7; Fwd x4 | Attackers' start (phase 1) | High (sample 1) |
| S1 Area D (POLY@12/71/104) | @266, @29 | @46 | LT x3, Dirt x2, Quad x2, APC x1, Tank x1, AtkHeli x1 = 10 | Defenders phase 1; attackers phase 2 | Medium |
| S2 Area C (POLY@35/203) | @209, @126 | @118, @232 | LT x5, Dirt x6, IFV x2, Tank x1, AtkHeli x1, TrHeli x1, Quad x1 = 17 | Defenders phase 2 (@118); attackers phase 3 (@118+@232) | Medium |
| S3 Area B (POLY@157/142) | @193, @39, @168 | @112, @173, @190 | LT x6, Dirt x6, Quad x2, Tank x2, IFV x1, APC x1, MobAA x1, TrHeli x1 = 20 | Defenders phase 3 (@112) | Low-medium |
| S4 Area A (POLY@28/163/251) | @66 | @42 | LT x3, Tank x1, AtkHeli x1, IFV x1, Dirt x2 = 8; HMG x3, AT x2 | Attackers phase 4 (@42 group); emplacements stay behind | Medium |
| West base (POLY@61/251) | none | @236 | LT x2, Tank x1, AtkHeli x1, Quad x2, Dirt x2 = 8; AutoAA x2 | Defenders' final base (phase 4) | Medium |

### Per-phase vehicles (attack vs defense)

HQ-group based. The in-game sample forces the chain to run east to west: attackers at sector 1 (TrHeli, Tank, APC, 2 LT, 2 Dirt) equals exactly the HQ@96 group (excluding its 4 Fwd pads), so HQ@96 is the attackers' start and this replaces my earlier west-to-east guess. Sectors (east to west): S1 = CP@266/@29 (HQ@46), S2 = CP@209/@126 (HQ@118/@232), S3 = CP@193/@39/@168 (HQ@112/@173/@190), S4 = CP@66 (HQ@42), final HQ@236 at the far west.

In-game samples: attackers at sector 1 = HQ@96 (exact). Attackers at a later sector = exactly HQ@42 (AtkHeli, Tank, IFV, 3 LT, 2 Dirt); it lands at phase 4 (HQ@42 is the HQ between S3 and S4), so the log's "3" lands at phase 4. The operator was unsure of that number; "3 sectors captured" is only an assumption. Defenders at sector 2 (4 Dirt, LT, IFV, TrHeli) fit HQ@118 as a subset (Dirt x5); HQ@173 has only Dirt x3 so does not strictly fit.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S1: CP@266/@29) | @96 (start): Dirt x2, APC x1, LT x2, Tank x1, TrHeli x1, Fwd x4 | @46: Dirt x2, Quad x2, APC x1, LT x3, Tank x1, AtkHeli x1 | Attackers match in-game sample 1 exactly (Fwd not in sample) |
| 2 (S2: CP@209/@126) | @46: Dirt x2, Quad x2, APC x1, LT x3, Tank x1, AtkHeli x1 | @118: LT x3, AtkHeli x1, Dirt x5, TrHeli x1, IFV x1 | Defenders match in-game sample as a subset; @46 plays defenders in phase 1 and attackers here |
| 3 (S3: CP@193/@39/@168) | @118+@232: LT x4, AtkHeli x1, Dirt x5, TrHeli x1, IFV x1, Tank x1 | @112: Dirt x3, LT x3, Quad x2, Tank x1, APC x1 | Attackers carry the captured S2 HQs (@118 plus @232 at CP@126); low confidence, no sample. @173 is the alternate defenders' group |
| 4 (S4: CP@66, last) | @42: HMG x3, AT x2, LT x3, AtkHeli x1, Tank x1, Dirt x2, IFV x1 | @236 (final): LT x2, Tank x1, AtkHeli x1, AutoAA x2, Quad x2, Dirt x2 | Attackers match in-game sample 2 exactly (HMG/AT are emplacements, not in the sample). The logged "3" lands here; the operator was unsure of the number |
| Unassigned | @173: IFV x1, Dirt x3, LT x3, TrHeli x1; @190: LT x1, IFV x1, Quad x1, MobAA x1, Tank x1, Dirt x1 | | @173 sits 10 m from @112 (likely alternate S3 defenders); @190 is off-axis (z 1152) and fits no phase cleanly |
