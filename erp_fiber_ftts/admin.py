
from django.contrib import admin
from .models import FTTSProject



class FTTSProjectAdmin(admin.ModelAdmin):

    list_display = ['project_name', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FTTSProject, FTTSProjectAdmin)
