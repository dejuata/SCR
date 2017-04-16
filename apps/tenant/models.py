from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_tenants.models import TenantMixin, DomainMixin
from django.conf import settings


class Tenant(TenantMixin):
    nit = models.IntegerField(unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    logo = models.ImageField(null=True, blank=True)
    razon_social = models.CharField(max_length=200)
    nombre_comercial = models.CharField(max_length=100, unique=True)
    telefono = models.IntegerField()
    correo = models.EmailField()
    ciudad = models.CharField(max_length=100)
    direccion = models.TextField(max_length=200)

    auto_create_schema = True

    class Meta:
        verbose_name = _('tenant')
        verbose_name_plural = _('tenants')

    def __str__(self):
        return self.schema_name


class Domain(DomainMixin):

    def __str__(self):
        return self.domain

    pass
