from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Project, ProcurementTeam, HealthDocumentsCivilTeam, CivilWorksTeam, FoundationImage, BTSAndGeneatorSlabsImage, SiteWallingImage, RFAndLinkImage, ElectricalImage, KPLCSolarImage, CommercialTeam, AccessApprovalCivil, AccessApprovalInstallation, HealthDocumentsInstallationTeam, InstallationTeam, SafaricomTeam


admin.site.register(User, UserAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'geotech_file', 'access_letter', 'approved_drawing',
                    'location', 'created_by', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(Project, ProjectAdmin)


class AccessApprovalCivilAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'access_approval',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(AccessApprovalCivil, AccessApprovalCivilAdmin)


class AccessApprovalInstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'access_approval',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(AccessApprovalInstallation,
                    AccessApprovalInstallationAdmin)


class CommercialTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'po_file', 'po_file_comment', 'initial_invoice',
                    'initial_invoice_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(CommercialTeam, CommercialTeamAdmin)


class ProcurementTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'po_steel', 'po_steel_comment', 'po_electrical_materials', 'po_electrical_materials_comment',
                    'po_subcontractors', 'po_subcontractors_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ProcurementTeam, ProcurementTeamAdmin)


class HealthDocumentsCivilTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'job_hazard_form', 'job_hazard_form_comment', 'incident_notification_form', 'incident_notification_form_comment', 'toolbox_meeting_form',
                    'toolbox_meeting_form_comment', 'communication_plan_form', 'communication_plan_form_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(HealthDocumentsCivilTeam, HealthDocumentsCivilTeamAdmin)


class FoundationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'foundation_and_curing_image',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(FoundationImage, FoundationImageAdmin)


class BTSAndGeneatorSlabsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'bts_and_generator_slabs_image',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(BTSAndGeneatorSlabsImage, BTSAndGeneatorSlabsImageAdmin)


class SiteWallingImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'site_walling_image',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SiteWallingImage, SiteWallingImageAdmin)


class RFAndLinkImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'rf_and_link_installation_image',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(RFAndLinkImage, RFAndLinkImageAdmin)


class ElectricalImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'electrical_installation_image',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(ElectricalImage, ElectricalImageAdmin)


class KPLCSolarImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'kplc_solar_installation_image',
                    'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(KPLCSolarImage, KPLCSolarImageAdmin)


class CivilWorksTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'health_documents_civil', 'health_documents_comment', 'access_approvals', 'access_approval_comment', 'foundation_images', 'foundation_and_curing_comment',
                    'slabs_images', 'bts_and_generator_slabs_comment', 'site_walling_images', 'site_walling_images_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(CivilWorksTeam, CivilWorksTeamAdmin)


class HealthDocumentsInstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'job_hazard_form', 'job_hazard_form_comment', 'incident_notification_form', 'incident_notification_form_comment', 'toolbox_meeting_form',
                    'toolbox_meeting_form_comment', 'communication_plan_form', 'communication_plan_form_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(HealthDocumentsInstallationTeam,
                    HealthDocumentsInstallationTeamAdmin)


class InstallationTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'health_documents_installation', 'health_documents_comment', 'access_approvals', 'access_approval_comment', 'rf_and_link_images', 'rf_and_link_installation_comment',
                    'electrical_connections_images', 'electrical_installation_comment', 'kplc_solar_images', 'kplc_solar_installation_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(InstallationTeam, InstallationTeamAdmin)


class SafaricomTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'signoff_and_rf_document', 'signoff_and_rf_document_comment', 'integration_parameter', 'integration_parameter_comment', 'snag_document', 'snag_document_comment',
                    'conditional_acceptance_cert', 'conditional_acceptance_cert_comment', 'final_acceptance_cert', 'final_acceptance_cert_comment', 'posted_by', 'is_approved', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('project_name', )
    list_filter = ('project_name',)
    search_fields = ('project_name', )
    list_editable = ('is_active',)


admin.site.register(SafaricomTeam, SafaricomTeamAdmin)
