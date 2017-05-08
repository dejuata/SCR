# -*- encoding:utf-8 -*-
from django import forms

# from captcha.fields import ReCaptchaField
from .models import Tenant


class TenantForm(forms.ModelForm):
    #
    # captcha = ReCaptchaField(
    # public_key='76wtgdfsjhsydt7r5FFGFhgsdfytd656sad75fgh',
    # private_key='98dfg6df7g56df6gdfgdfg65JHJH656565GFGFGs',
    # )

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
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            # 'captcha': ReCaptchaField(attrs={'theme': 'clean'}),
        }

    def clean_nombre_comercial(self):
        nombre_comercial = self.cleaned_data['nombre_comercial']
<<<<<<< HEAD
        if nombre_comercial.isupper() or (nombre_comercial.find(" ")>0) or not(nombre_comercial.islower()):

=======
        if nombre_comercial.isupper() or not(nombre_comercial.islower()) or (nombre_comercial.find(' ') > 0):
>>>>>>> ddf05e70fa213cf41ac142e0becfdaf28d1de99f
            self.add_error('nombre_comercial', 'El nombre comercial debe ir en minusculas')
        else:
            return self.cleaned_data['nombre_comercial']
