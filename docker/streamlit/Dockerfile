FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
COPY algolib ./algolib
COPY app.py ./
RUN pip install poetry && poetry config virtualenvs.create false \
    && poetry install --without dev --extras streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
