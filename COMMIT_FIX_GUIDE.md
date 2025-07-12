# Commit Message Fix Guide

This guide helps fix the commit message validation errors that are causing CI failures.

## Problem Summary

The CI pipeline is failing due to commitlint validation errors on several commits:

1. **Subject case errors**: Subjects must be lowercase
2. **Body length errors**: Body must be ≤ 800 characters
3. **Scope errors**: Invalid scopes need to be mapped to valid ones

## Affected Commits

The following commits need to be fixed:

1. `feat(scaffolding): Add core interfaces and directory structure`
   - **Issue**: Subject case + invalid scope
   - **Fix**: `feat(core): add core interfaces and directory structure`

2. `fix(ci): Resolve pytest collection warning`
   - **Issue**: Subject case
   - **Fix**: `fix(ci): resolve pytest collection warning`

3. `test(property): add property-based tests for core algorithms`
   - **Issue**: Invalid scope + body too long
   - **Fix**: `test(tests): add property-based tests for core algorithms` (truncated body)

4. `feat(runtime): add runtime checks and property-based tests`
   - **Issue**: Invalid scope + body too long
   - **Fix**: `feat(core): add runtime checks and property-based tests` (truncated body)

5. `feat(benchmarks): add detailed benchmark harness for merge, quick, heap sort and Dijkstra`
   - **Issue**: Subject case
   - **Fix**: `feat(benchmarks): add detailed benchmark harness for merge, quick, heap sort and dijkstra`

6. `feat(ci): implement CI & pre-commit pipeline updates`
   - **Issue**: Subject case + body too long
   - **Fix**: `feat(ci): implement ci & pre-commit pipeline updates` (truncated body)

7. `ci(quality-gate): enforce ruff F401, pre-commit in CI, and 95% coverage gate`
   - **Issue**: Invalid scope + subject case
   - **Fix**: `ci(ci): enforce ruff f401, pre-commit in ci, and 95% coverage gate`

## Quick Fix Scripts

### 1. Automatic Fix Script

Run the comprehensive fix script:

```bash
python scripts/fix_ci_commits.py
```

This will:
- Show all the fixes needed
- Generate a rebase script
- Provide detailed instructions

### 2. Validation Script

Check if commits are valid:

```bash
python scripts/validate_commits.py
```

## Manual Fix Instructions

### Option 1: Interactive Rebase (Recommended)

1. Start interactive rebase:
   ```bash
   git rebase -i HEAD~12
   ```

2. Change commits to fix from `pick` to `reword`:
   ```
   reword d0e7c98 feat(scaffolding): Add core interfaces and directory structure
   reword 039c2c5 fix(ci): Resolve pytest collection warning
   reword 33a572b test(property): add property-based tests for core algorithms
   reword 709ef88 feat(runtime): add runtime checks and property-based tests
   reword 78f7cb7 feat(benchmarks): add detailed benchmark harness for merge, quick, heap sort and Dijkstra
   reword 1e92c65 feat(ci): implement CI & pre-commit pipeline updates
   reword 1b29b98 ci(quality-gate): enforce ruff F401, pre-commit in CI, and 95% coverage gate
   pick ... # other commits
   ```

3. For each commit, replace the message with the fixed version from the script output

4. Continue the rebase:
   ```bash
   git rebase --continue
   ```

### Option 2: Individual Commit Amends

For each commit that needs fixing:

1. Checkout the commit:
   ```bash
   git checkout <commit-hash>
   ```

2. Amend the commit:
   ```bash
   git commit --amend
   ```

3. Replace the message with the fixed version

4. Force push (if on a feature branch):
   ```bash
   git push --force-with-lease
   ```

## Fixed Commit Messages

Here are the exact fixed messages to use:

### 1. Core Interfaces
```
feat(core): add core interfaces and directory structure

Introduces the foundational package structure and core algorithm interfaces, a key step in Phase 2 of the project.

This commit establishes the main directory hierarchy for different algorithm categories (basic, intermediate, advanced) and testing (unit, property). It also defines the fundamental , , and  protocols in , which will serve as the contracts for all future algorithm implementations.

Additionally, this commit includes several maintenance updates:
- Migrated  to the PEP 621 standard, resolving all All set! warnings.
- Fixed numerous pre-commit hook failures related to imports, typing, and formatting that arose from the interface changes.
- Cleaned up and consolidated abstract base classes for algorithms.
```

### 2. Pytest Warning
```
fix(ci): resolve pytest collection warning

Updates the pytest configuration to prevent the test runner from inspecting the  directory.

The  class within this directory was being incorrectly collected by pytest because its name starts with 'Test', causing a . This has been resolved by adding  to the  setting in , which correctly instructs pytest to ignore this directory.
```

