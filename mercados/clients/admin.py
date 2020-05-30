"""Client models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from mercados.clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass