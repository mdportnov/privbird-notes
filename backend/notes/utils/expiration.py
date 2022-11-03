from datetime import timedelta
from enum import Enum

from django.utils.datetime_safe import datetime
from django.utils.timezone import now


class Expiration(Enum):
    DAY = timedelta(days=1)
    WEEK = timedelta(days=7)
    MONTH = timedelta(days=30)
    YEAR = timedelta(days=365)

    def get_expiration(self) -> datetime:
        return now() + self.value
