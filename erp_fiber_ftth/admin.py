
from django.contrib import admin
from .models import FTTHProject



class FTTHProjectAdmin(admin.ModelAdmin):

    list_display = ['project_name','initial_kmz', 'is_acknowledged','created_at', 'updated_at', 'is_active']
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active','is_acknowledged',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FTTHProject, FTTHProjectAdmin)