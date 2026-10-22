"""Dump every MUT_* tweakable asset (name = value [min..max]) and list the other mode assets per decoded gm-*.json.
usage: python -I modes_mut.py decoded/modes --out modes-out"""
import json, sys, pathlib, re, collections
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[sys.argv.index('--out') + 1]); out.mkdir(parents=True, exist_ok=True)
NAME, VAL, MAX, MIN = 'Field_0c59fa06', 'Field_42c8b257', 'Field_3ff76ddb', 'Field_c06d0cbb'
def val(v):
    return v.get('value') if isinstance(v, dict) and 'value' in v else v
for f in sorted(src.glob('gm-*.json')):
    mode = f.stem[3:]
    d = json.load(open(f))['assets']
    lines = []; inventory = collections.Counter()
    for path, a in sorted(d.items()):
        base = path.rsplit('/', 1)[-1]
        inventory[re.sub(r'_.*', '', base) if '_' in base else base] += 1
        objs = a.get('objects') or []
        rows = [o for o in objs if isinstance(o, dict) and NAME in o and VAL in o]
        if base.startswith('MUT_') or rows:
            lines.append(f'===== {path}  ({len(objs)} objects, {len(rows)} tweakables)')
            for o in rows:
                rng = ''
                if MIN in o or MAX in o: rng = f'  [{val(o.get(MIN, ""))}..{val(o.get(MAX, ""))}]'
                lines.append(f"  {o[NAME]:50s} = {json.dumps(val(o[VAL]))}{rng}")
    (out / f'{mode}-tweakables.txt').write_text('\n'.join(lines), encoding='utf-8')
    inv = '\n'.join(f'{k:30s}{v}' for k, v in sorted(inventory.items()))
    (out / f'{mode}-assets.txt').write_text('\n'.join(sorted(d.keys())) + '\n\n' + inv, encoding='utf-8')
    print(f'{mode}: {len(d)} assets, {sum(1 for l in lines if l.startswith("====="))} with tweakables')
