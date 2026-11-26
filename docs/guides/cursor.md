# Cursor

[← Back to README](../../README.md#using-the-skills) · Paths checked against the official docs on **2026-11-25**.

Cursor's Agent loads `SKILL.md` folders from its own directories, from the shared `.agents/skills/` folder, and, for compatibility, from Claude Code and Codex folders.

## Where skills live

| Scope | Paths |
| --- | --- |
| Project | `.cursor/skills/` or `.agents/skills/`. Nested folders anywhere in the repo are scoped to their sub-tree. |
| User | `~/.cursor/skills/` or `~/.agents/skills/` |
| Compatibility | `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, `~/.codex/skills/` |

> [!TIP]
> If you already installed the skills for Claude Code or Codex, Cursor picks them up with no extra step.

## Install

```bash
git clone https://github.com/issaiass/robotics-architecture-skills ~/robotics-architecture-skills
mkdir -p .cursor/skills          # from your robot repo root
cp -r ~/robotics-architecture-skills/skills/* .cursor/skills/
```

```powershell
New-Item -ItemType Directory -Force ".cursor\skills" | Out-Null
Copy-Item -Recurse -Force "$HOME\robotics-architecture-skills\skills\*" ".cursor\skills\"
```

Cursor walks the skills folder recursively, so you may group skills in category sub-folders. A skill's name comes from its own folder.

## Use

| Mode | How |
| --- | --- |
| Automatic | Describe the task in Agent chat; Cursor matches it against each `description`. |
| Slash | Type `/` in Agent chat, search for `robotics-web-architecture`, and send your task. The skill applies to that message. |
| Session mode | Press <kbd>Alt</kbd>+<kbd>Enter</kbd> (Windows / Linux) or <kbd>Option</kbd>+<kbd>Enter</kbd> (macOS) on the selected skill to keep it as a custom mode for the session. |

## Example

```text
/robotics-web-architecture Document the operator console in apps/ and services/robot-gateway.
Trace one telemetry sample from the robot to the browser and one "go to waypoint"
command back. Use the mock gateway in environments/mock only.
```

Expected output: `ARCHITECTURE.md` with the browser → API → gateway → robot diagram, a contract table for each WebSocket event and REST route, and findings about server-side authorization for subscriptions and commands.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| The skill does not appear after `/` | Open Cursor's settings and check the **Skills** list. The `name` in the frontmatter must match the folder name (lowercase, digits, hyphens). |
| The agent ignores the workflow | Invoke it explicitly with `/`, or switch it to a session mode. |
| Same skill listed twice | It exists in two scanned folders (for example `.cursor/skills/` and `.claude/skills/`). Delete one copy. |

## Sources

- [Cursor: Agent Skills](https://cursor.com/docs/skills)
