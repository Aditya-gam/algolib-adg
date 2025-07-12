## v0.2.5 (2025-07-12)

### BREAKING CHANGE

- Benchmarking and coverage are now fully separated in CI and local workflows.
- Directory and import structure for algorithms and data structures has changed. See docs for migration details.

### Feat

- **ci**: implement CI & pre-commit pipeline updates
- **benchmarks**: add detailed benchmark harness for merge, quick, heap sort and Dijkstra
- **runtime**: add runtime checks and property-based tests
- **core**: major refactor and expansion of core algorithm/data-structure library
- **scaffolding**: Add core interfaces and directory structure
- **docs**: add PlantUML tooling and developer UX updates
- **docs**: add dedicated docs deployment workflow
- **testing**: enable property-based testing with Hypothesis

### Fix

- resolve quick sort recursion error in benchmarks and improve fallback comparison logic
- **docs**: add missing docs group to poetry for CI compatibility
- **core/scripts**: ensure commit message scripts and config pass strict typing, ruff, and pre-commit
- **api**: add requests dependency to resolve ModuleNotFoundError in CI
- **db/session**: lazy engine creation and type annotations for mypy strict mode
- **ci**: resolve alembic not found error in CI pipeline
- **ci**: migrate commitlint config to ES module format
- **ci**: improve auto-label error handling and permissions for draft PR workflow
- **ci**: add GitHub Actions permissions for draft PR management
- **ci**: resolve alembic command not found error in database initialization
- **pyproject**: resolve Poetry config errors, unify classic [tool.poetry] format, and ensure CI compatibility\n\n- Move all metadata and dependencies to [tool.poetry]\n- Remove [project] section\n- Add python version constraint to dependencies\n- Update poetry.lock\n- Pass pre-commit, mypy, ruff, and all checks
- **ci**: Resolve pytest collection warning

### Refactor

- improve code quality and maintainability across multiple modules

## v0.1.0 (2025-07-08)

### Feat

- **core**: domain interfaces, refactor algorithms, docs badge
- **core**: Refactor data structures and algorithms with protocols
- **core**: define and export domain interface protocols
- **ci**: add database service and smoke tests
- **api**: initialize FastAPI app with DB health check
- **db**: bootstrap database with SQLModel and Alembic
- **devops**: implement docker-compose for local development
- **deps**: revamp poetry configuration and dependencies
- **deps**: add FastAPI, SQLModel, and related dependencies
- **deps**: revamp poetry dependencies and pre-commit hooks

### Fix

- **ci**: resolve coverage and dependency issues
- **ci**: resolve coverage and dependency issues
- **ci**: provide model to ollama pull in agent workflow

## v0.2.0 (2025-07-04)

### BREAKING CHANGE

- Algorithm base classes moved from algorithms.base to algorithms.searching.base and algorithms.sorting.base

### Feat

- **agent**: implement intelligent and sandboxed self-correction loop
- **agent**: implement self-correction loop
- **agent**: add pip-audit and run smoke test
- **ci**: add GitHub Action for autonomous agent
- **ci**: add interface compliance check
- **agent**: create agent orchestration script
- **agent**: scaffold agent_tools file generation pipeline
- **agent**: scaffold agent tools and writers
- **specs**: implement extensible algorithm spec format
- **agentic-ai**: add ollama and langchain dev dependencies
- **core**: implement stack, queue, linked list, graph, disjoint-set, searches, sorts, bfs
- **api**: Expose public data structures and algorithms
- **testing**: Implement property-based tests and refactor graph algorithms
- **graph**: Implement Breadth-First Search (BFS) algorithm\n\n- Implement `BFS` class with `traverse` method in `algolib/algorithms/graph/traversal/bfs.py`.\n- Add `get_neighbors` method to `Graph` class in `algolib/data_structures/graph.py` to support graph traversal.\n- Add comprehensive test suite for `BFS` in `tests/algorithms/graph/traversal/test_bfs.py`, including 22 test cases covering various graph topologies and edge cases.\n- Refactor `tests/data_structures/test_graph.py` to improve test coverage to 100% and fix `ruff` E711 error.\n- Fix `test_linear.py` assertions to correctly reflect linear search behavior with comparable objects.\n- Address `mypy` type hinting errors in `algolib/algorithms/graph/traversal/bfs.py` and `tests/algorithms/graph/traversal/test_bfs.py`.
- **core**: implement foundational data structures and algorithms
- **bootstrap**: poetry, ruff, mypy, base skeleton & CI

### Fix

- **agent**: overhaul all generation templates
- **agent**: overhaul code generation template for correctness
- **agent**: switch to llama3.1 for tool support
- **ci**: correct poetry installation and caching in workflow
- **ci**: Resolve mypy path conflicts and type errors
- **mypy**: Configure pre-commit hook to resolve path issues

### Refactor

- **agent**: allow running agent on specific spec files
- **agent**: remove openai and default to ollama
- **agent**: integrate LangChain for orchestration
- restructure algorithms module with dedicated base classes and comprehensive tests
