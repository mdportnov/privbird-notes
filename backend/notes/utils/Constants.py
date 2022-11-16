class Constants:
    MAX_PASSWORD_LENGTH: int = 100
    MAX_CONTENT_LENGTH: int = 40_000
    SLUG_LENGTH: int = 12
    SALT_LENGTH: int = 32
    HASHER: str = 'pbkdf2_sha256'
