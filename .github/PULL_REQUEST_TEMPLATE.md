---
name: New Feature/Fix
about: Propose a change to the repository
title: 'feat: '
labels: ''
assignees: ''

---

## 📋 Pull Request Summary

### Description

A clear and concise description of what the pull request does.

### Related Issue

Please link to the issue this PR addresses.

### Algorithm Specification

If this PR implements a new algorithm, please cite the `spec.yml` file.

**Example:** `specs/BubbleSort.yml`

## 🔍 Review Requirements

### Code Quality Checklist

- [ ] **PEP 8 + Ruff Compliance**: Code follows style guidelines and passes `ruff check`
- [ ] **Strict Typing**: All code has proper type hints and passes `mypy --strict`
- [ ] **SOLID Principles**: Classes follow single responsibility and dependency inversion
- [ ] **Clean Code**: Functions are small, names are clear, no code duplication (DRY/KISS)
- [ ] **Test Coverage**: ≥95% coverage with meaningful tests
- [ ] **Documentation**: All public APIs are documented with docstrings

### Conventional Commits Validation

- [ ] **Commit Messages**: All commits follow conventional commit format
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation changes
  - `style:` for formatting changes
  - `refactor:` for code refactoring
  - `test:` for adding tests
  - `chore:` for maintenance tasks
- [ ] **Scope**: Commits include appropriate scope (e.g., `feat(algorithms): add binary search`)
- [ ] **Breaking Changes**: Breaking changes are marked with `!` and documented

### CI/CD Pipeline

- [ ] **All CI Checks Pass**:
  - ✅ Ruff formatting and linting
  - ✅ MyPy strict type checking
  - ✅ Pytest with ≥95% coverage
  - ✅ Interface compliance check
  - ✅ Pre-commit hooks
  - ✅ Security audit (pip-audit)
- [ ] **No Merge Conflicts**: Branch is up-to-date with main
- [ ] **Draft PR**: PR starts as draft and moves to ready when complete

## 🚀 Implementation Checklist

### For Algorithm Implementations

- [ ] I have run the algorithm agent locally to generate the code, tests, and documentation.
  ```bash
  # 1. Copy the template spec
  cp specs/template.yml specs/NewAlgorithm.yml
  # 2. Edit the new spec file
  # 3. Run the agent in dry-run mode
  poetry run python scripts/run_algo_agent.py --dry-run specs/NewAlgorithm.yml
  # 4. Run the agent to generate files
  poetry run python scripts/run_algo_agent.py specs/NewAlgorithm.yml
  ```
- [ ] I have verified the generated Pull Request URL and confirmed that CI checks are passing.
- [ ] All new and existing tests pass.
- [ ] My code follows the code style of this project.
- [ ] I have updated the documentation accordingly.

### For Data Structure Implementations

- [ ] Interface compliance with `algolib.interfaces`
- [ ] Property-based tests included
- [ ] Performance benchmarks added
- [ ] Documentation with complexity analysis

### For Infrastructure Changes

- [ ] Environment variables documented
- [ ] Security implications reviewed
- [ ] Backward compatibility maintained
- [ ] Rollback plan documented

## 👥 Review Process

### Required Reviews

- [ ] **Two Approvals**: Minimum of 2 maintainer approvals required
- [ ] **Code Review**: All code has been reviewed for:
  - Security vulnerabilities
  - Performance implications
  - Maintainability concerns
  - Test coverage adequacy
- [ ] **Documentation Review**: Documentation is clear and complete
- [ ] **Integration Testing**: Changes work correctly with existing systems

### Review Guidelines

1. **Be Constructive**: Provide specific, actionable feedback
2. **Check Standards**: Verify compliance with project standards
3. **Test Locally**: Reviewers should test changes locally when possible
4. **Security First**: Pay special attention to security implications
5. **Performance**: Consider performance impact of changes

## 🔒 Merge Requirements

### Before Merge

- [ ] **Draft Status**: PR is ready for review (not draft)
- [ ] **CI Green**: All CI checks are passing
- [ ] **Reviews Complete**: Required number of approvals received
- [ ] **No Conflicts**: Branch can be merged without conflicts
- [ ] **Documentation**: All changes are properly documented

### Merge Strategy

- **Squash and Merge**: For feature branches with multiple commits
- **Rebase and Merge**: For clean, linear history when appropriate
- **Create Merge Commit**: For complex changes requiring detailed history

### Post-Merge

- [ ] **Version Bump**: Update version in `pyproject.toml` if needed
- [ ] **Changelog**: Update `CHANGELOG.md` with changes
- [ ] **Release Notes**: Create release notes for significant changes
- [ ] **Cleanup**: Delete feature branch after successful merge

## 📝 Additional Notes

Any additional context, considerations, or notes for reviewers.

---

**Note**: This PR will be automatically converted to draft if any CI checks fail. Please ensure all requirements are met before requesting review.
