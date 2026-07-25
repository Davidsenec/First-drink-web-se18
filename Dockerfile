# ==========================================
# Stage 1: Build dependencies using uv
# ==========================================
FROM python:3.12-slim-bookworm AS builder

# Install uv binary directly from official source
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory for build
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy dependency definition files first for caching
COPY pyproject.toml uv.lock ./

# Install dependencies into a virtual environment (.venv)
# --no-dev: Excludes packages from the [dependency-groups] dev section
# --frozen: Guarantees that uv doesn't modify uv.lock during build
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --frozen

# ==========================================
# Stage 2: Minimal runtime image
# ==========================================
FROM python:3.12-slim-bookworm AS runner

WORKDIR /app

# Set Python behavior env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

# Create a secure non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Copy virtual environment from builder stage
COPY --from=builder /app/.venv /app/.venv

# Copy application code and scripts
COPY app ./app
COPY alembic ./alembic
COPY alembic.ini ./alembic.ini
COPY scripts ./scripts

# Change ownership of app directory to non-root user and ensure entrypoint script is executable
RUN chown -R appuser:appgroup /app && chmod +x /app/scripts/entrypoint.sh

# Switch to the secure non-root user
USER appuser

# Expose FastAPI's default port
EXPOSE 8000

# Set entrypoint script and default command
ENTRYPOINT ["/app/scripts/entrypoint.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

