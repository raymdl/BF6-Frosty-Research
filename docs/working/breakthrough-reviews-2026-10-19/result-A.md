# Breakthrough chains: batch A

Numbers are the instance index after "@" in the map files. Side rule: spawners in the sector being attacked serve defenders, spawners in the previously captured sector or the start base serve attackers.

## MP_ABBASID
Chain runs west to east along x. Attackers (team1 = Coalition) start at the west base, POLY21@21, which holds HQ313 plus APC104 and IFV167 and lies outside every sector box. Confidence in direction: high.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Start base (POLY21@21, no sector box) | none | HQ313 | APC x1 (104), IFV x1 (167) | Attackers during sector 1 | High |
| S1 = Sector@187, BOX253 + BOX218 (split box, z -75..23 and 23..134) | CP50, CP102 | HQ33 (in 218) | IFV x1 (61) | Defenders | Medium: only one spawner |
| S2 = Sector@311, BOX265 | CP71 | HQ8, HQ63 (adjacent pair) | APC x1 (119), IFV x1 (180) | Defenders while S2 is attacked, attackers once S2 is captured | Medium |
| S3 = Sector@221, BOX105 + BOX152 (split, z -18..79 and -126..-18) | CP284 (105), CP276 (152) | HQ74, HQ283 (152) | IFV x1 (277, in 105) | Defenders | Medium |
| S4 = Sector@95, BOX304 | CP312 | HQ198 (sector HQ), HQ151 (in final-base POLY24@179) | IFV x1 (47, in POLY24@179 with HQ151) | Defenders (final base) | Medium |

Anomalies:
- S1 and S3 are split boxes.
- BOX152 has HQs and a capture point but no spawner.
- The defenders' final base sits inside BOX304 (POLY24@179) rather than beyond it.
- 2 spawner classes: APC x2, IFV x5 (7 spawners).

### Per-phase vehicles (attack vs defense)
Built on HQ pad groups. HQs ordered along the chain; the defenders' HQ of phase N flips to the attackers once sector N is captured (HQ pairs at one spot cannot be told apart, so they are marked unresolved).

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ313: APC x1, IFV x1 | HQ33: IFV x1 |  |
| 2 | HQ33: IFV x1 | HQ8: IFV x1 / HQ63: APC x1 | HQ8 and HQ63 are coincident, one per side unresolved |
| 3 | the one of HQ8/HQ63 not used by defenders | HQ283: IFV x1 / HQ74: none | HQ283 and HQ74 coincident, unresolved |
| 4 | the one of HQ283/HQ74 not used by defenders | HQ151: IFV x1 (final base); HQ198: none |  |
| unassigned | - | - | none; every pad-bearing HQ is used |

Sample check (Siege of Cairo, Pax attacking, sector 1 attackers IFV x1 + APC x1): matches phase 1 attackers HQ313 (APC x1, IFV x1) exactly. Direction and start base confirmed.

Patch-note check (1.1.3.0): "Added an additional Attacker tank in sector 1 and 3". The data has no Tank pad on Abbasid (only APC and IFV), and the later in-game sample (sector 1 attackers IFV x1 + APC x1) also shows no tank. So either a later update removed the added tanks, or this data predates the patch. I cannot tell whether the APC key (9) maps differently; the sample's APC matches HQ313's APC pad, which argues against a remap. Sides unchanged: HQ313 (sector 1 attackers) and HQ33/HQ8/HQ63 groups remain as tabulated.

## MP_AFTERMATH
No boxes exist on this map; everything is polygons. The chain runs along z. The direction is a guess: I picked north (z +110) to south (z -167) with low confidence, because both ends have an HQ-only region with no sector marker. North is POLY18@110 (HQ114, whose pad group is HMG x1, 73 m away). South is POLY33@57 / POLY27@145 (HQ89 plus HMG71). The south end has the only emplacement, which suits a defenders' final base, so I chose north as the attackers' start.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Start base (POLY18@110) | none | HQ114 | HMG x1 (nearest-pad group of HQ114) | Attackers | Low (direction uncertain) |
| S1 = north zone (z -11..108, POLY35@9, POLY29@53). Markers Sector@20 and Sector@95 (both) share identical polygons | CP22, CP87, CP171 | HQ135 | HMG x2 (69, 151); HQ-group view gives HQ135 HMG x1 and HQ114 HMG x1 | Defenders | Low |
| S2 = middle zone (z -63..7, POLY19@150, POLY7@125). Its marker is not clear; Sector@83 lies at its south edge, in POLY29@94 and POLY27@175 as well as the south polygons | CP5, CP50, CP161 | HQ29, HQ176 | HMG x1 (88) | Defenders | Low |
| S3 = south zone (POLY27@108, POLY33@33; z -205..-52) | CP129 | HQ154, HQ157, HQ172 | none | Defenders | Low |
| Final base (POLY33@57 / POLY27@145) | none | HQ89 | HMG x1 (71) | Defenders | Low |

