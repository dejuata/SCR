from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.cliente.views import index, ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', ClienteCreate.as_view() , name='cliente_crear'),
    url(r'^list', ClienteList.as_view(), name='cliente_list'),
    url(r'^edit/(?P<pk>\d+)/$', ClienteUpdate.as_view(), name='cliente_edit'),
    #url(r'^delete/(?P<pk>\d+)/$', login_required(ClienteDelete.as_view()), name='cliente_delete'),
	url(r'^delete/(?P<pk>\d+)/$', ClienteDelete.as_view(), name='cliente_delete'),
]
