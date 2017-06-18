#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from custom_user.models import AbstractEmailUser
import random


class MyCustomEmailUser(AbstractEmailUser):
    """
    Custom user model that receives as an additional parameter an avatar,
    in addition to setting the USERNAME_FIELD variable with the email
    """

    username = models.CharField(max_length=100, null=True, blank=True, default='')
    first_name = models.CharField(_('first name'), max_length=30, null=True, blank=True, default='')
    last_name = models.CharField(_('last name'), max_length=30, null=True, blank=True, default='')
    logo = models.ImageField(upload_to='avatar', null=True, blank=True, default='avatar_defaults/' + str(random.randrange(5)) + '.png')
    theme = models.IntegerField(blank=True, default=1)

    def get_short_name(self):
        username = self.email.split('@')
        return username[0]
