# Breakthrough spawner interpretation (batch B)
All sides are inferred spatially; nothing in the data labels teams. Atk = attackers, Def = defenders. Numbers like S191 are Sector marker indices; box/poly numbers are shape indices.

## MP_EASTWOOD
Chain (med, reversed after in-game sample): west to east, NATO (team1) attacking. Attackers start west at HQ@76 (Tank x1); order S191 -> S151 -> S182; defenders' final base east (HQ@34 IFV+HMG, HQ@164 none). Sample forced the reversal: attackers at sector 2 had TrHeli x1 + IFV x1 = HQ@100 (TrHeli, Cart x2) + HQ@1 (IFV, AT), which both lie between S191 and S151; the old east-to-west chain had only HQ@79 (APC, Cart x2) there. The golf carts are not in the sample (probably not counted). No sector has a box; only polys. 4 CPs for 3 sectors.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (west, poly13) | none | HQ@76 (-335,-68) | Tank x1 (@199) | Atk | Med |
| 1: S191 (poly9/17/168/176) | CP41 (-180,13) | HQ@1 (-96,65) | IFV x1 (@172), AT x1 (@86) | Def | Med |
| 2: S151 (poly3, poly58/122/25) | CP85 (49,42), CP65 (192,-170) | HQ@100 (-42,71), HQ@79 (east side, 77,-31) | HQ@100: TrHeli x1, GolfCart x2; HQ@79: APC x1, GolfCart x2, HMG x1, AT x2 | HQ@1 and HQ@100 Atk (sample); HQ@79 Def | Med |
| 3: S182 (poly1; poly58/122/25) | CP184 (77,-31) | HQ@79 on CP184, HQ@34, HQ@164 | HQ@34: IFV x1, HMG x1 | Atk uses HQ@79 group; Def uses HQ@34 + HQ@164 (none) | Low-Med |

Anomalies: no sector has a box; CP85 sits on the edge of both S151 and S182 polys; 4 CPs for 3 sectors. Operator layout 1/2/1: CP65 (192,-170, near HQ@34) is put in sector 2 with CP85 (S1: CP41; S3: CP184); spatially CP65 sits east of CP184, so this is the operator's recollection overriding position. Totals: VehicleSpawner 9 (Tank1, IFV2, APC1, TransportHeli1, GolfCart4), Stationary 5 (HMG2, AT3). 7 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of their HQ group.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S191) | HQ@76: Tank x1 | HQ@1: IFV x1, AT x1 |  |
| 2 (S151) | HQ@1: IFV x1; HQ@100: TrHeli x1, Cart x2 | HQ@79: APC x1, Cart x2, HMG x1, AT x2 | Matches sample (TrHeli x1 + IFV x1; carts not mentioned) |
| 3 (S182) | HQ@79: APC x1, Cart x2 (HQ@100 may persist) | HQ@34: IFV x1, HMG x1; final HQ@164 none | Low-Med |
| Unassigned |  |  | none |

## MP_FIRESTORM
Chain (low-med): east to west. Attackers start in the large east base (HQ@158; Quad x2, LightTransport x2, IFV, Tank, TransportHeli, Forward); defenders' final base is HQ@8 in the west (IFV+Tank), outside all sector boxes. Order S103 -> S196 -> S216 -> west base.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (east, poly40) | none | HQ@158 (375,-118) | Tank x1 (@214), IFV x1 (@187), LightTransport x2, QuadBike x2, TransportHeli x1 (@197), Forward x1 (@140) | Atk | Med |
| 1: S103 (boxes 153,4) | CP164 | HQ@163 | IFV x1 (@44), Tank x1 (@47), Forward x1 (@229) | Def | Med |
| 2: S196 (box1; box169 sub-area) | CP233, CP243 (box151/3 outside box1, in poly32) | HQ@54, HQ@170 | IFV x2 (@198,@206), Tank x1 (@120) | Def (Atk later) | Med |
| 3: S216 (box2) | CP87 | HQ@93 | IFV x1 (@48), Tank x1 (@179) | Def | Med |
| Def final base (west, poly190) | none | HQ@8 | IFV x1 (@18), Tank x1 (@36) | Def (last phase/after S216) | Low-Med |

