from secrets import token_hex

from notes.utils.Constants import Constants


def generate_slug() -> str:
    from notes.models import Note
    slug = token_hex()[:Constants.SLUG_LENGTH]
    while Note.objects.filter(slug=slug).exists():
        slug = token_hex()[:Constants.SLUG_LENGTH]
    return slug


def generate_key() -> str:
    return token_hex()[:Constants.KEY_LENGTH]
