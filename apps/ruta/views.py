from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import RutaForm
from .models import Ruta
from .sorting import SortMixin


class RutaList(SortMixin, ListView):
    model = Ruta
    template_name = 'ruta/ruta_list.html'
    default_sort_params = ('codigo_ruta', 'asc')

    def sort_queryset(self, qs, sort_by, order):
        if sort_by == 'codigo_ruta':
            qs = qs.order_by('codigo_ruta')
        if order == 'desc':
            qs = qs.reverse()
        return qs


class RutaCreate(SuccessMessageMixin, CreateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'ruta/ruta_form.html'
    success_url = reverse_lazy('dashboard:ruta:ruta_list')
    success_message = "La ruta ha sido creada satisfactoriamente."


class RutaUpdate(SuccessMessageMixin, UpdateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'ruta/ruta_form.html'
    success_url = reverse_lazy('dashboard:ruta:ruta_list')
    success_message = "La ruta ha sido creada satisfactoriamente."
