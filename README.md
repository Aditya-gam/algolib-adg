# AlgoLib-ADG

[![CI](https://github.com/Aditya-gam/algolib-adg/actions/workflows/ci.yml/badge.svg)](https://github.com/Aditya-gam/algolib-adg/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/Aditya-gam/algolib-adg/branch/main/graph/badge.svg)](https://codecov.io/gh/Aditya-gam/algolib-adg)
[![PyPI version](https://badge.fury.io/py/algolib-adg.svg)](https://badge.fury.io/py/algolib-adg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python library of fundamental data structures and algorithms, built with a focus on clean code, SOLID principles, and robust testing.

## ✨ Features

A growing collection of classic algorithms and data structures, including:

**Data Structures:**
*   `Stack`: Last-In, First-Out (LIFO) stack implementation.
*   `Queue`: First-In, First-Out (FIFO) queue implementation.
*   `LinkedList`: Singly linked list.
*   `Graph`: Directed and undirected graph implementation with support for adjacency lists.
*   `DisjointSet`: Disjoint Set Union (DSU) or Union-Find data structure.

**Algorithms:**
*   **Sorting:**
    *   `BubbleSort`
    *   `MergeSort`
*   **Searching:**
    *   `LinearSearch`
    *   `BinarySearch` (for sorted sequences)
*   **Graph Traversal:**
    *   `bfs`: Breadth-First Search

## 🚀 Quick Start

Get started with `algolib` in just a few lines of code.

### Installation

The library is packaged with Poetry. To install it, you will need to add it as a dependency in your `pyproject.toml` or install it directly from the repository.

*(Note: Once published to PyPI, this will be `pip install algolib-adg`)*

### Example Usage

Here's a quick example of how to use the `Stack` data structure and `MergeSort` algorithm:

```python
from algolib.data_structures import Stack
from algolib.algorithms.sorting import MergeSort

# Using the Stack
print("--- Stack Example ---")
s = Stack[int]()
s.push(1)
s.push(2)
s.push(3)

print(f"Stack size: {s.size}")
print(f"Popped item: {s.pop()}")
print(f"Is stack empty? {s.is_empty()}")
print("-" * 20)


# Using MergeSort
print("--- MergeSort Example ---")
data_to_sort = [5, 2, 9, 1, 5, 6]
sorter = MergeSort[int]()
sorted_data = sorter.sort(data_to_sort)

print(f"Original list: {data_to_sort}")
print(f"Sorted list: {sorted_data}")
print("-" * 20)
```

## 🛠️ Development

We welcome contributions! Please follow these steps to set up a local development environment.

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Aditya-gam/algolib-adg.git
    cd algolib-adg
    ```

2.  **Install Poetry:**
    Follow the official instructions at [poetry.eustace.io](https://python-poetry.org/docs/#installation).

3.  **Install dependencies:**
    This command installs all main and development dependencies.
    ```bash
    poetry install --all-extras
    ```

### Running Checks

This project uses a suite of tools to ensure code quality.

*   **Linting and Formatting (Ruff):**
    ```bash
    # Check formatting
    poetry run ruff format --check .
    # Lint
    poetry run ruff check .
    ```

*   **Type Checking (mypy):**
    ```bash
    poetry run mypy --strict algolib tests
    ```

*   **Testing (pytest):**
    Run the full test suite with coverage.
    ```bash
    poetry run pytest --cov=algolib
    ```
    The CI pipeline requires a minimum of 95% test coverage.

### Pre-commit Hooks

This repository is configured with pre-commit hooks to automatically run checks before each commit. To install them, run:
```bash
poetry run pre-commit install
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feat/AmazingFeature`).
3.  Commit your changes using the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standard (`git commit -m 'feat(scope): some amazing feature'`).
4.  Push to the branch (`git push origin feat/AmazingFeature`).
5.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License.
