from django.contrib import admin
from .models import *


# Register your models here.
class ProjectIconAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'site_owner', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_owner', )
    search_fields = ('site_owner', )
    list_editable = ('is_active',)


admin.site.register(ProjectIcon, ProjectIconAdmin)

class BtsSiteAdmin(admin.ModelAdmin):
    list_display = ('id','site_name','project_name','site_number','BTS_type', 'site_owner', 'geotech_file', 'access_letter', 'approved_drawing','final_acceptance_cert', 'final_acceptance_cert_comment',
                    'location', 'created_by', 'status', 'turn_around_time', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_name', )
    search_fields = ('site_name', )
    list_editable = ('is_active',)


admin.site.register(BtsSite, BtsSiteAdmin)

class BtsProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'bts_project_name', 'icon', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('bts_project_name', )
    search_fields = ('bts_project_name', )
    list_editable = ('is_active',)


admin.site.register(BtsProject, BtsProjectAdmin)


# class AccessApprovalCivilAdmin(admin.ModelAdmin):
#     list_display = ('id', 'project_name', 'access_approval', 'access_approval_comment',
#                     'created_at', 'updated_at', 'is_active')
#     list_display_links = ('project_name', )
#     search_fields = ('project_name', )
#     list_editable = ('is_active',)


# admin.site.register(AccessApprovalCivil, AccessApprovalCivilAdmin)


# class AccessApprovalInstallationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'project_name', 'access_approval', 'access_approval_comment',
#                     'created_at', 'updated_at', 'is_active')
#     list_display_links = ('project_name', )
#     search_fields = ('project_name', )
#     list_editable = ('is_active',)


# admin.site.register(AccessApprovalInstallation, AccessApprovalInstallationAdmin)


# class ProjectCostingAdmin(admin.ModelAdmin):
#     list_display = ('id', 'project_name', 'project_costing_file', 'material_cost',
#                     'labour_cost', 'total_projected_cost', 'is_approved',
#                     'created_at', 'updated_at', 'is_active')
#     list_display_links = ('project_name', )
#     search_fields = ('project_name', )
#     list_editable = ('is_active', 'is_approved')


# admin.site.register(ProjectCosting, ProjectCostingAdmin)


class ProjectPurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'po_file', 'material_cost',
                    'labour_cost', 'total_cost_of_po', 'is_approved',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(ProjectPurchaseOrder, ProjectPurchaseOrderAdmin)


class CommercialTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'approved_quote_file', 'approved_quote_amount', 'po_data',
                    'project_costing_data', 'initial_invoice', 'initial_invoice_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(CommercialTeam, CommercialTeamAdmin)


class ProcurementTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'po_steel', 'po_electrical_materials', 'po_subcontractors', 'po_subcontractors_amount', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(ProcurementTeam, ProcurementTeamAdmin)


class HealthDocumentsCivilTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'job_hazard_form', 'job_hazard_form_comment', 'incident_notification_form', 'incident_notification_form_comment', 'toolbox_meeting_form',
                    'toolbox_meeting_form_comment', 'communication_plan_form', 'communication_plan_form_comment', 'health_documents_comment','access_approval', 'safety_picture','posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(HealthDocumentsCivilTeam, HealthDocumentsCivilTeamAdmin)

#######################################START FOUNDATION IMAGES########################################################################################################################################
class FoundationCreationTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'setting_site_clearing', 'excavation_tower_base', 'blinding', 'steel_fix_formwork','concrete_pour_curing_period', 'concrete_curing_period','foundation_and_curing_comment','engineers', 'names_of_engineers','start_date','end_date', 'raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(FoundationCreationTask, FoundationCreationTaskAdmin)




    # SubTask (1): Site-Clearing Subtask //////////////////

class SiteClearingSubtaskAdmin(admin.ModelAdmin):
    #list_display = ('id', 'project_name','task_id', 'setting_site_clearing_image_1', 'setting_site_clearing_image_2', 'setting_site_clearing_image_3', 'setting_site_clearing_comment', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'labour_cost', 'date_casual_cost', 'check_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display = ('id', 'project_name','task_id', 'setting_site_clearing_image_1', 'setting_site_clearing_image_2', 'setting_site_clearing_image_3', 'setting_site_clearing_comment', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SiteClearingSubtask, SiteClearingSubtaskAdmin)

class SiteClearingDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)


