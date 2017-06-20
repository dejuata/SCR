from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import PlanillaList, import_data, export_data, PlanillaCreate, create_data_ajax
# from .ajax import planilla_delete, planilla_get

urlpatterns = [
    url(r'^list/', login_required(PlanillaList.as_view()), name='planilla_list'),
    url(r'^new$', login_required(PlanillaCreate.as_view()), name='planilla_new'),
    url(r'^save$', login_required(create_data_ajax), name='planilla_save'),


    # url(r'^edit/(?P<pk>\d+)/$', login_required(PlanillaView.as_view()), name='planilla_edit'),

    # url(r'^get/$', login_required(planilla_get), name='planilla_get'),
    url(r'^import/', import_data, name='planilla_import'),
    url(r'^export/', export_data, name='planilla_export'),
]
