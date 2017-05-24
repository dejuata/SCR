from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response, render
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormMixin

from .forms import ClienteForm, UploadFileForm
from .models import Cliente
from .sorting import SortMixin

import django_excel as excel


def import_data(request):
    if request.method == 'POST':
        form = UploadFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print('valid form')
            request.FILES['file'].save_to_database(
                model=Cliente,
                # initializer=None,
                mapdict={"nit": "nit",
                         "razon_social": "razon_social",
                         "telefono": 'telefono',
                         'correo': 'correo',
                         'ciudad': 'ciudad',
                         'direccion': 'direccion',
                         }
            )

            return HttpResponseRedirect(reverse_lazy('dashboard:cliente:cliente_list'))
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })


def export_data(request):
    # return excel.make_response_from_a_table(Cliente, 'xls', file_name="clientes")
    query_sets = Cliente.objects.all()
    column_names = ['nit', 'razon_social', 'telefono', 'correo', 'ciudad', 'direccion', 'activo_inactivo']
    return excel.make_response_from_query_sets(
        query_sets,
        column_names,
        'xls',
        file_name="clientes"
    )


class ClienteList(FormMixin, SortMixin, ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    form_class = UploadFileForm
    # paginate_by = 10
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
