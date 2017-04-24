from custom_user.admin import EmailUserAdmin


class MyCustomEmailUserAdmin(EmailUserAdmin):
    """
    You can customize the interface of your model here.
    """
    list_display = (
        'last_name',
        'first_name',
        'email',
    )
    list_editable = ('email',)
    ordering = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name',)
    list_filter = (
        'last_name',
    )
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'password')
        }),
        (('Permissions'), {
            # 'classes': ('',),
            'fields': ('is_superuser', 'is_active', 'is_staff')
        }),
        (('Sessions'), {
            'fields': ('last_login', )
        }),
    )
