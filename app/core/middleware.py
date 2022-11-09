import json
import re

from django.conf import settings
from django.views.defaults import server_error
from rest_framework import status

from config.settings.base import CORS_URLS_REGEX


class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        # HTTP response status codes https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        if response.status_code == 500 and settings.DEBUG:
            if re.match(CORS_URLS_REGEX, request.path):
                response.headers = {"Content-Type": "application/json"}
                response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
                content = {
                    "error": "A server error occurred.  Please contact the administrator."
                }
                response.content = json.dumps(content).encode("utf-8")
            else:
                return server_error(request, template_name="500.html")
        return response
