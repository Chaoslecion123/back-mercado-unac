from rest_framework import serializers

from ..models.schedule import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields  = (
            'id',
            'time_start',
            'time_end',
            'markets'
        )