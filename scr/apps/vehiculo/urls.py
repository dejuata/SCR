from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import VehiculoList, VehiculoCreate, VehiculoUpdate, export_data, import_data
from .ajax import vehiculo_delete, vehiculo_get

urlpatterns = [
    url(r'^new$', login_required(VehiculoCreate.as_view()), name='vehiculo_new'),
    url(r'^list/', login_required(VehiculoList.as_view()), name='vehiculo_list'),
    url(r'^edit/(?P<pk>[^/]+)/$', login_required(VehiculoUpdate.as_view()), name='vehiculo_edit'),
    url(r'delete/$', login_required(vehiculo_delete), name='vehiculo_delete'),
    url(r'^get/$', login_required(vehiculo_get), name='vehiculo_get'),
    url(r'^import/', import_data, name='vehiculo_import'),
    url(r'^export/', export_data, name='vehiculo_export'),
]
