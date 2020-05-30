"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from mercados.staff.models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass
    #algo va pasar aqui