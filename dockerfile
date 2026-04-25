# Pull base image
FROM python:3.14-slim

# Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -Ls https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# copy only dependency files for caching
COPY pyproject.toml uv.lock* /app/

# Install python dependencies
RUN uv sync --no-dev --no-install-project

# Now copy rest of the project
COPY . /app/

# Install project itself
RUN uv sync --no-dev

# Expose Django dev port
EXPOSE 8000

# Default command: run Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]