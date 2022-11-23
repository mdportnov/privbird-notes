from django.core.cache import cache
from rest_framework.request import Request
from rest_framework.throttling import BaseThrottle


class RateThrottle(BaseThrottle):
    def allow_request(self, request: Request, view) -> bool:
        addr = request.META['REMOTE_ADDR']
        requests = cache.get_or_set(addr, 0, 0) + 1
        cache.set(addr, requests, 0)
        return True
