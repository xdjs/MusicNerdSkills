# Music Nerd Skills

Agent skills for building and marketing [Music Nerd](https://musicnerd.net). The repo root is one plugin;
every skill is a folder under [`skills/`](skills/) with a `SKILL.md`.

## What's inside

| Skill | What it's for |
|---|---|
| [`mn-dev`](skills/mn-dev/SKILL.md) | How Music Nerd plans, builds and ships work: the tracking issue (PR matrix, closure notes, dated decisions) and the delivery loop (docs first, TDD, preview verification, release). |
| [`mn-marketing`](skills/mn-marketing/SKILL.md) | Short videos that get artists to claim their Music Nerd profile: feature launches, artist highlights, how to claim. Script, $0 draft, final, publish, measure claims. Needs Recoup's `recoup-internal-marketing` skill (`npx skills add recoupable/skills`). |

[`RESOLVER.md`](RESOLVER.md) maps a request to the skill that handles it.

## Install

### npx (any agent)

```bash
npx skills add xdjs/MusicNerdSkills
```

This puts the skills where your agent loads them (`.agents/skills/`, `.claude/skills/`, and so on).

### Claude Code

```bash
/plugin marketplace add xdjs/MusicNerdSkills
/plugin install musicnerd-skills@musicnerd
```

### Codex and other hosts

Install this repository through the host's plugin marketplace or local-plugin flow. The Codex manifest is
`.codex-plugin/plugin.json`; the agents registry is `.agents/plugins/marketplace.json`. No MCP server or API
key is bundled.

## Contributing

See [`contributing.md`](contributing.md) and [`AGENTS.md`](AGENTS.md). Skills started in `xdjs/MusicNerdWeb`;
their history up to 2026-10-08 lives there.

## License

[MIT](LICENSE)
