from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy
from mercados.utils.models import MercadoUtil
from mercados.addresses.models import Address


class Market(MercadoUtil):
    name= models.CharField(
        'nombre del mercado',
        max_length=50,

    )
    address = models.OneToOneField(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name='users_addresses',
        related_query_name='users_address',
        blank=True,
        null=True
    )
    staff = models.ManyToManyField(
        "staff.Staff",
        related_name='users_staff',
        related_query_name='users_staffs',
        blank=True,
        null=True
    )
    aforo = models.IntegerField(
        'cantidad de personas que un mercado puede soportar',
        default=0
    )

    count_aforo = models.IntegerField(
        'contador para control de aforos',
        default=0
    )
    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name='users_client',
        related_query_name='users_clients',
        blank=True,
        null=True
    )
    schedule = models.ManyToManyField(
        "schedule.Schedule",
        related_name='users_schedule',
        related_query_name='users_schedules',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = pgettext_lazy(
            'Market model name',
            'mercado'
        )
        verbose_name_plural = pgettext_lazy(
            'Market model name',
            'mercados'
        )

    def __str__(self):
        return self.name