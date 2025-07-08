import datetime
from typing import Any, List, Optional

from sqlmodel import JSON, Column, Field, Relationship, SQLModel

__all__ = ["Spec", "Artefact", "Benchmark", "JobLog", "SQLModel"]


class Spec(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    content: str  # The YAML content of the spec
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)

    artefacts: List["Artefact"] = Relationship(back_populates="spec")


class Artefact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artefact_type: str = Field(index=True)  # e.g., 'code', 'test', 'docs'
    content: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)

    spec_id: int = Field(foreign_key="spec.id")
    spec: Spec = Relationship(back_populates="artefacts")

    benchmarks: List["Benchmark"] = Relationship(back_populates="artefact")


class Benchmark(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    results: dict[str, Any] = Field(sa_column=Column(JSON))
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)

    artefact_id: int = Field(foreign_key="artefact.id")
    artefact: Artefact = Relationship(back_populates="benchmarks")


class JobLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow, nullable=False, index=True
    )
    level: str
    message: str
    job_id: Optional[str] = Field(default=None, index=True)
