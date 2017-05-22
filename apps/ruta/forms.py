# -*- encoding:utf-8 -*-
from django import forms

from .models import Ruta


class RutaForm(forms.ModelForm):

    class Meta:
        model = Ruta

        fields = [
            'codRuta',
            'nit',
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
            # 'linkRuta',
        ]
        labels = {
            'codRuta': 'Codigo Ruta',
            'nit': 'NIT',
            'tipo_Ruta': 'Tipo Ruta',
            'tipo_Vehiculo_Requerido': 'Tipo Vehiculo Requerido',
            'origen': 'Origen',
            'destino': 'destino',
            'hora_Inicio': 'Hora inicio',
            'hora_Fin': 'Hora Fin',
            'valor_Hora_Add': 'Valor Hora Adicional',
            'valor_Ruta': 'Valor Ruta',
            'valor_Tercero': 'Valor Tercero',
            'comision_Conductor': 'Comision Conductor',
            'kilometros': 'Kilometros',
            # 'linkRuta': 'link Ruta',
        }
        widgets = {
            'codRuta': forms.NumberInput(attrs={'class': 'form-control'}),
            'nit': forms.Select(attrs={'class': 'form-control'}),
            'tipo_Ruta': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_Vehiculo_Requerido': forms.TextInput(attrs={'class': 'form-control'}),
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_Inicio': forms.NumberInput(attrs={'class': 'form-control'}),
            'hora_Fin': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_Hora_Add': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_Ruta': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_Tercero': forms.NumberInput(attrs={'class': 'form-control'}),
            'comision_Conductor': forms.NumberInput(attrs={'class': 'form-control'}),
            'kilometros': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'linkRuta': forms.TextInput(attrs={'class': 'form-control'}),
        }
