"""
Module 3: Hoare Triple Plan Validator
DISMATH Theory: Program Correctness & Hoare Logic (Ch. 08)

Every plan file in docs/plans/ must exhibit { P } S { Q } structure:
  {P} Pre-condition  = Goal + Affected Files (state before change)
  {S} Statement      = Core Code Snippets or Diffs (the change itself)
  {Q} Post-condition = Verification Plan + Rollback strategy (guaranteed after)

Missing any section means the plan is formally incomplete.
"""

import re
import sys
from pathlib import Path

# Fix Windows console encoding cleanly
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# {P} S {Q} — each section requires at least one pattern to match
HOARE_SECTIONS: dict[str, dict] = {
    "Pre-condition {P}": {
        "patterns": [
            r"##+\s*(?:\d+[\.\)]\s*)?(?:goal|pre.?condition|affected\s+files|context|background|source\s+of\s+truth)",
            r"\*\*(?:goal|pre.?condition)\*\*",
        ],
        "description": "Goal / Pre-condition / Affected Files section must be present",
    },
    "Statement {S}": {
        "patterns": [
            r"##+\s*(?:\d+[\.\)]\s*)?(?:proposed\s+changes|implementation|core.*|design|changes|statement)",
            r"```[a-z0-9_-]*\n",         # at least one code block
            r"```[a-z0-9_-]*\r\n",
        ],
        "description": "Code snippet, proposed changes, or core implementation block must be present",
    },
    "Post-condition {Q}": {
        "patterns": [
            r"##+\s*(?:\d+[\.\)]\s*)?(?:verification|post.?condition|rollback|revert|validation|decision\s+trail)",
            r"-\s+(?:plan\s+&\s+apply|verify|verification|validation):",
            r"\b(?:verify|verification|validation)\b.*(?:rule|plan|standard|file|source)",
            r"CATLAZY_DONE",
            r"CATLAZY_UNVERIFIED",
            r"CATLAZY_BLOCKED",
        ],
        "description": "Verification plan, decision trail, or terminal status must be present",
    },
}

DEFAULT_PLAN_DIR = "docs/plans"


def validate_plan(filepath: str) -> list[str]:
    """
    Validate {P} S {Q} structure of a plan file.
    Returns list of missing sections (empty = PASS).
    """
    content = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    missing: list[str] = []
    for section_name, spec in HOARE_SECTIONS.items():
        found = any(
            re.search(p, content, re.IGNORECASE | re.MULTILINE)
            for p in spec["patterns"]
        )
        if not found:
            missing.append(f"  ✗ [{section_name}] {spec['description']}")
    return missing


def run(plan_paths: list[str]) -> int:
    """Validate Hoare Triple structure in plan files."""
    if plan_paths:
        paths = [Path(p) for p in plan_paths if Path(p).exists()]
    else:
        plan_dir = Path(DEFAULT_PLAN_DIR)
        paths = list(plan_dir.glob("*.md")) if plan_dir.exists() else []

    if not paths:
        print(f"[N/A] No plan files found (looked in: {DEFAULT_PLAN_DIR})")
        return 0

    total_fail = 0
    for plan in sorted(paths):
        missing = validate_plan(str(plan))
        if missing:
            print(f"[FAIL] {plan.name} — Incomplete Hoare Triple {{P}} S {{Q}}:")
            print("\n".join(missing))
            total_fail += 1
        else:
            print(f"[PASS] {plan.name} — {{P}} S {{Q}} structure verified")

    if total_fail:
        print(f"\n  → {total_fail}/{len(paths)} plan(s) incomplete")
    else:
        print(f"\n  → All {len(paths)} plan(s) structurally valid")

    return 1 if total_fail else 0


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
