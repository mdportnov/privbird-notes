from django.core.cache import cache
from rest_framework.request import Request
from rest_framework.throttling import SimpleRateThrottle

from privnote import settings


class RateThrottle(SimpleRateThrottle):
    rate = '100/h'

    def get_cache_key(self, request: Request, view):
        addr = request.META['REMOTE_ADDR']
        return cache.get_or_set(addr, 0, 0) + 1

    def allow_request(self, request, view):
        allowed = super().allow_request(request, view)
        return allowed or settings.TEST
