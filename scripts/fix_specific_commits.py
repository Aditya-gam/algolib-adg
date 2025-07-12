#!/usr/bin/env python3
"""
Script to fix specific commit messages that are failing CI validation.

This script targets the specific commits mentioned in the CI error:
- feat(scaffolding): Add core interfaces and directory structure
- fix(ci): Resolve pytest collection warning
- test(property): add property-based tests for core algorithms
- feat(runtime): add runtime checks and property-based tests
- feat(benchmarks): add detailed benchmark harness for merge, quick, heap sort and Dijkstra
- feat(ci): implement CI & pre-commit pipeline updates
- ci(quality-gate): enforce ruff F401, pre-commit in CI, and 95% coverage gate
"""

import re
import subprocess
from typing import Tuple


def get_commit_by_subject(subject_pattern: str) -> Tuple[str, str]:
    """Get commit hash and full message by subject pattern."""
    result = subprocess.run(
        ["git", "log", "--format=%H %s", "--grep", subject_pattern, "-1"],
        capture_output=True,
        text=True,
        check=True,
    )

    if not result.stdout.strip():
        return None, None

    parts = result.stdout.strip().split(" ", 1)
    if len(parts) == 2:
        commit_hash = parts[0]
        full_message = get_full_commit_message(commit_hash)
        return commit_hash, full_message

    return None, None


def get_full_commit_message(commit_hash: str) -> str:
    """Get the full commit message for a given hash."""
    result = subprocess.run(
        ["git", "show", "--format=%B", "--no-patch", commit_hash],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def truncate_body(body: str, max_length: int = 800) -> str:
    """Truncate body to fit within max_length while preserving structure."""
    if len(body) <= max_length:
        return body

    # Try to truncate at sentence boundaries
    sentences = body.split(". ")
    truncated = ""
    for sentence in sentences:
        if len(truncated + sentence + ". ") <= max_length - 3:  # Leave room for "..."
            truncated += sentence + ". "
        else:
            break

    if truncated:
        return truncated.rstrip() + "..."

    # If no sentence fits, truncate at word boundaries
    words = body.split()
    truncated = ""
    for word in words:
        if len(truncated + word + " ") <= max_length - 3:
            truncated += word + " "
        else:
            break

    return truncated.rstrip() + "..."


def fix_commit_message(message: str) -> str:
    """Fix a commit message to comply with commitlint rules."""
    lines = message.strip().split("\n")
    if not lines:
        return message

    header = lines[0]
    body_lines = lines[1:] if len(lines) > 1 else []

    header_pattern = r"^(\w+)\(([^)]*)\):\s*(.+)$"
    match = re.match(header_pattern, header)

    if match:
        commit_type, scope, subject = match.groups()

        # Map scopes to valid ones
        scope_mapping = {
            "scaffolding": "core",
            "property": "tests",
            "runtime": "core",
            "benchmarks": "benchmarks",
            "ci": "ci",
            "quality-gate": "ci",
        }

        fixed_scope = scope_mapping.get(scope, "core")
        fixed_subject = subject.lower()
        fixed_header = f"{commit_type}({fixed_scope}): {fixed_subject}"
    else:
        fixed_header = header.lower()

    # Process body lines
    body_text = "\n".join(body_lines)

    # Truncate body if too long
    if len(body_text) > 800:
        body_text = truncate_body(body_text, 800)

    # Build result
    result_lines = [fixed_header]
    if body_text.strip():
        result_lines.append("")
        result_lines.append(body_text)

    return "\n".join(result_lines)


def main() -> None:
    """Main function to fix specific commit messages."""
    print("🔧 Specific Commit Message Fixer")
    print("=" * 50)

    # Define the problematic commits and their patterns
    problematic_commits = [
        "feat(scaffolding): Add core interfaces and directory structure",
        "fix(ci): Resolve pytest collection warning",
        "test(property): add property-based tests for core algorithms",
        "feat(runtime): add runtime checks and property-based tests",
        "feat(benchmarks): add detailed benchmark harness for merge, quick, heap sort and Dijkstra",
        "feat(ci): implement CI & pre-commit pipeline updates",
        "ci(quality-gate): enforce ruff F401, pre-commit in CI, and 95% coverage gate",
    ]

    print("Fixing the following problematic commits:")
    print("=" * 50)

    for i, subject_pattern in enumerate(problematic_commits, 1):
        print(f"\n--- Commit {i}: {subject_pattern} ---")

        try:
            commit_hash, full_message = get_commit_by_subject(subject_pattern)

            if commit_hash and full_message:
                fixed_message = fix_commit_message(full_message)
                print(f"Commit Hash: {commit_hash}")
                print("\nORIGINAL:")
                print(full_message)
                print("\nFIXED:")
                print(fixed_message)
                print("-" * 40)
            else:
                print(f"❌ Could not find commit matching: {subject_pattern}")

        except subprocess.CalledProcessError as e:
            print(f"❌ Error processing commit: {e}")

    print("\n" + "=" * 50)
    print("To fix these commits, use:")
    print("git rebase -i HEAD~20")
    print("\nThen replace each commit message with the corrected version above.")
    print("\nOr use git commit --amend for the most recent commit.")


if __name__ == "__main__":
    main()
