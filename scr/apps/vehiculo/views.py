from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormMixin

from .forms import VehiculoForm, UploadFileForm
from .models import Vehiculo
from .sorting import SortMixin

import django_excel as excel


class VehiculoList(FormMixin, SortMixin, ListView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_list.html'
    form_class = UploadFileForm
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


def import_data(request):
    if request.method == 'POST':
        form = UploadFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print('valid form')
            request.FILES['file'].save_to_database(
                model=Vehiculo,
                # initializer=None,
                mapdict={'placa': 'placa',
                        'numero_interno': 'numero_interno',
                        'combustible': 'combustible',

                        'numero_licencia_transito': 'numero_licencia_transito',
                        'organismo_transito': 'organismo_transito',
                        'fecha_expedicion': 'fecha_expedicion',
                        'marca': 'marca',
                        'linea': 'linea',
                        'cilindraje': 'cilindraje',
                        'modelo': 'modelo',
                        'clase_vehiculo': 'clase_vehiculo',
                        'color': 'color',
                        'tipo_servicio': 'tipo_servicio',
                        'carroceria': 'carroceria',
                        'capacidad': 'capacidad',
                        'numero_motor': 'numero_motor',
                        'numero_chasis': 'numero_chasis',
                        'propietario': 'propietario',
                        'id_propietario': 'id_propietario',

                        'numero_tarjeta_operacion': 'numero_tarjeta_operacion',
                        'fecha_inicio_tarjeta_operacion': 'fecha_inicio_tarjeta_operacion',
                        'fecha_vencimiento_tarjeta_operacion': 'fecha_vencimiento_tarjeta_operacion',
                        'empresa_afiliado': 'empresa_afiliado',
                        'id_empresa_afiliado': 'id_empresa_afiliado',

                        'numero_soat': 'numero_soat',
                        'fecha_inicio_soat': 'fecha_inicio_soat',
                        'fecha_vencimiento_soat': 'fecha_vencimiento_soat',
                        'aseguradora_soat': 'aseguradora_soat',

                        'numero_certificado_rtm': 'numero_certificado_rtm',
                        'fecha_inicio_rtm': 'fecha_inicio_rtm',
                        'fecha_vencimiento_rtm': 'fecha_vencimiento_rtm',
                        'centro_diagnostico_automotriz': 'centro_diagnostico_automotriz',

                        'numero_polizas_rce_rcc': 'numero_polizas_rce_rcc',
                        'fecha_inicio_rce_rcc': 'fecha_inicio_rce_rcc',
                        'fecha_vencimiento_rce_rcc': 'fecha_vencimiento_rce_rcc',
                        'aseguradora_rce_rcc': 'aseguradora_rce_rcc',

                        'activo_inactivo': 'activo_inactivo',
                        'conductor_default_id': 'conductor_default_id'
                        }
            )

            return HttpResponseRedirect(reverse_lazy('dashboard:vehiculo:vehiculo_list'))
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
    # return excel.make_response_from_a_table(Vehiculo, 'xls', file_name="vehiculos")
    query_sets = Vehiculo.objects.all()
    column_names = ['placa',
                    'numero_interno',
                    'combustible',
                    'numero_licencia_transito',
                    'organismo_transito',
                    'fecha_expedicion',
                    'marca',
                    'linea',
                    'cilindraje',
                    'modelo',
                    'clase_vehiculo',
                    'color',
                    'tipo_servicio',
                    'carroceria',
                    'capacidad',
                    'numero_motor',
                    'numero_chasis',
                    'propietario',
                    'id_propietario',
                    'numero_tarjeta_operacion',
                    'fecha_inicio_tarjeta_operacion',
                    'fecha_vencimiento_tarjeta_operacion',
                    'empresa_afiliado',
                    'id_empresa_afiliado',
                    'numero_soat',
                    'fecha_inicio_soat',
                    'aseguradora_soat',
                    'numero_certificado_rtm',
                    'fecha_inicio_rtm',
                    'fecha_vencimiento_rtm',
                    'centro_diagnostico_automotriz',
                    'numero_polizas_rce_rcc',
                    'fecha_inicio_rce_rcc',
                    'fecha_vencimiento_rce_rcc',
                    'aseguradora_rce_rcc',
                    'activo_inactivo',
                    'conductor_default_id'
                    ]
    return excel.make_response_from_query_sets(
        query_sets,
        column_names,
        'xls',
        file_name="vehiculos"
    )
