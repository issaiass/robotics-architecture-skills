# Perplexity (Computer, Agent API and Spaces)

[← Back to README](../../README.md#using-the-skills) · Checked against the official docs on **2026-11-25**.

Perplexity supports the `SKILL.md` format in **Perplexity Computer** and the **Agent API**. It has no local skill folder. You upload the skill, and you upload or paste the files you want analysed.

> [!TIP]
> Use Perplexity for **design reviews and research-backed architecture decisions**, such as comparing simulators, middleware or policy runtimes. Use a local agent (Claude Code, Codex, Cursor and similar) when the work needs your checkout or a running ROS 2 / Docker stack.

## Perplexity Computer

1. Upload `skills/<skill-name>/SKILL.md` directly as a custom skill.
2. Upload the project files to review (for example `package.xml`, `launch/*.py`, `config/*.yaml`, `compose.yaml`).
3. Ask, naming the skill:

```text
Use the ros2-robotics-architecture skill. From the uploaded files, draft ARCHITECTURE.md
Sections 1–3 and a ROS graph contract table. Mark every claim source-verified or
proposed; nothing here is runtime-verified.
```

## Agent API

Each request can carry a `skills` array with up to 16 entries: built-in, inline or custom.

1. Zip one skill folder. The archive must contain exactly one `SKILL.md`:

   ```bash
   cd ~/robotics-architecture-skills/skills && zip -r ~/ros2-robotics-architecture.zip ros2-robotics-architecture
   ```

2. Upload it as a custom skill:

   ```bash
   curl https://api.perplexity.ai/v1/skills \
     -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
     -F "file=@$HOME/ros2-robotics-architecture.zip;type=application/zip"
   ```

3. Reference the returned id in your Agent API request:

   ```json
   {
     "skills": [
       { "type": "custom", "id": "skill_..." }
     ]
   }
   ```

The model sees each skill's name and description and loads the full skill when it needs it. Naming the skill in the prompt ("Use the ros2-robotics-architecture skill…") makes activation reliable.

## Spaces and regular chat (fallback)

Spaces have no skill loader. Add `SKILL.md` as a Space file, then put the [chat prompt template](other-tools.md#any-chat-assistant-prompt-template) in the Space instructions so every thread applies the workflow.

## What to expect

| Capability | Local agents | Perplexity |
| --- | --- | --- |
| Read your whole checkout | Yes | Only uploaded files |
| Run `ros2`, `docker compose config` and similar | Yes, with permission | No |
| Web research for upstream docs and version compatibility | Varies | **Strong** |
| Highest evidence level reachable | Runtime-verified (sim / mock) | Source-verified (uploaded files) |

## Sources

- [Perplexity Agent API: Skills](https://docs.perplexity.ai/docs/agent-api/skills)
- [Designing, refining, and maintaining agent skills at Perplexity](https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity)
