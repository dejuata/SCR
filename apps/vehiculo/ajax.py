from django.http import JsonResponse

from .models import Vehiculo


def vehiculo_delete(request):
    pk = request.POST.get('identificadorV_id')
    identificador = Vehiculo.objects.get(placa=pk)
    response = {'delete': True, 'class': 'hide'}

    if identificador.activo_inactivo:
        identificador.activo_inactivo = False
        identificador.save()
    else:
        identificador.activo_inactivo = True
        identificador.save()

    return JsonResponse(response)
