"""Registry rows whose name contains all given substrings. python regshow.py M4A1_WB Index"""
import sys
from rawlib import *
reg = registry()
subs = [s.lower() for s in sys.argv[1:]]
n = 0
for k, v in sorted(reg.items()):
    if all(s in k.lower() for s in subs):
        print(k, "=", v); n += 1
        if n > 80: break
