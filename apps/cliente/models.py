from django.db import models

# Create your models here.
class Cliente(models.Model):

    nit = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=50, default='')
    logo = models.ImageField(blank=True, null=True, upload_to="logo_media",  default='')
    telefono = models.IntegerField(null=True)
    correo = models.EmailField()
    ciudad = models.CharField(max_length=50,  default='')
    direccion = models.TextField()
    activo_inactivo = models.BooleanField(default=True)
