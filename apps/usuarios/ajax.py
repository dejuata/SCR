from django.http import JsonResponse
from django.contrib.auth.models import User


# def usuario_delete(request):
#     pk = request.POST.get('identificador_id')
#     identificador = User.objects.get(pk=pk)
#     identificador.delete()
#     response = {'class': 'hide'}
#     return JsonResponse(response)

def usuario_delete(request):
    pk = request.POST.get('identificador_id')
    identificador = User.objects.get(pk=pk)
    response = {}

    if identificador.is_authenticated():
        identificador.is_active = False
        identificador.save()
        response = {'delete': 1, 'class': 'hide'}
    else:
        response = {'message': 'No eres tu, Ajam!'}

    return JsonResponse(response)
