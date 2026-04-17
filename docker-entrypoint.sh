#!/bin/sh
set -e

echo "Starting Folio Backend (FastAPI on port 7000)..."
cd /app/backend
uvicorn app:app --host 0.0.0.0 --port 7000 &

echo "Waiting for backend to be ready..."
until curl -sf http://localhost:7000/docs > /dev/null; do
  sleep 1
done

echo "Backend is up! Starting Frontend (Node.js on port 5000)..."
cd /app/frontend
exec node server.js