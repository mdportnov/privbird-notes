FROM python:3.10-alpine as builder

WORKDIR /app/

RUN apk add --update --virtual .build-deps \
    build-base \
    mariadb-dev \
    python3-dev

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

FROM python:3.10-alpine

COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . /app/

RUN apk add --update --virtual .build-deps \
    build-base \
    mariadb-connector-c-dev

WORKDIR /app/

RUN chmod +x entrypoint.sh

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app/backend/:$PYTHONPATH

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
