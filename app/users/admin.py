from django.contrib import admin

from app.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'phone', 'avatar']
    search_fields = ['email']


