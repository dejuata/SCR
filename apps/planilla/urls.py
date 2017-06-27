from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import PlanillaList, PlanillaCreate, PlanillaUpdate, create_data
from .ajax import get_template
from .excel import export_data, import_data


urlpatterns = [
    url(r'^list/', login_required(PlanillaList.as_view()), name='planilla_list'),

    url(r'^new$', login_required(PlanillaCreate.as_view()), name='planilla_new'),

    url(r'^save$', login_required(create_data), name='planilla_save'),

    url(r'^edit/(?P<pk>\d+)/$', login_required(PlanillaUpdate.as_view()), name='planilla_edit'),

    url(r'^get/$', login_required(get_template), name='planilla_get'),

    url(r'^import/', import_data, name='planilla_import'),

    url(r'^export/', export_data, name='planilla_export'),

]
