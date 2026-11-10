# Update checklists

One patch-specific checklist per game update, named `<version>-checklist.md`. Each holds what
is particular to that update: identity and baseline paths, decisions, a run-order row for
every stage, one row per change found in the files (patch-note lines attached as labels), the
"announced, nothing stored" lines, the decisions taken during the run, the items held for the
operator, and the outcome. Beside it, `<version>-site-checks.json`
holds the machine checks of its Site column (`scripts/checklist-site-check.py`). Method is in the Analyzer
[game update guide](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/GAME_UPDATE_GUIDE.md);
working files stay in the update's run folders under
`BF6 Datamining\reports\weapon-analyzer-research\`.

Start the checklist here before the update (identity, decisions, run order, the patch-note
watchlist), and add the change rows from the scripted change lists after the capture.

| Update | Checklist | Result | Run folders |
|---|---|---|---|
| 2.1.2.0 (Casino Heist), 10 November 2026 | [2.1.2.0-checklist.md](2.1.2.0-checklist.md) | New build; site updated 10 November (NSW4 Carbine, balance, new attachments); site check 220 of 220 ([2.1.2.0-site-checks.json](2.1.2.0-site-checks.json)) | `builds\2.1.1.0\capture\pre-update-5383516-2026-11-09\`, `2026-11-10-update-2120-post` |
| Hotfix, 22 October 2026 (archive head 5383516) | None | Hotfix, same build: type layouts identical; 6 catalog record changes (four single-player face BindAssets, `SimEx_BR_ApplyProgressionWeapon`, DataVersion); raw 4 changed, no stored values | `builds\2.1.1.0\reports\client-new-check-2026-10-22\` |
| Hotfix, 15 October 2026 (archive head 5383474) | None | Hotfix, same build: type layouts identical; 19 catalog record changes (13 non-English string tables, four single-player face BindAssets, sound MasterPatch, DataVersion); raw 3 changed | `builds\2.1.1.0\reports\client-new-check-2026-10-15\` |
| 2.1.1.0 (Season 5), 13 October 2026 | [2.1.1.0-checklist.md](2.1.1.0-checklist.md) | New build | `2026-10-12-update-2110-pretrace`, `2026-10-13-update-2110-post` |
| 1.4.3.5, 30 September 2026 | [1.4.3.5-report.md](1.4.3.5-report.md) (report from before the checklist template) | New build | `builds\1.4.3.5\reports\`, `2026-10-01T001542-0400-patch-notes-coverage` |
| Hotfix, client 1.0.443.60769, 3 October 2026 | None | Hotfix, same build: only DataVersion changed in raw; the catalog's 1,014 added entries came from a loaded versus rebuilt cache | `builds\1.4.3.5\reports\client-60769-check-2026-10-03\` |
| 1.4.3.0, 15 to 16 September 2026 | [1.4.3.0-report.md](1.4.3.0-report.md) (report from before the checklist template); plan in [FROSTY_1.4.3.0_UPDATE_PLAN.md](../archive/FROSTY_1.4.3.0_UPDATE_PLAN.md); site [Interdictor check](https://github.com/raymdl/BF6-Weapon-Analyzer/blob/main/docs/archive/INTERDICTOR_1.4.3.0_CHECK.md) | New build | `builds\1.4.3.0\capture\`, `builds\1.4.3.0\reports\` |
| Hotfix "1.4.3.1", 16 September 2026 | None | Hotfix, same build: catalog unchanged (467,208 assets); only `CL_PurchaseButtonGroup` (store UI) and DataVersion changed | `builds\1.4.3.0\reports\hotfix-2026-09-16-catalog\` |
