from django.db import models


class Conductor(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, null=True, upload_to="Conductor_media", validators='')
    direccion = models.TextField()
    rh = models.CharField(max_length=2)
    telefono = models.CharField(max_length=7, blank=True, null=True)
    celular = models.CharField(max_length=10)
    correo = models.EmailField(blank=True, null=True)
    fecha_nacimiento = models.DateField()
    nivel_estudio = models.TextField()
    numero_licencia_conduccion = models.IntegerField()
    documento_licencia_conduccion = models.FileField(blank=True, null=True, upload_to="licenciaConduccion_media")
    categoria_licencia = models.CharField(max_length=2)
    estado_licencia = models.BooleanField(blank=True, default=True)
    organismo_transito = models.TextField()
    fecha_expedicion = models.DateField()
    fecha_vencimiento = models.DateField()
    restricciones = models.TextField(blank=True, null=True)
    experiencia = models.CharField(max_length=2)  # IntegerField
    activo_inactivo = models.BooleanField(blank=True, default=True)

    def __str__(self):
        full_name = self.nombres + ' ' + self.apellidos
        return full_name
