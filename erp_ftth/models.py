from django.db import models
from erp_core.base import *
from erp_core.base import Project as CreateProject
from erp_construction.models import *
from users.models import *
from erp_core.models import *
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone, timedelta
from django.contrib.auth.models import User
from erp_core.fileshandler.filemixin import UploadToProjectDir # create Folders(Project name) with images & files per project in /media/..
from erp_ftts.models import *

class FTTHProject(CreateProject):
    initial_kmz = models.FileField(upload_to='files/ftth/InitialKMZ/%Y/%m/%d/', blank=True, null=True)
    signed_operation_acceptance = models.BooleanField(default=False, blank=True, null=True)
    ftth_final_acceptance_cert = models.FileField(upload_to='files/ftth/SafaricomTeamftth/finalcert/%Y/%m/%d/', blank=True, null=True)
    ftth_final_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_acknowledged = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.project_name)

"""FIBER FTTH TRACKING"""

####################################### FIBER KPI ###############################################################################################################################
class FtthKpi(TimeStampModel):
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.kpi)

######################################## END #######################################################################################################################################

####################################### TASKS ###############################################################################################################################
class FtthTask(TimeStampModel):
    category_name = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    task_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.task_name)

######################################## END #######################################################################################################################################

####################################### SUBTASKS ###############################################################################################################################
class FtthSubTask(TimeStampModel):
    task_name = models.ForeignKey(FtthTask, on_delete=models.DO_NOTHING)
    subtask_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subtask_name)

######################################## END #######################################################################################################################################
"""END"""

##########################################SURVEY DETAILS################################################################################################################################################################33

class FtthInterceptionPoint(TimeStampModel):
    interception_point_name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    county = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.interception_point_name)

