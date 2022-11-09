from typing import List

import pytest

from app.users.models import User


@pytest.fixture()
def superuser(db) -> User:
    """Return a Django admin user."""
    return User.objects.create_superuser("superuser@example.com", "password")


@pytest.fixture()
def staff_user(db) -> User:
    """Return a staff member."""
    return User.objects.create_user(
        email="staff_test@example.com",
        password="password",
        is_staff=True,
        is_active=True,
    )


@pytest.fixture(autouse=True)
def customer_user(db) -> User:
    """Return a staff member."""
    return User.objects.create_user(
        email="customer_user@example.com",
        password="password",
        is_active=True,
    )


@pytest.fixture(autouse=True)
def user_list(db, django_db_setup) -> List[User]:
    users = User.objects.bulk_create(
        [
            User(email="user-2@example.com"),
            User(email="user-1@example.com"),
            User(email="staff-1@example.com", is_staff=True),
            User(email="staff-2@example.com", is_staff=True),
        ]
    )
    return users
