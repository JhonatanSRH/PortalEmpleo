"""Users models."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utils
from utils.models import BasePortalModel


class User(BasePortalModel, AbstractUser):
    """User model.

    Clase Basada en los usuarios de Django y el modelo base del porjecto.
    """
    CC = 'CC'
    NIT = 'NIT'
    CE = 'CE'
    TI = 'TI'
    
    ID_TYPES = [
        (CC, 'Cedula de Ciudadania'),
        (NIT, 'NIT'),
        (CE, 'Cedula de Extranjeria'),
        (TI, 'Tarjeta de Identidad'),
    ]
    
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'Ya se ha registrado ese email con anterioridad.'
        },
    )
    
    other_first_name = models.CharField(max_length=50, blank=True)
    other_last_name = models.CharField(max_length=50, blank=True)
    
    id_type = models.CharField(
        max_length=3,
        choices=ID_TYPES,
        default=CC,
    )

    id_regex = RegexValidator(
        regex=r'\+?1?\d{8,10}$',
        message="La cedula debe ir en un formato numerico de la siguiente forma: +99999999. Hasta 10 caracteres permitidos."
    )
    id_number = models.CharField(
        validators=[id_regex], 
        unique=True, 
        max_length=10,
        error_messages={
            'unique': 'Ya se ha registrado ese numero de documento con anterioridad.'
        })

    profession = models.CharField(max_length=75, blank=True)
    profile = models.CharField(max_length=300, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
