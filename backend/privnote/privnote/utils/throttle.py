from django.core.cache import cache
from rest_framework.request import Request
from rest_framework.throttling import SimpleRateThrottle


class RateThrottle(SimpleRateThrottle):
    rate = '10/m'

    def get_cache_key(self, request: Request, view):
        addr = request.META['REMOTE_ADDR']
        return cache.get_or_set(addr, 0, 0) + 1
