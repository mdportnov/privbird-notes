import dataclasses
from dataclasses import dataclass
from typing import Dict

from drf_yasg.openapi import Schema, TYPE_STRING

from privbird.dto.Serializable import Serializable


@dataclass
class Message(Serializable):
    """
    Data transfer object for localized text messages that will
    be displayed to the client depending on the selected language
    """

    ru: str = ''
    en: str = ''
    api_properties = {
        'ru': Schema(type=TYPE_STRING),
        'en': Schema(type=TYPE_STRING)
    }
