"""Read the controlled exact schemas across three existing atlases. No unit transfer."""
from pathlib import Path
import json, hashlib, runpy, argparse
def ref(p):return {'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def write(p,d):
 if p.exists():raise RuntimeError('Refuse existing '+str(p))
 p.write_text(json.dumps(d,indent=1)+'\n',encoding='utf-8')
a=argparse.ArgumentParser(description=__doc__);a.add_argument('--control',type=Path,required=True,help='Pinned lead control JSON, kept outside the installed script folder');a.add_argument('--self-check',action='store_true');a.add_argument('--out',type=Path);args=a.parse_args()
if not args.self_check and args.out is None:a.error('Specify --self-check or --out')
control=json.loads(args.control.read_text(encoding='utf-8-sig'));assert control['passed']
controlRefs=control['assets']+[control['descriptor'],control['decoder'],control['rawCheckHelper'],control['originalControl']]+control['siteSources']+control['siteExecutionSources']+control['priorEvidence']+list(control['atlasSources'].values())
for item in controlRefs:assert ref(Path(item['path']))['sha256']==item['sha256'],item['path']
r=runpy.run_path(control['decoder']['path']);td=r['type_descriptors'](control['descriptor']['path'])
raw=runpy.run_path(control['rawCheckHelper']['path'])
for c in control['rawChecks']:
 actual=raw['read'](c['path'],c['offset'],c['type']);assert actual['rawSha256']==c['rawSha256'] and actual['bytesHex']==c['bytesHex'] and actual['value']==c['value']
schemas=[]
for s in control['schemas']:
 candidates=[(i,k,cls) for i,cls in enumerate(td['classes']) for k,v in td['byGuid'].items() if v is cls and cls['hash']==s['classHash'] and (s['typeKey'] is None or k==s['typeKey']) and any(f['hash']==s['fieldHash'] and f['flags']==s['flags'] and f['classRef']==s['classRef'] for f in cls['fields'])]
 # Nested types: descriptor index is resolved from the known control parent classRef.
 if s['classHash']=='c45202f2':
  parent=td['byGuid']['dfa24ed7807b19103d97b179c514ee7c'];idx=next(f['classRef'] for f in parent['fields'] if f['hash']=='edfc6df6');candidates=[v for v in candidates if v[0]==idx]
 if s['classHash']=='70fd8f5f':
  # DTA root varies; exact nested descriptor targets are collected from current root bytes.
  ebx=r['Ebx'](control['assets'][1]['path'],td);root=ebx.class_by_key(ebx.class_keys[ebx.instances[0]['classRef']]);idx=next(f['classRef'] for f in root['fields'] if f['hash']=='70fd8f5f');candidates=[v for v in candidates if v[0]==idx]
 assert len(candidates)==1,(s,candidates)
 idx,key,cls=candidates[0];schemas.append({**s,'typeKey':key,'descriptorIndex':idx,'descriptor':cls})
if args.self_check:
 print(json.dumps({'passed':True,'rawChecks':len(control['rawChecks']),'exactControlledSchemas':len(schemas),'nativeEvaluator':False,'verifiedControlSourceHashes':len(controlRefs),'control':ref(args.control)}))
 if not args.out:raise SystemExit(0)
atlasPaths={k:Path(v['path']) for k,v in control['atlasSources'].items()}
output={'lead':'L1002','controlPassed':True,'schemas':schemas,'atlases':{},'limits':['Exact schema matches authorize structural reading only. Units and interpolation require exact owner and consumer evidence. No tuple or class-layout match upgrades native meaning.','No failed native semantic control is used for absence claims. Native evaluator is unavailable.']}
for area,p in atlasPaths.items():
 d=json.loads(p.read_text());assert d['descriptorSha256']==td['sha256'];assert d['head']==4909002
 normalized=[]
 if area=='weapons':
  for i,f in enumerate(d['families']):
   identity=f['identity'];normalized.append((f'/families/{i}',identity['classHash'],identity['descriptorKeys'],identity['fieldHash'],identity['declaredType'],len(f['contexts']),f['familyId']))
 elif area=='soldier':
  for i,f in enumerate(d['typedFamilies']):
   key=f['schemaIdentity'].split(':',1)[-1] if f['schemaIdentity'].startswith('local-key:') else None
   # Global nested identities are resolved against their full exact descriptor, not hash alone.
   keys=[k for k,v in td['byGuid'].items() if v==f['descriptor']]
   if key is not None:keys=[key]
   for field,entry in f['fields'].items():normalized.append((f'/typedFamilies/{i}/fields/{field}',f['descriptor']['hash'],keys,field[6:],entry['descriptorField'],1,None))
 else:
  for name,f in d['fieldFamilies'].items():normalized.append(('/fieldFamilies/'+name,f['class'][6:],f['descriptorKeys'],f['field'][6:],f['descriptorField'],len(f['ownerRoutes']),name))
 matches=[]
 for pointer,ch,keys,fh,typ,contexts,fid in normalized:
  for s in schemas:
   if ch==s['classHash'] and s['typeKey'] in keys and fh==s['fieldHash'] and typ['flags']==s['flags'] and typ['classRef']==s['classRef']:
    matches.append({'pointer':pointer,'familyId':fid,'schema':{k:s[k] for k in ['classHash','typeKey','descriptorIndex','fieldHash','flags','classRef']},'contextCount':contexts,'structuralReaderApplicable':True,'structuralRole':s['structuralRole'],'ownerScopedMeaningTransferred':False,'unitsTransferred':False,'interpolationTransferred':False,'limitToMeaningChange':False})
 output['atlases'][area]={'source':ref(p),'normalizedFieldEntries':len(normalized),'exactSchemaMatches':len(matches),'matchedContextMemberships':sum(m['contextCount'] for m in matches),'limitToNativeMeaningChanges':0,'limitToSiteMeaningChanges':0,'matches':matches}
write(args.out,output)
print(json.dumps({k:{a:b for a,b in v.items() if a!='matches'} for k,v in output['atlases'].items()},indent=1))