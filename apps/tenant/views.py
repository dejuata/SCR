from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django_tenants.utils import tenant_context
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tenant, Domain
from .forms import TenantForm
from ..users.forms import UserForm


def create_admin_tenant(tenant, user_id, password):
    """
    Function that creates a superuser in the tenant schema.
    Receive the data of a registered user in the public schema
    and that belongs to a registry of the tenant.
    """
    user = get_user_model().objects.get(pk=user_id)
    tenant = Tenant(schema_name=tenant)

    with tenant_context(tenant):
        get_user_model().objects.create_superuser(username=user.username, password=password, email=user.email, first_name=user.first_name, last_name=user.last_name)

def validate_user(user_id, object):
    user = get_user_model().objects.get(pk=user_id)

    return user == object
   


class TenantCreateView(CreateView):
    """
    Class that creates a tenant and generates a new schema in BD.
    """
    model = Tenant
    form_class = TenantForm
    #second_form_class = UserForm
    template_name = 'tenant/tenant_form.html'
    success_url = '/'

    #def get_context_data(self, **kwargs):
    #    context = super(TenantCreateView, self).get_context_data(**kwargs)
    #    if 'form' not in context:
    #        context['form'] = self.form_class(self.request.GET)
    #    if 'form2' not in context:
    #        context['form2'] = self.second_form_class(self.request.GET)
    #    return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        password = request.POST.get('password')
        #form2 = self.second_form_class(request.POST)

        #if not form2.is_valid():
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

            # Llamo al tenant creado
            tenant_object = Tenant(schema_name=tenant.nombre_comercial)

            # TODO:
            # Debo validar los datos del form2 con los datos del usuario en bd
            # antes de guardar el usuario en el nuevo schema y antes
            # de que se generen los schemas y mandar un mensaje de que hubo un error
            # create superuser in the new schema_name
            user_id = tenant_registrado.user_id
            tenant = tenant_registrado.nombre_comercial
            create_admin_tenant(tenant, user_id, password)

            # tenant.save()

            return redirect(url)                

        else:
            return self.render_to_response(self.get_context_data(form=form))

    # def form_valid(self, form):
    #     tenant_registrado = form.instance
    #     # user = form2.instance
    #
    #     tenant_registrado.schema_name = tenant_registrado.nombre_comercial
    #     # user_password = user.password
    #
    #     self.object = form.save()
    #     dominio_tenant = Domain(domain=self.object.nombre_comercial + '.localhost',
    #                             is_primary=True,
    #                             tenant=tenant_registrado
    #                             )
    #     dominio_tenant.save()
    #
    #     # url redirect
    #     url = 'http://' + tenant_registrado.nombre_comercial + '.localhost:8000/admin'
    #
    #     # create superuser in the new schema_name
    #     user_id = tenant_registrado.user_id
    #     tenant = tenant_registrado.nombre_comercial
    #     create_admin_tenant(tenant, user_id)
    #
    #     super(TenantCreateView, self).form_valid(form)
    #     return redirect(url)
