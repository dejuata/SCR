from django.views.generic import CreateView
# from django.contrib.auth.models import User

from .models import Tenant, Domain
from .forms import TenantForm#, UserTenantForm


# class RegistroUserTenant(CreateView):
#     model = User
#     form_class = UserTenantForm
#     template_name = "tenant/registrar.html"
#     success_url = '/'


class TenantCreateView(CreateView):
    model = Tenant
    form_class = TenantForm
    template_name = 'tenant/tenant_form.html'
    success_url = '/'

    def form_valid(self, form):
        tenant_registrado = form.instance
        tenant_registrado.schema_name = tenant_registrado.razon_social
        self.object = form.save()
        dominio_tenant = Domain(domain=self.object.razon_social + '.localhost',
                                is_primary=True,
                                tenant=tenant_registrado
                                )
        dominio_tenant.save()
        return super(TenantCreateView, self).form_valid(form)
