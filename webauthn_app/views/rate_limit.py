from django.http import HttpResponse
from django.shortcuts import render

def rate_limited_error(request, exception=None):
    """
    View to handle rate-limited requests.
    This view is called when a request is rate-limited by django-ratelimit.
    """
    return HttpResponse(
        "Too many requests. Please try again later.",
        status=429,
        content_type="text/plain"
    )