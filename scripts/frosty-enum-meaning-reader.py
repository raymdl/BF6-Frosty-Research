"""Exact current descriptor enum overlay. Hash members are not names."""
import argparse,hashlib,importlib.util,json,pathlib
PIN='4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1'
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def apply(decoder,descriptor,atlas):
 s=importlib.util.spec_from_file_location('ebx_enum_decoder',decoder);d=importlib.util.module_from_spec(s);s.loader.exec_module(d);t=d.type_descriptors(descriptor)
 if t['sha256']!=PIN:raise ValueError('unapproved descriptor revision')
 a=json.loads(pathlib.Path(atlas).read_text(encoding='utf-8-sig'))
 if a.get('descriptorSha256')!=PIN or a.get('head')!=4909002:raise ValueError('atlas build identity mismatch')
 candidates=[]
 if 'families' in a:
  for i,f in enumerate(a['families']):
   z=f['identity'];q=z.get('declaredType',{});candidates.append((str(i),z.get('descriptorKeys',[]),z.get('descriptorIndex'),z.get('classHash'),z.get('fieldHash'),q.get('flags'),q.get('classRef')))
 elif 'typedFamilies' in a:
  for i,f in enumerate(a['typedFamilies']):
   ident=f.get('schemaIdentity','');keys=[ident.split(':',1)[1]] if ident.startswith('local-key:') else []
   c=f.get('descriptor',{}); idx=int(ident.split(':')[1]) if ident.startswith('global-descriptor:') else next((j for j,x in enumerate(t['classes']) if x==c),None)
   if ident.startswith('global-descriptor:'):
    if idx>=len(t['classes']) or t['classes'][idx]!=c:raise ValueError('nested global descriptor mismatch')
    keys=[k for k,v in t['byGuid'].items() if v is t['classes'][idx]]
   for k,v in f['fields'].items():
    q=v['descriptorField'];candidates.append((str(i)+'/'+k,keys,idx,c.get('hash'),q['hash'],q['flags'],q['classRef']))
 elif 'fieldFamilies' in a:
  for k,f in a['fieldFamilies'].items():
   q=f['descriptorField'];keys=f.get('descriptorKeys',[]);c=t['byGuid'].get(keys[0]) if keys else None;idx=next((j for j,x in enumerate(t['classes']) if x is c),None)
   candidates.append((k,keys,idx,c.get('hash') if c else None,q['hash'],q['flags'],q['classRef']))
 else:raise ValueError('unsupported atlas schema')
 rows=[];errors=[]
 for loc,keys,idx,ch,fh,flags,ref in candidates:
  if flags is None or d.debug_type(flags)!=d.ENUM:continue
  if idx is None or idx>=len(t['classes']):errors.append({'atlasIdentity':loc,'reason':'missing exact descriptor index'});continue
  c=t['classes'][idx]; matches=[f for f in c['fields'] if f['hash']==fh and f['flags']==flags and f['classRef']==ref]
  if c['hash']!=ch or not matches or not keys or any(t['byGuid'].get(k) is not c for k in keys):errors.append({'atlasIdentity':loc,'reason':'declaring local key/descriptor/member mismatch'});continue
  if ref>=len(t['classes']) or d.debug_type(t['classes'][ref]['type'])!=d.ENUM:errors.append({'atlasIdentity':loc,'reason':'enum reference not exact enum descriptor'});continue
  en=t['classes'][ref]; members=[{'hash':f['hash'],'value':f['offset'] if f['offset']<2**31 else f['offset']-2**32,'name':None} for f in en['fields']]
  labels={0:'single',1:'single with bolt action',2:'automatic',3:'burst'} if ref==543 and en['hash']=='16e6fa59' else {}
  for m in members:
   if m['value'] in labels:m['name']=labels[m['value']];m['nameBasis']='corrected known-answer FireLogicType control; FIELD_MAP; current exact index 543'
  rows.append({'atlasIdentity':loc,'declaringDescriptorIndex':idx,'declaringDescriptorKeys':keys,'fieldHash':fh,'enumDescriptorIndex':ref,'enumDescriptorHash':en['hash'],'enumerants':members,'meaningAdded':False,'limit':'Enum membership only. Named fire meanings were already documented. Hash-only members retain no name; no runtime claim.'})
 return {'atlasPath':str(atlas),'atlasSha256':sha(atlas),'descriptorSha256':PIN,'enumFieldIdentities':len(rows),'rejectedIdentities':len(errors),'distinctEnumDescriptorIndices':len({r['enumDescriptorIndex'] for r in rows}),'distinctEntriesChangingFromLimitsToMeaning':0,'rows':rows,'errors':errors}
