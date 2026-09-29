# BF6 Frosty Research

Frosty source research for the [BF6 Weapon Analyzer](https://github.com/raymdl/BF6-Weapon-Analyzer):
the research queue, topic pages, dated receipts with their `record` headers, the generated indexes and
the research scripts. Split out of the site repo on 29 September 2026 with its history.

## Setup

1. Clone this repo next to the site repo (`Documents\BF6 Weapon Analyzer`).
2. `python scripts/setup-site-links.py` links the site's `data/`, `sim/` and `ui/` into this checkout
   (gitignored junctions), so scripts keep reading site files at their usual paths.
3. `python scripts/frosty-records.py status`, then `check`.

Start with [docs/frosty/README.md](docs/frosty/README.md); tools are in [docs/frosty/TOOLS.md](docs/frosty/TOOLS.md).

## The site interface

`python scripts/frosty-records.py build` writes `reference-data/frosty/lead-index.json` and
`site-evidence.json` into the site repo as well. The site repo keeps byte-equal copies of the
receipts its data or tests pin (`binding: site`) and of the generator scripts it runs (listed in the
site's MAINTENANCE.md); `check` fails on a changed site-bound receipt and warns when a shared script
differs between the repos.
