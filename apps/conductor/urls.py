from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ConductorList, ConductorCreate, ConductorUpdate#, import_data, export_data
from .ajax import conductor_delete

urlpatterns = [
    url(r'^new$', login_required(ConductorCreate.as_view()), name='conductor_new'),
    url(r'^list/', login_required(ConductorList.as_view()), name='conductor_list'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(ConductorUpdate.as_view()), name='conductor_edit'),
    url(r'^delete/$', login_required(conductor_delete), name='conductor_delete'),
    # url(r'^import/', import_data, name='conductor_import'),
    # url(r'^export/', export_data, name='conductor_export'),
]
