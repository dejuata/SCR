from django.conf.urls import url
from django.contrib import admin
from apps.tenant.views import TenantCreateView#, RegistroUserTenant
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^registrar', RegistroUserTenant.as_view(), name="registrar"),
    # url(r'^admin/', admin.site.urls),
    url(r'^sign_up/$', TenantCreateView.as_view()),
    # url(r'^mostrar-mensajes/$', MensajesTenantsView.as_view()),
]
