# -*- encoding:utf-8 -*-
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

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

    def get_context_data(self, **kwargs):
        context = super(TenantCreateView, self).get_context_data(**kwargs)
        context['password'] = 'Contraseña invalida'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        user_id = request.POST.get('user')
        password = request.POST.get('password')

        if validate_user(user_id=user_id, password=password):
            if form.is_valid():

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
        else:
            return self.render_to_response(self.get_context_data(form=form))


class TenantUpdateView(SuccessMessageMixin, UpdateView):
    model = Tenant
    form_class = TenantForm
    template_name = 'tenant/tenant_form.html'
    success_url = reverse_lazy('login')
    success_message = "El cliente fue editado exitosamente"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(Tenant, pk=self.kwargs['pk'])

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return user.telefono
