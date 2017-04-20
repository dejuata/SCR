from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

from .tenant import TenantAdmin
from ..tenant.models import Tenant, Domain
from .users import UserAdmin


class MyAdminSite(AdminSite):
    """
    Instance of a django admin for public schema
    """
    site_header = 'Admin SCR'


admin_site = MyAdminSite(name='myadmin')
admin_site.register(Tenant, TenantAdmin)
admin_site.register(Domain)
admin_site.register(get_user_model(), UserAdmin)
admin_site.register(Group, GroupAdmin)
