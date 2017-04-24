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
            # 'first_name',
            # 'last_name',
            # 'avatar',
            'email',
            # 'password1',
            # 'password2',
        ]
        labels = {
            # 'first_name': 'Nombre',
            # 'last_name': 'Apellido',
            # 'avatar': 'Avatar',
            'email': 'Correo electrónico',
            # 'password1': 'Contraseña',
            # 'password2': 'Confirmar contraseña',
        }
        widgets = {
            # 'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Correo electrónico',
                                             'pattern': '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$',
                                             }),
            # 'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
