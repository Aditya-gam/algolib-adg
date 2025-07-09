## 0.2.0 (2025-07-08)

### Feat

- **docs**: add dedicated docs deployment workflow
- **testing**: enable property-based testing with Hypothesis

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
