from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# class CustomUserInline(admin.StackedInline):
#     model = CustomUser
#     can_delete = False


# Register your models here.
# @admin.register(User)
# class CustomUserAdmin(BaseUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'last_logout','date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)
#     inlines = (CustomUserInline, )

# admin.site.register(CustomUser, CustomUserAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'customuser_phone_no','customuser_profile_pic', 'team', 'position','get_permissions')
    list_display_links = ('user', )
    search_fields = ('user', )
    ordering = ('user',)

admin.site.register(CustomUser, CustomUserAdmin)

class PermissionMapAdmin(admin.ModelAdmin):
    list_display = ('position','content_type','view','edit','create','approver','is_superuser', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('position', )
    search_fields = ('position', )

admin.site.register(PermissionMap, PermissionMapAdmin)

class UserLoginActivityAdmin(admin.ModelAdmin):
    list_display = ('login_IP', 'login_datetime', 'login_username','status','user_agent_info')
    list_display_links = ('login_username', )
    search_fields = ('login_username', )

admin.site.register(UserLoginActivity, UserLoginActivityAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'is_active')
    list_display_links = ('location_name', )
    search_fields = ('location_name', )

admin.site.register(Location, LocationAdmin)

class CasualAdmin(admin.ModelAdmin):
    list_display = ('casual_name', 'casual_phone_no','location_name')
    list_display_links = ('casual_name', )
    search_fields = ('casual_name', )

admin.site.register(Casual, CasualAdmin)


class EngineerAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','engineer_name','engineer_phone_no','department','location_name', 'country_code', 'eng_profile_pic')
    list_display_links = ('id', )
    search_fields = ('id', )

admin.site.register(Engineer, EngineerAdmin)


class RatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker_type', 'rate', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id', )
    search_fields = ('id', )

admin.site.register(Rates, RatesAdmin)
