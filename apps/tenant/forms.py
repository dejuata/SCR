# -*- encoding:utf-8 -*-
from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

from .models import Tenant


# class UserTenantForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#         ]
#         labels = {
#             'username': 'Nombre de usuario',
#             'first_name': 'Nombre',
#             'last_name': 'Apellidos',
#             'email': 'Correo',
#         }


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
