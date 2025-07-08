from typing import Generator

import pytest
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from algolib.db.models import Artefact, Benchmark, JobLog, Spec


@pytest.fixture(name="session")
def session_fixture() -> Generator[Session, None, None]:
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_spec(session: Session) -> None:
    spec = Spec(name="test_spec", content="foo: bar")
    session.add(spec)
    session.commit()
    session.refresh(spec)

    assert spec.id is not None
    assert spec.name == "test_spec"


def test_create_artefact(session: Session) -> None:
    spec = Spec(name="test_spec", content="foo: bar")
    artefact = Artefact(artefact_type="code", content="def hello(): pass", spec=spec)
    session.add(artefact)
    session.commit()
    session.refresh(artefact)

    assert artefact.id is not None
    assert artefact.spec.name == "test_spec"


def test_create_benchmark(session: Session) -> None:
    spec = Spec(name="test_spec", content="foo: bar")
    artefact = Artefact(artefact_type="code", content="def hello(): pass", spec=spec)
    benchmark = Benchmark(results={"time": 1.23}, artefact=artefact)
    session.add(benchmark)
    session.commit()
    session.refresh(benchmark)

    assert benchmark.id is not None
    assert benchmark.results["time"] == pytest.approx(1.23)


def test_create_job_log(session: Session) -> None:
    job_log = JobLog(level="INFO", message="Test log message", job_id="123")
    session.add(job_log)
    session.commit()
    session.refresh(job_log)

    assert job_log.id is not None
    assert job_log.level == "INFO"


def test_get_session(session: Session) -> None:
    # The fixture already tests if a session can be created.
    # We can add a simple check to ensure it's a valid session.
    assert isinstance(session, Session)
