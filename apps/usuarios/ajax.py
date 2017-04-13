from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.models import User


def usuario_delete(request):
    pk = request.POST.get('identificador_id')
    identificador = User.objects.get(pk=pk)
    identificador.delete()
    response = {'class': 'hide'}
    return JsonResponse(response)
