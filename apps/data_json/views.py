from django.core.serializers import serialize
from django.http import HttpResponse

import django_excel as excel

from apps.users.models import MyCustomEmailUser
from apps.cliente.models import Cliente
from apps.vehiculo.models import Vehiculo
from apps.conductor.models import Conductor
from apps.ruta.models import Ruta
from apps.planilla.models import Planilla

import csv


def get_all_data_json(request):
    all_objects = list(MyCustomEmailUser.objects.all()) + list(Cliente.objects.all()) + list(Vehiculo.objects.all()) + list(Conductor.objects.all()) + list(Ruta.objects.all()) + list(Planilla.objects.all())
    data = serialize('json', all_objects)
    response = HttpResponse(data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=all_data.json'
    return response


def get_all_data_csv(request):
    return excel.make_response_from_tables(
        [MyCustomEmailUser,
         Cliente,
         Vehiculo,
         Conductor,
         Ruta,
         Planilla], 'csv', file_name="all_data")


def get_all_data_excel(request):
    pass
