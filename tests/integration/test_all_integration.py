"""Integration tests for API, database, and specifications."""

import unittest
from pathlib import Path
from typing import Generator
from unittest.mock import MagicMock

import pytest
import yaml
from fastapi.testclient import TestClient
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from algolib.api.main import app
from algolib.db.models import Artefact, Benchmark, JobLog, Spec
from algolib.db.session import get_session
from algolib.specs.schema import AlgorithmSpec


@pytest.fixture
def client() -> TestClient:
    """Return a TestClient instance for the app."""
    return TestClient(app)


@pytest.fixture(name="session")
def session_fixture() -> Generator[Session, None, None]:
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


class TestAPI:
    """API integration tests."""

    def test_health_db_ok(self, client: TestClient) -> None:
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

    def test_health_db_fail(self, client: TestClient) -> None:
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


class TestDatabase:
    """Database integration tests."""

    def test_create_spec(self, session: Session) -> None:
        spec = Spec(name="test_spec", content="foo: bar")
        session.add(spec)
        session.commit()
        session.refresh(spec)

        assert spec.id is not None
        assert spec.name == "test_spec"

    def test_create_artefact(self, session: Session) -> None:
        spec = Spec(name="test_spec", content="foo: bar")
        artefact = Artefact(artefact_type="code", content="def hello(): pass", spec=spec)
        session.add(artefact)
        session.commit()
        session.refresh(artefact)

        assert artefact.id is not None
        assert artefact.spec.name == "test_spec"

    def test_create_benchmark(self, session: Session) -> None:
        spec = Spec(name="test_spec", content="foo: bar")
        artefact = Artefact(artefact_type="code", content="def hello(): pass", spec=spec)
        benchmark = Benchmark(results={"time": 1.23}, artefact=artefact)
        session.add(benchmark)
        session.commit()
        session.refresh(benchmark)

        assert benchmark.id is not None
        assert benchmark.results["time"] == pytest.approx(1.23)

    def test_create_job_log(self, session: Session) -> None:
        job_log = JobLog(level="INFO", message="Test log message", job_id="123")
        session.add(job_log)
        session.commit()
        session.refresh(job_log)

        assert job_log.id is not None
        assert job_log.level == "INFO"

    def test_get_session(self, session: Session) -> None:
        # The fixture already tests if a session can be created.
        # We can add a simple check to ensure it's a valid session.
        assert isinstance(session, Session)


class TestSpecifications(unittest.TestCase):
    """Specifications integration tests."""

    def setUp(self) -> None:
        self.valid_spec_data = {
            "name": "Test Algorithm",
            "description": "A test algorithm.",
            "category": "Testing",
            "complexity": {
                "time_worst": "O(n^2)",
                "time_average": "O(n^2)",
                "time_best": "O(n)",
                "space_worst": "O(1)",
            },
            "parameters": [
                {"name": "data", "type": "List[int]", "description": "A list of integers."}
            ],
            "returns": {"type": "List[int]", "description": "A sorted list of integers."},
            "dependencies": [],
        }
        self.spec_file = Path("test_spec.yml")
        with open(self.spec_file, "w") as f:
            yaml.dump(self.valid_spec_data, f)

    def tearDown(self) -> None:
        if self.spec_file.exists():
            self.spec_file.unlink()

    def test_from_file_valid(self) -> None:
        spec = AlgorithmSpec.from_file(self.spec_file)
        self.assertEqual(spec.name, "Test Algorithm")
        self.assertEqual(spec.complexity.time_worst, "O(n^2)")

    def test_from_file_invalid_missing_field(self) -> None:
        del self.valid_spec_data["name"]
        with open(self.spec_file, "w") as f:
            yaml.dump(self.valid_spec_data, f)

        with self.assertRaises(ValidationError):
            AlgorithmSpec.from_file(self.spec_file)

    def test_from_file_invalid_wrong_type(self) -> None:
        self.valid_spec_data["complexity"] = "should_be_a_dict"
        with open(self.spec_file, "w") as f:
            yaml.dump(self.valid_spec_data, f)

        with self.assertRaises(ValidationError):
            AlgorithmSpec.from_file(self.spec_file)
