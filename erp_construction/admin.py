from django.contrib import admin

from .models import User, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'location', 'created_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(Project, ProjectAdmin)
