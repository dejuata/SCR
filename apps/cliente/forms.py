# -*- encoding:utf-8 -*-
from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):

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
            'nit': forms.NumberInput(attrs={'class': 'form-control'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control',
                                             'pattern': '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$',
                                             }),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
