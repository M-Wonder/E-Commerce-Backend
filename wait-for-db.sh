#!/bin/sh
set -e

cmd="$@"

echo "Waiting for PostgreSQL..."

# wait until Postgres is reachable
until PGPASSWORD=$DATABASE_PASSWORD psql -h "$DATABASE_HOST" -U "$DATABASE_USER" -d "$DATABASE_NAME" -c '\q' >/dev/null 2>&1; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Postgres is up - applying migrations"
python manage.py migrate

echo "Starting application"
exec $cmd
