# Review C: MP_CONTAMINATED, MP_ISOLATED, MP_GOLMUDRAILWAY

Checked against ../bt-hq-groups.txt. The model hands an HQ over: a phase-N defender HQ becomes the phase-(N+1) attacker HQ. I treat that reuse as the stated reason, not as double use.

## MP_CONTAMINATED
Verdict: minor fixes

- Counts: all HQ-group cells match bt-hq-groups. HQ@209 has LT 1, APC 1, Tank 1, Dirt 1. HQ@97 has Tank 1, APC 1, Dirt 2, AT 2. HQ@390 has LT 1, APC 1, HMG 1, AT 1. HQ@155 + HQ@262 together have Tank 1, LT 3, IFV 1, Dirt 2, AT 1, HMG 1. HQ@98 has LT 1. HQ@8 has IFV 1, HMG 1, AT 1. HQ@368 has no pads. Nothing is invented.
- HQ coverage: all 12 HQs appear. HQ@443 or HQ@390 is left as an "either/or" for phase-3 attackers. Both lie on the Sector@181 side, 31 m and 56 m from it, and HQ@210 is also there. The model gives no rule for picking one, so the choice is arbitrary. Assign one and list the other in the unassigned row by name.
- Direction: SE to NW fits the geometry. HQ@209 is the only base with pads, and HQ@368 at the NW end has none. With @377 and @277 merged, that gives 5 sectors, which matches the in-game count.
- Sample (Pax defenders at S2: Dirt 1, LT 2) does not fit HQ@210 (Dirt 1 only). It is larger than that group, so by the brief's rule it is an error, not just unresolved. No single HQ holds Dirt 1 + LT 2. The only S2-side group with any LT is HQ@390 (LT 1). Only HQ@155 has LT 2, and it sits at sector 3. The sample is a subset of the union HQ@210 + HQ@155. Either the S3 HQ is live for defenders in phase 2, or the LT pads are assigned to a different HQ than the nearest one. The current data can't settle which; this needs an in-game check.
- Stale first-section statements:
  - "Sector markers: 6 ... kept as two": the HQ table merges them.
  - The start-base row says Tank 2, Dirt 2; HQ@209 has Tank 1, Dirt 1.
  - The S1 row says APC 1, Dirt 1; HQ@97 has Tank 1, APC 1, Dirt 2.
  - The anomaly line "S6 has the only IFV" is wrong: HQ@155 has IFV 1, and the totals say IFV 2.
- Low confidence on S3/S4: I agree they are a single sector. Resolve it by treating HQ@155 + HQ@262 as one defender group, as the table already does.

Corrected row:
| 3 | HQ@390: LT 1, APC 1, HMG 1, AT 1 | HQ@155 + HQ@262: Tank 1, LT 3, IFV 1, Dirt 2, AT 1, HMG 1 | HQ@443 (Dirt 2, Tank 1, AT 1) unassigned |
| 2 | HQ@97: Tank 1, APC 1, Dirt 2 | HQ@210: Dirt 1 | sample Dirt 1 + LT 2 exceeds group (LT 2 only in HQ@155): error vs model |

## MP_ISOLATED
Verdict: minor fixes

- Counts: all cells match. HQ@150 has RHIB 2, Dirt 1, Quad 2, APC 1, LT 1. HQ@316 has Quad 2, RHIB 3, LT 1, APC 1. HQ@3 has LT 1, RHIB 1, Quad 2, Dirt 1. HQ@132 has LT 2, Quad 1, Dirt 1. HQ@76 has LT 1, RHIB 1, Quad 1. HQ@31 has LT 1, IFV 1, PatrolBoat 1, Quad 1, RHIB 1. HQ@336 has LT 2, Dirt 1, Quad 1, HMG 1. HQ@133 has LT 1, RHIB 2, PatrolBoat 1, IFV 1, Quad 2, AT 1.
- HQ coverage: all 8 HQs appear once, with HQ@316 handed over between phases 1 and 2. Handover is broken after that: HQ@3 defends phase 2 but is not the phase-3 attacker (HQ@132 is used instead), and HQ@76 defends phase 3 but HQ@31 attacks phase 4. The table should say why.
- Geometry order runs south to north: Sector@188 (z -219), @36 (z -21), @168 (z 140), @169 (z 413). HQ@31 (z 223, 38 m from CP@338 of S3) is on the defenders' side of S3. It is a plausible phase-3 defender alongside HQ@76, rather than only a phase-4 attacker.
- Sample: Pax attacking fits team 1 = Pax, and S-to-N fits.
  - S2 attackers (APC 1, LT 1, RHIB 2, Quad 2) are a subset of HQ@316. That fits.
  - S1 attackers (Dirt 2) exceed HQ@150 (Dirt 1). The sample is larger than the group, so by the brief's rule this is an error, not just "unexplained". HQ@316 has no Dirt, so even HQ@150 + HQ@316 doesn't explain it. The extra Dirt comes from some other pad.
