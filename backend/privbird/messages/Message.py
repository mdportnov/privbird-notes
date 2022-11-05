from dataclasses import dataclass

from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING

from privbird.utils.Serializable import Serializable


@dataclass
class Message(Serializable):
    """
    A data transfer object for localized text messages that will
    be displayed to the client depending on the selected language
    """

    ru: str = ''
    en: str = ''

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT,
            properties={
                'ru': Schema(type=TYPE_STRING),
                'en': Schema(type=TYPE_STRING)
            }
        )
