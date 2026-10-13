"""Which arithmetic reproduces the site's bolt/pump rpm? Prints site value and candidates."""
import json
import lib, extract
from lib import f32
site = {w["id"]: w for w in json.load(open(lib.SITE / "data/weapons.json", encoding="utf-8"))}
for sid, internal in (("m2010esr", "M2010ESR"), ("sv98", "SV98M"), ("psr", "MRAD"), ("miniscout", "MiniFix"), ("l115", "L115A3"),
                      ("interdictor", "DesertTechHTI"), ("m87a1", "590A1"), ("db12", "DP12"), ("elr40", "CDX40")):
    r = extract.raw(internal); b = r["bolt"]; d = extract.d32
    T, S, D, R = b["time"], b["speed"], b["delay"], r["rateOfFireSingle"]
    wide = 60.0 / (d(T) / d(S) + d(D) + 60.0 / d(R))
    dec = 60.0 / (f32(T) / f32(S) + f32(D) + 60.0 / f32(R))
    print(sid, "site", site.get(sid, {}).get("rpm"), "| float32-widened", wide, "| decimal", dec, "| T S D R", f32(T), f32(S), f32(D), f32(R),
          "frac", f32(b["frac"]), f32(b["fracZoom"]), "primaryMode", r["primaryMode"], r["altModes"], "burstRounds", r["burstRoundsField"], "bpm", f32(r["burstsPerMinute"]))
