"""Group Breakthrough vehicle pads by nearest HQ per map (from bt-maps.json)."""
import json, sys, pathlib, math, collections
sp = pathlib.Path(sys.argv[1])
maps = json.load(open(sp / 'bt-maps.json'))
SHORT = {'GMPF_VehicleSpawner_LightTransport': 'LT', 'GMPF_VehicleSpawner_IFV': 'IFV', 'GMPF_VehicleSpawner_Tank': 'Tank',
         'GMPF_VehicleSpawner_MobileAA': 'MobAA', 'GMPF_VehicleSpawner_AttackPlane': 'AtkPlane', 'GMPF_VehicleSpawner_FighterPlane': 'Fighter',
         'GMPF_VehicleSpawner_AttackHelicopter': 'AtkHeli', 'GMPF_VehicleSpawner_TransportHelicopter': 'TrHeli',
         'GMPF_VehicleSpawner_PTV_QuadBike': 'Quad', 'GMPF_VehicleSpawner_APC': 'APC', 'GMPF_VehicleSpawner_PTV_GolfCart': 'Cart',
         'GMPF_VehicleSpawner_RHIB': 'RHIB', 'GMPF_VehicleSpawner_ScoutHelicopter': 'ScoutHeli', 'GMPF_VehicleSpawner_PTV_DirtBike': 'Dirt',
         'GMPF_VehicleSpawner_PatrolBoat': 'PatrolBoat', 'GMPF_VehicleSpawner_MultirolePlane': 'Multirole', 'GMPF_VehicleSpawner_NavalFighterPlane': 'NavalFighter',
         'GMPF_VehicleSpawner_Forward': 'Fwd', 'GMPF_StationarySpawner_HMG': 'HMG', 'GMPF_StationarySpawner_AntiTank': 'AT',
         'GMPF_StationarySpawner_AntiAircraft': 'AA', 'GMPF_AutomaticAA': 'AutoAA'}
def short(v):
    if v is None: return '?'
    if 'CarrierJetLaunch' in v: return 'CarrierJet'
    return SHORT.get(v, v.replace('GMPF_VehicleSpawner_', ''))
PADS = ('GEM_VehicleSpawner', 'GEM_VehicleSpawner_Forward', 'GEM_StationarySpawner', 'GEM_AutomaticAA')
out = []
for m, rec in maps.items():
    inst = rec['instances']
    hqs = [x for x in inst if x['gem'] == 'GEM_HQ']
    secs = [x for x in inst if x['gem'] == 'GEM_Sector']
    cps = [x for x in inst if x['gem'] == 'GEM_CapturePoint']
    pads = [x for x in inst if x['gem'] in PADS]
    def d(a, b): return math.hypot(a['pos'][0] - b['pos'][0], a['pos'][2] - b['pos'][2])
    groups = collections.defaultdict(list)
    for p in pads:
        if not hqs: continue
        h = min(hqs, key=lambda h: d(h, p)); groups[h['idx']].append((p, d(h, p)))
    out.append(f'===== {m}  HQs={len(hqs)} sectors={len(secs)} CPs={len(cps)} pads={len(pads)}')
    for h in sorted(hqs, key=lambda h: (h['pos'][0], h['pos'][2])):
        g = groups.get(h['idx'], [])
        cnt = collections.Counter(short(p['variant']) for p, _ in g)
        far = max((dd for _, dd in g), default=0)
        nsec = min(secs, key=lambda s: d(s, h)) if secs else None
        ncp = min(cps, key=lambda c: d(c, h)) if cps else None
        out.append(f"  HQ@{h['idx']:<4} pos=({h['pos'][0]:7.1f},{h['pos'][2]:7.1f}) pads={sum(cnt.values()):2d} maxdist={far:5.0f}  {dict(cnt)}  nearestSector=@{nsec['idx'] if nsec else '-'} ({d(nsec,h):.0f}m)  nearestCP=@{ncp['idx'] if ncp else '-'} ({d(ncp,h):.0f}m)")
    for s in secs:
        out.append(f"  Sector@{s['idx']} pos=({s['pos'][0]:7.1f},{s['pos'][2]:7.1f}) boxes={s['inBoxes']}")
    for c in cps:
        nh = min(hqs, key=lambda h: d(h, c)) if hqs else None
        out.append(f"  CP@{c['idx']} pos=({c['pos'][0]:7.1f},{c['pos'][2]:7.1f}) nearestHQ=@{nh['idx'] if nh else '-'} ({d(nh,c):.0f}m)")
(sp / 'bt-hq-groups.txt').write_text('\n'.join(out), encoding='utf-8')
print('\n'.join(l for l in out if l.startswith('=====') or l.startswith('  HQ@')))
