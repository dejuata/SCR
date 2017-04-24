from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect

from .models import Tenant, Domain
from .forms import TenantForm
from .utils import create_admin_tenant, validate_user


class TenantCreateView(SuccessMessageMixin, CreateView):
    """
    Class that creates a tenant and generates a new schema in BD.
    """
    model = Tenant
    form_class = TenantForm
    template_name = 'tenant/tenant_form.html'
    success_url = '/'
    success_message = "el tenant was created successfully"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        user_id = request.POST.get('user')
        password = request.POST.get('password')

        if validate_user(user_id=user_id, password=password) and form.is_valid():

            tenant_registrado = form.instance
            tenant_registrado.schema_name = tenant_registrado.nombre_comercial
            # Guardo el formulario con respecto al tenant
            tenant = form.save()
            # Creo una instancia de la clase Domain para relacionarlo
            # con el tenant que se creo
            dominio_tenant = Domain(domain=tenant.nombre_comercial + '.localhost',
                                    is_primary=True,
                                    tenant=tenant_registrado
                                    )
            # Guardo el dominio
            dominio_tenant.save()
            # Genero la url de redireccion
            url = 'http://' + tenant_registrado.nombre_comercial + '.localhost:8000/admin'
            # url = 'http://localhost:8000/registrar-empresa/'

            user_id = tenant_registrado.user_id
            tenant = tenant_registrado.nombre_comercial
            create_admin_tenant(tenant, user_id, password)

            return redirect(url)

        else:
            return self.render_to_response(self.get_context_data(form=form))
