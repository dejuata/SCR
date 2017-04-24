from django.conf.urls import url, include
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static  # ARCHIVOS MEDIA JODA_BETA

from apps.custom_admin.admin_tenant import admin_site


urlpatterns = [
    url(r'^$', login, {'template_name': 'users/user_login.html'}, name='index'),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin_site.urls)),

    url(r'^logout/', logout_then_login, name='usuario_logout'),
    url(r'^accounts/login/', login, {'template_name': 'users/user_login.html'}, name='usuario_login'),

    url(r'^dashboard/', include('apps.cliente.urls', namespace='cliente')),
    url(r'^', include('apps.users.urls_usuario', namespace='usuario_tenant')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # ARCHIVOS MEDIA JODA_BETA

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
