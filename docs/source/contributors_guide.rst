.. _contributors_guide:

===================
Contributor's Guide
===================

Thank you for your interest in contributing to AlgoLib-ADG! This guide provides everything you need to know to contribute effectively. We value high-quality contributions and have established clear standards to ensure the library remains clean, consistent, and maintainable.

.. contents::
   :local:
   :depth: 2

Our Core Principles
-------------------

Before you begin, please familiarize yourself with the principles that guide this project:

- **PEP 8 + Ruff**: We use `Ruff` for auto-formatting on every commit to maintain a consistent code style.
- **Strict Typing + mypy**: All code must pass strict `mypy` type-checking in CI to ensure type safety.
- **SOLID OOP**: We follow SOLID principles, emphasizing single responsibility and dependency on abstractions.
- **Clean Code (DRY / KISS)**: We strive for clear, concise code with meaningful names and minimal duplication.
- **Conventional Commits + SemVer**: Commit messages must follow the Conventional Commits specification. This drives our semantic versioning.
- **TDD with ≥ 95% Coverage**: All logic must be introduced via tests first. Our CI pipeline enforces a strict 95% test coverage minimum.
- **Secure-by-Default**: Dependencies are pinned and scanned for vulnerabilities. Secrets are never committed to the repository.

The Agent-Driven Workflow
-------------------------

Adding a new algorithm is not done by manually creating files. Instead, we use a special agent-driven workflow that guarantees consistency and quality. The process revolves around creating a YAML specification file.

Here’s how it works:

**Step 1: Create a Specification File**

1.  Navigate to the `specs/` directory.
2.  Copy the `template.yml` to a new file named after your algorithm (e.g., `Dijkstra.yml`).
3.  Edit your new YAML file, filling in all the required fields:
    -   `name`: The display name of the algorithm (e.g., "Dijkstra's Algorithm").
    -   `short_name`: The module name (e.g., `dijkstra`).
    -   `category`: The algorithm's category (e.g., `graph`).
    -   `short_description`: A brief, one-line summary.
    -   `long_description`: A detailed explanation of how the algorithm works.
    -   `complexity`: The Big O complexities for time and space (best, average, worst cases).
    -   `interfaces`: The abstract base classes the implementation will inherit from.
    -   `youtube_url` (optional): A link to an educational video.

**Step 2: Perform a Dry Run**

Before generating the files, perform a dry run to validate your specification and see the files that *will* be created.

.. code-block:: bash

   poetry run python scripts/run_algo_agent.py --dry-run specs/YourAlgorithm.yml

The agent will parse your spec, generate the Jinja2 templates, and print the planned file structure without writing anything to disk. Review the output carefully.

**Step 3: Run the Agent**

Once you are satisfied with the dry run, execute the agent to generate the files for real.

.. code-block:: bash

   poetry run python scripts/run_algo_agent.py specs/YourAlgorithm.yml

The agent will create the following artifacts:
- The algorithm implementation in `algolib/algorithms/...`
- A complete test suite in `tests/algorithms/...`
- A documentation page in `docs/source/algorithms/...`
- A performance benchmark file.

**Step 4: Implement the Logic and Tests**

The agent generates the boilerplate, but you must still implement the core algorithm logic and the specific test cases.

1.  **Write Tests First (TDD)**: Open the generated test file. Write failing tests that define the expected behavior of your algorithm.
2.  **Implement the Algorithm**: Open the generated implementation file and write the code to make your tests pass.
3.  **Ensure Full Coverage**: Run the tests with coverage and ensure you meet the 95% minimum.

   .. code-block:: bash

      poetry run pytest

Submitting Your Contribution
----------------------------

1.  **Commit Your Changes**: Use a Conventional Commit message. For a new algorithm, the format should be `feat(search): add dijkstra algorithm`.
2.  **Run Pre-Commit Hooks**: The commit will trigger pre-commit hooks that format, lint, and type-check your code. Fix any issues that arise.
3.  **Push and Open a Pull Request**: Push your feature branch to the repository and open a pull request against the `main` branch.
4.  **Verify CI Checks**: Ensure all CI checks pass. Your PR will not be reviewed or merged otherwise.
