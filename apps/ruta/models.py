from django.db import models

from ..cliente.models import Cliente
#Create your models here.
class Ruta(models.Model):
    codRuta = models.IntegerField(unique=True)
    nit = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    tipo_Ruta = models.CharField(max_length=100)
    tipo_Vehiculo_Requerido = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    hora_Inicio = models.TimeField()
    hora_Fin = models.TimeField()
    valor_Hora_Add = models.IntegerField(null=True)
    valor_Ruta = models.IntegerField()
    valor_Tercero = models.IntegerField(null=True)
    comision_Conductor = models.IntegerField(null=True)
    kilometros = models.IntegerField(null=True)
    #linkRuta = models.CharField(max_length=100,null=True)
    activo_inactivo = models.BooleanField(default=True)
