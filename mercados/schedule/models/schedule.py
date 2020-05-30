from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy
from mercados.utils.models import MercadoUtil

class Schedule(MercadoUtil):
    time_start = models.TimeField()
    time_end = models.TimeField()

    class Meta:
        verbose_name = pgettext_lazy(
            'Horario model name',
            'horario'
        )
        verbose_name_plural = pgettext_lazy(
            'Horario model name',
            'horarios'
        )

    def __str__(self):
        return f'comienza {self.time_start} y termina {self.time_end}'