FROM python:3.10-slim as builder

WORKDIR /app

RUN pip install --user poetry

COPY pyproject.toml poetry.lock ./

RUN python -m poetry config virtualenvs.create false \
    && python -m poetry install --no-interaction --no-ansi --no-root

FROM python:3.10-alpine

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/poetry /usr/local/bin/poetry

COPY . .

RUN find /usr/local/lib/python3.10 -type d -name '__pycache__' -exec rm -rf {} +

EXPOSE 80

CMD ["poetry", "run", "task", "prod"]