from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import PlanillaList, PlanillaCreate, PlanillaUpdate
from .ajax import planilla_delete

urlpatterns = [
    url(r'^new$', login_required(PlanillaCreate.as_view()), name='planilla_new'),
    url(r'^list/', login_required(PlanillaList.as_view()), name='planilla_list'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(PlanillaUpdate.as_view()), name='planilla_edit'),
    url(r'^delete/$', login_required(planilla_delete), name='planilla_delete'),
]
