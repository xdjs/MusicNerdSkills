# Contributing

## Adding or changing a skill

1. Branch from `main` as `<contributor>/<slug>`.
2. Create or edit `skills/mn-<name>/SKILL.md`:

```yaml
---
name: mn-<name>
description: What it does and when to use it. Include the phrases a user would say.
---
```

3. Keep the body under 5,000 words, critical instructions first. Move long reference material to the
   skill's own `references/`, code to its own `scripts/`.
4. A new skill needs a row in `RESOLVER.md` and at least one fixture in `resolver-eval.jsonl`.
5. Run the gates, then open a draft PR against `main`.

## Checklist (runs in CI)

- [ ] **Public-safe.** No secrets, tokens, email addresses, Supabase refs or personal paths.
- [ ] **Self-contained.** Only files inside the skill's own directory; no `../`, no other skill's folder.
- [ ] **No platform variables** (`${CLAUDE_PLUGIN_ROOT}`, `$CLAUDE_*`) in the body.
- [ ] **Backtick paths, not markdown links,** for `references/` and `scripts/`.
- [ ] **Facts checked** against the live thing (handles, domains, endpoints, people).

```bash
python3 scripts/portability_lint.py
python3 scripts/validate_manifests.py
python3 scripts/check_resolvable.py
python3 scripts/run_resolver_eval.py
```

See `AGENTS.md` for the full rules.
