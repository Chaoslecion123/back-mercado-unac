"""markets models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from mercados.markets.models import Market, MarketPassRequest, CounterMarket


# class InlinesMarketsRequests(admin.TabularInline):
#     model = MarketPassRequest
#     extra = 0

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    pass

@admin.register(MarketPassRequest)
class MarketPassRequestAdmin(admin.ModelAdmin):
    pass

@admin.register(CounterMarket)
class CounterMarketAdmin(admin.ModelAdmin):
    pass
    #inlines = [InlinesMarketsRequests]