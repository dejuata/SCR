# -*- encoding:utf-8 -*-
from django import forms

from .models import Vehiculo


class UploadFileForm(forms.Form):
    file = forms.FileField()


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

        TIPO_COMBUSTIBLE = (
            ('', '---------'),
            ('GASOLINA', 'GASOLINA'),
            ('GAS NATURAL VEHICULAR', 'GAS NATURAL VEHICULAR'),
            ('DIESEL', 'DIESEL'),
            ('GASOLINA-GAS', 'GASOLINA-GAS'),
            ('ELÉCTRICO', 'ELÉCTRICO'),
            ('HIDRÓGENO', 'HIDRÓGENO'),
            ('ETANOL', 'ETANOL'),
            ('BIODIESEL', 'BIODIESEL')
        )

        CLASE_VEHICULO = (
            ('', '---------'),
            ('AUTOMÓVIL', 'AUTOMÓVIL'),
            ('BUS', 'BUS'),
            ('BUSETA', 'BUSETA'),
            ('CAMIÓN', 'CAMIÓN'),
            ('CAMIONETA', 'CAMIONETA'),
            ('CAMPERO', 'CAMPERO'),
            ('MICROBÚS', 'MICROBÚS'),
            ('TRACTOCAMIÓN', 'TRACTOCAMIÓN'),
            ('MOTOCICLETA', 'MOTOCICLETA'),
            ('MOTOTRICICLO', 'MOTOTRICICLO'),
            ('CUATRIMOTO', 'CUATRIMOTO'),
            ('VOLQUETA', 'VOLQUETA')
        )

        TIPO_SERVICIO = (
            ('', '---------'),
            ('PARTICULAR', 'PARTICULAR'),
            ('PÚBLICO', 'PÚBLICO'),
            ('DIPLOMÁTICO', 'DIPLOMÁTICO'),
            ('OFICIAL', 'OFICIAL')
        )

        fields = [
                'placa',
                'conductor_default',
                'numero_interno',
                'combustible',
                'logo',

                'numero_licencia_transito',
                'documento_licencia_transito',
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
                'numero_motor',
                'numero_chasis',
                'propietario',
                'id_propietario',

                'numero_tarjeta_operacion',
                'documento_tarjeta_operacion',
                'fecha_inicio_tarjeta_operacion',
                'fecha_vencimiento_tarjeta_operacion',
                'empresa_afiliado',
                'id_empresa_afiliado',

                'numero_soat',
                'documento_soat',
                'fecha_inicio_soat',
                'fecha_vencimiento_soat',
                'aseguradora_soat',

                'numero_certificado_rtm',
                'documento_rtm',
                'fecha_inicio_rtm',
                'fecha_vencimiento_rtm',
                'centro_diagnostico_automotriz',

                'numero_polizas_rce_rcc',
                'documento_polizas_rce_rcc',
                'fecha_inicio_rce_rcc',
                'fecha_vencimiento_rce_rcc',
                'aseguradora_rce_rcc',
        ]

        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '6', 'data-error': 'Ingrese la placa del vehiculo'}),
            'conductor_default': forms.Select(attrs={'class': 'form-control'}),
            'numero_interno': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '6', 'data-error': 'Ingrese el numero interno del vehiculo'}),
            'combustible': forms.Select(choices=TIPO_COMBUSTIBLE, attrs={'class': 'form-control', 'data-error': 'Ingrese tipo de combustible'}),
            'logo': forms.FileInput(),

            'numero_licencia_transito': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese numero de licencia de transito'}),
            'documento_licencia_transito': forms.FileInput(),
            'organismo_transito': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese organismo de transito'}),
            'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese marca del vehiculo'}),
            'linea': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese linea del vehiculo'}),
            'cilindraje': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese cilindraje del vehiculo'}),
            'modelo': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '4', 'data-error': 'Ingrese modelo del vehiculo'}),
            'clase_vehiculo': forms.Select(choices=CLASE_VEHICULO, attrs={'class': 'form-control', 'data-error': 'Ingrese la clase del vehiculo'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese color del vehiculo'}),
            'tipo_servicio': forms.Select(choices=TIPO_SERVICIO, attrs={'class': 'form-control', 'data-error': 'Ingrese tipo de servicio del vehiculo'}),
            'carroceria': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese tipo de carroceria del vehiculo'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '2', 'data-error': 'Ingrese la capacidad del vehiculo'}),
            'numero_motor': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el numero de motor del vehiculo'}),
            'numero_chasis': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el numero de chasis del vehiculo'}),
            'propietario': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese propietario del vehiculo'}),
            'id_propietario': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese identificacion de propietario del vehiculo'}),

            'numero_tarjeta_operacion': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el numero de tarjeta de operacion'}),
            'documento_tajeta_operacion': forms.FileInput(),
            'fecha_inicio_tarjeta_operacion': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'fecha_vencimiento_tarjeta_operacion': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'empresa_afiliado': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese empresa a la que se encuentra afiliado el vehiculo'}),
            'id_empresa_afiliado': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese identificacion de la empresa afiliadora'}),

            'numero_soat': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el numero de SOAT del vehiculo'}),
            'documento_soat': forms.FileInput(),
            'fecha_inicio_soat': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'fecha_vencimiento_soat': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'aseguradora_soat': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la aseguradora que expide el SOAT'}),

            'numero_certificado_rtm': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el numero de la revision tecnicomecanica'}),
            'documento_rtm': forms.FileInput(),
            'fecha_inicio_rtm': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'fecha_vencimiento_rtm': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'centro_diagnostico_automotriz': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el centro de diagnostico automotriz'}),

            'numero_polizas_rce_rcc': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese en numero de las polizas del vehiculo'}),
            'documento_polizas_rce_rcc': forms.FileInput(),
            'fecha_inicio_rce_rcc': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'fecha_vencimiento_rce_rcc': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'aseguradora_rce_rcc': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la aseguradora que expide las polizas'}),
        }
