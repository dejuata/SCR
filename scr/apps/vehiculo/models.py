from django.db import models
from apps.conductor.models import Conductor
from django.core import serializers


class Vehiculo(models.Model):
    placa = models.CharField(primary_key=True, max_length=6)
    conductor_default = models.ForeignKey(Conductor, blank=True, null=True, on_delete=models.CASCADE)
    numero_interno = models.CharField(max_length=6)
    combustible = models.CharField(max_length=20)
    logo = models.ImageField(blank=True, null=True, upload_to="vehiculo_media")

    numero_licencia_transito = models.IntegerField()
    documento_licencia_transito = models.FileField(blank=True, null=True, upload_to="licenciaTransito_media")
    organismo_transito = models.TextField()
    fecha_expedicion = models.DateField()
    marca = models.CharField(max_length=30)
    linea = models.CharField(max_length=30)
    cilindraje = models.IntegerField()
    modelo = models.IntegerField()
    clase_vehiculo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    tipo_servicio = models.CharField(max_length=30)
    carroceria = models.CharField(max_length=30)
    capacidad = models.IntegerField()
    numero_motor = models.TextField()
    numero_chasis = models.TextField()
    propietario = models.TextField()
    id_propietario = models.IntegerField()

    numero_tarjeta_operacion = models.CharField(max_length=15, null=True)# coloco null
    documento_tarjeta_operacion = models.FileField(blank=True, null=True, upload_to="TarjetasOperacion_media")
    fecha_inicio_tarjeta_operacion = models.DateField(null=True)# coloco null
    fecha_vencimiento_tarjeta_operacion = models.DateField(null=True)# coloco null
    empresa_afiliado = models.TextField(null=True) # coloco null
    id_empresa_afiliado = models.IntegerField(null=True)# coloco null

    numero_soat = models.CharField(max_length=15)
    documento_soat = models.FileField(blank=True, null=True, upload_to="Soat_media")
    fecha_inicio_soat = models.DateField()
    fecha_vencimiento_soat = models.DateField()
    aseguradora_soat = models.TextField()

    numero_certificado_rtm = models.CharField(max_length=15)
    documento_rtm = models.FileField(blank=True, null=True, upload_to="RevisionTecnicoMecanica_media")
    fecha_inicio_rtm = models.DateField()
    fecha_vencimiento_rtm = models.DateField()
    centro_diagnostico_automotriz = models.TextField()

    numero_polizas_rce_rcc = models.CharField(max_length=15, blank=True, null=True)
    documento_polizas_rce_rcc = models.FileField(blank=True, null=True, upload_to="PolizasRcc_Rce_media")
    fecha_inicio_rce_rcc = models.DateField()
    fecha_vencimiento_rce_rcc = models.DateField()
    aseguradora_rce_rcc = models.TextField()

    activo_inactivo = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.placa
