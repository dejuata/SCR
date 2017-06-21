from django.http import JsonResponse
from django.http import HttpResponse
from django.core.serializers import serialize

from .models import Planilla, Header


def planilla_delete(request):
    pkp = request.POST.get('identificadorP_id')
    identificador = Planilla.objects.get(id=pkp)
    response = {'delete': True, 'class': 'hide'}

    if identificador.id > 0:
        identificador.delete()

    return JsonResponse(response)


def get_template(request):
    header_id = request.POST.get('pk')
    header = Header.objects.get(pk=header_id)
    data = serialize('json', Planilla.objects.filter(fecha=header).order_by('pk'))
    return HttpResponse(data)
