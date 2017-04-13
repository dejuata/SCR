from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CrearUsuario, PerfilUsuario, EditarUsuario  # , EliminarUsuario
from .ajax import usuario_delete

urlpatterns = [
    url(r'^signup', CrearUsuario.as_view(), name="usuario_new"),
    url(r'^profile', PerfilUsuario.as_view(), name='usuario_profile'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(EditarUsuario.as_view()), name='usuario_edit'),
    # url(r'^delete/(?P<pk>\d+)/$', login_required(EliminarUsuario.as_view()), name='usuario_delete'),
    # url(r'^delete_user', CrearUsuario.as_view(), name="delete"),
    url(r'delete/$', usuario_delete, name='usuario_delete')
]
