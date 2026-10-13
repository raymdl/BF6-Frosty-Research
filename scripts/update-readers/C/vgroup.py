import json, collections
m = json.load(open('validate.json'))['mismatches']
c = collections.Counter(); ex = {}
for x in m:
    if x[1] == 'field': k = ('field', x[2], x[4], x[5], x[6], x[3] if x[2] != 'mag' else '')
    elif x[1] == 'record not on site': k = (x[1], x[2])
    elif x[1] == 'tooltip': k = (x[1], x[2], x[3], x[6], x[5][:14], x[4][:14])
    elif x[1] == 'list': k = (x[1], x[2], x[3], x[4])
    else: k = tuple(str(y) for y in x[1:])
    c[k] += 1; ex.setdefault(k, []).append(x[0])
for k, v in sorted(c.items(), key=str): print(v, k, ",".join(ex[k][:6]))
