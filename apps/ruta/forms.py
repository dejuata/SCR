# -*- encoding:utf-8 -*-
from django import forms

from .models import Ruta


class RutaForm(forms.ModelForm):

    class Meta:
        model = Ruta

        fields = [
            'nit',
            'tipo_Ruta',
            'tipo_Vehiculo_Requerido',
            'hora_Inicio',
            'hora_Fin',
            'valor_Hora_Add',
            'valor_Ruta',
            'valor_Tercero',
            'comision_Conductor',
            'kilometros',
            #'linkRuta',
            'activo_inactivo',
        ]
        labels = {
            'nit': 'NIT',
            'tipo_Ruta': 'Tipo Ruta',
            'tipo_Vehiculo_Requerido': 'Tipo Vehiculo Requerido',
            'hora_Inicio': 'Hora inicio',
            'hora_Fin': 'Hora Fin',
            'valor_Hora_Add': 'Valor Hora Adicional',
            'valor_Ruta': 'Valor Ruta',
            'valor_Tercero': 'Valor Tercero',
            'comision_Conductor': 'Comision Conductor',
            'kilometros': 'Kilometros',
            #'linkRuta': 'link Ruta',
            'activo_inactivo': 'Activo/Inactivo',
        }
        widgets = {
            'tipo_Ruta': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_Vehiculo_Requerido': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_Inicio': forms.NumberInput(attrs={'class': 'form-control'}),
            'hora_Fin': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_Hora_Add': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_Ruta': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_Tercero': forms.NumberInput(attrs={'class': 'form-control'}),
            'comision_Conductor': forms.NumberInput(attrs={'class': 'form-control'}),
            #'linkRuta': forms.TextInput(attrs={'class': 'form-control'}),
            'activo_inactivo': forms.TextInput(attrs={'class': 'form-control'}),
        }
