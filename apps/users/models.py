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

    first_name = models.CharField(_('first name'), max_length=30, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


# class User(AbstractUser, PermissionsMixin):
#     """
#     Custom user model that receives as an additional parameter an avatar,
#     in addition to setting the USERNAME_FIELD variable with the email
#     """
#
#     username = models.CharField(_('username'), unique=True, max_length=30)
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30)
#     last_name = models.CharField(_('last name'), max_length=30, null=True, blank=True)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True, editable=False)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
#
#     is_active = models.BooleanField(_('active'), default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(_('superuser'), default=False)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name']
#
#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#
#     def get_full_name(self):
#         '''
#         Returns the first_name plus the last_name, with a space in between.
#         '''
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()
#
#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.first_name
#
#     def email_user(self, subject, message, from_email=None, **kwargs):
#         '''
#         Sends an email to this User.
#         '''
#         send_mail(subject, message, from_email, [self.email], **kwargs)
