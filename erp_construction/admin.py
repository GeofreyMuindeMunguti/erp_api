from django.contrib import admin
from .models import *


# Register your models here.
class ProjectIconsAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'site_owner', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_owner', )
    search_fields = ('site_owner', )
    list_editable = ('is_active',)


admin.site.register(ProjectIcons, ProjectIconsAdmin)

class BtsProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'bts_project_name', 'icon', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('bts_project_name', )
    search_fields = ('bts_project_name', )
    list_editable = ('is_active',)

admin.site.register(BtsProject, BtsProjectAdmin)

class BtsSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'icon', 'site_number', 'BTS_type', 'site_owner', 'geotech_file','geotech_file_comment', 'access_letter', 'access_letter_comment','approved_drawing','final_acceptance_cert', 'final_acceptance_cert_comment',
                    'location', 'created_by', 'status', 'turn_around_time','rof_8','rof_8_comment','sign_off','sign_off_comment','rfi','rfi_comment','integration_parameter','integration_parameter_comment','ip_plan','ip_plan_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register(BtsSite, BtsSiteAdmin)

class IRROF7FreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'tower_complete','tower_complete_comment', 'free_issue_material','free_issue_material_comment', 'link_material','link_material_comment', 'posted_by', 'is_approved')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )


admin.site.register(IRROF7Free, IRROF7FreeAdmin)


class BtsBudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'beneficiary_name','description', 'date','phoneNumber','quantity', 'rate','unit','amount','is_approved','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BtsBudget, BtsBudgetAdmin)

class AccessApprovalCivilAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'access_approval', 'access_approval_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(AccessApprovalCivil, AccessApprovalCivilAdmin)


class AccessApprovalInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'access_approval', 'access_approval_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(AccessApprovalInstallation, AccessApprovalInstallationAdmin)


class ProjectCostingAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'project_costing_file', 'material_cost',
                    'labour_cost', 'total_projected_cost', 'is_approved',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(ProjectCosting, ProjectCostingAdmin)


class ProjectPurchaseOrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'po_file', 'material_cost',
                    'labour_cost', 'total_cost_of_po', 'is_approved',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(ProjectPurchaseOrders, ProjectPurchaseOrdersAdmin)


class CommercialTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'approved_quote_file', 'approved_quote_amount', 'po_data','drawings_revised_approved','tower_type_allocated',
    'material_collection_from_steel_supplier','PO_steel_fabrication','customer_issued_quotation','project_costing_data','initial_invoice', 'initial_invoice_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
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
#
# ####################################### KPI ###############################################################################################################################
#
# class KpiAdmin(admin.ModelAdmin):
#     list_display = ('id', 'kpi', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('kpi', )
#     search_fields = ('kpi', )
#     list_editable = ('is_active', 'is_approved')
#
#
# admin.site.register(Kpi, KpiAdmin)
#
# ######################################## END #######################################################################################################################################
#
# ####################################### TASKS #################################################################################################,'track_docs'##############################
#
#
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('id', 'category_name','task_name', 'kpi', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('task_name', )
#     list_filter = ('category_name',)
#     search_fields = ('task_name', )
#     list_editable = ('is_active', 'is_approved')
#
#
# admin.site.register(Task, TaskAdmin)
# ######################################## END #######################################################################################################################################
#
# ####################################### SUBTASKS ###############################################################################################################################
#
# class SubTaskAdmin(admin.ModelAdmin):
#     list_display = ('id', 'task_name', 'subtask_name', 'kpi','posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
#     list_display_links = ('subtask_name', )
#     list_filter = ('task_name',)
#     search_fields = ('subtask_name', )
#     list_editable = ('is_active', 'is_approved')
#
#
# admin.site.register(SubTask, SubTaskAdmin)
#
# ######################################## END #######################################################################################################################################

#######################################START FOUNDATION IMAGES########################################################################################################################################
class FoundationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'setting_site_clearing', 'excavation_tower_base', 'binding', 'steel_fix_formwork','concrete_pour_curing_period', 'concrete_curing_period','dom_equipment','foundation_and_curing_comment','engineers', 'names_of_engineers','start_date','end_date', 'raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(FoundationImage, FoundationImageAdmin)

class SetSiteClearingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','task_id', 'setting_site_clearing_image_1', 'setting_site_clearing_image_2', 'setting_site_clearing_image_3', 'setting_site_clearing_comment', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'labour_cost', 'date_casual_cost', 'check_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SetSiteClearingImage, SetSiteClearingImageAdmin)


class TowerBaseImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','task_id', 'towerbase_image_1', 'towerbase_image_2', 'towerbase_image_3', 'tower_base_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerBaseImage, TowerBaseImageAdmin)


class BindingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'binding_image_1', 'binding_image_2', 'binding_image_3', 'binding_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BindingImage, BindingImageAdmin)


class SteelFixFormworkImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'steel_fix_formwork_image_1', 'steel_fix_formwork_image_2', 'steel_fix_formwork_image_3', 'steel_fix_formwork_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SteelFixFormworkImage, SteelFixFormworkImageAdmin)


class ConcretePourImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'concrete_pour_curing_image_1', 'concrete_pour_curing_image_2', 'concrete_pour_curing_image_3', 'concrete_pour_curing_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ConcretePourImage, ConcretePourImageAdmin)

class ConcreteCuringPeriodDocsAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'Rebar_Concrete_Inspection', 'Concrete_Inspection_Report', 'Concrete_Cube_Test','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ConcreteCuringPeriodDocs, ConcreteCuringPeriodDocsAdmin)

class ConcreteCuringPeriodImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'concrete_pour_curing_period_image_1', 'concrete_pour_curing_period_image_2', 'concrete_pour_curing_period_image_3', 'concrete_pour_curing_period_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ConcreteCuringPeriodImage, ConcreteCuringPeriodImageAdmin)


class DeliveryOfMaterialandEquipementAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'dom_equipment_image_1', 'dom_equipment_image_2', 'dom_equipment_image_3', 'dom_equipment_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(DeliveryOfMaterialandEquipement, DeliveryOfMaterialandEquipementAdmin)
######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################

class ExcavationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'excavation_image_1', 'excavation_image_2', 'excavation_image_3', 'excavation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'raise_flag','start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ExcavationImage, ExcavationImageAdmin)

class BS241ConcretePourCuringPeriodImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'bs241_concrete_pour_curing_period_image_1', 'bs241_concrete_pour_curing_period_image_2','bs241_concrete_pour_curing_period_image_3', 'bs241_concrete_pour_curing_period_comment', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(BS241ConcretePourCuringPeriodImage, BS241ConcretePourCuringPeriodImageAdmin)

class BS241ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'bs241_image_1', 'bs241_image_2','bs241_image_3', 'bs241_comment', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BS241Image, BS241ImageAdmin)

class BS241AndGeneatorSlabsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'foundation_foot_pouring', 'bs241_concrete_pour_pouring_period','bs241_and_generator_slabs_comment','engineers', 'names_of_engineers', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BS241AndGeneatorSlabsImage, BS241AndGeneatorSlabsImageAdmin)

######################################## END #######################################################################################################################################

#######################################GENERATOR SLABS FOUNDATION ###########################################################################################################################

class GenExcavationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'gen_excavation_image_1', 'gen_excavation_image_2', 'gen_excavation_image_3', 'gen_excavation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'raise_flag','start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(GenExcavationImage, GenExcavationImageAdmin)

class GenConcretePourCuringPeriodImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'gen_concrete_pour_period_image_1', 'gen_concrete_pour_period_image_2','gen_concrete_pour_period_image_3', 'gen_concrete_pour_period_comment', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(GenConcretePourCuringPeriodImage, GenConcretePourCuringPeriodImageAdmin)

class GenCableConduitsSettingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'gen_cable_conduits_image_1', 'gen_cable_conduits_image_2','gen_cable_conduits_image_3', 'gen_cable_conduits_comment', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(GenCableConduitsSettingImage, GenCableConduitsSettingImageAdmin)

class GeneatorSlabsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'gen_excavation', 'gen_concrete_pour_period','gen_cable_conduits','generator_slabs_comment','engineers', 'names_of_engineers', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(GeneatorSlabsImage, GeneatorSlabsImageAdmin)

######################################## END #######################################################################################################################################

####################################### FABRICATION ###########################################################################################################################

