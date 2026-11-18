"""Sight files (optic lens blocks, reticle textures, sight meshes, aiming eye point): a per-build
record and a comparison between two builds.

  python -I scripts/frosty-sight-diff.py export <name> --build <build> --meshes <list file> [--keep-raw]
  python -I scripts/frosty-sight-diff.py compare <old folder> <new folder> --out <sight-changes.tsv>
      [--old-index <tsv> --new-index <tsv> --old-descriptors <ebx> --new-descriptors <ebx>]

Why: lens blocks, reticle textures and meshes are resources, not EBX routes, so the capture and
the weapon change list never see them, and frosty-weapon-semdiff.py leaves MD_* files out.

export (two FrostyCmd runs, one at a time, under the capture lock after guard) writes
builds/<build>/reports/<name>/, a new folder:
  1. export-res "win32/dpf/dpf_" and the --meshes names (one per line; start from the previous
     build's mesh-list.txt and add the meshes of new sights).
     Shader states: kept are the 1P depots holding a lens block, which is a block with a texture
     named T_RET* or T_RE_* (names from the build's capture/collection/asset-catalog.json). Skin
     variants (_ws/_wa/_gs + four digits) are left out.
     Meshes: the MeshSet resource (type 49b156d4, about 3 KB) and its meta only. It holds the
     bounding box, the buffer sizes, the section records and the ids of the vertex chunks. The
     vertex chunks themselves are not read: a mesh edit that left all of those identical would
     not show (not seen, and not tested across two builds).
  2. export-textures: every reticle texture a lens block names, and Common/FX/Textures/FLIR/T_FLIR_*.
  sight-files.tsv    kind, name, bytes, sha256 of every dumped file (lens-depot, texture, mesh)
  sight-values.tsv   bundle#block, parameter hash, value of every lens-block parameter
  texture-list.txt, mesh-list.txt, export-status-<kind>.tsv
The raw dumps are deleted afterwards unless --keep-raw: the two tables are what is compared.

compare reads the two folders' tables and writes section, key, kind (added, removed, changed),
old, new. Sections: file (raw SHA-256), lens (decoded values) and, with the four index and
descriptor arguments of frosty-weapon-semdiff.py, eye: MD.Sight.Main (mm) per part record of every
MD_* file whose raw SHA-256 differs. A folder compared with itself gives no rows.

Lens-block layout: docs/frosty/TOOLS.md (export-res). Parameter names are hashes; the known ones
are in docs/frosty/ATTACHMENTS.md (sight drawings). Checked on 2.1.2.0 only.
"""
import argparse, collections, hashlib, importlib.util, json, msvcrt, re, shutil, struct, subprocess, sys, uuid
from pathlib import Path

