# PrivBird

## Development server

```bash
docker-compose -f .\docker-compose.yml up --build -d
```

## Production server

```bash
docker-compose -f .\docker-compose.prod.yml up --build -d
```

## Run tests

```bash
python manage.py test
```

## Services

### OpenAPI

> available only in development mode

- /docs/swagger/ - swagger interface
- /docs/swagger.json - swagger scheme in json format
- /docs/swagger.yaml - swagger scheme in yaml format
- /docs/redoc/ - redoc interface

### Administration

> Credentials are configured in `.env` files

- /admin/ - Django admin panel
- /rosetta/ - Rosetta translation interface (authorization via admin panel required)
