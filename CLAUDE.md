# BF6 Frosty Research — Claude Guidelines

## Git Workflow

- **Do not push commits until explicitly told to.** Commit freely, but wait for the user to say "push" before running `git push`.
- **Squash research commits at push time.** Before pushing, combine the unpushed commits into one commit per research session, with a message that lists the leads or topics covered. If a squashed hash is cited anywhere in the repo, update the citation. Show the user the commit list and get their OK before pushing. Never rewrite pushed commits.
- **Site repo changes** (`..\BF6 Weapon Analyzer`: data/, sim/, ui/, copies of site-bound receipts and shared scripts, the lead-index/site-evidence interface files) are committed there, following that repo's CLAUDE.md. Research work never changes site data without the operator's approval.

## Records

- Close a lead with a receipt carrying a `record`, the topic-page edit, its queue row removed, then `python scripts/frosty-records.py build && python scripts/frosty-records.py check`. `build` also refreshes the site interface files; commit those in the site repo.
