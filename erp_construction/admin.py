from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *

# Register your models here.

# admin.site.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name','employee_id', 'team','position', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id', 'employee_id')
    list_filter = ('employee_id',)
    search_fields = ('user__username', )
    list_editable = ('is_active',)


admin.site.register(Employee, EmployeeAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'employee_id', 'team','position', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id', 'user')
    list_filter = ('employee_id',)
    search_fields = ('user__username', )
    list_editable = ('is_active',)


admin.site.register(UserProfile, UserProfileAdmin)

class UserProfileeInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    inlines = (UserProfileeInline, )
