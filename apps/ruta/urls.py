from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import RutaList, RutaCreate, RutaUpdate
from .ajax import ruta_delete

urlpatterns = [
    url(r'^rutanew$', login_required(RutaCreate.as_view()), name='ruta_new'),
    url(r'^rutalist/', login_required(RutaList.as_view()), name='ruta_list'),
    url(r'^rutaedit/(?P<pk>\d+)/$', login_required(RutaUpdate.as_view()), name='ruta_edit'),
    url(r'^rutadelete/$', login_required(ruta_delete), name='ruta_delete')
]
