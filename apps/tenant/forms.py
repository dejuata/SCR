# -*- encoding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User

from .models import Tenant


class TenantForm(forms.ModelForm):

    class Meta:
        model = Tenant

        fields = [
            'nit',
            'user',
            # 'logo',
            'razon_social',
            'nombre_comercial',
            'telefono',
            'correo',
            'ciudad',
            'direccion',
        ]
        labels = {
            'nit': 'Nit',
            # 'logo': 'Logo',
            'razon_social': 'Razón social',
            'nombre_comercial': 'Nombre Comercial',
            'telefono': 'Teléfono',
            'correo': 'Correo electrónico',
            'ciudad': 'Ciudad',
            'direccion': 'Dirección',
        }
        widgets = {
            'nit': forms.NumberInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(),
            # 'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class': 'form-control',
                                                        'data-container': 'body',
                                                        'data-toggle': 'popover',
                                                        'data-placement': 'top',
                                                        'data-content': 'Tenga en cuenta que con el Nombre comercial, se genera la URL a la cual debera acceder. Ejemplo: https://nombreComercial.scr.com'
                                                        }),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
