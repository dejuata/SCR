from django.http import JsonResponse

from .models import Ruta


def ruta_delete(request):
    pk = request.POST.get('identificador_id')
    identificador = Ruta.objects.get(codRuta=pk)
    response = {'delete': True, 'class': 'hide'}

    if identificador.activo_inactivo:
        identificador.activo_inactivo = False
        identificador.save()
    else:
        identificador.activo_inactivo = True
        identificador.save()

    return JsonResponse(response)
