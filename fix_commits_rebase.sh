#!/bin/bash
# Auto-generated rebase script to fix commit messages
# Run this script after starting an interactive rebase

echo 'Starting commit message fixes...'

echo 'Fixing commit 1: d0e7c98e'
git commit --amend -F - << 'EOF'
feat(core): add core interfaces and directory structure


Introduces the foundational package structure and core algorithm interfaces, a key step in Phase 2 of the project.

This commit establishes the main directory hierarchy for different algorithm categories (basic, intermediate, advanced) and testing (unit, property). It also defines the fundamental , , and  protocols in , which will serve as the contracts for all future algorithm implementations.

Additionally, this commit includes several maintenance updates:
- Migrated  to the PEP 621 standard, resolving all All set! warnings.
- Fixed numerous pre-commit hook failures related to imports, typing, and formatting that arose from the interface changes.
- Cleaned up and consolidated abstract base classes for algorithms.
EOF
echo 'Fixed commit message'

echo 'Fixing commit 2: 039c2c55'
git commit --amend -F - << 'EOF'
fix(ci): resolve pytest collection warning


Updates the pytest configuration to prevent the test runner from inspecting the  directory.

The  class within this directory was being incorrectly collected by pytest because its name starts with 'Test', causing a . This has been resolved by adding  to the  setting in , which correctly instructs pytest to ignore this directory.
EOF
echo 'Fixed commit message'

echo 'Fixing commit 3: 33a572b3'
git commit --amend -F - << 'EOF'
test(tests): add property-based tests for core algorithms

This commit introduces a comprehensive suite of property-based tests using Hypothesis to validate the correctness and invariants of core algorithms and data structures. - Added a `property` marker to `pytest.ini` to label these tests. - Implemented property tests for all sorting algorithms, ensuring their output matches Python's built-in `sorted()` function. - Created property tests for graph traversal algorithms (BFS and DFS) to verify that they visit all reachable nodes and that BFS traverses in non-decreasing depth order. - Added property tests for `AVLTree` and `RedBlackTree` to validate their structural invariants, such as balance factors, color rules, and black-height properties. - Refactored and consolidated existing sorting property tests into the new, centralized property...
EOF
echo 'Fixed commit message'

echo 'Fixing commit 4: 709ef88a'
git commit --amend -F - << 'EOF'
feat(core): add runtime checks and property-based tests


This commit introduces several improvements to enhance the robustness and correctness of the algorithms.

- Added `typeguard` to enable runtime type checking during tests, configured via `pytest.ini`. This helps in catching type-related errors that might not be caught by static analysis.

- The binary search algorithm now verifies that the input data is sorted, raising a `ValueError` if it's not. This prevents incorrect results from being returned silently. A corresponding test case has been added to validate this behavior.

- A new property-based test has been added for Dijkstra's algorithm to ensure it raises a `ValueError` when encountering a graph with negative edge weights, which it is not designed to handle....
EOF
echo 'Fixed commit message'

echo 'Fixing commit 5: 78f7cb73'
git commit --amend -F - << 'EOF'
feat(benchmarks): add detailed benchmark harness for merge, quick, heap sort and dijkstra


- Added tests/benchmarks/{merge,quick,heap,dijkstra}_bench.py with @pytest.mark.benchmark, 3 rounds, 1 warmup
- Updated pytest.ini and pyproject.toml to separate coverage from benchmarks
- Fixed all mypy and formatting issues, ensured pre-commit compliance
- Benchmarks now run cleanly and are excluded from main CI coverage

BREAKING CHANGE: Benchmarking and coverage are now fully separated in CI and local workflows.

Closes #phase2-benchmarks
EOF
echo 'Fixed commit message'

echo 'Fixing commit 6: 1e92c652'
git commit --amend -F - << 'EOF'
feat(ci): implement ci & pre-commit pipeline updates

- Update CI workflow to exclude benchmarks from regular test runs - Add nightly performance benchmark workflow (perf-nightly.yml) - Add pytest-collect hook to pre-commit for test validation - Rename benchmark files to follow pytest naming convention - Update documentation with pre-commit installation instructions - Exclude benchmarks from pre-commit pytest runs (temporary) CI Changes: - ci.yml: run 'pytest -q -m "not benchmark"' + coverage xml - perf-nightly.yml: new workflow for benchmark-only tests - Pre-commit: add pytest-collect hook, exclude benchmarks Documentation: - Add pre-commit setup instructions to contributors guide - Document CI pipeline structure and nightly benchmarks Benchmarks: - Rename *_bench.py files to test_*_bench.py for pytest discovery - Add __init__.py to...
EOF
echo 'Fixed commit message'

echo 'Fixing commit 7: 1b29b981'
git commit --amend -F - << 'EOF'
ci(ci): enforce ruff f401, pre-commit in ci, and 95% coverage gate


- Enable ruff F401 (unused imports) rule in lint config and verify no violations
- Add pre-commit run --all-files --show-diff-on-failure step before pytest in CI
- Enforce 95% minimum test coverage in CI and pyproject config
- Add Makefile target 'quality-gate' for local all-in-one quality checks
- Update contributors guide with quality gate and coverage requirements
- Remove obsolete benchmark test files for consistency
- Security: pip-audit run, no vulnerabilities found

Follows PEP8, strict typing, SOLID, DRY/KISS, Conventional Commits, TDD, CI gate, IaC, 12-Factor, and secure-by-default standards.
EOF
echo 'Fixed commit message'

echo 'All commits fixed successfully!'
echo 'Continue with: git rebase --continue'
