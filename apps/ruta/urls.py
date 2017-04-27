from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import Dashboard, RutaList, RutaCreate, RutaUpdate, RutaDelete

urlpatterns = [
    url(r'^$', login_required(Dashboard.as_view()), name='index'),
    url(r'^new$', login_required(RutaCreate.as_view()), name='ruta_new'),
    url(r'^list/', login_required(RutaList.as_view()), name='ruta_list'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(RutaUpdate.as_view()), name='ruta_edit'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(RutaDelete.as_view()), name='ruta_delete'),
]
