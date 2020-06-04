"""Users URLs."""

# Django
from django.urls import include, path

# Views
from .views import world as world_views


urlpatterns = [
    path('departamentos/', world_views.ObtenerDepartamentos.as_view()),
    path('ciudades/<int:id_departamento>/', world_views.ObtenerCiudades.as_view()),
    path('distritos/<int:id_departamento>/<int:id_ciudad>/', world_views.ObtenerDistritos.as_view())
]