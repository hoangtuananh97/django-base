"""
With these settings, tests run faster.
"""
import re
from re import Pattern

from django.utils.functional import SimpleLazyObject

from .base import *  # noqa
from .base import env


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


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="qZMPoGZQXp2c5LYKqGbu5kuAfAwOqYrnerIquvL0h9RDu6ovSTXFPy4Y0B7Oxm5T",
)

CELERY_TASK_ALWAYS_EAGER = True

TIME_ZONE = "Asia/Ho_Chi_Minh"
LANGUAGE_CODE = "en"

PATTERNS_IGNORED_IN_QUERY_CAPTURES: list[Pattern | SimpleLazyObject] = [
    lazy_re_compile(r"^SET\s+")
]

# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

MEDIA_ROOT = None
MEDIA_URL = "/media/"
ALLOWED_CLIENT_HOSTS = ["www.example.com"]
AUTH_PASSWORD_VALIDATORS = []
# DEBUGING FOR TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[0]["OPTIONS"]["debug"] = True  # type: ignore # noqa F405

INSTALLED_APPS.append("app.core.tests")  # noqa: F405
