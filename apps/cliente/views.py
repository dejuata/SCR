from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response, render

from .forms import ClienteForm, UploadFileForm
from .models import Cliente
from .sorting import SortMixin

import django_excel as excel


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'excel.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })


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
