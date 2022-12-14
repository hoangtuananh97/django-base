import re
from re import Pattern

from django.utils.functional import SimpleLazyObject

from config.settings.base import INSTALLED_APPS

from ..settings import *  # noqa


def lazy_re_compile(regex, flags=0):
    """Lazily compile a regex with flags."""

    def _compile():
        # Compile the regex if it was not passed pre-compiled.
        if isinstance(regex, str):
            return re.compile(regex, flags)
        else:
            assert (
                not flags
            ), "flags must be empty if regex is passed pre-compiled"
            return regex

    return SimpleLazyObject(_compile)


CELERY_TASK_ALWAYS_EAGER = True

SECRET_KEY = "NOTREALLY"

ALLOWED_CLIENT_HOSTS = ["www.example.com"]

TIME_ZONE = "Asia/Ho_Chi_Minh"
LANGUAGE_CODE = "en"


EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

COUNTRIES_ONLY = None

MEDIA_ROOT = None
MEDIA_URL = "/media/"
MAX_CHECKOUT_LINE_QUANTITY = 50

AUTH_PASSWORD_VALIDATORS = []

PASSWORD_HASHERS = ["app.core.tests.dummy_password_hasher.DummyHasher"]


PATTERNS_IGNORED_IN_QUERY_CAPTURES: list[Pattern | SimpleLazyObject] = [
    lazy_re_compile(r"^SET\s+")
]

INSTALLED_APPS.append("app.core.tests")  # noqa: F405

JWT_EXPIRE = True
