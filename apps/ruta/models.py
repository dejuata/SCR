from django.db import models

from ..cliente.models import Cliente


class Ruta(models.Model):
    codRuta = models.IntegerField(primary_key=True, unique=True)
    nit = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    nombre_ruta = models.CharField(default='', max_length=60)
    tipo_viaje = models.CharField(default='', max_length=10)
    tipo_Ruta = models.CharField(max_length=100)
    tipo_Vehiculo_Requerido = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    hora_Inicio = models.TimeField()
    hora_Fin = models.TimeField()
    valor_Hora_Add = models.IntegerField(null=True, blank=True)
    valor_Ruta = models.IntegerField()
    valor_Tercero = models.IntegerField(null=True, blank=True)
    comision_Conductor = models.IntegerField(null=True, blank=True)
    kilometros = models.FloatField(null=True, blank=True, max_length=10)
    linkRuta = models.CharField(null=True,blank=True,max_length=1000)
    activo_inactivo = models.BooleanField(default=True)
