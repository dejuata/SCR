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
            'codRuta',
            'nit',
            'nombre_ruta',
            'tipo_viaje',
            'tipo_Ruta',
            'tipo_Vehiculo_Requerido',
            'origen',
            'destino',
            'hora_Inicio',
            'hora_Fin',
            'valor_Hora_Add',
            'valor_Ruta',
            'valor_Tercero',
            'comision_Conductor',
            'kilometros',
            'linkRuta',
        ]
        labels = {
            'codRuta': 'Codigo Ruta',
            'nit': 'NIT',
            'nombre_ruta': 'Nombre Ruta',
            'tipo_viaje': 'Tipo de Viaje (E/S)',
            'tipo_Ruta': 'Tipo Ruta',
            'tipo_Vehiculo_Requerido': 'Tipo Vehiculo Requerido',
            'origen': 'origen',
            'destino': 'destino',
            'hora_Inicio': 'Hora inicio',
            'hora_Fin': 'Hora Fin',
            'valor_Hora_Add': 'Valor Hora Adicional',
            'valor_Ruta': 'Valor Ruta',
            'valor_Tercero': 'Valor Tercero',
            'comision_Conductor': 'Comision Conductor',
            'kilometros': 'Kilometros',
            'linkRuta': 'LinkRuta',
        }
        widgets = {
            'nit': forms.Select(attrs={'class': 'form-control',
                                            'data-error': "Seleccione el N° NIT del Cliente de la Ruta"}),

            'codRuta': forms.NumberInput(attrs={'class': 'form-control', 'data-error': "Ingrese el codigo de la Ruta"}),

            'nombre_ruta': forms.TextInput(attrs={'class': 'form-control', 'data-error': "Ingrese el nombre de ruta"}),

            'tipo_viaje': forms.Select(choices=TIPO_VIAJE, attrs={'class': 'form-control', 'data-error': "Ingrese el tipo de viaje (Entrada o Salida)"}),

            'tipo_Ruta': forms.TextInput(attrs={'class': 'form-control', 'data-error': "Ingrese el tipo de ruta"}),

            'tipo_Vehiculo_Requerido': forms.TextInput(attrs={'class': 'form-control', 'data-error': "Ingrese el tipo de vehiculo requerido para la ruta"}),

            'origen': forms.TextInput(attrs={'class': 'form-control',
                                             'id': "origen",
                                             'value': "",
                                             'data-error': "Seleccione el origen de la Ruta"}),

            'destino': forms.TextInput(attrs={'class': 'form-control',
                                              'id': "destino",
                                              'value': "",
                                              'data-error': "Seleccione el destino de la Ruta"}),

            'hora_Inicio': forms.TimeInput(attrs={'type':'time', 'class': 'form-control', 'data-error': "Ingrese la hora de inicio de la ruta"}),

            'hora_Fin': forms.TimeInput(attrs={'type':'time', 'class': 'form-control', 'data-error': "Ingrese la hora de finalizacion de la ruta"}),

            'valor_Hora_Add': forms.NumberInput(attrs={'class': 'form-control', 'data-error': "Ingrese el valor adicional/hora para la ruta"}),

            'valor_Ruta': forms.NumberInput(attrs={'class': 'form-control', 'data-error': "Ingrese el valor que tiene la ruta"}),

            'valor_Tercero': forms.NumberInput(attrs={'class': 'form-control', 'data-error': "Ingrese el valor para el Tercero que realiza la ruta"}),

            'comision_Conductor': forms.NumberInput(attrs={'class': 'form-control', 'data-error': "Ingrese la comision para el conductor de la ruta"}),

            'kilometros': forms.NumberInput(attrs={'class': 'form-control',
                                            'id': "kilometros",
                                            'value': "",
                                            'data-error': "Ingrese los Km de la ruta"}),

            'linkRuta': forms.TextInput(attrs={'class': 'form-control',
                                        'id': "linkRuta",
                                        'value': "",
                                        'data-error': "Ingrese el link de la ruta", 'disabled':'True'})
        }
