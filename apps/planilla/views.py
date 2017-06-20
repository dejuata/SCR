from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormMixin
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder


from .forms import UploadFileForm
from .models import Planilla, Header
from .sorting import SortMixin

from ..ruta.models import Ruta
from ..conductor.models import Conductor
from ..vehiculo.models import Vehiculo

import django_excel as excel
import json


class PlanillaList(SortMixin, ListView):
    model = Header
    template_name = 'planilla/planilla_list.html'
    form_class = UploadFileForm
    default_sort_params = ('fecha', 'asc')

    def sort_queryset(self, qs, sort_by, order):
        if sort_by == 'fecha':
            qs = qs.order_by('fecha')
        if order == 'desc':
            qs = qs.reverse()
        return qs


class PlanillaCreate(TemplateView):
    template_name = 'planilla/planilla_form.html'

    def post(self, request, *args, **kwargs):
        fecha = request.POST.get('fecha')

        if(Header.objects.get(fecha=fecha)):
            messages.add_message(request, messages.INFO, 'Ya existe una planilla con esa fecha')
            return HttpResponseRedirect(reverse_lazy('dashboard:planilla:planilla_list'))
        else:
            ruta = json.dumps(list(Ruta.objects.values('codigo_ruta',
                                                       'nombre_ruta',
                                                       'hora_inicio',
                                                       'hora_fin',
                                                       'valor_hora_adicional',
                                                       'kilometros',
                                                       'valor_ruta',
                                                       'valor_tercero',
                                                       )), cls=DjangoJSONEncoder)

            conductor = json.dumps(list(Conductor.objects.values('cedula',
                                                                 'apellidos',
                                                                 'nombres',
                                                                 ).order_by('apellidos')))

            vehiculo = json.dumps(list(Vehiculo.objects.values('placa')))

            return render(request, 'planilla/planilla_form.html', {'fecha': fecha,
                                                                   'ruta': ruta,
                                                                   'conductor': conductor,
                                                                   'vehiculo': vehiculo,
                                                                   'btn_value': 'Guardar Planilla',
                                                                   'btn_id': 'save_planilla'
                                                                   })


def create_data(request):
    fecha = request.POST['fecha']
    data = request.POST['table_content']
    data = json.loads(data)
    response = {'delete': True, 'class': 'hide'}
    # messages.add_message(request, messages.INFO, 'Hello world.')

    try:
        header = Header(fecha=fecha)
        header.save()

        for row in data:
            # Convierto los objectos None a ''
            for i in range(18):
                if row[i] is None:
                    row[i] = ''

            if row[0] != '':
                ruta = Ruta.objects.get(codigo_ruta=row[0])
                conductor = row[8]
                # print(conductor)
                placa = row[17]

                if row[8] != '':
                    conductor = Conductor.objects.get(cedula=row[8])

                # print(conductor)

                if row[17] != '':
                    placa = Vehiculo.objects.get(placa=row[17])

                planilla = Planilla(fecha=header,
                                    ruta=ruta,
                                    hora_inicio=row[1],
                                    hora_fin=row[2],
                                    hora_adicional=row[3],
                                    tiempo_operado=row[4],
                                    kilometros=row[5],
                                    observaciones=row[6],
                                    novedades=row[7],
                                    conductor=conductor,
                                    flota=row[10],
                                    valor_ruta=row[11],
                                    valor_tercero=row[12],
                                    valor_hora_adicional=row[13],
                                    viaticos=row[14],
                                    descuentos_conductor=row[15],
                                    adicional_conductor=row[16],
                                    placa=placa,
                                    total_ingreso=row[18])

                planilla.save()

        return redirect('dashboard:planilla:planilla_list')
    except Exception:
        return JsonResponse(response)

    return HttpResponseRedirect(reverse_lazy('dashboard:planilla:planilla_list'))

    # return JsonResponse(response)


class PlanillaUpdate(SuccessMessageMixin, UpdateView):
    model = Planilla
    # form_class = PlanillaForm
    template_name = 'planilla/planilla_form.html'
    success_url = reverse_lazy('dashboard:planilla:planilla_list')
    success_message = "La planilla fue editada exitosamente"

    def get(self, request, *args, **kwargs):
        id_planilla = kwargs['pk']
        fecha = Planilla.objects.get(pk=id_planilla).fecha
        data = serialize('json', Planilla.objects.filter(fecha=fecha))
        ruta = serialize('json', Ruta.objects.all())
        conductor = serialize('json', Conductor.objects.all())
        vehiculo = serialize('json', Vehiculo.objects.all())
        return render(request, 'planilla/planilla_form.html', {'data': data,
                                                               'fecha': fecha,
                                                               'ruta': ruta,
                                                               'conductor': conductor,
                                                               'vehiculo': vehiculo,
                                                               'btn_value': 'Actualizar Planilla',
                                                               'btn_id': 'update_planilla'
                                                               })
        # return HttpResponse(data, content_type='application/json')


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
    column_names = [
    # 'fecha',
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
