#!/usr/bin/env python3
"""
Interface Compliance Check Script

This script ensures that new code adheres to the project's interface rules.
It performs two main checks on new or modified Python files:
1.  Disallows subclassing from a predefined list of concrete data structures
    to prevent implementation inheritance where an interface should be used.
2.  Prevents writing to protected members (e.g., `_parent`) of core classes
    to enforce encapsulation.

The script is designed to be run in a CI pipeline. It takes a Git SHA as an
argument to identify the set of files to check.
"""

import argparse
import ast
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Set

# --- Configuration ---

# Add project root to sys.path to allow imports if needed, though this
# script primarily uses AST and doesn't need to import the actual modules.
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Concrete classes that should not be subclassed directly.
# Encourages depending on abstractions, not concretions.
CONCRETE_CLASSES_TO_PROTECT: Set[str] = {
    "DisjointSet",
    "Graph",
    "LinkedList",
    "Queue",
    "Stack",
    "BFS",
    "BinarySearcher",
    "LinearSearcher",
    "BubbleSorter",
    "MergeSorter",
}

# Protected members of core classes that should not be written to directly.
# Maps class name to a set of its protected members.
PROTECTED_MEMBERS: dict[str, Set[str]] = {
    "DisjointSet": {"_parent", "_rank"},
    "Graph": {"_adjacency_list"},
    "LinkedList": {"_head"},
    "Queue": {"_items"},
    "Stack": {"_items"},
}


class InterfaceChecker(ast.NodeVisitor):
    """
    AST visitor that checks for interface violations in a Python file.
    """

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.errors: List[str] = []
        self._current_class: str | None = None

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        # Check for subclassing from protected concrete classes
        for base in node.bases:
            if isinstance(base, ast.Name) and base.id in CONCRETE_CLASSES_TO_PROTECT:
                self.errors.append(
                    f"{self.file_path}:{node.lineno}: Class '{node.name}' "
                    f"must not subclass concrete class '{base.id}'."
                )

        # Keep track of the current class context for member access checks
        original_class = self._current_class
        self._current_class = node.name
        self.generic_visit(node)
        self._current_class = original_class

    def visit_Attribute(self, node: ast.Attribute) -> None:
        # Check for writes to protected members
        if isinstance(node.ctx, ast.Store):
            # This check is a heuristic: it identifies writes to attributes on `self`.
            # A more robust check might involve type inference, but for this
            # project's conventions, this is a strong signal of an issue.
            if isinstance(node.value, ast.Name) and node.value.id == "self":
                for class_name, members in PROTECTED_MEMBERS.items():
                    if node.attr in members:
                        self.errors.append(
                            f"{self.file_path}:{node.lineno}: Direct write to protected "
                            f"member 'self.{node.attr}' is disallowed. "
                            f"This may be a false positive if 'self' is not an instance of '{class_name}'."
                        )
        self.generic_visit(node)


def get_changed_python_files(base_sha: str) -> List[Path]:
    """
    Returns a list of new or modified .py files compared to the base SHA.
    """
    try:
        diff_output = subprocess.check_output(
            ["git", "diff", "--name-only", "--diff-filter=AM", base_sha, "--", "*.py"],
            text=True,
            cwd=project_root,
        ).strip()

        if not diff_output:
            return []
        return [project_root / file for file in diff_output.splitlines()]
    except subprocess.CalledProcessError as e:
        print(f"Error getting git diff: {e}", file=sys.stderr)
        return []


def main() -> None:
    """Main execution function."""
    parser = argparse.ArgumentParser(description="Check for interface compliance.")
    parser.add_argument(
        "base_sha",
        nargs="?",
        default=os.environ.get("BASE_SHA", "HEAD"),
        help="The base Git SHA to compare against for new/modified files. Defaults to env var BASE_SHA or 'HEAD'.",
    )
    args = parser.parse_args()

    py_files = get_changed_python_files(args.base_sha)
    if not py_files:
        print("No new or modified Python files to check.")
        sys.exit(0)

    print(f"Checking {len(py_files)} Python file(s) for interface compliance...")
    all_errors: List[str] = []

    for file_path in py_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                source_code = f.read()
            tree = ast.parse(source_code, filename=str(file_path))
            checker = InterfaceChecker(file_path)
            checker.visit(tree)
            all_errors.extend(checker.errors)
        except Exception as e:
            print(f"Error processing {file_path}: {e}", file=sys.stderr)
            all_errors.append(f"Could not process {file_path}.")

    if all_errors:
        print("\n--- Interface Compliance Errors Found ---", file=sys.stderr)
        for error in all_errors:
            print(error, file=sys.stderr)
        print(f"\nFound {len(all_errors)} compliance error(s).", file=sys.stderr)
        sys.exit(1)
    else:
        print("\n✅ All checked files comply with interface standards.")
        sys.exit(0)


if __name__ == "__main__":
    main()
