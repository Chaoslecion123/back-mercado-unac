from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy

from mercados.users.models import User

class Client(User):
    class Meta:
        proxy = True
        verbose_name = pgettext_lazy(
            'Client model name',
            'cliente'
        )
        verbose_name_plural = pgettext_lazy(
            'Client model name',
            'clientes'
        )
        permissions = (
            (
                'manage_client', pgettext_lazy(
                    'Permission description',
                    'Puede gestionar clientes'
                )
            ),
            (
                'export_client', pgettext_lazy(
                    'Permission description',
                    'Puede exportar clientes'
                )
            ),
        )

    def save(self,*args,**kwargs):
        self.is_client=True