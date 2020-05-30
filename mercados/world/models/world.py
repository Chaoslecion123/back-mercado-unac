from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy
from mercados.utils.models import MercadoUtil

class Country(MercadoUtil):
    """Country model."""
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = pgettext_lazy(
            'Country model name',
            'país'
        )
        verbose_name_plural = pgettext_lazy(
            'Country model name',
            'paises'
        )

    def __str__(self):
        return self.name


class CountryArea(MercadoUtil):
    """Country area model.
    In the peruvian political division this will represent `Departamentos`."""
    country = models.ForeignKey(
        Country,
        related_name='country_areas',
        related_query_name='country_area',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = pgettext_lazy(
            'Country Area model name',
            'departamento'
        )
        verbose_name_plural = pgettext_lazy(
            'Country Area model name',
            'departamentos'
        )

    def __str__(self):
        return self.name


class City(MercadoUtil):
    """City model.
    In the peruvian political division this will represent `Provincias`."""
    country_area = models.ForeignKey(
        CountryArea,
        related_name='cities',
        related_query_name='city',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = pgettext_lazy(
            'City model name',
            'provincia'
        )
        verbose_name_plural = pgettext_lazy(
            'City model name',
            'provincias'
        )

    def __str__(self):
        return self.name


class CityArea(MercadoUtil):
    """City area model.
    In the peruvian political division this will represent `Distritos`."""
    city = models.ForeignKey(
        City,
        related_name='city_areas',
        related_query_name='city_area',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = pgettext_lazy(
            'City Area model name',
            'distrito'
        )
        verbose_name_plural = pgettext_lazy(
            'City Area model name',
            'distritos'
        )

    def __str__(self):
        return self.name