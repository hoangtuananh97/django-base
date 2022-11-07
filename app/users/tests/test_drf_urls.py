from django.urls import resolve, reverse


def test_user_list():
    assert reverse("api:user-list") == "/api/v1/users/"
    assert resolve("/api/users/").view_name == "api:user-list"


def test_user_me():
    assert reverse("api:user-me") == "/api/v1/users/me/"
    assert resolve("/api/users/me/").view_name == "api:user-me"
