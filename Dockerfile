FROM python:3.10

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Ensure Poetry binary is in the PATH
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

# Create the src directory and main.py file
RUN mkdir -p src && echo '' > src/main.py

COPY pyproject.toml  poetry.lock* ./

RUN poetry install

COPY src /app/src

EXPOSE 8000




