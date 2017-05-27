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

        NIVEL_ESCOLARIDAD = (
            ('primaria', 'Primaria'),
            ('bachiller', 'Bachiller'),
            ('tecnico', 'Técnico'),
            ('tecnologo', 'Tecnólogo'),
            ('profesional', 'Profesional'),
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
            'num_licencia_conduccion',
            'doc_licencia_conduccion',
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
            'logo': forms.FileInput(attrs={'accept': 'image/png, .jpeg, .jpg'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese la dirección del conductor'}),
            'rh': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2', 'data-error': 'Ingrese el tipo de sangre del conductor'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '7'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '10', 'data-error': 'Ingrese el Teléfono del conductor'}),
            'correo': forms.TextInput(attrs={'class': 'form-control',
                                             'pattern': '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$',
                                             }),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control datepicker', }),
            'nivel_estudio': forms.Select(choices=NIVEL_ESCOLARIDAD, attrs={'class': 'form-control', 'data-error': 'Ingrese el nivel de escolaridad del conductor'}),
            'num_licencia_conduccion': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Ingrese el N° de licencia de conducción'}),
            'doc_licencia_conduccion': forms.FileInput(),
            'categoria_licencia': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2', 'data-error': 'Ingrese la categoria de la licencia'}),
            'estado_licencia': forms.CheckboxInput(),
            'organismo_transito': forms.TextInput(attrs={'class': 'form-control', 'data-error': 'Ingrese organismo de transito de la licencia'}),
            'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control datepicker', }),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control datepicker', }),
            'restricciones': forms.TextInput(attrs={'class': 'form-control', }),
            'experiencia': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '2'}),
        }

    def validar_fecha(self):
        fechaexpedicion = self.fecha_expedicion

        if fechaexpedicion.isdigit():
            self.add_error('fecha_expedicion', 'error en campo fecha de expedicion')
        else:
            return self.cleaned_data['fecha_expedicion']
