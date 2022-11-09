from django.urls import path

from app.users import views

app_name = "users"
urlpatterns = [
    path("", view=views.home, name="index"),
]
