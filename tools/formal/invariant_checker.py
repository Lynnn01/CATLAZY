"""
Module 1: Architecture Layer Invariant Checker
DISMATH Theory: Predicate Logic & Nested Quantifiers (Ch. 03, 04)

Formal Invariants enforced:
  ∀f ∈ DomainLayer,     ∀d ∈ Imports(f) : d ∉ (Infrastructure ∪ Presentation)
  ∀f ∈ ApplicationLayer, ∀d ∈ Imports(f) : d ∉ (Infrastructure ∪ Presentation)
  ∀s ∈ SharedModules,   ∀d ∈ Imports(s) : d ∉ Features  (Zero Inward Leakage)
"""

import re
import sys
from pathlib import Path

# Fix Windows console encoding cleanly
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Layer classification keywords (path-segment based)
LAYER_PATTERNS: dict[str, list[str]] = {
    "domain":   ["domain", "entities", "value-objects", "value_objects", "aggregates"],
    "app":      ["application", "use-cases", "usecases", "use_cases"],
    "infra":    ["infrastructure", "infra", "persistence", "adapters"],
    "pres":     ["presentation", "controllers", "resolvers", "http"],
    "shared":   ["shared", "core"],
    "features": ["features"],
}

# ∀f ∈ <layer> → ∀d ∈ Imports(f) : d ∉ <forbidden layers>
FORBIDDEN_IMPORTS: dict[str, list[str]] = {
    "domain": ["infra", "pres"],
    "app":    ["infra", "pres"],
    "shared": ["features"],
}

SUPPORTED_EXTENSIONS = (".py", ".ts", ".js", ".tsx", ".jsx")


def classify_file(filepath: str) -> str | None:
    """Universal Instantiation: determine layer c from ∀x Layer(x)."""
    parts = [p.lower() for p in Path(filepath).parts]
    for layer, keywords in LAYER_PATTERNS.items():
        if any(kw in part for part in parts for kw in keywords):
            return layer
    return None


def extract_imports(filepath: str) -> list[str]:
    """Extract import paths from Python/TS/JS files."""
    content = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    # Python: from x import y | import x
    py = re.findall(r"^(?:from|import)\s+([\w./]+)", content, re.MULTILINE)
    # TS/JS: import ... from '...' | require('...')
    ts = re.findall(r'from\s+[\'"]([^\'"]+)[\'"]', content)
    req = re.findall(r'require\([\'"]([^\'"]+)[\'"]\)', content)
    return py + ts + req


def check_invariant(filepath: str) -> dict | None:
    """
    Check: ∀f ∈ Layer(file), ∀d ∈ Imports(f) : d ∉ ForbiddenLayers(layer)
    Returns a Counterexample dict if violated, None if invariant holds.
    """
    file_layer = classify_file(filepath)
    if not file_layer or file_layer not in FORBIDDEN_IMPORTS:
        return None

    for imp in extract_imports(filepath):
        imp_lower = imp.lower()
        for forbidden in FORBIDDEN_IMPORTS[file_layer]:
            if any(kw in imp_lower for kw in LAYER_PATTERNS[forbidden]):
                return {
                    "file": filepath,
                    "file_layer": file_layer,
                    "import_path": imp,
                    "violation": f"imports from '{forbidden}' layer",
                    "rule": f"∀f ∈ {file_layer}, d ∉ {forbidden}",
                }
    return None


def run(paths: list[str]) -> int:
    """Scan paths for architecture invariant violations."""
    violations: list[dict] = []
    checked = 0
    for path in paths:
        p = Path(path)
        files = p.rglob("*") if p.is_dir() else [p]
        for f in files:
            if f.suffix in SUPPORTED_EXTENSIONS:
                checked += 1
                result = check_invariant(str(f))
                if result:
                    violations.append(result)

    if violations:
        print(f"[FAIL] {len(violations)} architecture invariant violation(s) in {checked} file(s):")
        for v in violations:
            print(f"  ✗ [{v['file_layer'].upper()}] {v['file']}")
            print(f"    Rule: {v['rule']}")
            print(f"    Import: '{v['import_path']}'")
        return 1

    print(f"[PASS] All architecture invariants satisfied ({checked} file(s) scanned)")
    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:] or ["."]))
