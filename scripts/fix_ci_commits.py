#!/usr/bin/env python3
"""
Comprehensive script to fix commit messages that are failing CI validation.

This script provides both automatic fixes and manual instructions for the specific
commits mentioned in the CI error.
"""

import re
import subprocess
from typing import List, Optional, Tuple


def get_commit_by_subject(subject_pattern: str) -> Optional[Tuple[str, str]]:
    """Get commit hash and full message by subject pattern."""
    try:
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep", subject_pattern, "-1"],
            capture_output=True,
            text=True,
            check=True,
        )

        if not result.stdout.strip():
            return None

        parts = result.stdout.strip().split(" ", 1)
        if len(parts) == 2:
            commit_hash = parts[0]
            full_message = get_full_commit_message(commit_hash)
            return commit_hash, full_message

        return None
    except subprocess.CalledProcessError:
        return None


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


def create_rebase_script(commits: List[Tuple[str, str, str]]) -> str:
    """Create a rebase script for fixing commits."""
    script_lines = [
        "#!/bin/bash",
        "# Auto-generated rebase script to fix commit messages",
        "# Run this script after starting an interactive rebase",
        "",
        "echo 'Starting commit message fixes...'",
        "",
    ]

    for i, (hash_val, _original, fixed) in enumerate(commits, 1):
        script_lines.extend([
            f"echo 'Fixing commit {i}: {hash_val[:8]}'",
            "git commit --amend -F - << 'EOF'",
            fixed,
            "EOF",
            "echo 'Fixed commit message'",
            "",
        ])

    script_lines.extend([
        "echo 'All commits fixed successfully!'",
        "echo 'Continue with: git rebase --continue'",
    ])

    return "\n".join(script_lines)


def main() -> None:
    """Main function to fix commit messages."""
    print("🔧 CI Commit Message Fixer")
    print("=" * 60)

    # Define the problematic commits from the CI error
    problematic_commits = [
        "feat(scaffolding): Add core interfaces and directory structure",
        "fix(ci): Resolve pytest collection warning",
        "test(property): add property-based tests for core algorithms",
        "feat(runtime): add runtime checks and property-based tests",
        "feat(benchmarks): add detailed benchmark harness for merge, quick, heap sort and Dijkstra",
        "feat(ci): implement CI & pre-commit pipeline updates",
        "ci(quality-gate): enforce ruff F401, pre-commit in CI, and 95% coverage gate",
    ]

    print("Analyzing problematic commits...")
    print("=" * 60)

    fixes = []

    for i, subject_pattern in enumerate(problematic_commits, 1):
        print(f"\n--- Commit {i}: {subject_pattern} ---")

        result = get_commit_by_subject(subject_pattern)

        if result:
            commit_hash, full_message = result
            fixed_message = fix_commit_message(full_message)
            fixes.append((commit_hash, full_message, fixed_message))

            print(f"✅ Found: {commit_hash[:8]}")
            print(f"Original: {full_message.split()[0]}...")
            print(f"Fixed:    {fixed_message.split()[0]}...")
        else:
            print(f"❌ Not found: {subject_pattern}")

    if not fixes:
        print("\n❌ No commits found to fix!")
        return

    print(f"\n✅ Found {len(fixes)} commits to fix")
    print("=" * 60)

    # Show detailed fixes
    print("\nDetailed fixes:")
    print("=" * 60)

    for i, (hash_val, original, fixed) in enumerate(fixes, 1):
        print(f"\n--- Fix {i}: {hash_val[:8]} ---")
        print("ORIGINAL:")
        print(original)
        print("\nFIXED:")
        print(fixed)
        print("-" * 40)

    # Create rebase script
    script_content = create_rebase_script(fixes)
    script_path = "fix_commits_rebase.sh"

    with open(script_path, "w") as f:
        f.write(script_content)

    # Make script executable
    subprocess.run(["chmod", "+x", script_path], check=True)

    print("\n" + "=" * 60)
    print("🔧 AUTOMATIC FIX INSTRUCTIONS")
    print("=" * 60)
    print(f"1. Interactive rebase: git rebase -i HEAD~{len(fixes) + 5}")
    print("2. For each commit to fix, change 'pick' to 'reword'")
    print("3. Save and close the editor")
    print("4. For each commit, replace the message with the fixed version above")
    print("5. Continue with: git rebase --continue")
    print("\nOr use the generated script:")
    print(f"1. Start rebase: git rebase -i HEAD~{len(fixes) + 5}")
    print("2. Change commits to 'edit' instead of 'pick'")
    print(f"3. Run: ./{script_path}")
    print("4. Continue: git rebase --continue")

    print("\n" + "=" * 60)
    print("🔧 MANUAL FIX INSTRUCTIONS")
    print("=" * 60)
    print("For each commit above:")
    print("1. git commit --amend")
    print("2. Replace the message with the fixed version")
    print("3. Save and close")
    print("4. git push --force-with-lease")

    print(f"\n📝 Generated script: {script_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
