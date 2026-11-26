# Windsurf (Cascade)

[← Back to README](../../README.md#using-the-skills) · Paths checked against the official docs on **2026-11-25**.

Windsurf's Cascade agent supports `SKILL.md` skills with progressive disclosure. By default the model sees only each skill's name and description. The full file loads when Cascade invokes the skill or when you mention it.

> [!IMPORTANT]
> **Naming note:** Windsurf's skills documentation now redirects to the *Devin Local* docs, which share the same harness. Newer builds add `.devin/skills/` and `~/.config/devin/skills/` and keep reading `.agents/skills/` and the legacy `.windsurf/skills/`. **`.agents/skills/` is the safest choice across versions.**

## Where skills live

| Scope | Paths |
| --- | --- |
| Workspace | `.windsurf/skills/<name>/` or `.agents/skills/<name>/` (newer builds also read `.devin/skills/<name>/`) |
| Global | `~/.codeium/windsurf/skills/<name>/` or `~/.agents/skills/<name>/` (newer builds also read `~/.config/devin/skills/<name>/`) |
| Organisation | `/etc/windsurf/skills/` (Linux / WSL) · `C:\ProgramData\Windsurf\skills\` (Windows) |

## Install

```bash
git clone https://github.com/issaiass/robotics-architecture-skills ~/robotics-architecture-skills
mkdir -p .agents/skills          # from your robot repo root
cp -r ~/robotics-architecture-skills/skills/* .agents/skills/
```

```powershell
New-Item -ItemType Directory -Force ".agents\skills" | Out-Null
Copy-Item -Recurse -Force "$HOME\robotics-architecture-skills\skills\*" ".agents\skills\"
```

You can also create skills from the UI: open the Cascade panel, open the customizations menu, choose **Skills**, then add a workspace or global skill and paste the `SKILL.md` content.

## Use

| Mode | How |
| --- | --- |
| Automatic | Describe the task; Cascade invokes the skill whose description matches. |
| Mention | `@robotics-simulation-validation` in the Cascade input (Windsurf builds). |
| Slash | `/robotics-simulation-validation` (Devin Local builds). |

## Example

```text
@robotics-simulation-validation Build a smoke test for our MuJoCo scene in scenes/warehouse.xml:
robot spawns, clock advances, reset restores the initial pose. Then add one regression
scenario with a 5 kg payload and record pass criteria with units.
```

Expected output: a `tests/` smoke script, a scenario file with seeds and thresholds, and an `ARCHITECTURE.md` Section 3 table for physics timestep, solver settings and sensor rates. Every result is labelled *simulation-verified* and none is reported as hardware evidence.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Skill name rejected | Names must be lowercase letters, numbers and hyphens, and match the folder name. |
| Works in one build, missing in another | Move the skills to `.agents/skills/`, which both Windsurf and Devin Local builds read. |

## Sources

- [Windsurf: Cascade skills](https://docs.windsurf.com/windsurf/cascade/skills) (now redirects to [Devin Local skills](https://docs.devin.ai/desktop/cascade/skills))
