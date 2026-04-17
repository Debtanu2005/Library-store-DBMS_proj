# ═══════════════════════════════════════════════════════════════════
#  Folio — Library Store DBMS
#  Single Multi-Stage Dockerfile (Frontend + Backend)
# ═══════════════════════════════════════════════════════════════════


# ── Stage 1: Build Frontend ─────────────────────────────────────────
FROM node:20-alpine AS frontend-builder

WORKDIR /frontend

COPY frontend/package*.json ./
RUN npm ci --silent

COPY frontend/ .


# ── Stage 2: Build Backend ──────────────────────────────────────────
FROM python:3.11-slim AS backend-builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt


# ── Stage 3: Final Runtime Image ────────────────────────────────────
FROM python:3.11-slim AS runtime

WORKDIR /app

# Install Node.js into the Python runtime image
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from backend builder
COPY --from=backend-builder /install /usr/local

# Copy backend source
COPY backend/ ./backend/

# Copy frontend build + node_modules from frontend builder
COPY --from=frontend-builder /frontend ./frontend/

# Copy startup script
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# Create a non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
RUN chown -R appuser:appgroup /app
USER appuser

# Expose both ports
EXPOSE 7000 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
    CMD curl -f http://localhost:7000/docs && curl -f http://localhost:5000 || exit 1

ENTRYPOINT ["/app/docker-entrypoint.sh"]