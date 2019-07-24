from django.contrib import admin
from .models import *
from erp_construction.models import *
from users.models import *



class FTTSProjectAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','created_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FTTSProject, FTTSProjectAdmin)

class FttsCommercialTeamAdmin(admin.ModelAdmin):
    list_display = ('id','quote', 'project_name','po_requisition','wayleave_application', 'project_plan', 'initial_invoice','po_client','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FttsCommercialTeam, FttsCommercialTeamAdmin)


class FttsProcurementTeamAdmin(admin.ModelAdmin):
    list_display = ('id','project_name', 'ftts_material_requisition','material_receipt_order', 'perchase_request','po_quote_service', 'po_subcontractors', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)
    

admin.site.register(FttsProcurementTeam, FttsProcurementTeamAdmin)

######################################################## FIBER CIVIL TEAM ########################################################################################################################################################################################
class SitePoleInstallationImageAdmin(admin.ModelAdmin):

    list_display = ['id','site_pole_installation_image1','site_pole_installation_image2','site_pole_installation_image3','pole_installation_task','site_name','posted_by','is_approved' ,'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SitePoleInstallationImage, SitePoleInstallationImageAdmin)

class SitePoleInstallationAdmin(admin.ModelAdmin):

    list_display = ['id','project_name','start_date','end_date','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SitePoleInstallation, SitePoleInstallationAdmin)

class TrenchingImageAdmin(admin.ModelAdmin):

    list_display = ['id','site_trenching_image_1','site_trenching_image_2','site_trenching_image_3','trenching_task','site_name','is_approved','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(TrenchingImage, TrenchingImageAdmin)

class SiteTrenchingAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','description','start_date','end_date','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(SiteTrenching, SiteTrenchingAdmin)


class SiteBackfillingAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','start_date','end_date','site_backfilling_image_1','site_backfilling_image_2', 'site_backfilling_image_3', 'site_backfilling_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteBackfilling, SiteBackfillingAdmin)

class SiteCableInstallationAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','start_date','end_date','site_cable_installation_image_1','site_cable_installation_image_2','site_cable_installation_image_3','site_cable_installation_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SiteCableInstallation, SiteCableInstallationAdmin)

class FttsCivilTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftts_pole_installation', 'ftts_trenching','ftts_backfiling', 'ftts_cable_installation','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsCivilTeam, FttsCivilTeamAdmin)

######################################################## END ####################################################################################################################################################################################################

######################################################## FIBER INSTALLATION TEAM ########################################################################################################################################################################################
class SiteTerminalInHseAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','start_date','end_date','site_terminal_in_hse_image_1','site_terminal_in_hse_image_2','site_terminal_in_hse_image_3','site_terminal_in_hse_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SiteTerminalInHse, SiteTerminalInHseAdmin)

class SiteInterceptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','start_date','end_date','site_inception_image_1', 'site_inception_image_2','site_inception_image_3', 'site_inception_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteInterception, SiteInterceptionAdmin)

class SiteIntegrationAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','start_date','end_date','site_integration_image_1','site_integration_image_2', 'site_integration_image_3', 'site_integration_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteIntegration, SiteIntegrationAdmin)

class SiteAsBuiltAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','start_date','end_date','site_as_built_image_1','site_as_built_image_2','site_as_built_image_3','site_as_built_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SiteAsBuilt, SiteAsBuiltAdmin)

class FttsInstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftts_terminal_in_hse', 'ftts_inception','ftts_integration', 'ftts_as_built','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsInstallationTeam, FttsInstallationTeamAdmin)

######################################################## END ####################################################################################################################################################################################################
