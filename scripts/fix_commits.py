#!/usr/bin/env python3
"""
Script to fix commit messages to comply with commitlint rules.

This script helps rewrite commit messages to meet the following requirements:
- Body lines ≤ 300 characters
- Subject lines lowercase
- Valid scopes from predefined list
- Footer lines ≤ 300 characters
- Body max length ≤ 800 characters
"""

import re
import subprocess
from typing import List, Tuple


def get_commit_messages() -> List[Tuple[str, str]]:
    """Get recent commit hashes and messages."""
    result = subprocess.run(
        ["git", "log", "--format=%H %s", "-10"], capture_output=True, text=True, check=True
    )

    commits = []
    for line in result.stdout.strip().split("\n"):
        if line.strip():
            parts = line.split(" ", 1)
            if len(parts) == 2:
                commits.append((parts[0], parts[1]))

    return commits


def get_full_commit_message(commit_hash: str) -> str:
    """Get the full commit message for a given hash."""
    result = subprocess.run(
        ["git", "show", "--format=%B", "--no-patch", commit_hash],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def _get_prefix_and_content(text: str) -> tuple[str, str]:
    if text.startswith("- "):
        return "- ", text[2:]
    if text.startswith("* "):
        return "* ", text[2:]
    if text.startswith("BREAKING CHANGE:"):
        return "BREAKING CHANGE: ", text[17:]
    if text.startswith("Closes:"):
        return "Closes: ", text[8:]
    if text.startswith("Fixes:"):
        return "Fixes: ", text[7:]
    return "", text


def wrap_text(text: str, max_length: int = 300) -> str:
    """Wrap text to specified line length, preserving bullet points."""
    if not text.strip():
        return ""
    prefix, content = _get_prefix_and_content(text)
    available_length = max_length - len(prefix)
    words = content.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= available_length:
            current_line += (word + " ") if current_line else word
        else:
            if current_line:
                lines.append(prefix + current_line.rstrip())
            current_line = word
    if current_line:
        lines.append(prefix + current_line.rstrip())
    return "\n".join(lines)


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
            "deps": "deps",
            "ci": "ci",
            "core": "core",
            "property": "tests",
            "db/session": "db",
            "pyproject": "config",
            "pr": "docs",
            "review-merge": "ci",
            "runtime": "core",
            "quality-gate": "ci",
            "benchmarks": "benchmarks",
        }

        fixed_scope = scope_mapping.get(scope, "core")
        fixed_subject = subject.lower()
        fixed_header = f"{commit_type}({fixed_scope}): {fixed_subject}"
    else:
        fixed_header = header.lower()

    # Process body lines
    fixed_body_lines = []
    body_text = ""

    for line in body_lines:
        if line.strip():
            wrapped_line = wrap_text(line, 300)
            if wrapped_line:
                fixed_body_lines.append(wrapped_line)
                body_text += wrapped_line + "\n"
        else:
            fixed_body_lines.append("")
            body_text += "\n"

    # Truncate body if too long
    if len(body_text) > 800:
        body_text = truncate_body(body_text, 800)
        # Rebuild body lines from truncated text
        fixed_body_lines = [line for line in body_text.split("\n") if line.strip()]

    # Build result
    result_lines = [fixed_header]
    if fixed_body_lines:
        result_lines.append("")
        result_lines.extend(fixed_body_lines)

    return "\n".join(result_lines)


def main() -> None:
    """Main function to fix commit messages."""
    print("🔧 Commit Message Fixer")
    print("=" * 50)
    commits = get_commit_messages()
    print(f"Found {len(commits)} recent commits:")
    for i, (hash_val, _subject) in enumerate(commits, 1):
        print(f"{i}. {hash_val[:8]} - {_subject}")
    print("\n" + "=" * 50)
    print("Here are the corrected commit messages:")
    print("=" * 50)
    for i, (hash_val, _subject) in enumerate(commits, 1):
        print(f"\n--- Commit {i}: {hash_val[:8]} ---")
        try:
            full_message = get_full_commit_message(hash_val)
            fixed_message = fix_commit_message(full_message)
            print("ORIGINAL:")
            print(full_message)
            print("\nFIXED:")
            print(fixed_message)
            print("-" * 40)
        except subprocess.CalledProcessError as e:
            print(f"Error getting commit message for {hash_val}: {e}")
    print("\n" + "=" * 50)
    print("To fix these commits, you can use:")
    print("git rebase -i HEAD~10")
    print("\nThen replace each commit message with the corrected version above.")
    print("\nOr use git commit --amend for the most recent commit.")


if __name__ == "__main__":
    main()
