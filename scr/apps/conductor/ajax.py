from django.http import JsonResponse

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
