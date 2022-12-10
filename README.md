# PrivBird

## Run services

```bash
docker-compose -f ./backend/feedback/docker-compose.yml up --build -d
docker-compose -f ./backend/privnote/docker-compose.yml up --build -d
docker-compose -f ./frontend/docker-compose.yml up --build -d
```

> If you want to run the backend services in development mode, pass `DJANGO_DEBUG=1` in the `.env` file

## Run tests

```bash
python manage.py test
```

## Infrastructure

`{service}` means:
- feedback
- privnote

### OpenAPI

> Available only in development mode

- `/{service}/docs/swagger/` - swagger interface
- `/{service}/docs/swagger.json` - swagger scheme in json format
- `/{service}/docs/swagger.yaml` - swagger scheme in yaml format
- `/{service}/docs/redoc/` - redoc interface

### Administration

> Credentials are configured in `.env` files

- `/{service}/admin/` - Django admin panel
- `/{service}/rosetta/` - Rosetta translation interface (authorization via admin panel required)
