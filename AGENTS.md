# AGENTS.md: Music Nerd Skills

Context for any AI agent working in this repository.

## Purpose

Music Nerd's agent skills: how the team builds and ships [Music Nerd](https://musicnerd.net), and how it
markets it. The skills moved here from `xdjs/MusicNerdWeb` (`skills/mn-dev`, `.agents/skills/mn-marketing`);
their history up to 2026-10-08 lives there. MusicNerdWeb refers to them by name, so keep the names.

## Structure

The repo **is one flat plugin**, rooted at the repo root. It installs as a Claude/agents marketplace plugin,
a Codex plugin, or with a bare `npx skills add xdjs/MusicNerdSkills`.

```text
xdjs/MusicNerdSkills/         ← the repo root IS the plugin
├── skills/
│   ├── mn-dev/               ← tracking issues, PR matrix, TDD, preview verification, release
│   └── mn-marketing/         ← short videos that get artists to claim their profile
├── RESOLVER.md               ← routing table (request → one skill)
├── resolver-eval.jsonl       ← routing fixtures
├── scripts/                  ← the four validation gates
├── .claude-plugin/           ← plugin.json + marketplace.json (Claude)
├── .codex-plugin/            ← plugin.json (Codex)
├── .agents/plugins/          ← marketplace.json (agents registry)
├── README.md
├── contributing.md
└── AGENTS.md                 ← this file (CLAUDE.md symlinks here)
```

A skill may carry its own `references/`, `scripts/`, `templates/` and `fixtures/`. There are no shared root
folders, agents, MCP servers or hooks; add them only when a skill needs them.

**Prerequisite, not a dependency:** `mn-marketing` builds on Recoup's `recoup-internal-marketing` skill for the
shared video mechanics. Install it separately with `npx skills add recoupable/skills`. Nothing from it is
copied here; `scripts/portability_lint.py` lists the files `mn-marketing` points at in that skill.

## How skills load

1. **Frontmatter** (`name` + `description`): always in context. This is how an agent decides to load a skill.
2. **SKILL.md body**: loaded when the skill is relevant.
3. **Linked files** (`references/`, `scripts/`, ...): loaded on demand.

The `description` is the trigger. A vague one never fires.

## Rules

1. **Public repo.** No secrets, tokens, email addresses, Supabase refs, private customer data or personal
   paths. Env-var names only.
2. **Read before you act.** Read a skill's `SKILL.md` before running or citing it.
3. **Self-contained.** A skill reads only files inside its own directory, with backtick paths
   (`` `references/foo.md` ``), never markdown links, `../` or `${CLAUDE_*}` variables.
4. **One skill, one job.** One skill owns each rule; link to it from others instead of copying it.
5. **Composable.** Other skills may be loaded at once; never assume yours is the only one.
6. **No slash-command files or lifecycle hooks.** A skill already gets a `/name` entry.

## Skill format

```text
skills/mn-<name>/
├── SKILL.md          ← required: instructions + YAML frontmatter
├── references/       ← optional
├── scripts/          ← optional; run as `python3 scripts/foo.py`
├── templates/        ← optional
└── fixtures/         ← optional
```

```yaml
---
name: mn-<name>          # matches the folder
description: What it does, when to use it, and the phrases a user would say.
---
```

## Adding a skill

1. Create `skills/mn-<name>/SKILL.md`.
2. Add a row in `RESOLVER.md` and at least one positive fixture in `resolver-eval.jsonl` (plus a `not` case
   for the nearest neighbour).
3. Keep the version in sync across `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json` and both
   `marketplace.json` files (the two marketplaces must agree on name, source and version).
4. Run the gates. All four must exit 0; CI runs them on every PR and push to `main`:

```bash
python3 scripts/portability_lint.py      # every skill is self-contained and portable
python3 scripts/validate_manifests.py    # manifests valid, versions match, marketplace parity
python3 scripts/check_resolvable.py      # every skill routed; every route resolves
python3 scripts/run_resolver_eval.py     # fixtures valid; every skill covered
```

## Branches and PRs

Per `skills/mn-dev`: branch from `main` as `<contributor>/<slug>` (your own prefix; `codex/<slug>` for Codex),
conventional commits, open the PR as a draft and keep it a draft until its developer says it is ready, squash
merge to `main`.

## Keep facts current

A skill that names a handle, domain, endpoint or person is checked against the live thing when it changes.
2026-10-08: the X/Instagram handle became `@musicnerdnet`.
