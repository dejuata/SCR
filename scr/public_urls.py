from django.conf.urls import url, include
# from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

from apps.tenant.views import TenantCreateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^login/', login, {'template_name': 'usuario/login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^accounts/login/', login, {'template_name': 'usuario/login.html'}, name='login'),
    url(r'^usuario/', include('apps.usuarios.urls', namespace='usuario')),
    url(r'^registrar-empresa/$', login_required(TenantCreateView.as_view())),
]
