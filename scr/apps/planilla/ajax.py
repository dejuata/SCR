from django.http import JsonResponse
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import Planilla


def planilla_delete(request):
    pkp = request.POST.get('identificadorP_id')
    identificador = Planilla.objects.get(id=pkp)
    response = {'delete': True, 'class': 'hide'}

    if identificador.id > 0:
        identificador.delete()

    return JsonResponse(response)


def planilla_get(request):
    fecha = request.POST.get('fecha')
    data = serialize('json', Planilla.objects.filter(fecha=fecha))
    return HttpResponse(data, content_type='application/json')
