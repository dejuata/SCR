# -*- encoding:utf-8 -*-
from django import forms

from .models import Tenant


class TenantForm(forms.ModelForm):

    class Meta:
        model = Tenant

        fields = [
            'nit',
            # 'logo',
            'razon_social',
            # 'nombre_comercial',
            'telefono',
            'correo',
            'ciudad',
            'direccion',
        ]
        labels = {
            'nit': 'Nit',
            # 'logo': 'Logo',
            'razon_social': 'Razón social',
            # 'nombre_comercial': 'Nombre Comercial',
            'telefono': 'Teléfono',
            'correo': 'Correo electrónico',
            'ciudad': 'Ciudad',
            'direccion': 'Dirección',
        }
        widgets = {
            'nit': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            # 'nombre_comercial': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
