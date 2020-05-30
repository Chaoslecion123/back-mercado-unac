"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from mercados.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass