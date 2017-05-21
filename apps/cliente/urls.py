from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ClienteList, ClienteCreate, ClienteUpdate, upload, import_data, export_data
from .ajax import cliente_delete

urlpatterns = [
    url(r'^new$', login_required(ClienteCreate.as_view()), name='cliente_new'),
    url(r'^list/', login_required(ClienteList.as_view()), name='cliente_list'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(ClienteUpdate.as_view()), name='cliente_edit'),
    url(r'delete/$', login_required(cliente_delete), name='cliente_delete'),
    url(r'^excel/', upload, name='excel'),
    url(r'^import/', import_data, name='import'),
    url(r'^export/(.*)', export_data, name="export")
    
]
