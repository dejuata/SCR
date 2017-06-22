from django.contrib.auth import get_user_model
from django_tenants.utils import tenant_context
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Tenant


def send_mailgun(subject, to, url):
    print('enviando correo')
    merge_data = {
        'url': url,
    }

    html_body = render_to_string("emails/welcome.html", merge_data)
    msg = EmailMultiAlternatives(subject=subject, from_email="Juan Pino <info@scr.com>", to=[to],)
    msg.attach_alternative(html_body, "text/html")
    msg.send()


def create_admin_tenant(tenant, user_id, password, url):
    """
    Function that creates a superuser in the tenant schema.
    Receive the data of a registered user in the public schema
    and that belongs to a registry of the tenant.
    """
    user = get_user_model().objects.get(pk=user_id)
    tenant = Tenant(schema_name=tenant)

    # Send email of welcome
    # send_mailgun("Bienvenido a SCR", user.email, url)

    with tenant_context(tenant):
        get_user_model().objects.create_superuser(email=user.email, password=password, first_name=user.first_name, last_name=user.last_name)


def validate_user(user_id, password):
    user = get_user_model().objects.get(pk=user_id)
    return user.check_password(password)
