"""Addresses models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from mercados.addresses.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass