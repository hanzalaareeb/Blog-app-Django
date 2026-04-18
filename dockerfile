# Pull base image
FROM python:3.14-slim

# Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Set work directory
WORKDIR /code

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install --no-cache-dir poetry

# copy only dependencies
COPY pyproject.toml poetry.lock* /code/

# Install python dependencies
RUN uv add --without dev --no-root

# Now copy rest of the project
COPY . /code/

# Expose Django dev port
EXPOSE 8000

# Default command: run Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]