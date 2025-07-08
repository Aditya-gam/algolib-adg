from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from algolib.db.session import get_session

app = FastAPI(title="AlgoLib-ADG API")


@app.get("/health/db")
def health_db(sess: Annotated[Session, Depends(get_session)]) -> dict[str, str]:
    """Check database connectivity."""
    try:
        sess.execute(text("SELECT 1"))
        return {"db": "ok"}
    except SQLAlchemyError:
        return {"db": "fail"}
