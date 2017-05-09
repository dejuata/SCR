from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import Dashboard, ConductorList, ConductorCreate, ConductorUpdate
from .ajax import conductor_delete

urlpatterns = [
    url(r'^$', login_required(Dashboard.as_view()), name='index'),
    url(r'^conductornew$', login_required(ConductorCreate.as_view()), name='conductor_new'),
    url(r'^conductorlist/', login_required(ConductorList.as_view()), name='conductor_list'),
    url(r'^conductoredit/(?P<pk>\d+)/$', login_required(ConductorUpdate.as_view()), name='conductor_edit'),
    url(r'^conductordelete/$', login_required(conductor_delete), name='conductor_delete')
]
