from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import GroupAdmin

from .tenant import TenantAdmin
from .users import MyCustomEmailUserAdmin
from ..tenant.models import Tenant, Domain
from ..users.models import MyCustomEmailUser


class MyAdminSite(AdminSite):
    """
    Instance of a django admin for public schema
    """
    site_header = 'Admin SCR'


admin_site = MyAdminSite(name='myadmin')
admin_site.register(Tenant, TenantAdmin)
admin_site.register(Domain)
admin_site.register(MyCustomEmailUser, MyCustomEmailUserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Permission)
