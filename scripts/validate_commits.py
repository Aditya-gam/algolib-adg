#!/usr/bin/env python3
"""
Simple commit message validation script that checks against our commitlint rules.

This script validates commit messages without requiring external dependencies.
"""

import re
import sys
from typing import List, Tuple

# Rules from commitlint.config.mjs
VALID_TYPES = [
    "feat",
    "fix",
    "docs",
    "style",
    "refactor",
    "test",
    "chore",
    "perf",
    "ci",
    "build",
    "revert",
]

VALID_SCOPES = [
    "algorithms",
    "searching",
    "sorting",
    "graph",
    "dynamic-programming",
    "greedy",
    "backtracking",
    "math",
    "data-structures",
    "tree",
    "heap",
    "graph-ds",
    "linked-list",
    "stack",
    "queue",
    "trie",
    "ci",
    "cd",
    "docs",
    "tests",
    "benchmarks",
    "api",
    "db",
    "security",
    "performance",
    "core",
    "utils",
    "interfaces",
    "typing",
    "deps",
    "config",
    "scripts",
    "tools",
    "scaffolding",
    "property",
]

MAX_HEADER_LENGTH = 100
MAX_SUBJECT_LENGTH = 72
MAX_BODY_LINE_LENGTH = 300
MAX_FOOTER_LINE_LENGTH = 300


def _validate_header(header: str) -> Tuple[bool, List[str], Tuple[str, str, str]]:
    errors = []
    header_pattern = r"^(\w+)\(([^)]*)\):\s*(.+)$"
    match = re.match(header_pattern, header)
    if not match:
        errors.append("Invalid header format. Expected: type(scope): description")
        return False, errors, ("", "", "")
    commit_type, scope, subject = match.groups()
    if len(header) > MAX_HEADER_LENGTH:
        errors.append(f"Header line too long ({len(header)} > {MAX_HEADER_LENGTH})")
    if commit_type not in VALID_TYPES:
        errors.append(f"Invalid type '{commit_type}'. Valid types: {', '.join(VALID_TYPES)}")
    if commit_type != commit_type.lower():
        errors.append("Type must be lowercase")
    if scope and scope not in VALID_SCOPES:
        errors.append(f"Invalid scope '{scope}'. Valid scopes: {', '.join(VALID_SCOPES)}")
    if scope and scope != scope.lower():
        errors.append("Scope must be lowercase")
    if subject != subject.lower():
        print(f"  ⚠️  Warning: Subject should be lowercase: '{subject}'")
    if len(subject) > MAX_SUBJECT_LENGTH:
        errors.append(f"Subject too long ({len(subject)} > {MAX_SUBJECT_LENGTH})")
    if subject.endswith("."):
        errors.append("Subject should not end with a period")
    return len(errors) == 0, errors, (commit_type, scope, subject)


def _validate_body(body_lines: List[str]) -> List[str]:
    errors = []
    for i, line in enumerate(body_lines, 2):
        if len(line) > MAX_BODY_LINE_LENGTH:
            errors.append(f"Body line {i} too long ({len(line)} > {MAX_BODY_LINE_LENGTH})")
    return errors


def validate_commit_message(message: str) -> Tuple[bool, List[str]]:
    """Validate a commit message against our rules."""
    errors = []
    lines = message.strip().split("\n")
    if not lines:
        return False, ["Empty commit message"]
    header = lines[0]
    body_lines = lines[1:] if len(lines) > 1 else []
    header_ok, header_errors, _ = _validate_header(header)
    errors.extend(header_errors)
    errors.extend(_validate_body(body_lines))
    return len(errors) == 0, errors


def main() -> int:
    """Main function to validate commit messages."""
    test_messages = [
        """chore(deps): update development dependencies and format codebase

This commit prepares the project for the next phase of development by performing several maintenance tasks.

- Switched to the `feat/core-library` branch.
- Updated development dependencies `pytest-benchmark` and `hypothesis` to their latest minor versions.
- Formatted the entire codebase using Ruff to ensure consistent styling.
- Resolved all linting issues identified by Ruff to maintain code quality.""",
        """feat(scaffolding): Add core interfaces and directory structure

Introduces the foundational package structure and core algorithm interfaces, a key step in Phase 2 of the project.

This commit establishes the main directory hierarchy for different algorithm categories (basic, intermediate, advanced) and testing (unit, property). It also defines the fundamental , , and  protocols in , which will serve as the contracts for all future algorithm implementations.

Additionally, this commit includes several maintenance updates:
- Migrated  to the PEP 621 standard, resolving all All set! warnings.
- Fixed numerous pre-commit hook failures related to imports, typing, and formatting that arose from the interface changes.
- Cleaned up and consolidated abstract base classes for algorithms.""",
        """fix(ci): Resolve pytest collection warning

Updates the pytest configuration to prevent the test runner from inspecting the  directory.

The  class within this directory was being incorrectly collected by pytest because its name starts with 'Test', causing a . This has been resolved by adding  to the  setting in , which correctly instructs pytest to ignore this directory.""",
        """feat(core): major refactor and expansion of core algorithm/data-structure library

- Added: backtracking, dynamic programming, graph, greedy, math, searching, sorting algorithms, and corresponding tests/docs
- Added: AVL, BST, binary tree, heap, red-black tree, trie, and supporting data structures with full test coverage
- Refactored: moved each algorithm to its own file, updated imports, improved modularity and SOLID compliance
- Updated: CI, pre-commit config, pyproject, docs, and complexity cheatsheet
- Fixed: all lint, type, and test issues; ensured 95%+ coverage and pre-commit compliance
- Removed: legacy/duplicate files, consolidated test and doc structure

BREAKING CHANGE: Directory and import structure for algorithms and data structures has changed. See docs for migration details.""",
        """test(property): add property-based tests for core algorithms

This commit introduces a comprehensive suite of property-based tests using Hypothesis to validate the correctness and invariants of core algorithms and data structures.

- Added a `property` marker t""",
    ]

    print("Validating commit messages against our rules...")
    print("=" * 80)

    all_passed = True
    for i, message in enumerate(test_messages, 1):
        print(f"\n--- Test {i} ---")
        print("Message preview:")
        lines = message.split("\n")
        print(f"Subject: {lines[0]}")
        if len(lines) > 1:
            print(f"Body preview: {lines[1][:50]}...")

        passed, errors = validate_commit_message(message)
        if passed:
            print("✅ PASSED")
        else:
            print("❌ FAILED")
            print("Errors:")
            for error in errors:
                print(f"  - {error}")
            all_passed = False

    print("\n" + "=" * 80)
    if all_passed:
        print("🎉 All tests passed! Commitlint configuration should work correctly.")
    else:
        print("⚠️ Some tests failed. The commitlint configuration may need adjustment.")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
