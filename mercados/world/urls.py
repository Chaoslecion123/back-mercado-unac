"""Users URLs."""

# Django
from django.urls import include, path

# Views
from .views import world as world_views


urlpatterns = [
    path('departamentos/', world_views.ObtenerDepartamentos.as_view()),
    path('ciudades/', world_views.ObtenerCiudades.as_view()),
    path('distritos/', world_views.ObtenerDistritos.as_view())
]