from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CreateUser, EditUser, settings, password
from .ajax import user_delete

urlpatterns = [
    url(r'^signup', CreateUser.as_view(), name="usuario_new"),
    url(r'^edit/(?P<pk>\d+)/$', login_required(EditUser.as_view()), name='usuario_edit'),
    url(r'delete/$', login_required(user_delete), name='usuario_delete'),

    url(r'^settings/$', login_required(settings), name='usuario_settings'),
    url(r'^password/$', login_required(password), name='usuario_password'),
]
