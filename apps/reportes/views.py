from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader
from ..planilla.models import Planilla

from .utils import render_to_pdf
from .json import (total_clientes,
                   total_rutas,
                   total_conductores,
                   lic_vencida_conductores,
                   total_vehiculos,
                   to_vencida_vehiculos,
                   horas_laboradas_por_conductor,
                   reporte_horas_laboradas_por_conductor,
                   reporte_adicionales_por_conductor,
                   reporte_flota_utilizada)


class Dashboard(TemplateView):
    template_name = 'dashboard/index.html'

    def get(self, request, *args, **kwargs):
        clientes = total_clientes
        rutas = total_rutas
        conductores = total_conductores
        conductores_lic_vencida = lic_vencida_conductores
        vehiculos = total_vehiculos
        vehiculos_to_vencida = to_vencida_vehiculos
        data = horas_laboradas_por_conductor

        return render(request, 'dashboard/index.html', {'clientes': clientes,
                                                        'rutas': rutas,
                                                        'data': data,
                                                        'total_conductores': conductores,
                                                        'conductores_lic_vencida': conductores_lic_vencida,
                                                        'vehiculos': vehiculos,
                                                        'vehiculos_to_vencida': vehiculos_to_vencida
                                                        })


def reporte1(request):
    pdf = render_to_pdf('reportes/reporte1.html', {'data': reporte_horas_laboradas_por_conductor,
                                                   'column3': 'Tiempo operado (horas)',
                                                   'title': 'Tiempo laborado por conductor'})
    return HttpResponse(pdf, content_type='application/pdf')


def reporte2(request):
    pdf = render_to_pdf('reportes/reporte1.html', {'data': reporte_adicionales_por_conductor,
                                                   'column3': '$ Adicional',
                                                   'title': 'Adicional por conductor'})
    return HttpResponse(pdf, content_type='application/pdf')


def reporte3(request):
    pdf = render_to_pdf('reportes/reporte1.html', {'data': reporte_flota_utilizada,
                                                   'column3': 'Flota',
                                                   'title': 'Flota Utilizada'})
    return HttpResponse(pdf, content_type='application/pdf')
    # return render(request, 'reportes/reporte1.html', {'data': reporte_adicionales_por_conductor,
    #                                                   'column3': '$ Adicional',
    #                                                   'title': 'Adicional por conductor'})
