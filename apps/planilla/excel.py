from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

from .forms import UploadFileForm
from .models import Planilla

import django_excel as excel


def import_data(request):
    if request.method == 'POST':
        form = UploadFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print('valid form')
            request.FILES['file'].save_to_database(
                model=Planilla,
                # initializer=None,
                mapdict={
                # 'header': 'header',
                        'kilometros': 'kilometros',
                        'hora_adicional': 'hora_adicional',
                        'hora_inicio': 'hora_inicio',
                        'hora_fin': 'hora_fin',
                        'tiempo_operado': 'tiempo_operado',
                        'observaciones': 'observaciones',
                        'novedades': 'novedades',
                        'flota': 'flota',
                        'valor_ruta': 'valor_ruta',
                        'valor_tercero': 'valor_tercero',
                        'viaticos': 'viaticos',
                        'descuentos_conductor': 'descuentos_conductor',
                        'valor_hora_adicional': 'valor_hora_adicional',
                        'adicional_conductor': 'adicional_conductor',
                        'total_ingreso': 'total_ingreso',
                        'conductor_id': 'conductor_id',
                        'placa_id': 'placa_id',
                        'ruta_id': 'ruta_id'
                        }
            )

            return HttpResponseRedirect(reverse_lazy('dashboard:planilla:planilla_list'))
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
    query_sets = Planilla.objects.all()
    column_names = ['fecha_id',
                    'kilometros',
                    'hora_adicional',
                    'hora_inicio',
                    'hora_fin',
                    'tiempo_operado',
                    'observaciones',
                    'novedades',
                    'flota',
                    'valor_ruta',
                    'valor_tercero',
                    'viaticos',
                    'descuentos_conductor',
                    'valor_hora_adicional',
                    'adicional_conductor',
                    'total_ingreso',
                    'conductor_id',
                    'placa_id',
                    'ruta_id']
    return excel.make_response_from_query_sets(
        query_sets,
        column_names,
        'xls',
        file_name="planilla"
    )
