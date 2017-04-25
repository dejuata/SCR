from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import Dashboard, ClienteList, ClienteCreate, ClienteUpdate
from .ajax import cliente_delete

urlpatterns = [
    url(r'^$', login_required(Dashboard.as_view()), name='index'),
    url(r'^new$', login_required(ClienteCreate.as_view()), name='cliente_new'),
    url(r'^list/', login_required(ClienteList.as_view()), name='cliente_list'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(ClienteUpdate.as_view()), name='cliente_edit'),
    url(r'delete/$', login_required(cliente_delete), name='cliente_delete')
]
