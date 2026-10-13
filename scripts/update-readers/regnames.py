"""Field hash -> name pairs stored in the build's tweakable registries. Writes <work>\regnames.tsv.

A registry node keeps a hash array (Field_4471d2f1) beside its children array (Field_080f1aaa);
position i of one pairs with position i of the other (the association FIELD_MAP.md uses).
Columns: hash, leaf name, count, other names, sample owners. Run once per build before part A."""
import collections, importlib.util, pathlib
import settings

spec = importlib.util.spec_from_file_location("dec", settings.REPO / "scripts/frosty-ebx-decode.py")
dec = importlib.util.module_from_spec(spec); spec.loader.exec_module(dec)
types = dec.type_descriptors(settings.DESCRIPTORS)
pairs = collections.defaultdict(collections.Counter)
parents = collections.defaultdict(set)
unequal = files = 0
for route, (path, _) in sorted(settings.held_routes().items()):
    if "/tweakables/" not in route:
        continue
    try:
        objs = dec.Ebx(pathlib.Path(path), types).decode()["objects"]
    except Exception:
        continue
    files += 1
    for o in objs:
        hs, ch = o.get("Field_4471d2f1"), o.get("Field_080f1aaa")
        if not isinstance(hs, list) or not isinstance(ch, list) or not hs:
            continue
        if len(hs) != len(ch):
            unequal += 1
            continue
        pname = o.get("Field_0c59fa06") or ""
        for h, c in zip(hs, ch):
            if not (isinstance(c, dict) and "$ref" in c):
                continue
            cn = objs[c["$ref"]].get("Field_0c59fa06")
            if not isinstance(cn, str) or not isinstance(h, int):
                continue
            leaf = cn[len(pname) + 1:] if pname and cn.startswith(pname + ".") else cn.rsplit(".", 1)[-1]
            hx = f"{h & 0xffffffff:08x}"
            pairs[hx][leaf] += 1
            if len(parents[hx]) < 4:
                parents[hx].add(pname.split(".")[0])
out = settings.WORK / "regnames.tsv"
out.parent.mkdir(parents=True, exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    f.write("hash\tname\tcount\tother names\tsample owners\n")
    for h, c in sorted(pairs.items()):
        (n, k), rest = c.most_common(1)[0], c.most_common()[1:4]
        f.write(f"{h}\t{n}\t{k}\t{'; '.join(f'{a}({b})' for a, b in rest)}\t{', '.join(sorted(parents[h]))}\n")
print("registry files", files, "hashes", len(pairs), "unequal arrays", unequal, "ambiguous", sum(len(c) > 1 for c in pairs.values()), "->", out)