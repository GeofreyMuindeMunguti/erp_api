from django.db import models
from erp_core.models import *
from erp_construction.models import *
from users.models import *
from erp_core.fileshandler.filemixin import UploadToProjectDir  # create Folders(Project name) with images & files per project in /media/..



class FTTSProject(Project):
    project_name = models.ForeignKey(Site, on_delete=models.DO_NOTHING, blank=True)#, null=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.project_name

# from django.db import models
# from erp_construction.models import *
# from django.contrib.auth.models import User
# from users.models import *
# from django.contrib.postgres.fields import ArrayField
# from datetime import datetime, timezone, timedelta
#
# # Create your models here.\
#
# class FttsCommercialTeam(models.Model):
#     # site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
#     ftts_quote = models.FileField(upload_to='files/ftts/CommercialTeam/quote/%Y/%m/%d/', blank=True, null=True)
#     ftts_po_requisition = models.FileField(upload_to='files/ftts/CommercialTeam/requisition/%Y/%m/%d/', blank=True, null=True)
#     ftts_wayleave_application = models.FileField(upload_to='files/ftts/CommercialTeam/wayleaveapplication/%Y/%m/%d/', blank=True, null=True)
#     ftts_project_plan = models.FileField(upload_to='files/ftts/CommercialTeam/projectplan/%Y/%m/%d/', blank=True, null=True)
#     ftts_initial_invoice = models.FileField(upload_to='files/ftts/CommercialTeam/initialinvoice/%Y/%m/%d/', blank=True, null=True)
#     ftts_po_client = models.FileField(upload_to='files/ftts/CommercialTeam/poclient/%Y/%m/%d/', blank=True, null=True)
#     is_approved = models.BooleanField(default=False)
#     created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return str(self.site_name)
#
# class FttsProcurementTeam(models.Model):
#     # site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
#     ftts_material_requisition = models.FileField(upload_to='files/ftts/CommercialTeam/materialrequisition/%Y/%m/%d/', blank=True, null=True)
#     ftts_material_receipt_order = models.FileField(upload_to='files/ftts/CommercialTeam/receiptorder/%Y/%m/%d/', blank=True, null=True)
#     ftts_pr = models.FileField(upload_to='files/ftts/CommercialTeam/pr/%Y/%m/%d/', blank=True, null=True)
#     ftts_po_quote_service = models.FileField(upload_to='files/ftts/CommercialTeam/quoteservice/%Y/%m/%d/', blank=True, null=True)
#     ftts_po_subcontractors = models.FileField(upload_to='files/ftts/CommercialTeam/posubcontractors/%Y/%m/%d/', blank=True, null=True)
#     is_approved = models.BooleanField(default=False)
#     created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return str(self.site_name)
#
# ######################################################## FIBER CIVIL TEAM ########################################################################################################################################################################################
#
# class SitePoleInstallation(models.Model):
#     # site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField(blank=True, null=True)
#     site_pole_installation_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
#     site_pole_installation_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
#     site_pole_installation_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
#     site_pole_installation_comment = models.CharField(max_length=100, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return str(self.site_name)
#
# class SiteTrenching(models.Model):
#     # site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField(blank=True, null=True)
#     site_trenching_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
#     site_trenching_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
#     site_trenching_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
#     site_trenching_comment = models.CharField(max_length=100, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return str(self.site_name)
#
# class SiteBackfilling(models.Model):
#     # site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField(blank=True, null=True)
#     site_backfilling_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/backfilling/%Y/%m/%d/')
#     site_backfilling_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/backfilling/%Y/%m/%d/')
#     site_backfilling_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/backfilling/%Y/%m/%d/')
#     site_backfilling_comment = models.CharField(max_length=100, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return str(self.site_name)
#
# class SiteCableInstallation(models.Model):
#     # site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField(blank=True, null=True)
#     site_cable_installation_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
#     site_cable_installation_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
#     site_cable_installation_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
#     site_cable_installation_comment = models.CharField(max_length=100, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return str(self.site_name)
#
#
# class FttsCivilTeam(models.Model):
#     # site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
#     ftts_pole_installation = models.OneToOneField(SitePoleInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
#     ftts_trenching = models.OneToOneField(SiteTrenching, on_delete=models.DO_NOTHING, blank=True, null=True)
#     ftts_backfiling = models.OneToOneField(SiteBackfilling, on_delete=models.DO_NOTHING, blank=True, null=True)
#     ftts_cable_installation = models.OneToOneField(SiteCableInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
#     is_approved = models.BooleanField(default=False)
#     created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return str(self.site_name)
#
# ######################################################## END ################################################################################################################################################################################################
