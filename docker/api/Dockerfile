FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
COPY algolib ./algolib
COPY scripts ./scripts
COPY alembic.ini ./
COPY migrations ./migrations
RUN pip install poetry && poetry config virtualenvs.create false \
    && poetry install --without dev --extras "api streamlit"
CMD ["uvicorn", "algolib.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
