from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect


from .forms import UploadFileForm
from .models import Ruta

import django_excel as excel


def import_data(request):
    if request.method == 'POST':
        form = UploadFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print('valid form')
            request.FILES['file'].save_to_database(
                model=Ruta,
                # initializer=None,
                mapdict={'codigo_ruta': 'codigo_ruta',
                         'nombre_ruta': 'nombre_ruta',
                         'tipo_viaje': 'tipo_viaje',
                         'tipo_ruta': 'tipo_ruta',
                         'tipo_vehiculo_requerido': 'tipo_vehiculo_requerido',
                         'origen': 'origen',
                         'destino': 'destino',
                         'hora_inicio': 'hora_inicio',
                         'hora_fin': 'hora_fin',
                         'valor_ruta': 'valor_ruta',
                         'nit_id': 'nit_id'
                        }
            )

            return HttpResponseRedirect(reverse_lazy('dashboard:ruta:ruta_list'))
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
    # return excel.make_response_from_a_table(Ruta, 'xls', file_name="rutas")
    query_sets = Ruta.objects.all()
    column_names = ['codigo_ruta',
                    'nombre_ruta',
                    'tipo_viaje',
                    'tipo_ruta',
                    'tipo_vehiculo_requerido',
                    'origen',
                    'destino',
                    'hora_inicio',
                    'hora_fin',
                    'valor_hora_adicional',
                    'valor_ruta',
                    'valor_tercero',
                    'comision_conductor',
                    'kilometros',
                    'link_ruta',
                    'nit_id',
                    'activo_inactivo']
    return excel.make_response_from_query_sets(
        query_sets,
        column_names,
        'xls',
        file_name="rutas"
    )
