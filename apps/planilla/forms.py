# -*- encoding:utf-8 -*-
from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()