class FabricationQualityInspectionImageAdmin(admin.ModelAdmin):
   list_display = ('id', 'project_name','task_id','start_date','end_date', 'fabrication_quality_inspection_image_1','fabrication_quality_inspection_image_2','fabrication_quality_inspection_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','fabrication_quality_inspection_image_comment')
   list_display_links = ('project_name', )
   search_fields = ('project_name', )

admin.site.register(FabricationQualityInspectionImage, FabricationQualityInspectionImageAdmin)


class FabricationSteelDeckImageAdmin(admin.ModelAdmin):
   list_display = ('id', 'project_name','task_id','start_date','end_date', 'fabrication_steel_deck_image_1','fabrication_steel_deck_image_2','fabrication_steel_deck_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','fabrication_steel_deck_image_comment')
   list_display_links = ('project_name', )
   search_fields = ('project_name', )

admin.site.register(FabricationSteelDeckImage, FabricationSteelDeckImageAdmin)

class GalvanisationImageAdmin(admin.ModelAdmin):
   list_display = ('id', 'project_name','start_date','end_date', 'galvanisation_image_1','galvanisation_image_2','galvanisation_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','galvanisation_image_comment')
   list_display_links = ('project_name', )
   search_fields = ('project_name', )

admin.site.register(GalvanisationImage, GalvanisationImageAdmin)

class FabricationRooftopImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','team_task_id','start_date','end_date','engineers', 'names_of_engineers','raise_flag','fabrication_quality_inspection_image','fabrication_steel_deck_image','galvanization_image','fabrication_rooftop_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register(FabricationRooftopImage, FabricationRooftopImageAdmin)
######################################## END #######################################################################################################################################

####################################### BOUNDARY WALL ###########################################################################################################################

class FoundFootPourImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'foundfootpour_image_1', 'foundfootpour_image_2', 'foundfootpour_image_3', 'foundfootpour_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(FoundFootPourImage, FoundFootPourImageAdmin)

class BlockworkPanelConstImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'blockwallpanelconst_image_1', 'blockwallpanelconst_image_2', 'blockwallpanelconst_image_3', 'blockwallpanelconst_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BlockworkPanelConstImage, BlockworkPanelConstImageAdmin)

class GateInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'gateinstallation_image_1', 'gateinstallation_image_2', 'gateinstallation_image_3','gateinstallation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(GateInstallationImage, GateInstallationImageAdmin)


class RazorElectricFenceImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'razorelectricfance_image_1', 'razorelectricfance_image_2', 'razorelectricfance_image_3', 'razorelectricfance_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(RazorElectricFenceImage, RazorElectricFenceImageAdmin)

class BWConcretePourCuringPeriodImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'bw_concrete_pour_curing_period_image_1', 'bw_concrete_pour_curing_period_image_2', 'bw_concrete_pour_curing_period_image_3', 'bw_concrete_pour_curing_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(BWConcretePourCuringPeriodImage, BWConcretePourCuringPeriodImageAdmin)

class ExcavationstripFoundationsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'excavationstrip_foundations_image_1', 'excavationstrip_foundations_image_2', 'excavationstrip_foundations_image_3', 'excavationstrip_foundations_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(ExcavationstripFoundationsImage, ExcavationstripFoundationsImageAdmin)

class BWBlindingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'bw_blinding_image_1', 'bw_blinding_image_2', 'bw_blinding_image_3', 'bw_blinding_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(BWBlindingImage, BWBlindingImageAdmin)

class BWCableConduitsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'bw_cable_conduits_image_1', 'bw_cable_conduits_image_2', 'bw_cable_conduits_image_3', 'bw_cable_conduits_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(BWCableConduitsImage, BWCableConduitsImageAdmin)

class BoundaryWallImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'foundation_foot_pouring', 'block_construction', 'gate_installation', 'razor_electric_fence','boundary_wall_comment','engineers', 'names_of_engineers', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BoundaryWallImage, BoundaryWallImageAdmin)
####################################### END###########################################################################################################################

####################################### MANHOLE SETTING OUT CONSTRUCTION ###########################################################################################################################
class  ManholeSettingExcavationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','start_date','end_date', 'manhole_setting_excavation_image_1','manhole_setting_excavation_image_2','manhole_setting_excavation_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','manhole_setting_excavation_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register( ManholeSettingExcavationImage, ManholeSettingExcavationImageAdmin)

