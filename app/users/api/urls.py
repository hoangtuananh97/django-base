from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app.users.api import views
from app.users.api.views import TokenLogoutView

urlpatterns = [
    path("users/", views.UserView.as_view(), name="List, Create users"),
    path(
        "user/<user_id>/",
        views.UserDetailView.as_view(),
        name="Get detail, Update, delete user",
    ),
    path(
        "token/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/logout/", TokenLogoutView.as_view(), name="token_logout"),
]
