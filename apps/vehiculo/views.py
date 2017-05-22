from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import VehiculoForm
from .models import Vehiculo
from .sorting import SortMixin


class VehiculoList(SortMixin, ListView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_list.html'
    paginate_by = 10
    default_sort_params = ('placa', 'asc')

    def sort_queryset(self, qs, sort_by, order):
        if sort_by == 'placa':
            qs = qs.order_by('placa')
        if order == 'desc':
            qs = qs.reverse()
        return qs


class VehiculoCreate(SuccessMessageMixin, CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('dashboard:vehiculo:vehiculo_list')
    success_message = "El vehiculo fue creado exitosamente"


class VehiculoUpdate(SuccessMessageMixin, UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('dashboard:vehiculo:vehiculo_list')
    success_message = "El vehiculo fue editado exitosamente"
