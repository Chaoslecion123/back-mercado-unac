from rest_framework import serializers

# MODELO
from mercados.markets.models import Market

class MarketSerializer(serializers.ModelSerializer):
    distrito = serializers.SerializerMethodField()
    ciudad = serializers.SerializerMethodField()
    departamento = serializers.SerializerMethodField()
    direccion = serializers.SerializerMethodField()


    class Meta:
        model = Market
        fields = (
            'name',
            'direccion',
            'aforo',
            'distrito',
            'ciudad',
            'departamento'
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

    

