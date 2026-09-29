"""Link the site repo's data/, sim/ and ui/ into this research checkout.

Research scripts read site files at their repo-relative paths (ROOT/'data/weapons.json'); their bytes are
pinned by receipts, so the layout stays the same and the site folders are reached through directory
junctions (no admin rights needed). The links are gitignored.

usage: python scripts/setup-site-links.py [--site-root PATH]   (default: the sibling "BF6 Weapon Analyzer")
"""
import argparse, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--site-root', default=str(ROOT.parent / 'BF6 Weapon Analyzer'))
    site = Path(ap.parse_args().site_root).resolve()
    if not (site / 'index.html').exists(): sys.exit(f'not a site checkout: {site}')
    for name in ('data', 'sim', 'ui'):
        link, target = ROOT / name, site / name
        if link.exists():
            print(f'{name}: exists ({"junction" if link.is_junction() else "folder"} -> {link.resolve()})'); continue
        subprocess.run(['cmd', '/c', 'mklink', '/J', str(link), str(target)], check=True, capture_output=True)
        print(f'{name}: linked -> {target}')

if __name__ == '__main__':
    main()
