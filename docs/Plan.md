### Algorithm Library & Docs Showcase

_A clean-code, agent-augmented reference library of classic algorithms, backed by rigorous tests, rich documentation, and an automated CI/CD pipeline._

---
## 1. Vision & Purpose
Modern learners—and hiring managers—judge a codebase by its readability, testability, and maintainability. Most algorithm repositories fail that test. This project bridges the gap by delivering:
- **A production-grade Python library** that implements foundational data-structures and algorithms using SOLID OOP, type hints, and docstrings.
- **>95 % unit-test coverage** with property-based and performance tests that guard against regressions.
- **Zero-touch docs & demo deployment** (Sphinx-generated API docs on GitHub Pages + Streamlit playground).
- **An Agentic-AI workflow** that converts concise YAML specs into ready-to-merge pull requests—code, tests, docs, and benchmarks included.

The result is both a teaching resource and a live demonstration of next-generation developer tooling.

---
## 2. High-Level Objectives
1. **Code Quality**
    - 100 % PEP 8 compliant (enforced by _Black_, _isort_, _Flake8_, _ruff_).
    - ≥ 95 % line coverage; ≤ 0.5 % branch misses on `main`.
    - Strict type checking with _mypy_ (CI gate).
    
2. **Developer Experience**
    - One-command setup via **Poetry** (or `pip-tools`) and _pre-commit_ hooks.
    - GitHub Actions pipeline that executes lint → type-check → tests → benchmark → Sphinx build.
    - Badges for build status, coverage, and docs health.
    
3. **Documentation & Demo**
    - Auto-generated API docs (Sphinx + _furo_ theme) published to GitHub Pages.
    - Rich narrative pages: algorithm intuition, complexity analysis, ASCII/PlantUML diagrams.
    - Interactive Streamlit app letting visitors run algorithms and visualise steps.
    
4. **Agentic-AI Integration** _(Phase 0.5)_
    - LangChain-driven **Algo-Agent** that reads YAML specs (`/specs/*.yml`) and produces:
        - `algolib/…` implementation class
        - `tests/test_<algo>.py` with exhaustive cases & property tests
        - Sphinx reStructuredText page with explanation + complexity table
        - `benchmarks/test_<algo>.py` for `pytest-benchmark`
        
    - Action triggers on push to `specs/`, commits generated code to a feature branch, opens an auto-PR, and comments if coverage / lint fail.
---
## 3. Architecture & Tooling
```text
algolib/
├── algorithms/
│   ├── sorting/
│   │   ├── base.py          # BaseAlgorithm ABC
│   │   ├── bubble_sort.py
│   │   └── merge_sort.py
│   └── graph/
│       ├── traversal/
│       │   └── bfs.py
│       └── shortest_path/
│           └── dijkstra.py
├── data_structures/
│   └── graph.py             # Adjacency-list Graph class
├── __init__.py
tests/
benchmarks/
docs/                         # Sphinx source
specs/                        # YAML algorithm specs for the Agent
agent_tools/                  # CodeWriter, TestWriter, DocWriter, BenchRunner
spec_builder/                 # Streamlit components for interactive YAML authoring
.streamlit/
.github/workflows/ci.yml
pyproject.toml
```
_The `spec_builder` package is a thin Streamlit + pyyaml front-end that validates a user-filled form, writes the YAML file into `/specs/`, and pushes a `spec-builder/<slug>` branch so the **Algo-Agent** workflow can pick it up._
- **Python 3.11** target; use `typing` generics and `match` where appropriate.
- **Testing:** `pytest`, `hypothesis`, `pytest-benchmark`.
- **Formatting & Linting:** _Black_, _isort_, _ruff_, _Flake8_ (complexity plugins).
- **Docs:** Sphinx, _autodoc_, _napoleon_, _autodoc-typehints_, _furo_ theme.
- **CI/CD:** GitHub Actions matrix (`ubuntu-latest`, `macos-latest`), Poetry caching, parallel jobs, Codecov upload, gh-pages publish.
- **Public Demo:** Streamlit Cloud or Vercel (`/app.py`) serving both the Algorithm Playground and Spec Builder.
---
## 4. Phased Roadmap
### Phase 0 — Project Bootstrap _(½ day)_
1. Create GitHub repo (`algolib-adg`).
2. Configure _Poetry_ environment, `pyproject.toml` with `tool.black`, `tool.isort`, `tool.pytest.ini_options`.
3. Add pre-commit hooks (black, isort, flake8, mypy).
4. Write minimal `BaseAlgorithm` ABC + stub modules.
5. Set up CI workflow running lint → type → tests → docs. Green build required before merge.
### Phase 0.5 — Agentic-AI Extension _(≈ 2 days, parallel — replaces old Phase 0.5)_
1. **Spec schema** gains a mandatory `dependencies:` array listing any framework interfaces required (e.g. `Sorter`, `Graph`, `DisjointSet`).
2. Implement **CodeWriter**, **TestWriter**, **DocWriter**, **BenchRunner** (safe edits via `ast` + `astor`).
3. Build LangChain Agent (ReAct, structured-tool pattern) targeting **GPT-4o-mini** or local **OpenHermes-2.5**.
4. GitHub Action `algo-agent.yml` triggers on pushes to `specs/*` _or_ `spec-builder/*`, runs the Agent, and opens `agent/<algo>` PRs.
5. **Interface-Compliance Check:** CI fails if generated code re-implements or mutates any core classes authored in Phase 1.
6. **Success metric:** ≥ 80 % of new specs merge green on the first PR attempt.