### 3. Property Tests
```
test(tests): add property-based tests for core algorithms

This commit introduces a comprehensive suite of property-based tests using Hypothesis to validate the correctness and invariants of core algorithms and data structures. - Added a `property` marker to `pytest.ini` to label these tests. - Implemented property tests for all sorting algorithms, ensuring their output matches Python's built-in `sorted()` function. - Created property tests for graph traversal algorithms (BFS and DFS) to verify that they visit all reachable nodes and that BFS traverses in non-decreasing depth order. - Added property tests for `AVLTree` and `RedBlackTree` to validate their structural invariants, such as balance factors, color rules, and black-height properties. - Refactored and consolidated existing sorting property tests into the new, centralized...
```

### 4. Runtime Checks
```
feat(core): add runtime checks and property-based tests

This commit introduces several improvements to enhance the robustness and correctness of the algorithms.

- Added `typeguard` to enable runtime type checking during tests, configured via `pytest.ini`. This helps in catching type-related errors that might not be caught by static analysis.

- The binary search algorithm now verifies that the input data is sorted, raising a `ValueError` if it's not. This prevents incorrect results from being returned silently. A corresponding test case has been added to validate this behavior.

- A new property-based test has been added for Dijkstra's algorithm to ensure it raises a `ValueError` when encountering a graph with negative edge weights, which it is not designed to handle....
```

### 5. Benchmarks
```
feat(benchmarks): add detailed benchmark harness for merge, quick, heap sort and dijkstra

- Added tests/benchmarks/{merge,quick,heap,dijkstra}_bench.py with @pytest.mark.benchmark, 3 rounds, 1 warmup
- Updated pytest.ini and pyproject.toml to separate coverage from benchmarks
- Fixed all mypy and formatting issues, ensured pre-commit compliance
- Benchmarks now run cleanly and are excluded from main CI coverage

BREAKING CHANGE: Benchmarking and coverage are now fully separated in CI and local workflows.

Closes #phase2-benchmarks
```

### 6. CI Pipeline
```
feat(ci): implement ci & pre-commit pipeline updates

- Update CI workflow to exclude benchmarks from regular test runs - Add nightly performance benchmark workflow (perf-nightly.yml) - Add pytest-collect hook to pre-commit for test validation - Rename benchmark files to follow pytest naming convention - Update documentation with pre-commit installation instructions - Exclude benchmarks from pre-commit pytest runs (temporary) CI Changes: - ci.yml: run 'pytest -q -m "not benchmark"' + coverage xml - perf-nightly.yml: new workflow for benchmark-only tests - Pre-commit: add pytest-collect hook, exclude benchmarks Documentation: - Add pre-commit setup instructions to contributors guide - Document CI pipeline structure and nightly benchmarks Benchmarks: - Rename *_bench.py files to test_*_bench.py for pytest discovery - Add __init__.py to...
```

### 7. Quality Gate
```
ci(ci): enforce ruff f401, pre-commit in ci, and 95% coverage gate

- Enable ruff F401 (unused imports) rule in lint config and verify no violations
- Add pre-commit run --all-files --show-diff-on-failure step before pytest in CI
- Enforce 95% minimum test coverage in CI and pyproject config
- Add Makefile target 'quality-gate' for local all-in-one quality checks
- Update contributors guide with quality gate and coverage requirements
- Remove obsolete benchmark test files for consistency
- Security: pip-audit run, no vulnerabilities found

Follows PEP8, strict typing, SOLID, DRY/KISS, Conventional Commits, TDD, CI gate, IaC, 12-Factor, and secure-by-default standards.
```

## Prevention

To prevent future issues:

1. **Use the validation script** before pushing:
   ```bash
   python scripts/validate_commits.py
   ```

2. **Follow commit message guidelines**:
   - Use lowercase subjects
   - Keep bodies under 800 characters
   - Use valid scopes from `commitlint.config.mjs`

3. **Use the fix script** for new commits:
   ```bash
   python scripts/fix_commits.py
   ```

## Scope Mapping

Invalid scopes are automatically mapped to valid ones:

- `scaffolding` → `core`
- `property` → `tests`
- `runtime` → `core`
- `quality-gate` → `ci`
- `benchmarks` → `benchmarks` (already valid)

## After Fixing

1. Push the fixed commits:
   ```bash
   git push --force-with-lease
   ```

2. Verify CI passes:
   - Check the PR status
   - Ensure all commitlint checks pass

3. Update documentation if needed:
   - Update commit message guidelines
   - Add validation to pre-commit hooks
