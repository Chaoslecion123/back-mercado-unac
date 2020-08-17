from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy
from mercados.utils.models import MercadoUtil
from mercados.addresses.models import Address
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.dispatch import receiver




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


class CounterMarket(MercadoUtil):
    markets = models.ForeignKey(
        Market,
        on_delete=models.CASCADE,
        related_name="passrequest"
    )

    count_aforo = models.IntegerField(
        'contador para control de aforos',
        default=0,
        blank=True,
        null=True
    )

    schedule = models.ForeignKey(
        "schedule.Schedule",
        on_delete=models.CASCADE,
        related_name='users_schedule',
        related_query_name='users_schedules',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = pgettext_lazy(
            'counterMarket model name',
            'Conteo de pases por Mercado'
        )
        verbose_name_plural = pgettext_lazy(
            'counterMarket model name',
            'conteos de pases por Mercados'
        )

    def __str__(self):
        return  "{} - personas({})".format(self.schedule,self.count_aforo)
    

class MarketPassRequest(MercadoUtil):
    counter_market = models.ForeignKey(
        CounterMarket, 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="market_pass_requests"
    )

    count = models.IntegerField(
        'contador para el pdf',
        default=0,
        blank=True,
        null=True
    )
    

    archivopdf = models.TextField(blank=True, null=True)

    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name='users_client',
        related_query_name='users_clients',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = pgettext_lazy(
            'MarketPassRequest model name',
            'Registro de  pase por Mercado'
        )
        verbose_name_plural = pgettext_lazy(
            'MarketPassRequest model name',
            'Registros de pases por Mercados'
        )

    def __str__(self):
        return "{} - {} pase  generado nro {} ".format(self.counter_market.markets.name,self.counter_market.schedule,self.count)
    




# @receiver(post_save,sender=MarketPassRequest)
# def actualizar_ultimo_count_aforo(sender,instance,created,**kwargs):
#     if created:
#         print('*** ** ***')
#         print(instance)
#         print('*** ** ***')

#         instance.count_aforo +=1
#         instance.save()