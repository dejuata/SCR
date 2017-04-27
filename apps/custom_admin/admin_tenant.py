from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, Permission
# from custom_user.admin import Group, Permission
from django.contrib.auth.admin import GroupAdmin

from .users import MyCustomEmailUserAdmin
from ..users.models import MyCustomEmailUser


class AdminSite(AdminSite):
    """
    Instance of a django admin for private schema
    """
    site_header = 'Admin TENANT'


admin_site = AdminSite(name='admin')
admin_site.register(MyCustomEmailUser, MyCustomEmailUserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Permission)
