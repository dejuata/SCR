from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormMixin
from django.core.serializers import serialize
from django.http import HttpResponse

from .forms import PlanillaForm, UploadFileForm
from .models import Planilla
from .sorting import SortMixin

import django_excel as excel


class PlanillaList(FormMixin, ListView):
    # model = Planilla
    queryset = Planilla.objects.order_by('fecha').distinct('fecha')
    template_name = 'planilla/planilla_list.html'
    form_class = UploadFileForm
    # default_sort_params = ('fecha', 'asc')

    # def sort_queryset(self, qs, sort_by, order):
    #     if sort_by == 'fecha':
    #         qs = qs.order_by('fecha')
    #     if order == 'desc':
    #         qs = qs.reverse()
    #     return qs

    # def get(self, request, *args, **kwargs):
    #     fecha = Planilla.objects.all()
    #     return render(request, 'planilla/planilla_list.html', {'data': fecha})


class PlanillaCreate(SuccessMessageMixin, CreateView):
    model = Planilla
    form_class = PlanillaForm
    template_name = 'planilla/planilla_form.html'
    success_url = reverse_lazy('dashboard:planilla:planilla_list')
    success_message = "la planilla fue creada exitosamente"


class PlanillaUpdate(SuccessMessageMixin, UpdateView):
    model = Planilla
    form_class = PlanillaForm
    template_name = 'planilla/planilla_form.html'
    success_url = reverse_lazy('dashboard:planilla:planilla_list')
    success_message = "La planilla fue editada exitosamente"

    def get(self, request, *args, **kwargs):
        id_planilla = kwargs['pk']
        fecha = Planilla.objects.get(pk=id_planilla).fecha
        data = serialize('json', Planilla.objects.filter(fecha=fecha))
        return render(request, 'planilla/planilla_form.html', {'data': data})
        # return HttpResponse(data, content_type='application/json')

    # def get_context_data(self, **kwargs):
    #     context = super(PlanillaUpdate, self).get_context_data(**kwargs)
    #     data = serialize('json', Planilla.objects.all())
    #     context['data'] = data
    #     return context

def import_data(request):
    if request.method == 'POST':
        form = UploadFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print('valid form')
            request.FILES['file'].save_to_database(
                model=Planilla,
                # initializer=None,
                mapdict={'fecha': 'fecha',
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
    column_names = ['fecha',
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
