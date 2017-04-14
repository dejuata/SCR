from django.views.generic import CreateView
from .models import Tenant, Domain
from .forms import TenantForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect


class TenantCreateView(CreateView):
    model = Tenant
    form_class = TenantForm
    template_name = 'tenant/tenant_form.html'
    success_url = '/'

    def form_valid(self, form):
        tenant_registrado = form.instance
        tenant_registrado.schema_name = tenant_registrado.nombre_comercial
        self.object = form.save()
        dominio_tenant = Domain(domain=self.object.nombre_comercial + '.localhost',
                                is_primary=True,
                                tenant=tenant_registrado
                                )
        dominio_tenant.save()
        url = 'http://' + tenant_registrado.nombre_comercial + '.localhost:8000/admin'
        super(TenantCreateView, self).form_valid(form)
        return redirect(url)

    # def post(self, request, *args, **kwargs):
    #     url = 'http://' + request.POST.get('nombre_comercial') + '.localhost:8000'
    #     return redirect(url)
