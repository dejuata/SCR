from django.db import models

from ..ruta.models import Ruta
from ..vehiculo.models import Vehiculo
from ..conductor.models import Conductor


class PlanillaManager(models.Manager):
    def create_planilla(self, ruta,
                        hora_inicio,
                        hora_fin,
                        hora_adicional,
                        tiempo_operado,
                        placa,
                        conductor,
                        kilometros,
                        observaciones,
                        novedades,
                        flota,
                        valor_ruta,
                        valor_tercero,
                        valor_hora_adicional,
                        viaticos,
                        descuentos_conductor,
                        adicional_conductor,
                        total_ingreso
                        ):
        planilla = self.create(ruta=ruta,
                               hora_inicio=hora_inicio,
                               hora_fin=hora_fin,
                               hora_adicional=hora_adicional,
                               tiempo_operado=tiempo_operado,
                               conductor=conductor,
                               kilometros=kilometros,
                               observaciones=observaciones,
                               novedades=novedades,
                               flota=flota,
                               valor_ruta=valor_ruta,
                               valor_tercero=valor_tercero,
                               valor_hora_adicional=valor_hora_adicional,
                               viaticos=viaticos,
                               descuentos_conductor=descuentos_conductor,
                               adicional_conductor=adicional_conductor,
                               placa=placa,
                               total_ingreso=total_ingreso
                               )
        return planilla


class Header(models.Model):
    fecha = models.DateField(unique=True)
    template = models.BooleanField(default=False)

    def __str__(self):
        return str(self.fecha)


class Planilla(models.Model):
    fecha = models.ForeignKey(Header, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, null=True)
    kilometros = models.FloatField(default=0, null=True)
    hora_adicional = models.IntegerField(default=0, null=True)
    hora_inicio = models.TimeField(null=True)
    hora_fin = models.TimeField(null=True)
    tiempo_operado = models.FloatField(null=True)
    placa = models.ForeignKey(Vehiculo, null=True)
    conductor = models.ForeignKey(Conductor, null=True)
    observaciones = models.TextField(blank=True, null=True)
    novedades = models.CharField(max_length=100, blank=True, null=True)
    flota = models.CharField(max_length=100, null=True)  # lo coloque null
    valor_ruta = models.IntegerField(default=0, null=True)
    valor_tercero = models.IntegerField(default=0, null=True)
    viaticos = models.IntegerField(default=0, null=True)
    descuentos_conductor = models.IntegerField(default=0, null=True)
    valor_hora_adicional = models.IntegerField(default=0, null=True)
    adicional_conductor = models.IntegerField(default=0, null=True)
    total_ingreso = models.IntegerField(null=True)

    # objects = PlanillaManager()

    def __str__(self):
        return self.ruta
