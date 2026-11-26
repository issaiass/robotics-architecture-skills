# Grok (Grok Build CLI and Grok chat)

[← Back to README](../../README.md#using-the-skills) · Paths checked against the official docs on **2026-11-25**.

xAI's **Grok Build** CLI loads `SKILL.md` skills natively and also reads Claude Code skills with no configuration. **Grok chat** (web and app) has no skill loader, so use the attach-and-instruct fallback at the end of this page.

## Grok Build CLI: where skills live

| Scope | Paths |
| --- | --- |
| Project | `.grok/skills/`, searched from the current directory up to the repo root |
| User | `~/.grok/skills/` and `~/.agents/skills/` |
| Claude Code compatibility | Claude Code skills (`.claude/skills/`, `~/.claude/skills/`) are read automatically |
| Extra folders | `[skills] paths` in `~/.grok/config.toml` |
| Plugins | the `skills/` folder of any enabled plugin |

## Install

**Option A: point Grok at the clone, no copying.** `git pull` then updates the skills in place.

```toml
# ~/.grok/config.toml
[skills]
paths = ["/home/<you>/robotics-architecture-skills/skills"]
# Windows: paths = ["C:/Users/<you>/robotics-architecture-skills/skills"]
```

**Option B: copy into the project.**

```bash
git clone https://github.com/issaiass/robotics-architecture-skills ~/robotics-architecture-skills
mkdir -p .grok/skills
cp -r ~/robotics-architecture-skills/skills/* .grok/skills/
```

```powershell
New-Item -ItemType Directory -Force ".grok\skills" | Out-Null
Copy-Item -Recurse -Force "$HOME\robotics-architecture-skills\skills\*" ".grok\skills\"
```

> [!TIP]
> If you already installed the skills for Claude Code (`~/.claude/skills/`), Grok Build sees them with no further step.

## Use

| Mode | How |
| --- | --- |
| Slash | `/robot-learning <task>`, because user-invocable skills appear as slash commands |
| Manage | `/skills` opens the extensions view, where you can enable and disable skills |
| Automatic | Describe the task; the model loads a matching skill unless its frontmatter sets `disable-model-invocation` |

## Example

```text
/robot-learning Review our PPO setup in configs/ppo_walker.yaml and envs/walker_env.py.
Check the observation/action contract against the controller, termination vs truncation,
and propose a fixed evaluation protocol against the scripted baseline.
```

Expected output: a contract table (shapes, units, frames, normalisation, action bounds), a list of reward-shaping risks, an evaluation table that keeps return and task success separate, and a README Section 8 walkthrough for one reproducible train → evaluate run.

## Grok chat (no skill loader)

1. Create a Project, or start a conversation, and **attach** `skills/<skill-name>/SKILL.md`.
2. Attach the repository files you want reviewed: manifests, launch files, Compose files, configs.
3. Send the [chat prompt template](other-tools.md#any-chat-assistant-prompt-template).

> [!WARNING]
> Grok chat cannot read your checkout or run commands. Expect *source-verified* claims about the files you attached and nothing more.

## Sources

- [xAI: Skills, plugins and marketplaces](https://docs.x.ai/build/features/skills-plugins-marketplaces)
- [Grok Build CLI](https://x.ai/cli)
