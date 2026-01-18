#!/usr/bin/env bash
set -e

echo "Starting database migrations..."

if [ -z "$DATABASE_URL" ]; then
  echo "DATABASE_URL not set"
  exit 1
fi

for f in migrations/*.sql; do
  echo "▶ Applying $f"
  psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f "$f"
done

echo "Migrations finished successfully"
