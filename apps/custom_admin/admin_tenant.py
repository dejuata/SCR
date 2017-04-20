from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

from .users import UserAdmin


class AdminSite(AdminSite):
    """
    Instance of a django admin for private schema
    """
    site_header = 'Admin tenant'


admin_site = AdminSite(name='admin')
admin_site.register(get_user_model(), UserAdmin)
admin_site.register(Group, GroupAdmin)
