# -*- encoding:utf-8 -*-
from django import forms
from .models import Planilla


class UploadFileForm(forms.Form):
    file = forms.FileField()


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
            'placa',
            'conductor',
            'observaciones',
            'novedades',
            'flota',
            'valor_ruta',
            'valor_tercero',
            'viaticos',
            'descuentos_conductor',
            'valor_hora_adicional',
            'adicional_conductor',
            'total_ingreso',
        ]

        widgets = {
            'fecha': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'ruta': forms.Select(attrs={'class': 'form-control', 'data-error': 'Seleccione la ruta'}),
            'kilometros': forms.NumberInput(attrs={'class': 'form-control'}),
            'hora_adicional': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '2', 'id': 'hora_adicional'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control',  'type': 'Time', 'id': 'hora_inicio', 'onkeyup': 'timeop(); return false'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'Time', 'id': 'hora_fin', 'onkeyup': 'timeop(); return false'}),
            'tiempo_operado': forms.NumberInput(attrs={'class': 'form-control', 'id': 'tiempo_operado'}),
            'placa': forms.Select(attrs={'class': 'form-control', 'data-error': 'Seleccione el vehiculo'}),
            'conductor': forms.Select(attrs={'class': 'form-control', 'data-error': 'Seleccione el conductor'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'novedades': forms.TextInput(attrs={'class': 'form-control'}),
            'flota': forms.Select(choices=FLOTA, attrs={'class': 'form-control', 'data-error': 'Selecione la flota', 'id': 'flota'}),
            'valor_ruta': forms.NumberInput(attrs={'class': 'form-control', 'value': '0',  'id': 'valor_ruta', 'onkeyup': 'total(); return false'}),
            'valor_tercero': forms.NumberInput(attrs={'class': 'form-control', 'value': '0', 'id': 'valor_tercero', 'onkeyup': 'total(); return false'}),
            'viaticos': forms.NumberInput(attrs={'class': 'form-control', 'value': '0', 'id': 'viaticos', 'onkeyup': 'total(); return false'}),
            'descuentos_conductor': forms.NumberInput(attrs={'class': 'form-control', 'value': '0', 'id': 'descuentos_conductor', 'onkeyup': 'total(); return false'}),
            'valor_hora_adicional': forms.NumberInput(attrs={'class': 'form-control', 'value': '0', 'id': 'valor_hora_adicional', 'onkeyup': 'total(); return false'}),
            'adicional_conductor': forms.NumberInput(attrs={'class': 'form-control', 'value': '0', 'id': 'adicional_conductor', 'onkeyup': 'total(); return false'}),
            'total_ingreso': forms.NumberInput(attrs={'class': 'form-control', 'id': 'total_ingreso'}),
        }
