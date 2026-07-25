#!/bin/sh
set -e

echo "🚀 Running Alembic database migrations..."
alembic upgrade head

if [ "$ENV" = "development" ]; then
    echo "🌱 Seeding development admin user..."
    python -m app.init_db
fi

echo "⚡ Launching application server..."
exec "$@"
