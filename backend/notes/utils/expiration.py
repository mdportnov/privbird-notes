from datetime import timedelta
from enum import Enum
from typing import Dict

from django.utils.datetime_safe import datetime
from django.utils.timezone import now


class Expiration(Enum):
    DAY = timedelta(days=1)
    WEEK = timedelta(days=7)
    MONTH = timedelta(days=30)
    YEAR = timedelta(days=365)

    def __str__(self) -> str:
        return f'Expiration.{self.name}'

    def get_expiration(self) -> datetime:
        return now() + self.value