class  ManholeBlindingAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','start_date','end_date', 'manhole_blinding_image_1','manhole_blinding_image_2','manhole_blinding_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','manhole_blinding_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register( ManholeBlinding, ManholeBlindingAdmin)

class  ManholeBlockworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','start_date','end_date', 'manhole_blindingwork_image_1','manhole_blindingwork_image_2','manhole_blindingwork_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','manhole_blindingwork_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register( ManholeBlockwork, ManholeBlockworkAdmin)

class ManholeSettingOutConstructionImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','team_task_id','start_date','end_date','engineers', 'names_of_engineers','raise_flag','manhole_setting_excavation_image','manhole_blinding_image','manhole_blockwork_image','manhole_setting_out_construction_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register( ManholeSettingOutConstructionImage, ManholeSettingOutConstructionImageAdmin)

#######################################  END ###########################################################################################################################

#######################################  TOWER & ANTENNA_COAX ###########################################################################################################################

class TowerErectionImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'tower_erection_image_1', 'tower_erection_image_2', 'tower_erection_image_3', 'tower_erection_comment', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerErectionImage, TowerErectionImageAdmin)

class TowerPaintImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'tower_painting_image_1', 'tower_painting_image_2', 'tower_painting_image_3', 'tower_painting_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerPaintImage, TowerPaintImageAdmin)

class CableWaysImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'cable_ways_image_1', 'cable_ways_image_2', 'cable_ways_image_3','cable_ways_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost', 'start_date','end_date','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(CableWaysImage, CableWaysImageAdmin)


class AntennaCoaxInstallImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'antenna_coax_installation_image_1', 'antenna_coax_installation_image_2', 'antenna_coax_installation_image_3', 'antenna_coax_installation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(AntennaCoaxInstallImage, AntennaCoaxInstallImageAdmin)

class EarthInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'earth_Installation_image_1', 'earth_Installation_image_2', 'earth_Installation_image_3', 'earth_Installation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(EarthInstallationImage, EarthInstallationImageAdmin)

class CableInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'cable_installation_image_1', 'cable_installation_image_2', 'cable_installation_image_3', 'cable_installation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(CableInstallationImage, CableInstallationImageAdmin)

class AviationLightsInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'aviation_lights_installation_image_1', 'aviation_lights_installation_image_2', 'aviation_lights_installation_image_3', 'aviation_lights_installation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(AviationLightsInstallationImage, AviationLightsInstallationImageAdmin)

class TowerDeliveryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'tower_delivery_image_1', 'tower_delivery_image_2', 'tower_delivery_image_3', 'tower_delivery_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(TowerDeliveryImage, TowerDeliveryImageAdmin)

class TowerAntennaCoaxImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'tower_erection', 'tower_painting', 'cable_ways', 'antenna_coax_installation','tower_delivery','aviation_lights_installation_image',
    'earth_installation','cable_installation','tower_antenna_coax_comment','engineers', 'names_of_engineers', 'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerAntennaCoaxImage, TowerAntennaCoaxImageAdmin)
####################################### END###########################################################################################################################

class BTSinstallationTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost',  'start_date', 'BTSinstallation_image_1', 'BTSinstallation_image_2', 'BTSinstallation_image_3', 'BTSinstallation_comment',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(BTSinstallationTask, BTSinstallationTaskAdmin)


class MWInstallationTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost',  'start_date','MWinstallation_image_1', 'MWinstallation_image_2', 'MWinstallation_image_3', 'MWinstallation_comment',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(MWInstallationTask, MWInstallationTaskAdmin)


class TelecomTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'engineers', 'names_of_engineers', 'Installation_of_BTS', 'Installation_of_MW_links', 'link_commissioning', 'is_approved',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(TelecomTasks, TelecomTasksAdmin)


class UndergroundTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'Underground_ducting_and_manholes_image_1', 'Underground_ducting_and_manholes_image_2', 'Underground_ducting_and_manholes_image_3', 'Underground_ducting_and_manholes_images_comment',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(UndergroundTasks, UndergroundTasksAdmin)


class ReticulationAPSinstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'Electricalreticulation_APSInstallation_image_1', 'Electricalreticulation_APSInstallation_image_2', 'Electricalreticulation_APSInstallation_image_3', 'Electricalreticulation_APSInstallation_images_comment',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ReticulationAPSinstallation, ReticulationAPSinstallationAdmin)


class ElectricalEarthingAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date', 'Earthing_connections_and_testing_image_1', 'Earthing_connections_and_testing_image_2', 'Earthing_connections_and_testing_image_3', 'Earthing_connections_and_testing_images_comment',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ElectricalEarthing, ElectricalEarthingAdmin)


class GeneratorInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'Generator_and_Fuel_Tank_Installation_image_1', 'Generator_and_Fuel_Tank_Installation_image_2', 'Generator_and_Fuel_Tank_Installation_image_3', 'before_fuel_image_1',
                    'before_fuel_image_2', 'after_fuel_image_1', 'after_fuel_image_2', 'Generator_and_Fuel_Tank_Installation_comment', 'start_date','end_date','raise_flag', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(GeneratorInstallation, GeneratorInstallationAdmin)


class KPLCSolarImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'task_id', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'kplc_solar_installation_image_1', 'kplc_solar_installation_image_2', 'kplc_solar_installation_image_3', 'kplc_solar_installation_comment',
                     'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(KPLCSolarImage, KPLCSolarImageAdmin)


class ElectricalTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'team_task_id', 'engineers', 'names_of_engineers', 'Underground_ducting_and_manholes', 'Electricalreticulation_APSInstallation', 'Earthing_connections_and_testing', 'Generator_and_Fuel_Tank_Installation', 'KPLC_solar_installation',
                    'is_approved',  'start_date','end_date','raise_flag','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(ElectricalTasks, ElectricalTasksAdmin)


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


class IssuesAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'issue', 'issue_image', 'issue_sorted_image', 'closed', 'posted_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('issue', )
    list_filter = ('project_name',)
    search_fields = ('issue', )
    list_editable = ('is_active',)


admin.site.register(Issues, IssuesAdmin)


class InstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'health_documents_installation', 'electrical_tasks_data',
                    'telecom_tasks_data', 'as_built', 'snag_document', 'snag_document_comment',
                    'project_issues', 'conditional_acceptance_cert', 'conditional_acceptance_cert_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(InstallationTeam, InstallationTeamAdmin)


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

class HackingExistingColumnsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','start_date','end_date', 'hacking_existing_columns_image_1','hacking_existing_columns_image_2','hacking_existing_columns_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','hacking_existing_columns_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register(HackingExistingColumnsImage, HackingExistingColumnsImageAdmin)

class FormworkColumnsConcretePourCuringImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','start_date','end_date', 'formwork_columns_concrete_pour_curing_image_1','formwork_columns_concrete_pour_curing_image_2','formwork_columns_concrete_pour_curing_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','formwork_columns_concrete_pour_curing_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register(FormworkColumnsConcretePourCuringImage, FormworkColumnsConcretePourCuringImageAdmin)

class DeliveryToSiteImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','start_date','end_date', 'delivery_to_site_image_1','delivery_to_site_image_2','delivery_to_site_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','delivery_to_site_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register(DeliveryToSiteImage, DeliveryToSiteImageAdmin)

class LiftingHoistingFreeIssueImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','start_date','end_date', 'lifting_hoisting_free_issue_image_1','lifting_hoisting_free_issue_image_2','lifting_hoisting_free_issue_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','lifting_hoisting_free_issue_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register(LiftingHoistingFreeIssueImage, LiftingHoistingFreeIssueImageAdmin)

class FenceInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','start_date','end_date', 'fence_installation_image_1','fence_installation_image_2','fence_installation_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','fence_installation_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register(FenceInstallationImage, FenceInstallationImageAdmin)

class  SiteRestorationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','start_date','end_date', 'site_restoration_image_1','site_restoration_image_2','site_restoration_image_3','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','raise_flag','site_restoration_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register( SiteRestorationImage, SiteRestorationImageAdmin)

class InstallationRooftopImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','team_task_id','start_date','end_date','engineers', 'names_of_engineers','raise_flag','hacking_existing_columns_image','formwork_columns_concrete_pour_curing_image','delivery_to_site_image','lifting_hoisting_freeissue_image','fence_installation_image','site_restoration_image','installation_rooftop_image_comment')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )

admin.site.register( InstallationRooftopImage, InstallationRooftopImageAdmin)
