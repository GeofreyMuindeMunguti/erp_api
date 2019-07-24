
from django.contrib import admin
from .models import *



class FTTHProjectAdmin(admin.ModelAdmin):

    list_display = ['id','project_name','initial_kmz', 'is_acknowledged','created_at', 'updated_at', 'is_active']
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active','is_acknowledged',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FTTHProject, FTTHProjectAdmin)

class FtthCommercialTeamAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','ftth_boq','ftth_quote','ftth_wayleave_application','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthCommercialTeam, FtthCommercialTeamAdmin)

class FtthProcurementTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftth_bom','ftth_initial_invoice','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FtthProcurementTeam, FtthProcurementTeamAdmin)

######################################################## FTTH CIVIL TEAM ########################################################################################################################################################################################
class FtthPoleInstallationAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','start_date','end_date','ftth_pole_installation_image_1','ftth_pole_installation_image_2','ftth_pole_installation_image_3','ftth_pole_installation_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthPoleInstallation, FtthPoleInstallationAdmin)

class FtthTrenchingAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','start_date','end_date','ftth_trenching_image_1', 'ftth_trenching_image_2','ftth_trenching_image_3', 'ftth_trenching_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FtthTrenching, FtthTrenchingAdmin)


class FtthBackfillingAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','start_date','end_date','ftth_backfilling_image_1','ftth_backfilling_image_2', 'ftth_backfilling_image_3', 'ftth_backfilling_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FtthBackfilling, FtthBackfillingAdmin)

class FtthCableInstallationAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','start_date','end_date','ftth_cable_installation_image_1','ftth_cable_installation_image_2','ftth_cable_installation_image_3','ftth_cable_installation_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthCableInstallation, FtthCableInstallationAdmin)

class FtthCivilTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftth_pole_installation', 'ftth_trenching','ftth_backfiling', 'ftth_cable_installation','is_approved','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FtthCivilTeam, FtthCivilTeamAdmin)

######################################################## END ####################################################################################################################################################################################################

######################################################## FTTH INSTALLATION TEAM ########################################################################################################################################################################################

class FtthSplicingEnclosureAdmin(admin.ModelAdmin):

    list_display = ('id', 'site_name','start_date','end_date','ftth_splicing_encore_image_1', 'ftth_splicing_encore_image_2','ftth_splicing_encore_image_3', 'ftth_splicing_encore_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthSplicingEnclosure, FtthSplicingEnclosureAdmin)

class FtthSplicingFATAdmin(admin.ModelAdmin):

    list_display = ('id', 'site_name','start_date','end_date','ftth_splicing_fat_image_1', 'ftth_splicing_fat_image_2','ftth_splicing_fat_image_3', 'ftth_splicing_fat_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthSplicingFAT, FtthSplicingFATAdmin)

class FtthSplicingFDTAdmin(admin.ModelAdmin):

    list_display = ('id', 'site_name','start_date','end_date','ftth_splicing_fdt_image_1', 'ftth_splicing_fdt_image_2','ftth_splicing_fdt_image_3', 'ftth_splicing_fdt_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthSplicingFDT, FtthSplicingFDTAdmin)

class FtthSplicingAdmin(admin.ModelAdmin):

    list_display = ('id', 'site_name','ftth_splicing_encore','ftth_splicing_fat','ftth_splicing_fdt','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthSplicing, FtthSplicingAdmin)

class FtthCoreProvisionAdmin(admin.ModelAdmin):

    list_display = ('id', 'site_name','start_date','end_date','ftth_core_provision_image_1', 'ftth_core_provision_image_2','ftth_core_provision_image_3', 'ftth_core_provision_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthCoreProvision, FtthCoreProvisionAdmin)

class FtthPowerLevelsAdmin(admin.ModelAdmin):

    list_display = ('id', 'site_name','start_date','end_date','ftth_power_level_image_1', 'ftth_power_level_image_2','ftth_power_level_image_3', 'ftth_power_level_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthPowerLevels, FtthPowerLevelsAdmin)

class FtthOTDRTracesAdmin(admin.ModelAdmin):

    list_display = ('id', 'site_name','start_date','end_date','ftth_otdr_traces_image_1', 'ftth_otdr_traces_image_2','ftth_otdr_traces_image_3', 'ftth_otdr_traces_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthOTDRTraces, FtthOTDRTracesAdmin)

class FtthAsBuiltAdmin(admin.ModelAdmin):

    list_display = ('id', 'site_name','ftth_asbuit_received','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthAsBuilt, FtthAsBuiltAdmin)

class FtthSignalTestingAdmin(admin.ModelAdmin):

    list_display = ('id', 'site_name','ftth_splicing_encore','ftth_splicing_fat','ftth_splicing_fdt', 'is_approved','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthSignalTesting, FtthSignalTestingAdmin)

class FtthInstallationTeamAdmin(admin.ModelAdmin):

    list_display = ('id', 'site_name','ftth_splicing','ftth_signal_testing','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthInstallationTeam, FtthInstallationTeamAdmin)
######################################################## END ################################################################################################################################################################################################
