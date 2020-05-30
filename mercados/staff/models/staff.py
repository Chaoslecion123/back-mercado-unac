from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy

from mercados.users.models import User


class Staff(User):
    class Meta:
        proxy = True
        verbose_name = pgettext_lazy(
            'Affiliation Activity model name',
            'empleado'
        )
        verbose_name_plural = pgettext_lazy(
            'Affiliation Activity model name',
            'empleados'
        )
        permissions = (
            (
                'manage_staff', pgettext_lazy(
                    'Permission description',
                    'Puede gestionar empleados'
                )
            ),
        )

    def save(self, *args, **kwargs):
        self.is_staff = True
        super().save(*args, **kwargs)