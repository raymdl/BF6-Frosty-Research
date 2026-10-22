"""Per-map Breakthrough extraction from decoded raw layers (bt.json).
Writes bt-maps.json and bt-maps.txt in the scratchpad."""
import json, sys, pathlib, collections, re
sp = pathlib.Path(sys.argv[1])
cat = json.load(open(r'C:\Users\royal\Documents\BF6 Datamining\builds\2.1.1.0\capture\collection\asset-catalog.json'))
g2p = {x['guid']: x['path'] for x in cat['assets']}
d = json.load(open(sp / 'decoded' / 'bt.json'))['assets']
d.update(json.load(open(sp / 'decoded' / 'globals.json'))['assets'])
NAMES = {int(k): v for k, v in json.load(open(sp / 'mi-names.json')).items()}
table = json.load(open(sp / 'gem-variant-table.json'))
FACTION = {607944106: 'Alliance/NATO', -1865993703: 'Coalition/Pax Armata'}
TEAM_SLOT = {227737705: 1, 227737706: 2}

def imp(x):
    i = x.get('$import') if isinstance(x, dict) else None
    return g2p.get(i['fileGuid'], '?').rsplit('/', 1)[-1] if i else None

def pos(o):
    p = o['Field_d6351ede']['Field_bc4b07b4']
    return [round(p['Field_3901db14'], 1), round(p['Field_42fc0f5e'], 1), round(p['Field_32a99b9c'], 1)]

def pip(pt, poly):
    x, z = pt; inside = False; n = len(poly)
    for i in range(n):
        x1, z1 = poly[i]; x2, z2 = poly[(i + 1) % n]
        if (z1 > z) != (z2 > z):
            if x1 + (z - z1) * (x2 - x1) / (z2 - z1) > x: inside = not inside
    return inside

def variant(gem, key):
    t = table.get('<' + gem + '>')
    if not t: return None
    return (t['variants'].get(str(key)) or t['default']).strip('<>')

