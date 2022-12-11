from django.utils.translation import gettext_lazy as _


def compose_email(is_real: bool, slug: str, is_destroyed: bool) -> str:
    message = _('The {real} note with ID {id} has just been read, {ending}.')
    real = '' if is_real else _('fake')
    ending = _('the content was destroyed') if is_destroyed \
        else _('the next time someone reads it, a fake note will be displayed')
    return message.format(real=real, id=slug, ending=ending).strip().capitalize()
