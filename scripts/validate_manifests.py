#!/usr/bin/env python3
"""Validate the Music Nerd Skills plugin and marketplace manifests.

Checks:
  - every marketplace.json / plugin.json is valid JSON;
  - the package is skills plus one MCP server: `.mcp.json` declares only the
    `musicnerd` HTTP server, the Codex and Cursor manifests point at it, there
    are no hooks, apps or commands, and every manifest carries the same version;
  - marketplace plugins have name + source + semver version, source dir exists,
    names are unique;
  - dual-manifest PARITY: .claude-plugin/marketplace.json and
    .agents/plugins/marketplace.json list the same plugins (name/source/version);
    the .agents copy may add an `interface{}` block, which is ignored.

Usage: python3 scripts/validate_manifests.py
Exit 0 = valid; 1 = problems (printed). Standard library only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SEMVER = re.compile(r"^\d+\.\d+\.\d+([-+].+)?$")

CLAUDE_MARKET = REPO_ROOT / ".claude-plugin" / "marketplace.json"
AGENTS_MARKET = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"


def load_json(path: Path) -> tuple[dict | list | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except json.JSONDecodeError as exc:
        return None, f"invalid JSON: {exc}"
    except OSError as exc:
        return None, f"cannot read: {exc}"


def discover(name: str) -> list[Path]:
    skip = {"node_modules", ".git", ".worktrees"}
    return sorted(
        p for p in REPO_ROOT.rglob(name)
        if not skip.intersection(p.relative_to(REPO_ROOT).parts)
    )


def validate_marketplace(path: Path, problems: list[str]) -> list[dict]:
    data, err = load_json(path)
    rel = path.relative_to(REPO_ROOT)
    if err:
        problems.append(f"{rel}: {err}")
        return []
    if not isinstance(data, dict) or not isinstance(data.get("plugins"), list):
        problems.append(f"{rel}: missing top-level 'plugins' array")
        return []

    plugins = data["plugins"]
    seen_names: set[str] = set()
    for i, plugin in enumerate(plugins):
        loc = f"{rel} plugins[{i}]"
        for field in ("name", "source", "version"):
            if field not in plugin:
                problems.append(f"{loc}: missing required field '{field}'")
        name = plugin.get("name", "")
        if name in seen_names:
            problems.append(f"{loc}: duplicate plugin name '{name}'")
        seen_names.add(name)
        version = plugin.get("version", "")
        if version and not SEMVER.match(str(version)):
            problems.append(f"{loc}: version '{version}' is not semver")
        source = plugin.get("source")
        if source:
            src_dir = (REPO_ROOT / source).resolve()
            if not src_dir.is_dir():
                problems.append(f"{loc}: source '{source}' is not a directory")
    return plugins


def parity(claude: list[dict], agents: list[dict], problems: list[str]) -> None:
    def key_set(plugins: list[dict]) -> set[tuple[str, str, str]]:
        return {(p.get("name", ""), p.get("source", ""), str(p.get("version", ""))) for p in plugins}

    c, a = key_set(claude), key_set(agents)
    only_claude = c - a
    only_agents = a - c
    for name, source, version in sorted(only_claude):
        problems.append(f"PARITY: in .claude-plugin only: {name} ({source} @ {version})")
    for name, source, version in sorted(only_agents):
        problems.append(f"PARITY: in .agents only: {name} ({source} @ {version})")


PLUGIN_NAME = "musicnerd"
PLUGIN_MANIFESTS = (".claude-plugin", ".codex-plugin", ".cursor-plugin")
MARKETPLACES = (".claude-plugin", ".agents/plugins")
MCP_FILE = ".mcp.json"
MCP_SERVERS = {"musicnerd": {"type": "http", "url": "https://api.musicnerd.net/mcp"}}


def validate_mcp(problems: list[str]) -> None:
    """One MCP file at the root, declaring only the Music Nerd server. Claude Code reads
    it by default; the Codex and Cursor manifests point at it."""
    data, err = load_json(REPO_ROOT / MCP_FILE)
    if err or not isinstance(data, dict):
        problems.append(f"{MCP_FILE}: missing or invalid ({err or 'not an object'})")
    elif data.get("mcpServers") != MCP_SERVERS:
        problems.append(f"{MCP_FILE}: mcpServers must be exactly {json.dumps(MCP_SERVERS)}")
    for folder in (".codex-plugin", ".cursor-plugin"):
        data, _ = load_json(REPO_ROOT / folder / "plugin.json")
        if isinstance(data, dict) and data.get("mcpServers") != f"./{MCP_FILE}":
            problems.append(f'{folder}/plugin.json: expected "mcpServers": "./{MCP_FILE}"')
    data, _ = load_json(REPO_ROOT / ".claude-plugin" / "plugin.json")
    if isinstance(data, dict) and "mcpServers" in data:
        problems.append(f".claude-plugin/plugin.json: drop 'mcpServers'; Claude Code reads {MCP_FILE}")


def validate_distribution(problems: list[str]) -> None:
    """Keep the package to skills and the MCP server: no hooks, apps or commands,
    and one name and version across every plugin.json and both marketplaces."""
    versions = set()
    for folder in PLUGIN_MANIFESTS:
        path = REPO_ROOT / folder / "plugin.json"
        data, err = load_json(path)
        if err or not isinstance(data, dict):
            problems.append(f"{folder}/plugin.json: missing or invalid manifest")
            continue
        versions.add(data.get("version"))
        if data.get("name") != PLUGIN_NAME:
            problems.append(f"{folder}/plugin.json: name must be '{PLUGIN_NAME}'")
        for key in ("hooks", "apps", "commands", "agents"):
            if key in data:
                problems.append(f"{folder}/plugin.json: '{key}' is not shipped")
        if folder != ".claude-plugin" and data.get("skills") != "./skills/":
            problems.append(f'{folder}/plugin.json: expected "skills": "./skills/"')
    for folder in MARKETPLACES:
        data, err = load_json(REPO_ROOT / folder / "marketplace.json")
        if err or not isinstance(data, dict):
            problems.append(f"{folder}: missing or invalid marketplace")
            continue
        names = [entry.get("name") for entry in data.get("plugins", [])]
        if names != [PLUGIN_NAME]:
            problems.append(f"{folder}/marketplace.json: must list exactly one plugin, '{PLUGIN_NAME}'")
        for entry in data.get("plugins", []):
            if entry.get("name") == PLUGIN_NAME:
                versions.add(entry.get("version"))
    if len(versions) != 1 or None in versions:
        problems.append("All plugin and marketplace versions must match")
    for name in ("mcp.json", ".app.json", "hooks"):
        if (REPO_ROOT / name).exists():
            problems.append(f"{name}: not shipped (one MCP file, {MCP_FILE}; no apps or lifecycle hooks)")
    for path in (REPO_ROOT / "skills").glob("*/SKILL.md"):
        sections = path.read_text(encoding="utf-8").split("---", 2)
        if len(sections) == 3 and re.search(r"^hooks\s*:", sections[1], re.MULTILINE):
            problems.append(f"{path.relative_to(REPO_ROOT)}: remove skill lifecycle hooks")


def main() -> int:
    problems: list[str] = []

    validate_distribution(problems)
    validate_mcp(problems)

    # 1. JSON validity for every manifest file.
    checked = 0
    for fname in ("marketplace.json", "plugin.json"):
        for path in discover(fname):
            checked += 1
            _, err = load_json(path)
            if err:
                problems.append(f"{path.relative_to(REPO_ROOT)}: {err}")

    # 2. Marketplace structure.
    claude_plugins = validate_marketplace(CLAUDE_MARKET, problems) if CLAUDE_MARKET.exists() else []
    if not CLAUDE_MARKET.exists():
        problems.append(f"missing {CLAUDE_MARKET.relative_to(REPO_ROOT)}")
    agents_plugins = validate_marketplace(AGENTS_MARKET, problems) if AGENTS_MARKET.exists() else []
    if not AGENTS_MARKET.exists():
        problems.append(f"missing {AGENTS_MARKET.relative_to(REPO_ROOT)}")

    # 3. Dual-manifest parity.
    if claude_plugins and agents_plugins:
        parity(claude_plugins, agents_plugins, problems)

    if problems:
        print(f"MANIFEST VALIDATION FAILED — {len(problems)} problem(s):\n")
        for p in problems:
            print(f"  ✗ {p}")
        return 1

    print(f"MANIFEST VALIDATION PASSED — {checked} manifest file(s) valid; dual-manifest parity OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
