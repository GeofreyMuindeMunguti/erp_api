from django.db import models
from erp_core.base import *
from erp_construction.models import *
from users.models import *
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone, timedelta
from django.contrib.auth.models import User
from erp_core.fileshandler.filemixin import UploadToProjectDir # create Folders(Project name) with images & files per project in /media/..


class FTTHProject(Project):
    initial_kmz = models.FileField(upload_to='FTTH/files/InitialKMZ/%Y/%m/%d/', blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_acknowledged = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.project_name)


##########################################SURVEY DETAILS################################################################################################################################################################33


class InterceptionPoint(models.Model):
    interception_point_name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    county = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return interception_point_name


class ftthSurveyPhotos(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    survey_image_1 = models.ImageField(upload_to='images/ftth/survey/%Y/%m/%d/')
    survey_image_2 = models.ImageField(upload_to='images/ftth/survey/%Y/%m/%d/', blank=True, null=True)
    survey_image_3 = models.ImageField(upload_to='images/ftth/survey/%Y/%m/%d/', blank=True, null=True)
    survey_images_comment = models.CharField(max_length=200)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

    def ftth_survey_id(self):
        try:
            survey = ftthSurvey.objects.get(site_name=self.site_name)
            survey_id = survey.id
            return survey_id
        except Exception as e:
            return


class ftthSurvey(models.Model):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    ftth_interception_point = models.ForeignKey(InterceptionPoint, on_delete=models.DO_NOTHING, blank=True, null=True)
    site_latitude = models.FloatField()
    site_longitude = models.FloatField()
    distance_from_ip = models.FloatField(blank=True, null=True)
    survey_photos = models.ManyToManyField(ftthSurveyPhotos)
    high_level_design = models.FileField(upload_to='files/ftth/survey/highleveldesigns/%Y/%m/%d/', blank=True, null=True)
    county = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

##############################################END OF FTTH SURVEY#############################################33


class FtthCommercialTeam(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_boq = models.FileField(upload_to='files/ftth/CommercialTeam/boq/%Y/%m/%d/', blank=True, null=True)
    ftth_quote = models.FileField(upload_to='files/ftth/CommercialTeam/quote/%Y/%m/%d/', blank=True, null=True)
    ftth_wayleave_application = models.FileField(upload_to='files/ftth/CommercialTeam/wayleaveapplication/%Y/%m/%d/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthProcurementTeam(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_bom = models.FileField(upload_to='files/ftth/CommercialTeam/bom/%Y/%m/%d/', blank=True, null=True)
    ftth_initial_invoice = models.FileField(upload_to='files/ftth/CommercialTeam/initialinvoice/%Y/%m/%d/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

######################################################## FTTH CIVIL TEAM ########################################################################################################################################################################################

class FtthPoleInstallation(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_pole_installation_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    ftth_pole_installation_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    ftth_pole_installation_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    ftth_pole_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthTrenching(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_trenching_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')
    ftth_trenching_image_2 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')
    ftth_trenching_image_3 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')
    ftth_trenching_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthBackfilling(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_backfilling_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')
    ftth_backfilling_image_2 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')
    ftth_backfilling_image_3 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')
    ftth_backfilling_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthCableInstallation(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_cable_installation_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    ftth_cable_installation_image_2 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    ftth_cable_installation_image_3 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    ftth_cable_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)


class FtthCivilTeam(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_pole_installation = models.OneToOneField(FtthPoleInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftth_trenching = models.OneToOneField(FtthTrenching, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftth_backfiling = models.OneToOneField(FtthBackfilling, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftth_cable_installation = models.OneToOneField(FtthCableInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.site_name)

######################################################## END ################################################################################################################################################################################################

######################################################## FTTH INSTALLATION TEAM ########################################################################################################################################################################################

class FtthSplicingEnclosure(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_splicing_encore_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingencore/%Y/%m/%d/')
    ftth_splicing_encore_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingencore/%Y/%m/%d/')
    ftth_splicing_encore_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingencore/%Y/%m/%d/')
    ftth_splicing_encore_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthSplicingFAT(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_splicing_fat_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')
    ftth_splicing_fat_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')
    ftth_splicing_fat_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')
    ftth_splicing_fat_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthSplicingFDT(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_splicing_fdt_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')
    ftth_splicing_fdt_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')
    ftth_splicing_fdt_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')
    ftth_splicing_fdt_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthSplicing(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_splicing_encore = models.OneToOneField(FtthSplicingEnclosure, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftth_splicing_fat = models.OneToOneField(FtthSplicingFAT, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftth_splicing_fdt = models.OneToOneField(FtthSplicingFDT, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthCoreProvision(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_core_provision_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')
    ftth_core_provision_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')
    ftth_core_provision_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')
    ftth_core_provision_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthPowerLevels(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_power_level_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')
    ftth_power_level_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')
    ftth_power_level_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')
    ftth_power_level_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthOTDRTraces(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    ftth_otdr_traces_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')
    ftth_otdr_traces_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')
    ftth_otdr_traces_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')
    ftth_otdr_traces_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthAsBuilt(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_asbuit_received = models.BooleanField(default=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthSignalTesting(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_splicing_encore = models.OneToOneField(FtthCoreProvision, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftth_splicing_fat = models.OneToOneField(FtthPowerLevels, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftth_splicing_fdt = models.OneToOneField(FtthOTDRTraces, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FtthInstallationTeam(TimeStampModel):
    site_name = models.OneToOneField(Site, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True)
    ftth_splicing = models.OneToOneField(FtthSplicing, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftth_signal_testing = models.OneToOneField(FtthSignalTesting, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)
######################################################## END ################################################################################################################################################################################################
