from rest_framework import serializers
from mercados.world.models import *


class CountryAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryArea
        fields = (
            'id',
            'name'
        )

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name'
        )

class CityAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityArea
        fields = (
            'id',
            'name'
        )