Anomalies:
- 3 sector markers cover only 2 distinct polygons on the north side (Sector@20 and Sector@95 are duplicates).
- Sector@83 straddles the middle and south zones.
- There are no vehicle spawners at all, only 4 HMG StationarySpawners. Spawner classes: HMG x4.
- The sector order in the table is inferred from capture point groups, not from markers.

### Per-phase vehicles (attack vs defense)
Built on HQ pad groups. HQs ordered along the chain; the defenders' HQ of phase N flips to the attackers once sector N is captured (HQ pairs at one spot cannot be told apart, so they are marked unresolved).

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ114: HMG x1 | HQ135: HMG x1 | direction uncertain |
| 2 | HQ135: HMG x1 | HQ176: HMG x1 / HQ29: none | north-to-south order is a guess |
| 3 | HQ176 / HQ29: HMG x1 or none | HQ89: HMG x1 (final); HQ154, HQ172, HQ157: none |  |
| unassigned | - | - | none |

Objective-count note (operator recalls Empire State as 1/2/1 = 4 objectives; the layer has 7 capture points): proposed live set: S1 = CP171 (-608, 62; nearest HQ135 17 m, in the sector marker area), S2 = CP5 (-639, -38) + CP50 (-556, -31), S3 = CP129 (-594, -113). Extras: CP161 (0.9 m from CP50, a duplicate) and CP22 (-652, 33) + CP87 (-649, 78), the outer north flank points, likely another layout's set. Confidence low: CP22/CP87 versus CP171 for the north point cannot be separated from the data, and CP50 versus CP161 is a coin flip.

