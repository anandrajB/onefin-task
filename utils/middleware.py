from django.contrib.sessions.models import Session
from django.utils import timezone
from django.core.cache import cache


class RequestCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        key = "request_count"
        count = cache.get(key, 0)
        cache.set(key, count + 1, timeout=None)
        response = self.get_response(request)
        return response
