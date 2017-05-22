from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ClienteForm
from .models import Cliente
from .sorting import SortMixin


class ClienteList(SortMixin, ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    paginate_by = 10
    default_sort_params = ('razon_social', 'asc')

    def sort_queryset(self, qs, sort_by, order):
        if sort_by == 'razon_social':
            qs = qs.order_by('razon_social')
        if order == 'desc':
            qs = qs.reverse()
        return qs


class ClienteCreate(SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('dashboard:cliente:cliente_list')
    success_message = "El cliente fue creado exitosamente"


class ClienteUpdate(SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('dashboard:cliente:cliente_list')
    success_message = "El cliente fue editado exitosamente"
