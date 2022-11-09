from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.exceptions import AuthenticationFailed


class PageNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Not found."
    default_code = "not_found"


class BadRequestException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Bad request")
    default_code = "bad_request"


class EmailNotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Email not found")
    default_code = "email_not_found"


class IdInvalid(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _("Id not found")
    default_code = "id_not_found"


class UserIsActivated(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("User is activate")
    default_code = "user_is_activated"


class NotMatchPassword(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Not match password")
    default_code = "not_match_password"


class IntegrityDataError(APIException):
    default_detail = _("Integrity data error")
    default_code = "integrity_data_error"


class ServerDatabaseError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _("Server Database Error")
    default_code = "server_database_error"


class LoginInvalid(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _("User unauthorized")
    default_code = "user_unauthorized"


class UserNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _("User not found")
    default_code = "user_not_found"


class UserIsActivatedOrIsDeleted(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("User is not activate or deleted")
    default_code = "user_is_activated_or_deleted"


class ErrorFormatFile(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Error Format File")
    default_code = "error_format_file"


class ErrorMaxLengthFile(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Error Max length File")
    default_code = "error_length_file"


class InvalidToken(AuthenticationFailed):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _("Token is invalid or expired")
    default_code = "token_not_valid"
