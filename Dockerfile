# Creative Flask Web App Dockerfile
# Multi-stage build for optimized production image

# Build stage
FROM python:3.11-slim as builder

# Set build arguments
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION=1.0.0

# Labels for metadata
LABEL maintainer="CICD Demo <demo@example.com>" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Creative Flask Web App" \
      org.label-schema.description="A modern, responsive web application built with Flask and Bootstrap" \
      org.label-schema.url="https://github.com/gh-srinivas/cicddemo-repo1-sv" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/gh-srinivas/cicddemo-repo1-sv" \
      org.label-schema.vendor="CICD Demo" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create app directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim

# Set production environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    FLASK_ENV=production \
    FLASK_DEBUG=False \
    FLASK_HOST=0.0.0.0 \
    FLASK_PORT=5000

# Create non-root user for security
RUN groupadd -r flaskapp && \
    useradd -r -g flaskapp -d /app -s /bin/bash flaskapp

# Create app directory and set ownership
WORKDIR /app
RUN chown -R flaskapp:flaskapp /app

# Install runtime dependencies only
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        ca-certificates \
        && rm -rf /var/lib/apt/lists/* \
        && apt-get clean

# Copy Python packages from builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY --chown=flaskapp:flaskapp app/ ./app/
COPY --chown=flaskapp:flaskapp requirements.txt ./
COPY --chown=flaskapp:flaskapp *.py ./

# Create logs directory
RUN mkdir -p /app/logs && \
    chown -R flaskapp:flaskapp /app/logs

# Switch to non-root user
USER flaskapp

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${FLASK_PORT}/api/health || exit 1

# Expose application port
EXPOSE ${FLASK_PORT}

# Set default command
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--worker-class", "sync", "--worker-connections", "1000", "--max-requests", "1000", "--max-requests-jitter", "100", "--timeout", "30", "--keep-alive", "2", "--log-level", "info", "--access-logfile", "-", "--error-logfile", "-", "app:app"]