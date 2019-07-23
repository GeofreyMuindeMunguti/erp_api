# from django.contrib import admin
# from .models import *
#
#
# # Register your models here.
#
# class FttsCommercialTeamAdmin(admin.ModelAdmin):
#     list_display = ('id', 'site_name','ftts_quote', 'ftts_po_requisition','ftts_wayleave_application', 'ftts_project_plan', 'ftts_initial_invoice','ftts_po_client','created_by', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('site_name', )
#     search_fields = ('site_name', )
#     list_editable = ('is_active',)
#
# admin.site.register(FttsCommercialTeam, FttsCommercialTeamAdmin)
#
#
# class FttsProcurementTeamAdmin(admin.ModelAdmin):
#     list_display = ('id','site_name', 'ftts_material_requisition','ftts_material_receipt_order', 'ftts_pr','ftts_po_quote_service', 'ftts_po_subcontractors', 'created_by', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('site_name', )
#     search_fields = ('site_name', )
#     list_editable = ('is_active',)
#
# admin.site.register(FttsProcurementTeam, FttsProcurementTeamAdmin)
#
# ################################################# FIBER CIVIL TEAM ##############################################################################################################################################################################################################################################
# class SitePoleInstallationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'site_name','start_date', 'end_date','site_pole_installation_image_1', 'site_pole_installation_image_2', 'site_pole_installation_image_3','site_pole_installation_comment','created_by', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('site_name', )
#     search_fields = ('site_name', )
#     list_editable = ('is_active',)
#
# admin.site.register(SitePoleInstallation, SitePoleInstallationAdmin)
#
# class SiteTrenchingAdmin(admin.ModelAdmin):
#     list_display = ('id','site_name', 'start_date','end_date', 'site_trenching_image_1', 'site_trenching_image_2','site_trenching_image_3', 'site_trenching_comment','created_by', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('site_name', )
#     search_fields = ('site_name', )
#     list_editable = ('is_active',)
#
# admin.site.register(SiteTrenching, SiteTrenchingAdmin)
#
# class SiteBackfillingAdmin(admin.ModelAdmin):
#     list_display = ('id', 'site_name','start_date', 'end_date','site_backfilling_image_1', 'site_backfilling_image_2', 'site_backfilling_image_3','site_backfilling_comment','created_by', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('site_name', )
#     search_fields = ('site_name', )
#     list_editable = ('is_active',)
#
# admin.site.register(SiteBackfilling, SiteBackfillingAdmin)
#
# class SiteCableInstallationAdmin(admin.ModelAdmin):
#     list_display = ('id','site_name', 'start_date','end_date', 'site_cable_installation_image_1', 'site_cable_installation_image_2','site_cable_installation_image_3','site_cable_installation_comment','created_by', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('site_name', )
#     search_fields = ('site_name', )
#     list_editable = ('is_active',)
#
# admin.site.register(SiteCableInstallation, SiteCableInstallationAdmin)
#
#
# class FttsCivilTeamAdmin(admin.ModelAdmin):
#     list_display = ('id','site_name', 'ftts_pole_installation','ftts_trenching', 'ftts_backfiling', 'ftts_cable_installation','created_by', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('site_name', )
#     search_fields = ('site_name', )
#     list_editable = ('is_active',)
#
# admin.site.register(FttsCivilTeam, FttsCivilTeamAdmin)
#
# ################################################ END ##############################################################################################################################################################################################################################################################
