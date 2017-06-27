from django.conf.urls import url, include


urlpatterns = [
    url(r'', include('apps.reportes.urls', namespace='reporte')),
    url(r'^cliente/', include('apps.cliente.urls', namespace='cliente')),
    url(r'^conductor/', include('apps.conductor.urls', namespace='conductor')),
    url(r'^vehiculo/', include('apps.vehiculo.urls', namespace='vehiculo')),
    url(r'^ruta/', include('apps.ruta.urls', namespace='ruta')),
    url(r'^planilla/', include('apps.planilla.urls', namespace='planilla')),
    url(r'^theme/', include('apps.custom_ui.urls', namespace='theme')),
    url(r'^data/', include('apps.data.urls', namespace='data')),
]
