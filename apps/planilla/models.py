from django.db import models

from ..ruta.models import Ruta
from ..vehiculo.models import Vehiculo
from ..conductor.models import Conductor


class Planilla(models.Model):

    fecha = models.DateField()
    ruta = models.OneToOneField(Ruta, on_delete=models.CASCADE)
    kilometros = models.FloatField()
    hora_adicional = models.IntegerField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    tiempo_operado = models.TimeField()
    entrada = models.BooleanField()
    salida = models.BooleanField()
    placa = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
    conductor = models.OneToOneField(Conductor, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=100)
    novedades = models.CharField(max_length=100)
    flota = models.CharField(max_length=100)
    valor_tercero = models.IntegerField()
    viaticos = models.IntegerField()
    descuentos_conductor = models.IntegerField()
    valor_hora_adicional = models.IntegerField()
    adicional_conductor = models.IntegerField()
    total_ingreso = models.IntegerField()