_Example amended spec file (Bubble Sort):_
```yaml
name: BubbleSort
category: sorting
dependencies: [Sorter]
stability: deterministic
complexity:
  worst: O(n^2)
  avg:  O(n^2)
  best: O(n)
description: >
  Repeatedly steps through the list, compares adjacent items, and swaps when out of order.
benchmark_input: random_int_list
references:
  - CLRS 3rd Edition, §2.1
```
### Phase 1 — Core Library _(1½ days)_
Implement **five algorithms** with full OOP wrappers & type hints:

| Category       | Artefact                 | Purpose in Framework                    | Key Classes                 |
| -------------- | ------------------------ | --------------------------------------- | --------------------------- |
| Data Structure | **Stack**                | LIFO container for algorithms/backtrack | `Stack[T]`                  |
| Data Structure | **Queue**                | FIFO container for BFS                  | `Queue[T]`                  |
| Data Structure | **LinkedList**           | Node pattern & iterator demo            | `LinkedList[T]`, `_Node[T]` |
| Data Structure | **Graph**                | Base for all graph algorithms           | `Graph`, `Vertex`           |
| Data Structure | **DisjointSet**          | Needed by Kruskal/Union-Find            | `DisjointSet`               |
| Search         | **LinearSearch**         | Baseline; validates `Searcher` iface    | `Searcher`, `LinearSearch`  |
| Search         | **BinarySearch**         | Divide-and-conquer example              | `BinarySearch`              |
| Sort           | **BubbleSort**           | Simple Strategy pattern seed            | `Sorter`, `BubbleSort`      |
| Sort           | **MergeSort**            | Template-Method pattern seed            | `MergeSort`                 |
| Graph Algo     | **Breadth-First Search** | Traversal scaffold                      | `BFS`                       |
_Deliverables_: full type hints, Google-style docstrings, 100 % unit tests, property tests, ≥ 95 % coverage.
### Phase 2 — Testing & Documentation _(1 day)_
- Exhaustive unit tests: edge cases (empty list, single-element, duplicates), property-based checks for idempotence & stability.
	
- Configure `pytest --cov=algolib --typeguard-packages=algolib`. Coverage gate ≥ 95 %.
	
- Create Sphinx docs:
    - `index.rst`, `usage/quickstart.rst`, `algorithms/sorting/bubble_sort.rst`, …
    - Include diagrams via PlantUML (rendered by Sphinx-contrib-plantuml).
    
- Deploy to GitHub Pages (`gh-pages` branch).
### Phase 3 — Public Showcase _(1 day — replaces old Phase 3)_
1. **Algorithm Playground**
    - Sidebar → select category & algorithm.
    - Dynamic input widgets (array editor, graph builder).
    - Visual output (matplotlib chart or NetworkX graph) plus time-complexity badge.
    
2. **Spec Builder**
    - Form: algorithm name, category, complexity fields, _dependencies_ multiselect.
    - **On Submit:**
        1. Write YAML into `/specs/` on a new `spec-builder/<slug>` branch.
        2. Push branch and auto-open PR via GitHub API.
        3. Display PR link and live CI status; refresh algorithm list when merged.

Both pages live in the same Streamlit workspace; the sidebar toggles between **Playground** and **Create New Algorithm**.
Deployed to Streamlit Cloud with status badge and docs link in README & navbar.

---
## 5. Agentic-AI Feature Backlog
1. **Custom Spec Ingestion** – fully supported via Spec Builder UI.
    
2. **Interface-Compliance Checker** — enforced in Phase 0.5 CI gate.
	
3. **Auto-Explain & Diagram Agent** (Phase 2+)
    - After merge, run algorithm on sample data, ask LLM for natural-language explanation & PlantUML sequence/state diagram.
    - Commit artefacts to `docs/auto-explain/<algo>.rst`.
    
4. **Performance-Regression Agent** (Phase 3+)
    - Parse latest `pytest-benchmark` JSON; post PR comment if current run >10 % slower than `main`.
    - Suggest micro-optimisations with annotated diff.
---
## 6. Quality Gates & Metrics

|Metric|Threshold|Enforcement|
|---|---|---|
|**Coverage**|≥ 95 %|`pytest-cov` + CI fail|
|**Lint**|0 errors|Flake8 & ruff in CI|
|**Type Safety**|0 `error:` lines|mypy strict mode|
|**Agent Success**|80 % specs pass on first PR|CI status + dashboard|
|**Docs Build**|100 % success|`sphinx-build -b html` in CI|
|**Demo Uptime**|24 × 7 green|Streamlit health-check badge|

