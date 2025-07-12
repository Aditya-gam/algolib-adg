# Merge Strategy Guide

This document outlines the merge strategy and process for the Algolib project, ensuring consistent and clean git history.

## Merge Methods

### 1. Squash and Merge

**When to use:**
- Feature branches with multiple commits
- Bug fix branches with iterative fixes
- When you want to combine all changes into a single commit

**Benefits:**
- Clean, linear history
- Single commit per feature/fix
- Easy to revert entire features
- Reduces noise in main branch

**Example:**
```bash
# Before merge: feature branch with 5 commits
feat(algorithms): add binary search implementation
fix(algorithms): handle edge case in binary search
test(algorithms): add comprehensive test suite
docs(algorithms): add docstring and examples
style(algorithms): format code according to standards

# After squash merge: single commit on main
feat(algorithms): add binary search implementation with tests and docs
```

**Process:**
1. Ensure all CI checks pass
2. Get required approvals (2 maintainers)
3. Use "Squash and merge" button on GitHub
4. Edit commit message to be descriptive
5. Delete feature branch after merge

### 2. Rebase and Merge

**When to use:**
- When you want to preserve individual commit history
- For complex changes that benefit from detailed commit history
- When commits are well-structured and meaningful

**Benefits:**
- Preserves detailed commit history
- Clean, linear history
- Individual commits remain intact
- Good for tracking incremental changes

**Example:**
```bash
# Before merge: feature branch with meaningful commits
feat(algorithms): add binary search base implementation
test(algorithms): add unit tests for binary search
perf(algorithms): optimize binary search for edge cases
docs(algorithms): add comprehensive documentation

# After rebase merge: same commits on main
feat(algorithms): add binary search base implementation
test(algorithms): add unit tests for binary search
perf(algorithms): optimize binary search for edge cases
docs(algorithms): add comprehensive documentation
```

**Process:**
1. Ensure all CI checks pass
2. Get required approvals (2 maintainers)
3. Use "Rebase and merge" button on GitHub
4. Delete feature branch after merge

### 3. Create Merge Commit

**When to use:**
- Complex changes requiring detailed history
- When you want to preserve branch information
- For major feature branches with multiple contributors

**Benefits:**
- Preserves branch information
- Clear merge points in history
- Good for tracking feature development
- Maintains context of development

**Example:**
```bash
# Before merge: feature branch with multiple commits
feat(algorithms): add binary search implementation
test(algorithms): add comprehensive test suite
docs(algorithms): add documentation

# After merge commit: merge commit + original commits
Merge pull request #123 from user/feat-binary-search
feat(algorithms): add binary search implementation
test(algorithms): add comprehensive test suite
docs(algorithms): add documentation
```

**Process:**
1. Ensure all CI checks pass
2. Get required approvals (2 maintainers)
3. Use "Create merge commit" button on GitHub
4. Delete feature branch after merge

## Pre-Merge Checklist

### For Contributors

- [ ] **Draft Status**: PR is ready for review (not draft)
- [ ] **CI Green**: All CI checks are passing
- [ ] **Reviews Complete**: Required number of approvals received
- [ ] **No Conflicts**: Branch can be merged without conflicts
- [ ] **Documentation**: All changes are properly documented
- [ ] **Tests**: Comprehensive test coverage (≥95%)
- [ ] **Code Quality**: Follows all project standards
- [ ] **Security**: No security vulnerabilities
- [ ] **Performance**: No obvious performance issues

### For Reviewers

- [ ] **Code Review**: Thorough review of all changes
- [ ] **Testing**: Verify tests are comprehensive
- [ ] **Documentation**: Check documentation quality
- [ ] **Standards**: Verify compliance with project standards
- [ ] **Security**: Review for security implications
- [ ] **Performance**: Consider performance impact
- [ ] **Integration**: Ensure changes work with existing systems

### For Maintainers

- [ ] **Merge Method**: Choose appropriate merge method
- [ ] **Commit Message**: Ensure descriptive commit message
- [ ] **Branch Cleanup**: Delete feature branch after merge
- [ ] **Version Update**: Update version if needed
- [ ] **Changelog**: Update CHANGELOG.md
- [ ] **Release Notes**: Create release notes for significant changes

## Post-Merge Process

### 1. Version Management

**When to bump version:**
- New features: Minor version bump (0.2.0 → 0.3.0)
- Bug fixes: Patch version bump (0.2.0 → 0.2.1)
- Breaking changes: Major version bump (0.2.0 → 1.0.0)

**Process:**
```bash
# Update version in pyproject.toml
poetry version patch  # or minor, major
git add pyproject.toml
git commit -m "chore(release): bump version to 0.2.1"
git tag v0.2.1
git push origin main --tags
```

