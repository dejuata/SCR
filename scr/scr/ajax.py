from django.http import JsonResponse
from django.core.serializers import serialize
from django.http import HttpResponse

from apps.users.models import MyCustomEmailUser
from apps.cliente.models import Cliente
from apps.vehiculo.models import Vehiculo
from apps.conductor.models import Conductor
from apps.ruta.models import Ruta
from apps.planilla.models import Planilla
import json


def json_get(request):
    all_objects = list(MyCustomEmailUser.objects.all()) + list(Cliente.objects.all()) + list(Vehiculo.objects.all()) + list(Conductor.objects.all()) + list(Ruta.objects.all()) + list(Planilla.objects.all())
    data = serialize('json', all_objects)
    # date = json.loads(data)
    with open('datos.json', 'w') as file:
        json.dump(data, file)
    #  data = serialize('json', Vehiculo.objects.all())
    with open('datos.json', 'r') as file:
        d = json.load(file)
        print(d)
    return HttpResponse(data, content_type='application/json')
