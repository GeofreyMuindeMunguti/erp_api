from django.contrib import admin
from .models import *


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'customuser_phone_no','customuser_profile_pic', 'team', 'position')
    list_display_links = ('user', )
    search_fields = ('user', )

admin.site.register(CustomUser, CustomUserAdmin)

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
    list_display = ('casual_first_name', 'casual_last_name', 'casual_phone_no','location_name')
    list_display_links = ('casual_last_name', )
    search_fields = ('casual_last_name', )

admin.site.register(Casual, CasualAdmin)


class EngineerAdmin(admin.ModelAdmin):
    list_display = ('user', 'engineer_phone_no','department','location_name', 'eng_profile_pic')
    list_display_links = ('user', )
    search_fields = ('user', )

admin.site.register(Engineer, EngineerAdmin)


class RatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker_type', 'rate', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id', )
    search_fields = ('id', )

admin.site.register(Rates, RatesAdmin)
