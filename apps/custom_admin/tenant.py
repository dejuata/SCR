from django.contrib.admin import ModelAdmin


class TenantAdmin(ModelAdmin):
    list_display = (
        'nit',
        'schema_name',
        'user_id',
    )
    search_fields = ('nit',)
