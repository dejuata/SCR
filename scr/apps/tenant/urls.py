from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import TenantCreateView, TenantUpdateView


urlpatterns = [
    url(r'^new/$', login_required(TenantCreateView.as_view()), name='tenant_new'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(TenantUpdateView.as_view()), name='tenant_edit'),
]
