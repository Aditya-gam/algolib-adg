# AlgoLib-ADG

[![CI](https://github.com/Aditya-gam/algolib-adg/actions/workflows/ci.yml/badge.svg)](https://github.com/Aditya-gam/algolib-adg/actions/workflows/ci.yml)
[![Docs](https://github.com/Aditya-gam/algolib-adg/actions/workflows/docs.yml/badge.svg)](https://github.com/Aditya-gam/algolib-adg/actions/workflows/docs.yml)
[![Agent Success](https://img.shields.io/badge/Agent-Passing-brightgreen)](https://github.com/Aditya-gam/algolib-adg/actions/workflows/agent.yml) <!-- TODO: Update with real workflow -->
[![codecov](https://codecov.io/gh/Aditya-gam/algolib-adg/branch/main/graph/badge.svg)](https://codecov.io/gh/Aditya-gam/algolib-adg)
[![PyPI version](https://badge.fury.io/py/algolib-adg.svg)](https://badge.fury.io/py/algolib-adg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AlgoLib-ADG** is a Python library of fundamental data structures and algorithms, uniquely built using an **AI-powered agentic workflow**. It combines classic computer science with cutting-edge automation, ensuring high-quality, well-tested, and fully documented code.

## ✨ Features

*   **🤖 AI-Powered Development**: Algorithms are generated, tested, and documented by an autonomous AI agent from simple YAML specifications.
*   **📚 Comprehensive Library**: A growing collection of classic algorithms and data structures.
*   **✅ Strictly Typed & Tested**: Enforced static typing with `mypy` and a test coverage requirement of over 95%.
*   **🧼 Clean Code & SOLID Principles**: Adherence to `PEP 8`, `SOLID` design, and `Clean Code` practices (DRY/KISS).
*   **⚙️ Automated Quality Gates**: A robust CI pipeline validates every change with linting, type-checking, testing, and documentation builds.
*   **📦 Modern Tooling**: Built with Poetry, Ruff, Pytest, and Sphinx.

## 🤖 Add a New Algorithm in Three Steps

Our AI agent makes contributing new algorithms incredibly simple.

1.  **Define the Spec**: Copy `specs/template.yml` to `specs/YourAlgorithm.yml` and fill in the details: name, description, complexity, etc.

    ```yaml
    # specs/MyAwesomeSort.yml
    name: "My Awesome Sort"
    category: "Sorting"
    description: "A revolutionary sorting algorithm."
    # ... and other fields
    ```

2.  **Commit & Push**: Commit the new spec file. The AI agent takes over from here.
    ```bash
    git add specs/MyAwesomeSort.yml
    git commit -m "feat(sorting): add spec for My Awesome Sort"
    git push
    ```

3.  **Review the PR**: The agent will generate the code, tests, and documentation, then open a Pull Request. Review the generated files, and once all checks pass, merge it.

That's it! The agent handles the boilerplate, letting you focus on the algorithm's design.

## 🚀 Local Development

While the agent handles most of the work, you can also run it locally.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Aditya-gam/algolib-adg.git
    cd algolib-adg
    ```

2.  **Install dependencies with Poetry:**
    ```bash
    poetry install --all-extras
    ```

3.  **Set up pre-commit hooks:**
    This is essential for ensuring your spec file is valid before committing.
    ```bash
    poetry run pre-commit install
    ```

### Running the Agent Locally

You can test the generation process without committing using the `--dry-run` flag. This is useful for validating your spec file and seeing the generated output.

```bash
# Example: Run the agent for the BubbleSort spec
poetry run python scripts/run_algo_agent.py --dry-run specs/BubbleSort.yml
```
The generated files will be placed in the `.agent-tmp/` directory for your review.

## Running Tests

To run the full test suite, including coverage analysis:

```bash
poetry run pytest
```

## Database

This project uses PostgreSQL as its database, managed with `SQLModel` and `Alembic`. The entire database setup is containerized using Docker.

### Initializing the Database

To create the database and apply all migrations, first ensure Docker is running, then run the following commands:

```bash
# Start the PostgreSQL container
docker-compose up -d db

# Apply migrations
docker-compose exec api poetry run alembic upgrade head
```

You can also use the provided script to apply migrations after the container is running:

```bash
./scripts/db_init.sh
```

---

## 🤝 Contributing

We welcome all contributions! Please see the `CONTRIBUTING.rst` file for more detailed instructions on our development standards and workflow.

## 📄 License

This project is licensed under the MIT License.
