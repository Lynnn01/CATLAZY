---
name: catlazy10-loop
description: Force the agent to continuously execute a task until validated multiple times without findings
---

# Catlazy Continuous Loop Mode

Activate continuous execution mode for a specific task.

**Usage:** `/catlazy10-loop [task] [counter]`
* `[task]`: The objective or task the agent must complete.
* `[counter]`: The number of consecutive clean iterations required before reporting completion (Default: 3).

## 🔄 Core Loop Logic

When this skill is invoked, you **MUST** follow this strict state machine:

1. **Initialization:**
   - Set `CURRENT_COUNTER = 0`.
   - Set `TARGET_COUNTER = [counter]` (default is 3 if not provided).

2. **Action Phase (Fresh Look):**
   - You must treat each iteration as a fresh attempt. "Forget" that you just checked this; assume there is still hidden work, edge cases, or bugs related to `[task]`.
   - Execute the necessary discovery, audits, edits, or tests required to fulfill the `[task]`.

3. **Evaluation Phase:**
   - **Condition A (Work Found/Changes Made):** If you found a bug, wrote code, edited a file, or performed any constructive action towards the `[task]`, you MUST reset the counter: `CURRENT_COUNTER = 0`. Go back to Step 2.
   - **Condition B (No Work Found/Nothing Left To Do):** If you genuinely searched and found absolutely nothing left to do to satisfy `[task]`, you must increment the counter: `CURRENT_COUNTER = CURRENT_COUNTER + 1`.

4. **Completion Check:**
   - If `CURRENT_COUNTER < TARGET_COUNTER`: Do **NOT** report `CATLAZY_DONE`. Go back to Step 2 and try again from a different angle or deeper inspection.
   - If `CURRENT_COUNTER >= TARGET_COUNTER`: You have successfully proven stability. You may report `CATLAZY_DONE` and present your final findings to the user.

### 📐 Formal Basis (DISMATH Reasoning Foundation)

Loop execution and stability proofs are formally grounded in:
- **Ch. 07 (Mathematical Induction & Loop Invariants):** Loop termination is guaranteed by the Well-Ordering Property. The Loop Variant function $V = \text{TARGET\_COUNTER} - \text{CURRENT\_COUNTER} \ge 0$ strictly decreases toward 0 upon successive stable states. Reference: [`docs/logics/dismath/07-mathematical-induction-and-recursion.md`](../../docs/logics/dismath/07-mathematical-induction-and-recursion.md).
- **Ch. 08 (Hoare Logic Loop Correctness):** The invariant $\{I: \text{TaskInvariantsSatisfied} \land 0 \le \text{CURRENT\_COUNTER} \le \text{TARGET\_COUNTER}\}$ is maintained across every iteration. Reference: [`docs/logics/dismath/08-program-correctness-and-hoare-logic.md`](../../docs/logics/dismath/08-program-correctness-and-hoare-logic.md).

## 🛑 Rules
- **Do not fake the counter:** You cannot just print "Counter is 3, I am done." You must actually stop your tool calls, evaluate, and explicitly track the counter in your internal thoughts or concise status updates.
- **Continuous Loop:** You must not stop and wait for user input during the loop unless you are completely blocked by an external factor (e.g. `CATLAZY_BLOCKED`). Keep making tool calls and investigating until `TARGET_COUNTER` is reached.
