from django.contrib.admin import TabularInline
from django.contrib.auth.models import Permission
from custom_user.admin import EmailUserAdmin

# from ..users.forms import UserAdminForm, UserForm


class MyCustomEmailUserAdmin(EmailUserAdmin):
    """
    User model customization
    """
    # form = UserForm
    # add_form = UserAdminForm

    list_display = (
        'last_name',
        'first_name',
        'email',
    )
    list_editable = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    ordering = (
        'last_name',
        'first_name'
    )
    search_fields = (
        'last_name',
        'first_name',
    )

    list_filter = (
        'last_name',
        'email'
    )
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'password')
        }),
        (('Permissions'), {
            'fields': ('is_superuser', 'is_active', 'is_staff', 'groups', 'user_permissions')
        }),
        (('Sessions'), {
            'fields': ('last_login', )
        }),
    )
