#!/bin/bash
set -e

# Apply database migrations
poetry run alembic upgrade head
