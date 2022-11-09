import json


def get_content_from_response(response):
    return json.loads(response.content.decode("utf8"))


def get_content(response, *, ignore_errors: bool = False):
    """Gets content from the response, and optionally checks if it
    contains any operating-related errors, eg. schema errors or lack of
    permissions.
    """
    content = get_content_from_response(response)
    if not ignore_errors:
        assert content["error"] is None, content["error"]
    return content


def assert_no_permission(response):
    content = get_content_from_response(response)
    assert content["error"] is not None, content["error"]
    assert content["error"]["message"] == (
        "Authentication credentials were not provided."
    ), content["error"]


def assert_error_with_message(response, message):
    content = get_content_from_response(response)
    assert content["error"] is not None, content["error"]
    assert message in content["error"]["message"], content["error"]


def get_multipart_request_body(query, variables, file, file_name):
    """Create request body for multipart requests.

    Multipart requests are different than standard requests, because
    of additional 'operations' and 'map' keys.
    """
    return {
        file_name: file,
    }
