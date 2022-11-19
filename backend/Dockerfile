FROM python:3.10-slim as builder

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y \
    gcc \
    default-libmysqlclient-dev

ADD requirements.txt requirements.txt

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.10-slim

WORKDIR /app/

RUN apt update && apt install -y \
    default-libmysqlclient-dev \
    gettext

COPY --from=builder /app/wheels /wheels

RUN pip install --no-cache /wheels/*

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
