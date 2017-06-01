from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ConductorForm
from ..cliente.forms import UploadFileForm
from .models import Conductor
from .sorting import SortMixin

import django_excel as excel


# def import_data(request):
#     if request.method == 'POST':
#         form = UploadFileForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             print('valid form')
#             request.FILES['file'].save_to_database(
#                 model=Cliente,
#                 # initializer=None,
#                 mapdict={"nit": "nit",
#                          "razon_social": "razon_social",
#                          "telefono": 'telefono',
#                          'correo': 'correo',
#                          'ciudad': 'ciudad',
#                          'direccion': 'direccion',
#                          }
#             )
#
#             return HttpResponseRedirect(reverse_lazy('dashboard:cliente:cliente_list'))
#         else:
#             return HttpResponseBadRequest()
#     else:
#         form = UploadFileForm()
#     return render(
#         request,
#         'upload_form.html',
#         {
#             'form': form,
#             'title': 'Import excel data into database example',
#             'header': 'Please upload sample-data.xls:'
#         })
#
#
# def export_data(request):
#     # return excel.make_response_from_a_table(Cliente, 'xls', file_name="clientes")
#     query_sets = Conductor.objects.all()
#     column_names = ['cedula', 'nombres',
#                     'apellidos', 'direccion',
#                     'rh', 'telefono',
#                     'celular', 'correo',
#                     'fechaNacimiento', 'nivelEstudio',
#                     'numLicenciaConduccion', 'docLicenciaConduccion',
#                     'categoriaLicencia', 'estadoLicencia',
#                     'organismoTransito'
#                     'activo_inactivo']
#     return excel.make_response_from_query_sets(
#         query_sets,
#         column_names,
#         'xls',
#         file_name="clientes"
#     )


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
