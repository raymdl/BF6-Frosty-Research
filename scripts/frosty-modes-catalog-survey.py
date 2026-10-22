import json, re, collections, os
cat=json.load(open(r'C:\Users\royal\Documents\BF6 Datamining\builds\2.1.1.0\capture\collection\asset-catalog.json',encoding='utf-8'))
items = cat if isinstance(cat,list) else (cat.get('assets') or cat.get('items') or cat)
paths=[]
if isinstance(items,dict):
    for k,v in items.items():
        paths.append(v.get('name') or v.get('path') or k if isinstance(v,dict) else k)
else:
    for v in items:
        paths.append(v.get('name') or v.get('path') if isinstance(v,dict) else v)
paths=[p for p in paths if isinstance(p,str)]
print('total',len(paths))
raw=r'C:\Users\royal\Documents\BF6 Datamining\builds\2.1.1.0\capture\collection\raw'
have=set()
for root,ds,fs in os.walk(raw):
    for f in fs:
        if f.endswith('.ebx'):
            have.add(os.path.relpath(os.path.join(root,f[:-4]),raw).replace(os.sep,'/').lower())
gm=collections.Counter(); layers=collections.Counter(); lvl=collections.defaultdict(set)
for p in paths:
    m=re.match(r'Game/GlacierMP/Gamemodes/([^/]+)/',p)
    if m: gm[m.group(1)]+=1
    m=re.match(r'Game/GlacierMP/Levels/(MP_[^/]+)/_layers_gameplay/([^/]+)/',p,re.I)
    if m: layers[m.group(2)]+=1; lvl[m.group(2)].add(m.group(1))
print('--- Gamemodes folders'); 
for k,v in sorted(gm.items()): print(f'{k:40s}{v}')
print('--- layer folders (count, maps)')
for k,v in sorted(layers.items(), key=lambda x:-x[1]): print(f'{k:40s}{v:5d} maps={len(lvl[k])}')
# other gamemode-ish roots
roots=collections.Counter()
for p in paths:
    if re.search(r'/Gamemodes?/',p) and not p.startswith('Game/GlacierMP/Gamemodes/'):
        roots[p.split('/Gamemode')[0]]+=1
print('--- other gamemode roots'); 
for k,v in roots.most_common(15): print(f'{k:60s}{v}')
json.dump(paths,open('catalog-paths.json','w'))
json.dump(sorted(have),open('have-raw.json','w'))
