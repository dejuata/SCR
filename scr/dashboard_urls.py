from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.tenant.views import Dashboard


urlpatterns = [
    url(r'^$', login_required(Dashboard.as_view()), name='index'),
    url(r'^cliente/', include('apps.cliente.urls', namespace='cliente')),
    url(r'^conductor/', include('apps.conductor.urls', namespace='conductor')),
    url(r'^vehiculo/', include('apps.vehiculo.urls', namespace='vehiculo')),
]
