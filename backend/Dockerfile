FROM python:3.10-slim-bullseye

RUN apt update && apt install -y netcat python-dev

WORKDIR /app/

COPY . .
RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /app/backend/:$PYTHONPATH

ENTRYPOINT ["sh", "/app/backend/entrypoint.sh"]