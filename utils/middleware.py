from django.core.cache import cache


from django.core.cache import cache


from django.core.cache import cache


class RequestCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.key = "request_count"
        cache.set(self.key, 0, timeout=None)

    def __call__(self, request):
        try:
            cache.incr(self.key)
        except ValueError:
            cache.set(self.key, 1, timeout=None)

        response = self.get_response(request)
        return response
