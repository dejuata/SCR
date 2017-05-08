# -*- encoding:utf-8 -*-
from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['nit'].widget.attrs['readonly'] = True

    def clean_nit(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.nit
        else:
            return self.cleaned_data['nit']

    class Meta:
        model = Cliente

        fields = [
            'nit',
            'razon_social',
            'logo',
            'telefono',
            'correo',
            'ciudad',
            'direccion',
        ]
        labels = {
            'nit': 'NIT',
            'razon_social': 'Razon Social',
            'logo': 'Logo',
            'telefono': 'Telefono',
            'correo': 'Correo',
            'ciudad': 'Ciudad',
            'direccion': 'Direccion',
        }
        widgets = {
            'nit': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el N° NIT de la empresa'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la Razón Social de la empresa'}),
            'logo': forms.FileInput(),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '12', 'data-error': 'Ingrese el Teléfono de la empresa'}),
            'correo': forms.TextInput(attrs={'class': 'form-control',
                                             'pattern': '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$',
                                             'data-error': 'Ingrese el Correo de la empresa'
                                             }),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la ciudad donde esta ubicada la empresa'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la dirección de la empresa'}),
        }
