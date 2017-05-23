from django.views.generic import FormView
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse

from ..cliente.forms import UploadFileForm
from .models import CitiesColombia

import django_excel as excel


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        if form.is_valid():

            request.FILES['file'].save_to_database(
                model=CitiesColombia,
                # initializer=None,
                mapdict={"id_departamento": "department_id", "nombre_municipio": "name"}
            )
            # time.sleep(5)

            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()

    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })


def export_data(request):
    return excel.make_response_from_a_table(CitiesColombia, 'xls', file_name="ciudades")
    # if atype == "sheet":
    #     return excel.make_response_from_a_table(
    #         Question, 'xls', file_name="sheet")
    # elif atype == "book":
    #     return excel.make_response_from_tables(
    #         [Question, Choice], 'xls', file_name="book")
    # elif atype == "custom":
    #     question = Question.objects.get(slug='ide')
    #     query_sets = Choice.objects.filter(question=question)
    #     column_names = ['choice_text', 'id', 'votes']
    #     return excel.make_response_from_query_sets(
    #         query_sets,
    #         column_names,
    #         'xls',
    #         file_name="custom"
    #     )
    # else:
    #     return HttpResponseBadRequest(
    #         "Bad request. please put one of these " +
    #         "in your url suffix: sheet, book or custom")


class TemplateFormView(FormView):
    template_name = 'form.html'
