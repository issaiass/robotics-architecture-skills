# Other tools: GitHub Copilot, Gemini CLI, ChatGPT, Aider and any chat assistant

[← Back to README](../../README.md#using-the-skills) · Paths checked against the official docs on **2026-11-25**.

The skills follow the open [Agent Skills](https://agentskills.io) format, which about 40 clients support, including GitHub Copilot, VS Code, Gemini CLI, Goose, OpenCode, Roo Code, Amp and Kiro. **Most of them read `.agents/skills/`**, so try that folder first, then check the tool's docs.

## GitHub Copilot (VS Code, Copilot CLI, cloud agent)

| Scope | Paths |
| --- | --- |
| Project | `.github/skills/`, `.claude/skills/` or `.agents/skills/` |
| Personal | `~/.copilot/skills/` or `~/.agents/skills/` |

```bash
mkdir -p .github/skills
cp -r ~/robotics-architecture-skills/skills/* .github/skills/
```

Describe the task in Copilot Chat or assign an issue to the cloud agent. Copilot loads the skill whose description matches. The GitHub CLI also provides `gh skill` to discover and install skills from repositories; see [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).

## Gemini CLI

> [!WARNING]
> Google replaced Gemini CLI with **Antigravity CLI** for unpaid and Google One users on 2026-06-18. Paid plans keep Gemini CLI. Check the current docs for Antigravity paths.

| Scope | Paths (`.agents/` takes precedence within a tier) |
| --- | --- |
| Workspace | `.gemini/skills/` or `.agents/skills/` |
| User | `~/.gemini/skills/` or `~/.agents/skills/` |

```bash
# install one skill from this repository into the workspace
gemini skills install https://github.com/issaiass/robotics-architecture-skills.git \
  --path skills/robotics-agentic-ai-architecture --scope workspace

gemini skills list --all        # confirm it is discovered
```

Inside a session: `/skills list`, `/skills link <path> --scope workspace`, `/skills reload`. Gemini asks for consent before it activates a skill.

## ChatGPT

Where skills are enabled for your workspace, type `@` and select the skill (the same skills Codex uses). Otherwise create a **Project**, add `SKILL.md` as a project file, and paste the template below into the project instructions.

## Aider

Aider has no skill loader, but it can load a file as read-only context:

```bash
aider --read ~/robotics-architecture-skills/skills/ros2-robotics-architecture/SKILL.md
```

Then ask: `Follow the workflow in SKILL.md to audit src/ and write ARCHITECTURE.md.`

## Any chat assistant: prompt template

Use this with Grok chat, Perplexity Spaces, ChatGPT Projects, Le Chat, DeepSeek, local LLMs, or any assistant that accepts files or long prompts.

```text
You are applying the skill below. Follow its Workflow steps in order and use its
"Embedded documentation standard" for any document you write.
Label every claim as: proposed, source-verified, runtime-verified or unresolved.
Never claim runtime or hardware evidence you did not observe. List what still
needs a simulator, bench rig or the physical robot.

<skill>
[paste the full contents of skills/<skill-name>/SKILL.md]
</skill>

<files>
[paste or attach: manifests, launch files, configs, Compose files …]
</files>

Task: [for example: draft ARCHITECTURE.md Sections 1–3 for this ROS 2 workspace]
```

## Sources

- [Agent Skills specification and client list](https://agentskills.io)
- [GitHub Copilot: about agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Gemini CLI: skills](https://geminicli.com/docs/cli/skills/)
- [Build skills (ChatGPT / Codex)](https://learn.chatgpt.com/docs/build-skills)
