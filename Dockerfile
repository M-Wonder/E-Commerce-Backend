FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first (for caching)
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Make wait-for-db.sh executable
RUN chmod +x /app/wait-for-db.sh

EXPOSE 8000

# The actual command is defined in docker-compose.yml
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
