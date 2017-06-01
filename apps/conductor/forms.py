# -*- encoding:utf-8 -*-
from django import forms
from os import path
from os.path import os
from datetime import date

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

        NIVEL_ESCOLARIDAD = (
            ('----', '----'),
            ('primaria', 'Primaria'),
            ('bachiller', 'Bachiller'),
            ('tecnico', 'Técnico'),
            ('tecnologo', 'Tecnólogo'),
            ('profesional', 'Profesional'),
        )

        CATEGORIA_LICENCIA = (
            ('--', '--'),
            ('C1', 'C1'),
            ('C2', 'C2'),
            ('C3', 'C3'),
        )

        TIPO_SANGRE = (
            ('--', '--'),
            ('O+', 'O+'),
            ('O-', 'O-'),
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
        )

        fields = [
            'cedula',
            'nombres',
            'apellidos',
            'logo',
            'direccion',
            'rh',
            'telefono',
            'celular',
            'correo',
            'fecha_nacimiento',
            'nivel_estudio',
            'numero_licencia_conduccion',
            'documento_licencia_conduccion',
            'categoria_licencia',
            'estado_licencia',
            'organismo_transito',
            'fecha_expedicion',
            'fecha_vencimiento',
            'restricciones',
            'experiencia',
        ]

        widgets = {
            'cedula': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el N° de Cedula del conductor'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese los Nombres del conductor'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese los Apellidos del conductor'}),
            'logo': forms.FileInput(attrs={'accept': 'png, .jpeg, .jpg'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la dirección del conductor'}),
            'rh': forms.Select(choices=TIPO_SANGRE, attrs={'class': 'form-control', 'maxlength': '2', 'data-error': 'Ingrese el tipo de sangre del conductor'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '7'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10', 'data-error': 'Ingrese el Teléfono del conductor'}),
            'correo': forms.TextInput(attrs={'class': 'form-control',
                                             'pattern': '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$',
                                             }),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control datepicker', }),
            'nivel_estudio': forms.Select(choices=NIVEL_ESCOLARIDAD, attrs={'class': 'form-control', 'data-error': 'Ingrese el nivel de escolaridad del conductor'}),
            'num_licencia_conduccion': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el N° de licencia de conducción'}),
            'doc_licencia_conduccion': forms.FileInput(attrs={'accept': '.pdf'}),
            'categoria_licencia': forms.Select(choices=CATEGORIA_LICENCIA, attrs={'class': 'form-control', 'maxlength': '2', 'data-error': 'Ingrese la categoria de la licencia'}),
            'estado_licencia': forms.CheckboxInput(),
            'organismo_transito': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese organismo de transito de la licencia'}),
            'fecha_expedicion': forms.TextInput(attrs={'class': 'form-control datepicker', }),
            'fecha_vencimiento': forms.TextInput(attrs={'class': 'form-control datepicker', }),
            'restricciones': forms.TextInput(attrs={'class': 'form-control', }),
            'experiencia': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '2'}),
        }

    #  validators
    def clean(self):
        cleaned_data = self.cleaned_data
        fecha_expedicion = cleaned_data["fecha_expedicion"]
        fecha_vencimiento = cleaned_data["fecha_vencimiento"]
        if fecha_expedicion > date.today():
            self.add_error('fecha_expedicion', 'La fecha de expedicion no puede superar la fecha actual')
        elif fecha_vencimiento <= fecha_expedicion:
            self.add_error('fecha_vencimiento', 'la fecha de vencimiento no puede ser menor a la de expedicion')
        else:
            return self.cleaned_data['fecha_expedicion'] and self.cleaned_data['fecha_vencimiento']

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data["fecha_nacimiento"]
        if fecha_nacimiento >= date.today():
            self.add_error('fecha_nacimiento', 'La fecha de nacimiento no puede superar la fecha actual')
        else:
            return self.cleaned_data['fecha_nacimiento']

    def clean_rh(self):
        rh = self.cleaned_data["rh"]
        print(rh)
        if rh == "--":
            self.add_error('rh', 'Seleccione un tipo de sangre')
        else:
            return self.cleaned_data['rh']

    def clean_doc_licencia_conduccion(self):
        doc_licencia_conduccion = self.cleaned_data["doc_licencia_conduccion"]
        # tam = os.path.getsize(doc_licencia_conduccion.name)
        # print(tam)
        if not(doc_licencia_conduccion is None):
            if doc_licencia_conduccion.name.count(".pdf") == 0:
                self.add_error('doc_licencia_conduccion', 'El archivo licencia de transito debe ser PDF')
        else:
            return self.cleaned_data['doc_licencia_conduccion']

    def clean_logo(self):
        logo = self.cleaned_data["logo"]
        # tam = os.path.getsize(logo.name)
        # print(tam)
        if not(logo is None):
            if logo.name.count(".png") == 0 and logo.name.count(".jpeg") == 0 and logo.name.count(".jpg") == 0:
                self.add_error('logo', 'La foto debe ser una imagen')
        else:
            return self.cleaned_data['logo']
