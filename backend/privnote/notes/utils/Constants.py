class Constants:
    MAX_PASSWORD_LENGTH: int = 100
    MAX_EMAIL_LENGTH: int = 256
    MAX_CONTENT_LENGTH: int = 40_000
    SLUG_LENGTH: int = 12
    KEY_LENGTH: int = 12
    SALT_LENGTH: int = 32
    HASHER: str = 'pbkdf2_sha256'
    MAX_WAITING_PERIOD: int = 2
