from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required

from .views import get_all_data_json, get_all_data_csv, get_all_data_excel

urlpatterns = [
    url(r'^json$', staff_member_required(get_all_data_json), name='data_json'),
    url(r'^csv$', staff_member_required(get_all_data_csv), name='data_csv'),
    url(r'^excel$', staff_member_required(get_all_data_excel), name='data_excel'),
]