---
## Tech Stack
Using MacOS on MacBook 2 Pro

| Layer                                     | Tool(s)                                             | Why It’s the Best Fit                                                                                           |
| ----------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Dependency & Packaging**                | **Poetry ≤ 1.8**                                    | • Lock-file reproducibility across macOS/Linux• `poetry build/publish` for PyPI once project matures            |
| **Formatting & Lint**                     | **Ruff** (`lint` + `format`)                        | • One binary replaces Black, isort, Flake8 → 10-20× faster CI• Minimal config drift                             |
| **Static Typing**                         | **mypy** (CI) + Pyright (IDE)                       | • mypy’s strict mode catches generics / Protocol issues• Pyright offers instant IDE feedback without slowing CI |
| **Testing & Property-Based**              | **pytest** + **hypothesis** + **pytest-benchmark**  | • Familiar DSL + shrinking counter-examples• Benchmark plugin emits JSON your agent can parse                   |
| **Performance Regression Gate**           | **pytest-benchmark** + custom GitHub Action comment | • No external telemetry; compare JSON to last successful run                                                    |
| **Documentation Site**                    | **Sphinx 7 + furo theme**                           | • Autodoc pulls docstrings; PlantUML diagrams; built-in search                                                  |
| **Local LLM Serving**                     | **Ollama 0.23+**                                    | • Runs GGUF/ggml models on CPU/GPU• `openhermes-2.5-mistral` or **CodeGeeX-4k-Instruct** for code               |
| **Agent Framework**                       | **LangChain** → **LangGraph** (incremental)         | • Rapid prototyping of tool-calling in LangChain• Port mature chains to LangGraph for DAG determinism           |
| **Agent Execution Runner**                | **agent_tools/** (CodeWriter, TestWriter, …)        | • Thin wrappers using AST to ensure deterministic edits                                                         |
| **User-Facing Playground & Spec Builder** | **Streamlit 1.38**                                  | • 1-click deploy on _Streamlit Community Cloud_ (free)• Sidebar navigation between algorithms & builder UI      |
| **Continuous Integration / Delivery**     | **GitHub Actions**                                  | • 2 000 free Linux minutes/month; macOS for furo screenshots• Pages deploy for Sphinx docs                      |
| **Coverage Reporting**                    | **Codecov Bash Uploader**                           | • Still free for OSS; integrates with Actions.                                                                  |
| **Badges & Shields**                      | **shields.io**                                      | • README shows CI, coverage, docs, Streamlit health-check                                                       |

|Model|Context Window|Strengths|RAM / VRAM Needs|
|---|---|---|---|
|**`openhermes-2.5-mistral`**|8 k|Balanced reasoning & code-gen; trained with function-calling samples|10 GB RAM CPU-only; 6 GB VRAM for GPU|
|**`mistral-7b-instruct-v0.3`**|8 k|Fast; good for quick YAML-to-code stubs|8 GB RAM|
|**`codegeex-4k-instruct`**|4 k|Code-centric; fewer hallucinations in Python snippets|8 GB RAM|
|**`phi-3-mini-4k-instruct`**|4 k|Extremely small; use for integration tests to speed CI|5 GB RAM|

---
## 7. Risk Management
- **Scope Creep** — Lock v1.0 to five algorithms; all others via agent backlog.
- **LLM Hallucinations** — AST validation + CI tests stop bad code.
- **Token Cost** — Default to local model for bulk generation; reserve GPT-4o for complex tasks.
- **Demo Downtime** — Keep Streamlit stateless; add simple retry & cache.
---
## 8. Stretch Enhancements
- **Data-Structures**: Red-Black Tree, Heap, Union-Find.
- **Dynamic Programming**: 0/1 Knapsack, Edit Distance.
- **Search**: A* with heuristic pluggability.
- **Packaging**: Publish to PyPI (`pip install algolib-adg`), include wheels and `type:` hints.
- **API Service**: FastAPI micro-service exposing `/sort` (POST list) and `/shortest-path` (POST graph).
- **Multi-Language Output**: Extend Agent to emit Java (`algolib-java`), using `javalang` for AST safety.
- **Self-Tuning Benchmarks**: Agent iteratively optimises until benchmark delta < threshold.
---
## 9. Résumé / Portfolio Highlight
> **Built** a production-quality Python algorithm library with SOLID class design, _98 % test coverage_ and fully auto-generated Sphinx docs. **Integrated** a LangChain “junior-dev” agent that converts YAML specs into ready-to-merge PRs—cutting human boilerplate by 60 %. Deployed searchable docs (GitHub Pages) and a Streamlit playground for live algorithm visualisation.
---
## 10. Live Demo & Interview Story
- Show the Streamlit UI sorting a random list, then switch to Dijkstra on a sample graph.
- Walk through an auto-generated PR: spec → agent tools output → CI green → merge.
- Discuss prompt-engineering, AST safety nets, and how CI enforces determinism.