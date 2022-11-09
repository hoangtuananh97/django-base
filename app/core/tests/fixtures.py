import json
import logging

import pytest
from django.contrib.auth.models import AnonymousUser, User
from django.core.serializers.json import DjangoJSONEncoder
from django.test.client import MULTIPART_CONTENT, Client
from rest_framework_simplejwt.tokens import RefreshToken

from ...tests.utils import flush_post_commit_hooks
from .utils import assert_no_permission


ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"


class ApiClient(Client):
    """Rest API client."""
    simple_token = RefreshToken()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", AnonymousUser())
        self._user = None
        self.token = None
        self.user = user
        if not user.is_anonymous:
            self.token = str(self.simple_token.for_user(user))
        super().__init__(*args, **kwargs)

    def _base_environ(self, **request):
        environ = super()._base_environ(**request)
        if not self.user.is_anonymous:
            environ["HTTP_AUTHORIZATION"] = f"Bearer {self.token}"
        return environ

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user
        if not user.is_anonymous:
            self.token = str(self.simple_token.for_user(user))

    def post(self, path, data=None, **kwargs):
        """Send a POST request.

        This wrapper sets the `application/json` content type which is
        more suitable for standard requests and doesn't mismatch with
        handling multipart requests in Graphene.
        """
        if data:
            data = json.dumps(data, cls=DjangoJSONEncoder)
        kwargs["content_type"] = "application/json"
        return super().post(path, data, **kwargs)

    def post_method(
        self,
        path,
        data,
        permissions=None,
        check_no_permissions=True,
        **kwargs,
    ):
        """Dedicated helper for posting queries.

        Sets the `application/json` content type and json.dumps the variables
        if present.
        """
        if data:
            data = json.dumps(data, cls=DjangoJSONEncoder)
        kwargs["content_type"] = "application/json"

        if permissions:
            if check_no_permissions:
                response = super().post(path, data, **kwargs)
                assert_no_permission(response)
                self.user.user_permissions.add(*permissions)
        result = super().post(path, data, **kwargs)
        flush_post_commit_hooks()
        return result

    def post_multipart(self, path, *args, permissions=None, **kwargs):
        """Send a multipart POST request.

        This is used to send multipart requests to API when e.g.
        uploading files.
        """
        kwargs["content_type"] = MULTIPART_CONTENT

        if permissions:
            response = super().post(path, *args, **kwargs)
            assert_no_permission(response)
            self.user.user_permissions.add(*permissions)
        return super().post(path, *args, **kwargs)


@pytest.fixture
def staff_api_client(staff_user):
    return ApiClient(user=staff_user)


@pytest.fixture
def superuser_api_client(superuser):
    return ApiClient(user=superuser)


@pytest.fixture
def user_api_client(customer_user):
    return ApiClient(user=customer_user)


@pytest.fixture
def api_client():
    return ApiClient(user=AnonymousUser())


class LoggingHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.messages = []

    def emit(self, record: logging.LogRecord):
        exc_type, exc_value, _tb = record.exc_info
        self.messages.append(
            f"{record.name}[{record.levelname.upper()}].{exc_type.__name__}"
        )


@pytest.fixture
def user_list_not_active(user_list):
    users = User.objects.filter(pk__in=[user.pk for user in user_list])
    users.update(is_active=False)
    return users


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath

