#!/usr/bin/env python3
r"""Capture the multiplayer copy of every captured asset whose capture holds the campaign copy.

  python scripts/frosty-mp-copies.py <name> [--build 2.1.2.0]

Why: the install holds two copies of many assets under one name, one in the campaign
superbundles (win32/sp/...) and one in the multiplayer ones. Frosty keeps the first it meets per
name, so a Frosty capture can hold the campaign copy, which the multiplayer game does not read
(found 10 November 2026: weapon name lists, attachment descriptors, UI metadata).

What it does, without starting Frosty and reading the install read-only:
  1. frosty-build.py guard (stops if the installed client is not the open build).
  2. Reads every superbundle toc and lists each EBX record's SHA-1 and CAS location.
  3. For each route the build's capture holds (capture/collection, then collection-fresh-cache)
     that has exactly one multiplayer version differing from a campaign version, reads the
     multiplayer record, checks its record SHA-1, decompresses it (the game's own Oodle DLL) and
     keeps it when its bytes differ from the captured file.
  4. Writes builds/<build>/reports/<name>/raw/<route>.ebx, raw-status.jsonl (capture shape plus
     recordSha1 and capturedSha256), summary.json, then frosty-build.py record.
  5. Writes asset-catalog.json: for each file GUID that the loaded-cache catalog gives to a
     campaign-only route while a multiplayer route shares it (an asset renamed since the campaign
     bundle was built, e.g. AD_SF300 and AD_SF300_RightRail), the multiplayer route. A GUID index
     that reads this catalog first resolves imports to the multiplayer asset.
     --catalog-only writes only this file, campaign-only.txt and summary.json.
  6. Writes campaign-only.txt: captured routes no multiplayer bundle holds. They are not evidence
     of what multiplayer offers (PD_12ga00Buck*, Attachment_Ultimax_BRL_Short).

Readers that take the build's reports/*/raw folders after the main capture (update readers) or a
later --raw (site generators, frosty-check-all --raw) then read the multiplayer copy.
The toc and bundle layout follows FrostySdk CasAssetLoader / BaseBinarySbReader.
"""
import argparse
import collections
import ctypes
import hashlib
import json
import msvcrt
import os
import re
import struct
import subprocess
import sys
from pathlib import Path

RESEARCH = Path(__file__).resolve().parents[1]
TOC_START = 0x22C


def be32(b, o):
    return struct.unpack_from(">I", b, o)[0]


def bundle_object(buf):
    size = be32(buf, 0)
    magic = be32(buf, 4) ^ 0x7065636E
    en = ">"
    if magic not in (0xED1CEDB8, 0xC3889333, 0xC3E5D5C3):
        en = "<"
    total, ebx_count, _, _, strings, _, _ = struct.unpack_from(en + "7I", buf, 8)
    strings -= 0x20
    body = buf[36:36 + size - 0x20]
    p, out = total * 20, []
    for i in range(ebx_count):
        name_offset, orig = struct.unpack_from(en + "2I", body, p)
        p += 8
        end = body.find(b"\0", strings + name_offset)
        out.append([body[strings + name_offset:end].decode(), body[i * 20:i * 20 + 20].hex(), orig])
    return out


def location(view, p, flag, prev):
    if flag == 0:
        cat, cas = prev[0], prev[1]
    elif flag == 1:
        cat, cas = ("idx", view[p + 2]), view[p + 3]
        p += 4
    elif flag == 128:
        cat, cas = ("hash", be32(view, p + 2)), struct.unpack_from(">H", view, p + 6)[0]
        p += 8
    else:
        raise ValueError(f"location flag {flag}")
    return (cat, cas, be32(view, p), be32(view, p + 4)), p + 8


def bundle_entries(view, read_cas):
    """[(name, record sha1, original size, location)] for one bundle's EBX records."""
    b_off, b_size, loc_off, total, data_off = struct.unpack_from(">iiIII", view, 0)
    flags = view[loc_off:loc_off + total]
    p, z, prev = data_off, 0, None
    if b_off == 0 and b_size == 0:
        prev, p = location(view, p, flags[0], None)
        z = 1
        entries = bundle_object(read_cas(prev))
    else:
        entries = bundle_object(view[b_off:b_off + b_size])
    for e in entries:
        prev, p = location(view, p, flags[z], prev)
        z += 1
        e.append(prev)
    return entries


