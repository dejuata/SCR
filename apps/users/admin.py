# from django.contrib import admin
# from django.contrib.admin import ModelAdmin
# # from django.contrib.auth.models import User
# from .models import User
#
#
# class UserAdmin(ModelAdmin):
#     list_display = (
#         'last_name',
#         'first_name',
#         'username',
#         'email',
#     )
#     list_editable = ('email',)
#     ordering = ('last_name', 'first_name')
#     search_fields = ('username', 'last_name', 'first_name',)
#     list_filter = (
#         'username',
#         'last_name',
#     )
#     fieldsets = (
#         (None, {
#             'fields': ('username', 'first_name', 'last_name', 'email', 'password')
#         }),
#         (('Permissions'), {
#             # 'classes': ('',),
#             'fields': ('is_superuser', 'is_active', 'is_staff')
#         }),
#         (('Sessions'), {
#             # 'classes': ('',),
#             'fields': ('last_login', )
#         }),
#     )
#
#
# # admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
