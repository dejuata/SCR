from django.db import models

from ..cliente.models import Cliente


class Ruta(models.Model):
    codigo_ruta = models.IntegerField(primary_key=True, unique=True)
    nit = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    nombre_ruta = models.CharField(default='', max_length=60)
    tipo_viaje = models.CharField(default='', max_length=10)
    tipo_ruta = models.CharField(max_length=100)
    tipo_vehiculo_requerido = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    valor_hora_adicional = models.IntegerField(null=True, blank=True)
    valor_ruta = models.IntegerField()
    valor_tercero = models.IntegerField(null=True, blank=True)
    comision_conductor = models.IntegerField(null=True, blank=True)
    kilometros = models.FloatField(null=True, blank=True, max_length=10)
    link_ruta = models.CharField(null=True, blank=True, max_length=1000)
    activo_inactivo = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_Ruta
