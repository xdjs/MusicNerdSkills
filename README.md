# Music Nerd plugin

The `musicnerd` plugin for the Music Nerd team: the agent skills we use to build and market
[Music Nerd](https://musicnerd.net), plus the Music Nerd MCP server (`https://api.musicnerd.net/mcp`). The repo
root is one plugin; every skill is a folder under [`skills/`](skills/) with a `SKILL.md`.

## What's inside

| Skill | What it's for |
|---|---|
| [`mn-dev`](skills/mn-dev/SKILL.md) | How Music Nerd plans, builds and ships work: the tracking issue (PR matrix, closure notes, dated decisions) and the delivery loop (docs first, TDD, preview verification, release). |
| [`mn-board`](skills/mn-board/SKILL.md) | Share issues and PRs with the team on the Vercel Board: one `code-review` thread per issue, matrix rows as tasks, preview-test and shipped posts. Connect through the Music Nerd MCP or the `vercel board` CLI. |
| [`mn-marketing`](skills/mn-marketing/SKILL.md) | Short videos that get artists to claim their Music Nerd profile: feature launches, artist highlights, how to claim. Script, $0 draft, final, publish, measure claims. Needs Recoup's `recoup-internal-marketing` skill (`npx skills add recoupable/skills`). |
| [`mn-feed-fwd-podcast`](skills/mn-feed-fwd-podcast/SKILL.md) | FEED//FWD editing, audio, artwork, episode packaging and handoff in the pilot style. |
| [`mn-feed-fwd-recap`](skills/mn-feed-fwd-recap/SKILL.md) | Source-backed FEED//FWD articles and companion recaps. |

[`RESOLVER.md`](RESOLVER.md) maps a request to the skill that handles it.

## Install

Install steps for Claude Code, Codex and Cursor, and how to sign in to the MCP server, are at
[docs.musicnerd.net/plugin](https://docs.musicnerd.net/plugin). In Claude Code:

```bash
claude plugin install musicnerd --marketplace xdjs/MusicNerdSkills
```

The plugin's MCP server signs in with your Music Nerd account (OAuth); there is no API key.

Skills only, for any agent:

```bash
npx skills add xdjs/MusicNerdSkills
```

## Layout

| Path | For |
|---|---|
| `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` | Claude Code |
| `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` | Codex |
| `.cursor-plugin/plugin.json` | Cursor |
| `.mcp.json` | The `musicnerd` MCP server, shared by all three |
| `skills/` | The skills, shared by all three |

## Contributing

See [`contributing.md`](contributing.md) and [`AGENTS.md`](AGENTS.md). Skills started in `xdjs/MusicNerdWeb`;
their history up to 2026-10-08 lives there.

## License

[MIT](LICENSE)
