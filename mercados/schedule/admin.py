"""schedule models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from mercados.schedule.models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass