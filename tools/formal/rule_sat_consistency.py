"""
Module 2: Cross-Platform Rule SAT Consistency Checker
DISMATH Theory: Propositional Logic & SAT Modeling (Ch. 01, 02, 10)

Model:
  φ = R₁ ∧ R₂ ∧ ... ∧ Rₙ  (conjunction of all rules across all platforms)
  Satisfiable(φ) = T → all rules consistent ✓
  Satisfiable(φ) = F → Contradiction detected → [FAIL]

Each CONTRADICTION_PAIR represents a clause pair (A ∧ B) that is logically
unsatisfiable — i.e., no assignment can make both true simultaneously.
"""

import re
import sys
from pathlib import Path

# Fix Windows console encoding cleanly
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Each tuple: (pattern_A_regex, pattern_B_regex, human_readable_description)
# If both A and B match in the combined rule corpus → CONTRADICTION (φ unsatisfiable)
CONTRADICTION_PAIRS: list[tuple[str, str, str]] = [
    (
        r"always operate.*\[full\]|default.*\[full\]",
        r"disable.*catlazy|catlazy.*off|turn off.*catlazy",
        "Mode conflict: [full] mode required vs Catlazy disabled",
    ),
    (
        r"wait for.*approval before.*edit|never.*edit.*without.*approval",
        r"^\s*[-*]\s+(?!.*\b(?:do not|never|not|don't)\b).*\bauto.?fix\b",
        "Approval gate conflict: manual approval required vs unconditional auto-fix enabled",
    ),
    (
        r"respond in.*user.*language|use.*user.s language",
        r"english only|respond.*only in english|always.*respond.*english",
        "Language policy conflict: user language vs English-only",
    ),
    (
        r"one question per message|ask only one question",
        r"ask.*multiple question|several question.*at once",
        "Questioning style conflict: one-at-a-time vs multiple questions",
    ),
    (
        r"shared.*never import.*feature|shared.*must not import.*feature",
        r"shared.*may import.*feature|shared.*can use.*feature",
        "Shared module boundary conflict: zero inward leakage vs allowed",
    ),
    (
        r"do not create.*plan|skip.*planning gate",
        r"always create.*plan|planning gate.*required|never.*edit.*without.*plan",
        "Planning gate conflict: skip plan vs always plan required",
    ),
]

DEFAULT_RULE_FILES = [
    ".rules/AGENTS.md",
    "AGENTS.md",
    "CLAUDE.md",
    ".cursorrules",
    ".windsurfrules",
    ".cursor/rules/catlazy.mdc",
    ".github/copilot-instructions.md",
]


def load_rule_files(rule_files: list[str]) -> dict[str, str]:
    """Load content of each rule file that exists."""
    return {
        f: Path(f).read_text(encoding="utf-8", errors="ignore")
        for f in rule_files
        if Path(f).exists()
    }


def check_consistency(rule_contents: dict[str, str]) -> list[dict]:
    """
    Check satisfiability of φ = ∧Rᵢ by detecting CONTRADICTION_PAIRS.
    Returns list of conflict dicts if φ is unsatisfiable.
    """
    conflicts: list[dict] = []
    for pat_a, pat_b, description in CONTRADICTION_PAIRS:
        hits_a: list[tuple[str, str]] = []
        hits_b: list[tuple[str, str]] = []
        for filepath, content in rule_contents.items():
            for line in content.splitlines():
                stripped = line.strip()
                if stripped and re.search(pat_a, stripped, re.IGNORECASE):
                    hits_a.append((filepath, stripped))
                if stripped and re.search(pat_b, stripped, re.IGNORECASE):
                    hits_b.append((filepath, stripped))
        if hits_a and hits_b:
            conflicts.append({
                "description": description,
                "clause_A": hits_a[0],
                "clause_B": hits_b[0],
                "logical_form": f"A ∧ B = CONTRADICTION (φ unsatisfiable)",
            })
    return conflicts


def run(rule_files: list[str]) -> int:
    """Run SAT consistency check over rule files."""
    targets = rule_files if rule_files else DEFAULT_RULE_FILES
    contents = load_rule_files(targets)

    if not contents:
        print(f"[N/A] No rule files found at: {targets}")
        return 0

    conflicts = check_consistency(contents)
    if conflicts:
        print(f"[FAIL] φ UNSATISFIABLE — {len(conflicts)} contradiction(s) across {len(contents)} file(s):")
        for c in conflicts:
            print(f"\n  ⚡ {c['description']}")
            print(f"     Clause A → [{c['clause_A'][0]}]")
            print(f"       \"{c['clause_A'][1][:100]}\"")
            print(f"     Clause B → [{c['clause_B'][0]}]")
            print(f"       \"{c['clause_B'][1][:100]}\"")
            print(f"     {c['logical_form']}")
        return 1

    print(f"[PASS] φ SATISFIABLE — {len(contents)} rule file(s) are consistent")
    for f in contents:
        print(f"  ✓ {f}")
    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