admin.site.register(SiteClearingDate, SiteClearingDateAdmin)


class SiteClearingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'setting_site_clearing_image',  'setting_site_clearing_comment', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)


admin.site.register(SiteClearingImage, SiteClearingImageAdmin)

    # SubTask (2): Tower-Base Subtask //////////////////

class TowerBaseSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','task_id', 'towerbase_image_1', 'towerbase_image_2', 'towerbase_image_3', 'tower_base_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)
    
admin.site.register(TowerBaseSubtask, TowerBaseSubtaskAdmin)

class TowerBaseDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day', 'tower_base_comment','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task',)
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(TowerBaseDate,TowerBaseDateAdmin)

class TowerBaseImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','towerbase_image','tower_base_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(TowerBaseImage, TowerBaseImageAdmin)
    # SubTask (3):Blinding Subtask //////////////////

class BlindingSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'blinding_image_1', 'blinding_image_2', 'blinding_image_3', 'blinding_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BlindingSubtask, BlindingSubtaskAdmin)


class BlindingDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)


admin.site.register(BlindingDate, BlindingDateAdmin)

class BlindingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','blinding_image', 'blinding_image_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)


admin.site.register(BlindingImage, BlindingImageAdmin)


    # SubTask (4): SteelFixFormwork Subtask //////////////////

class SteelFixFormworkSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'steel_fix_formwork_image_1', 'steel_fix_formwork_image_2', 'steel_fix_formwork_image_3', 'steel_fix_formwork_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SteelFixFormworkSubtask, SteelFixFormworkSubtaskAdmin)


class SteelFixFormworkDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)


admin.site.register(SteelFixFormworkDate, SteelFixFormworkDateAdmin)

class SteelFixFormworkImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','steel_fixformwork_image', 'steel_fixformwork_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(SteelFixFormworkImage, SteelFixFormworkImageAdmin)

    # SubTask (5): ConcretePour Subtask //////////////////


class ConcretePourSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'concrete_pour_curing_image_1', 'concrete_pour_curing_image_2', 'concrete_pour_curing_image_3', 'concrete_pour_curing_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ConcretePourSubtask, ConcretePourSubtaskAdmin)

class ConcretePourDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)


admin.site.register(ConcretePourDate, ConcretePourDateAdmin)

class ConcretePourImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image','concrete_pour_curing_image', 'concrete_pour_curing_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(ConcretePourImage, ConcretePourImageAdmin)



    # SubTask (5): ConcretePourCuring Period Subtask //////////////////

class ConcreteCuringPeriodSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'concrete_pour_curing_period_image_1', 'concrete_pour_curing_period_image_2', 'concrete_pour_curing_period_image_3', 'concrete_pour_curing_period_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ConcreteCuringPeriodSubtask, ConcreteCuringPeriodSubtaskAdmin)

class ConcreteCuringPeriodDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)


admin.site.register(ConcreteCuringPeriodDate, ConcreteCuringPeriodDateAdmin)

class ConcreteCuringPeriodImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'concrete_curing_period_image', 'concrete_curing_period_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)


admin.site.register(ConcreteCuringPeriodImage, ConcreteCuringPeriodImageAdmin)

# ######################################## END #######################################################################################################################################

# #######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################
    # SubTask (1): ConcretePourCuring Period Subtask //////////////////
class ExcavationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'excavation_image_1', 'excavation_image_2', 'excavation_image_3', 'excavation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'raise_flag','start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ExcavationSubtask, ExcavationImageAdmin)


class ExcavationDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)


admin.site.register(ExcavationDate, ExcavationDateAdmin)

class ExcavationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'excavation_image', 'excavation_image_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)


admin.site.register(ExcavationImage, ExcavationImageAdmin)


    # SubTask (2): BS241ConcretePourCuringPeriodI Subtask //////////////////
class BS241ConcretePourCuringPeriodImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'bs241_concrete_pour_curing_period_image', 'bs241_concrete_pour_curing_period_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)


admin.site.register(BS241ConcretePourCuringPeriodImage, BS241ConcretePourCuringPeriodImageAdmin)


class BS241ConcretePourCuringPeriodDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)


admin.site.register(BS241ConcretePourCuringPeriodDate, BS241ConcretePourCuringPeriodDateAdmin)

class BS241ConcretePourCuringPeriodSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'bs241_concrete_pour_curing_period_image_1', 'bs241_concrete_pour_curing_period_image_2','bs241_concrete_pour_curing_period_image_3', 'bs241_concrete_pour_curing_period_comment', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BS241ConcretePourCuringPeriodSubtask, BS241ConcretePourCuringPeriodSubtaskAdmin)

    # TASK [2]: BS241AndGeneatorSlab Subtask //////////////////

class BS241AndGeneratorSlabTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'foundation_foot_pouring', 'bs241_concrete_pour_pouring_period','bs241_and_generator_slabs_comment','engineers', 'names_of_engineers', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BS241AndGeneratorSlabTask, BS241AndGeneratorSlabTaskAdmin)

# ######################################## END #######################################################################################################################################

# ####################################### BOUNDARY WALL ###########################################################################################################################
   
    # SubTasl  [1]: FoundFootPour Subtask //////////////////
class FoundFootPourImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'foundfootpour_image', 'foundfootpour_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)


admin.site.register(FoundFootPourImage, FoundFootPourImageAdmin)


class FoundFootPourDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)


admin.site.register(FoundFootPourDate, FoundFootPourDateAdmin)

class FoundFootPourSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'foundfootpour_image_1', 'foundfootpour_image_2', 'foundfootpour_image_3', 'foundfootpour_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(FoundFootPourSubtask, FoundFootPourSubtaskAdmin)

    # SubTasl  [2]: BlockworkPanelConst Subtask //////////////////
    
class BlockworkPanelConstSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'blockwallpanelconst_image_1', 'blockwallpanelconst_image_2', 'blockwallpanelconst_image_3', 'blockwallpanelconst_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BlockworkPanelConstSubtask, BlockworkPanelConstSubtaskAdmin)


class BlockworkPanelConstDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)


admin.site.register(BlockworkPanelConstDate, BlockworkPanelConstDateAdmin)

class BlockworkPanelConstImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'blockwallpanelconst_image', 'blockwallpanelconst_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)


admin.site.register(BlockworkPanelConstImage, BlockworkPanelConstImageAdmin)

    # SubTasl  [3]: GateInstallation Subtask //////////////////

class GateInstallationSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'gateinstallation_image_1', 'gateinstallation_image_2', 'gateinstallation_image_3','gateinstallation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)
admin.site.register(GateInstallationSubtask, GateInstallationSubtaskAdmin)

class GateInstallationDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(GateInstallationDate, GateInstallationDateAdmin)

class GateInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'gateinstallation_image', 'gateinstallation_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(GateInstallationImage, GateInstallationImageAdmin)

    # SubTasl  [3]: GateInstallation Subtask //////////////////

class RazorElectricFenceSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'razorelectricfance_image_1', 'razorelectricfance_image_2', 'razorelectricfance_image_3', 'razorelectricfance_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(RazorElectricFenceSubtask, RazorElectricFenceSubtaskAdmin)


class RazorElectricFenceDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(RazorElectricFenceDate, RazorElectricFenceDateAdmin)

class RazorElectricFenceImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'razorelectricfance_image', 'razorelectricfance_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(RazorElectricFenceImage, RazorElectricFenceImageAdmin)





class BoundaryWallTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'foundation_foot_pouring', 'block_construction', 'gate_installation', 'razor_electric_fence','boundary_wall_comment','engineers', 'names_of_engineers', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BoundaryWallTask, BoundaryWallTaskAdmin)
# ####################################### END###########################################################################################################################


# #######################################  TOWER & ANTENNA_COAX ###########################################################################################################################

class TowerErectionSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'tower_erection_image_1', 'tower_erection_image_2', 'tower_erection_image_3', 'tower_erection_comment', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerErectionSubtask, TowerErectionSubtaskAdmin)

class TowerErectionDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(TowerErectionDate, TowerErectionDateAdmin)

class TowerErectionImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'tower_erection_image', 'tower_erection_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(TowerErectionImage, TowerErectionImageAdmin)

####
class TowerPaintSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'tower_painting_image_1', 'tower_painting_image_2', 'tower_painting_image_3', 'tower_painting_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerPaintSubtask, TowerPaintSubtaskAdmin)

class TowerPaintDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(TowerPaintDate, TowerPaintDateAdmin)

class TowerPaintImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'tower_painting_image', 'tower_painting_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(TowerPaintImage, TowerPaintImageAdmin)
#####

class CableWaysSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'cable_ways_image_1', 'cable_ways_image_2', 'cable_ways_image_3','cable_ways_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost', 'start_date','end_date','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(CableWaysSubtask, CableWaysSubtaskAdmin)

class CableWaysDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(CableWaysDate, CableWaysDateAdmin)

class CableWaysImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'cable_ways_image', 'cable_ways_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(CableWaysImage, CableWaysImageAdmin)

class AntennaCoaxInstallSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'antenna_coax_installation_image_1', 'antenna_coax_installation_image_2', 'antenna_coax_installation_image_3', 'antenna_coax_installation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(AntennaCoaxInstallSubtask, AntennaCoaxInstallSubtaskAdmin)

class AntennaCoaxInstallDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(AntennaCoaxInstallDate, AntennaCoaxInstallDateAdmin)

class AntennaCoaxInstallImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'antenna_coax_installation_image', 'antenna_coax_installation_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(AntennaCoaxInstallImage,AntennaCoaxInstallImageAdmin)


# TASK
class TowerAntennaCoaxTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'tower_erection', 'tower_painting', 'cable_ways', 'antenna_coax_installation','tower_antenna_coax_comment','engineers', 'names_of_engineers', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerAntennaCoaxTask, TowerAntennaCoaxTaskAdmin)

# ####################################### END###########################################################################################################################

# class BTSinstallationTaskAdmin(admin.ModelAdmin):
#     list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost',  'start_date', 'BTSinstallation_image_1', 'BTSinstallation_image_2', 'BTSinstallation_image_3', 'BTSinstallation_comment',
#                      'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
#     list_display_links = ('project_name', )
#     list_filter = ('project_name',)
#     search_fields = ('project_name', )
#     list_editable = ('is_active',)

# admin.site.register(BTSinstallationTask, BTSinstallationTaskAdmin)


# class MWInstallationTaskAdmin(admin.ModelAdmin):
#     list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost',  'start_date','MWinstallation_image_1', 'MWinstallation_image_2', 'MWinstallation_image_3', 'MWinstallation_comment',
#                      'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
#     list_display_links = ('project_name', )
#     list_filter = ('project_name',)
#     search_fields = ('project_name', )
#     list_editable = ('is_active',)


# admin.site.register(MWInstallationTask, MWInstallationTaskAdmin)


# class TelecomTasksAdmin(admin.ModelAdmin):
#     list_display = ('id', 'project_name', 'team_task_id', 'engineers', 'names_of_engineers', 'Installation_of_BTS', 'Installation_of_MW_links', 'link_commissioning', 'is_approved',
#                      'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
#     list_display_links = ('project_name', )
#     list_filter = ('project_name',)
#     search_fields = ('project_name', )
#     list_editable = ('is_active', 'is_approved')


# admin.site.register(TelecomTasks, TelecomTasksAdmin)


class UndergroundTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'underground_ducting_and_manholes_image_1', 'underground_ducting_and_manholes_image_2', 'underground_ducting_and_manholes_image_3', 'underground_ducting_and_manholes_images_comment',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(UndergroundTask, UndergroundTaskAdmin)

class UndergroundTaskDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(UndergroundTaskDate, UndergroundTaskDateAdmin)

class UndergroundTaskImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image',  'underground_ducting_and_manholes_image', 'underground_ducting_and_manholes_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(UndergroundTaskImage,UndergroundTaskImageAdmin)

#Reticulation

class ReticulationAPSinstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'electricalreticulation_APSInstallation_image_1', 'electricalreticulation_APSInstallation_image_2', 'electricalreticulation_APSInstallation_image_3', 'electricalreticulation_APSInstallation_images_comment',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(ReticulationAPSinstallation, ReticulationAPSinstallationAdmin)

class ReticulationAPSinstallationDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(ReticulationAPSinstallationDate, ReticulationAPSinstallationDateAdmin)

class ReticulationAPSinstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image',  'electricalreticulation_APSInstallation_image', 'electricalreticulation_APSInstallation_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(ReticulationAPSinstallationImage,ReticulationAPSinstallationImageAdmin)

