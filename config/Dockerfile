FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy application
COPY src/alma ./src/alma
COPY config/alma.env ./config/alma.env

# Create necessary directories (empty, will be mounted as volumes)
RUN mkdir -p db

# Set environment
ENV PYTHONPATH=/app/src

# Run alma
ENTRYPOINT ["alma"]
CMD ["chat"]