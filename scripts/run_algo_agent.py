#!/usr/bin/env python3
"""
Orchestration script to generate algorithm implementations from specs.

This script identifies new or changed algorithm specification files, then uses
the agent_tools to generate, validate, and commit the corresponding code,
tests, and documentation.

Features:
- Identifies changed specs using Git diff.
- Parses and validates specs using Pydantic models.
- Generates artifacts into a temporary directory (.agent-tmp).
- Validates generated code with ruff, mypy, and pytest.
- If validation passes, moves artifacts into the main repo.
- Creates a new branch, commits, and pushes the changes.
- Prints a pull request URL for easy review.
- Supports a --dry-run mode to generate files without committing.
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List

from git import Repo
from git.exc import GitCommandError

from agent_tools.agent import Agent
from algolib.specs.schema import AlgorithmSpec

# Add project root to sys.path to allow imports from algolib and agent_tools
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


def get_changed_specs(base_sha: str) -> List[Path]:
    """
    Returns a list of new or modified .yml files in the specs/ directory
    compared to the base SHA.
    """
    repo = Repo(project_root)
    try:
        diff_output = repo.git.diff("--name-only", base_sha, "--", "specs/*.yml")
        if not diff_output:
            return []
        return [project_root / file for file in diff_output.splitlines()]
    except GitCommandError as e:
        print(f"Error getting git diff: {e}", file=sys.stderr)
        return []


def validate_generated_files(temp_dir: Path) -> bool:
    """
    Runs ruff, mypy, and pytest on the generated files in the temp directory.
    """
    print(f"Running validation in: {temp_dir}")
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{temp_dir}:{env.get('PYTHONPATH', '')}"

    try:
        print("\n--- Running Ruff Formatter ---")
        subprocess.run(
            ["ruff", "format", "."], cwd=temp_dir, check=True, capture_output=True, text=True
        )

        print("\n--- Running Ruff Linter ---")
        subprocess.run(
            ["ruff", "check", "--fix", "."],
            cwd=temp_dir,
            check=True,
            capture_output=True,
            text=True,
        )

        print("\n--- Running MyPy ---")
        subprocess.run(["mypy", "."], cwd=temp_dir, check=True, capture_output=True, text=True)

        print("\n--- Running Pytest ---")
        subprocess.run(
            ["pytest", "-q"], cwd=temp_dir, check=True, capture_output=True, text=True, env=env
        )

        print("\n✅ Validation successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Validation failed: {e.cmd}", file=sys.stderr)
        print(e.stdout, file=sys.stdout)
        print(e.stderr, file=sys.stderr)
        return False


def main(base_sha: str, dry_run: bool) -> None:
    """Main execution function."""
    changed_specs = get_changed_specs(base_sha)
    if not changed_specs:
        print("No new or changed specs found.")
        return

    for spec_path in changed_specs:
        print(f"\nProcessing spec: {spec_path.name}")
        try:
            spec = AlgorithmSpec.from_file(spec_path)
        except Exception as e:
            print(f"Error parsing spec {spec_path.name}: {e}", file=sys.stderr)
            continue

        agent = Agent(spec)
        generated_files = agent.run()

        slug = spec.name.lower().replace(" ", "_")
        temp_dir = project_root / ".agent-tmp" / slug

        if not validate_generated_files(temp_dir):
            print(f"Skipping {spec.name} due to validation errors.")
            if not dry_run:
                shutil.rmtree(temp_dir)
            continue

        if dry_run:
            print(f"Dry run: Artifacts for {spec.name} are in {temp_dir}")
            continue

        # --- Git Operations ---
        repo = Repo(project_root)
        origin = repo.remotes.origin

        # Move files from temp to repo
        for _file_type, src_path in generated_files.items():
            # The output_path in the writers already includes the target structure
            dest_path = project_root / src_path.relative_to(temp_dir)
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src_path), str(dest_path))

        # Create branch, commit, and push
        branch_name = f"agent/{slug}"
        try:
            new_branch = repo.create_head(branch_name)
            new_branch.checkout()

            repo.index.add([str(p.relative_to(project_root)) for p in generated_files.values()])
            repo.index.commit(f"feat({spec.category}): implement {spec.name} via agent")

            print(f"Pushing branch {branch_name} to origin...")
            origin.push(refspec=f"{branch_name}:{branch_name}")

            # Construct PR URL
            repo_url = origin.url.split(".git")[0].replace(":", "/").replace("git@", "https://")
            pr_url = f"{repo_url}/pull/new/{branch_name}"
            print(f"\n🚀 Successfully created and pushed branch for {spec.name}.")
            print(f"   Create a PR: {pr_url}")

        except Exception as e:
            print(f"Error during Git operations for {spec.name}: {e}", file=sys.stderr)
            repo.heads.master.checkout()  # Or main
            repo.delete_head(branch_name, force=True)
        finally:
            shutil.rmtree(temp_dir)
            # Switch back to the original branch
            # This is a simplification; a more robust implementation would store the original branch name
            repo.heads.master.checkout()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate and commit algorithm implementations from specs."
    )
    parser.add_argument(
        "base_sha", help="The base Git SHA to compare against for detecting changed specs."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run the script without performing Git operations or cleaning up temp files.",
    )
    args = parser.parse_args()

    main(args.base_sha, args.dry_run)
