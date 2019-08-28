from django.contrib import admin
from .models import *
from erp_construction.models import *
from erp_core.base import *
from users.models import *


class FttsSiteInline(admin.TabularInline):
    model  = FttsSite

class FTTSProjectAdmin(admin.ModelAdmin):

    list_display = ['id','project_name','ftts_activation','ftts_activation_comment','ftts_final_acceptance_cert','ftts_final_acceptance_cert_comment','ftts_accumulated_BOM_survey','ftts_accumulated_BOM_survey_comment',
                    'ftts_sites_count','sites_list','start_date','end_date','posted_by', 'created_at', 'updated_at', 'is_active']
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)
    readonly_fields = ['created_at', 'updated_at', 'is_active']
    inlines = [
        FttsSiteInline,
    ]

admin.site.register(FTTSProject, FTTSProjectAdmin)

class FttsSiteAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','location','created_at','posted_by',  'updated_at', 'is_active')
    list_display_links = ('site_name',)
    search_fields = ('site_name',)
    list_editable = ('is_active',)
    readonly_fields = ['created_at', 'updated_at', 'is_active']


admin.site.register(FttsSite, FttsSiteAdmin)

##########################FTTH SURVEY###########################################

class InterceptionPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'interception_point_name', 'latitude', 'longitude', 'county','posted_by',  'created_at', 'updated_at', 'is_active')
    list_display_links = ('interception_point_name', )
    search_fields = ('interception_point_name', )
    list_editable = ('is_active',)


admin.site.register(InterceptionPoint, InterceptionPointAdmin)


class fttsSurveyPhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'survey_image_1', 'survey_image_2', 'survey_image_3', 'survey_images_comment', 'ftts_survey_id', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)


admin.site.register(fttsSurveyPhotos, fttsSurveyPhotosAdmin)


class fttsSurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'start_date', 'end_date', 'ftts_interception_point', 'site_latitude', 'site_longitude', 'distance_from_ip', 'high_level_design', 'county','survey_comment', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)


admin.site.register(fttsSurvey, fttsSurveyAdmin)

##########################END OF FTTH SURVEY#####################################

class FttsCommercialTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftts_quote', 'ftts_po_requisition','ftts_po_requisition_no','ftts_po_requisition_amount','ftts_wayleave_application', 'ftts_project_plan', 'ftts_initial_invoice','ftts_po_client','ftts_po_client_no','ftts_po_client_amount','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsCommercialTeam, FttsCommercialTeamAdmin)


class FttsProcurementTeamAdmin(admin.ModelAdmin):
    list_display = ('id','site_name', 'ftts_material_requisition','ftts_po_quote_serviceno','ftts_po_quote_serviceamount', 'ftts_po_subcontractors', 'ftts_po_quote_subconamount','ftts_po_quote_subconno','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsProcurementTeam, FttsProcurementTeamAdmin)

######################################################## FIBER CIVIL TEAM ########################################################################################################################################################################################
class SiteTrenchingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','site_trenching_image_1', 'site_trenching_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(SiteTrenchingImage, SiteTrenchingImageAdmin)

class DailySiteTrenchingAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','no_of_casuals', 'casuals_list','work_day','distance_trenched', 'site_trenching_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailySiteTrenching, DailySiteTrenchingAdmin)

class SiteTrenchingAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftts_task_id', 'start_date','end_date','site_trenched_distance','site_trenching_image_1', 'site_trenching_image_2','site_trenching_image_3', 'site_trenching_comment','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteTrenching, SiteTrenchingAdmin)
"""END"""
class SiteDuctInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','site_duct_image_1', 'site_duct_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(SiteDuctInstallationImage, SiteDuctInstallationImageAdmin)

class DailySiteDuctInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','no_of_casuals', 'casuals_list','work_day','distance_duct', 'site_duct_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailySiteDuctInstallation, DailySiteDuctInstallationAdmin)

class SiteDuctInstallationAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','ftts_task_id','start_date','end_date','site_duct_distance','site_duct_installation_image_1','site_duct_installation_image_2', 'site_duct_installation_image_3', 'site_duct_installation_comment','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteDuctInstallation, SiteDuctInstallationAdmin)
"""END"""

class ManHoleInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','manhole_image_1', 'manhole_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(ManHoleInstallationImage, ManHoleInstallationImageAdmin)

class DailyManHoleInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','no_of_casuals', 'casuals_list','work_day','distance_manhole', 'manhole_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailyManHoleInstallation, DailyManHoleInstallationAdmin)

class ManHoleInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftts_task_id','start_date','end_date','site_manhole_distance','manhole_image_1','manhole_image_2','manhole_image_3','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(ManHoleInstallation, ManHoleInstallationAdmin)
"""END"""

class SiteCableInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','cable_image_1', 'cable_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(SiteCableInstallationImage, SiteCableInstallationImageAdmin)

class DailySiteCableInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','no_of_casuals', 'casuals_list','work_day','distance_cable', 'cable_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailySiteCableInstallation, DailySiteCableInstallationAdmin)

class SiteCableInstallationAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','ftts_task_id','start_date','end_date','site_cable_distance','site_cable_installation_image_1','site_cable_installation_image_2','site_cable_installation_image_3','site_cable_installation_comment', 'raise_flag','created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SiteCableInstallation, SiteCableInstallationAdmin)
"""END"""

class FttsAccessApprovalCivilAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'access_approval', 'access_approval_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsAccessApprovalCivil, FttsAccessApprovalCivilAdmin)

class FttsHealthDocumentsCivilTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_safety_comm_plan', 'project_safety_comm_plan_comment','hazard_analysis_form','hazard_analysis_form_comment','attendance_form','attendance_form_comment',
                    'health_documents_comment','access_approval','posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    list_filter = ('site_name',)
    search_fields = ('site_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(FttsHealthDocumentsCivilTeam, FttsHealthDocumentsCivilTeamAdmin)

class FttsCivilTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftts_trenching','ftts_duct_installation', 'ftts_cable_installation','ftts_manhole_installation','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsCivilTeam, FttsCivilTeamAdmin)

######################################################## END ####################################################################################################################################################################################################

######################################################## FIBER INSTALLATION TEAM ########################################################################################################################################################################################

class SiteTerminalInHseImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','terminal_image_1', 'terminal_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(SiteTerminalInHseImage, SiteTerminalInHseImageAdmin)

class DailySiteTerminalInHseAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','no_of_casuals', 'casuals_list','work_day','distance_terminal', 'terminal_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailySiteTerminalInHse, DailySiteTerminalInHseAdmin)

class SiteTerminalInHseAdmin(admin.ModelAdmin):

    list_display = ['id','site_name','ftts_task_id','start_date','end_date','site_terminal_in_hse_image_1','site_terminal_in_hse_image_2','site_terminal_in_hse_image_3','site_terminal_in_hse_comment','raise_flag','created_at', 'updated_at', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_active']

admin.site.register(SiteTerminalInHse, SiteTerminalInHseAdmin)
"""END"""

class SiteInterceptionImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','interception_image_1', 'interception_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(SiteInterceptionImage, SiteInterceptionImageAdmin)

class DailySiteInterceptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','no_of_casuals', 'casuals_list','work_day','distance_interception', 'interception_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(DailySiteInterception, DailySiteInterceptionAdmin)

class SiteInterceptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftts_task_id','site_interception_distance','manhole','start_date','end_date','site_interception_image_1', 'site_interception_image_2','site_interception_image_3', 'site_interception_comment','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(SiteInterception, SiteInterceptionAdmin)
"""END"""

class FttsAccessApprovalInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'access_approval', 'access_approval_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsAccessApprovalInstallation, FttsAccessApprovalInstallationAdmin)

class FttsHealthDocsInstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','project_safety_comm_plan', 'project_safety_comm_plan_comment','hazard_analysis_form','hazard_analysis_form_comment','attendance_form','attendance_form_comment',
                    'health_documents_comment','access_approval','posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    list_filter = ('site_name',)
    search_fields = ('site_name', )
    list_editable = ('is_active', 'is_approved')

admin.site.register(FttsHealthDocsInstallationTeam, FttsHealthDocsInstallationTeamAdmin)

class FttsIssuesAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','ftts_issue', 'ftts_issue_image', 'ftts_issue_sorted_image', 'closed', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('ftts_issue', )
    list_filter = ('site_name',)
    search_fields = ('ftts_issue', )
    list_editable = ('is_active',)

admin.site.register(FttsIssues, FttsIssuesAdmin)

class FttsInstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftts_terminal_in_hse', 'ftts_interception','ftts_integration','ftts_integration_comment','ftts_installation_team_comment','ftts_asbuit_received','ftts_asbuilt_comment','snag_document',
                    'snag_document_comment','project_issues','conditional_acceptance_cert','conditional_acceptance_cert_comment', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsInstallationTeam, FttsInstallationTeamAdmin)

class FttsTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name','ftts_survey', 'ftts_civil_team','ftts_installation_team', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)

admin.site.register(FttsTeam, FttsTeamAdmin)
######################################################### END ####################################################################################################################################################################################################


class DailyCivilWorkProductionAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','work_day','trenched_distance','backfilled_distance','duct_installed_length','cable_installed_length','pole_installed',
                    'manhole_installed','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id','site_name')
    search_fields = ('work_day','site_name', )
    list_filter =('site_name','work_day')
    list_editable = ('is_active',)

admin.site.register(DailyCivilWorkProduction, DailyCivilWorkProductionAdmin)


class CasualDailyRegisterAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','work_day','work_type','others','casuals_list_file','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id','site_name',)
    search_fields = ('work_day','site_name', )
    list_filter =('site_name','work_day')
    list_editable = ('is_active',)

admin.site.register(CasualDailyRegister, CasualDailyRegisterAdmin)

class FTTSCasualDailyRegisterAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','work_day','posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id','site_name',)
    search_fields = ('work_day','site_name', )
    list_filter =('site_name','work_day')
    list_editable = ('is_active',)

admin.site.register(FTTSCasualDailyRegister, FTTSCasualDailyRegisterAdmin)

