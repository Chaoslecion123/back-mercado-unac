from rest_framework import serializers

# MODELO
from mercados.markets.models import Market,MarketPassRequest,CounterMarket

class MarketSerializer(serializers.ModelSerializer):
    distrito = serializers.SerializerMethodField()
    ciudad = serializers.SerializerMethodField()
    departamento = serializers.SerializerMethodField()
    direccion = serializers.SerializerMethodField()


    class Meta:
        model = Market
        fields = (
            'id',
            'name',
            'direccion',
            'distrito',
            'ciudad',
            'departamento',
            'aforo'
        )

    
    def get_direccion(self,obj):
        if obj.address:
            return f"{obj.address.line_1} - {obj.address.line_2}" 

    def get_distrito(self,obj):
        if obj.address.city_area:
            return obj.address.city_area.name

    def get_ciudad(self,obj):
        if obj.address.city:
            return obj.address.city.name

    def get_departamento(self,obj):
        if obj.address.country_area:
            return obj.address.country_area.name




class CounterMarketSerializer(serializers.ModelSerializer):
    name_schedule = serializers.SerializerMethodField()

    class Meta:
        model = CounterMarket
        fields = (
            'id',
            'markets',
            'count_aforo',
            'schedule',
            'name_schedule',
        )

    def get_name_schedule(self,obj):
        return f'inicia {obj.schedule.time_start} y termina {obj.schedule.time_end}'


class MarketPassRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPassRequest
        fields = (
            'id',
            'counter_market',
            'count',
            'archivopdf',
            'client'
        )