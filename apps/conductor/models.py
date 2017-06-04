from django.db import models
from django.core.validators import RegexValidator


class Conductor(models.Model):
    only_images = RegexValidator(
            regex='^[a-zA-Z0-9]*$',
            message='Username must be Alphanumeric',
            code='invalid_username'
        )

    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, null=True, upload_to="Conductor_media", validators='')
    direccion = models.TextField()
    rh = models.CharField(max_length=2, blank=True, null=True)  # lo puse null
    telefono = models.CharField(max_length=7, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)  # lo puse null
    correo = models.EmailField(blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)  # lo puse null en bd para pruebas
    nivel_estudio = models.TextField(blank=True, null=True) # lo puse null
    numero_licencia_conduccion = models.IntegerField(blank=True, null=True)  #lo puse null
    documento_licencia_conduccion = models.FileField(blank=True, null=True, upload_to="licenciaConduccion_media")
    categoria_licencia = models.CharField(max_length=2, blank=True, null=True) #lo puse null
    estado_licencia = models.BooleanField(blank=True, default=True) #lo puse null
    organismo_transito = models.TextField(blank=True, null=True) #lo puse null
    fecha_expedicion = models.DateField(null=True, blank=True)  # lo puse null en bd para pruebas
    fecha_vencimiento = models.DateField(null=True, blank=True)  # lo puse null en bd para pruebas
    restricciones = models.TextField(blank=True, null=True)
    experiencia = models.CharField(max_length=2, blank=True, null=True)  # lo puse null IntegerField
    activo_inactivo = models.BooleanField(blank=True, default=True)

    def __str__(self):
        full_name = self.nombres + ' ' + self.apellidos
        return full_name