RESEARCH = Path(__file__).resolve().parent.parent
DM = r"C:\Users\royal\Documents\BF6 Datamining"
GAME = r"C:\Program Files\EA Games\Battlefield 6"
RUNTIME = r"FrostyToolsuite-battlefield6\FrostyEditor\bin\Release\Final"
SIZES = {0x14a0b1c1: 4, 0x25f81af1: 12, 0x39ab6941: 8, 0xdef2e1a5: 16, 0xa1c34f4a: 4, 0x34791132: 4}
INTS, TEX = (0xa1c34f4a, 0x34791132), 0xcc84d53d
SKIN = re.compile(r"_(ws|wa|gs)[a-z]*\d{4}")
BUNDLE = re.compile(r"_[a-z0-9]+_bundle_1p(_win32_shaderstate)?$")
SIGHT_MAIN = "4c59b0bd-e1c1-ac8d-4c59-b0bde1c1ac8d"


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def parse_depot(b):
    """Blocks of (name hash, type hash, values) records; None when a record cannot be read."""
    pos = struct.unpack_from("<Q", b, 0)[0]
    while True:
        h, off = struct.unpack_from("<QQ", b, pos)
        if not (0 < off <= len(b)) or h < 1 << 32:
            break
        pos += 16
    blocks = []
    while pos + 4 <= len(b):
        n = struct.unpack_from("<I", b, pos)[0]
        if not 0 < n < 4096:
            break
        p, recs = pos + 4, []
        for _ in range(n):
            if p + 16 > len(b):
                return None
            name, typ, flags, _rid = struct.unpack_from("<QIHH", b, p); p += 16
            if flags & 0x8000:
                cnt = struct.unpack_from("<I", b, p)[0]; p += 4
                sz = SIZES.get(typ)
                if sz is None or cnt > 64:
                    return None
                vals = []
                for k in range(cnt):
                    raw = b[p:p + sz]; p += sz if k == cnt - 1 else 16
                    vals.append(str(struct.unpack("<i", raw)[0]) if typ in INTS
                                else ",".join("%g" % round(x, 5) for x in struct.unpack("<%df" % (sz // 4), raw)))
                recs.append((name, typ, vals))
            else:
                cnt = b[p]; p += 1
                if typ != TEX or cnt > 8:
                    return None
                recs.append((name, typ, [str(uuid.UUID(bytes_le=b[p + 32 * k + 16:p + 32 * k + 32])) for k in range(cnt)]))
                p += 32 * cnt
        blocks.append(recs); pos = p
    return blocks


def write_tsv(path, header, rows):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(header) + "\n")
        for r in sorted(rows):
            f.write("\t".join(str(v) for v in r) + "\n")


def read_tsv(path, nkey):
    rows = {}
    for line in open(path, encoding="utf-8").read().splitlines()[1:]:
        p = line.split("\t")
        rows[" ".join(p[:nkey])] = " ".join(p[nkey:])
    return rows


def export(a):
    dm, build_dir = Path(a.datamining), Path(a.datamining) / "builds" / a.build
    out = build_dir / "reports" / a.name
    if out.exists():
        sys.exit(f"STOP: {out} exists. Use a new name.")
    meshes = sorted({l.strip().lower() for l in open(a.meshes, encoding="utf-8-sig") if l.strip()})
    lock = open(dm / ".frosty-capture.lock", "a+")
    try:
        msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
    except OSError:
        sys.exit("STOP: the capture lock is held. Only one Frosty process at a time.")
    busy = subprocess.run(["powershell", "-NoProfile", "-Command", "@(Get-Process FrostyCmd -ErrorAction SilentlyContinue).Count"],
                          capture_output=True, text=True).stdout.strip()
    if busy != "0":
        sys.exit(f"STOP: {busy} FrostyCmd process(es) already running.")

    def build_tool(*args):
        return subprocess.run([sys.executable, "scripts/frosty-build.py", "--datamining", str(dm), *args],
                              cwd=RESEARCH, capture_output=True, text=True)
    g = build_tool("guard", a.build, "--game", a.game)
    print(g.stdout.strip() or g.stderr.strip())
    if g.returncode:
        sys.exit("STOP: guard failed.")
    print("reading the catalog")
    cat = json.load(open(build_dir / "capture" / "collection" / "asset-catalog.json", encoding="utf-8-sig"))["assets"]
    by_guid = {x["guid"].lower(): x["path"] for x in cat}
    out.mkdir(parents=True)
    raw, exe = out / "raw", dm / RUNTIME / "FrostyCmd.exe"

    def frosty(cmd, kind, lines):
        inp = out / f"{kind}-input.txt"
        inp.write_text("\n".join(lines) + "\n", encoding="ascii")
        r = subprocess.run([str(exe), cmd, "bf6", a.game, str(inp), str(raw / kind)], capture_output=True, text=True,
                           timeout=7200, cwd=exe.parent)
        if r.returncode:
            sys.exit(f"STOP: {cmd} failed: {r.stdout[-1500:]} {r.stderr[-1500:]}")
        status = (raw / kind / "export-status.tsv").read_text(encoding="utf-8-sig").splitlines()
        (out / f"export-status-{kind}.tsv").write_text("\n".join(status) + "\n", encoding="utf-8")
        ext = {"textures": ".bin"}.get(kind)
        have = {str(f.relative_to(raw / kind))[:-len(ext)].replace("\\", "/").lower() for f in (raw / kind).rglob("*" + ext)} if ext else set()
        missing[kind] = [l for l in lines if l.lower() not in have] if ext else []
        print(f"{cmd}: {len(status) - 1} status rows, {len(missing[kind])} not dumped")
        for l in missing[kind][:20]:
            print("   not dumped:", l)
        inp.unlink()

    def file_rows(kind, folder, files):
        return [(kind, str(f.relative_to(raw / folder)).replace("\\", "/").lower(), f.stat().st_size, sha(f)) for f in files]

    files, values, textures, unread, missing = [], [], set(), [], {}
    frosty("export-res", "res", ["win32/dpf/dpf_"] + meshes)
    missing["meshes"] = []
    for m in meshes:
        f = raw / "res" / (m + ".49b156d4.res")
        if not f.exists():
            missing["meshes"].append(m); continue
        files.append(("mesh", m + ".res", f.stat().st_size, sha(f)))
        files.append(("mesh", m + ".resmeta", f.with_suffix(".resmeta").stat().st_size, sha(f.with_suffix(".resmeta"))))
    print(f"meshes {len(meshes) - len(missing['meshes'])}, not dumped {len(missing['meshes'])}: {missing['meshes'][:20]}")
    for f in sorted((raw / "res").glob("win32/dpf/*_bundle_1p_win32_shaderstate/*.73312045.res")):
        name = BUNDLE.sub("", f.parent.name)[4:]
        if SKIN.search(name):
            continue
        blocks = parse_depot(f.read_bytes())
        if blocks is None:
            unread.append(f.parent.name); continue
        lens = False
        for i, recs in enumerate(blocks):
            tex = {"%016x" % n: by_guid.get(v[0], v[0]) for n, t, v in recs if t == TEX and v}
            ret = [p for p in tex.values() if p.rsplit("/", 1)[-1].startswith(("T_RET", "T_RE_"))]
            if not ret:
                continue
            lens = True; textures.update(ret)
            values += [(f"{name}#{i}", "tex:" + h, p) for h, p in tex.items()]
            values += [(f"{name}#{i}", "%016x" % n, " | ".join(v)) for n, t, v in recs if t != TEX]
        if lens:
            files.append(("lens-depot", name, f.stat().st_size, sha(f)))
    print(f"lens depots {sum(r[0] == 'lens-depot' for r in files)}, lens-block values {len(values)}, depots not read {len(unread)}: {unread[:10]}")
    textures |= {x["path"] for x in cat if x["path"].startswith("Common/FX/Textures/FLIR/T_FLIR_")}
    textures = sorted(t for t in textures if "/" in t)
    (out / "texture-list.txt").write_text("\n".join(textures) + "\n", encoding="ascii")
    (out / "mesh-list.txt").write_text("\n".join(meshes) + "\n", encoding="ascii")
    frosty("export-textures", "textures", textures)
    files += file_rows("texture", "textures", [f for f in (raw / "textures").rglob("*") if f.suffix in (".bin", ".json")])
    write_tsv(out / "sight-files.tsv", ("kind", "name", "bytes", "sha256"), files)
    write_tsv(out / "sight-values.tsv", ("block", "parameter", "value"), values)
    if not a.keep_raw:
        shutil.rmtree(raw)
    rec = build_tool("record", a.build)
    print(rec.stdout.strip()[-400:] or rec.stderr.strip()[-400:])
    print(json.dumps({"folder": str(out), "files": collections.Counter(r[0] for r in files), "values": len(values),
                      "textures": len(textures), "meshes": len(meshes), "not_dumped": missing, "depots_not_read": unread}))


def eye_points(path, types, dec):
    """MD.Sight.Main (mm) per part record: {bundle without its hash: [x, y, z]}."""
    objs = dec.Ebx(Path(path if path.endswith(".ebx") else path + ".ebx"), types).decode()["objects"]

    def imports(o):
        if isinstance(o, dict):
            if "$import" in o:
                yield o["$import"]["fileGuid"]
            for v in o.values():
                yield from imports(v)
        elif isinstance(o, list):
            for v in o:
                yield from imports(v)
    out, seen = {}, collections.Counter()
    for x in objs:
        if x.get("$class") != "Class_0653128c":
            continue
        for r in x.get("Field_eb9379b0") or []:
            t = objs[r["$ref"]] if isinstance(r, dict) and "$ref" in r else {}
            if SIGHT_MAIN not in set(imports(t.get("Field_b7b33071", {}))):
                continue
            v = t["Field_8cf424e7"]; v = v.get("Field_bc4b07b4", v)
            key = BUNDLE.sub("", str(x.get("Field_5af77230") or "-"))
            if SKIN.search(key):
                continue
            seen[key] += 1
            out[key if seen[key] == 1 else f"{key}#{seen[key]}"] = ",".join(
                "%g" % round(v[k] * 1000, 1) for k in ("Field_3901db14", "Field_42fc0f5e", "Field_32a99b9c"))
    return out


def diff(section, old, new, rows):
    for k in sorted(old.keys() | new.keys()):
        if old.get(k) != new.get(k):
            rows.append((section, k, "added" if k not in old else "removed" if k not in new else "changed",
                         old.get(k, ""), new.get(k, "")))


def compare(a):
    rows, failed = [], []
    diff("file", read_tsv(Path(a.old) / "sight-files.tsv", 2), read_tsv(Path(a.new) / "sight-files.tsv", 2), rows)
    diff("lens", read_tsv(Path(a.old) / "sight-values.tsv", 2), read_tsv(Path(a.new) / "sight-values.tsv", 2), rows)
    md = 0
    if a.old_index:
        spec = importlib.util.spec_from_file_location("frosty_ebx_decode", Path(__file__).resolve().parent / "frosty-ebx-decode.py")
        dec = importlib.util.module_from_spec(spec); spec.loader.exec_module(dec)
        to, tn = dec.type_descriptors(Path(a.old_descriptors)), dec.type_descriptors(Path(a.new_descriptors))
        idx = []
        for path in (a.old_index, a.new_index):
            d = {}
            for line in open(path, encoding="utf-8"):
                p = line.rstrip("\n").split("\t")
                if len(p) >= 3 and p[0].lower().startswith("common/hardware/weapons/") and p[0].rsplit("/", 1)[-1].startswith("MD_"):
                    d[p[0]] = (p[1], p[2])
            idx.append(d)
        old, new = idx
        for r in sorted(old.keys() | new.keys()):
            if r in old and r in new and old[r][1] == new[r][1]:
                continue
            md += 1
            try:
                x = eye_points(old[r][0], to, dec) if r in old else {}
                y = eye_points(new[r][0], tn, dec) if r in new else {}
            except Exception as e:
                failed.append(f"{r}: {type(e).__name__}: {e}"); continue
            diff("eye", {f"{r} {k}": v for k, v in x.items()}, {f"{r} {k}": v for k, v in y.items()}, rows)
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        f.write("section\tkey\tkind\told\tnew\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    print(json.dumps({"rows": len(rows), "by": collections.Counter(f"{r[0]} {r[2]}" for r in rows),
                      "md_files_differing": md, "decode_failed": failed}))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("export")
    e.add_argument("name", help="<topic>-<yyyy-mm-dd>, the new folder under builds/<build>/reports/")
    e.add_argument("--build", required=True)
    e.add_argument("--meshes", required=True)
    e.add_argument("--keep-raw", action="store_true")
    e.add_argument("--datamining", default=DM)
    e.add_argument("--game", default=GAME)
    c = sub.add_parser("compare")
    c.add_argument("old"); c.add_argument("new")
    c.add_argument("--out", required=True)
    for n in ("--old-index", "--new-index", "--old-descriptors", "--new-descriptors"):
        c.add_argument(n)
    a = ap.parse_args()
    if a.cmd == "compare" and len({bool(a.old_index), bool(a.new_index), bool(a.old_descriptors), bool(a.new_descriptors)}) > 1:
        sys.exit("Give all four of --old-index, --new-index, --old-descriptors, --new-descriptors, or none.")
    export(a) if a.cmd == "export" else compare(a)


if __name__ == "__main__":
    main()