class Install:
    def __init__(self, game):
        self.game = Path(game)
        self.roots = [self.game / "Data"] + sorted(p / "Data" for p in (self.game / "Update").iterdir() if (p / "Data").is_dir())
        names = set()
        for m in re.findall(rb"[\x20-\x7e]{4,}", (self.game / "Data" / "layout.toc").read_bytes()):
            s = m.decode()
            names.update(s[k:] for k in range(3))
        self.by_hash = {}
        for n in names:
            h = 5381
            for c in n:
                h = (ord(c) ^ (33 * h)) & 0xFFFFFFFF
            self.by_hash.setdefault(h, n)
        self.dirs, self.handles, self.oodle = {}, {}, None

    def cas_path(self, loc):
        cat, cas = loc[0], loc[1]
        if cat[0] != "hash":
            raise ValueError(f"unsupported CAS catalog reference {cat}")
        name = self.by_hash[cat[1]]
        if name not in self.dirs:
            self.dirs[name] = next((r / "Win32" / name for r in self.roots
                                    if (r / "Win32" / name).is_dir() and any((r / "Win32" / name).glob("cas_*"))), None)
        if self.dirs[name] is None:
            raise FileNotFoundError(name)
        return self.dirs[name] / f"cas_{cas:02d}.cas"

    def read(self, loc):
        path = self.cas_path(loc)
        f = self.handles.get(path)
        if f is None:
            f = self.handles[path] = open(path, "rb")
        f.seek(loc[2])
        return f.read(loc[3])

    def decompress(self, data, orig):
        if self.oodle is None:
            self.oodle = ctypes.WinDLL(str(self.game / "oo2core_9_win64.dll")).OodleLZ_Decompress
            self.oodle.restype = ctypes.c_int64
            self.oodle.argtypes = [ctypes.c_char_p, ctypes.c_int64, ctypes.c_char_p, ctypes.c_int64, ctypes.c_int,
                                   ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int64, ctypes.c_void_p,
                                   ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int64, ctypes.c_int]
        out, p = bytearray(), 0
        while len(out) < orig:
            size, kind, packed = struct.unpack_from(">IHH", data, p)
            p += 8
            if kind in (0x0070, 0x0071):
                out += data[p:p + packed]
            elif kind in (0x1170, 0x1570, 0x1970, 0x1171):
                buf = ctypes.create_string_buffer(size + 64)
                n = self.oodle(data[p:p + packed], packed, buf, size, 0, 0, 0, None, 0, None, None, None, 0, 3)
                if n != size:
                    raise ValueError(f"Oodle returned {n}, expected {size}")
                out += buf.raw[:size]
            else:
                raise ValueError(f"block type {kind:04x}")
            p += packed
        if len(out) != orig:
            raise ValueError("decompressed size differs")
        return bytes(out)

    def tocs(self):
        for root in self.roots:
            for parent, _, names in os.walk(root):
                for name in sorted(names):
                    if name.lower().endswith(".toc") and name.lower() != "layout.toc":
                        path = Path(parent, name)
                        yield path.relative_to(root).with_suffix("").as_posix().lower(), path

    def scan(self, wanted):
        """name -> {record sha1: [in a multiplayer superbundle, original size, location]} for wanted names."""
        versions, counts = collections.defaultdict(dict), collections.Counter()
        for superbundle, path in self.tocs():
            campaign = "sp" in superbundle.split("/")
            d = path.read_bytes()
            _, bundle_data, bundle_count = struct.unpack_from(">IIi", d, TOC_START)
            sb = None
            for i in range(bundle_count):
                o = TOC_START + bundle_data + i * 16
                size, offset = be32(d, o + 4), struct.unpack_from(">q", d, o + 8)[0]
                if size == 0xFFFFFFFF or offset == -1:
                    continue
                kind, size = size >> 30, size & 0x3FFFFFFF
                if kind == 1:
                    view = d[offset + TOC_START:offset + TOC_START + size]
                elif kind == 0:
                    sb = sb or open(path.with_suffix(".sb"), "rb")
                    sb.seek(offset)
                    view = sb.read(size)
                else:
                    raise ValueError(f"{superbundle} bundle {i}: flag {kind}")
                for name, sha1, orig, loc in bundle_entries(view, self.read):
                    if name in wanted:
                        v = versions[name].setdefault(sha1, [False, orig, loc])
                        v[0] = v[0] or not campaign
                counts["bundles"] += 1
            if sb:
                sb.close()
            counts["tocs"] += 1
        return versions, counts


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("name", help="reports folder name, <topic>-<yyyy-mm-dd>")
    ap.add_argument("--build", default="2.1.2.0")
    ap.add_argument("--datamining", default=r"C:\Users\royal\Documents\BF6 Datamining")
    ap.add_argument("--game", default=r"C:\Program Files\EA Games\Battlefield 6")
    ap.add_argument("--catalog-only", action="store_true", help="write only asset-catalog.json (renamed assets), no raw files")
    a = ap.parse_args()
    bdir = Path(a.datamining) / "builds" / a.build
    out = bdir / "reports" / a.name
    if out.exists():
        sys.exit(f"STOP: {out} exists")

    lock = open(Path(a.datamining) / ".frosty-capture.lock", "a+")
    try:
        msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
    except OSError:
        sys.exit("STOP: a capture is running.")

    def build_tool(*args):
        return subprocess.run([sys.executable, "scripts/frosty-build.py", "--datamining", a.datamining, *args],
                              cwd=RESEARCH, capture_output=True, text=True)
    guard = build_tool("guard", a.build, "--game", a.game)
    print(guard.stdout.strip() or guard.stderr.strip())
    if guard.returncode:
        sys.exit("STOP: guard failed. The game may have updated: run the game update check first.")

    captured = {}                      # lower-case route -> (route, sha256); the later capture wins
    for folder in ("collection", "collection-fresh-cache"):
        status = bdir / "capture" / folder / "raw-status.jsonl"
        if status.exists():
            for line in open(status, encoding="utf-8-sig"):
                r = json.loads(line)
                if r["status"] == "success":
                    captured[r["path"].lower()] = (r["path"], r["sha256"])
    install = Install(a.game)
    versions, counts = install.scan(set(captured))
    print(f"{counts['tocs']} tocs, {counts['bundles']} bundles; {len(versions)} of {len(captured)} captured routes found")

    # Renamed assets: a campaign bundle can still hold an asset under its old name, with the file
    # GUID the multiplayer asset now has. Where the loaded-cache catalog names the campaign-only
    # route for a GUID, list the multiplayer route so a GUID index reads this catalog first.
    def multiplayer(route):
        return any(v[0] for v in versions.get(route.lower(), {}).values())
    listed = []
    for folder in ("collection", "collection-fresh-cache"):
        by_guid = collections.defaultdict(list)
        for asset in json.loads((bdir / "capture" / folder / "asset-catalog.json").read_text(encoding="utf-8"))["assets"]:
            by_guid[asset["guid"].lower()].append(asset["path"])
        listed.append(by_guid)
    renamed = []
    for guid, paths in sorted(listed[0].items()):
        if len(paths) == 1 and paths[0].lower() in versions and not multiplayer(paths[0]):
            others = [p for p in listed[1].get(guid, []) if p != paths[0] and multiplayer(p)]
            if len(others) == 1:
                renamed.append({"path": others[0], "guid": guid, "campaignOnlyPath": paths[0]})
    print(f"  {len(renamed):6} GUIDs the loaded-cache catalog gives to a campaign-only route")

    rows, tally = [], collections.Counter()
    for key in sorted(versions) if not a.catalog_only else []:
        found = versions[key]
        mp = [(sha1, v) for sha1, v in found.items() if v[0]]
        if len(found) < 2:
            tally["one version"] += 1
            continue
        if len(mp) != 1:
            tally["no multiplayer version" if not mp else "several multiplayer versions"] += 1
            if mp:
                print(f"  SKIPPED {captured[key][0]}: {len(mp)} multiplayer versions")
            continue
        sha1, (_, orig, loc) = mp[0]
        data = install.read(loc)
        if hashlib.sha1(data).hexdigest() != sha1:
            sys.exit(f"STOP: record SHA-1 mismatch for {key}")
        raw = install.decompress(data, orig)
        digest = hashlib.sha256(raw).hexdigest()
        route, had = captured[key]
        if digest == had:
            tally["capture already holds the multiplayer copy"] += 1
            continue
        tally["written"] += 1
        target = out / "raw" / (route + ".ebx")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        rows.append({"path": route, "status": "success", "file": f"raw/{route}.ebx", "bytes": len(raw),
                     "sha256": digest, "reason": None, "recordSha1": sha1, "capturedSha256": had})
    if not rows and not renamed:
        sys.exit("Nothing to write: the capture holds the multiplayer copy of every route.")
    out.mkdir(parents=True, exist_ok=True)
    (out / "asset-catalog.json").write_text(json.dumps({"assets": renamed}, indent=1) + "\n", encoding="utf-8")
    campaign_only = sorted(captured[k][0] for k in versions if not multiplayer(k))
    (out / "campaign-only.txt").write_text("\n".join(campaign_only) + "\n", encoding="utf-8")
    print(f"  {len(campaign_only):6} captured routes found only in campaign bundles (campaign-only.txt)")
    if not a.catalog_only:
        with open(out / "raw-status.jsonl", "w", encoding="utf-8", newline="\n") as fh:
            for r in rows:
                fh.write(json.dumps(r) + "\n")
    (out / "summary.json").write_text(json.dumps({
        "schemaVersion": 1, "method": "scripts/frosty-mp-copies.py: multiplayer EBX records read from the install's CAS files",
        "build": a.build, "tocs": counts["tocs"], "bundles": counts["bundles"],
        "capturedRoutes": len(captured), "routesFoundInTocs": len(versions), "result": dict(sorted(tally.items())),
        "renamedAssetGuids": len(renamed)},
        indent=1) + "\n", encoding="utf-8")
    for k, v in sorted(tally.items()):
        print(f"  {v:6} {k}")
    print(f"-> {out}")
    rec = build_tool("record", a.build)
    print(rec.stdout.strip().splitlines()[-1] if rec.stdout.strip() else rec.stderr.strip())
    if rec.returncode:
        sys.exit("STOP: record failed; the files are on disk but not in the manifest.")


if __name__ == "__main__":
    main()
