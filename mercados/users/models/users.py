"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#model Utils
from mercados.utils.models import MercadoUtil

class User(MercadoUtil,AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    dni = models.CharField(
        'documento de identidad',
        max_length=8,
        unique=True,
        error_messages={
            'unique':'A user with is dni already exists.'
        }
    )

    birthdate = models.DateField(
        'fecha de nacimiento',
        blank=True,
        null=True
    )

    is_client = models.BooleanField(
        default=True,
        help_text='help esasy to distinguish users and perfom querys'
    )

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username