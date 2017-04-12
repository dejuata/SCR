from __future__ import unicode_literals
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    nit = models.IntegerField(null=False, blank=True)
    logo = models.ImageField(null=True)
    razon_social = models.CharField(null=True, max_length=200)
    telefono = models.IntegerField(null=True)
    correo = models.EmailField(null=False, blank=True)
    ciudad = models.CharField(null=False, max_length=100)
    direccion = models.TextField(null=False, max_length=200)
    # nit = models.IntegerField(primary_key=True)
    # logo = models.ImageField(null=True)
    # razon_social = models.CharField(max_length=200)
    # nombre_comercial = models.CharField(max_length=100, unique=True)
    # telefono = models.IntegerField()
    # correo = models.EmailField()
    # ciudad = models.CharField(max_length=100)
    # direccion = models.TextField(max_length=200)

    auto_create_schema = True

    def __str__(self):
        return self.schema_name


class Domain(DomainMixin):
    pass
