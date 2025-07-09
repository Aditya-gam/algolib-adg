.PHONY: help dev down diagrams test-all

help:
	@echo "Commands:"
	@echo "  dev         : Start the Docker Compose stack with a build."
	@echo "  down        : Stop and remove the Docker Compose stack."
	@echo "  diagrams    : Generate diagrams from PlantUML files."
	@echo "  test-all    : Run the full test suite, including property tests."

diagrams:
	@find docs/uml -name '*.puml' -exec java -jar tools/plantuml.jar -tpng {} +
	@find docs/uml -name '*.puml' -exec java -jar tools/plantuml.jar -tsvg {} +

test-all:
	@poetry run pytest

dev: ## start compose stack
	docker-compose up --build
down:
	docker-compose down -v
