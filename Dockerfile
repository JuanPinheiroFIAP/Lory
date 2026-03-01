FROM python:3.12-slim

WORKDIR /app

# Copia apenas arquivos de dependência primeiro (melhora cache)
COPY pyproject.toml poetry.lock* ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Agora copia o resto do projeto
COPY . .

CMD ["python", "-m", "lory"]