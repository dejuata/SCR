from django.db import models

from ..ruta.models import Ruta
from ..vehiculo.models import Vehiculo
from ..conductor.models import Conductor


class Planilla(models.Model):

    fecha = models.DateField()
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    kilometros = models.FloatField()
    hora_adicional = models.IntegerField(blank=True, null=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    tiempo_operado = models.FloatField()
    placa = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    novedades = models.CharField(max_length=100, blank=True, null=True)
    flota = models.CharField(max_length=100)
    valor_ruta = models.IntegerField(default='')
    valor_tercero = models.IntegerField(blank=True, null=True)
    viaticos = models.IntegerField(blank=True, null=True)
    descuentos_conductor = models.IntegerField(blank=True, null=True)
    valor_hora_adicional = models.IntegerField(blank=True, null=True)
    adicional_conductor = models.IntegerField(blank=True, null=True)
    total_ingreso = models.IntegerField()

    def __str__(self):
        return self.fecha
