from django.http import JsonResponse
from django.contrib.auth import get_user_model


def user_delete(request):
    pk = request.POST.get('identificador_id')
    identificador = get_user_model().objects.get(pk=pk)
    response = {}

    if identificador.is_authenticated():
        identificador.is_active = False
        identificador.save()
        response = {'delete': 1, 'class': 'hide'}
    else:
        response = {'message': 'No eres tu, Ajam!'}

    return JsonResponse(response)
