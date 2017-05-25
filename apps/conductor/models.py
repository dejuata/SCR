from django.db import models


class Conductor(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, null=True, upload_to="Conductor_media")
    direccion = models.TextField()
    rh = models.CharField(max_length=2)
    telefono = models.CharField(max_length=7, blank=True, null=True)
    celular = models.CharField(max_length=10)
    correo = models.EmailField(blank=True, null=True)
    fechaNacimiento = models.DateField()
    nivelEstudio = models.TextField()
    numLicenciaConduccion = models.IntegerField()
    docLicenciaConduccion = models.FileField(blank=True, null=True, upload_to="licenciaConduccion_media")
    categoriaLicencia = models.CharField(max_length=2)
    estadoLicencia = models.BooleanField(blank=True, default=True)
    organismoTransito = models.TextField()
    fechaExpedicion = models.DateField()
    fechaVencimiento = models.DateField()
    restricciones = models.TextField(blank=True, null=True)
    experiencia = models.CharField(max_length=2)  # IntegerField
    activo_inactivo = models.BooleanField(blank=True, default=True)

    def __str__(self):
        full_name = self.nombres + ' ' + self.apellidos
        return full_name
