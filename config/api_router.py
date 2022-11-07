from django.urls import path, include


urlpatterns = [
    path("", include("app.users.api.urls")),
]

