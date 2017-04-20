from django.db import models

# Create your models here.
class Cliente(models.Model):
    nit = models.CharField(max_length=9, primary_key=True)
    razon_social = models.CharField(max_length=50)
    logo = models.ImageField(blank=False, upload_to="logo_media")
    telefono = models.CharField(max_length=12)
    correo = models.EmailField()
    ciudad = models.CharField(max_length=50)
    direccion = models.TextField()
    activo_inactivo = models.BooleanField()
