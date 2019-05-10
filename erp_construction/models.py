from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class Employee(models.Model):
    employee_id = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    team = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.employee_id

    @classmethod
    def get_employees(cls):
        employees = Employee.objects.all()
        return employees

    @classmethod
    def get_single_emp(cls, employee_id):
        single_emp = Employee.objects.get(employee=employee_id)
        return single_emp


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    #employee_id = models.ForeignKey(Employee, null=True, on_delete=models.DO_NOTHING, related_name='employees')
    username = models.CharField(blank=True, null=True, max_length=150)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Project(models.Model):
    project_name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200)
    geotech_file = models.FileField(
        upload_to='files/Project/geotech/%Y/%m/%d/')
    access_letter = models.FileField(
        upload_to='files/Project/accessletters/%Y/%m/%d/')
    approved_drawing = models.FileField(
        upload_to='files/Project/approveddrawings/%Y/%m/%d/')
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name


class FoundationImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    foundation_and_curing_image = models.ImageField(
        upload_to='images/CivilWorksTeam/foundation/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class BTSAndGeneatorSlabsImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    bts_and_generator_slabs_image = models.ImageField(
        upload_to='images/CivilWorksTeam/slabs/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class SiteWallingImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    site_walling_image = models.ImageField(
        upload_to='images/CivilWorksTeam/sitewalling/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class RFAndLinkImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    rf_and_link_installation_image = models.ImageField(
        upload_to='images/InstallationTeam/RFAndLink/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class ElectricalImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    electrical_installation_image = models.ImageField(
        upload_to='images/InstallationTeam/Electrical/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class KPLCSolarImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    kplc_solar_installation_image = models.ImageField(
        upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class CommercialTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    po_file = models.FileField(
        upload_to='files/CommercialTeam/pofile/%Y/%m/%d/')
    po_file_comment = models.CharField(max_length=100, blank=True, null=True)
    initial_invoice = models.FileField(
        upload_to='files/CommercialTeam/initialinvoice/%Y/%m/%d/')
    initial_invoice_comment = models.CharField(
        max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class ProcurementTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    po_steel = models.FileField(
        upload_to='files/ProcurementTeam/posteel/%Y/%m/%d/')
    po_steel_comment = models.CharField(max_length=100, blank=True, null=True)
    po_electrical_materials = models.FileField(
        upload_to='files/ProcurementTeam/poelectrical/%Y/%m/%d/')
    po_electrical_materials_comment = models.CharField(
        max_length=100, blank=True, null=True)
    po_subcontractors = models.FileField(
        upload_to='files/ProcurementTeam/posubcontractor/%Y/%m/%d/')
    po_subcontractors_comment = models.CharField(
        max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class HealthDocumentsCivilTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(
        upload_to='files/HealthDocumentsCivilTeam/jobhazard/%Y/%m/%d/')
    job_hazard_form_comment = models.CharField(
        max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(
        upload_to='files/HealthDocumentsCivilTeam/incident/%Y/%m/%d/')
    incident_notification_form_comment = models.CharField(
        max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(
        upload_to='files/HealthDocumentsCivilTeam/toolbox/%Y/%m/%d/')
    toolbox_meeting_form_comment = models.CharField(
        max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(
        upload_to='files/HealthDocumentsCivilTeam/communication/%Y/%m/%d/')
    communication_plan_form_comment = models.CharField(
        max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class AccessApprovalCivil(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    access_approval = models.FileField(
        upload_to='files/CivilWorksTeam/accessapproval/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class CivilWorksTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsCivilTeam)
    health_documents_comment = ArrayField(
        models.CharField(max_length=100, blank=True, null=True))
    access_approvals_field = models.ManyToManyField(AccessApprovalCivil)
    access_approval_comment = models.CharField(
        max_length=100, blank=True, null=True)
    foundation_and_curing_images = models.ManyToManyField(FoundationImage)
    foundation_and_curing_comment = models.CharField(
        max_length=100, blank=True, null=True)
    bts_and_generator_slabs_images = models.ManyToManyField(
        BTSAndGeneatorSlabsImage)
    bts_and_generator_slabs_comment = models.CharField(
        max_length=100, blank=True, null=True)
    site_walling_images_field = models.ManyToManyField(SiteWallingImage)
    site_walling_images_comment = models.CharField(
        max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def health_documents_civil(self):
        return "\n , ".join(str([v.project_name for v in self.health_documents.all()]))

    def foundation_images(self):
        return "\n , ".join(str([v.project_name for v in self.foundation_and_curing_images.all()]))

    def slabs_images(self):
        return "\n , ".join(str([v.project_name for v in self.bts_and_generator_slabs_images.all()]))

    def site_walling_images(self):
        return "\n , ".join(str([v.project_name for v in self.site_walling_images_field.all()]))

    def access_approvals(self):
        return "\n , ".join(str([v.project_name for v in self.access_approvals_field.all()]))


class HealthDocumentsInstallationTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(
        upload_to='files/HealthDocumentsInstallationTeam/jobhazard/%Y/%m/%d/')
    job_hazard_form_comment = models.CharField(
        max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(
        upload_to='files/HealthDocumentsInstallationTeam/incident/%Y/%m/%d/')
    incident_notification_form_comment = models.CharField(
        max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(
        upload_to='files/HealthDocumentsInstallationTeam/toolbox/%Y/%m/%d/')
    toolbox_meeting_form_comment = models.CharField(
        max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(
        upload_to='files/HealthDocumentsInstallationTeam/communication/%Y/%m/%d/')
    communication_plan_form_comment = models.CharField(
        max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class AccessApprovalInstallation(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    access_approval = models.FileField(
        upload_to='files/InstallationTeam/accessapproval/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class InstallationTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsInstallationTeam)
    health_documents_comment = ArrayField(
        models.CharField(max_length=100, blank=True, null=True))
    access_approvals_field = models.ManyToManyField(AccessApprovalInstallation)
    access_approval_comment = models.CharField(
        max_length=100, blank=True, null=True)
    rf_and_link_installation_images = models.ManyToManyField(RFAndLinkImage)
    rf_and_link_installation_comment = models.CharField(
        max_length=100, blank=True, null=True)
    electrical_installation_images = models.ManyToManyField(ElectricalImage)
    electrical_installation_comment = models.CharField(
        max_length=100, blank=True, null=True)
    kplc_solar_installation_images = models.ManyToManyField(KPLCSolarImage)
    kplc_solar_installation_comment = models.CharField(
        max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def health_documents_installation(self):
        return "\n , ".join(str([v.project_name for v in self.health_documents.all()]))

    def rf_and_link_images(self):
        return "\n , ".join(str([v.project_name for v in self.rf_and_link_installation_images.all()]))

    def electrical_connections_images(self):
        return "\n , ".join(str([v.project_name for v in self.electrical_installation_images.all()]))

    def kplc_solar_images(self):
        return "\n , ".join(str([v.project_name for v in self.kplc_solar_installation_images.all()]))

    def access_approvals(self):
        return "\n , ".join(str([v.project_name for v in self.access_approvals_field.all()]))


class SafaricomTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    signoff_and_rf_document = models.FileField(
        upload_to='files/SafaricomTeam/rfsignoff/%Y/%m/%d/')
    signoff_and_rf_document_comment = models.CharField(
        max_length=100, blank=True, null=True)
    integration_parameter = models.FileField(
        upload_to='files/SafaricomTeam/integrationparameters/%Y/%m/%d/')
    integration_parameter_comment = models.CharField(
        max_length=100, blank=True, null=True)
    snag_document = models.FileField(
        upload_to='files/SafaricomTeam/snag/%Y/%m/%d/')
    snag_document_comment = models.CharField(
        max_length=100, blank=True, null=True)
    conditional_acceptance_cert = models.FileField(
        upload_to='files/SafaricomTeam/conditionalcert/%Y/%m/%d/')
    conditional_acceptance_cert_comment = models.CharField(
        max_length=100, blank=True, null=True)
    final_acceptance_cert = models.FileField(
        upload_to='files/SafaricomTeam/finalcert/%Y/%m/%d/')
    final_acceptance_cert_comment = models.CharField(
        max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)
