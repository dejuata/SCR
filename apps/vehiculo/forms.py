# -*- encoding:utf-8 -*-
from django import forms

from .models import Vehiculo


class VehiculoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VehiculoForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['placa'].widget.attrs['readonly'] = True

    def clean_placa(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.placa
        else:
            return self.cleaned_data['placa']

    class Meta:
        model = Vehiculo

        fields = [
                'placa',
                'conductor_default',
                'numero_interno',
                'combustible',
                'logo',
                'num_licencia_transito',
                'doc_licencia_transito',
                'organismo_transito',
                'fecha_expedicion',
                'marca',
                'linea',
                'cilindraje',
                'modelo',
                'clase_vehiculo',
                'color',
                'tipo_servicio',
                'carroceria',
                'capacidad',
                'num_motor',
                'num_chasis',
                'propietario',
                'id_propietario',
                'num_tarjeta_operacion',
                'doc_to',
                'fecha_inicio_to',
                'fecha_vencimiento_to',
                'empresa_afiliado',
                'id_empresa_afiliado',
                'num_soat',
                'doc_soat',
                'fecha_inicio_soat',
                'fecha_vencimiento_soat',
                'aseguradora_soat',
                'num_certificado_rtm',
                'doc_rtm',
                'fecha_inicio_rtm',
                'fecha_vencimiento_rtm',
                'cda',
                'numero_polizas_rce_rcc',
                'doc_polizas_rce_rcc',
                'fecha_inicio_rce_rcc',
                'fecha_vencimiento_rce_rcc',
                'aseguradora_rce_rcc',
        ]

        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '6', 'data-error': 'Ingrese la placa del vehiculo'}),
            'conductor_default': forms.Select(attrs={'class': 'form-control'}),
            'numero_interno': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '6', 'data-error': 'Ingrese el numero interno del vehiculo'}),
            'combustible': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese tipo de combustible'}),
            'logo': forms.FileInput(),
            'num_licencia_transito': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese numero de licencia de transito'}),
            'doc_licencia_transito': forms.FileInput(),
            'organismo_transito': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese organismo de transito'}),
            'fecha_expedicion': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese marca del vehiculo'}),
            'linea': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese linea del vehiculo'}),
            'cilindraje': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese cilindraje del vehiculo'}),
            'modelo': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '4', 'data-error': 'Ingrese modelo del vehiculo'}),
            'clase_vehiculo': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la clase del vehiculo'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese color del vehiculo'}),
            'tipo_servicio': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese tipo de servicio del vehiculo'}),
            'carroceria': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese tipo de carroceria del vehiculo'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '2', 'data-error': 'Ingrese la capacidad del vehiculo'}),
            'num_motor': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el numero de motor del vehiculo'}),
            'num_chasis': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el numero de chasis del vehiculo'}),
            'propietario': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese propietario del vehiculo'}),
            'id_propietario': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese identificacion de propietario del vehiculo'}),
            'num_tarjeta_operacion': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el numero de tarjeta de operacion'}),
            'doc_to': forms.FileInput(),
            'fecha_inicio_to': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'fecha_vencimiento_to': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'empresa_afiliado': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese empresa a la que se encuentra afiliado el vehiculo'}),
            'id_empresa_afiliado': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese identificacion de la empresa afiliadora'}),
            'num_soat': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el numero de SOAT del vehiculo'}),
            'doc_soat': forms.FileInput(),
            'fecha_inicio_soat': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'fecha_vencimiento_soat': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'aseguradora_soat': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la aseguradora que expide el SOAT'}),
            'num_certificado_rtm': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el numero de la revision tecnicomecanica'}),
            'doc_rtm': forms.FileInput(),
            'fecha_inicio_rtm': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'fecha_vencimiento_rtm': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'cda': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el centro de diagnostico automotriz'}),
            'numero_polizas_rce_rcc': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese en numero de las polizas del vehiculo'}),
            'doc_polizas_rce_rcc': forms.FileInput(),
            'fecha_inicio_rce_rcc': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'fecha_vencimiento_rce_rcc': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'aseguradora_rce_rcc': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la aseguradora que expide las polizas'}),
        }
