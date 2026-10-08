# Music Nerd skills

Agent skills for building and marketing [Music Nerd](https://musicnerd.net). Each skill is a folder under
[`skills/`](skills/) with a `SKILL.md`.

| Skill | What it's for |
|---|---|
| [`mn-dev`](skills/mn-dev/SKILL.md) | How Music Nerd plans, builds and ships work: the tracking issue (PR matrix, closure notes, dated decisions) and the delivery loop (docs first, TDD, preview verification, release). |
| [`mn-marketing`](skills/mn-marketing/SKILL.md) | Short videos that get artists to claim their Music Nerd profile: feature launches, artist highlights, how to claim. Script, $0 draft, final, publish, measure claims. |

## Install

```bash
npx skills add xdjs/MusicNerdSkills
```

This puts the skills where your agent loads them (`.agents/skills/`, `.claude/skills/`, and so on).

## Contributing

Skills started in `xdjs/MusicNerdWeb` (`skills/mn-dev`, `.agents/skills/mn-marketing`); their history up to
2026-10-08 lives there. Change them here: branch from `main`, open a draft PR, follow [`AGENTS.md`](AGENTS.md).
