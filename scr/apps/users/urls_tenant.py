from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CreateUser, EditUser, HomeView
from .ajax import user_delete

urlpatterns = [
    url(r'^demo', HomeView.as_view(), name="usuario_home"),
    url(r'^signup', CreateUser.as_view(), name="usuario_new"),
    url(r'^edit/(?P<pk>\d+)/$', login_required(EditUser.as_view()), name='usuario_edit'),
    url(r'delete/$', user_delete, name='usuario_delete')
]
