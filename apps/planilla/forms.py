# -*- encoding:utf-8 -*-
from django import forms

from .models import Planilla


class PlanillaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PlanillaForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['fecha'].widget.attrs['readonly'] = True

    class Meta:
        model = Planilla

        FLOTA = (
            ('propia', 'Propia'),
            ('afiliado', 'Afiliado'),
            ('tercero', 'Tercero'),

        )

        fields = [
            'fecha',
            'ruta',
            'kilometros',
            'hora_adicional',
            'hora_inicio',
            'hora_fin',
            'tiempo_operado',
            'entrada',
            'salida',
            'placa',
            'conductor',
            'observaciones',
            'novedades',
            'flota',
            'valor_tercero',
            'viaticos',
            'descuentos_conductor',
            'valor_hora_adicional',
            'adicional_conductor',
            'total_ingreso',
        ]

        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'ruta': forms.Select(attrs={'class': 'form-control', 'data-error': 'Seleccione la ruta'}),
            'kilometros': forms.NumberInput(attrs={'class': 'form-control'}),
            'hora_adicional': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '2'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control'}),
            'tiempo_operado': forms.TimeInput(attrs={'class': 'form-control'}),
            'entrada': forms.CheckboxInput(),
            'salida': forms.CheckboxInput(),
            'placa': forms.Select(attrs={'class': 'form-control', 'data-error': 'Seleccione el vehiculo'}),
            'conductor': forms.Select(attrs={'class': 'form-control', 'data-error': 'Seleccione el conductor'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'novedades': forms.TextInput(attrs={'class': 'form-control'}),
            'flota': forms.Select(choices=FLOTA, attrs={'class': 'form-control', 'data-error': 'Selecione la flota'}),
            'valor_tercero': forms.NumberInput(attrs={'class': 'form-control'}),
            'viaticos': forms.NumberInput(attrs={'class': 'form-control'}),
            'descuentos_conductor': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_hora_adicional': forms.NumberInput(attrs={'class': 'form-control'}),
            'adicional_conductor': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_ingreso': forms.NumberInput(attrs={'class': 'form-control'}),
        }
