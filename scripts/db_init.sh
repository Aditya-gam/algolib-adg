#!/bin/bash
set -e

# Ensure we're in the right directory
cd "$(dirname "$0")/.."

# Debug information
echo "Current directory: $(pwd)"
echo "Poetry version: $(poetry --version)"
echo "Python version: $(poetry run python --version)"

# Check if alembic is available in the Poetry environment
if ! poetry run alembic --version > /dev/null 2>&1; then
    echo "Error: alembic is not available in the Poetry environment"
    echo "Installed packages:"
    poetry run pip list | grep -i alembic || echo "No alembic found in pip list"
    exit 1
fi

echo "Alembic version: $(poetry run alembic --version)"

# Apply database migrations
echo "Running database migrations..."
poetry run alembic upgrade head
echo "Database migrations completed successfully"
