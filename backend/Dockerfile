# Use the official Python image from the Docker Hub
FROM python:3.12

# Set environment variables
ENV POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    PYTHONPATH="/app"

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y dos2unix netcat-openbsd

# Install Poetry
RUN pip install --upgrade pip && pip install poetry

# Copy only the necessary files for dependency installation
COPY pyproject.toml poetry.lock ./

# Install dependencies globally
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the working directory contents into the container
COPY . /app

# Convert line endings and make scripts executable
RUN find /app -type f -name "*.sh" -exec dos2unix {} + && \
    find /app -type f -name "*.sh" -exec chmod +x {} +

# Debug: List files and installed packages
RUN ls -l /app && pip list

# Expose the backend port
EXPOSE 8000

# Add a health check for the database
HEALTHCHECK --interval=10s --timeout=5s --start-period=5s --retries=3 \
    CMD nc -z $POSTGRES_SERVER $POSTGRES_PORT || exit 1

# Run the prestart script and start the FastAPI server
CMD ["/bin/bash", "-c", "while ! nc -z $POSTGRES_SERVER $POSTGRES_PORT; do sleep 1; done; /app/prestart.sh && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000"]