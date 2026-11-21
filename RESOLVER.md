# RESOLVER: Music Nerd Skills dispatcher

> The routing table for every skill in `skills/`. Match the request to one row, then
> **read that skill's `SKILL.md` before acting.** Verified by `scripts/check_resolvable.py`
> (every skill has a route; every route resolves) and `scripts/run_resolver_eval.py`
> (routing fixtures + full coverage).

## dev: building Music Nerd

| Intent | Skill |
|---|---|
| write / update a tracking issue, add a row to the PR matrix, log what shipped, close out an issue | `mn-dev` |
| implement / ship / build out issue #N, open PRs for the remaining rows | `mn-dev` |
| preview-test a PR, documented-vs-observed matrix, merge and promote a release to production | `mn-dev` |
| which repo does this go in (MusicNerdWeb vs MusicNerdAPI), branch names, draft PRs | `mn-dev` |
| file a bug, triage bugs at stand-up, acceptance criteria, owner / done when / customer, is this done, the GitHub Project for the sprint, coding standards (KISS, YAGNI, DRY, SRP, OCP, no dead code) | `mn-dev` |

## board: sharing work with the team

| Intent | Skill |
|---|---|
| post an issue or PR to the Vercel Board, update the code-review thread, post a preview test or a shipped message there | `mn-board` |
| connect an agent to the board, claim or complete a board task, what's on the board | `mn-board` |

## marketing: getting artists to claim their profile

| Intent | Skill |
|---|---|
| Music Nerd marketing, this week's Music Nerd videos | `mn-marketing` |
| a video announcing a shipped Music Nerd feature | `mn-marketing` |
| highlight an artist who uses Music Nerd | `mn-marketing` |
| get more artists to claim, show how claiming works, measure claims per post | `mn-marketing` |

## FEED//FWD episodes and recaps

| Intent | Skill |
|---|---|
| edit or package a FEED//FWD podcast, match the pilot, fix audio or lower thirds, make episode artwork and description | `mn-feed-fwd-podcast` |
| write or revise a FEED//FWD session recap or podcast companion article from a recording | `mn-feed-fwd-recap` |

---

## Boundaries

- **GitHub Project vs Vercel Board.** Adding an issue to the GitHub Project (Todo / In Progress / Done lanes)
  → `mn-dev`. Posting to the team's Vercel Board (`code-review`, `tasks`) → `mn-board`.
- **Building vs announcing.** Shipping the feature (issue, PRs, preview, release) → `mn-dev`.
  The video that announces it once it is live → `mn-marketing`.
- **Music Nerd vs Recoup.** `mn-marketing` is only for Music Nerd posts. Recoup's own daily
  marketing is Recoup's `recoup-internal-marketing` skill (installed separately with
  `npx skills add recoupable/skills`); `mn-marketing` reuses its video mechanics but never
  runs Recoup's accounts.

- Episode video and packaging use `mn-feed-fwd-podcast`; standalone articles use `mn-feed-fwd-recap`. A shipped-feature promo remains `mn-marketing`.
