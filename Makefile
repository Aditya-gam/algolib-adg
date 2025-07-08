.PHONY: help dev down

help:
	@echo "Commands:"
	@echo "  dev         : Start the Docker Compose stack with a build."
	@echo "  down        : Stop and remove the Docker Compose stack."

dev: ## start compose stack
	docker-compose up --build
down:
	docker-compose down -v
