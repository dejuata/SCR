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


class ClienteList(FormMixin, SortMixin, ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    form_class = UploadFileForm
    paginate_by = 10
    default_sort_params = ('razon_social', 'asc')

    def sort_queryset(self, qs, sort_by, order):
        if sort_by == 'razon_social':
            qs = qs.order_by('razon_social')
        if order == 'desc':
            qs = qs.reverse()
        return qs

    # def get(self, request, *args, **kwargs):
    #     self.object = None
    #     self.form = self.get_form(self.form_class)
    #     # Explicitly states what get to call:
    #     return ListView.get(self, request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     # When the form is submitted, it will enter here
    #     self.object = None
    #     self.form = self.get_form(self.form_class)
    #
    #     if self.form.is_valid():
    #         self.object = self.form.save()
    #         # Here ou may consider creating a new instance of form_class(),
    #         # so that the form will come clean.
    #
    #     # Whether the form validates or not, the view will be rendered by get()
    #     return self.get(request, *args, **kwargs)
    #
    # def get_context_data(self, *args, **kwargs):
    #     # Just include the form
    #     context = super(ClienteList, self).get_context_data(*args, **kwargs)
    #     context['form'] = self.form
    #     return context


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
