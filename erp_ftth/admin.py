from django.contrib import admin
from .models import *
from erp_construction.models import *
from erp_core.base import *
from users.models import *
from erp_core.models import *


class FTTHProjectAdmin(admin.ModelAdmin):

    list_display = ['id','project_name','initial_kmz','signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment','created_by','is_acknowledged','created_at', 'updated_at', 'is_active']
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active','is_acknowledged',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FTTHProject, FTTHProjectAdmin)


##########################FTTH SURVEY###########################################
class FtthInterceptionPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'interception_point_name', 'latitude', 'longitude', 'county', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('interception_point_name', )
    search_fields = ('interception_point_name', )
    list_editable = ('is_active',)


admin.site.register(FtthInterceptionPoint, FtthInterceptionPointAdmin)


class ftthSurveyPhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'survey_image_1', 'survey_image_2', 'survey_image_3', 'survey_images_comment', 'ftth_survey_id', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ftthSurveyPhotos, ftthSurveyPhotosAdmin)


class ftthSurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'start_date', 'end_date', 'ftth_interception_point', 'site_latitude', 'site_longitude', 'distance_from_ip', 'high_level_design', 'county', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ftthSurvey, ftthSurveyAdmin)

##########################END OF FTTH SURVEY####################################

class FtthCommercialTeamAdmin(admin.ModelAdmin):

    list_display = ('id','project_name','ftth_po','ftts_po_no','ftts_po_amount','ftth_boq','ftth_quote','ftth_wayleave_application','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(FtthCommercialTeam, FtthCommercialTeamAdmin)

class FtthProcurementTeamAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','ftth_bom','ftth_initial_invoice','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(FtthProcurementTeam, FtthProcurementTeamAdmin)

######################################################## FTTH CIVIL TEAM ########################################################################################################################################################################################
class FtthPoleInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','poleinstallation_image_1', 'poleinstallation_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(FtthPoleInstallationImage, FtthPoleInstallationImageAdmin)

class DailyFtthPoleInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','image_list','no_of_casuals', 'casuals_list','work_day','poleinstallation_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyFtthPoleInstallation, DailyFtthPoleInstallationAdmin)

class FtthPoleInstallationAdmin(admin.ModelAdmin):

    list_display = ['id','project_name','days_list','start_date','end_date','ftth_pole_installation_image_1','ftth_pole_installation_image_2','ftth_pole_installation_image_3','ftth_pole_installation_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthPoleInstallation, FtthPoleInstallationAdmin)
"""END"""
class FtthTrenchingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','trenching_image_1', 'trenching_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(FtthTrenchingImage, FtthTrenchingImageAdmin)

class DailyFtthTrenchingAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','image_list','no_of_casuals', 'casuals_list','work_day','trenching_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyFtthTrenching, DailyFtthTrenchingAdmin)

class FtthTrenchingAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','days_list','start_date','end_date','ftth_trenching_image_1', 'ftth_trenching_image_2','ftth_trenching_image_3', 'ftth_trenching_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(FtthTrenching, FtthTrenchingAdmin)
"""END"""
class FtthBackfillingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','backfilling_image_1', 'backfilling_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(FtthBackfillingImage, FtthBackfillingImageAdmin)

class DailyFtthBackfillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','image_list','no_of_casuals', 'casuals_list','work_day','backfilling_date','backfilling_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyFtthBackfilling, DailyFtthBackfillingAdmin)

class FtthBackfillingAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','days_list','start_date','end_date','ftth_backfilling_image_1','ftth_backfilling_image_2', 'ftth_backfilling_image_3', 'ftth_backfilling_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(FtthBackfilling, FtthBackfillingAdmin)
"""END"""
class FtthCableInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','cableinstallation_image_1', 'cableinstallation_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(FtthCableInstallationImage, FtthCableInstallationImageAdmin)

class DailyFtthCableInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','image_list','no_of_casuals', 'casuals_list','work_day','cableinstallation_date','cableinstallation_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyFtthCableInstallation, DailyFtthCableInstallationAdmin)

class FtthCableInstallationAdmin(admin.ModelAdmin):

    list_display = ['id','project_name','days_list','start_date','end_date','ftth_cable_installation_image_1','ftth_cable_installation_image_2','ftth_cable_installation_image_3','ftth_cable_installation_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthCableInstallation, FtthCableInstallationAdmin)

class FtthCivilTeamAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','ftth_pole_installation', 'ftth_trenching','ftth_backfiling', 'ftth_cable_installation','is_approved','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(FtthCivilTeam, FtthCivilTeamAdmin)

######################################################## END ####################################################################################################################################################################################################

######################################################## FTTH INSTALLATION TEAM ########################################################################################################################################################################################
class FtthSplicingEnclosureImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','splicingencore_image_1', 'splicingencore_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(FtthSplicingEnclosureImage, FtthSplicingEnclosureImageAdmin)

class DailyFtthSplicingEnclosureAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','image_list','no_of_casuals', 'casuals_list','work_day','splicingencore_date','splicingencore_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyFtthSplicingEnclosure, DailyFtthSplicingEnclosureAdmin)

