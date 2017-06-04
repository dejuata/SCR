from django.conf.urls import url

# from .forms import citiesForm
from .views import import_data, export_data

urlpatterns = [
    # url(r'^cities/', TemplateFormView.as_view(form_class=citiesForm), name='cities'),
    url(r'^import/', import_data, name='import'),
    url(r'^export/', export_data, name="export")
]
