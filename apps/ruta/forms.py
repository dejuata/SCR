# -*- encoding:utf-8 -*-
from django import forms

from .models import Ruta


class RutaForm(forms.ModelForm):

    class Meta:
        model = Ruta

        TIPO_VIAJE = (
            ('entrada', 'ENTRADA'),
            ('salida', 'SALIDA')
        )

        fields = [
            'codigo_ruta',
            'nit',
            'nombre_ruta',
            'tipo_viaje',
            'tipo_ruta',
            'tipo_vehiculo_requerido',
            'origen',
            'destino',
            'hora_inicio',
            'hora_fin',
            'valor_hora_adicional',
            'valor_ruta',
            'valor_tercero',
            'comision_conductor',
            'kilometros',
            'link_ruta',
        ]
        widgets = {
            'nit': forms.Select(attrs={'class': 'form-control',
                                            'data-error': "Seleccione el N° NIT del Cliente de la Ruta"}),

            'codigo_ruta': forms.NumberInput(attrs={'class': 'form-control', 'data-error': "Ingrese el codigo de la Ruta"}),

            'nombre_ruta': forms.TextInput(attrs={'class': 'form-control', 'data-error': "Ingrese el nombre de ruta"}),

            'tipo_viaje': forms.Select(choices=TIPO_VIAJE, attrs={'class': 'form-control', 'data-error': "Ingrese el tipo de viaje (Entrada o Salida)"}),

            'tipo_ruta': forms.TextInput(attrs={'class': 'form-control', 'data-error': "Ingrese el tipo de ruta"}),

            'tipo_vehiculo_requerido': forms.TextInput(attrs={'class': 'form-control', 'data-error': "Ingrese el tipo de vehiculo requerido para la ruta"}),

            'origen': forms.TextInput(attrs={'class': 'form-control',
                                             'id': "origen",
                                             'value': "",
                                             'data-error': "Seleccione el origen de la Ruta"}),

            'destino': forms.TextInput(attrs={'class': 'form-control',
                                              'id': "destino",
                                              'value': "",
                                              'data-error': "Seleccione el destino de la Ruta"}),

            'hora_inicio': forms.TimeInput(attrs={'type':'time', 'class': 'form-control', 'data-error': "Ingrese la hora de inicio de la ruta"}),

            'hora_fin': forms.TimeInput(attrs={'type':'time', 'class': 'form-control', 'data-error': "Ingrese la hora de finalizacion de la ruta"}),

            'valor_hora_adicional': forms.NumberInput(attrs={'class': 'form-control', 'data-error': "Ingrese el valor adicional/hora para la ruta"}),

            'valor_ruta': forms.NumberInput(attrs={'class': 'form-control', 'data-error': "Ingrese el valor que tiene la ruta"}),

            'valor_tercero': forms.NumberInput(attrs={'class': 'form-control', 'data-error': "Ingrese el valor para el Tercero que realiza la ruta"}),

            'comision_conductor': forms.NumberInput(attrs={'class': 'form-control', 'data-error': "Ingrese la comision para el conductor de la ruta"}),

            'kilometros': forms.NumberInput(attrs={'class': 'form-control',
                                            'id': "kilometros",
                                            'value': "",
                                            'data-error': "Ingrese los Km de la ruta"}),

            'link_ruta': forms.HiddenInput(attrs={'class': 'form-control',
                                        'id': "linkRuta",
                                        'value': "",
                                        'data-error': "Ingrese el link de la ruta", 'disabled':'True'})
        }
