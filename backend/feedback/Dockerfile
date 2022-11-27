FROM python:3.10-slim as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN apt update && apt install -y \
    default-libmysqlclient-dev \
    gettext \
    gcc

FROM base as builder

RUN pip install poetry

COPY pyproject.toml pyproject.toml

RUN poetry install --no-dev --no-root

COPY . .

RUN poetry build

FROM base as final

COPY --from=builder /app .

RUN pip install --no-cache /app/dist/*.whl

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
