from django.views.generic import FormView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseBadRequest, HttpResponse

from .forms import UploadFileForm
from .models import DepartmentColombia, CitiesColombia

import django_excel as excel


class TemplateFormView(FormView):
    template_name = 'cities/cities_form.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('ciudades:cities')

    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            print('entro aqui')
            request.FILES['file'].save_book_to_database(
                models=[DepartmentColombia, CitiesColombia],
                initializers=[None, None],
                mapdicts=[
                    ['id', 'name'],
                    ['department_id', 'name']]
            )

            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()


def export_data(request):
    return excel.make_response_from_tables(
            [DepartmentColombia, CitiesColombia], 'xls', file_name="colombia")