# ELECTRICAL E
class ElectricalEarthingAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date', 'earthing_connections_and_testing_image_1', 'earthing_connections_and_testing_image_2', 'earthing_connections_and_testing_image_3', 'earthing_connections_and_testing_images_comment',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ElectricalEarthing, ElectricalEarthingAdmin)

class ElectricalEarthingDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(ElectricalEarthingDate, ElectricalEarthingDateAdmin)

class ElectricalEarthingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image',  'earthing_connections_and_testing_image', 'earthing_connections_and_testing_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(ElectricalEarthingImage,ElectricalEarthingImageAdmin)

## Generator

class GeneratorInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'Generator_and_Fuel_Tank_Installation_image_1', 'Generator_and_Fuel_Tank_Installation_image_2', 'Generator_and_Fuel_Tank_Installation_image_3', 'before_fuel_image_1',
                    'before_fuel_image_2', 'after_fuel_image_1', 'after_fuel_image_2', 'Generator_and_Fuel_Tank_Installation_comment', 'start_date','end_date','raise_flag', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(GeneratorInstallation, GeneratorInstallationAdmin)

class GeneratorInstallationDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(GeneratorInstallationDate, GeneratorInstallationDateAdmin)

class GeneratorInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'generator_image', 'generator_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(GeneratorInstallationImage,GeneratorInstallationImageAdmin)


# KPLC Subtask
class KPLCSolarSubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'kplc_solar_installation_image_1', 'kplc_solar_installation_image_2', 'kplc_solar_installation_image_3', 'kplc_solar_installation_comment',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(KPLCSolarSubtask, KPLCSolarSubtaskAdmin)

class KPLCSolarDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_task','work_day','casuals_list', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('sub_task', )
    list_filter = ('sub_task','work_day')
    search_fields = ('sub_task', )
    list_editable = ('is_active',)

admin.site.register(KPLCSolarDate, KPLCSolarDateAdmin)

class KPLCSolarImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_image', 'kplc_solar_installation_image', 'kplc_solar_installation_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('day_image', )
    list_filter = ('day_image',)
    search_fields = ('day_image', )
    list_editable = ('is_active',)

admin.site.register(KPLCSolarImage,KPLCSolarImageAdmin)


class ElectricalTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'engineers', 'names_of_engineers', 'underground_ducting_and_manholes', 'electricalreticulation_APSInstallation', 'earthing_connections_and_testing', 'generator_and_Fuel_Tank_Installation', 'kPLC_solar_installation',
                    'is_approved',  'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(ElectricalTask, ElectricalTaskAdmin)


class CivilWorksTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'health_documents_civil', 'foundation_and_curing_images',
                    'bs241_and_generator_slabs_images', 'site_walling_images_field', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(CivilWorksTeam, CivilWorksTeamAdmin)


class HealthDocumentsInstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'job_hazard_form', 'job_hazard_form_comment', 'incident_notification_form', 'incident_notification_form_comment', 'toolbox_meeting_form',
                    'toolbox_meeting_form_comment', 'communication_plan_form', 'communication_plan_form_comment', 'health_documents_comment', 'access_approval', 'safety_picture', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(HealthDocumentsInstallationTeam, HealthDocumentsInstallationTeamAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'issue', 'issue_image', 'issue_sorted_image', 'closed', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('issue', )
    list_filter = ('project_name',)
    search_fields = ('issue', )
    list_editable = ('is_active',)


admin.site.register(Issue, IssueAdmin)


# class InstallationTeamAdmin(admin.ModelAdmin):
#     list_display = ('id', 'project_name', 'health_documents_installation', 'electrical_tasks_data',
#                     'telecom_tasks_data', 'as_built', 'signoff', 'signoff_comment','rfi_document','rfi_document_comment', 'integration_parameter', 'integration_parameter_comment', 'snag_document', 'snag_document_comment',
#                     'project_issues', 'conditional_acceptance_cert', 'conditional_acceptance_cert_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('project_name', )
#     list_filter = ('project_name',)
#     search_fields = ('project_name', )
#     list_editable = ('is_active',)


# admin.site.register(InstallationTeam, InstallationTeamAdmin)


class WarrantyCertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'civilworks_installation_certificate', 'connectors_torque_certificate', 'safe_to_climb_certificate', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(WarrantyCertificate, WarrantyCertificateAdmin)


class TestCetificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'cube_test_7days', 'cube_test_28days', 'earth_test', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(TestCetificate, TestCetificateAdmin)
