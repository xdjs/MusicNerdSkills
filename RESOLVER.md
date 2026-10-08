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

## marketing: getting artists to claim their profile

| Intent | Skill |
|---|---|
| Music Nerd marketing, this week's Music Nerd videos | `mn-marketing` |
| a video announcing a shipped Music Nerd feature | `mn-marketing` |
| highlight an artist who uses Music Nerd | `mn-marketing` |
| get more artists to claim, show how claiming works, measure claims per post | `mn-marketing` |

---

## Boundaries

- **Building vs announcing.** Shipping the feature (issue, PRs, preview, release) → `mn-dev`.
  The video that announces it once it is live → `mn-marketing`.
- **Music Nerd vs Recoup.** `mn-marketing` is only for Music Nerd posts. Recoup's own daily
  marketing is Recoup's `recoup-internal-marketing` skill (installed separately with
  `npx skills add recoupable/skills`); `mn-marketing` reuses its video mechanics but never
  runs Recoup's accounts.
