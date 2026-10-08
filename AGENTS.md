# AGENTS.md

This repo holds Music Nerd's agent skills, one folder per skill: `skills/<name>/SKILL.md`, with YAML frontmatter
(`name` matching the folder, a `description` that says when to use it).

- **Public repo.** No secrets, tokens, email addresses, Supabase refs, private customer data or personal paths.
  Env-var names only.
- **Branches and PRs** follow `skills/mn-dev`: branch from `main` (`<contributor>/<slug>`), open the PR as a draft,
  squash merge to `main`.
- **Keep a skill's facts current.** A skill that names a handle, domain, endpoint or person is checked against the
  live thing when it changes (2026-10-08: the X/Instagram handle became `@musicnerdnet`).
- One skill owns each rule; link to it from others instead of copying it.