maps = sorted({k.split('/')[3].upper() for k in d if '/levels/' in k.lower() and 'breakthrough' in k.lower()})
out = {}
lines = []
for m in maps:
    keys = [k for k in d if k.lower().startswith(f'game/glaciermp/levels/{m.lower()}/') and '/breakthrough/' in k.lower()]
    allkeys = [k for k in d if k.lower().startswith(f'game/glaciermp/levels/{m.lower()}/')]
    rec = {'assets': [re.split('/[Bb]reakthrough/', k)[-1] for k in keys], 'factionOverrides': {}, 'instances': [], 'boxes': [], 'polygons': []}
    # faction overrides: any object with Field_21943083 entries whose id is a team slot
    rec['namedOverrides'] = {}
    for k in allkeys:
        for o in d[k]['objects']:
            if o.get('$class') == 'Class_f5c6eb31':
                for v in o.get('Field_10cf85cd') or []:
                    n = NAMES.get(v['Field_93bf7d99'])
                    if n: rec['namedOverrides'][k.split('/')[-1] + ':' + n] = v['Field_8cf424e7'].get('value') if isinstance(v['Field_8cf424e7'], dict) else v['Field_8cf424e7']
            for ent in o.get('Field_21943083', []) if isinstance(o.get('Field_21943083'), list) else []:
                cid = ent.get('Field_c1ad37da')
                val = (ent.get('Field_47f25917') or {}).get('value')
                if cid in TEAM_SLOT and isinstance(val, int):
                    rec['factionOverrides'][f'team{TEAM_SLOT[cid]}'] = FACTION.get(val, val)
        # also connection ids mapping (Field_c41fb636 -> Field_2d7314c9) in root
        root = d[k]['objects'][0]
        for c in root.get('Field_c78408a3', []) or []:
            if c.get('Field_2d7314c9') in TEAM_SLOT:
                src = c.get('Field_c41fb636')
                # find data entry with that id
                for o in d[k]['objects']:
                    for ent in (o.get('Field_21943083') or []):
                        if ent.get('Field_c1ad37da') == src:
                            val = (ent.get('Field_47f25917') or {}).get('value')
                            if isinstance(val, int):
                                rec['factionOverrides'][f'team{TEAM_SLOT[c["Field_2d7314c9"]]}'] = FACTION.get(val, val)
    # instances and shapes from every layer under Breakthrough
    for k in keys:
        layer = re.split('/[Bb]reakthrough/', k)[-1]
        for i, o in enumerate(d[k]['objects']):
            c = o['$class']
            if c == 'Class_2f332f01':
                gem = imp(o.get('Field_cbd4eb97'))
                if gem and gem.startswith('GEM_'):
                    key = o['Field_cd465eb9']['Field_8cf424e7']
                    rec['instances'].append({'layer': layer, 'idx': i, 'gem': gem, 'key': key, 'variant': variant(gem, key), 'pos': pos(o), 'id': o.get('Field_5645e663')})
            elif c == 'Class_78096792':
                pts = [(p['Field_3901db14'], p['Field_32a99b9c']) for p in o['Field_edfc6df6']]
                xs = [p[0] for p in pts]; zs = [p[1] for p in pts]
                entry = {'layer': layer, 'idx': i, 'n': len(pts), 'bbox': [round(min(xs)), round(min(zs)), round(max(xs)), round(max(zs))], 'pts': pts}
                (rec['boxes'] if len(pts) == 4 else rec['polygons']).append(entry)
    # containment
    for inst in rec['instances']:
        pt = (inst['pos'][0], inst['pos'][2])
        inst['inBoxes'] = [b['idx'] for b in rec['boxes'] if pip(pt, b['pts'])]
        inst['inPolys'] = [p['idx'] for p in rec['polygons'] if pip(pt, p['pts'])]
    for b in rec['boxes'] + rec['polygons']:
        b['contains'] = [f"{x['gem'][4:]}{'#'+str(x['key']) if x['key']!=-1 else ''}@{x['idx']}" for x in rec['instances'] if x['gem'] in ('GEM_Sector', 'GEM_HQ', 'GEM_VehicleSpawner', 'GEM_VehicleSpawner_Forward', 'GEM_CapturePoint', 'GEM_StationarySpawner', 'GEM_AutomaticAA') and pip((x['pos'][0], x['pos'][2]), b['pts'])]
        del b['pts']
    out[m] = rec
    lines.append(f'===== {m}')
    lines.append('assets: ' + ', '.join(rec['assets']))
    lines.append('factionOverrides: ' + json.dumps(rec['factionOverrides']))
    lines.append('namedOverrides: ' + json.dumps(rec['namedOverrides']))
    cnt = collections.Counter(x['gem'] for x in rec['instances'])
    lines.append('gem counts: ' + json.dumps(cnt))
    for x in rec['instances']:
        if x['gem'] in ('GEM_Sector', 'GEM_HQ', 'GEM_VehicleSpawner', 'GEM_VehicleSpawner_Forward', 'GEM_CapturePoint', 'GEM_StationarySpawner', 'GEM_AutomaticAA'):
            lines.append(f"  {x['layer']}@{x['idx']} {x['gem'][4:]} key={x['key']} variant={x['variant']} pos={x['pos']} boxes={x['inBoxes']} polys={x['inPolys']}")
    for b in rec['boxes']:
        lines.append(f"  BOX@{b['idx']} bbox={b['bbox']} contains={b['contains']}")
    for b in rec['polygons']:
        lines.append(f"  POLY{b['n']}@{b['idx']} bbox={b['bbox']} contains={b['contains']}")
json.dump(out, open(sp / 'bt-maps.json', 'w'), indent=1)
(sp / 'bt-maps.txt').write_text('\n'.join(lines), encoding='utf-8')
print('\n'.join(l for l in lines if l.startswith('=====') or l.startswith('gem counts') or l.startswith('factionOverrides') or l.startswith('assets') or l.startswith('namedOverrides')))
