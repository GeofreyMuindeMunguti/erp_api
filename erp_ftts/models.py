from django.db import models
from erp_core.models import Project as CreateProject
from erp_core.base import *
from erp_core.models import *
from erp_construction.models import *
from users.models import *
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone, timedelta
from django.contrib.auth.models import User
from erp_core.fileshandler.filemixin import UploadToProjectDir
file_path = 'FTTSProjects'

# Create your models here.
class FTTSProject(CreateProject,TimeTrackModel):
    ftts_activation = models.BooleanField(default=False)
    ftts_activation_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_final_acceptance_cert = models.FileField(upload_to='FTTS/files/SafaricomTeamftts/finalcert/%Y/%m/%d/', blank=True, null=True)
    ftts_final_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_accumulated_BOM_survey = models.FileField(upload_to='FTTS/files/accumulatedBOM/%Y/%m/%d/', blank=True, null=True)
    ftts_accumulated_BOM_survey_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return str(self.project_name)

    def ftts_sites_count(self):
        try:
            return FttsSite.objects.filter(ftts_project_id =self.id).count()

        except Exception as e:
            return e

    def sites_list(self):
        try:
            return [FttsSite.objects.get(site_name= _psite.site_name).id for _psite in FttsSite.objects.filter(ftts_project_id = self.id).all()]
        except Exception as e:
            return e

class FttsSite(TimeStampModel):
    site_name = models.CharField(max_length=100, unique = True, blank=True, null=True)
    ftts_project = models.ForeignKey(FTTSProject, on_delete=models.DO_NOTHING )
    location = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True, null=True )
    posted_by = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return 'Site: {}, Project:{}'.format(self.site_name,self.ftts_project)

    class Meta:
        unique_together = (['site_name', 'ftts_project',])

##########################################SURVEY DETAILS################################################################################################################################################################33
class ManHole(TimeStampModel):
    manhole_no = models.CharField(max_length=100, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.manhole_no)

class Pole(TimeStampModel):
    pole_no = models.CharField(max_length=100, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.pole_no)


class InterceptionPoint(TimeStampModel):
    # manhole_no = models.ForeignKey(ManHole, on_delete=models.DO_NOTHING, blank=True, null=True)
    # pole_no = models.ForeignKey(Pole, on_delete=models.DO_NOTHING, blank=True, null=True)
    interception_point_name = models.CharField(max_length=50)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    county = models.ForeignKey(Location,related_name = 'interceptionpointftts', on_delete=models.DO_NOTHING, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.interception_point_name)


