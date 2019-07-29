from django.contrib import admin
from .models import *
from erp_construction.models import *
from users.models import *



class FTTSProjectAdmin(admin.ModelAdmin):

    list_display = ['id','project_name', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FTTSProject, FTTSProjectAdmin)

class FttsCommercialTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_name','ftts_quote', 'ftts_po_requisition','ftts_wayleave_application', 'ftts_project_plan', 'ftts_initial_invoice','ftts_po_client','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsCommercialTeam, FttsCommercialTeamAdmin)


class FttsProcurementTeamAdmin(admin.ModelAdmin):
    list_display = ('id','site_name', 'project_name','ftts_material_requisition','ftts_material_receipt_order', 'ftts_pr', 'ftts_pr','ftts_po_quote_service', 'ftts_po_subcontractors', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsProcurementTeam, FttsProcurementTeamAdmin)

######################################################## FIBER CIVIL TEAM ########################################################################################################################################################################################
class SitePoleInstallationAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','project_name','start_date','end_date','site_pole_installation_image_1','site_pole_installation_image_2','site_pole_installation_image_3','site_pole_installation_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SitePoleInstallation, SitePoleInstallationAdmin)

class SiteTrenchingAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_name','start_date','end_date','site_trenching_image_1', 'site_trenching_image_2','site_trenching_image_3', 'site_trenching_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteTrenching, SiteTrenchingAdmin)


class SiteBackfillingAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','project_name','start_date','end_date','site_backfilling_image_1','site_backfilling_image_2', 'site_backfilling_image_3', 'site_backfilling_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteBackfilling, SiteBackfillingAdmin)

class SiteCableInstallationAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','project_name','start_date','end_date','site_cable_installation_image_1','site_cable_installation_image_2','site_cable_installation_image_3','site_cable_installation_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SiteCableInstallation, SiteCableInstallationAdmin)

class FttsCivilTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_name','ftts_pole_installation', 'ftts_trenching','ftts_backfiling', 'ftts_cable_installation','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsCivilTeam, FttsCivilTeamAdmin)

######################################################## END ####################################################################################################################################################################################################

######################################################## FIBER INSTALLATION TEAM ########################################################################################################################################################################################
class SiteTerminalInHseAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','project_name','start_date','end_date','site_terminal_in_hse_image_1','site_terminal_in_hse_image_2','site_terminal_in_hse_image_3','site_terminal_in_hse_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SiteTerminalInHse, SiteTerminalInHseAdmin)

class SiteInterceptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_name','start_date','end_date','site_inception_image_1', 'site_inception_image_2','site_inception_image_3', 'site_inception_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteInterception, SiteInterceptionAdmin)

class SiteIntegrationAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','project_name','start_date','end_date','site_integration_image_1','site_integration_image_2', 'site_integration_image_3', 'site_integration_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteIntegration, SiteIntegrationAdmin)

class SiteAsBuiltAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','project_name','ftts_asbuit_received','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SiteAsBuilt, SiteAsBuiltAdmin)

class FttsInstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_name','ftts_terminal_in_hse', 'ftts_inception','ftts_integration', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsInstallationTeam, FttsInstallationTeamAdmin)

######################################################## END ####################################################################################################################################################################################################