class ftthSurveyPhotos(TimeStampModel):
    project_name = models.ForeignKey(FTTHProject, on_delete=models.CASCADE, blank=True)
    survey_image_1 = models.ImageField(upload_to='images/ftth/survey/%Y/%m/%d/')
    survey_image_2 = models.ImageField(upload_to='images/ftth/survey/%Y/%m/%d/', blank=True, null=True)
    survey_image_3 = models.ImageField(upload_to='images/ftth/survey/%Y/%m/%d/', blank=True, null=True)
    survey_images_comment = models.CharField(max_length=200, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def ftth_survey_id(self):
        try:
            survey = ftthSurvey.objects.get(site_name=self.site_name)
            survey_id = survey.id
            return survey_id
        except Exception as e:
            return


class ftthSurvey(TimeStampModel,TimeTrackModel):
    project_name = models.ForeignKey(FTTHProject, on_delete=models.CASCADE, blank=True)
    ftth_interception_point = models.ForeignKey(FtthInterceptionPoint, on_delete=models.CASCADE, blank=True, null=True)
    site_latitude = models.FloatField()
    site_longitude = models.FloatField()
    distance_from_ip = models.FloatField(blank=True, null=True) #total
    no_of_fdts = models.IntegerField(blank=True, null=True)
    survey_photos = models.ManyToManyField(ftthSurveyPhotos)
    high_level_design = models.FileField(upload_to='files/ftth/survey/highleveldesigns/%Y/%m/%d/', blank=True, null=True)
    county = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    ftth_survey_comment = models.CharField(max_length=200, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def raise_flag(self):
        try:
            kpi_data = FtthTask.objects.get(task_name='FTTH Survey Task')
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

##############################################END OF FTTH SURVEY#############################################33
class FtthCommercialTeam(TimeStampModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE, blank=True)
    ftth_po = models.FileField(upload_to='files/ftth/CommercialTeam/po/%Y/%m/%d/', blank=True, null=True)
    ftth_po_no = models.IntegerField(blank=True, null=True)
    ftth_po_amount = models.IntegerField(blank=True, null=True)
    ftth_boq = models.FileField(upload_to='files/ftth/CommercialTeam/boq/%Y/%m/%d/', blank=True, null=True)
    ftth_quote = models.FileField(upload_to='files/ftth/CommercialTeam/quote/%Y/%m/%d/', blank=True, null=True)
    ftth_wayleave_application = models.FileField(upload_to='files/ftth/CommercialTeam/wayleaveapplication/%Y/%m/%d/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

class FtthPoToSupplier(TimeStampModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE, blank=True)
    ftth_duct = models.FileField(upload_to='files/ftth/ProcurementTeam/poduct/%Y/%m/%d/', blank=True, null=True)
    ftth_cable = models.FileField(upload_to='files/ftth/ProcurementTeam/pocable/%Y/%m/%d/', blank=True, null=True)
    ftth_manholes = models.FileField(upload_to='files/ftth/ProcurementTeam/pomanholes/%Y/%m/%d/', blank=True, null=True)
    ftth_cabinets = models.FileField(upload_to='files/ftth/ProcurementTeam/pocabinets/%Y/%m/%d/', blank=True, null=True)
    ftth_poles = models.FileField(upload_to='files/ftth/ProcurementTeam/popoles/%Y/%m/%d/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)


class FtthProcurementTeam(TimeStampModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE, blank=True)
    ftth_bom = models.FileField(upload_to='files/ftth/ProcurementTeam/bom/%Y/%m/%d/', blank=True, null=True)
    po_to_supplier = models.OneToOneField(FtthPoToSupplier, on_delete=models.CASCADE, blank=True)
    ftth_initial_invoice = models.FileField(upload_to='files/ftth/ProcurementTeam/initialinvoice/%Y/%m/%d/', blank=True, null=True)
    # ftth_budget = models.FileField(upload_to='files/ftth/ProcurementTeam/budget/%Y/%m/%d/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

class FtthCertificates(TimeStampModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE)
    ftth_snag_document = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/SafaricomTeamftth/snag/'), blank=True, null=True)
    ftth_snag_document_comment = models.CharField(max_length=100, blank=True, null=True)
    ftth_crq_ticketno = models.IntegerField(blank=True, null=True)
    ftth_crq_document = models.FileField(upload_to='files/SafaricomTeamftth/crq/%Y/%m/%d/', blank=True, null=True)
    ftth_crq_comment = models.CharField(max_length=100, blank=True, null=True)
    ftth_final_acceptance_cert = models.FileField(upload_to=UploadToProjectDir(file_path ,'files/SafaricomTeamftth/finalcert/'), blank=True, null=True)
    ftth_final_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    ftth_operational_acceptance_cert = models.FileField(upload_to=UploadToProjectDir(file_path ,'files/SafaricomTeamftth/opsacceptance/'), blank=True, null=True)
    ftth_operational_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    ftth_homepass_acceptance_cert = models.FileField(upload_to=UploadToProjectDir(file_path ,'files/SafaricomTeamftth/opsacceptance/'), blank=True, null=True)
    ftth_homepass_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    ftth_conditional_acceptance_cert = models.FileField(upload_to=UploadToProjectDirSubTask(file_path ,'files/SafaricomTeamftth/conditionalcert/'), blank=True, null=True)
    ftth_conditional_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

######################################################## FTTH CIVIL TEAM ########################################################################################################################################################################################
class FtthPoleInstallationImage(TimeStampModel):
    day_image = models.ForeignKey('DailyFtthPoleInstallation', on_delete=models.CASCADE ,related_name='poleinstallationimage')
    poleinstallation_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    poleinstallation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day_image)

class DailyFtthPoleInstallation(TimeStampModel):
    sub_task = models.ForeignKey('FtthPoleInstallation', on_delete=models.CASCADE ,related_name='poleinstallationdays')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to='files/ftth/Casuals/poleinstallation/%Y/%m/%d/',blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    poleinstallation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sub_task)

    def image_list(self):
        try:
            return [FtthPoleInstallationImage.objects.get(poleinstallation_image_1 = _dimage.poleinstallation_image_1).id for _dimage in FtthPoleInstallationImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class FtthPoleInstallation(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE,related_name='ftthpoleinstallations', blank=True,null =True)
    ftth_pole_installation_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    ftth_pole_installation_image_2 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    ftth_pole_installation_image_3 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/poleinstallation/%Y/%m/%d/')
    ftth_pole_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def days_list(self):
        try:
            return [DailyFtthPoleInstallation.objects.get(work_day= _pday.work_day).id for _pday in DailyFtthPoleInstallation.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

    def ftth_task_id(self):
        try:
            task = FtthCivilTeam.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthSubTask.objects.get(subtask_name='Upload Pole Installation Images')
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
class FtthTrenchingImage(TimeStampModel):
    day_image = models.ForeignKey('DailyFtthTrenching', on_delete=models.CASCADE ,related_name='ftthtrenchingimages')
    trenching_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')
    trenching_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day_image)

class DailyFtthTrenching(TimeStampModel):
    sub_task = models.ForeignKey('FtthTrenching', on_delete=models.CASCADE ,related_name='ftthtrenchingdays')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to='files/ftth/Casuals/trenching/%Y/%m/%d/',blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    trenching_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sub_task)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def image_list(self):
        try:
            return [FtthTrenchingImage.objects.get(trenching_image_1 = _dimage.trenching_image_1).id for _dimage in FtthTrenchingImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class FtthTrenching(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE,related_name= 'ftthtrenchings', blank=True,null =True)
    ftth_trenching_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')
    ftth_trenching_image_2 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')
    ftth_trenching_image_3 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/trenching/%Y/%m/%d/')
    ftth_trenching_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def days_list(self):
        try:
            return [DailyFtthTrenching.objects.get(work_day= _pday.work_day).id for _pday in DailyFtthTrenching.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

    def ftth_task_id(self):
        try:
            task = FtthCivilTeam.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthSubTask.objects.get(subtask_name='Upload Site Trenching Images')
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
class FtthBackfillingImage(TimeStampModel):
    day_image = models.ForeignKey('DailyFtthBackfilling', on_delete=models.CASCADE ,related_name='ftthbackfillingimages')
    backfilling_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')
    backfilling_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day_image)

class DailyFtthBackfilling(TimeStampModel):
    sub_task = models.ForeignKey('FtthBackfilling', on_delete=models.CASCADE ,related_name='ftthbackfillingdays')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to='files/ftth/Casuals/backfilling/%Y/%m/%d/',blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    backfilling_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sub_task)

    def image_list(self):
        try:
            return [FtthBackfillingImage.objects.get(backfilling_image_1 = _dimage.backfilling_image_1).id for _dimage in FtthBackfillingImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class FtthBackfilling(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE,related_query_name='ftthbackfillings', blank=True,null =True)
    ftth_backfilling_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')
    ftth_backfilling_image_2 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')
    ftth_backfilling_image_3 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/backfilling/%Y/%m/%d/')
    ftth_backfilling_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def days_list(self):
        try:
            return [DailyFtthBackfilling.objects.get(work_day= _pday.work_day).id for _pday in DailyFtthBackfilling.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

    def ftth_task_id(self):
        try:
            task = FtthCivilTeam.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthSubTask.objects.get(subtask_name='Upload Backfilling Images')
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
class FtthCableInstallationImage(TimeStampModel):
    day_image = models.ForeignKey('DailyFtthCableInstallation', on_delete=models.CASCADE ,related_name='cableinstallationimage')
    cableinstallation_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    cableinstallation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day_image)

class DailyFtthCableInstallation(TimeStampModel):
    sub_task = models.ForeignKey('FtthCableInstallation', on_delete=models.CASCADE ,related_name='cableinstallation')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to='files/ftth/Casuals/cableinstallation/%Y/%m/%d/',blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    cableinstallation_date = models.DateField(unique =True, blank=True, null=True)
    cableinstallation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sub_task)

    def image_list(self):
        try:
            return [FtthCableInstallationImage.objects.get(cableinstallation_image_1 = _dimage.cableinstallation_image_1).id for _dimage in FtthCableInstallationImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class FtthCableInstallation(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE,related_name = 'ftthcableinstallations', blank=True,null =True)
    ftth_cable_installation_image_1 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    ftth_cable_installation_image_2 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    ftth_cable_installation_image_3 = models.ImageField(upload_to='images/ftth/CivilWorksTeam/cableinstallation/%Y/%m/%d/')
    ftth_cable_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def days_list(self):
        try:
            return [DailyFtthCableInstallation.objects.get(work_day= _pday.work_day).id for _pday in DailyFtthCableInstallation.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

    def ftth_task_id(self):
        try:
            task = FtthCivilTeam.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthSubTask.objects.get(subtask_name='Upload Cable Installation Images')
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

class FtthAccessApprovalCivil(TimeStampModel):
    project_name = models.OneToOneField(FTTHProject,related_name= 'ftthcivilaccessapproval', on_delete=models.CASCADE)
    access_approval = models.FileField(upload_to='files/CivilWorksTeam/ftth/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

"""END"""

class FtthHealthDocumentsCivilTeam(TimeStampModel):
    project_name = models.OneToOneField(FTTHProject,related_name= 'ftthcivilhealthdocuments' , on_delete=models.CASCADE)
    project_safety_comm_plan = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CivilWorksTeam/ftth/projectsafety/'))
    project_safety_comm_plan_comment = models.CharField(max_length=100, blank=True, null=True)
    hazard_analysis_form = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CivilWorksTeam/ftth/hazardanalysis/'))
    hazard_analysis_form_comment = models.CharField(max_length=100, blank=True, null=True)
    attendance_form = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CivilWorksTeam/ftth/attendanceform/'))
    attendance_form_comment = models.CharField(max_length=100, blank=True, null=True)
    OHS_risk_treatment_plan = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CivilWorksTeam/ftth/OHSrtp/'))
    OHS_risk_treatment_plan_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_report = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CivilWorksTeam/ftth/OHSrtp/'))
    incident_report_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(FtthAccessApprovalCivil, on_delete=models.CASCADE, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

class FtthCivilTeam(TimeStampModel):
    project_name = models.ForeignKey(FTTHProject, on_delete=models.CASCADE, blank=True)
    ftth_pole_installation = models.OneToOneField(FtthPoleInstallation, on_delete=models.CASCADE, blank=True, null=True)
    ftth_trenching = models.OneToOneField(FtthTrenching, on_delete=models.CASCADE, blank=True, null=True)
    ftth_backfiling = models.OneToOneField(FtthBackfilling, on_delete=models.CASCADE, blank=True, null=True)
    ftth_cable_installation = models.OneToOneField(FtthCableInstallation, on_delete=models.CASCADE, blank=True, null=True)
    health_documents = models.ManyToManyField(FtthHealthDocumentsCivilTeam, blank=True )
    ftth_civil_team_comment = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def team_task_id(self):
        try:
            team = FtthCivilTeam.objects.get(project_name=self.project_name)
            team_id = team.id
            return team_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthTask.objects.get(task_name='FTTH Civil Tasks')
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

######################################################## END ################################################################################################################################################################################################

######################################################## FTTH INSTALLATION TEAM ########################################################################################################################################################################################
class FtthSplicingEnclosureImage(TimeStampModel):
    day_image = models.ForeignKey('DailyFtthSplicingEnclosure', on_delete=models.CASCADE ,related_name='splicingenclosureimage')
    splicingencore_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingenclosure/%Y/%m/%d/')
    splicingencore_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day_image)

class DailyFtthSplicingEnclosure(TimeStampModel):
    sub_task = models.ForeignKey('FtthSplicingEnclosure', on_delete=models.CASCADE ,related_name='splicingencore')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to='files/ftth/Casuals/splicingencore/%Y/%m/%d/',blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    splicingencore_date = models.DateField(unique =True, blank=True, null=True)
    splicingencore_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sub_task)

    def image_list(self):
        try:
            return [FtthSplicingEnclosureImage.objects.get(splicingencore_image_1 = _dimage.splicingencore_image_1).id for _dimage in FtthSplicingEnclosureImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class FtthSplicingEnclosure(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE,related_name ='ftthsplicingenclosures')
    splicing_encore_distance  = models.FloatField(default=0)
    ftth_splicing_encore_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingenclosure/%Y/%m/%d/')
    ftth_splicing_encore_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingenclosure/%Y/%m/%d/')
    ftth_splicing_encore_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingenclosuresplicingenclosure/%Y/%m/%d/')
    ftth_splicing_encore_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def days_list(self):
        try:
            return [DailyFtthSplicingEnclosure.objects.get(work_day= _pday.work_day).id for _pday in DailyFtthSplicingEnclosure.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

    def ftth_task_id(self):
        try:
            task = FtthSplicing.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthSubTask.objects.get(subtask_name='Upload Enclosure Images')
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

class FtthSplicingFATImage(TimeStampModel):
    day_image = models.ForeignKey('DailyFtthSplicingFAT', on_delete=models.CASCADE ,related_name='splicingFATimage')
    splicingFAT_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')
    splicingFAT_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day_image)

class DailyFtthSplicingFAT(TimeStampModel):
    sub_task = models.ForeignKey('FtthSplicingFAT', on_delete=models.CASCADE ,related_name='splicingFAT')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to='files/ftth/Casuals/splicingFAT/%Y/%m/%d/',blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    splicingFAT_date = models.DateField(unique =True, blank=True, null=True)
    splicingFAT_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sub_task)

    def image_list(self):
        try:
            return [FtthSplicingFATImage.objects.get(splicingFAT_image_1 = _dimage.splicingFAT_image_1).id for _dimage in FtthSplicingFATImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class FtthSplicingFAT(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE,related_name ='ftthsplicingfat')
    ftth_splicing_fat_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')
    ftth_splicing_fat_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')
    ftth_splicing_fat_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFAT/%Y/%m/%d/')
    ftth_splicing_fat_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def days_list(self):
        try:
            return [DailyFtthSplicingFAT.objects.get(work_day= _pday.work_day).id for _pday in DailyFtthSplicingFAT.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

    def ftth_task_id(self):
        try:
            task = FtthSplicing.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthSubTask.objects.get(subtask_name='Upload FAT Images')
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

class FtthSplicingFDTImage(TimeStampModel):
    day_image = models.ForeignKey('DailyFtthSplicingFDT', on_delete=models.CASCADE ,related_name='splicingFDTimage')
    splicingFDT_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')
    splicingFDT_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day_image)

class DailyFtthSplicingFDT(TimeStampModel):
    sub_task = models.ForeignKey('FtthSplicingFDT', on_delete=models.CASCADE ,related_name='splicingFDT')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to='files/ftth/Casuals/splicingFDT/%Y/%m/%d/',blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    splicingFDT_date = models.DateField(unique =True, blank=True, null=True)
    splicingFDT_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sub_task)

    def image_list(self):
        try:
            return [FtthSplicingFDTImage.objects.get(splicingFDT_image_1 = _dimage.splicingFDT_image_1).id for _dimage in FtthSplicingFDTImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class FtthSplicingFDT(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE,related_name='ftthsplicingfdts')
    ftth_splicing_fdt_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')
    ftth_splicing_fdt_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')
    ftth_splicing_fdt_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/splicingFDT/%Y/%m/%d/')
    ftth_splicing_fdt_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def days_list(self):
        try:
            return [DailyFtthSplicingFDT.objects.get(work_day= _pday.work_day).id for _pday in DailyFtthSplicingFDT.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

    def ftth_task_id(self):
        try:
            task = FtthSplicing.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthSubTask.objects.get(subtask_name='Upload FDT Images')
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
class FtthSplicing(TimeStampModel):
    project_name = models.ForeignKey(FTTHProject, on_delete=models.CASCADE, blank=True)
    ftth_splicing_encore = models.OneToOneField(FtthSplicingEnclosure, on_delete=models.CASCADE, blank=True, null=True)
    ftth_splicing_fat = models.OneToOneField(FtthSplicingFAT, on_delete=models.CASCADE, blank=True, null=True)
    ftth_splicing_fdt = models.OneToOneField(FtthSplicingFDT, on_delete=models.CASCADE, blank=True, null=True)
    ftth_splicing_comment = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def team_task_id(self):
        try:
            team = FtthSplicing.objects.get(project_name=self.project_name)
            team_id = team.id
            return team_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthTask.objects.get(task_name='Splicing Tasks')
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

"""END SPLICING"""

class FtthCoreProvisionImage(TimeStampModel):
    day_image = models.ForeignKey('DailyFtthCoreProvision', on_delete=models.CASCADE ,related_name='coreprovisionimage')
    coreprovision_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')
    coreprovision_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day_image)

class DailyFtthCoreProvision(TimeStampModel):
    sub_task = models.ForeignKey('FtthCoreProvision', on_delete=models.CASCADE ,related_name='coreprovision')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to='files/ftth/Casuals/coreprovision/%Y/%m/%d/',blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    coreprovision_date = models.DateField(unique =True, blank=True, null=True)
    coreprovision_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sub_task)

    def image_list(self):
        try:
            return [FtthCoreProvisionImage.objects.get(coreprovision_image_1 = _dimage.coreprovision_image_1).id for _dimage in FtthCoreProvisionImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class FtthCoreProvision(TimeStampModel,TimeTrackModel):
    project_name = models.ForeignKey(FTTHProject, on_delete=models.CASCADE, blank=True)
    ftth_core_provision_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')
    ftth_core_provision_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')
    ftth_core_provision_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/coreprovision/%Y/%m/%d/')
    ftth_core_provision_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def days_list(self):
        try:
            return [DailyFtthCoreProvision.objects.get(work_day= _pday.work_day).id for _pday in DailyFtthCoreProvision.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

    def ftth_task_id(self):
        try:
            task = FtthSignalTesting.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthSubTask.objects.get(subtask_name='Upload Core Provision Images')
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

class FtthPowerLevelsImage(TimeStampModel):
    day_image = models.ForeignKey('DailyFtthPowerLevels', on_delete=models.CASCADE ,related_name='powerlevelsimage')
    powerlevels_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')
    powerlevels_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day_image)

class DailyFtthPowerLevels(TimeStampModel):
    sub_task = models.ForeignKey('FtthPowerLevels', on_delete=models.CASCADE ,related_name='ftthpowerlevelsdays')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to='files/ftth/Casuals/powerlevels/%Y/%m/%d/',blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    powerlevels_date = models.DateField(unique =True, blank=True, null=True)
    powerlevels_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sub_task)

    def image_list(self):
        try:
            return [FtthPowerLevelsImage.objects.get(powerlevels_image_1 = _dimage.powerlevels_image_1).id for _dimage in FtthPowerLevelsImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class FtthPowerLevels(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE, related_name= 'ftthpowerlevels')
    ftth_power_level_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')
    ftth_power_level_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')
    ftth_power_level_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/powerlevels/%Y/%m/%d/')
    ftth_power_level_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def days_list(self):
        try:
            return [DailyFtthPowerLevels.objects.get(work_day= _pday.work_day).id for _pday in DailyFtthPowerLevels.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

    def ftth_task_id(self):
        try:
            task = FtthSignalTesting.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthSubTask.objects.get(subtask_name='Upload Power Levels Images')
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

class FtthOTDRTracesImage(TimeStampModel):
    day_image = models.ForeignKey('DailyFtthOTDRTraces', on_delete=models.CASCADE ,related_name='OTDRTracesimage')
    OTDRTraces_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')
    OTDRTraces_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day_image)

class DailyFtthOTDRTraces(TimeStampModel):
    sub_task = models.ForeignKey('FtthOTDRTraces', on_delete=models.CASCADE ,related_name='OTDRTraces')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to='files/ftth/Casuals/OTDRTraces/%Y/%m/%d/',blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    OTDRTraces_date = models.DateField(unique =True, blank=True, null=True)
    OTDRTraces_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.sub_task)

    def image_list(self):
        try:
            return [FtthOTDRTracesImage.objects.get(OTDRTraces_image_1 = _dimage.OTDRTraces_image_1).id for _dimage in FtthOTDRTracesImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class FtthOTDRTraces(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.CASCADE,related_name = 'otdrtrace')
    ftth_otdr_traces_image_1 = models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')
    ftth_otdr_traces_image_2 = models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')
    ftth_otdr_traces_image_3 = models.ImageField(upload_to='images/ftth/InstallationTeam/OTDRTraces/%Y/%m/%d/')
    ftth_otdr_traces_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def days_list(self):
        try:
            return [DailyFtthOTDRTraces.objects.get(work_day= _pday.work_day).id for _pday in DailyFtthOTDRTraces.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

    def ftth_task_id(self):
        try:
            task = FtthSignalTesting.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthSubTask.objects.get(subtask_name='Upload OTDR Traces Images')
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

class FtthSignalTesting(TimeStampModel):
    project_name = models.ForeignKey(FTTHProject, on_delete=models.CASCADE, blank=True)
    ftth_core_provision = models.OneToOneField(FtthCoreProvision, on_delete=models.CASCADE, blank=True, null=True)
    ftth_power_levels = models.OneToOneField(FtthPowerLevels, on_delete=models.CASCADE, blank=True, null=True)
    ftth_otdr_traces = models.OneToOneField(FtthOTDRTraces, on_delete=models.CASCADE, blank=True, null=True)
    ftth_signal_testing_comment = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def team_task_id(self):
        try:
            team = FtthSignalTesting.objects.get(project_name=self.project_name)
            team_id = team.id
            return team_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthTask.objects.get(task_name='Signal Testing Task')
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

"""END SIGNAL TESTING"""
"""aCCESS APPROVALS"""

class FtthAccessApprovalInstallation(TimeStampModel):
    project_name = models.OneToOneField(FTTHProject,related_name= 'ftthaccessapprovalinstallation', on_delete=models.CASCADE)
    access_approval = models.FileField(upload_to='files/InstallationTeamFtth/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

"""END"""

class FtthHealthDocsInstallationTeam(TimeStampModel):
    project_name = models.OneToOneField(FTTHProject,related_name= 'ftthinstallationhealthdocuments' , on_delete=models.CASCADE)
    project_safety_comm_plan = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/InstallationTeamFtth/projectsafety/'))
    project_safety_comm_plan_comment = models.CharField(max_length=100, blank=True, null=True)
    hazard_analysis_form = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/InstallationTeamFtth/hazardanalysis/'))
    hazard_analysis_form_comment = models.CharField(max_length=100, blank=True, null=True)
    attendance_form = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/InstallationTeamFtth/attendanceform/'))
    attendance_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_report = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/InstallationTeamFtth/ftth/OHSrtp/'))
    incident_report_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(FtthAccessApprovalInstallation, on_delete=models.CASCADE, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

class FtthIssues(TimeStampModel):
    project_name = models.ForeignKey(FTTHProject, on_delete=models.CASCADE )
    ftth_issue = models.CharField(max_length=200)
    ftth_issue_image = models.ImageField(upload_to='images/InstallationTeamFtth/issues/%Y/%m/%d/', blank=True, null=True)
    ftth_issue_sorted_image = models.ImageField(upload_to='images/InstallationTeamFtth/issues/%Y/%m/%d/', blank=True, null=True)
    closed = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ftts_issue)

class FtthInstallationTeam(TimeStampModel):
    project_name = models.ForeignKey(FTTHProject, on_delete=models.CASCADE, blank=True)
    ftth_splicing = models.OneToOneField(FtthSplicing, on_delete=models.CASCADE, blank=True, null=True)
    ftth_signal_testing = models.OneToOneField(FtthSignalTesting, on_delete=models.CASCADE, blank=True, null=True)
    ftth_issues = models.ManyToManyField(FtthIssues, blank=True)
    ftth_asbuit_received = models.BooleanField(default=False)
    ftth_asbuilt_comment = models.CharField(max_length=200, blank=True, null=True)
    ftth_network_activation = models.BooleanField(default=False)
    ftth_network_activation_comment = models.CharField(max_length=200, blank=True, null=True)
    health_documents = models.ManyToManyField(FtthHealthDocsInstallationTeam, blank=True )
    ftth_installation_team_comment = models.CharField(max_length=200, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

    def project_issues(self):
        return [v.project_name for v in self.ftth_issues.all()]

    def team_task_id(self):
        try:
            team = FtthInstallationTeam.objects.get(project_name=self.project_name)
            team_id = team.id
            return team_id
        except Exception as e:
            return

    def raise_flag(self):
        try:
            kpi_data = FtthTask.objects.get(task_name='INstallation Tasks')
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

class FtthTeam(TimeStampModel):
    project_name = models.ForeignKey(FTTHProject, on_delete=models.CASCADE, blank=True)
    ftth_survey = models.OneToOneField(ftthSurvey, on_delete=models.CASCADE, blank=True, null=True)
    ftth_civil_team = models.OneToOneField(FtthCivilTeam, on_delete=models.CASCADE, blank=True, null=True)
    ftth_installation_team = models.OneToOneField(FtthInstallationTeam, on_delete=models.CASCADE, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project_name)

######################################################## END ################################################################################################################################################################################################
