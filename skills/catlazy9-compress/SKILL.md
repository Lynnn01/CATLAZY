---
name: catlazy9-compress
description: Assess or configure optional Headroom context compression
---
# Catlazy Compression (Headroom)

Use this skill when large logs, JSON, or LLM API traffic may exceed a useful context budget.

### ⚙️ Workflow

1. Determine whether compression is needed; do not compress small or already readable output.
2. Prefer bounded inspection and targeted summaries before adding a proxy.
3. If the user chooses Headroom, verify Docker availability and route only explicitly configured API traffic through `http://localhost:8787`.
4. Never assume tool output was compressed and never expose or rewrite API keys.
5. Verify that compressed output preserves errors, identifiers, ordering, and actionable details.

Headroom is optional. The skill does not modify application code or environment secrets without explicit approval.
