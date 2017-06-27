from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import Dashboard, reporte1, reporte2, reporte3


urlpatterns = [
    url(r'^$', login_required(Dashboard.as_view()), name='index'),
    url(r'^reporte1/', login_required(reporte1), name='reporte1'),
    url(r'^reporte2/', login_required(reporte2), name='reporte2'),
    url(r'^reporte3/', login_required(reporte3), name='reporte3'),
]
