from _datetime import datetime
from rest_framework.views import exception_handler

from app.core.api_exception import PageNotFound


def exception_handler_response(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if isinstance(exc, PageNotFound):
        response.data = None
        return response

    if response is not None:
        code = exc.default_code
        message = exc.detail
        response.data = {
            "status": "ERROR",
            "body": None,
            "error": {
                "message": message,
                "code": code,
                "timestamp": datetime.now(),
            },
        }
        response.content_type = "application/json"

    return response
