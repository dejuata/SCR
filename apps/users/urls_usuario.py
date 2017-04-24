from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import ProfileUserTenant


urlpatterns = [
    url(r'^profile', login_required(ProfileUserTenant.as_view()), name='usuario_profile'),
]
