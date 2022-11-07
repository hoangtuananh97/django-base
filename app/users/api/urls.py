
from django.urls import path

from app.users.api import views

urlpatterns = [
    path('users', views.UserView.as_view(), name="List, Create users"),
    path('user/<user_id>', views.UserDetailView.as_view(), name="Get detail, Update, delete user"),
]
