from django.contrib.auth.models import User
from django.views.generic import CreateView
from apps.usuarios.forms import RegistroForm


class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = '/'
