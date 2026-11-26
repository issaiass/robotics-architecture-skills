# Prompt cookbook

[← Back to README](../../README.md#using-the-skills)

Each skill handles four kinds of request: **design** (new system), **document** (existing repo → `ARCHITECTURE.md` + `README.md`), **audit** (findings with locations and verification steps), and **implement** (change files within scope).

> [!TIP]
> The prompts use `/name`. Replace it with your tool's syntax: `$name` in Codex, `@name` in Windsurf, or no prefix with automatic activation.

## A good prompt states four things

| Element | Why the skill needs it | Example |
| --- | --- | --- |
| Scope | Workflow step 1 starts by fixing the task and boundary | "the `/cmd_vel` path", "the sim Compose profile" |
| Deliverable | Picks between full docs, an audit or an implementation | "write ARCHITECTURE.md and README.md", "findings only" |
| Mode | Evidence stays attached to sim, mock, bench or robot | "isolated Gazebo only", "static review, no commands" |
| Boundary | What the agent must not touch | "do not start containers with host devices", "no hardware" |

## `ros2-robotics-architecture`

```text
/ros2-robotics-architecture Design the package layout and ROS graph for a 6-DoF arm with a
parallel gripper on ROS 2 Jazzy, ros2_control and MoveIt 2. Label every choice as proposed.
```

```text
/ros2-robotics-architecture Document this workspace: write ARCHITECTURE.md (Sections 1–11) and
a README.md walkthrough from clean checkout to the sim demo.
```

```text
/ros2-robotics-architecture Audit QoS and TF ownership for the perception pipeline in src/perception.
Findings only, with file:line, effect and a ros2 command that verifies each.
```

## `docker-ros2-robotics-architecture`

```text
/docker-ros2-robotics-architecture Design a Bake + Compose layout with dev, sim and robot targets
for amd64 CI and an arm64 Jetson.
```

```text
/docker-ros2-robotics-architecture Audit privileges, devices, host networking and DDS discovery
in compose.yaml. Static review only.
```

## `robotics-web-architecture`

```text
/robotics-web-architecture Design a fleet console: live map, robot health, mission dispatch and
e-stop request. Separate read-only monitoring from command-capable modes.
```

```text
/robotics-web-architecture Audit server-side authorization for WebSocket subscriptions and
commands in services/robot-gateway. Cover stale commands, duplicate delivery and reconnect.
```

## `robotics-agentic-ai-architecture`

```text
/robotics-agentic-ai-architecture Design a mission agent that turns "restock aisle 4" into
typed robot tool calls, with operator approval, checkpoints and recovery after restart.
```

```text
/robotics-agentic-ai-architecture Compare a deterministic state machine baseline with our
LLM planner in src/orchestration. Where does model reasoning add value, and where must
authorization stay in code?
```

## `robotics-simulation-validation`

```text
/robotics-simulation-validation Build a smoke test and three regression scenarios for our
Isaac Sim warehouse scene. Pin seeds, timestep and pass thresholds with units.
```

```text
/robotics-simulation-validation Audit sim-to-real gaps between our Gazebo wheel model and the
recorded bag in data/bench_2026-10-02. Compare synchronised odometry and state the remaining gaps.
```

## `robot-learning`

```text
/robot-learning Design an imitation-learning pipeline from 200 teleop demos for pick-and-place:
dataset schema, episode splits by session, baseline, and evaluation protocol.
```

```text
/robot-learning Review train/eval/inference parity for policies/vla: preprocessing,
normalisation, action decoding and the 20 Hz inference deadline.
```