class fttsSurveyPhotos(TimeStampModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
    survey_image_1 = models.ImageField(upload_to='images/ftts/survey/%Y/%m/%d/')
    survey_image_2 = models.ImageField(upload_to='images/ftts/survey/%Y/%m/%d/', blank=True, null=True)
    survey_image_3 = models.ImageField(upload_to='images/ftts/survey/%Y/%m/%d/', blank=True, null=True)
    survey_images_comment = models.CharField(max_length=200, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        #return str(self.site_name)
        return 'survey for {}'.format(self.site_name)

    def ftts_survey_id(self):
        try:
            survey = fttsSurvey.objects.get(site_name=self.site_name)
            survey_id = survey.id
            return survey_id
        except Exception as e:
            return

class fttsSurvey(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
    ftts_interception_point = models.ForeignKey(InterceptionPoint, on_delete=models.DO_NOTHING, blank=True, null=True)
    site_latitude = models.FloatField(blank=True, null=True)
    site_longitude = models.FloatField(blank=True, null=True)
    distance_from_ip = models.FloatField(blank=True, null=True)
    survey_photos = models.ManyToManyField(fttsSurveyPhotos)
    high_level_design = models.FileField(upload_to='files/ftts/survey/highleveldesigns/%Y/%m/%d/', blank=True, null=True)
    county = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True)
    survey_comment = models.CharField(max_length=200, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

##############################################END OF FTTH SURVEY#############################################33


class FttsCommercialTeam(TimeStampModel):
    site_name = models.OneToOneField(FTTSProject, on_delete=models.DO_NOTHING)
    ftts_quote = models.FileField(upload_to='files/ftts/CommercialTeam/quote/%Y/%m/%d/', blank=True, null=True)
    ftts_po_requisition = models.FileField(upload_to='files/ftts/CommercialTeam/requisition/%Y/%m/%d/', blank=True, null=True)
    ftts_po_requisition_no = models.IntegerField(blank=True, null=True)
    ftts_po_requisition_amount = models.IntegerField(blank=True, null=True)
    ftts_wayleave_application = models.FileField(upload_to='files/ftts/CommercialTeam/wayleaveapplication/%Y/%m/%d/', blank=True, null=True)
    ftts_project_plan = models.FileField(upload_to='files/ftts/CommercialTeam/projectplan/%Y/%m/%d/', blank=True, null=True)
    ftts_initial_invoice = models.FileField(upload_to='files/ftts/CommercialTeam/initialinvoice/%Y/%m/%d/', blank=True, null=True)
    ftts_po_client = models.FileField(upload_to='files/ftts/CommercialTeam/poclient/%Y/%m/%d/', blank=True, null=True)
    ftts_po_client_no = models.IntegerField(blank=True, null=True)
    ftts_po_client_amount = models.IntegerField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FttsProcurementTeam(TimeStampModel):
    site_name = models.OneToOneField(FTTSProject, on_delete=models.DO_NOTHING)
    ftts_material_requisition = models.FileField(upload_to='files/ftts/CommercialTeam/materialrequisition/%Y/%m/%d/', blank=True, null=True)
    ftts_po_quote_serviceno = models.IntegerField(blank=True, null=True)
    ftts_po_quote_serviceamount = models.IntegerField(blank=True, null=True)
    ftts_po_subcontractors = models.FileField(upload_to='files/ftts/CommercialTeam/posubcontractors/%Y/%m/%d/', blank=True, null=True)
    ftts_po_quote_subconamount = models.IntegerField(blank=True, null=True)
    ftts_po_quote_subconno = models.IntegerField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

######################################################## FIBER CIVIL TEAM ########################################################################################################################################################################################
class SiteTrenchingImage(TimeStampModel):
    site_name = models.ForeignKey('DailySiteTrenching', on_delete=models.DO_NOTHING ,related_name='trenchingimage')
    site_trenching_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
    site_trenching_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

class DailySiteTrenching(TimeStampModel):
    site_name = models.ForeignKey('SiteTrenching', on_delete=models.DO_NOTHING ,related_name='dailytrenchings')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to='files/ftts/Casuals/trenching/%Y/%m/%d/',blank=True, null=True)
    trenching_date = models.DateField(unique =True, blank=True, null=True)
    distance_trenched = models.FloatField(blank=True, null=True)
    site_trenching_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class SiteTrenching(TimeStampModel,TimeTrackModel):
    site_name = models.ForeignKey(FttsSite, on_delete=models.DO_NOTHING ,related_name='sitetrenchings')
    site_trenched_distance  = models.FloatField(default=0)
    site_trenching_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
    site_trenching_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
    site_trenching_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/trenching/%Y/%m/%d/')
    site_trenching_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def ftts_task_id(self):
        try:
            task = FttsCivilTeam.objects.get(project_name=self.site_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FiberSubTask.objects.get(task_name='Upload Site Trenching Images')
            kpi = kpi_data.kpi
            projected_end_date = self.start_date + timedelta(days=kpi)
            flag = ""

            if bool(self.end_date) is False:
                today = datetime.now(timezone.utc)

                if today < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

            else:
                if self.end_date < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

        except Exception as e:
            return e
"""END"""

class SiteDuctInstallationImage(TimeStampModel):
    site_name = models.ForeignKey('DailySiteDuctInstallation', on_delete=models.DO_NOTHING ,related_name='ductimage')
    site_duct_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/duct/%Y/%m/%d/')
    site_duct_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

class DailySiteDuctInstallation(TimeStampModel):
    site_name = models.ForeignKey('SiteDuctInstallation', on_delete=models.DO_NOTHING ,related_name='dailyduct')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to='files/ftts/Casuals/duct/%Y/%m/%d/',blank=True, null=True)
    duct_date = models.DateField(unique =True, blank=True, null=True)
    distance_duct = models.FloatField(blank=True, null=True)
    site_duct_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class SiteDuctInstallation(TimeStampModel,TimeTrackModel):
    site_name = models.ForeignKey(FttsSite, on_delete=models.DO_NOTHING ,related_name='siteductinstallation')
    site_duct_distance  = models.FloatField(default=0)
    site_duct_installation_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/duct/%Y/%m/%d/')
    site_duct_installation_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/duct/%Y/%m/%d/')
    site_duct_installation_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/duct/%Y/%m/%d/')
    site_duct_installation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def ftts_task_id(self):
        try:
            task = FttsCivilTeam.objects.get(project_name=self.site_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FiberSubTask.objects.get(task_name='Upload Site Duct Installation Images')
            kpi = kpi_data.kpi
            projected_end_date = self.start_date + timedelta(days=kpi)
            flag = ""

            if bool(self.end_date) is False:
                today = datetime.now(timezone.utc)

                if today < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

            else:
                if self.end_date < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

        except Exception as e:
            return e
"""END"""

class ManHoleInstallationImage(TimeStampModel):
    site_name = models.ForeignKey('DailyManHoleInstallation', on_delete=models.DO_NOTHING ,related_name='manholeimage')
    manhole_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/manhole/%Y/%m/%d/')
    manhole_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

class DailyManHoleInstallation(TimeStampModel):
    site_name = models.ForeignKey('ManHoleInstallation', on_delete=models.DO_NOTHING ,related_name='manhole')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to='files/ftts/Casuals/manhole/%Y/%m/%d/',blank=True, null=True)
    manhole_date = models.DateField(unique =True, blank=True, null=True)
    distance_manhole = models.FloatField(blank=True, null=True)
    manhole_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class ManHoleInstallation(TimeStampModel,TimeTrackModel):
    site_name = models.ForeignKey(FttsSite, on_delete=models.DO_NOTHING ,related_name='manholeinstallations')
    site_manhole_distance  = models.FloatField(default=0)
    manhole_image_1 = models.ImageField(upload_to='images/ftts/InstallationTeam/manhole/%Y/%m/%d/')
    manhole_image_2 = models.ImageField(upload_to='images/ftts/InstallationTeam/manhole/%Y/%m/%d/')
    manhole_image_3 = models.ImageField(upload_to='images/ftts/InstallationTeam/manhole/%Y/%m/%d/')
    manhole_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def ftts_task_id(self):
        try:
            task = FttsCivilTeam.objects.get(project_name=self.site_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FiberSubTask.objects.get(task_name='Upload Site Manhole Installation Images')
            kpi = kpi_data.kpi
            projected_end_date = self.start_date + timedelta(days=kpi)
            flag = ""

            if bool(self.end_date) is False:
                today = datetime.now(timezone.utc)

                if today < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

            else:
                if self.end_date < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

        except Exception as e:
            return e
"""END"""

class SiteCableInstallationImage(TimeStampModel):
    site_name = models.ForeignKey('DailySiteCableInstallation', on_delete=models.DO_NOTHING ,related_name='cableimage')
    cable_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cable/%Y/%m/%d/')
    cable_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

class DailySiteCableInstallation(TimeStampModel):
    site_name = models.ForeignKey('SiteCableInstallation', on_delete=models.DO_NOTHING ,related_name='cable')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to='files/ftts/Casuals/cable/%Y/%m/%d/',blank=True, null=True)
    cable_date = models.DateField(unique =True, blank=True, null=True)
    distance_cable = models.FloatField(blank=True, null=True)
    cable_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class SiteCableInstallation(TimeStampModel,TimeTrackModel):
    site_name = models.ForeignKey(FttsSite, on_delete=models.DO_NOTHING ,related_name= 'sitecableinstallation')
    site_cable_distance  = models.FloatField(default=0)
    site_cable_installation_image_1 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_cable_installation_image_2 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_cable_installation_image_3 = models.ImageField(upload_to='images/ftts/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    site_cable_installation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def ftts_task_id(self):
        try:
            task = FttsCivilTeam.objects.get(project_name=self.site_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FiberSubTask.objects.get(task_name='Upload Site Cable Installation Images')
            kpi = kpi_data.kpi
            projected_end_date = self.start_date + timedelta(days=kpi)
            flag = ""

            if bool(self.end_date) is False:
                today = datetime.now(timezone.utc)

                if today < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

            else:
                if self.end_date < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

        except Exception as e:
            return e
"""aCCESS APPROVALS"""

class FttsAccessApprovalCivil(TimeStampModel):
    site_name = models.OneToOneField(FttsSite,related_name= 'civilaccessapproval', on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to='files/ftts/CivilWorksTeam/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

"""END"""

class FttsHealthDocumentsCivilTeam(TimeStampModel):
    site_name = models.OneToOneField(FttsSite,related_name= 'civilhealthdocuments' , on_delete=models.DO_NOTHING)
    project_safety_comm_plan = models.FileField(upload_to='files/ftts/CivilWorksTeam/projectsafety/%Y/%m/%d/')
    project_safety_comm_plan_comment = models.CharField(max_length=100, blank=True, null=True)
    hazard_analysis_form = models.FileField(upload_to='files/ftts/CivilWorksTeam/hazardanalysis/%Y/%m/%d/')
    hazard_analysis_form_comment = models.CharField(max_length=100, blank=True, null=True)
    attendance_form = models.FileField(upload_to='files/ftts/CivilWorksTeam/attendanceform/%Y/%m/%d/')
    attendance_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(FttsAccessApprovalCivil, on_delete=models.CASCADE, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FttsCivilTeam(TimeStampModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
    ftts_trenching = models.OneToOneField(SiteTrenching, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_duct_installation = models.OneToOneField(SiteDuctInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_manhole_installation = models.OneToOneField(ManHoleInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_cable_installation = models.OneToOneField(SiteCableInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    health_documents = models.ManyToManyField(FttsHealthDocumentsCivilTeam, blank=True )
    ftts_civil_team_comment = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

    def health_documents_civil(self):
        return [v.site_name for v in self.health_documents.all()]

    def access_approvals(self):
        return [v.site_name for v in self.access_approvals_field.all()]


    def raise_flag(self):
        try:
            kpi_data =FiberTask.objects.get(task_name='Civil Team')
            kpi = kpi_data.kpi
            projected_end_date = self.start_date + timedelta(days=kpi)
            flag = ""

            if bool(self.end_date) is False:
                today = datetime.now(timezone.utc)

                if today < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

            else:
                if self.end_date < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

        except Exception as e:
            return e

    def team_task_id(self):
        try:
            team = CivilWorksTeam.objects.get(project_name=self.project_name)
            team_id = team.id
            return team_id
        except Exception as e:
            return

######################################################## END ################################################################################################################################################################################################

######################################################## FIBER INSTALLATION TEAM ########################################################################################################################################################################################
class SiteTerminalInHseImage(TimeStampModel):
    site_name = models.ForeignKey('DailySiteTerminalInHse', on_delete=models.DO_NOTHING ,related_name='terminalinhseimage')
    terminal_image_1 = models.ImageField(upload_to='images/ftts/InstallationTeam/terminalinhse/%Y/%m/%d/')
    terminal_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

class DailySiteTerminalInHse(TimeStampModel):
    site_name = models.ForeignKey('SiteTerminalInHse', on_delete=models.DO_NOTHING ,related_name='terminalinhse')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to='files/ftts/Casuals/terminalinhse/%Y/%m/%d/',blank=True, null=True)
    terminal_date = models.DateField(unique =True, blank=True, null=True)
    distance_terminal = models.FloatField(blank=True, null=True)
    terminal_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class SiteTerminalInHse(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING ,related_name='siteterminalinhse')
    site_terminal_in_hse_distance = models.FloatField(default=0)
    site_terminal_in_hse_image_1 = models.ImageField(upload_to='images/ftts/InstallationTeam/terminalinhse/%Y/%m/%d/')
    site_terminal_in_hse_image_2 = models.ImageField(upload_to='images/ftts/InstallationTeam/terminalinhse/%Y/%m/%d/')
    site_terminal_in_hse_image_3 = models.ImageField(upload_to='images/ftts/InstallationTeam/terminalinhse/%Y/%m/%d/')
    site_terminal_in_hse_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def ftts_task_id(self):
        try:
            task = FttsCivilTeam.objects.get(project_name=self.site_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FiberSubTask.objects.get(task_name='Upload Site Terminal-In-House Images')
            kpi = kpi_data.kpi
            projected_end_date = self.start_date + timedelta(days=kpi)
            flag = ""

            if bool(self.end_date) is False:
                today = datetime.now(timezone.utc)

                if today < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

            else:
                if self.end_date < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

        except Exception as e:
            return e
"""END"""

class SiteInterceptionImage(TimeStampModel):
    site_name = models.ForeignKey('DailySiteInterception', on_delete=models.DO_NOTHING ,related_name='interceptionimage')
    interception_image_1 = models.ImageField(upload_to='images/ftts/InstallationTeam/interception/%Y/%m/%d/')
    interception_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

class DailySiteInterception(TimeStampModel):
    site_name = models.ForeignKey('SiteInterception', on_delete=models.DO_NOTHING ,related_name='interception')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to='files/ftts/Casuals/interception/%Y/%m/%d/',blank=True, null=True)
    interception_date = models.DateField(unique =True, blank=True, null=True)
    distance_interception = models.FloatField(blank=True, null=True)
    interception_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class SiteInterception(TimeStampModel,TimeTrackModel):
    site_name = models.ForeignKey(FttsSite, on_delete=models.DO_NOTHING)
    site_interception_distance = models.FloatField(default=0)
    manhole = models.ForeignKey(ManHole, on_delete=models.DO_NOTHING ,blank=True, null=True)
    site_interception_image_1 = models.ImageField(upload_to='images/ftts/InstallationTeam/interception/%Y/%m/%d/')
    site_interception_image_2 = models.ImageField(upload_to='images/ftts/InstallationTeam/interception/%Y/%m/%d/')
    site_interception_image_3 = models.ImageField(upload_to='images/ftts/InstallationTeam/interception/%Y/%m/%d/')
    site_interception_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def ftts_task_id(self):
        try:
            task = FttsCivilTeam.objects.get(project_name=self.site_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FiberSubTask.objects.get(task_name='Upload Site Interception Images')
            kpi = kpi_data.kpi
            projected_end_date = self.start_date + timedelta(days=kpi)
            flag = ""

            if bool(self.end_date) is False:
                today = datetime.now(timezone.utc)

                if today < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

            else:
                if self.end_date < projected_end_date:
                    flag = "OnTrack"
                    return flag
                else:
                    flag = "OffTrack"
                    return flag

        except Exception as e:
            return e
"""END"""
"""aCCESS APPROVALS"""

class FttsAccessApprovalInstallation(TimeStampModel):
    site_name = models.OneToOneField(FttsSite,related_name= 'accessapprovalcivil', on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to='files/ftts/InstallationTeamFtts/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

"""END"""

class FttsHealthDocsInstallationTeam(TimeStampModel):
    site_name = models.OneToOneField(FttsSite,related_name= 'installationhealthdocuments' , on_delete=models.DO_NOTHING)
    project_safety_comm_plan = models.FileField(upload_to='files/ftts/InstallationTeamFtts/projectsafety/%Y/%m/%d/')
    project_safety_comm_plan_comment = models.CharField(max_length=100, blank=True, null=True)
    hazard_analysis_form = models.FileField(upload_to='files/ftts/InstallationTeamFtts/hazardanalysis/%Y/%m/%d/')
    hazard_analysis_form_comment = models.CharField(max_length=100, blank=True, null=True)
    attendance_form = models.FileField(upload_to='files/ftts/InstallationTeamFtts/attendanceform/%Y/%m/%d/')
    attendance_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(FttsAccessApprovalCivil, on_delete=models.CASCADE, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

class FttsIssues(TimeStampModel):
    site_name = models.ForeignKey(FttsSite, on_delete=models.DO_NOTHING)
    ftts_issue = models.CharField(max_length=100)
    ftts_issue_image = models.ImageField(upload_to='images/InstallationTeamFtts/issues/%Y/%m/%d/', blank=True, null=True)
    ftts_issue_sorted_image = models.ImageField(upload_to='images/InstallationTeamFtts/issues/%Y/%m/%d/', blank=True, null=True)
    closed = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ftts_issue

class FttsInstallationTeam(TimeStampModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to='files/ftts/Casuals/installationteam/%Y/%m/%d/',blank=True, null=True)
    ftts_terminal_in_hse = models.OneToOneField(SiteTerminalInHse, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_interception = models.OneToOneField(SiteInterception, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_integration = models.BooleanField(default=False)
    ftts_integration_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_installation_team_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_asbuit_received = models.BooleanField(default=True)
    ftts_asbuilt_comment = models.CharField(max_length=100, blank=True, null=True)
    snag_document = models.FileField(upload_to='files/SafaricomTeamftts/snag/%Y/%m/%d/', blank=True, null=True)
    snag_document_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_issues = models.ManyToManyField(FttsIssues, blank=True )
    conditional_acceptance_cert = models.FileField(upload_to='files/SafaricomTeamftts/conditionalcert/%Y/%m/%d/', blank=True, null=True)
    conditional_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents = models.ManyToManyField(FttsHealthDocsInstallationTeam, blank=True )
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

    def project_issues(self):
        return [v.project_name for v in self.ftts_issues.all()]

    def health_documents_installation(self):
        return [v.site_name for v in self.health_documents.all()]

    def access_approvals(self):
        return [v.site_name for v in self.access_approvals_field.all()]

class FttsTeam(TimeStampModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING)
    ftts_survey = models.OneToOneField(fttsSurvey, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_civil_team = models.OneToOneField(FttsCivilTeam, on_delete=models.DO_NOTHING, blank=True, null=True)
    ftts_installation_team = models.OneToOneField(FttsInstallationTeam, on_delete=models.DO_NOTHING, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.site_name)

######################################################## END ################################################################################################################################################################################################

####DAILY ACTIVITY

class DailyCivilWorkProduction(TimeStampModel):
    site_name = models.ForeignKey(FttsSite, on_delete=models.DO_NOTHING)
    work_day = models.DateField(blank=True, null=True)
    trenched_distance = models.FloatField( blank=True, null=True)
    backfilled_distance = models.FloatField( blank=True, null=True)
    duct_installed_length = models.FloatField( blank=True, null=True)
    cable_installed_length = models.FloatField( blank=True, null=True)
    pole_installed =models.IntegerField(blank=True, null=True)
    manhole_installed =models.IntegerField(blank=True, null=True)
    site_dailyproduction_comment = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        #return str(self.project_name)
        return 'Production for {}'.format(self.work_day)


    class Meta:
        unique_together = (['site_name', 'work_day',])

    ###DAILY CASUAL REGISTER

# Current Implementation
class CasualDailyRegister(TimeStampModel):
    ''' Class to track Casuals per SITE for EACH FTTS Project per task
    '''
  
    site_name = models.ForeignKey(FttsSite, on_delete=models.DO_NOTHING )
    work_day = models.DateField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)


    WORKS_TYPE = [
        ('T', 'Trenching'),
        ('B', 'Backfilling'),
        ('TB', 'Trenching & Backfiling'),
        ('CI', 'Cable Installation'),
        ('TBI', 'Trenching & Backfiling &Cable Installation'),
        ('O', 'Others'),

    ]
    work_type = models.CharField(
        max_length=2,
        choices= WORKS_TYPE,
        #default=OTHERS,
    )
    others = models.CharField(max_length = 250 ,help_text='If work type is others specify the kind of work here',blank =True,null=True)
    casuals_list_file = models.FileField(upload_to='files/ftts/Casuals/%Y/%m/%d/')#,unique_for_date="work_day",)


    def __str__(self):
        return str(self.work_day)

    class Meta:
        unique_together = (['site_name', 'work_day',])


    #Future implementation
class FTTSCasualDailyRegister(TimeStampModel):
    ''' Class to track Casuals per SITE for EACH FTTS Project
    '''

    site_name = models.ForeignKey(FttsSite, on_delete=models.DO_NOTHING )
    work_day = models.DateField(blank=True, null=True)
    ftts_casual =models.ManyToManyField(Casual,related_name= 'fttscasualregister')
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)


    def __str__(self):
        return str(self.work_day)
        #return 'Casual list for Site : {} of Project: {} Date : {}'.format(self.work_day,self.site_trenching,self.trenching_day)

    class Meta:
        unique_together = (['site_name', 'work_day',])




