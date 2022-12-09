from datetime import timedelta
from enum import Enum

from django.utils.datetime_safe import datetime
from django.utils.timezone import now


class Expires(Enum):
    DAY = 'DAY'
    WEEK = 'WEEK'
    MONTH = 'MONTH'
    YEAR = 'YEAR'

    def __str__(self) -> str:
        return self.name

    def get_expiration(self) -> datetime:
        delta = {
            self.DAY: timedelta(days=1),
            self.WEEK: timedelta(days=7),
            self.MONTH: timedelta(days=30),
            self.YEAR: timedelta(days=365)
        }
        return now() + delta[self]
