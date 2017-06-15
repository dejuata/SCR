from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormMixin

from .forms import ConductorForm, UploadFileForm
from .models import Conductor
from .sorting import SortMixin

import django_excel as excel


class ConductorList(FormMixin, SortMixin, ListView):
    model = Conductor
    template_name = 'conductor/conductor_list.html'
    form_class = UploadFileForm
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


def import_data(request):
    if request.method == 'POST':
        form = UploadFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print('valid form')
            request.FILES['file'].save_to_database(
                model=Conductor,
                # initializer=None,
                mapdict={'cedula': 'cedula',
                        'nombres': 'nombres',
                        'apellidos': 'apellidos',
                        'direccion': 'direccion',
                        'rh': 'rh',
                        'telefono': 'telefono',
                        'celular': 'celular',
                        'correo': 'correo',
                        'fecha_nacimiento': 'fecha_nacimiento',
                        'nivel_estudio': 'nivel_estudio',
                        'numero_licencia_conduccion': 'numero_licencia_conduccion',
                        'categoria_licencia': 'categoria_licencia',
                        'estado_licencia': 'estado_licencia',
                        'organismo_transito': 'organismo_transito',
                        'fecha_expedicion': 'fecha_expedicion',
                        'fecha_vencimiento': 'fecha_vencimiento',
                        'restricciones': 'restricciones',
                        'experiencia': 'experiencia'
                        }
            )

            return HttpResponseRedirect(reverse_lazy('dashboard:conductor:conductor_list'))
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        '404.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })


def export_data(request):
    query_sets = Conductor.objects.all()
    column_names = ["cedula",
                    "nombres",
                    'apellidos',
                    'direccion',
                    'rh',
                    'telefono',
                    'celular',
                    'correo',
                    'fecha_nacimiento',
                    'nivel_estudio',
                    'numero_licencia_conduccion',
                    'categoria_licencia',
                    'estado_licencia',
                    'organismo_transito',
                    'fecha_expedicion',
                    'fecha_vencimiento',
                    'restricciones',
                    'experiencia',
                    'activo_inactivo']
    return excel.make_response_from_query_sets(
        query_sets,
        column_names,
        'xls',
        file_name="conductores"
    )