Anomalies: CP243 lies in its own boxes 151/3, outside S196's box1 (assigned by polygon 32); direction is a guess because both ends have IFV+Tank; Forward@229 is inside the S103 box and could serve attackers once S103 falls. Totals: VehicleSpawner 16 (IFV6, Tank5, Quad2, LightTransport2, TransportHeli1) + Forward 2. 6 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of the HQ group they belong to.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S103) | HQ@158: Tank x1, IFV x1, LT x2, Quad x2, TrHeli x1, Fwd x1 | HQ@163: IFV x1, Tank x1, Fwd x1 |  |
| 2 (S196) | HQ@163: IFV x1, Tank x1, Fwd x1 | HQ@54: Tank x1, IFV x2; HQ@170 none | HQ@54/@170 are a pair 6 m apart |
| 3 (S216) | HQ@54: Tank x1, IFV x2; HQ@170 none | HQ@93: IFV x1, Tank x1; final HQ@8: IFV x1, Tank x1 | Defenders total IFV x2, Tank x2 |
| Unassigned |  |  | none |

### Patch-note check (1.1.3.0)

Operation Firestorm. Sector 2 "adjusted defender armour": consistent (defenders hold HQ@54 Tank x1, IFV x2; no contradiction). Sector 3 "added 2 Attacker tanks and 1 Attacker IFV; removed the Defender tank": does NOT fit cleanly. The sector 3 attackers' group (HQ@54: Tank x1, IFV x2) has one tank, and the sector 3 defenders still hold Tank x2 (HQ@93 + final HQ@8). No single HQ group has Tank x2 + IFV x1, and reversing the chain (west to east) does not produce one either (attackers' sector 3 would still be HQ@54). Direction and sides left unchanged; the extracted layer probably reflects a different build than 1.1.3.0 (later updates), so the notes are not forcing a change here.

## MP_OUTSKIRTS
Chain (low-med, revised for in-game sample): west to east, NATO (team1) attacking, 3 sectors in-game. Merge: S15 (-26,-84) is folded into S207 (-129,-131) as sector 1; operator layout 2/1/2 (5 of the 6 layer CPs): sector 1 = CP18 + CP144, sector 2 = S175 with CP109 only, sector 3 = S131 with CP122 + CP103. Odd one out: CP177 (-142,-168), isolated in its own box150, 76 m from CP18 and far south of the chain line, so probably unused in the live layout; CP109 stays in S175 because it is 5 m from HQ@156 (the Quad group) while CP103 (61,-98) lies 44 m from the S175 marker and toward S131. Low-Med confidence. Attackers start west (HQ@56: Fwd2, IFV, LT); defenders' final base east (HQ@71: LT + IFV; HQ@152 empty). Sample: Pax defenders sector 2 Quad x1 = HQ@156 exactly, sector 3 LT x1 + IFV x1 = HQ@71 exactly; sector 1 "none" is weak evidence (HQ@46, HQ@73, HQ@94 hold APC, LT x2, IFV in that area, so they were probably taken or not all enabled). East-to-west was tested and fits worse (LT count and extras do not match).

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (poly146) | none | HQ@56 | Forward x2 (@158,@167), IFV x1 (@166), LightTransport x1 (@190) | Atk | Med |
| 1: S207 + S15 merged (box2, poly216; poly184/212/215/3) | CP18, CP144 (CP177 box150 dropped as unused) | HQ@46, HQ@73, HQ@94 | APC x1 (@194), HMG x2, AT x2, IFV x1 (@105), LightTransport x2 (@135,@219) | Def | Low-Med |
| 2: S175 (poly126/140/1) | CP109 | HQ@156, HQ@157 | QuadBike x1 (@57), HMG x1 (@33), AT x1 (@77) | Def | Med |
| 3: S131 (poly30 only) | CP122, CP103 | HQ@152 (205,-158), final HQ@71 | HQ@71: LightTransport x1 (@61), IFV x1 (@133); HQ@152 none | Def | Med |

Anomalies: only S207 has a box; S131 has no sub-polygon and no pads; the HQ@71 base is about 92 m from S175. Totals: VehicleSpawner 9 (Quad1, LightTransport4, IFV3, APC1) + Forward 2 + Stationary 6 (HMG3, AT3). 7 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of their HQ group.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S207+S15) | HQ@56: Fwd x2, IFV x1, LT x1 | HQ@46: APC x1, HMG x2, AT x1; HQ@73: LT x2, AT x1; HQ@94: IFV x1 | Sample "none" weak; if only part is enabled, defenders hold a subset |
| 2 (S175) | HQ@46/@73/@94 set (same vehicles) | HQ@156: Quad x1; HQ@157: HMG x1, AT x1 | Matches sample Quad x1 |
| 3 (S131) | HQ@156: Quad x1 | HQ@152 none; final HQ@71: LT x1, IFV x1 | Matches sample LT x1 + IFV x1 |
| Unassigned |  |  | none |

### Patch-note check (1.1.3.0)

