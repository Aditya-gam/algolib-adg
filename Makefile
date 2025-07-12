.PHONY: help dev down diagrams test-all quality-gate

help:
	@echo "Commands:"
	@echo "  dev         : Start the Docker Compose stack with a build."
	@echo "  down        : Stop and remove the Docker Compose stack."
	@echo "  diagrams    : Generate diagrams from PlantUML files."
	@echo "  test-all    : Run the full test suite, including property tests."
	@echo "  quality-gate: Run all quality checks (lint, type-check, tests, coverage)."

diagrams:
	@find docs/uml -name '*.puml' -exec java -jar tools/plantuml.jar -tpng {} +
	@find docs/uml -name '*.puml' -exec java -jar tools/plantuml.jar -tsvg {} +

test-all:
	@poetry run pytest

quality-gate:
	@echo "Running quality gate checks..."
	@poetry run ruff format --check .
	@poetry run ruff check .
	@poetry run mypy --strict algolib tests
	@poetry run pytest --cov=algolib --cov-fail-under=95 --cov-report=term-missing -m "not benchmark"
	@echo "✅ All quality gate checks passed!"

dev: ## start compose stack
	docker-compose up --build
down:
	docker-compose down -v
