"""Tests for the API module."""

from typing import Generator
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError

from algolib.api.main import app
from algolib.db.session import get_session


@pytest.fixture
def client() -> TestClient:
    """Return a TestClient instance for the app."""
    return TestClient(app)


def test_health_db_ok(client: TestClient) -> None:
    """Test the /health/db endpoint when the database is available."""

    def mock_get_session_ok() -> Generator[MagicMock, None, None]:
        """Mock session that executes successfully."""
        mock_sess = MagicMock()
        mock_sess.execute.return_value = None
        yield mock_sess

    app.dependency_overrides[get_session] = mock_get_session_ok

    response = client.get("/health/db")
    assert response.status_code == 200
    assert response.json() == {"db": "ok"}

    app.dependency_overrides = {}


def test_health_db_fail(client: TestClient) -> None:
    """Test the /health/db endpoint when the database is unavailable."""

    def mock_get_session_fail() -> Generator[MagicMock, None, None]:
        """Mock session that raises an error."""
        mock_sess = MagicMock()
        mock_sess.execute.side_effect = SQLAlchemyError("Connection failed")
        yield mock_sess

    app.dependency_overrides[get_session] = mock_get_session_fail

    response = client.get("/health/db")
    assert response.status_code == 200
    assert response.json() == {"db": "fail"}

    app.dependency_overrides = {}
