# Django
from django.db.models import Q

# Django rest framework
from rest_framework.views import APIView
from rest_framework.response import Response

#Modelos
from mercados.world.models import *

# Serializers
from mercados.world.serializers.world import *

class ObtenerDepartamentos(APIView):
    def get(self,request):
        departamentos = CountryArea.objects.all()
        return Response(CountryAreaSerializer(departamentos,many=True).data)


class ObtenerCiudades(APIView):
    def get(self,request,id_departamento):
        ciudades = City.objects.filter(country_area__id=id_departamento)
        return Response(CitySerializer(ciudades,many=True).data)

class ObtenerDistritos(APIView):
    def get(self,request,id_departamento,id_ciudad):
        distritos = CityArea.objects.filter(
            Q(city__id=id_ciudad) & Q(city__country_area__id=id_departamento)
        )
        return Response(CityAreaSerializer(distritos,many=True).data)