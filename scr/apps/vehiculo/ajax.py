from django.http import JsonResponse
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import Vehiculo, Conductor


def vehiculo_delete(request):
    pk = request.POST.get('identificador_id')

    identificador = Vehiculo.objects.get(placa=pk)
    response = {'delete': True, 'class': 'hide'}

    if identificador.activo_inactivo:
        identificador.activo_inactivo = False
        identificador.save()
    else:
        identificador.activo_inactivo = True
        identificador.save()

    return JsonResponse(response)


def vehiculo_get(request):
    all_objects = list(Vehiculo.objects.all()) + list(Conductor.objects.all())
    data = serialize('json', all_objects)
    #  data = serialize('json', Vehiculo.objects.all())
    print(data)
    return HttpResponse(data, content_type='application/json')
