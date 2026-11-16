# Slim official Python image keeps the image small and reduces attack surface.
FROM python:3.12-slim

# Don't write .pyc files; print logs straight to the container output.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements first so Docker caches the dependency layer
# and only reinstalls when requirements.txt changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Version shown by the app; the pipeline passes the git commit SHA here.
ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}

# Security: run as a non-root user.
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

# Container health check (uses Python so no extra tools are needed).
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

# gunicorn is a production WSGI server (Flask's dev server is not for production).
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
