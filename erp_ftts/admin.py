from django.contrib import admin
from .models import *
from erp_construction.models import *
from erp_core.base import *
from users.models import *



class FTTSProjectAdmin(admin.ModelAdmin):

    list_display = ['id','project_name','ftts_final_acceptance_cert','ftts_final_acceptance_cert_comment','ftts_accumulated_BOM_survey','ftts_accumulated_BOM_survey_comment','start_date','end_date','created_at', 'updated_at', 'is_active']
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(FTTSProject, FTTSProjectAdmin)


##########################FTTH SURVEY###########################################


class InterceptionPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'interception_point_name', 'latitude', 'longitude', 'county', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('interception_point_name', )
    search_fields = ('interception_point_name', )
    list_editable = ('is_active',)


admin.site.register(InterceptionPoint, InterceptionPointAdmin)


class fttsSurveyPhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'survey_image_1', 'survey_image_2', 'survey_image_3', 'survey_images_comment', 'ftth_survey_id', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)


admin.site.register(fttsSurveyPhotos, fttsSurveyPhotosAdmin)


class fttsSurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'start_date', 'end_date', 'ftts_interception_point', 'site_latitude', 'site_longitude', 'distance_from_ip', 'high_level_design', 'county', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)


admin.site.register(fttsSurvey, fttsSurveyAdmin)



##########################END OF FTTH SURVEY####################################


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

class SiteTrenchingAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_name','start_date','end_date','site_trenching_image_1', 'site_trenching_image_2','site_trenching_image_3', 'site_trenching_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteTrenching, SiteTrenchingAdmin)


class SiteDuctInstallationAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','project_name','start_date','end_date','site_duct_installation_image_1','site_duct_installation_image_2', 'site_duct_installation_image_3', 'site_duct_installation_comment','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteDuctInstallation, SiteDuctInstallationAdmin)

class SiteCableInstallationAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','project_name','start_date','end_date','site_cable_installation_image_1','site_cable_installation_image_2','site_cable_installation_image_3','site_cable_installation_comment','posted_by', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SiteCableInstallation, SiteCableInstallationAdmin)

class ManHoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'manhole_no','latitude','longitude','location','created_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('manhole_no', )
    search_fields = ('manhole_no', )
    list_editable = ('is_active',)

admin.site.register(ManHole, ManHoleAdmin)

class ManHoleInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_name', 'start_date','end_date','manhole_image_1','manhole_image_2','manhole_image_3','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(ManHoleInstallation, ManHoleInstallationAdmin)

class FttsCivilTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_name','ftts_trenching','ftts_duct_installation', 'ftts_cable_installation','ftts_manhole_installation','posted_by', 'created_at', 'updated_at', 'is_active')
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
    list_display = ('id', 'site_name','project_name','manhole','start_date','end_date','site_inception_image_1', 'site_inception_image_2','site_inception_image_3', 'site_inception_comment','posted_by', 'created_at', 'updated_at', 'is_active')
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

class FttsIssuesAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'ftts_issue', 'ftts_issue_image', 'ftts_issue_sorted_image', 'closed', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('ftts_issue', )
    list_filter = ('project_name',)
    search_fields = ('ftts_issue', )
    list_editable = ('is_active',)


admin.site.register(FttsIssues, FttsIssuesAdmin)

class FttsInstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_name','ftts_terminal_in_hse', 'ftts_inception','ftts_integration','ftts_asbuit_received','snag_document','snag_document_comment','project_issues','conditional_acceptance_cert','conditional_acceptance_cert_comment', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsInstallationTeam, FttsInstallationTeamAdmin)

class FttsTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_name','ftts_survey', 'ftts_civil_team','ftts_installation_team', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsTeam, FttsTeamAdmin)
######################################################### END ####################################################################################################################################################################################################


class DailyCivilWorkProductionAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','site_name','work_day','trenched_distance','backfilled_distance','duct_installed_length','cable_installed_length','pole_installed','manhole_installed','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id','site_name')
    search_fields = ('work_day','site_name', )
    list_filter =('project_name','site_name','work_day')
    list_editable = ('is_active',)

admin.site.register(DailyCivilWorkProduction, DailyCivilWorkProductionAdmin)


class CasualDailyRegisterAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','site_name','work_day','work_type','others','casuals_list_file','created_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id','site_name',)
    search_fields = ('work_day','site_name', )
    list_filter =('project_name','site_name','work_day')
    list_editable = ('is_active',)

admin.site.register(CasualDailyRegister, CasualDailyRegisterAdmin)

class FTTSCasualDailyRegisterAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','site_name','work_day','created_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id','site_name',)
    search_fields = ('work_day','site_name', )
    list_filter =('project_name','site_name','work_day')
    list_editable = ('is_active',)

admin.site.register(FTTSCasualDailyRegister, FTTSCasualDailyRegisterAdmin)
