from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth import get_user_model


class Theme(TemplateView):
    """
    Shows user data
    """
    template_name = "custom_ui/custom_ui_theme.html"
    # form_class = UserForm


def save_theme(request):
    pk = request.POST.get('id')
    value = request.POST.get('value')
    identificador = get_user_model().objects.get(pk=pk)
    response = {}

    if identificador.is_authenticated():
        print(identificador.theme)
        identificador.theme = value
        identificador.save()
        response = {'delete': True,
                    'class': 'hide',
                    'message': 'El tema se guardo con exito'}
    else:
        response = {'message': 'Houston tenemos problemas'}

    return JsonResponse(response)
