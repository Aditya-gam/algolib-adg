Contributing to Algolib
======================

Welcome to Algolib! This document outlines the contribution process, coding standards, and review guidelines.

Getting Started
--------------

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch** from `main`
4. **Make your changes** following our standards
5. **Test thoroughly** before submitting
6. **Submit a pull request** following our template

Coding Standards
---------------

We follow strict coding standards to maintain code quality:

**PEP 8 + Ruff**
- Auto-format on every commit
- Consistent style across the codebase
- Line length: 100 characters
- Use `poetry run ruff format .` to format code

**Strict Typing + MyPy**
- All code must have proper type hints
- MyPy strict mode enforced in CI
- No `Any` types without justification
- Use `typing_extensions` for advanced types

**SOLID OOP Principles**
- Single Responsibility: One class, one purpose
- Open/Closed: Open for extension, closed for modification
- Liskov Substitution: Subtypes are substitutable
- Interface Segregation: Small, focused interfaces
- Dependency Inversion: Depend on abstractions

**Clean Code (DRY/KISS)**
- Don't Repeat Yourself: Extract common functionality
- Keep It Simple, Stupid: Clear, readable code
- Small functions (≤20 lines)
- Descriptive names
- No magic numbers or strings

**Conventional Commits**
- Format: `type(scope): description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Scope: `algorithms`, `data-structures`, `ci`, etc.
- Breaking changes: Add `!` after type

Example: `feat(algorithms): add binary search implementation`

Testing Standards
----------------

**Test-Driven Development (TDD)**
- Write tests first
- Red-Green-Refactor cycle
- ≥95% coverage required
- CI blocks on coverage regression

**Test Types**
- Unit tests for individual functions
- Integration tests for components
- Property-based tests for algorithms
- Performance benchmarks for critical paths

**Test Structure**
```python
def test_function_name_should_do_something():
    """Test description of what the test verifies."""
    # Arrange
    input_data = ...
    expected = ...

    # Act
    result = function(input_data)

    # Assert
    assert result == expected
```

Review Process
-------------

**Pull Request Workflow**

1. **Create Draft PR**: Start with draft status
2. **Self-Review**: Check your own code first
3. **CI Checks**: Ensure all automated checks pass
4. **Ready for Review**: Mark PR as ready when complete
5. **Review Process**: Address reviewer feedback
6. **Merge**: Only when all requirements are met

**Required Reviews**

- **Minimum 2 approvals** from maintainers
- **Code owner review** required for sensitive areas
- **All CI checks must pass**
- **No merge conflicts**

**Review Checklist**

As a reviewer, check for:

✅ **Code Quality**
- Follows PEP 8 and project style
- Proper type hints and MyPy compliance
- SOLID principles applied
- Clean, readable code

✅ **Testing**
- Adequate test coverage (≥95%)
- Tests are meaningful and well-written
- Property-based tests for algorithms
- Performance tests where appropriate

✅ **Documentation**
- Clear docstrings for all public APIs
- Updated README/docs if needed
- Inline comments for complex logic
- Examples in docstrings

✅ **Security**
- No obvious security vulnerabilities
- Input validation where needed
- No hardcoded secrets
- Proper error handling

✅ **Performance**
- Efficient algorithms and data structures
- No obvious performance issues
- Benchmarks for critical paths
- Memory usage considerations

**Review Guidelines**

1. **Be Constructive**: Provide specific, actionable feedback
2. **Focus on Code**: Review the code, not the person
3. **Ask Questions**: Clarify unclear implementations
4. **Suggest Improvements**: Offer specific alternatives
5. **Check Standards**: Verify compliance with project standards
6. **Test Locally**: When possible, test changes locally

**Review Comments**

Use these prefixes for review comments:

- `nit:` Minor style or formatting issues
- `suggestion:` Optional improvements
- `blocker:` Must be fixed before merge
- `question:` Seeking clarification
- `praise:` Positive feedback

Example:
```
nit: Consider using a more descriptive variable name here
suggestion: This could be simplified using list comprehension
blocker: This will cause a runtime error when input is None
question: Why do we need this additional check?
praise: Great use of type hints here!
```

**Addressing Review Comments**

1. **Acknowledge**: Respond to each comment
2. **Fix**: Make necessary changes
3. **Explain**: Provide context for decisions
4. **Push**: Update the PR with fixes
5. **Re-request**: Ask for re-review when ready

Merge Requirements
-----------------

**Before Merge**

- [ ] **Draft Status**: PR is ready for review (not draft)
- [ ] **CI Green**: All CI checks are passing
- [ ] **Reviews Complete**: Required number of approvals received
- [ ] **No Conflicts**: Branch can be merged without conflicts
- [ ] **Documentation**: All changes are properly documented

**Merge Strategies**

- **Squash and Merge**: For feature branches with multiple commits
- **Rebase and Merge**: For clean, linear history when appropriate
- **Create Merge Commit**: For complex changes requiring detailed history

**Post-Merge**

- [ ] **Version Bump**: Update version in `pyproject.toml` if needed
- [ ] **Changelog**: Update `CHANGELOG.md` with changes
- [ ] **Release Notes**: Create release notes for significant changes
- [ ] **Cleanup**: Delete feature branch after successful merge

Algorithm Implementation Guidelines
---------------------------------

**For New Algorithms**

1. **Specification**: Create `specs/AlgorithmName.yml`
2. **Implementation**: Follow the algorithm template
3. **Tests**: Include unit and property-based tests
4. **Documentation**: Add comprehensive docstrings
5. **Benchmarks**: Include performance benchmarks
6. **Integration**: Ensure it works with existing systems

**Algorithm Standards**

- Implement the appropriate interface from `algolib.interfaces`
- Include complexity analysis in docstrings
- Provide usage examples
- Handle edge cases gracefully
- Optimize for common use cases

Data Structure Guidelines
------------------------

**For New Data Structures**

1. **Interface**: Implement the appropriate interface
2. **Tests**: Include comprehensive test suite
3. **Documentation**: Document complexity and usage
4. **Performance**: Include benchmarks
5. **Integration**: Work with existing algorithms

**Data Structure Standards**

- Follow the established patterns
- Implement all required methods
- Provide clear documentation
- Include performance characteristics
- Handle edge cases properly

Security Guidelines
------------------

**General Security**

- Never commit secrets or sensitive data
- Use environment variables for configuration
- Validate all inputs
- Handle errors gracefully
- Follow the principle of least privilege

**Dependency Security**

- Keep dependencies updated
- Use `pip-audit` to check for vulnerabilities
- Pin dependency versions in `poetry.lock`
- Review security advisories regularly

Performance Guidelines
---------------------

**Algorithm Performance**

- Document time and space complexity
- Include benchmarks for critical paths
- Optimize for common use cases
- Consider memory usage
- Profile when necessary

**Code Performance**

- Use appropriate data structures
- Avoid unnecessary computations
- Profile performance-critical code
- Consider caching where appropriate
- Monitor memory usage

Getting Help
-----------

- **Issues**: Create GitHub issues for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Documentation**: Check existing docs first
- **Code Review**: Ask questions in PR reviews

Thank you for contributing to Algolib! 🚀
