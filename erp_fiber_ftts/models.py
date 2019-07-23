from django.db import models
from erp_core.models import *
from erp_construction.models import *
from users.models import *
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone, timedelta
from django.contrib.auth.models import User
from erp_core.fileshandler.filemixin import UploadToProjectDir  # create Folders(Project name) with images & files per project in /media/..


# Create your models here.
class FTTSProject(Project):
    site_name = models.ManyToManyField(Site, blank=True)#, null=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.project_name

class FttsCommercialTeam(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    ftts_quote = models.FileField(upload_to='files/ftts/CommercialTeam/quote/%Y/%m/%d/', blank=True, null=True)
    ftts_po_requisition = models.FileField(upload_to='files/ftts/CommercialTeam/requisition/%Y/%m/%d/', blank=True, null=True)
    ftts_wayleave_application = models.FileField(upload_to='files/ftts/CommercialTeam/wayleaveapplication/%Y/%m/%d/', blank=True, null=True)
    ftts_project_plan = models.FileField(upload_to='files/ftts/CommercialTeam/projectplan/%Y/%m/%d/', blank=True, null=True)
    ftts_initial_invoice = models.FileField(upload_to='files/ftts/CommercialTeam/initialinvoice/%Y/%m/%d/', blank=True, null=True)
    ftts_po_client = models.FileField(upload_to='files/ftts/CommercialTeam/poclient/%Y/%m/%d/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

class FttsProcurementTeam(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    ftts_material_requisition = models.FileField(upload_to='files/ftts/CommercialTeam/materialrequisition/%Y/%m/%d/', blank=True, null=True)
    ftts_material_receipt_order = models.FileField(upload_to='files/ftts/CommercialTeam/receiptorder/%Y/%m/%d/', blank=True, null=True)
    ftts_pr = models.FileField(upload_to='files/ftts/CommercialTeam/pr/%Y/%m/%d/', blank=True, null=True)
    ftts_po_quote_service = models.FileField(upload_to='files/ftts/CommercialTeam/quoteservice/%Y/%m/%d/', blank=True, null=True)
    ftts_po_subcontractors = models.FileField(upload_to='files/ftts/CommercialTeam/posubcontractors/%Y/%m/%d/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

######################################################## FIBER CIVIL TEAM ########################################################################################################################################################################################

class SitePoleInstallation(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    site_pole_installation_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    site_pole_installation_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    site_pole_installation_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    site_pole_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

class SiteTrenching(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    site_trenching_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
    site_trenching_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
    site_trenching_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
    site_trenching_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

class SiteBackfilling(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    site_backfilling_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/backfilling/%Y/%m/%d/')
    site_backfilling_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/backfilling/%Y/%m/%d/')
    site_backfilling_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/backfilling/%Y/%m/%d/')
    site_backfilling_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

class SiteCableInstallation(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    site_cable_installation_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_cable_installation_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_cable_installation_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_cable_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)


class FttsCivilTeam(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    ftts_pole_installation = models.OneToOneField(SitePoleInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_trenching = models.OneToOneField(SiteTrenching, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_backfiling = models.OneToOneField(SiteBackfilling, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_cable_installation = models.OneToOneField(SiteCableInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

######################################################## END ################################################################################################################################################################################################

######################################################## FIBER INSTALLATION TEAM ########################################################################################################################################################################################

class SiteTerminalInHse(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    site_terminal_in_hse_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_terminal_in_hse_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_terminal_in_hse_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_terminal_in_hse_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

class SiteInterception(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    site_inception_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_inception_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_inception_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_inception_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

class SiteIntegration(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    site_integration_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_integration_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_integration_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_integration_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

class SiteAsBuilt(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    site_as_built_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_as_built_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_as_built_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_as_built_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

class FttsInstallationTeam(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    ftts_terminal_in_hse = models.OneToOneField(SiteTerminalInHse, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_inception = models.OneToOneField(SiteInterception, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_integration = models.OneToOneField(SiteIntegration, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_as_built = models.OneToOneField(SiteAsBuilt, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

######################################################## END ################################################################################################################################################################################################
