from django.contrib.admin import ModelAdmin


class ClienteAdmin(ModelAdmin):
    list_display = (
        'nit',
        'razon_social',
        'telefono',
        'correo',
        'state',
    )
    search_fields = (
        'nit',
        'razon_social'
    )
    ordering = (
        'nit',
        'razon_social'
    )
    list_display_links = (
        'razon_social',
        'nit'
    )
    list_filter = (
        'nit',
        'razon_social',
        'activo_inactivo'
    )
    actions = ['active_user']

    def active_user(self, request, queryset):
        return queryset.update(activo_inactivo=True)
    active_user.short_description = 'Activar cliente'
