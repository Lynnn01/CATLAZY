# Cross-Platform Catlazy Embedding & Rule Persistence

## Goal

Enable `/catlazy` to automatically embed and persist Catlazy as the mandatory default workflow across multiple AI coding assistants and environments (Google Antigravity, Anthropic Claude, OpenAI Codex, Cursor IDE, Windsurf, GitHub Copilot).

## Affected files

- `skills/catlazy/SKILL.md`
- `.rules/AGENTS.md`
- `docs/plans/2026-08-22-cross-platform-catlazy-embedding.md`

## Cross-Platform Embedding Protocol

When `/catlazy` is invoked with `--embed [global|project|all]` or when requested to persist globally, detect the active AI host environment and embed the following standard Catlazy rule snippet:

### Standard Catlazy Rule Snippet
```markdown
<!-- CATLAZY_EMBED_START -->
# Catlazy Mode (Lazy Senior Dev)
- Always operate under CATLAZY [full] mode by default.
- Apply the Ladder of Laziness before writing code: YAGNI -> Reuse -> Stdlib -> Native -> Dependency -> One-line -> Minimum.
- Read before writing. Never guess execution flows or prop contracts.
- Lazy, not negligent: Preserve security, data-loss handling, accessibility, and UX feedback.
- Adhere strictly to .rules/AGENTS.md and universal 3-section output reporting.
<!-- CATLAZY_EMBED_END -->
```

### Platform Target Matrix

1. **Google Antigravity:**
   - Project: `.rules/AGENTS.md`
   - Global: `~/.gemini/antigravity/rules/user_global.md`
2. **Anthropic Claude (Code / Desktop):**
   - Project: `CLAUDE.md` (root)
   - Global: `~/.claude/CLAUDE.md` or `~/.claude.json`
3. **OpenAI Codex / ChatGPT:**
   - Project: `AGENTS.md` or `.codex/instructions.md`
   - Global: Custom Instructions / Assistant System Prompt
4. **Cursor IDE:**
   - Project: `.cursorrules` or `.cursor/rules/catlazy.mdc`
   - Global: Cursor Settings > Rules for AI
5. **Windsurf (Codeium Cascade):**
   - Project: `.windsurfrules`
   - Global: Cascade Global Rules
6. **GitHub Copilot:**
   - Project: `.github/copilot-instructions.md`

## Verification

- Inspect `skills/catlazy/SKILL.md` to ensure the protocol and output schema are complete.
- Verify sync to host plugin.
