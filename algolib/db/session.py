import os
from typing import Generator, Optional

from dotenv import load_dotenv
from sqlalchemy.engine import Engine
from sqlmodel import Session, create_engine

load_dotenv()

# Lazy initialization - only create engine when needed
_engine: Optional[Engine] = None


def _get_engine() -> Engine:
    """Get or create the database engine."""
    global _engine
    if _engine is None:
        DATABASE_URL = os.getenv("DATABASE_URL")
        if not DATABASE_URL or DATABASE_URL == "None":
            raise ValueError("DATABASE_URL environment variable not set")
        _engine = create_engine(DATABASE_URL, echo=True)
    return _engine


def get_session() -> Generator[Session, None, None]:
    engine = _get_engine()
    with Session(engine) as session:
        yield session
