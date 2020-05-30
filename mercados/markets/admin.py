"""markets models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from mercados.markets.models import Market


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    pass