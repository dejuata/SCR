# -*- encoding:utf-8 -*-
from django import forms

from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from .models import Tenant
from ..cities.forms import departamento_widget, ciudad_widget


class TenantForm(forms.ModelForm):

    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    departamento = departamento_widget()
    ciudad = ciudad_widget()

    class Meta:
        model = Tenant

        fields = [
            'nit',
            'user',
            'logo',
            'razon_social',
            'nombre_comercial',
            'telefono',
            'correo',
            'departamento',
            'ciudad',
            'direccion',
        ]
        labels = {
            'nit': 'Nit',
            'user': 'id_user',
            'logo': 'Logo',
            'razon_social': 'Razón social',
            'nombre_comercial': 'Nombre Comercial',
            'telefono': 'Teléfono Corporativo',
            'correo': 'Correo Corporativo',
            'departamento': 'Departamento',
            'ciudad': 'Ciudad',
            'direccion': 'Dirección',
        }
        widgets = {
            'nit': forms.NumberInput(attrs={'class': 'form-control'}),
            'user': forms.NumberInput(),
            'logo': forms.FileInput(),
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class': 'form-control',
                                                       'data-container': 'body',
                                                       'data-toggle': 'popover',
                                                       'data-placement': 'top',
                                                       'data-content': 'Tenga en cuenta que con el Nombre comercial, se genera la URL a la cual debera acceder. Ejemplo: https://nombreComercial.scr.com'
                                                       }),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'departamento':  forms.TextInput(attrs={'class': 'form-control'}),
            # 'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre_comercial(self):
        nombre_comercial = self.cleaned_data['nombre_comercial']
        if nombre_comercial.isupper() or not(nombre_comercial.islower()) or (nombre_comercial.find(' ') > 0):
        if nombre_comercial.isupper() or (nombre_comercial.find(" ") > 0) or not(nombre_comercial.islower()):
            self.add_error('nombre_comercial', 'El nombre comercial debe ir en minusculas y sin espacios')
        else:
            return self.cleaned_data['nombre_comercial']
