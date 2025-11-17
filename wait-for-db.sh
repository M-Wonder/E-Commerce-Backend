#!/bin/sh
# wait-for-db.sh

set -e

host="$1"
shift
cmd="$@"

# Wait until PostgreSQL is ready
until PGPASSWORD=$DATABASE_PASSWORD psql -h "$host" -U "$DATABASE_USER" -d "$DATABASE_NAME" -c '\q'; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Postgres is up - running migrations"
# Run migrations
python manage.py migrate

echo "Starting application"
exec $cmd
