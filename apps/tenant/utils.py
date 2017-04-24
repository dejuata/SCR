from django.contrib.auth import get_user_model
from django_tenants.utils import tenant_context

from .models import Tenant


def create_admin_tenant(tenant, user_id, password):
    """
    Function that creates a superuser in the tenant schema.
    Receive the data of a registered user in the public schema
    and that belongs to a registry of the tenant.
    """
    user = get_user_model().objects.get(pk=user_id)
    tenant = Tenant(schema_name=tenant)

    with tenant_context(tenant):
        get_user_model().objects.create_superuser(email=user.email, password=password, first_name=user.first_name, last_name=user.last_name)


def validate_user(user_id, password):
    user = get_user_model().objects.get(pk=user_id)
    return user.check_password(password)
