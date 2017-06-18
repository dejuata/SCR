from django.db import models


class Thema(models.Model):
    header = models.CharField(max_length=50, blank=True, default='navbar-default')
    sidenav = models.CharField(max_length=50, blank=True, )
