from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import save_theme, Theme

urlpatterns = [
    url(r'^theme$', login_required(save_theme), name='save_theme'),

    url(r'^theme1$', login_required(Theme.as_view(template_name="custom_ui/theme1.html")), name='theme1'),
    url(r'^theme2$', login_required(Theme.as_view(template_name="custom_ui/theme2.html")), name='theme2'),
    url(r'^theme3$', login_required(Theme.as_view(template_name="custom_ui/theme3.html")), name='theme3'),
    url(r'^theme4$', login_required(Theme.as_view(template_name="custom_ui/theme4.html")), name='theme4'),
    url(r'^theme5$', login_required(Theme.as_view(template_name="custom_ui/theme5.html")), name='theme5'),
    url(r'^theme6$', login_required(Theme.as_view(template_name="custom_ui/theme6.html")), name='theme6'),
    url(r'^theme7$', login_required(Theme.as_view(template_name="custom_ui/theme7.html")), name='theme7'),
    url(r'^theme8$', login_required(Theme.as_view(template_name="custom_ui/theme8.html")), name='theme8'),
    url(r'^theme9$', login_required(Theme.as_view(template_name="custom_ui/theme9.html")), name='theme9'),
]
