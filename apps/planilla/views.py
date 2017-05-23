from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import PlanillaForm
from .models import Planilla
from .sorting import SortMixin


class PlanillaList(SortMixin, ListView):
    model = Planilla
    template_name = 'planilla/planilla_list.html'
    paginate_by = 10
    default_sort_params = ('fecha', 'asc')

    def sort_queryset(self, qs, sort_by, order):
        if sort_by == 'fecha':
            qs = qs.order_by('fecha')
        if order == 'desc':
            qs = qs.reverse()
        return qs


class PlanillaCreate(SuccessMessageMixin, CreateView):
    model = Planilla
    form_class = PlanillaForm
    template_name = 'planilla/planilla_form.html'
    success_url = reverse_lazy('dashboard:planilla:planilla_list')
    success_message = "la planilla fue creada exitosamente"


class PlanillaUpdate(SuccessMessageMixin, UpdateView):
    model = Planilla
    form_class = PlanillaForm
    template_name = 'planilla/planilla_form.html'
    success_url = reverse_lazy('dashboard:planilla:planilla_list')
    success_message = "La planilla fue editada exitosamente"
