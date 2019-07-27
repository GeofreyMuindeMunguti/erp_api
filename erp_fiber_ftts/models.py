from django.db import models
from erp_core.base import *
from erp_construction.models import *
from users.models import *
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone, timedelta
from django.contrib.auth.models import User
from erp_core.fileshandler.filemixin import UploadToProjectDir  # create Folders(Project name) with images & files per project in /media/..


# Create your models here.
class FTTSProject(Project,TimeTrackModel):
    
    site_name = models.ManyToManyField(Site,related_name="fttsprojects", blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True)
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.project_name)

class FttsCommercialTeam(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    ftts_quote = models.FileField(upload_to='files/ftts/CommercialTeam/quote/%Y/%m/%d/', blank=True, null=True)
    ftts_po_requisition = models.FileField(upload_to='files/ftts/CommercialTeam/requisition/%Y/%m/%d/', blank=True, null=True)
    ftts_wayleave_application = models.FileField(upload_to='files/ftts/CommercialTeam/wayleaveapplication/%Y/%m/%d/', blank=True, null=True)
    ftts_project_plan = models.FileField(upload_to='files/ftts/CommercialTeam/projectplan/%Y/%m/%d/', blank=True, null=True)
    ftts_initial_invoice = models.FileField(upload_to='files/ftts/CommercialTeam/initialinvoice/%Y/%m/%d/', blank=True, null=True)
    ftts_po_client = models.FileField(upload_to='files/ftts/CommercialTeam/poclient/%Y/%m/%d/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FttsProcurementTeam(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    ftts_material_requisition = models.FileField(upload_to='files/ftts/CommercialTeam/materialrequisition/%Y/%m/%d/', blank=True, null=True)
    ftts_material_receipt_order = models.FileField(upload_to='files/ftts/CommercialTeam/receiptorder/%Y/%m/%d/', blank=True, null=True)
    ftts_pr = models.FileField(upload_to='files/ftts/CommercialTeam/pr/%Y/%m/%d/', blank=True, null=True)
    ftts_po_quote_service = models.FileField(upload_to='files/ftts/CommercialTeam/quoteservice/%Y/%m/%d/', blank=True, null=True)
    ftts_po_subcontractors = models.FileField(upload_to='files/ftts/CommercialTeam/posubcontractors/%Y/%m/%d/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

######################################################## FIBER CIVIL TEAM ########################################################################################################################################################################################

class SitePoleInstallation(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    site_pole_installation_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    site_pole_installation_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    site_pole_installation_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    site_pole_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

        ######### TRENCHING TIME TRACKING and IMAGES MODELS###############

class ProjectTrenching(TimeStampModel,TimeTrackModel):
    ''' Class to track Trenching timelines per FTTS Project |ALL SITES
    :: Here One can calculate  if the Trenching works for an FTTS Project is on Track 
    
    '''
    project_name = models.OneToOneField(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.project_name)
     


class SiteTrenching(TimeStampModel,TimeTrackModel):
    ''' Class to track Trenching timelines per SITE for EACH FTTS Project 
      :: Here One can calculate  if the Trenching works for  A SITE per Project  is on Track 

    '''
    project_trenching = models.ForeignKey(ProjectTrenching,related_name='sitetrenchings', on_delete=models.DO_NOTHING, blank=True,null =True)# Not BLANK
    trenched_distance = models.FloatField( blank=True, null=True)
    backfilled_distance = models.FloatField( blank=True, null=True)
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    

    def __str__(self):
        #return str(self.project_name)
        return 'Site : {} of Project: {}'.format(self.site_name,self.project_trenching)


class FTTSTrenchingImage(TimeStampModel):
    ''' Create  n*3 number of Images per FTTS Project per SITE per DAY '''
    site_trenching = models.ForeignKey(SiteTrenching,related_name='fttstrenchingimages', on_delete=models.DO_NOTHING, blank=True,null =True)
    trenching_day = models.DateField(blank=True, null=True)
    description =  models.CharField(max_length=100, blank=True, null=True)
    
    site_trenching_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
    site_trenching_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
    site_trenching_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
    site_trenching_comment = models.CharField(max_length=100, blank=True, null=True)
    
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        #return str(self.project_name)
        return 'Images for {}'.format(self.site_trenching)
     
class FTTSCasualDailyRegister(TimeStampModel):
    ''' Class to track Casuals per SITE for EACH FTTS Project 
    '''
    site_trenching = models.OneToOneField(SiteTrenching,related_name='fttscasualregisterprojectsite', on_delete=models.DO_NOTHING,blank =True ,null =True)
    site_name = models.ForeignKey(Site, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_casual =models.ManyToManyField(Casual,related_name= 'fttscasualregister')

    trenching_day = models.DateField(blank=True, null=True)
    
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    

    def __str__(self):
        #return str(self.project_name)
        return 'Casual list for Site : {} of Project: {} Date : {}'.format(self.site_name,self.site_trenching,self.trenching_day)

       ######### BACKFILLING TIME TRACKING and IMAGES MODELS###############


class SiteBackfilling(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    site_backfilling_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/backfilling/%Y/%m/%d/')
    site_backfilling_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/backfilling/%Y/%m/%d/')
    site_backfilling_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/backfilling/%Y/%m/%d/')
    site_backfilling_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class SiteCableInstallation(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    site_cable_installation_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_cable_installation_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_cable_installation_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_cable_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.site_name)


class FttsCivilTeam(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    ftts_pole_installation = models.OneToOneField(SitePoleInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_trenching = models.OneToOneField(SiteTrenching, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_backfiling = models.OneToOneField(SiteBackfilling, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_cable_installation = models.OneToOneField(SiteCableInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

######################################################## END ################################################################################################################################################################################################

######################################################## FIBER INSTALLATION TEAM ########################################################################################################################################################################################

class SiteTerminalInHse(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    site_terminal_in_hse_image_1 = models.ImageField(upload_to='images/ftts/InstallationTeam/terminalinhse/%Y/%m/%d/')
    site_terminal_in_hse_image_2 = models.ImageField(upload_to='images/ftts/InstallationTeam/terminalinhse/%Y/%m/%d/')
    site_terminal_in_hse_image_3 = models.ImageField(upload_to='images/ftts/InstallationTeam/terminalinhse/%Y/%m/%d/')
    site_terminal_in_hse_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class SiteInterception(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    site_inception_image_1 = models.ImageField(upload_to='images/ftts/InstallationTeam/inception/%Y/%m/%d/')
    site_inception_image_2 = models.ImageField(upload_to='images/ftts/InstallationTeam/inception/%Y/%m/%d/')
    site_inception_image_3 = models.ImageField(upload_to='images/ftts/InstallationTeam/inception/%Y/%m/%d/')
    site_inception_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class SiteIntegration(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    site_integration_image_1 = models.ImageField(upload_to='images/ftts/InstallationTeam/integration/%Y/%m/%d/')
    site_integration_image_2 = models.ImageField(upload_to='images/ftts/InstallationTeam/integration/%Y/%m/%d/')
    site_integration_image_3 = models.ImageField(upload_to='images/ftts/InstallationTeam/integration/%Y/%m/%d/')
    site_integration_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class SiteAsBuilt(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    ftts_asbuit_received = models.BooleanField(default=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

class FttsInstallationTeam(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING, blank=True)
    ftts_terminal_in_hse = models.OneToOneField(SiteTerminalInHse, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_inception = models.OneToOneField(SiteInterception, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_integration = models.OneToOneField(SiteIntegration, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

######################################################## END ################################################################################################################################################################################################
