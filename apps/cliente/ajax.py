from django.http import JsonResponse

from .models import Cliente


def cliente_delete(request):
    pk = request.POST.get('identificador_id')
    identificador = Cliente.objects.get(nit=pk)
    response = {'delete': True, 'class': 'hide'}

    if identificador.activo_inactivo:
        identificador.activo_inactivo = False
        identificador.save()
    else:
        identificador.activo_inactivo = True
        identificador.save()

    return JsonResponse(response)
