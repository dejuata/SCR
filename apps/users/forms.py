# -*- encoding:utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from django.utils.translation import ugettext_lazy as _
from django import forms


class UserForm(UserCreationForm):
    """
    Class for the creation of the form with the data of the user
    and that is used for the creation and edition of the data of the user
    """

    class Meta:
        model = get_user_model()

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
