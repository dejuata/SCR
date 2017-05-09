from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import Dashboard, VehiculoList, VehiculoCreate, VehiculoUpdate
from .ajax import vehiculo_delete

urlpatterns = [
    url(r'^$', login_required(Dashboard.as_view()), name='index'),
    url(r'^vehiculonew$', login_required(VehiculoCreate.as_view()), name='vehiculo_new'),
    url(r'^vehiculolist/', login_required(VehiculoList.as_view()), name='vehiculo_list'),
    url(r'^vehiculoedit/(?P<pk>[^/]+)/$', login_required(VehiculoUpdate.as_view()), name='vehiculo_edit'),
    url(r'vehiculodelete/$', login_required(vehiculo_delete), name='vehiculo_delete')
]
