FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy application
COPY src/alma ./src/alma
COPY config/alma.env ./config/alma.env
COPY meta/schema.sql ./meta/schema.sql

# Create necessary directories
RUN mkdir -p db

# Initialize database
RUN python -c "
import sqlite3
import os
os.makedirs('db', exist_ok=True)
conn = sqlite3.connect('db/alma.db')
with open('meta/schema.sql', 'r') as f:
    conn.executescript(f.read())
conn.close()
"

# Set environment
ENV PYTHONPATH=/app/src

# Run alma
CMD ["alma", "chat"]