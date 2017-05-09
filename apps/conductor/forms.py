# -*- encoding:utf-8 -*-
from django import forms

from .models import Conductor


class ConductorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConductorForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['cedula'].widget.attrs['readonly'] = True

    def clean_cedula(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.cedula
        else:
            return self.cleaned_data['cedula']

    class Meta:
        model = Conductor

        fields = [
            'cedula',
            'nombres',
            'apellidos',
            'foto',
            'direccion',
            'rh',
            'telefono',
            'celular',
            'correo',
            'fechaNacimiento',
            'nivelEstudio',
            'numLicenciaConduccion',
            'docLicenciaConduccion',
            'categoriaLicencia',
            'estadoLicencia',
            'organismoTransito',
            'fechaExpedicion',
            'fechaVencimiento',
            'restricciones',
            'experiencia',
        ]
        labels = {
            'cedula': 'Cedula',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'foto': 'Foto',
            'direccion': 'Direccion',
            'rh': 'Tipo de Sangre (RH)',
            'telefono': 'Telefono',
            'celular': 'Celular',
            'correo': 'Correo',
            'fechaNacimiento': 'Fecha de nacimiento',
            'nivelEstudio': 'Nivel de escolaridad',
            'numLicenciaConduccion': 'Numero de liccencia',
            'docLicenciaConduccion': 'Documento Licencia',
            'categoriaLicencia': 'Categoria',
            'estadoLicencia': 'Estado',
            'organismoTransito': 'Orgnismo de transito',
            'fechaExpedicion': 'Fecha de expedición',
            'fechaVencimiento': 'Fecha de vencimiento',
            'restricciones': 'Restricciones de conducción',
            'experiencia': 'Años de experiencia',
        }
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el N° de Cedula del conductor'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese los Nombres del conductor'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese los Apellidos del conductor'}),
            'foto': forms.FileInput(),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la dirección del conductor'}),
            'rh': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2', 'data-error': 'Ingrese el tipo de sangre del conductor'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '7'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10', 'data-error': 'Ingrese el Teléfono del conductor'}),
            'correo': forms.TextInput(attrs={'class': 'form-control',
                                             'pattern': '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$',
                                             }),
            'fechaNacimiento': forms.DateInput(),
            'nivelEstudio': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el nivel de escolaridad del conductor'}),
            'numLicenciaConduccion': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el N° de licencia de conducción'}),
            'docLicenciaConduccion': forms.FileInput(),
            'categoriaLicencia': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2', 'data-error': 'Ingrese la categoria de la licencia'}),
            'estadoLicencia': forms.CheckboxInput(),
            'organismoTransito': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese organismo de transito de la licencia'}),
            'fechaExpedicion': forms.DateInput(),
            'fechaVencimiento': forms.DateInput(),
            'restricciones': forms.TextInput(),
            'experiencia': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2'}),
        }
