from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView, UpdateView  # , DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import RegistroForm


class CrearUsuario(CreateView):
    model = User
    template_name = "usuario/usuario_new.html"
    form_class = RegistroForm
    success_url = '/login'


class PerfilUsuario(TemplateView):
    template_name = "usuario/usuario_profile.html"
    form_class = RegistroForm


class EditarUsuario(UpdateView):
    model = User
    form_class = RegistroForm
    template_name = "usuario/usuario_edit.html"
    success_url = '/'


# class EliminarUsuario(DeleteView):
#     model = User
#     template_name = 'usuario/usuario_delete.html'
#     success_url = '/'
