"""Tests for database session management."""

import os
from unittest.mock import patch

import pytest
from sqlmodel import Session


class TestDatabaseSession:
    """Test database session creation and management."""

    def test_get_session_success(self) -> None:
        """Test successful session creation."""
        with patch.dict(os.environ, {"DATABASE_URL": "sqlite:///test.db"}):
            from algolib.db.session import get_session

            session_gen = get_session()
            session = next(session_gen)
            assert isinstance(session, Session)
            try:
                next(session_gen)
            except StopIteration:
                pass

    def test_empty_database_url_raises_value_error(self) -> None:
        """Test that empty DATABASE_URL raises ValueError."""
        with patch.dict(os.environ, {"DATABASE_URL": ""}):
            import sys

            if "algolib.db.session" in sys.modules:
                del sys.modules["algolib.db.session"]
            with pytest.raises(ValueError, match="DATABASE_URL environment variable not set"):
                import algolib.db.session  # noqa: F401

    def test_none_database_url_raises_sqlalchemy_error(self) -> None:
        """Test that 'None' DATABASE_URL raises SQLAlchemy ArgumentError."""
        with patch.dict(os.environ, {"DATABASE_URL": "None"}):
            import sys

            if "algolib.db.session" in sys.modules:
                del sys.modules["algolib.db.session"]

            with pytest.raises(ValueError, match="DATABASE_URL environment variable not set"):
                import algolib.db.session  # noqa: F401