### 2. Changelog Updates

**Format:**
```markdown
## [0.2.1] - 2024-01-15

### Added
- Binary search algorithm implementation
- Comprehensive test suite for searching algorithms

### Changed
- Improved performance of linear search

### Fixed
- Bug in edge case handling for empty arrays

### Security
- Updated dependencies to fix CVE-2024-1234
```

**Process:**
1. Update `CHANGELOG.md` with changes
2. Use conventional commit format
3. Include issue/PR references
4. Categorize changes appropriately

### 3. Release Notes

**For significant releases:**
1. Create detailed release notes
2. Include migration guides for breaking changes
3. Highlight new features and improvements
4. Document known issues and limitations

### 4. Branch Cleanup

**Automatic cleanup:**
- GitHub can automatically delete branches after merge
- Configure in repository settings
- Manual cleanup for branches not auto-deleted

**Manual cleanup:**
```bash
# Delete local branch
git branch -d feature-branch

# Delete remote branch
git push origin --delete feature-branch
```

## Merge Conflict Resolution

### 1. Prevention

- Keep feature branches short-lived
- Regularly sync with main branch
- Use `git rebase` to keep history clean

### 2. Resolution Process

1. **Identify conflicts:**
   ```bash
   git status
   ```

2. **Resolve conflicts:**
   - Edit conflicted files
   - Remove conflict markers
   - Test changes thoroughly

3. **Commit resolution:**
   ```bash
   git add .
   git commit -m "fix(merge): resolve conflicts with main branch"
   ```

4. **Push changes:**
   ```bash
   git push origin feature-branch
   ```

### 3. Conflict Resolution Guidelines

- **Preserve both changes** when possible
- **Test thoroughly** after resolution
- **Get review** for complex resolutions
- **Document decisions** in commit messages

## Emergency Hotfixes

### Process for Critical Issues

1. **Create hotfix branch:**
   ```bash
   git checkout -b hotfix/critical-security-fix main
   ```

2. **Make minimal changes:**
   - Focus only on the critical issue
   - Avoid unrelated changes
   - Test thoroughly

3. **Fast-track review:**
   - Expedited review process
   - Maintain quality standards
   - Get approval from maintainers

4. **Merge to main:**
   - Use "Squash and merge"
   - Create release immediately
   - Deploy to production

5. **Backport to release branches:**
   - Cherry-pick to stable branches
   - Create patch releases
   - Update all affected versions

## Quality Gates

### Automated Checks

- **CI Pipeline**: All tests must pass
- **Code Coverage**: ≥95% coverage required
- **Type Checking**: MyPy strict mode
- **Linting**: Ruff formatting and linting
- **Security**: pip-audit for vulnerabilities
- **Conventional Commits**: Proper commit format

### Manual Checks

- **Code Review**: Minimum 2 approvals
- **Documentation**: Updated and accurate
- **Testing**: Comprehensive test suite
- **Performance**: No regressions
- **Security**: No vulnerabilities introduced

## Best Practices

### 1. Commit Message Quality

- Use conventional commit format
- Be descriptive and specific
- Include scope when relevant
- Reference issues when applicable

### 2. Branch Naming

- Use descriptive branch names
- Include issue numbers
- Follow consistent patterns
- Examples:
  - `feat/algorithms-binary-search`
  - `fix/security-vulnerability-123`
  - `docs/api-documentation-update`

### 3. Review Quality

- Be thorough and constructive
- Focus on code quality
- Consider security implications
- Test changes locally when possible

### 4. Communication

- Keep PR descriptions clear
- Respond to review comments promptly
- Provide context for decisions
- Update status regularly

## Troubleshooting

### Common Issues

1. **CI Failures:**
   - Check logs for specific errors
   - Fix issues locally first
   - Re-run CI after fixes

2. **Review Delays:**
   - Ping reviewers politely
   - Provide context for urgency
   - Consider breaking into smaller PRs

3. **Merge Conflicts:**
   - Resolve conflicts promptly
   - Test thoroughly after resolution
   - Get review for complex resolutions

4. **Version Conflicts:**
   - Coordinate with other contributors
   - Use semantic versioning
   - Update changelog appropriately

### Getting Help

- Check existing documentation
- Ask in PR comments
- Create issues for problems
- Reach out to maintainers

## Conclusion

Following this merge strategy ensures:
- Clean, maintainable git history
- Consistent quality standards
- Efficient collaboration
- Reliable releases
- Clear audit trail

Remember: Quality over speed. It's better to take time to do it right than to rush and create technical debt.
