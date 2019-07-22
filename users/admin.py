from django.contrib import admin
from .models import *


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'customuser_phone_no','customuser_profile_pic', 'team', 'position','get_permissions')
    list_display_links = ('user', )
    search_fields = ('user', )

admin.Site.register(CustomUser, CustomUserAdmin)

class PermissionMapAdmin(admin.ModelAdmin):
    list_display = ('position','content_type','view','edit','create','approver','is_superuser', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('position', )
    search_fields = ('position', )

admin.Site.register(PermissionMap, PermissionMapAdmin)

class UserLoginActivityAdmin(admin.ModelAdmin):
    list_display = ('login_IP', 'login_datetime', 'login_username','status','user_agent_info')
    list_display_links = ('login_username', )
    search_fields = ('login_username', )

admin.Site.register(UserLoginActivity, UserLoginActivityAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'is_active')
    list_display_links = ('location_name', )
    search_fields = ('location_name', )

admin.Site.register(Location, LocationAdmin)

class CasualAdmin(admin.ModelAdmin):
    list_display = ('casual_name', 'casual_phone_no','location_name')
    list_display_links = ('casual_name', )
    search_fields = ('casual_name', )

admin.Site.register(Casual, CasualAdmin)


class EngineerAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','engineer_phone_no','department','location_name', 'country_code', 'eng_profile_pic')
    list_display_links = ('id', )
    search_fields = ('id', )

admin.Site.register(Engineer, EngineerAdmin)


class RatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker_type', 'rate', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id', )
    search_fields = ('id', )

admin.Site.register(Rates, RatesAdmin)
