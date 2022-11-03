from secrets import token_hex


def generate_slug() -> str:
    from notes.models import Note
    slug = token_hex(12)
    while Note.objects.filter(slug=slug).exists():
        slug = token_hex(12)
    return slug
