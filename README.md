<div align="center">
  <h1>🐈 Catlazy Agent Architecture</h1>
  <p><strong>The Lazy Senior Dev Philosophy for AI Agents</strong></p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![AI: Antigravity](https://img.shields.io/badge/AI_Agent-Antigravity-blue.svg)]()
  [![Paradigm: Lazy](https://img.shields.io/badge/Paradigm-YAGNI-success.svg)]()
</div>

---

**Catlazy** is a ready-to-use plugin of architecture, rules, and skills for AI agents such as Antigravity. Its goal is to teach agents **creative laziness**: solve the requested problem directly, avoid redundant work and over-engineering, and use tokens and other resources deliberately.

---

## 🌟 Why Catlazy? (Concept and Philosophy)

AI agents often work too hard in the wrong direction: they write speculative code, build layers of abstraction, or add external libraries when a native solution would be enough.

The **Catlazy framework** counters that behavior with three principles:

- **YAGNI (You Aren’t Gonna Need It):** build only what today’s requirement needs.
- **Deletion before addition:** look for code that can be removed before writing more code.
- **Native over external:** prefer standard-library and built-in capabilities over unnecessary dependencies.

---

## ✨ Key Features

1. **🛡️ Automated guardrails:** control agent behavior through `.rules/AGENTS.md`.
2. **🗜️ Context compression:** optionally use the **Headroom Proxy** to compress LLM API traffic that is configured to pass through it.
3. **🔍 Focused audits:** inspect architecture, UI, UX, complexity, technical debt, and agent rules against focused standards.
4. **🛣️ SDLC workflow:** use skills ordered from 0–9 to guide real development work.

---

## 🗂️ Project Structure

The project is intentionally small. Its important directories are:

```text
├── .rules/              # Agent rules
│   └── AGENTS.md        # Operating instructions for the AI
├── docs/                # Architecture and design standards
│   ├── architecture/    # Clean Architecture and DDD guidance
│   └── design/          # Unified UI/UX design guidance
│       ├── user_experience/
│       └── user_interface/
├── skills/              # Eleven skills (the core skill plus 0–9)
│   ├── catlazy/         # Configure the Catlazy intensity
│   ├── catlazy0-help/   # Help and command reference
│   └── catlazy9-compress/
└── plugin.json          # Plugin configuration for the AI host
```

After updating the plugin, reload or reinstall it using your AI host’s process so the host-loaded skills match the repository version.

---

## 🛠️ Catlazy Skills Workflow (Commands 0–9)

The skills are ordered along a practical software-development lifecycle:

| Step | Command | Purpose |
|:---:|---|---|
| **—** | `/catlazy` | **Configure:** change the main intensity (`lite`, `full`, `ultra`, or `off`). |
| **0** | `/catlazy0-help` | **Guide:** show Catlazy commands and operating rules. |
| **1** | `/catlazy1-design` | **Plan:** run a short three-step brainstorm before implementation. |
| **2** | `/catlazy2-review` | **During work:** review the latest Git diff for over-engineering and rule violations. |
| **3** | `/catlazy3-architecture` | **Focused audit:** check the repository against `docs/architecture/`. |
| **4** | `/catlazy4-interface` | **Focused audit:** check UI against the design tokens and interface rules. |
| **5** | `/catlazy5-experience` | **Focused audit:** check UX, progressive disclosure, and feedback. |
| **6** | `/catlazy6-audit` | **Repository audit:** find dead code, duplication, and candidates for deletion or consolidation. |
| **7** | `/catlazy7-debt` | **Debt management:** collect small intentional technical-debt markers (`catlazy:`). |
| **8** | `/catlazy8-agent` | **System care:** review and simplify the agent rules themselves. |
| **9** | `/catlazy9-compress` | **Resource saving:** assess or configure optional Headroom compression. |

You can type `/catlazy`, `/catlazy off`, or `/catlazy ultra` at any time to change the main operating mode. `lite` reviews the final diff and states missing checks; `full` adds approved scope, current validation evidence, and a finish status; `ultra` adds hollow review and critical negative-path validation. Fault probes remain optional and must be approved and isolated from a live dirty worktree.

### Task-scoped reviews

Use Catlazy reviews with an explicit task context when the worktree is dirty:

```text
/catlazy2-review report --scope ui --base origin/main --files src/features/screener
/catlazy2-review fix-safe --scope ui --files src/features/screener --format normal
```

`report` only reports findings. `fix-safe` may repair small, local, low-risk findings in the selected files and then reviews them again. It never auto-changes migrations, dependencies, generated files, authentication, public contracts, or files outside scope.

For a task that spans several messages, copy `.catlazy/task.json.example` to `.catlazy/task.json` and set its baseline, scope, files, report format, and validation profile. After user approval, `files` is the approved write scope: Catlazy may read elsewhere for discovery, but it stops and asks before writing another path. The manifest is optional and must not turn unrelated dirty worktree files into task output.

Validation profiles are selected from the task context after Catlazy discovers the project’s real scripts: `ui` runs relevant typecheck and lint, `backend` adds tests and build, `api` adds contract/type checks, and `full` runs all applicable checks. Catlazy reports missing scripts instead of guessing commands.

The optional `evidence` array keeps short validation records using `profile`, `command`, `exitStatus`, and ISO-8601 `ranAt`. Evidence is current only when it was recorded after the last relevant edit; later changes require rerunning only the affected profile.

### Catlazy finish contract

Before reporting completion, Catlazy checks the approved scope, applicable validation, evidence freshness, final diff, generated files, and unresolved P1/P2 findings:

```text
🐈 Scope       PASS
🐈 Validation  PASS
🐈 Freshness   PASS
🐈 Diff        PASS
🐈 Generated   PASS
🐈 P1/P2       PASS
CATLAZY_DONE
```

If an external dependency or decision prevents completion, it reports `CATLAZY_BLOCKED: <reason>`. If required evidence is missing, stale, unavailable, or failing, it reports `CATLAZY_UNVERIFIED: <missing check>`. Catlazy rules and skills are workflow guardrails, not filesystem enforcement, so the final diff remains the source of truth for scope.

In `ultra`, `catlazy2-review` also checks for completion-shaped placeholders such as required `TODO` markers, empty handlers, fake success responses, inactive UI controls, meaningless skipped tests, and production mock data. Optional fault probes are reserved for critical calculations, financial logic, authorization, parsers, validators, and regression fixes.

---

## 🔁 Incremental Decision Trail

For complex, ambiguous, or multi-file work, Catlazy proceeds one issue at a time: **Observe → Decide → Plan → Apply → Verify → Continue**. It shows concise evidence and decisions without requesting or revealing private chain-of-thought.

Small, clear work uses only **Plan → Apply → Verify** so the process does not add unnecessary overhead.

---

## 🚀 Quick Start

### 1. Prerequisite

Use an AI agent framework such as Antigravity that supports a plugin or skills directory.

### 2. Optional Headroom Proxy

Install Docker only if you choose to use this proxy. It compresses only LLM API traffic configured to route through it:

```bash
# Port 8787 accepts requests from your configured client.
docker run -p 8787:8787 ghcr.io/chopratejas/headroom
```

On Windows, you can double-click the included `run-headroom.bat`.

### 3. Environment Variables

If you choose the proxy, copy `.env.example` to `.env` and provide your API keys:

```bash
cp .env.example .env
```

The example routes `OPENAI_BASE_URL` or `ANTHROPIC_BASE_URL` to `http://localhost:8787`. Only clients configured with those variables send traffic through the proxy; no application code needs to change.

---

## 💡 Usage Examples

**Example 1: Before a large feature**

> **User:** `/catlazy1-design` I need a shopping cart with Redis.
>
> **Agent:** “Do we need Redis today? Could a simple in-memory store or session meet the current requirement with less complexity?”

**Example 2: Architecture check**

> **User:** `/catlazy3-architecture` Please check the project.
>
> **Agent:** “Found `[arch-bypass]` in `CartController.ts`: it calls the database directly instead of going through the Application Layer use case.”

**Example 3: UX check**

> **User:** `/catlazy5-experience`
>
> **Agent:** “Found `[ux-silent]` in `Login.tsx`: the submit button has no loading state, so users may submit twice.”

---

<div align="center">
  <p><i>More laziness, shorter code, fewer bugs. 🐈💤</i></p>
</div>
