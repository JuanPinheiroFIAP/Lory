FROM python:3.12-slim

# Impede que o Python gere arquivos .pyc e permite logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# Instala dependências de sistema para banco de dados e build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && pip install --no-cache-dir poetry \
    && rm -rf /var/lib/apt/lists/*

# 1. Copia os arquivos de configuração (Poetry)
COPY pyproject.toml poetry.lock* README.md* ./

# 2. Configura o Poetry e instala as dependências
# O "touch" evita erro caso o pyproject peça um README inexistente
RUN touch README.md && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main --no-root

# 3. Copia o código fonte (mantendo a pasta src)
COPY src/ ./src/

# Configura usuário não-root para segurança
RUN useradd -m appuser && \
    chown -R appuser /app

USER appuser

# Porta padrão para o Railway (ele injetará a variável PORT automaticamente)
EXPOSE 8000

# Comando para rodar o app. 
# Importante: Aponta para o objeto 'app' dentro de src/app/main.py
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
