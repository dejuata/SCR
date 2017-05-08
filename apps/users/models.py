from __future__ import unicode_literals

from django.db import models
# from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser

# from .managers import UserManager
from custom_user.models import AbstractEmailUser


class MyCustomEmailUser(AbstractEmailUser):
    """
    Custom user model that receives as an additional parameter an avatar,
    in addition to setting the USERNAME_FIELD variable with the email
    """

    first_name = models.CharField(_('first name'), max_length=30, null=True, blank=True, default='')
    last_name = models.CharField(_('last name'), max_length=30, null=True, blank=True, default='')
    logo = models.ImageField(upload_to='avatars/', null=True, blank=True, default='')

    # aqui limpiar el email
    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.email
