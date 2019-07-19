from django.contrib import admin
from .models import FTTSProject ,FTTHProject



class FTTSProjectAdmin(admin.ModelAdmin):
  #  form = FTTHProjectAdminForm
    list_display = ['project_name', 'description', 'created_at', 'updated_at', 'is_active']
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(FTTSProject, FTTSProjectAdmin)


class FTTHProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'description', 'initial_kmz', 'is_acknowledged', 'created_at', 'updated_at', 'is_active']
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(FTTHProject, FTTHProjectAdmin)