## MP_BADLANDS
Direction (operator-confirmed: Pax Armata attacks, samples were recorded from the other side's view): the chain runs west/north-west to east. Attackers start at HQ64 (final base in the forward reading, POLY26@146, no pads); the defenders' final base is the east base POLY10@3 (HQ109, Tank x1, AT x1). The first table below is listed in the old forward order (east to west) and is a spatial inventory only; sector numbers S1 to S3 are reversed for play: sector 1 = Sector@28, sector 2 = Sector@139, sector 3 = Sector@116. The forward per-phase table is superseded. Direction confidence: medium to high (fits all samples).

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Start base (POLY10@3, z -13..136) | none | HQ109 | Tank x1 (143), AntiTank x1 | Attackers during S1 | High |
| S1 = Sector@116, POLY25@108 / POLY5@3 (small boxes 53, 39, 151 are single-CP outlines) | CP1, CP120, CP149 | HQ107 | APC x1 (121), AntiTank x1 | Defenders | Medium |
| S2 = Sector@139, POLY45@45 / POLY33@57 / POLY17@60 / POLY7@2 | CP26 | HQ98 | Tank x1 (157), AntiTank x2 (18, 77), HMG x1 (119) | Defenders | Medium |
| S3 = Sector@28, POLY32@51 / POLY19@63 / POLY9@1 | CP14 | HQ48, HQ135 (POLY13@37, adjacent to S2/S3) | APC x1 (168, POLY13@37) | Defenders (APC168 may also serve attackers after S2 is captured) | Low to medium |
| Final base (POLY26@146) | none | HQ64 | none | Defenders | Medium |

Anomalies:
- APC168 and HQ48/HQ135 sit in POLY13@37, between S2 and S3, and overlap S3's POLY32@51.
- The final base (HQ64) has no spawners.
- The two AntiTank spawners at S1 split between HQ109 and HQ107 by the HQ-group data (loosest assignments on the map, 96-97 m).
- Spawner classes: Tank x2, APC x2, AntiTank x4, HMG x1 (4 vehicle and 5 stationary spawners).

### Per-phase vehicles (attack vs defense) -- SUPERSEDED forward chain, kept for reference only
Built on HQ pad groups. HQs ordered along the chain; the defenders' HQ of phase N flips to the attackers once sector N is captured (HQ pairs at one spot cannot be told apart, so they are marked unresolved).

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ109: Tank x1, AT x1 | HQ107: APC x1, AT x1 |  |
| 2 | HQ107: APC x1, AT x1 | HQ98: Tank x1, AT x2, HMG x1 |  |
| 3 | HQ98: Tank x1, AT x2, HMG x1 | HQ135: APC x1; HQ48: none; HQ64 (final): none | HQ135 is closest to S3 but 96m from its marker |
| unassigned | - | - | none |

### Per-phase vehicles (attack vs defense) -- MAIN (reversed chain)
Operator confirmed Pax attacking, so the reversed chain fits all three samples (none, none, APC x1; "none" is weak evidence). Start HQ64; HQ135/HQ48 are a pair near sector 1/2; final base HQ109.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ64: none | HQ48: none (HQ135 is the pair partner) | matches sample |
| 2 | HQ135: APC x1 | HQ98: Tank x1, AT x2, HMG x1 | matches sample |
| 3 | HQ98: Tank x1, AT x2, HMG x1 | HQ107: APC x1, AT x1 | |
| final | - | HQ109: Tank x1, AT x1 (final base) | |

## MP_CAPSTONE
Direction (fixed by an in-game sample: NATO attackers had Tank x1 + IFV x1 in both sector 1 and sector 2, which only HQ184 and HQ205 match): the chain runs from the west base to the north-east. Attackers start at POLY31@73 (HQ184, outside every box); the defenders' final base is POLY34@215 (HQ2). Confidence: high. Only Sector@48 and Sector@75 are real markers. Sector@46, @94 and @103 sit at the same coordinates as Abbasid Sector@95, @311 and @221 and are stray copies, so sectors 2 to 4 are taken from boxes and have no valid marker.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Start base (POLY31@73) | none | HQ184 | IFV x1 (84), Tank x1 (320) | Attackers during S1 | High (sample) |
| S1 = Sector@75, BOX5 / POLY21@123 | CP304 | HQ205 | IFV x1 (10), Tank x1 (160) | Defenders in S1, attackers in S2 | High (sample) |
| S2 = BOX2 + BOX1 / POLY35@116 (split, no valid marker) | CP3 (BOX2), CP77 (BOX1) | HQ213, HQ263 (same position) | IFV x1 (165), Tank x1 (169) | Defenders | Medium |
| S3 = BOX6 + BOX7 / POLY45@209 (split, no valid marker) | CP51 (BOX6), CP42 (BOX7) | HQ189, HQ272 | IFV x1 (179) | Defenders | Medium |
| S4 = BOX4 / POLY53@144 (no valid marker) | CP155 | HQ246, HQ266 | IFV x1 (290), QuadBike x2 (65, 240) | Defenders | Medium |
| S5 = Sector@48, BOX3 / POLY29@308 | CP41 | HQ188 | IFV x1 (93), LightTransport x1 (235), QuadBike x1 (126) | Defenders | Medium |
| Final base (POLY34@215) | none | HQ2 | IFV x1 (12), LightTransport x1 (185), QuadBike x2 (249, 277) | Defenders | Medium |

Anomalies:
- S2 and S3 are split boxes.
- Sector@46, @94 and @103 are stray markers.
- HQ213 and HQ263 duplicate each other.
- 4 spawner classes: IFV x7, Tank x3, QuadBike x5, LightTransport x2 (17 spawners).

### Per-phase vehicles (attack vs defense)
Note: the in-game sample (NATO attackers Tank x1 + IFV x1 in sectors 1 and 2) forced the west-to-north-east direction used above.

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ184: IFV x1, Tank x1 (start base, west) | HQ205: IFV x1, Tank x1 |  |
| 2 | HQ205: IFV x1, Tank x1 | HQ213: IFV x1, Tank x1 / HQ263: none | HQ213 and HQ263 share a position |
| 3 | HQ213 / HQ263 (the one not used by defenders) | HQ189: IFV x1 / HQ272: none | 12 m apart; same ambiguity |
| 4 | HQ189 / HQ272 (the one not used by defenders) | HQ246: IFV x1 / HQ266: Quad x2 | HQ246 and HQ266 are 35 m apart; both could be defenders' HQs |
| 5 | HQ246 / HQ266 (the one not used by defenders) | HQ188: IFV x1, LT x1, Quad x1; HQ2 (final): IFV x1, LT x1, Quad x2 | defenders total IFV x2, LT x2, Quad x3 |
| unassigned | - | - | none |

Patch-note check (1.1.3.0): Sector 3 "Removed Defender tank": agrees, phase 3 defenders (HQ189 IFV x1 / HQ272 none) hold no tank. Sector 5 "Added 2 Attacker IFVs; removed the Defender transport": does not agree with this data. Phase 5 attackers (HQ246 IFV x1 / HQ266 Quad x2) hold at most 1 IFV, and the phase 5 defenders (HQ188, HQ2) still have a LightTransport. No HQ-side or direction change fits both statements (the in-game samples fix the direction), so the data most likely predates the patch, or a later update changed it again. No table change.

Sector-count note (operator remembers 1/2/2/1 objectives, the match log said 5 sectors): the data's 1/2/2/1/1 fits the 5-sector log, so it is kept. The 1/2/2/1 recollection may have merged the last two single-point sectors.

## MP_DUMBO
The chain runs from east (x about 200) to west. Attackers start at POLY16@95 (HQ17, outside every sector box), which touches Sector@189's POLY13@235. The defenders' final base is POLY13@238 in the far west (HQ123). Direction confidence: high.

| Phase/Sector | Capture points | HQs | Vehicle spawners | Likely side | Confidence |
|---|---|---|---|---|---|
| Start base (POLY16@95) | none | HQ17 | IFV x1 (197), LightTransport x1 (234), QuadBike x1 (232) | Attackers during S1 | High |
| S1 = Sector@189, POLY13@235 / POLY10@110, BOX4 + BOX5 (CP outlines) | CP176 (BOX5/206), CP241 (BOX4/122) | HQ111 (BOX4) | IFV x1 (126) | Defenders | Medium |
| S2 = Sector@73, BOX1 / POLY14@98 / POLY18@91 | CP202 (BOX1), CP9 (BOX3) | HQ93, HQ194 | IFV x1 (208), QuadBike x2 (90, 146), AntiTank x1 (25, BOX3) | Defenders | High |
| S3 = Sector@243, POLY15@84 / POLY9@100 / POLY22@193 | CP8 | HQ24 | IFV x1 (141), QuadBike x2 (128, 173), HMG x1 (179) | Defenders | High |
| Final base (POLY13@238) | none | HQ123 | none | Defenders | Medium |

Anomalies:
- Sector@189 and Sector@243 lie in no box; they are in polygons only.
- The final base has no spawners.
- Spawner classes total 5: IFV x4, QuadBike x5, LightTransport x1, AntiTank x1, HMG x1 (10 vehicle and 2 stationary spawners).

### Per-phase vehicles (attack vs defense)
Built on HQ pad groups. HQs ordered along the chain; the defenders' HQ of phase N flips to the attackers once sector N is captured (HQ pairs at one spot cannot be told apart, so they are marked unresolved).

| Phase | Attackers' HQ and vehicles | Defenders' HQ and vehicles | Note |
|---|---|---|---|
| 1 | HQ17: IFV x1, LT x1, Quad x1 | HQ111: IFV x1 |  |
| 2 | HQ111: IFV x1 | HQ93: IFV x1, Quad x2 / HQ194: AT x1 | HQ93 and HQ194 are 55 m apart; both could be defenders' HQs; HQ93 is closer to Sector@73 |
| 3 | the one of HQ93/HQ194 not used by defenders | HQ24: IFV x1, Quad x2, HMG x1; HQ123 (final): none |  |
| unassigned | - | - | none |

Note: an in-game sample showed no vehicles on either side in Dumbo sector 1; the table above does not match it (possible phase-1 enabler effect).

Patch-note check (1.1.3.0, Manhattan Bridge = MP_DUMBO): "Removed Defender vehicles in Sector 2 and 3; added an Attacker IFV in Sector 3". The pair in phase 2 resolves with the note: HQ194 (AT emplacement only) is the sector 2 defenders' HQ, HQ93 (IFV x1, Quad x2) is the phase 3 attackers' HQ, which gives the sector 3 attackers an IFV (agrees). Sector 3 defenders (HQ24: IFV x1, Quad x2, HMG x1) still hold vehicles in this data, which contradicts the note, so the data likely predates the patch or a later update changed it. Reversing the chain does not help (the sector 2 and 3 defenders would then be HQ94/HQ93 and HQ111/HQ17, all with vehicles). No direction change; table kept with HQ194 = phase 2 defenders, HQ93 = phase 3 attackers.
