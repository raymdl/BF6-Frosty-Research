# Result C: MP_CONTAMINATED, MP_ISOLATED, MP_GOLMUDRAILWAY

Abbrev: LT = LightTransport, Dirt/Quad = PTV_DirtBike/QuadBike. Grouping is by HQ pad group (bt-hq-groups.txt); HMG/AT/AA are emplacements counted with the nearest HQ. The earlier area-based sector tables were removed because they disagreed with the HQ groups.

## MP_CONTAMINATED
Chain runs SE to NW: start HQ@209 (SE, x~440), final HQ@368 (NW, no pads). Team1 = Alliance/NATO attackers. In-game it has 5 sectors, so Sector@377 and @277 (20 m apart) are one sector: S1 Sector@226 (CP@183), S2 Sector@181 (CP@52, @82), S3 Sector@377/@277 (CP@452, @75, @309), S4 Sector@180 (CP@231, @351), S5 Sector@9 (CP@228). Totals: 23 vehicle pads (Dirt 8, LT 6, Tank 4, APC 3, IFV 2) and 9 emplacements (HMG 3, AT 6); no pads outside every poly. Direction: medium-high.

### Per-phase vehicles (attack vs defense)

Sample: Pax defenders at sector 2 had Dirt 1 + LT 2 only. No single HQ holds that (HQ@210 Dirt 1; HQ@155 LT 2 with Tank 1, IFV 1, AT 1). It is a subset only of the union HQ@210 + HQ@155, so it exceeds any single group: either the S3 HQ@155 is live for defenders in phase 2 or the LT pads belong to another HQ. Needs an in-game check.

| Phase | Attackers' HQ (index) and vehicles | Defenders' HQ (index) and vehicles | Note |
|---|---|---|---|
| 1 | HQ@209 (start): LT 1, APC 1, Tank 1, Dirt 1 | HQ@97: Tank 1, APC 1, Dirt 2, AT 2 | |
| 2 | HQ@97: Tank 1, APC 1, Dirt 2 | HQ@210: Dirt 1 | sample Dirt 1 + LT 2 exceeds the group (fits only HQ@210 + HQ@155 together): error vs model |
| 3 | HQ@390: LT 1, APC 1, HMG 1, AT 1 | HQ@155 + HQ@262: Tank 1, LT 3, IFV 1, Dirt 2, AT 1, HMG 1 | HQ@390 vs HQ@443 as attackers is arbitrary: both lie on the Sector@181 side (56 m and 31 m) and the model has no rule to pick; HQ@443 (Dirt 2, Tank 1, AT 1) listed unassigned |
| 4 | HQ@155 + HQ@262 (handed over): Tank 1, LT 3, IFV 1, Dirt 2, AT 1, HMG 1 | HQ@98: LT 1 | |
| 5 | HQ@98: LT 1 | HQ@8: IFV 1, HMG 1, AT 1; final HQ@368: none | |
| Unassigned | HQ@443: Dirt 2, Tank 1, AT 1; HQ@47, HQ@256: none | | |

### Capture-point layouts (operator 1/2/2/1 vs log 5 sectors)

