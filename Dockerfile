FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.4.0 /uv /bin/uv

WORKDIR /app

COPY uv.lock /app/uv.lock
COPY pyproject.toml /app/pyproject.toml

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-cache --no-install-project

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-cache

CMD ["uv", "run", "--no-sync", "python", "lessons_reporter_bot/main.py"]
