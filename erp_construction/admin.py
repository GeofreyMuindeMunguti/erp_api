from django.contrib import admin
from .models import *
from .flag import *


# Register your models here.
class ProjectIconsAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'site_owner', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_owner', )
    search_fields = ('site_owner', )
    list_editable = ('is_active',)


admin.site.register(ProjectIcons, ProjectIconsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('category_name', )
    search_fields = ('category_name', )
    list_editable = ('is_active',)


admin.site.register(Category, CategoryAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'icon', 'site_number', 'BTS_type', 'site_owner', 'geotech_file', 'access_letter', 'approved_drawing','final_acceptance_cert', 'final_acceptance_cert_comment',
                    'location', 'created_by', 'status', 'turn_around_time', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(Project, ProjectAdmin)


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
    list_display = ('id', 'project_name', 'approved_quote_file', 'approved_quote_amount', 'po_data',
                    'project_costing_data', 'initial_invoice', 'initial_invoice_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(CommercialTeam, CommercialTeamAdmin)


class ProcurementTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'po_steel', 'po_steel_cost', 'po_electrical_materials', 'po_electrical_materials_cost',
                    'po_subcontractors', 'po_subcontractors_cost', 'total_material_cost','posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(ProcurementTeam, ProcurementTeamAdmin)


class HealthDocumentsCivilTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'job_hazard_form', 'job_hazard_form_comment', 'incident_notification_form', 'incident_notification_form_comment', 'toolbox_meeting_form',
                    'toolbox_meeting_form_comment', 'communication_plan_form', 'communication_plan_form_comment', 'health_documents_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(HealthDocumentsCivilTeam, HealthDocumentsCivilTeamAdmin)

####################################### KPI ###############################################################################################################################

class KpiAdmin(admin.ModelAdmin):
    list_display = ('id', 'kpi', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('kpi', )
    search_fields = ('kpi', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(Kpi, KpiAdmin)

######################################## END #######################################################################################################################################

####################################### TASKS #################################################################################################,'track_docs'##############################


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name','task_name', 'kpi', 'posted_by', 'is_approved', 'created_at', 'updated_at','end_date', 'is_active','track_docs')
    list_display_links = ('task_name', )
    list_filter = ('category_name',)
    search_fields = ('task_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(Task, TaskAdmin)
######################################## END #######################################################################################################################################

####################################### SUBTASKS ###############################################################################################################################

class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_name', 'subtask_name', 'kpi', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('subtask_name', )
    list_filter = ('task_name',)
    search_fields = ('subtask_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(SubTask, SubTaskAdmin)

######################################## END #######################################################################################################################################

#######################################START FOUNDATION IMAGES########################################################################################################################################
class FoundationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'setting_site_clearing', 'excavation_tower_base', 'binding', 'steel_fix_formwork','concrete_pour_curing', 'concrete_pour_period','foundation_and_curing_comment','engineers', 'names_of_engineers', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(FoundationImage, FoundationImageAdmin)

class SetSiteClearingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'setting_site_clearing_image_1', 'setting_site_clearing_image_2', 'setting_site_clearing_image_3', 'setting_site_clearing_comment', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'labour_cost', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SetSiteClearingImage, SetSiteClearingImageAdmin)


class TowerBaseImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','towerbase_image_1', 'towerbase_image_2', 'towerbase_image_3', 'tower_base_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerBaseImage, TowerBaseImageAdmin)


class BindingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'binding_image_1', 'binding_image_2', 'binding_image_3', 'binding_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BindingImage, BindingImageAdmin)


class SteelFixFormworkImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','steel_fix_formwork_image_1', 'steel_fix_formwork_image_2', 'steel_fix_formwork_image_3', 'steel_fix_formwork_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SteelFixFormworkImage, SteelFixFormworkImageAdmin)


class ConcretePourImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'concrete_pour_curing_image_1', 'concrete_pour_curing_image_2', 'concrete_pour_curing_image_3', 'concrete_pour_curing_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ConcretePourImage, ConcretePourImageAdmin)


class ConcreteCuringPeriodImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','concrete_pour_curing_period_image_1', 'concrete_pour_curing_period_image_2', 'concrete_pour_curing_period_image_3', 'concrete_pour_curing_period_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ConcreteCuringPeriodImage, ConcreteCuringPeriodImageAdmin)


######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################

class ExcavationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'excavation_image_1', 'excavation_image_2', 'excavation_image_3', 'excavation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ExcavationImage, ExcavationImageAdmin)

class BS241ConcretePourCuringPeriodImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'bs241_concrete_pour_curing_period_image_1', 'bs241_concrete_pour_curing_period_image_2','bs241_concrete_pour_curing_period_image_3', 'bs241_concrete_pour_curing_period_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BS241ConcretePourCuringPeriodImage, BS241ConcretePourCuringPeriodImageAdmin)

class BS241AndGeneatorSlabsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'foundation_foot_pouring', 'bs241_concrete_pour_pouring_period','bs241_and_generator_slabs_comment','engineers', 'names_of_engineers','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BS241AndGeneatorSlabsImage, BS241AndGeneatorSlabsImageAdmin)

######################################## END #######################################################################################################################################

####################################### BOUNDARY WALL ###########################################################################################################################

class FoundFootPourImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'foundfootpour_image_1', 'foundfootpour_image_2', 'foundfootpour_image_3', 'foundfootpour_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(FoundFootPourImage, FoundFootPourImageAdmin)

class BlockworkPanelConstImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','blockwallpanelconst_image_1', 'blockwallpanelconst_image_2', 'blockwallpanelconst_image_3', 'blockwallpanelconst_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BlockworkPanelConstImage, BlockworkPanelConstImageAdmin)

class GateInstallationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'gateinstallation_image_1', 'gateinstallation_image_2', 'gateinstallation_image_3','gateinstallation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(GateInstallationImage, GateInstallationImageAdmin)


class RazorElectricFenceImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'razorelectricfance_image_1', 'razorelectricfance_image_2', 'razorelectricfance_image_3', 'razorelectricfance_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(RazorElectricFenceImage, RazorElectricFenceImageAdmin)

class BoundaryWallImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','foundation_foot_pouring', 'block_construction', 'gate_installation', 'razor_electric_fence','boundary_wall_comment','engineers', 'names_of_engineers','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BoundaryWallImage, BoundaryWallImageAdmin)
####################################### END###########################################################################################################################


#######################################  TOWER & ANTENNA_COAX ###########################################################################################################################

class TowerErectionImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'tower_erection_image_1', 'tower_erection_image_2', 'tower_erection_image_3', 'tower_erection_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerErectionImage, TowerErectionImageAdmin)

class TowerPaintImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','tower_painting_image_1', 'tower_painting_image_2', 'tower_painting_image_3', 'tower_painting_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerPaintImage, TowerPaintImageAdmin)

class CableWaysImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'cable_ways_image_1', 'cable_ways_image_2', 'cable_ways_image_3','cable_ways_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(CableWaysImage, CableWaysImageAdmin)


class AntennaCoaxInstallImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'antenna_coax_installation_image_1', 'antenna_coax_installation_image_2', 'antenna_coax_installation_image_3', 'antenna_coax_installation_comment','no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(AntennaCoaxInstallImage, AntennaCoaxInstallImageAdmin)

class TowerAntennaCoaxImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','tower_erection', 'tower_painting', 'cable_ways', 'antenna_coax_installation','tower_antenna_coax_comment','engineers', 'names_of_engineers','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerAntennaCoaxImage, TowerAntennaCoaxImageAdmin)
####################################### END###########################################################################################################################

class BTSinstallationTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost',  'start_date', 'BTSinstallation_image_1', 'BTSinstallation_image_2', 'BTSinstallation_image_3', 'BTSinstallation_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(BTSinstallationTask, BTSinstallationTaskAdmin)


class MWInstallationTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost','engineers_cost',  'start_date','MWinstallation_image_1', 'MWinstallation_image_2', 'MWinstallation_image_3', 'MWinstallation_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(MWInstallationTask, MWInstallationTaskAdmin)


class TelecomTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'engineers', 'names_of_engineers', 'Installation_of_BTS', 'Installation_of_MW_links', 'link_commissioning', 'is_approved',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(TelecomTasks, TelecomTasksAdmin)


class UndergroundTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'Underground_ducting_and_manholes_image_1', 'Underground_ducting_and_manholes_image_2', 'Underground_ducting_and_manholes_image_3', 'Underground_ducting_and_manholes_images_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(UndergroundTasks, UndergroundTasksAdmin)


class ReticulationAPSinstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'Electricalreticulation_APSInstallation_image_1', 'Electricalreticulation_APSInstallation_image_2', 'Electricalreticulation_APSInstallation_image_3', 'Electricalreticulation_APSInstallation_images_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ReticulationAPSinstallation, ReticulationAPSinstallationAdmin)


class ElectricalEarthingAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost', 'start_date', 'Earthing_connections_and_testing_image_1', 'Earthing_connections_and_testing_image_2', 'Earthing_connections_and_testing_image_3', 'Earthing_connections_and_testing_images_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ElectricalEarthing, ElectricalEarthingAdmin)


class GeneratorInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'Generator_and_Fuel_Tank_Installation_image_1', 'Generator_and_Fuel_Tank_Installation_image_2', 'Generator_and_Fuel_Tank_Installation_image_3', 'before_fuel_image_1',
                    'before_fuel_image_2', 'after_fuel_image_1', 'after_fuel_image_2', 'Generator_and_Fuel_Tank_Installation_comment', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(GeneratorInstallation, GeneratorInstallationAdmin)


class KPLCSolarImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'engineers_cost',  'start_date', 'kplc_solar_installation_image_1', 'kplc_solar_installation_image_2', 'kplc_solar_installation_image_3', 'kplc_solar_installation_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(KPLCSolarImage, KPLCSolarImageAdmin)


class ElectricalTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'engineers', 'names_of_engineers', 'Underground_ducting_and_manholes', 'Electricalreticulation_APSInstallation', 'Earthing_connections_and_testing', 'Generator_and_Fuel_Tank_Installation', 'KPLC_solar_installation',
                    'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(ElectricalTasks, ElectricalTasksAdmin)


class CivilWorksTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'health_documents_civil', 'access_approvals', 'foundation_and_curing_images',
                    'bs241_and_generator_slabs_images', 'site_walling_images_field', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(CivilWorksTeam, CivilWorksTeamAdmin)


class HealthDocumentsInstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'job_hazard_form', 'job_hazard_form_comment', 'incident_notification_form', 'incident_notification_form_comment', 'toolbox_meeting_form',
                    'toolbox_meeting_form_comment', 'communication_plan_form', 'communication_plan_form_comment', 'health_documents_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(HealthDocumentsInstallationTeam, HealthDocumentsInstallationTeamAdmin)


class InstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'health_documents_installation', 'access_approvals', 'electrical_tasks_data',
                    'telecom_tasks_data', 'as_built', 'signoff', 'signoff_comment','rfi_document','rfi_document_comment', 'integration_parameter', 'integration_parameter_comment', 'snag_document', 'snag_document_comment',
                    'conditional_acceptance_cert', 'conditional_acceptance_cert_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(InstallationTeam, InstallationTeamAdmin)
