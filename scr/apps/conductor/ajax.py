from django.http import JsonResponse
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import Conductor


def conductor_delete(request):
    pkc = request.POST.get('identificadorC_id')
    identificador = Conductor.objects.get(cedula=pkc)
    response = {'delete': True, 'class': 'hide'}

    if identificador.activo_inactivo:
        identificador.activo_inactivo = False
        identificador.save()
    else:
        identificador.activo_inactivo = True
        identificador.save()

    return JsonResponse(response)


def conductor_get(request):
    data = serialize('json', Conductor.objects.all())
    return HttpResponse(data, content_type='application/json')
