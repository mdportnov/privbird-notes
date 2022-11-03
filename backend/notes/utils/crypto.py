from base64 import urlsafe_b64encode

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_key(password: str, salt: str) -> bytes:
    cipher = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=bytes.fromhex(salt),
        iterations=390000,
    )
    return urlsafe_b64encode(cipher.derive(password.encode()))


def encrypt(password: str, salt: str, content: str) -> str:
    f = Fernet(generate_key(password, salt))
    return f.encrypt(content.encode()).decode()


def decrypt(password: str, salt: str, content: str) -> str:
    f = Fernet(generate_key(password, salt))
    return f.decrypt(content.encode()).decode()
