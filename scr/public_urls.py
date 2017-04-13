from django.conf.urls import url, include
# from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

from apps.tenant.views import TenantCreateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="landing/index.html")),
    url(r'^login/', login, {'template_name': 'usuario/tenant_login.html'}, name='tenant_login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^accounts/login/', login, {'template_name': 'usuario/tenant_login.html'}, name='tenant_login'),
    url(r'^', include('apps.usuarios.urls-tenant', namespace='usuario')),
    url(r'^registrar-empresa/$', login_required(TenantCreateView.as_view()), name='registrar-empresa'),
]
