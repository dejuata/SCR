from django.conf.urls import url

from .views import  TemplateFormView, export_data


urlpatterns = [
    url(r'^cities/', TemplateFormView.as_view(), name='cities'),    
    url(r'^export/', export_data, name="cities_export")
]
