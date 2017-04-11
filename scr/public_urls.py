from django.conf.urls import url
from django.contrib import admin
# from tenant.views import TenantCreateView, MensajesTenantsView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^admin/', admin.site.urls),
    # url(r'^registrar-tenant/$', TenantCreateView.as_view()),
    # url(r'^mostrar-mensajes/$', MensajesTenantsView.as_view()),
]
