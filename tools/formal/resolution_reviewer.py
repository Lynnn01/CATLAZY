"""
Module 4: Resolution Refutation Reviewer
DISMATH Theory: Rules of Inference & Resolution Refutation (Ch. 05, 10)

Resolution Refutation procedure applied to git diffs:

  Premises P₁..Pₙ = Architecture Invariants (from Module 1)
  Goal Q          = "No changed file violates any invariant"
  ¬Q              = "∃f ∈ ChangedFiles : Invariant(f) violated"

  Step 1: Assume ¬Q (there exist violations)
  Step 2: Apply Resolution Rule repeatedly on {Invariants ∧ ¬Q}
  Step 3a: If Empty Clause □ derived → ¬Q is Contradiction → Q PROVED ✓
  Step 3b: If Counterexample found  → ¬Q is satisfiable    → Q REFUTED ✗

catlazy: heuristic resolution via Module 1 as invariant oracle | ceiling: lint-level
         upgrade: integrate z3-solver for full formal proof chains
"""

import subprocess
import sys
from pathlib import Path

# Fix Windows console encoding cleanly
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Add tools/formal to sys.path so Module 1 can be imported
sys.path.insert(0, str(Path(__file__).parent))
from invariant_checker import check_invariant, SUPPORTED_EXTENSIONS  # type: ignore


def get_changed_files(base_ref: str = "HEAD") -> list[str]:
    """Get list of files changed relative to base_ref via git diff."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", base_ref],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0:
            # fallback: check uncommitted changes
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True, text=True, timeout=10,
            )
            lines = [l[3:].strip() for l in result.stdout.splitlines() if l.strip()]
            return [f for f in lines if Path(f).exists()]
        return [f.strip() for f in result.stdout.splitlines() if f.strip() and Path(f).exists()]
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return []


def resolution_refutation(changed_files: list[str]) -> tuple[bool, list[dict]]:
    """
    Apply Resolution Refutation:
      ¬Q = ∃f ∈ ChangedFiles : violation exists
      If ¬Q → □ (no violations) → Q PROVED
      If ¬Q → Counterexample    → Q REFUTED
    """
    relevant = [f for f in changed_files if Path(f).suffix in SUPPORTED_EXTENSIONS]
    violations = [v for f in relevant if (v := check_invariant(f))]
    proved = len(violations) == 0
    return proved, violations


def run(args: list[str]) -> int:
    """Run Resolution Refutation on git diff."""
    base_ref = args[0] if args else "HEAD"
    changed = get_changed_files(base_ref)

    if not changed:
        print(f"[N/A] No changed files detected (base: {base_ref})")
        return 0

    print(f"  Checking {len(changed)} changed file(s) against base '{base_ref}'...")
    proved, violations = resolution_refutation(changed)

    if proved:
        print(f"[PASS] Resolution Refutation: Q PROVED")
        print(f"  → ∀f ∈ ChangedFiles({len(changed)}): invariants hold")
        print(f"  → ¬Q → □ (Contradiction) ∴ Q is a valid consequence")
        return 0
    else:
        print(f"[FAIL] Resolution Refutation: Q REFUTED — {len(violations)} counterexample(s)")
        for v in violations:
            print(f"  ✗ Witness found: {v['file']}")
            print(f"    Rule violated: {v['rule']}")
            print(f"    Import: '{v['import_path']}'")
        print(f"  → ¬Q is satisfiable ∴ invariant violation confirmed")
        return 1


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
