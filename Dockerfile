FROM python:3.12-slim

WORKDIR /app

# Copia dependências primeiro (cache)
COPY pyproject.toml poetry.lock* ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copia projeto
COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]