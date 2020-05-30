from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy
from mercados.utils.models import MercadoUtil



# Create your models here.
class Address(MercadoUtil):
    """Model definition for Address."""
    line_1 = models.CharField(
        max_length=128
    )

    line_2 = models.CharField(
        max_length=128,
        blank=True
    )

    # country = models.ForeignKey(
    #     "world.Country",
    #     on_delete=models.CASCADE,
    #     related_name='+',
    #     blank=True,
    #     null=True
    # )

    country_area = models.ForeignKey(
        "world.CountryArea",
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True
    )

    city = models.ForeignKey(
        "world.City",
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True
    )

    city_area = models.ForeignKey(
        "world.CityArea",
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = pgettext_lazy(
            'Address model name',
            'dirección'
        )
        verbose_name_plural = pgettext_lazy(
            'Address model name',
            'direcciones'
        )
        permissions = (
            (
                'manage_address', pgettext_lazy(
                    'Permission description',
                    'Puede gestionar direcciones'
                )
            ),
        )

    def __str__(self):
        """Unicode representation of Address."""
        return f"{self.line_1}, {self.line_2}"