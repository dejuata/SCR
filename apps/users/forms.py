# -*- encoding:utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class UserForm(UserCreationForm):
    """
    Class for the creation of the form with the data of the user
    and that is used for the creation of the user
    """

    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model = get_user_model()

        fields = [
            'email',
        ]
        labels = {
            'email': 'Correo electrónico',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Correo electrónico',
                                             'pattern': '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$',
                                             }),
        }


class UserUpdateForm(UserCreationForm):
    """
    Class for the update of the data of the user
    """

    class Meta:
        model = get_user_model()

        fields = [
            'first_name',
            'last_name',
            'logo',
            'email',
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'logo': 'Avatar',
            'email': 'Correo electrónico',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Correo electrónico',
                                             'pattern': '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$',
                                             }),
        }


class UserAdminForm(UserCreationForm):
    """
    Class for the creation of the form with the data of the user
    and that is used for the creation and edition of the data of the user
    in the admin django
    """

    class Meta:
        model = get_user_model()

        fields = ['first_name', 'last_name', 'email']
