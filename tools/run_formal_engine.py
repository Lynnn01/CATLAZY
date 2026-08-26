"""
Catlazy Formal Engine — CLI Entry Point
Runs any combination of the 4 DISMATH-backed verification modules.

Usage:
  python tools/run_formal_engine.py [--module 1,2,3,4|all] [--base HEAD] [paths...]

Examples:
  python tools/run_formal_engine.py --all
  python tools/run_formal_engine.py --module 1 src/
  python tools/run_formal_engine.py --module 1,4 --base main
  python tools/run_formal_engine.py --module 3 docs/plans/

Integrates with Catlazy Skills:
  catlazy3-architecture → --module 1   (Architecture Invariant)
  catlazy2-review       → --module 4   (Resolution Refutation)
  catlazy1-design       → --module 3   (Hoare Plan Validator)
  catlazy (after embed) → --module 2   (SAT Consistency)
  CI/CD pre-commit      → --module 1,4
"""

import argparse
import sys
from pathlib import Path

# Fix Windows console encoding cleanly
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Ensure tools/formal is importable
sys.path.insert(0, str(Path(__file__).parent / "formal"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Catlazy Formal Engine (DISMATH Automated Verification)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Run all verification modules (default)",
    )
    parser.add_argument(
        "--module", "-m",
        default="all",
        help="Comma-separated module numbers (1,2,3,4) or 'all' (default: all)",
    )
    parser.add_argument(
        "--base", "-b",
        default="HEAD",
        help="Git base ref for Module 4 diff (default: HEAD)",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="Paths to scan for Modules 1, 2, 3 (default: .)",
    )
    args = parser.parse_args()

    if args.all or args.module == "all":
        mods = ["1", "2", "3", "4"]
    else:
        mods = [m.strip() for m in args.module.split(",")]
    exit_codes: list[int] = []

    if "1" in mods:
        print("\n" + "=" * 60)
        print("Module 1: Architecture Invariant Checker")
        print("Theory: Predicate Logic Af.Ad (DISMATH Ch. 03, 04)")
        print("=" * 60)
        from invariant_checker import run as run1  # type: ignore
        exit_codes.append(run1(args.paths))

    if "2" in mods:
        print("\n" + "=" * 60)
        print("Module 2: Rule SAT Consistency Checker")
        print("Theory: Propositional SAT / CNF (DISMATH Ch. 01, 02, 10)")
        print("=" * 60)
        from rule_sat_consistency import run as run2  # type: ignore
        exit_codes.append(run2(args.paths if any(Path(p).is_file() for p in args.paths) else []))

    if "3" in mods:
        print("\n" + "=" * 60)
        print("Module 3: Hoare Triple Plan Validator")
        print("Theory: Program Correctness {P}S{Q} (DISMATH Ch. 08)")
        print("=" * 60)
        from hoare_plan_validator import run as run3  # type: ignore
        plan_paths = [p for p in args.paths if "plan" in p.lower() or p.endswith(".md")]
        exit_codes.append(run3(plan_paths))

    if "4" in mods:
        print("\n" + "=" * 60)
        print("Module 4: Resolution Refutation Reviewer")
        print("Theory: Resolution Rule / Theorem Proving (DISMATH Ch. 05, 10)")
        print("=" * 60)
        from resolution_reviewer import run as run4  # type: ignore
        exit_codes.append(run4([args.base]))

    overall = max(exit_codes) if exit_codes else 0
    print("\n" + "=" * 60)
    if overall == 0:
        print("[PASS] CATLAZY FORMAL ENGINE: All checks PASSED")
    else:
        print("[FAIL] CATLAZY FORMAL ENGINE: Verification FAILED")
    print("=" * 60)
    sys.exit(overall)


if __name__ == "__main__":
    main()
