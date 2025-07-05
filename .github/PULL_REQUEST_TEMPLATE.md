---
name: New Feature/Fix
about: Propose a change to the repository
title: 'feat: '
labels: ''
assignees: ''

---

### Description

A clear and concise description of what the pull request does.

### Related Issue

Please link to the issue this PR addresses.

### Algorithm Specification

If this PR implements a new algorithm, please cite the `spec.yml` file.

**Example:** `specs/BubbleSort.yml`

### Contributor Checklist

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
