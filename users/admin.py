from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'customuser_phone_no','customuser_profile_pic', 'team', 'position','last_seen','online')
    list_display_links = ('user', )
    search_fields = ('user', )
    ordering = ('user',)

admin.site.register(CustomUser, CustomUserAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action','timestamp')
    list_display_links = ('user', )
    search_fields = ('user', )
    ordering = ('user',)

admin.site.register(Log, LogAdmin)

"""MESSAGING"""

"""CHAT"""
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','message','timestamp','is_read')
    list_display_links = ('sender', )
    search_fields = ('sender', )

admin.site.register(Message, MessageAdmin)

class SentEmailAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','subject','message','timestamp','attachment','is_read')
    list_display_links = ('sender', )
    search_fields = ('sender', )

admin.site.register(SentEmail, SentEmailAdmin)

class EmailConfigAdmin(admin.ModelAdmin):
    list_display = ('email_host','sender_port','email_host_user','email_host_password','email_use_ssl','email_use_tls')
    list_display_links = ('email_host', )
    search_fields = ('email_host', )

admin.site.register(EmailConfig, EmailConfigAdmin)
"""END"""

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

class TeamMemberTypeAdmin(admin.ModelAdmin):
    list_display = ['role','posted_by']
    list_display_links = ('role', )
    search_fields = ('role', )
    list_filter = ('role',)

admin.site.register(TeamMemberType, TeamMemberTypeAdmin)

class ProjectTeamFTTHAdmin(admin.ModelAdmin):
    list_display = ['id','engineer_name','team_member_type','project_name',]
    list_display_links = ('team_member_type','engineer_name', )
    search_fields = ('team_member_type' ,)
    list_filter = ('project_name','team_member_type')
    #readonly_fields = ['team_member_type']

admin.site.register(ProjectTeamFTTH, ProjectTeamFTTHAdmin)

class ProjectTeamFTTSAdmin(admin.ModelAdmin):
    list_display = ['id','engineer_name','team_member_type','project_name','site_name']
    list_display_links = ('team_member_type','engineer_name','site_name' )
    search_fields = ('team_member_type' ,'site_name')
    list_filter = ('project_name','team_member_type')
    #readonly_fields = ['team_member_type']

admin.site.register(ProjectTeamFTTS, ProjectTeamFTTSAdmin)
