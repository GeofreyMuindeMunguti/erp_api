from django.contrib import admin
from .models import *


# Register your models here.
class FttsSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)


admin.site.register(FttsSite, FttsSiteAdmin)

class FttsCommercialTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftts_quote', 'ftts_po_requisition','ftts_wayleave_application', 'ftts_project_plan', 'ftts_initial_invoice','ftts_po_client','created_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsCommercialTeam, FttsCommercialTeamAdmin)
