from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

from .users import MyCustomEmailUserAdmin
from ..users.models import MyCustomEmailUser
from ..conductor.models import Conductor


class AdminSite(AdminSite):
    """
    Instance of a django admin for private schema
    """
    site_header = 'Admin tenant'


admin_site = AdminSite(name='admin')
admin_site.register(MyCustomEmailUser, MyCustomEmailUserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Conductor)
