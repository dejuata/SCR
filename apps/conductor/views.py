from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ConductorForm
from .models import Conductor
from .sorting import SortMixin


class ConductorList(SortMixin, ListView):
    model = Conductor
    template_name = 'conductor/conductor_list.html'    
    default_sort_params = ('nombres', 'asc')

    def sort_queryset(self, qs, sort_by, order):
        if sort_by == 'nombres':
            qs = qs.order_by('nombres')
        if order == 'desc':
            qs = qs.reverse()
        return qs


class ConductorCreate(SuccessMessageMixin, CreateView):
    model = Conductor
    form_class = ConductorForm
    template_name = 'conductor/conductor_form.html'
    success_url = reverse_lazy('dashboard:conductor:conductor_list')
    success_message = "El conductor fue creado exitosamente"


class ConductorUpdate(SuccessMessageMixin, UpdateView):
    model = Conductor
    form_class = ConductorForm
    template_name = 'conductor/conductor_form.html'
    success_url = reverse_lazy('dashboard:conductor:conductor_list')
    success_message = "El conductor fue editado exitosamente"
