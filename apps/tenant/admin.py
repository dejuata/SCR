from django.contrib.admin import AdminSite
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User

from .models import Tenant, Domain


class MyAdminSite(AdminSite):
    site_header = 'Superuser'


class TenantAdmin(ModelAdmin):
    list_display = (
        'nit',
        'schema_name',
        'user_id',
    )
    search_fields = ('nit',)


class UserAdmin(ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'username',
        'email',
    )
    list_editable = ('email',)
    ordering = ('last_name', 'first_name')
    search_fields = ('username', 'last_name', 'first_name',)
    list_filter = (
        'username',
        'last_name',
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'password')
        }),
        (('Permissions'), {
            # 'classes': ('',),
            'fields': ('is_superuser', 'is_active', 'is_staff')
        }),
        (('Sessions'), {
            # 'classes': ('',),
            'fields': ('last_login', 'date_joined', )
        }),
    )


admin_site = MyAdminSite(name='myadmin')
admin_site.register(Tenant, TenantAdmin)
admin_site.register(Domain)
admin_site.register(User, UserAdmin)
