from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser, Location, Casual, Engineer, Rates
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class ProjectIcons(models.Model):
    icon = models.ImageField(upload_to='images/Project/Icons/%Y/%m/%d/')
    site_owner = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.site_owner


class Project(models.Model):
    project_name = models.CharField(max_length=100, unique=True)
    site_number = models.CharField(max_length=100, unique=True)
    BTS_type = models.CharField(max_length=100)
    site_owner = models.CharField(max_length=100)
    icon = models.ForeignKey(ProjectIcons, on_delete=models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    geotech_file = models.FileField(upload_to='files/Project/geotech/%Y/%m/%d/')
    access_letter = models.FileField(upload_to='files/Project/accessletters/%Y/%m/%d/')
    approved_drawing = models.FileField(upload_to='files/Project/approveddrawings/%Y/%m/%d/')
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name


class SetSiteClearingImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    setting_site_clearing_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/siteclearing/%Y/%m/%d/')
    setting_site_clearing_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/siteclearing/%Y/%m/%d/')
    setting_site_clearing_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/siteclearing/%Y/%m/%d/')
    setting_site_clearing_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class TowerBaseImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    towerbase_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/towerbase/%Y/%m/%d/')
    towerbase_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/towerbase/%Y/%m/%d/')
    towerbase_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/towerbase/%Y/%m/%d/')
    tower_base_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class BindingImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    binding_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/binding/%Y/%m/%d/')
    binding_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/binding/%Y/%m/%d/')
    binding_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/binding/%Y/%m/%d/')
    binding_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class SteelFixFormworkImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    steel_fix_formwork_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/steelfix/%Y/%m/%d/')
    steel_fix_formwork_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/steelfix/%Y/%m/%d/')
    steel_fix_formwork_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/steelfix/%Y/%m/%d/')
    steel_fix_formwork_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class ConcretePourCuringImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    concrete_pour_curing_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/')
    concrete_pour_curing_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/')
    concrete_pour_curing_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/')
    concrete_pour_curing_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class FoundationImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    setting_site_clearing = models.ForeignKey(SetSiteClearingImage, on_delete=models.DO_NOTHING)
    excavation_tower_base = models.ForeignKey(TowerBaseImage, on_delete=models.DO_NOTHING)
    binding = models.ForeignKey(BindingImage, on_delete=models.DO_NOTHING)
    steel_fix_formwork = models.ForeignKey(SteelFixFormworkImage, on_delete=models.DO_NOTHING)
    concrete_pour_curing = models.ForeignKey(ConcretePourCuringImage, on_delete=models.DO_NOTHING)
    foundation_and_curing_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class BTSAndGeneatorSlabsImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    bts_and_generator_slabs_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/slabs/%Y/%m/%d/')
    bts_and_generator_slabs_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/slabs/%Y/%m/%d/')
    bts_and_generator_slabs_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/slabs/%Y/%m/%d/')
    bts_and_generator_slabs_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class SiteWallingImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    site_walling_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/sitewalling/%Y/%m/%d/')
    site_walling_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/sitewalling/%Y/%m/%d/')
    site_walling_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/sitewalling/%Y/%m/%d/')
    site_walling_images_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class ProjectPurchaseOrders(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    po_file = models.FileField(upload_to='files/CommercialTeam/pofile/%Y/%m/%d/', blank=True, null=True)
    material_cost = models.IntegerField()
    labour_cost = models.IntegerField()
    total_cost_of_po = models.IntegerField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def totalPOS(self):
        count = self.objects.all().count()
        return count


class ProjectCosting(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    project_costing_file = models.FileField(upload_to='files/CommercialTeam/projectcosting/%Y/%m/%d/', blank=True, null=True)
    material_cost = models.IntegerField()
    labour_cost = models.IntegerField()
    total_projected_cost = models.IntegerField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def totalPOS(self):
        count = self.objects.all().count()
        return count


class CommercialTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    approved_quote_file = models.FileField(upload_to='files/CommercialTeam/approvedquote/%Y/%m/%d/')
    approved_quote_amount = models.IntegerField()
    po_data = models.OneToOneField(ProjectPurchaseOrders, on_delete=models.CASCADE, blank=True, null=True)
    project_costing_data = models.OneToOneField(ProjectCosting, on_delete=models.CASCADE, blank=True, null=True)
    initial_invoice = models.FileField(upload_to='files/CommercialTeam/initialinvoice/%Y/%m/%d/', blank=True, null=True)
    initial_invoice_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class ProcurementTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    po_steel = models.FileField(upload_to='files/ProcurementTeam/posteel/%Y/%m/%d/', blank=True, null=True)
    po_steel_comment = models.CharField(max_length=100, blank=True, null=True)
    po_electrical_materials = models.FileField(upload_to='files/ProcurementTeam/poelectrical/%Y/%m/%d/', blank=True, null=True)
    po_electrical_materials_comment = models.CharField(max_length=100, blank=True, null=True)
    po_subcontractors = models.FileField(upload_to='files/ProcurementTeam/posubcontractor/%Y/%m/%d/', blank=True, null=True)
    po_subcontractors_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class HealthDocumentsCivilTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/jobhazard/%Y/%m/%d/')
    job_hazard_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/incident/%Y/%m/%d/')
    incident_notification_form_comment = models.CharField(max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/toolbox/%Y/%m/%d/')
    toolbox_meeting_form_comment = models.CharField(max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/communication/%Y/%m/%d/')
    communication_plan_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class AccessApprovalCivil(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to='files/CivilWorksTeam/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class CivilWorksTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsCivilTeam)
    access_approvals_field = models.ManyToManyField(AccessApprovalCivil)
    foundation_and_curing_images = models.OneToOneField(FoundationImage, on_delete=models.DO_NOTHING)
    bts_and_generator_slabs_images = models.OneToOneField(BTSAndGeneatorSlabsImage, on_delete=models.DO_NOTHING)
    site_walling_images_field = models.OneToOneField(SiteWallingImage, on_delete=models.DO_NOTHING)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def health_documents_civil(self):
        return "\n , ".join(str([v.project_name for v in self.health_documents.all()]))

    def access_approvals(self):
        return "\n , ".join(str([v.project_name for v in self.access_approvals_field.all()]))


class HealthDocumentsInstallationTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/jobhazard/%Y/%m/%d/')
    job_hazard_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/incident/%Y/%m/%d/')
    incident_notification_form_comment = models.CharField(max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/toolbox/%Y/%m/%d/')
    toolbox_meeting_form_comment = models.CharField(max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/communication/%Y/%m/%d/')
    communication_plan_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class AccessApprovalInstallation(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to='files/InstallationTeam/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class UndergroundTasks(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    Underground_ducting_and_manholes_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTasks/%Y/%m/%d/')
    Underground_ducting_and_manholes_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTasks/%Y/%m/%d/')
    Underground_ducting_and_manholes_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTasks/%Y/%m/%d/')
    Underground_ducting_and_manholes_images_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        rate_data = Rates.objects.get(id=1)
        casual_rate = rate_data.casuals_rate
        count = self.no_of_casuals_atsite.count()
        cost = (count * casual_rate)
        return cost


class ReticulationAPSinstallation(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    Electricalreticulation_APSInstallation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/')
    Electricalreticulation_APSInstallation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/')
    Electricalreticulation_APSInstallation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/')
    Electricalreticulation_APSInstallation_images_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        rate_data = Rates.objects.get(id=1)
        casual_rate = rate_data.casuals_rate
        count = self.no_of_casuals_atsite.count()
        cost = (count * casual_rate)
        return cost


class ElectricalEarthing(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    Earthing_connections_and_testing_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/')
    Earthing_connections_and_testing_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/')
    Earthing_connections_and_testing_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/')
    Earthing_connections_and_testing_images_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        rate_data = Rates.objects.get(id=1)
        casual_rate = rate_data.casuals_rate
        count = self.no_of_casuals_atsite.count()
        cost = (count * casual_rate)
        return cost


class GeneratorInstallation(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    Generator_and_Fuel_Tank_Installation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/')
    Generator_and_Fuel_Tank_Installation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/')
    Generator_and_Fuel_Tank_Installation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/')
    before_fuel_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    before_fuel_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    after_fuel_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    after_fuel_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    Generator_and_Fuel_Tank_Installation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        rate_data = Rates.objects.get(id=1)
        casual_rate = rate_data.casuals_rate
        count = self.no_of_casuals_atsite.count()
        cost = (count * casual_rate)
        return cost


class KPLCSolarImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    kplc_solar_installation_image_1 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/')
    kplc_solar_installation_image_2 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/')
    kplc_solar_installation_image_3 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/')
    kplc_solar_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        rate_data = Rates.objects.get(id=1)
        casual_rate = rate_data.casuals_rate
        count = self.no_of_casuals_atsite.count()
        cost = (count * casual_rate)
        return cost


class ElectricalTasks(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
    Underground_ducting_and_manholes = models.OneToOneField(UndergroundTasks, on_delete=models.CASCADE, blank=True, null=True)
    Electricalreticulation_APSInstallation = models.OneToOneField(ReticulationAPSinstallation, on_delete=models.CASCADE, blank=True, null=True)
    Earthing_connections_and_testing = models.OneToOneField(ElectricalEarthing, on_delete=models.CASCADE, blank=True, null=True)
    Generator_and_Fuel_Tank_Installation = models.OneToOneField(GeneratorInstallation, on_delete=models.CASCADE, blank=True, null=True)
    KPLC_solar_installation = models.OneToOneField(KPLCSolarImage, on_delete=models.CASCADE, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.engineer_name for v in self.engineers_atsite.all()]


class BTSinstallationTask(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    BTSinstallation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Telecom/BTSinstallation/%Y/%m/%d/')
    BTSinstallation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Telecom/BTSinstallation/%Y/%m/%d/')
    BTSinstallation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Telecom/BTSinstallation/%Y/%m/%d/')
    BTSinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        rate_data = Rates.objects.get(id=1)
        casual_rate = rate_data.casuals_rate
        count = self.no_of_casuals_atsite.count()
        cost = (count * casual_rate)
        return cost


class MWInstallationTask(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    MWinstallation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Telecom/MWinstallation/%Y/%m/%d/')
    MWinstallation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Telecom/MWinstallation/%Y/%m/%d/')
    MWinstallation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Telecom/MWinstallation/%Y/%m/%d/')
    MWinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        rate_data = Rates.objects.get(id=1)
        casual_rate = rate_data.casuals_rate
        count = self.no_of_casuals_atsite.count()
        cost = (count * casual_rate)
        return cost


class TelecomTasks(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
    Installation_of_BTS = models.OneToOneField(BTSinstallationTask, on_delete=models.CASCADE, blank=True, null=True)
    Installation_of_MW_links = models.OneToOneField(MWInstallationTask, on_delete=models.CASCADE, blank=True, null=True)
    link_commissioning = models.BooleanField(default=False);
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.engineer_name for v in self.engineers_atsite.all()]


class InstallationTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsInstallationTeam)
    access_approvals_field = models.ManyToManyField(AccessApprovalInstallation)
    electrical_tasks_data = models.OneToOneField(ElectricalTasks, on_delete=models.DO_NOTHING, blank=True, null=True)
    telecom_tasks_data = models.OneToOneField(TelecomTasks, on_delete=models.DO_NOTHING, blank=True, null=True)
    signoff = models.FileField(upload_to='files/SafaricomTeam/signoff/%Y/%m/%d/')
    signoff_comment = models.CharField(max_length=100, blank=True, null=True)
    rf_document = models.FileField(upload_to='files/SafaricomTeam/rf/%Y/%m/%d/')
    rf_document_comment = models.CharField(max_length=100, blank=True, null=True)
    integration_parameter = models.BooleanField(default=False)
    integration_parameter_comment = models.CharField(max_length=100, blank=True, null=True)
    snag_document = models.FileField(upload_to='files/SafaricomTeam/snag/%Y/%m/%d/')
    snag_document_comment = models.CharField(max_length=100, blank=True, null=True)
    conditional_acceptance_cert = models.FileField(upload_to='files/SafaricomTeam/conditionalcert/%Y/%m/%d/')
    conditional_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    final_acceptance_cert = models.FileField(upload_to='files/SafaricomTeam/finalcert/%Y/%m/%d/')
    final_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def health_documents_installation(self):
        return "\n , ".join(str([v.project_name for v in self.health_documents.all()]))

    def access_approvals(self):
        return "\n , ".join(str([v.project_name for v in self.access_approvals_field.all()]))
