# PrivBird

## Backend

### Development servers

```bash
docker-compose -f ./backend/docker-compose.yml up --build -d
```

### Production servers

```bash
docker-compose -f ./backend/docker-compose.prod.yml up --build -d
```

### Run tests

```bash
python manage.py test
```

## Frontend

```bash
docker-compose -f ./frontend/docker-compose.yml up --build -d
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
