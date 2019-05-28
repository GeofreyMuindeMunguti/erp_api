from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class Project(models.Model):
    project_name = models.CharField(max_length=100, unique=True)
    site_number = models.CharField(max_length=100, unique=True)
    BTS_type = models.CharField(max_length=100)
    site_owner = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    geotech_file = models.FileField(upload_to='files/Project/geotech/%Y/%m/%d/')
    access_letter = models.FileField(upload_to='files/Project/accessletters/%Y/%m/%d/')
    approved_drawing = models.FileField(upload_to='files/Project/approveddrawings/%Y/%m/%d/')
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name

#######################################START FOUNDATION IMAGES########################################################################################################################################
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
    excavation_tower_base= models.ForeignKey(TowerBaseImage, on_delete=models.DO_NOTHING)
    binding = models.ForeignKey(BindingImage, on_delete=models.DO_NOTHING)
    steel_fix_formwork= models.ForeignKey(SteelFixFormworkImage, on_delete=models.DO_NOTHING)
    concrete_pour_curing = models.ForeignKey(ConcretePourCuringImage, on_delete=models.DO_NOTHING)
    foundation_and_curing_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)
######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################

class ExcavationImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    excavation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    excavation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    excavation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    excavation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

class ConcretePourCuringPeriodImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    concrete_pour_curing_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/')
    concrete_pour_curing_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/')
    concrete_pour_curing_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/')
    concrete_pour_curing_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class BTSAndGeneatorSlabsImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    foundation_foot_pouring = models.ForeignKey(ExcavationImage, on_delete=models.DO_NOTHING)
    concrete_pour_period = models.ForeignKey(ConcretePourCuringPeriodImage, on_delete=models.DO_NOTHING)
    bts_and_generator_slabs_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)
######################################## END #######################################################################################################################################

####################################### BOUNDARY WALL ###########################################################################################################################


class FoundFootPourImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    foundfootpour_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    foundfootpour_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    foundfootpour_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    foundfootpour_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

class BlockworkPanelConstImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    blockwallpanelconst_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/BlockworkPanelConst/%Y/%m/%d/')
    blockwallpanelconst_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/BlockworkPanelConst/%Y/%m/%d/')
    blockwallpanelconst_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/BlockworkPanelConst/%Y/%m/%d/')
    blockwallpanelconst_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

class GateInstallationImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    gateinstallation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/GateInstallation/%Y/%m/%d/')
    gateinstallation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/GateInstallation/%Y/%m/%d/')
    gateinstallation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/GateInstallation/%Y/%m/%d/')
    gateinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

class RazorElectricFenceImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    razorelectricfance_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/RazorElectricFence/%Y/%m/%d/')
    razorelectricfance_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/RazorElectricFence/%Y/%m/%d/')
    razorelectricfance_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/RazorElectricFence/%Y/%m/%d/')
    razorelectricfance_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

class BoundaryWallImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    foundation_foot_pouring = models.ForeignKey(FoundFootPourImage, on_delete=models.DO_NOTHING)
    block_construction = models.ForeignKey(BlockworkPanelConstImage, on_delete=models.DO_NOTHING)
    gate_installation = models.ForeignKey(GateInstallationImage, on_delete=models.DO_NOTHING)
    razor_electric_fence = models.ForeignKey(RazorElectricFenceImage, on_delete=models.DO_NOTHING)
    boundary_wall_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)
######################################## END #######################################################################################################################################

####################################### TOWER & ANTENNA_COAX ###########################################################################################################################

class TowerErectionImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    tower_erection_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/towererection/%Y/%m/%d/')
    tower_erection_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/towererection/%Y/%m/%d/')
    tower_erection_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/towererection/%Y/%m/%d/')
    tower_erection_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

class TowerPaintImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    tower_painting_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/towerpainting/%Y/%m/%d/')
    tower_painting_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/towerpainting/%Y/%m/%d/')
    tower_painting_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/towerpainting/%Y/%m/%d/')
    tower_painting_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

class CableWaysImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    cable_ways_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/cableways/%Y/%m/%d/')
    cable_ways_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/cableways/%Y/%m/%d/')
    cable_ways_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/cableways/%Y/%m/%d/')
    cable_ways_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

class AntennaCoaxInstallImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    antenna_coax_installation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/antennacoaxinstallation/%Y/%m/%d/')
    antenna_coax_installation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/antennacoaxinstallation/%Y/%m/%d/')
    antenna_coax_installation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/antennacoaxinstallation/%Y/%m/%d/')
    antenna_coax_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

class TowerAntennaCoaxImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    tower_erection = models.ForeignKey(TowerErectionImage, on_delete=models.DO_NOTHING)
    tower_painting = models.ForeignKey(TowerPaintImage, on_delete=models.DO_NOTHING)
    cable_ways = models.ForeignKey(CableWaysImage, on_delete=models.DO_NOTHING)
    antenna_coax_installation = models.ForeignKey(AntennaCoaxInstallImage, on_delete=models.DO_NOTHING)
    tower_antenna_coax_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

######################################## END #######################################################################################################################################


####################################### INSTALLATION ###########################################################################################################################


class RFAndLinkImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    rf_and_link_installation_image_1 = models.ImageField(upload_to='images/InstallationTeam/RFAndLink/%Y/%m/%d/')
    rf_and_link_installation_image_2 = models.ImageField(upload_to='images/InstallationTeam/RFAndLink/%Y/%m/%d/')
    rf_and_link_installation_image_3 = models.ImageField(upload_to='images/InstallationTeam/RFAndLink/%Y/%m/%d/')
    rf_and_link_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class ElectricalImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    electrical_installation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/%Y/%m/%d/')
    electrical_installation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/%Y/%m/%d/')
    electrical_installation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/%Y/%m/%d/')
    electrical_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class KPLCSolarImage(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    kplc_solar_installation_image_1 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/')
    kplc_solar_installation_image_2 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/')
    kplc_solar_installation_image_3 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/')
    kplc_solar_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class CommercialTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    po_file = models.FileField(upload_to='files/CommercialTeam/pofile/%Y/%m/%d/', blank=True, null=True)
    po_file_comment = models.CharField(max_length=100, blank=True, null=True)
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
    po_steel_cost = models.IntegerField(blank=True, null=True)
    po_electrical_materials = models.FileField(upload_to='files/ProcurementTeam/poelectrical/%Y/%m/%d/', blank=True, null=True)
    po_electrical_materials_cost = models.IntegerField(blank=True, null=True)
    po_subcontractors = models.FileField(upload_to='files/ProcurementTeam/posubcontractor/%Y/%m/%d/', blank=True, null=True)
    po_subcontractors_cost = models.IntegerField(blank=True, null=True)
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
    site_walling_images_field = models.OneToOneField(BoundaryWallImage, on_delete=models.DO_NOTHING)
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


class InstallationTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsInstallationTeam)
    access_approvals_field = models.ManyToManyField(AccessApprovalInstallation)
    rf_and_link_installation_images = models.OneToOneField(RFAndLinkImage, on_delete=models.DO_NOTHING)
    electrical_installation_images = models.OneToOneField(ElectricalImage, on_delete=models.DO_NOTHING)
    kplc_solar_installation_images = models.OneToOneField(KPLCSolarImage, on_delete=models.DO_NOTHING)
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
