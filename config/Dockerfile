# config/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN pip install poetry

# Configurar Poetry para no crear un entorno virtual
RUN poetry config virtualenvs.create false

# Copiar archivos de dependencias
COPY pyproject.toml poetry.lock* ./

# Instalar dependencias
RUN poetry install --no-dev

# Copiar el código fuente
COPY src/ ./src/
COPY config/alma.env ./.env

# Exponer el puerto
EXPOSE 8000

# Comando por defecto
CMD ["alma", "start"]