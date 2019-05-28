from django.contrib import admin
from .models import *


# Register your models here.
class ProjectIconsAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'site_owner', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('site_owner', )
    search_fields = ('site_owner', )
    list_editable = ('is_active',)


admin.site.register(ProjectIcons, ProjectIconsAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'icon', 'site_number', 'BTS_type', 'site_owner', 'geotech_file', 'access_letter', 'approved_drawing',
                    'location', 'created_by', 'created_at', 'updated_at', 'is_active')
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
    list_display = ('id', 'project_name', 'po_steel', 'po_steel_comment', 'po_electrical_materials', 'po_electrical_materials_comment',
                    'po_subcontractors', 'po_subcontractors_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
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


class SetSiteClearingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'setting_site_clearing_image_1', 'setting_site_clearing_image_2', 'setting_site_clearing_image_3', 'setting_site_clearing_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SetSiteClearingImage, SetSiteClearingImageAdmin)


class TowerBaseImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','towerbase_image_1', 'towerbase_image_2', 'towerbase_image_3', 'tower_base_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(TowerBaseImage, TowerBaseImageAdmin)


class BindingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'binding_image_1', 'binding_image_2', 'binding_image_3', 'binding_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BindingImage, BindingImageAdmin)


class SteelFixFormworkImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name','steel_fix_formwork_image_1', 'steel_fix_formwork_image_2', 'steel_fix_formwork_image_3', 'steel_fix_formwork_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SteelFixFormworkImage, SteelFixFormworkImageAdmin)


class ConcretePourCuringImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'concrete_pour_curing_image_1', 'concrete_pour_curing_image_2', 'concrete_pour_curing_image_3', 'concrete_pour_curing_comment','created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ConcretePourCuringImage, ConcretePourCuringImageAdmin)


class BTSAndGeneatorSlabsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'bts_and_generator_slabs_image_1', 'bts_and_generator_slabs_image_2', 'bts_and_generator_slabs_image_3', 'bts_and_generator_slabs_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BTSAndGeneatorSlabsImage, BTSAndGeneatorSlabsImageAdmin)


class SiteWallingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'site_walling_image_1', 'site_walling_image_2', 'site_walling_image_3', 'site_walling_images_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SiteWallingImage, SiteWallingImageAdmin)


class BTSinstallationTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'start_date', 'BTSinstallation_image_1', 'BTSinstallation_image_2', 'BTSinstallation_image_3', 'BTSinstallation_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)

admin.site.register(BTSinstallationTask, BTSinstallationTaskAdmin)


class MWInstallationTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'start_date','MWinstallation_image_1', 'MWinstallation_image_2', 'MWinstallation_image_3', 'MWinstallation_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(MWInstallationTask, MWInstallationTaskAdmin)


class TelecomTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'engineers', 'Installation_of_BTS', 'Installation_of_MW_links', 'link_commissioning', 'is_approved',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(TelecomTasks, TelecomTasksAdmin)


class UndergroundTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'start_date', 'Underground_ducting_and_manholes_image_1', 'Underground_ducting_and_manholes_image_2', 'Underground_ducting_and_manholes_image_3', 'Underground_ducting_and_manholes_images_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(UndergroundTasks, UndergroundTasksAdmin)


class ReticulationAPSinstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'start_date', 'Electricalreticulation_APSInstallation_image_1', 'Electricalreticulation_APSInstallation_image_2', 'Electricalreticulation_APSInstallation_image_3', 'Electricalreticulation_APSInstallation_images_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ReticulationAPSinstallation, ReticulationAPSinstallationAdmin)


class ElectricalEarthingAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'start_date', 'Earthing_connections_and_testing_image_1', 'Earthing_connections_and_testing_image_2', 'Earthing_connections_and_testing_image_3', 'Earthing_connections_and_testing_images_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ElectricalEarthing, ElectricalEarthingAdmin)


class GeneratorInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'start_date', 'Generator_and_Fuel_Tank_Installation_image_1', 'Generator_and_Fuel_Tank_Installation_image_2', 'Generator_and_Fuel_Tank_Installation_image_3', 'before_fuel_image_1',
                    'before_fuel_image_2', 'after_fuel_image_1', 'after_fuel_image_2', 'Generator_and_Fuel_Tank_Installation_comment', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(GeneratorInstallation, GeneratorInstallationAdmin)


class KPLCSolarImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'no_of_casuals', 'names_of_casuals', 'casuals_cost', 'start_date', 'kplc_solar_installation_image_1', 'kplc_solar_installation_image_2', 'kplc_solar_installation_image_3', 'kplc_solar_installation_comment',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(KPLCSolarImage, KPLCSolarImageAdmin)


class ElectricalTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'engineers', 'Underground_ducting_and_manholes', 'Electricalreticulation_APSInstallation', 'Earthing_connections_and_testing', 'Generator_and_Fuel_Tank_Installation', 'KPLC_solar_installation',
                    'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active', 'is_approved')


admin.site.register(ElectricalTasks, ElectricalTasksAdmin)


class CivilWorksTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'health_documents_civil', 'access_approvals', 'foundation_and_curing_images',
                    'bts_and_generator_slabs_images', 'site_walling_images_field', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
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
                    'telecom_tasks_data', 'signoff', 'signoff_comment','rf_document','rf_document_comment', 'integration_parameter', 'integration_parameter_comment', 'snag_document', 'snag_document_comment',
                    'conditional_acceptance_cert', 'conditional_acceptance_cert_comment', 'final_acceptance_cert', 'final_acceptance_cert_comment','posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(InstallationTeam, InstallationTeamAdmin)