New Sobek City. The extracted layer has no Tank pads at all (only Quad, LT, IFV, APC), so "Sector 2: added 1 Defender tank and IFV" and "Sector 3: removed Defender tank and LT" cannot be reproduced from this data. The in-game sample (defenders sector 2 Quad x1, sector 3 LT x1 + IFV x1) matches the HQ groups exactly (HQ@156, HQ@71), so a later update has superseded those notes (reading A: notes are older than the build; reading B, a different sector numbering, also fails because no HQ group holds a tank). Table unchanged; the sample is trusted over the notes.

## MP_PARADISE
Attackers = Pax Armata (team1). Chain (med): north to south, 3 sectors confirmed in-game. Attackers start in the north base (HQ@32, z=422-499, outside all sector shapes). Order S27 -> S23 -> S51 (S59 dropped).

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (north, poly20/105) | none | HQ@32 | APC x1 (@41), Tank x1 (@62), DirtBike x1 (@112), LightTransport x1 (@113) | Atk | Med-High |
| 1: S27 (box54; poly7/136/156) | CP48, CP124 (boxes 1,44) | HQ@28 | IFV x1 (@43), APC x1 (@125) | Def | Med |
| 2: S23 (poly81/123/26) | CP24, CP114 (z=-25), CP38, CP133 | HQ@116 (south edge), HQ@8, HQ@47 (north staging block z 108-172) | staging block: LightTransport x1 (@4), APC x1 (@15), IFV x1 (@131), Forward x1 (@87) | HQ@47 block (LT, APC, IFV, Fwd) serves phase 2 defenders and phase 3 attackers per the in-game sample; HQ@8/HQ@116 have no pads | Low-Med |
| 3: S51 (poly135, south) | none | HQ@115, HQ@137 | APC x2 (@39,@61), IFV x2 (@84,@155) | Def (south end, reads like a final base) | Med |

Anomalies: dropped S59, CP103, HQ@144 (and HQ@100) sit at y=226 versus y~50 elsewhere and have no pads; S51's polygon has no CP; S23 holds 4 CPs. 7 CPs total. Totals: VehicleSpawner 13 (APC5, IFV4, LightTransport2, Tank1, DirtBike1) + Forward 1. 6 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of the HQ group they belong to.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S27) | HQ@32: APC x1, Tank x1, Dirt x1, LT x1 | HQ@28: IFV x1, APC x1 | Sample: defenders sector 1 IFV (APC not listed in sample) |
| 2 (S23) | HQ@28: IFV x1, APC x1 | HQ@47: LT x1, IFV x1, APC x1, Fwd x1 | Sample: attackers IFV+APC matches HQ@28 exactly; defenders APC (LTV) + IFV is a subset of HQ@47. HQ@8 and HQ@116 (none) sit at S23 CPs |
| 3 (S51) | HQ@47: LT x1, IFV x1, APC x1, Fwd x1 | HQ@137: APC x2, IFV x1; final HQ@115: IFV x1 | Defenders total APC x2, IFV x2; direction north to south; S59 dropped |
| Unassigned |  |  | HQ@8, HQ@116, HQ@100, HQ@144: all none (HQ@144 belonged to dropped S59) |

## MP_PLAZA
Attackers = Pax Armata (team1). Chain (med): south to north. Attackers start in the south base (poly42/46: HQ@147, IFV@99, outside sector shapes); the north HQ@50 (poly109, no spawners) is the defenders' last base. Order S182 -> S56 -> S143.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (south) | none | HQ@147 (-62,-71) | IFV x1 (@99) | Atk | Med |
| 1: S182 (poly91/127/156) | CP177, CP40 | HQ@52 | none | Def | Med |
| 2: S56 (-182,-4, no polys; stray marker) | CP162, CP90 (poly48/126/139, assigned by elimination) | HQ@158 | IFV x1 (@112), HMG x2 (@74,@80), AT x1 (@142) | Def | Low |
| 3: S143 (poly138/183) | CP2, CP93 | HQ@10, HQ@31, HQ@113 | HMG x1 (@35), AT x2 (@58,@181) | Def | Med |
| Def final base (north) | none | HQ@50 (150,231) | none | Def | Low |

Anomalies: S56 (-182.4, 66.6, -3.9) is identical to Eastwood S191 and lies outside the other sectors' x range, so it is probably a displaced marker; the HQ@158 pad group sits between S182 and S143 and is assigned to the middle phase. Totals: VehicleSpawner 2 (IFV2) + Stationary 6 (HMG3, AT3). 3 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of their HQ group.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S182) | HQ@147: IFV x1 | HQ@52: none | Start IFV is HQ@147 (south); matches sample IFV x1 |
| 2 (S56 middle) | HQ@52: none | HQ@158: IFV x1, HMG x2, AT x1 | Matches sample: attackers none; HQ@158 group moves to defenders here |
| 3 (S143) | HQ@158: IFV x1 (HMG/AT emplacements stay defender assets) | HQ@113 none, HQ@31: HMG x1, AT x1, HQ@10: AT x1, final HQ@50 none | Defenders total HMG x1, AT x2 |
| Unassigned |  |  | none |

