from django.http import JsonResponse

from .models import Conductor


def conductor_delete(request):
    print('llegue aca')
    pk = request.POST.get('identificador_id')
    identificador = Conductor.objects.get(cedula=pk)
    response = {'delete': True, 'class': 'hide'}

    if identificador.activo_inactivo:
        identificador.activo_inactivo = False
        identificador.save()
    else:
        identificador.activo_inactivo = True
        identificador.save()

    return JsonResponse(response)
