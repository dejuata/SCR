from django.conf.urls import url, include
from django.contrib import admin
# from mensajes.views import MensajeCreateView
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="tenant.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^usuario/', include('apps.usuarios.urls', namespace='usuario')),
    # url(r'^registrar-mensaje/$', MensajeCreateView.as_view()),
]
