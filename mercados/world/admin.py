"""World models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from mercados.world.models import Country,CountryArea,City,CityArea


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(CountryArea)
class CountryAreaAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(CityArea)
class CityAreaAdmin(admin.ModelAdmin):
    pass