Sample note (Cairo Bazaar): attackers sector 1 = IFV x1, sector 2 = none; this forced the start IFV onto HQ@147 and the HQ@158 IFV group onto the sector 2 defenders. Direction stays south to north.

## MP_SUBSURFACE
No vehicle spawners at all (HQ/CP only). Direction undetermined; listed west to east (arbitrary). 6 Sector markers form 4 sectors (operator layout 2/1/1/2): S1 = S145 (CP73, CP57), S2 = S147 (CP70), S3 = S53+S84 merged (CP138), S4 = S105+S193 merged (CP135, CP66); the chain ends with the 2-point sector.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| S145 (box1; poly60/188/199) | CP73, CP57 (poly5/208, west) | HQ@92 | none | n/a | n/a |
| S147 (poly69/196/3) | CP70 | HQ@110, HQ@16 | none | n/a | n/a |
| S53 (boxes 174,2) + S84 (box2) | CP138 | HQ@68, HQ@80, HQ@120 | none | n/a | n/a |
| S105 (box8) + S193 (poly131/4) | CP135, CP66 | HQ@48 | none | n/a | n/a |
| Outer HQs | none | HQ@180 (-260,107) west, HQ@116 (273,-127) east | none | candidate start bases, side unknown | Low |

Anomalies: S53+S84 share box2 and S105+S193 share poly131 (split or duplicate markers). Totals: 0 spawner classes.

### Per-phase vehicles (attack vs defense)

No vehicle spawners.

## MP_TUNGSTEN
Chain (low-med): west to east. Attackers start west (HQ@39, LightTransport+Tank+IFV); defenders' final base east (HQ@199, Tank+IFV). Both ends are nearly equal, so direction is a guess. Operator layout 2/2/2 with 3 sectors: S75 and S139 are merged into one middle sector. Order S217 -> S75+S139 -> S32.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Atk start base (poly224) | none | HQ@39 | Tank x1 (@137), IFV x1 (@281), LightTransport x1 (@5) | Atk | Med |
| 1: S217 (poly13; box6 sub-area) | CP71 (box6), CP186 (box5) | HQ@218 | Tank x1 (@80), IFV x1 (@196) | Def | Med |
| 2: S75 + S139 merged (box1, poly322) | CP311, CP178 (boxes 179,4) | HQ@116, HQ@312 | LightTransport x2 (@131, @271), IFV x1 (@215), Tank x1 (@328) | Def | Med |
| 3: S32 (poly266) | CP23 (box3), CP287 (box2) | HQ@110 | Tank x1 (@25), IFV x1 (@30) | Def | Med |
| Def final base (east, poly295) | none | HQ@199 | Tank x1 (@214), IFV x1 (@298) | Def (or Atk if reversed) | Low |

Anomalies: S75 and S139 share poly322; every sector has spawners. Totals: VehicleSpawner 13 (Tank5, IFV5, LightTransport3). 3 classes.

### Per-phase vehicles (attack vs defense)

Pads grouped by HQ (from bt-hq-groups.txt). Emplacements (HMG/AT) counted as defenders' assets of the HQ group they belong to.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 (S217) | HQ@39: Tank x1, IFV x1, LT x1 | HQ@218: Tank x1, IFV x1 | Direction low confidence |
| 2 (S75+S139) | HQ@218: Tank x1, IFV x1 | HQ@116: LT x2; HQ@312: IFV x1, Tank x1 | Merged sector; both defender HQs in one phase |
| 3 (S32) | HQ@116: LT x2; HQ@312: IFV x1, Tank x1 | HQ@110: Tank x1, IFV x1; final HQ@199: Tank x1, IFV x1 | Defenders total Tank x2, IFV x2 |
| Unassigned |  |  | none |

### Patch-note check (1.1.3.0)

The Mirak Valley notes (all pads attackers', sector 1 attackers Tank x2 + IFV x1, sectors 2 and 3 an IFV each) could not be matched to a map: Mirak Valley is not identified among the maps in this batch, and MP_TUNGSTEN (4 sectors, no HQ group with Tank x2 + IFV x1, LT x2 at HQ@116) does not fit. No change made.

