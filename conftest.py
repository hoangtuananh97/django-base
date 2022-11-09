import pytest


@pytest.fixture(scope="session")
def django_db_setup(django_db_blocker, django_db_keepdb=True) -> None:
    yield


pytest_plugins = [
    "app.tests.fixtures",
    "app.core.tests.fixtures",
]