- Stale first-section statements:
  - "direction is ambiguous ... Reverse order is equally plausible": the sample settles the direction.
  - The S4 row says "none" for vehicles, but HQ@336 (63 m from Sector@169) has LT 2, Dirt 1, Quad 1, and the HQ table uses it for phase 4.
  - The start-base row's "Medium (direction)" is also outdated.

Corrected row:
| 1 | HQ@150 (start): RHIB 2, Dirt 1, Quad 2, APC 1, LT 1 | HQ@316: Quad 2, RHIB 3, LT 1, APC 1 | sample Dirt 2 exceeds group Dirt 1: error vs model, source of second Dirt unknown |

## MP_GOLMUDRAILWAY
Verdict: minor fixes

- Counts: all cells match. HQ@269 has LT 2, APC 1, Dirt 2, IFV 2, Tank 1, AtkPlane 2. HQ@271 has APC 2, Dirt 2, LT 1, Tank 2, ScoutHeli 1. HQ@111 has its 15 pads exactly. HQ@48 has APC 1, Dirt 5, IFV 3, LT 1, Tank 1, HMG 1. HQ@306 has Quad 2, Dirt 1, IFV 1, HMG 1. HQ@154 has IFV 2, Dirt 1, LT 2, AT 2. HQ@328 and HQ@261 have no pads.
- HQ coverage: all 8 appear, and the handover chain is consistent: @271, then @111, then @48.
- Contradiction on the planes: the unassigned row says AttackPlane @177/@257 "belong to no HQ". bt-hq-groups puts them in HQ@269 (AtkPlane 2, maxdist 911 m), and the phase-1 row counts them there.
- Sample, attackers S2 (AtkPlane 1, ScoutHeli 1, Tank 2, APC 2, LT 1, Dirt 2): HQ@271 matches exactly, plus 1 plane. That plane is not in HQ@271, so the sample exceeds the group. It fits only if HQ@269's plane pads stay live after phase 1. That is a deviation from the model, and the result should call it one rather than "matches".
- Sample, defenders S2 (Dirt 2, LT 1, Tank 1, IFV 1): a subset of HQ@111. That fits.
- Direction: S to N fits the sample, and the 4 CP clusters give 4 sectors as in-game. S1 is CP@71/@99 (z ~250), S2 is CP@301/@212 (z 440-548), S3 is CP@158 (z 685), S4 is CP@321/@348 (z 851-909). That clustering resolves the author's low confidence about the markers: Sector@272/@280 sit at the attackers' start (HQ@269), and @89 is a stray. Neither is a sector in the chain.
- Stale first-section statements:
  - The intro sentence contradicts itself: "attackers start at HQ@269 (old note: N to S from poly64)", then "(z ~975, HQ@154 ...)", then "defenders' final stand is the S end (poly107, HQ@269)".
  - The area table runs N to S with 5 phases, and its start base is poly64/HQ@154.
  - Its P5 row (HQ@269: IFV 1, no planes) differs from the group (IFV 2, AtkPlane 2).
  - The anomaly line counts the planes as strays outside every HQ.
  - Mark the whole first section superseded, or drop it.

Corrected rows:
| 2 | HQ@271: APC 2, Dirt 2, LT 1, Tank 2, ScoutHeli 1 (+ AtkPlane from HQ@269 per sample) | HQ@111: ... | sample exceeds HQ@271 by AtkPlane 1: start-HQ planes stay live, deviation from model |
| Unassigned | HQ@328, HQ@261: none | | AttackPlane @177/@257 are in HQ@269's group (maxdist 911 m) |
