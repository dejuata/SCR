from django.db import models


class Cliente(models.Model):
    nit = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, null=True, upload_to="logo_media")
    telefono = models.IntegerField()
    correo = models.EmailField()
    ciudad = models.CharField(max_length=50)
    direccion = models.TextField()
    activo_inactivo = models.BooleanField(blank=True, default=True)
