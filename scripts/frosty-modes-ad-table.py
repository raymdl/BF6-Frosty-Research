"""Build GEM -> GMPF variant tables from every AD_Objective_* asset in the decoded mode files."""
import json, glob, collections
cat=json.load(open(r'C:\Users\royal\Documents\BF6 Datamining\builds\2.1.1.0\capture\collection\asset-catalog.json'))
g2p={x['guid']:x['path'] for x in cat['assets']}
def imp(x):
    i=x.get('$import') if isinstance(x,dict) else None
    return g2p.get(i['fileGuid'],'?').rsplit('/',1)[-1] if i else None
per_mode={}; merged={}; conflicts=[]
for f in glob.glob('decoded/modes/gm-*.json')+['decoded/bt.json']:
    d=json.load(open(f))['assets']
    for path,a in d.items():
        base=path.rsplit('/',1)[-1]
        if not base.startswith('AD_'): continue
        objs=a['objects']; root=objs[0] if objs else {}
        entries=root.get('Field_5cdd107e')
        if not isinstance(entries,list): continue
        byguid={o.get('$guid'):o for o in objs}
        def deref(r):
            if isinstance(r,dict) and '$ref' in r:
                o=objs[r['$ref']] if isinstance(r['$ref'],int) and r['$ref']<len(objs) else None
                return imp(o.get('Field_6b831b88')) if o else None
            return None
        table={}
        for e in entries:
            gem=imp(e.get('Field_cbd4eb97'))
            if not gem: continue
            default=deref(e.get('Field_32623c4b'))
            variants={}
            for v in e.get('Field_fd8bca99') or []:
                key=(v.get('Field_cd465eb9') or {}).get('Field_8cf424e7')
                variants[str(key)]=deref(v.get('Field_32623c4b'))
            table['<'+gem+'>']={'default':'<'+str(default)+'>','variants':{k:'<'+str(v)+'>' for k,v in variants.items()}}
        per_mode[base]=table
        for g,t in table.items():
            if g in merged and merged[g]!=t: conflicts.append((g,base))
            merged.setdefault(g,t)
json.dump(per_mode,open('ad-tables-by-mode.json','w'),indent=1)
json.dump(merged,open('gem-variant-table-all.json','w'),indent=1)
print({k:len(v) for k,v in per_mode.items()}); print('merged',len(merged),'conflicts',conflicts[:20])
