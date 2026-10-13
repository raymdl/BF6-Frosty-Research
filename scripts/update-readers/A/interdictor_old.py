"""Interdictor Precision table in the previous build's raw settings file (route from <run>/raw-index-old.tsv)."""
import pathlib, json, sys
import lib
old = None
for l in open(lib.RUN / "raw-index-old.tsv", encoding="utf-8"):
    r, p = l.rstrip("\n").split("\t")
    if r.lower() == "common/gamesetup/gameconfigurations/glaciergameconfiguration/settings":
        old = pathlib.Path(p)
print("old settings file:", old)
build = [x for x in old.parts if x[:1].isdigit() and x.count(".") == 3]
print("build folder:", build)
td = None
for cand in old.parents:
    c = cand / "toolchain" / "SharedTypeDescriptors.ebx"
    if c.exists():
        td = c; break
    c = cand / "capture" / "toolchain" / "SharedTypeDescriptors.ebx"
    if c.exists():
        td = c; break
print("descriptors:", td)
types = lib.dec.type_descriptors(td)
a = lib.dec.Ebx(old, types).decode()
F = lambda h: "Field_" + h
for o in a["objects"]:
    if o["$class"] == "Class_0fd27406" and abs(o[F("e5bb1946")] - 732.7392) < 0.01:
        rows = o[F("4da34085")][F("f028b424")][F("59491962")]
        print("old Interdictor rows:", [(lib.f32(r[F("14c4a054")]), lib.f32(r[F("aee62a28")])) for r in rows])
