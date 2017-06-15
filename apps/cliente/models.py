from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Cliente(models.Model):

    # only_letters = RegexValidator(r'^[a-z A-Z]*$', 'Only letters are allowed.') # validators=[only_letters]

    nit = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, null=True, upload_to="logo_media", default='')
    telefono = models.IntegerField(null=True)
    correo = models.EmailField()
    ciudad = models.CharField(max_length=50, default='')
    direccion = models.TextField()
    activo_inactivo = models.BooleanField(blank=True, default=True)

    def state(self):
        return self.activo_inactivo

    state.boolean = True
    state.short_description = 'Estado'

    def __str__(self):
        return self.razon_social
