from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import RutaList, RutaCreate, RutaUpdate
from .ajax import ruta_delete
from .excel import import_data, export_data

urlpatterns = [
    url(r'^new$', login_required(RutaCreate.as_view()), name='ruta_new'),
    url(r'^list/', login_required(RutaList.as_view()), name='ruta_list'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(RutaUpdate.as_view()), name='ruta_edit'),
    url(r'^delete/$', login_required(ruta_delete), name='ruta_delete'),
    url(r'^import/', import_data, name='ruta_import'),
    url(r'^export/', export_data, name='ruta_export'),
]