class FtthSplicingEnclosureAdmin(admin.ModelAdmin):

    list_display = ('id','project_name','days_list','start_date','end_date','ftth_splicing_encore_image_1', 'ftth_splicing_encore_image_2','ftth_splicing_encore_image_3', 'ftth_splicing_encore_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthSplicingEnclosure, FtthSplicingEnclosureAdmin)
"""END"""
class FtthSplicingFATImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','splicingFAT_image_1', 'splicingFAT_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(FtthSplicingFATImage, FtthSplicingFATImageAdmin)

class DailyFtthSplicingFATAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','image_list','no_of_casuals', 'casuals_list','work_day','splicingFAT_date','splicingFAT_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyFtthSplicingFAT, DailyFtthSplicingFATAdmin)

class FtthSplicingFATAdmin(admin.ModelAdmin):

    list_display = ('id','project_name','days_list','start_date','end_date','ftth_splicing_fat_image_1', 'ftth_splicing_fat_image_2','ftth_splicing_fat_image_3', 'ftth_splicing_fat_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthSplicingFAT, FtthSplicingFATAdmin)
"""END"""
class FtthSplicingFDTImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','splicingFDT_image_1', 'splicingFDT_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(FtthSplicingFDTImage, FtthSplicingFDTImageAdmin)

class DailyFtthSplicingFDTAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','image_list','no_of_casuals', 'casuals_list','work_day','splicingFDT_date','splicingFDT_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyFtthSplicingFDT, DailyFtthSplicingFDTAdmin)

class FtthSplicingFDTAdmin(admin.ModelAdmin):

    list_display = ('id','project_name','days_list','start_date','end_date','ftth_splicing_fdt_image_1', 'ftth_splicing_fdt_image_2','ftth_splicing_fdt_image_3', 'ftth_splicing_fdt_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthSplicingFDT, FtthSplicingFDTAdmin)

class FtthSplicingAdmin(admin.ModelAdmin):

    list_display = ('id','project_name','ftth_splicing_encore','ftth_splicing_fat','ftth_splicing_fdt','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthSplicing, FtthSplicingAdmin)
"""END"""

class FtthCoreProvisionImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','coreprovision_image_1', 'coreprovision_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(FtthCoreProvisionImage, FtthCoreProvisionImageAdmin)

class DailyFtthCoreProvisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','image_list','no_of_casuals', 'casuals_list','work_day','coreprovision_date','coreprovision_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyFtthCoreProvision, DailyFtthCoreProvisionAdmin)

class FtthCoreProvisionAdmin(admin.ModelAdmin):

    list_display = ('id','project_name','days_list','start_date','end_date','ftth_core_provision_image_1', 'ftth_core_provision_image_2','ftth_core_provision_image_3', 'ftth_core_provision_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthCoreProvision, FtthCoreProvisionAdmin)
"""END"""

class FtthPowerLevelsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','powerlevels_image_1', 'powerlevels_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(FtthPowerLevelsImage, FtthPowerLevelsImageAdmin)

class DailyFtthPowerLevelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','image_list','no_of_casuals', 'casuals_list','work_day','powerlevels_date','powerlevels_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyFtthPowerLevels, DailyFtthPowerLevelsAdmin)

class FtthPowerLevelsAdmin(admin.ModelAdmin):

    list_display = ('id','project_name','days_list','start_date','end_date','ftth_power_level_image_1', 'ftth_power_level_image_2','ftth_power_level_image_3', 'ftth_power_level_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthPowerLevels, FtthPowerLevelsAdmin)
"""END"""

class FtthOTDRTracesImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','OTDRTraces_image_1', 'OTDRTraces_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(FtthOTDRTracesImage, FtthOTDRTracesImageAdmin)

class DailyFtthOTDRTracesAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','image_list','no_of_casuals', 'casuals_list','work_day','OTDRTraces_date','OTDRTraces_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyFtthOTDRTraces, DailyFtthOTDRTracesAdmin)

class FtthOTDRTracesAdmin(admin.ModelAdmin):

    list_display = ('id','project_name','days_list','start_date','end_date','ftth_otdr_traces_image_1', 'ftth_otdr_traces_image_2','ftth_otdr_traces_image_3', 'ftth_otdr_traces_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthOTDRTraces, FtthOTDRTracesAdmin)


class FtthSignalTestingAdmin(admin.ModelAdmin):

    list_display = ('id','project_name','ftth_core_provision','ftth_power_levels','ftth_otdr_traces', 'is_approved','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthSignalTesting, FtthSignalTestingAdmin)


class FtthIssuesAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','ftth_issue', 'ftth_issue_image', 'ftth_issue_sorted_image', 'closed', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('ftth_issue', )
    list_filter = ('project_name',)
    search_fields = ('ftth_issue', )
    list_editable = ('is_active',)

admin.site.register(FtthIssues, FtthIssuesAdmin)

class FtthInstallationTeamAdmin(admin.ModelAdmin):

    list_display = ('id','project_name','ftth_splicing','ftth_signal_testing','project_issues','ftth_crq_document','ftth_homepass_report','ftth_operation_acceptance','ftth_asbuit_received','ftth_asbuilt_comment',
    'ftth_network_activation','ftth_network_activation_comment','snag_document','snag_document_comment','conditional_acceptance_cert','conditional_acceptance_cert_comment','ftth_installation_team_comment','is_approved','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FtthInstallationTeam, FtthInstallationTeamAdmin)


class FtthTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','ftth_survey', 'ftth_civil_team','ftth_installation_team', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(FtthTeam, FtthTeamAdmin)
######################################################## END ################################################################################################################################################################################################