def self_check(decoder, descriptor, manifest):
 import struct
 s=importlib.util.spec_from_file_location('control_decoder',decoder);d=importlib.util.module_from_spec(s);s.loader.exec_module(d);t=d.type_descriptors(descriptor)
 if t['sha256']!=PIN:raise ValueError('control descriptor mismatch')
 m=json.loads(pathlib.Path(manifest).read_text(encoding='utf-8-sig'))
 if m['descriptorSha256']!=PIN:raise ValueError('manifest descriptor mismatch')
 class Probe(d.Ebx):
  def _read_field(self,parent,kind,ref):
   at=self.pos;v=super()._read_field(parent,kind,ref)
   if kind==d.ENUM:self.enum_reads.append((at,ref,v))
   return v
 checked=[]
 for c in m['checks']:
  e=Probe(c['path'],t);e.enum_reads=[]
  if e.sha256!=c['rawSha256']:raise ValueError('control raw hash mismatch')
  if any(e.class_by_key(k) is None for k in e.class_keys):raise ValueError('control unresolved local key')
  e.decode()
  if e.data[c['offset']:c['offset']+4].hex()!=c['bytesHex']:raise ValueError('control byte mismatch')
  if (c['offset'],m['enumDescriptorIndex'],c['value']) not in e.enum_reads:raise ValueError('control exact typed enum read missing')
  en=t['classes'][m['enumDescriptorIndex']]
  if en['hash']!=m['enumDescriptorHash'] or not any(f['offset']==c['value'] for f in en['fields']):raise ValueError('control enumerant mismatch')
  checked.append({'path':c['path'],'offset':c['offset'],'value':c['value']})
 if not {0,2,3}.issubset({c['value'] for c in checked}):raise ValueError('control must retain single0 automatic2 burst3')
 return {'passed':True,'controlledManifestPath':str(manifest),'controlledManifestSha256':sha(manifest),'checks':checked,'limit':'Known FireLogic labels only; no labels transfer to other enums.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--decoder',required=True);p.add_argument('--descriptors',required=True);p.add_argument('--atlas',action='append',default=[]);p.add_argument('--self-check',action='store_true');p.add_argument('--control-manifest');p.add_argument('--out',required=True);z=p.parse_args();o=pathlib.Path(z.out)
 if o.exists():raise ValueError('output exists')
 if z.self_check and not z.control_manifest:p.error('--self-check requires --control-manifest')
 if not z.self_check and not z.atlas:p.error('provide --atlas or --self-check')
 x={'readerSha256':sha(__file__),'decoderSha256':sha(z.decoder),'descriptorPath':z.descriptors}
 if z.self_check:x['selfCheck']=self_check(z.decoder,z.descriptors,z.control_manifest)
 x['atlases']=[apply(z.decoder,z.descriptors,a) for a in z.atlas];o.write_text(json.dumps(x,indent=2),encoding='utf-8');print(json.dumps({'selfCheck':x.get('selfCheck'),'atlases':[{k:v for k,v in a.items() if k not in ('rows','errors')} for a in x['atlases']]}))
if __name__=='__main__':main()