Positions (x,z): CP@183 (264,211); CP@52 (109,183); CP@82 (154,89); CP@75 (25,99); CP@452 (-4,57); CP@309 (-27,39); CP@231 (-138,-17); CP@351 (-89,-118); CP@228 (-141,-252). Near-duplicates: CP@452 and CP@309 are 33 m apart and each sits on one of the two merged markers (Sector@377 exact, Sector@277 within 9 m); CP@75 is ~50 m from CP@452 and has its own box7 with HQ@155 at 13 m. CP@351 has its own box (253/5) and poly with HQ@47 but no Sector marker, 120-135 m from its neighbours CP@231 and CP@228. The current table (1/2/3/2/1) is unchanged.
- 4-sector reading (1/2/2/1, 6 points): CP@183 | CP@52, CP@82 | CP@75, CP@309 | CP@228. Extras: CP@452 (duplicate of CP@309's site), CP@231 and CP@351 (the Sector@180 pair, whose HQ@98 has only LT 1). Low confidence; which of the middle trio is dropped is arbitrary.
- 5-sector reading (1/2/2/2/1, 8 points): CP@183 | CP@52, CP@82 | CP@75, CP@309 | CP@231, CP@351 | CP@228. Extra: CP@452 only (one of the near-duplicate pair; CP@309 could be dropped instead). Medium confidence; this matches the log with 8 of the 9 points.

## MP_ISOLATED
Chain runs S to N (Sector@188, @36, @168, @169; z -219 to 413), start HQ@150 (poly310), final HQ@133 (poly155). Team1 = Coalition/Pax Armata attackers. Direction is settled by the Tsuru Reef samples (medium-high). Totals: 42 vehicle pads (LT, Quad, RHIB, Dirt, APC, IFV, PatrolBoat) and 2 emplacements (HMG, AT). S4 (Sector@169) has HQ@336 (LT 2, Dirt 1, Quad 1, HMG 1) beside it, plus the final HQ@133.

### Per-phase vehicles (attack vs defense)

Samples (Pax attacking): S1 attackers APC 1, LT 1, RHIB 2, Quad 2, Dirt 2; S2 attackers APC 1, LT 1, RHIB 2, Quad 2. S2 is a subset of HQ@316 (RHIB 3). S1 matches HQ@150 except Dirt (sample 2 vs group 1): the extra dirt bike is not covered by HQ@150, and HQ@316 has none, so its source is unknown (error vs model).

| Phase | Attackers' HQ (index) and vehicles | Defenders' HQ (index) and vehicles | Note |
|---|---|---|---|
| 1 | HQ@150 (start): RHIB 2, Dirt 1, Quad 2, APC 1, LT 1 | HQ@316: Quad 2, RHIB 3, LT 1, APC 1 | sample Dirt 2 exceeds HQ@150 Dirt 1; source of second dirt bike unknown |
| 2 | HQ@316: Quad 2, RHIB 3, LT 1, APC 1 | HQ@3: LT 1, RHIB 1, Quad 2, Dirt 1 | |
| 3 | HQ@132: LT 2, Quad 1, Dirt 1 | HQ@76 + HQ@31: LT 2, RHIB 2, Quad 2, IFV 1, PatrolBoat 1 (HQ@76: LT 1, RHIB 1, Quad 1; HQ@31: LT 1, IFV 1, PatrolBoat 1, Quad 1, RHIB 1) | handover breaks after phase 2 (HQ@3 is not reused): HQ@132 and HQ@76 both lie between S2 and S3, HQ@31 (38 m from CP@338) is on S3's defender side, so it is a plausible phase-3 defender as well as the phase-4 attacker |
| 4 | HQ@31: LT 1, IFV 1, PatrolBoat 1, Quad 1, RHIB 1 | HQ@336: LT 2, Dirt 1, Quad 1, HMG 1; final HQ@133: LT 1, RHIB 2, PatrolBoat 1, IFV 1, Quad 2, AT 1 | final base joins in last phase |
| Unassigned | none | | all 8 HQs used |

### Patch-note check (1.4.3.0)

Capture points per sector in the chain from MP_ISOLATED.txt: S1 Sector@188 has 2 (CP@217, @246), S2 Sector@36 has 2 (CP@134, @272), S3 Sector@168 has 2 (CP@97, @338), S4 Sector@169 has 1 (CP@45); 7 total. The chain is unchanged by this check.
- S1: agrees. Attackers HQ@150 has APC 1 (and RHIB 2, matching the 2 added RHIBs); 2 capture points (A and B). HQ@150 still lists LT 1 beside the APC, which the notes do not explain (it could be a second LT pad).
- S2: agrees. Attackers HQ@316 has APC 1; defenders HQ@3 has Quad 2; 2 capture points. HQ@3 still has LT 1.
- S3: agrees, with a caveat. Attackers HQ@132 has LT 2 and no APC; defenders HQ@76 + HQ@31 have no APC. The data shows 2 capture points, which fits an added point only if the old S3 had 1; 3 would make 8 total against the 7 in the file, so 2 is the supported count.
- S4: agrees. 1 capture point (CP@45); defenders HQ@336 and HQ@133 have no APC.

## MP_GOLMUDRAILWAY
Chain runs S to N, confirmed 4 sectors in-game, NATO attacking (default factions): start HQ@269 (south), S1 CP@71/@99 (HQ@271, Sector@267), S2 CP@301/@212 (HQ@111), S3 CP@158 (HQ@48), S4 CP@321/@348 (HQ@306), final HQ@154. Sector@272 and @280 sit at the attackers' start (HQ@269) and Sector@89 is a stray; none is a chain sector. Totals: 51 vehicle pads (including the two stray-position AttackPlane pads, which belong to HQ@269, and a dummy IFV at 0,0,0 from Breakthrough_Cover) and 6 emplacements (HMG 2, AT 3, AA 1): 11 spawner classes.

### Per-phase vehicles (attack vs defense)

| Phase | Attackers' HQ (index) and vehicles | Defenders' HQ (index) and vehicles | Note |
|---|---|---|---|
| 1 | HQ@269 (start, south): LT 2, APC 1, Dirt 2, IFV 2, Tank 1, AtkPlane 2 | HQ@271: APC 2, Dirt 2, LT 1, Tank 2, ScoutHeli 1 | HQ@271 is on Sector@267 |
| 2 | HQ@271: APC 2, Dirt 2, LT 1, Tank 2, ScoutHeli 1, plus AtkPlane 1 from HQ@269 | HQ@111 (HQ@261 twin has no pads): Dirt 2, Tank 1, AA 1, ScoutHeli 1, APC 1, Quad 2, IFV 2, LT 4, AT 1 | sample exceeds HQ@271 by AtkPlane 1: the start HQ's plane pads stay live at sector 2 (deviation from the model). Defenders' sample (Dirt 2, LT 1, Tank 1, IFV 1) is a subset of HQ@111. Medium |
| 3 | HQ@111: as above | HQ@48 (HQ@328 twin none): APC 1, Dirt 5, IFV 3, LT 1, Tank 1, HMG 1 | |
| 4 | HQ@48: as above | HQ@306: Quad 2, Dirt 1, IFV 1, HMG 1; final HQ@154: IFV 2, Dirt 1, LT 2, AT 2 | final base joins in last phase |
| Unassigned | HQ@328, HQ@261: none | | duplicate twins at the same position as HQ@48 and HQ@111; AttackPlane @177/@257 (z -664/-789) are in HQ@269's group (maxdist 911 m) |
