FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy only after project exists
COPY . /app/

# collect static files
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD [ "Python", "manage.py", "runserver", "0.0.0.0:8000"]

