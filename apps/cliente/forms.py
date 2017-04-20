from django import forms
from apps.cliente.models import Cliente

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
            'activo_inactivo',
        ]
        labels = {
            'nit' : 'NIT',
            'razon_social' : 'Razon Social',
            'logo' : 'Logo',
            'telefono' : 'Telefono',
            'correo' : 'Correo',
            'ciudad' : 'Ciudad',
            'direccion' : 'Direccion',
            'activo_inactivo' : 'Activo/Inactivo',
        }
        widgets = {
            'nit' : forms.TextInput(attrs={'class':'form-control'}),
            'razon_social' : forms.TextInput(attrs={'class':'form-control'}),
            'logo' : forms.FileInput(attrs={'class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control'}),
            'correo' : forms.TextInput(attrs={'class':'form-control'}),
            'ciudad' : forms.TextInput(attrs={'class':'form-control'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
            'activo_inactivo' : forms.RadioSelect(choices=( (1,'True'),
                        (0,'False'),
                      ))
        }
