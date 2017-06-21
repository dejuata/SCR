from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib import messages

from .forms import UploadFileForm
from .models import Planilla, Header
from .sorting import SortMixin
from .json import ruta_json, conductor_json, vehiculo_json

from ..ruta.models import Ruta
from ..conductor.models import Conductor
from ..vehiculo.models import Vehiculo

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
        header = Header.objects.filter(fecha=fecha).count()

        if header > 0:
            messages.add_message(request, messages.INFO, 'Ya existe una planilla con esa fecha')
            return HttpResponseRedirect(reverse_lazy('dashboard:planilla:planilla_list'))
        else:
            templates = Header.objects.filter(template=True)
            ruta = ruta_json
            conductor = conductor_json
            vehiculo = vehiculo_json
            return render(request, 'planilla/planilla_form.html', {'fecha': fecha,
                                                                   'ruta': ruta,
                                                                   'conductor': conductor,
                                                                   'vehiculo': vehiculo,
                                                                   'templates': templates,
                                                                   'planilla_id': 0,
                                                                   'btn_value': 'Guardar Planilla',
                                                                   'btn_id': 'save_planilla'
                                                                   })


def create_data(request):
    fecha = request.POST['fecha']
    data = request.POST['table_content']
    template = True if request.POST.get('template') == 'true' else False
    data = json.loads(data)
    response = {'delete': True, 'class': 'hide'}
    print(template)

    try:
        header = Header(fecha=fecha, template=template)
        header.save()

        for row in data:
            # Convierto los objectos None a ''
            for i in range(18):
                if row[i] is None:
                    row[i] = ''

            if row[0] != '':
                ruta = Ruta.objects.get(codigo_ruta=row[0])
                conductor = row[8]
                placa = row[17]

                if row[8] != '':
                    conductor = Conductor.objects.get(cedula=row[8])

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
        planilla_id = kwargs['pk']
        fecha = Header.objects.get(pk=planilla_id)

        template = ''
        if fecha.template:
            template = 'active'

        data = serialize('json', Planilla.objects.filter(fecha=fecha).order_by('pk'))
        ruta = ruta_json
        conductor = conductor_json
        vehiculo = vehiculo_json
        return render(request, 'planilla/planilla_form.html', {'data': data,
                                                               'fecha': fecha,
                                                               'ruta': ruta,
                                                               'conductor': conductor,
                                                               'vehiculo': vehiculo,
                                                               'planilla_id': planilla_id,
                                                               'template': template,
                                                               'btn_value': 'Actualizar Planilla',
                                                               'btn_id': 'update_planilla'
                                                               })

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        fecha = request.POST['fecha']
        template = True if request.POST.get('template') == 'true' else False
        data = request.POST['table_content']
        data = json.loads(data)

        header = Header.objects.filter(fecha=fecha).delete()

        if header[0] > 0:
            try:
                header = Header(pk=pk, fecha=fecha, template=template)
                header.save()

                for row in data:
                    # Convierto los objectos None a ''
                    for i in range(18):
                        if row[i] is None:
                            row[i] = ''

                    if row[0] != '':
                        ruta = Ruta.objects.get(codigo_ruta=row[0])
                        conductor = row[8]
                        placa = row[17]

                        if row[8] != '':
                            conductor = Conductor.objects.get(cedula=row[8])

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
                return JsonResponse({'messages': 'hubo algun error'})
        else:
            return JsonResponse({'messages': 'no se pudo actualizar'})
