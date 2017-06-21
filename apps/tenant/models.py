from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_tenants.models import TenantMixin, DomainMixin
from django.conf import settings
from django.db.models.fields import IntegerField
from django.conf import settings


class BigIntegerField(IntegerField):
    empty_strings_allowed = False

    def get_internal_type(self):
        return "BigIntegerField"

    # Note this won't work with Oracle.
    def db_type(self):
        return 'bigint'


class Tenant(TenantMixin):
    nit = BigIntegerField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='tenant', null=True, blank=True, default='')
    razon_social = models.CharField(max_length=200)
    nombre_comercial = models.CharField(max_length=100, unique=True)
    telefono = models.IntegerField()
    correo = models.EmailField()
    departamento = models.CharField(max_length=100, default='')
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
