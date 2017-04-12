from django.conf.urls import url, include
# from django.contrib import admin
from apps.tenant.views import TenantCreateView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^usuario/', include('apps.usuarios.urls', namespace='usuario')),
    url(r'^sign_up/$', TenantCreateView.as_view()),
]
