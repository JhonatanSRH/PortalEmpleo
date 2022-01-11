"""Django models utilities."""

# Django
from django.db import models


class BasePortalModel(models.Model):
    """Base Portal Model.
    Genera los campos creado y modificado para los modelos que lo requieran
    basado en la estructura de modelos de Django.
    """

    created = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha en la que fue creado el objeto.'
    )
    modified = models.DateTimeField(
        auto_now=True,
        help_text='Fecha en la que fue alterado el objeto.'
    )

    class Meta:

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']