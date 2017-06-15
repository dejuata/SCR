from django.conf.urls import url, include
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf import settings
from django.conf.urls.static import static

from apps.custom_admin.admin_tenant import admin_site


urlpatterns = [
    url(r'^$', login, {'template_name': 'tenant/tenant_login.html'}, name='index'),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin_site.urls)),

    url(r'^logout/', logout_then_login, name='usuario_logout'),
    url(r'^accounts/login/', login, {'template_name': 'tenant/tenant_login.html'}, name='tenant_login'),

    url(r'^', include('apps.users.urls_usuario', namespace='usuario_tenant')),

    url(r'^dashboard/', include('scr.dashboard_urls', namespace='dashboard')),

    url(r'^reset/password_reset/$', password_reset,
        {'template_name': 'password_reset/password_reset_form.html',
         'html_email_template_name': 'password_reset/password_reset_email.html'},
        name='password_reset'),
    url(r'^password_reset_done/$', password_reset_done,
        {'template_name': 'password_reset/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'password_reset/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', password_reset_complete,
        {'template_name': 'password_reset/password_reset_complete.html'},
        name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
