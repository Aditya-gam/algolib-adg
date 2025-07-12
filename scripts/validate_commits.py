#!/usr/bin/env python3
"""
Script to validate commit messages against commitlint rules.

This script helps check if commit messages comply with the project's
commitlint configuration before pushing to avoid CI failures.
"""

import re
import subprocess
import sys
from typing import List, Tuple


def get_recent_commits(count: int = 10) -> List[Tuple[str, str]]:
    """Get recent commit hashes and messages."""
    try:
        result = subprocess.run(
            ["git", "log", "--format=%H %s", f"-{count}"],
            capture_output=True,
            text=True,
            check=True,
        )

        commits = []
        for line in result.stdout.strip().split("\n"):
            if line.strip():
                parts = line.split(" ", 1)
                if len(parts) == 2:
                    commits.append((parts[0], parts[1]))

        return commits
    except subprocess.CalledProcessError as e:
        print(f"Error getting commits: {e}")
        return []


def get_full_commit_message(commit_hash: str) -> str:
    """Get the full commit message for a given hash."""
    result = subprocess.run(
        ["git", "show", "--format=%B", "--no-patch", commit_hash],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


# Split out header, type, and scope validation into helper functions to reduce complexity


def _validate_header_format(header: str) -> Tuple[bool, List[str], Tuple[str, str, str]]:
    errors = []
    header_pattern = r"^(\w+)\(([^)]*)\):\s*(.+)$"
    match = re.match(header_pattern, header)
    if not match:
        errors.append("Invalid header format. Expected: type(scope): description")
        return False, errors, ("", "", "")
    return True, [], match.groups()


def _validate_type(commit_type: str) -> List[str]:
    valid_types = [
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
    errors = []
    if commit_type not in valid_types:
        errors.append(f"Invalid type '{commit_type}'. Valid types: {', '.join(valid_types)}")
    if commit_type != commit_type.lower():
        errors.append("Type must be lowercase")
    return errors


def _validate_scope(scope: str) -> List[str]:
    valid_scopes = [
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
        "runtime",
        "quality-gate",
    ]
    errors = []
    if scope and scope not in valid_scopes:
        errors.append(f"Invalid scope '{scope}'. Valid scopes: {', '.join(valid_scopes)}")
    if scope and scope != scope.lower():
        errors.append("Scope must be lowercase")
    return errors


def _validate_subject(subject: str) -> List[str]:
    errors = []
    if subject != subject.lower():
        errors.append("Subject must be lowercase")
    if len(subject) > 72:
        errors.append(f"Subject too long ({len(subject)} > 72)")
    if subject.endswith("."):
        errors.append("Subject should not end with a period")
    return errors


def validate_commit_message_locally(message: str) -> Tuple[bool, List[str]]:
    errors = []
    lines = message.strip().split("\n")
    if not lines:
        return False, ["Empty commit message"]
    header = lines[0]
    body_lines = lines[1:] if len(lines) > 1 else []
    header_ok, header_errors, (commit_type, scope, subject) = _validate_header_format(header)
    errors.extend(header_errors)
    if not header_ok:
        return False, errors
    errors.extend(_validate_type(commit_type))
    errors.extend(_validate_scope(scope))
    errors.extend(_validate_subject(subject))
    if len(header) > 100:
        errors.append(f"Header too long ({len(header)} > 100)")
    body_text = "\n".join(body_lines)
    if len(body_text) > 800:
        errors.append(f"Body too long ({len(body_text)} > 800)")
    for i, line in enumerate(body_lines, 2):
        if len(line) > 300:
            errors.append(f"Body line {i} too long ({len(line)} > 300)")
    return len(errors) == 0, errors


def main() -> None:
    """Main function to validate commit messages."""
    print("🔍 Commit Message Validator")
    print("=" * 50)

    # Get recent commits
    commits = get_recent_commits(10)

    if not commits:
        print("❌ No commits found!")
        sys.exit(1)

    print(f"Validating {len(commits)} recent commits...")
    print("=" * 50)

    all_valid = True
    invalid_commits = []

    for i, (hash_val, subject) in enumerate(commits, 1):
        print(f"\n--- Commit {i}: {hash_val[:8]} ---")
        print(f"Subject: {subject}")

        try:
            full_message = get_full_commit_message(hash_val)
            is_valid, errors = validate_commit_message_locally(full_message)

            if is_valid:
                print("✅ Valid")
            else:
                print("❌ Invalid")
                for error in errors:
                    print(f"  - {error}")
                invalid_commits.append((hash_val, subject, errors))
                all_valid = False

        except subprocess.CalledProcessError as e:
            print(f"❌ Error reading commit: {e}")
            all_valid = False

    print("\n" + "=" * 50)

    if all_valid:
        print("🎉 All commits are valid!")
        sys.exit(0)
    else:
        print(f"❌ Found {len(invalid_commits)} invalid commits:")
        print("=" * 50)

        for hash_val, subject, errors in invalid_commits:
            print(f"\nCommit: {hash_val[:8]}")
            print(f"Subject: {subject}")
            print("Errors:")
            for error in errors:
                print(f"  - {error}")

        print("\n" + "=" * 50)
        print("🔧 To fix these commits:")
        print("1. Use: python scripts/fix_ci_commits.py")
        print("2. Follow the provided instructions")
        print("3. Re-run this validation script")

        sys.exit(1)


if __name__ == "__main__":
    main()
