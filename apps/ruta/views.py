from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .forms import RutaForm
from .models import Ruta


class Dashboard(TemplateView):
    template_name = 'dashboard/index.html'


class RutaList(ListView):
    model = Ruta
    template_name = 'ruta/ruta_list.html'
    paginate_by = 10


class RutaCreate(SuccessMessageMixin, CreateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'ruta/ruta_form.html'
    success_url = reverse_lazy('ruta:ruta_list')
    success_message = "La ruta ha sido creada satisfactoriamente."
    # messages.add_message(request, messages.INFO, 'Hello world.')


class RutaUpdate(SuccessMessageMixin, UpdateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'ruta/ruta_form.html'
    success_url = reverse_lazy('ruta:ruta_list')
    success_message = "La ruta ha sido creada satisfactoriamente."


class RutaDelete(DeleteView):
    model = Ruta
    template_name = 'ruta/ruta_delete.html'
    success_url = reverse_lazy('ruta:ruta_list')
