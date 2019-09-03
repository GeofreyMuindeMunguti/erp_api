from django.db import models
from erp_core.models import Project as CreateProject
from erp_core.base import *
from erp_core.models import *
from erp_construction.models import *
from users.models import *
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone, timedelta
from django.contrib.auth.models import User
from erp_core.fileshandler.filemixin import *
from erp_ftth.models import *

file_path = 'FTTSProjects'

# Create your models here.
class FTTSProject(CreateProject,TimeTrackModel):
    ftts_activation = models.BooleanField(default=False)
    ftts_activation_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

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
    ftts_project = models.ForeignKey(FTTSProject, on_delete=models.CASCADE )
    location = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True, null=True )
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '{}:{}'.format(self.site_name,self.ftts_project)

    class Meta:
        unique_together = (['site_name', 'ftts_project',])

##########################################SURVEY DETAILS################################################################################################################################################################33
class ManHole(TimeStampModel):
    manhole_no = models.CharField(max_length=100, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.manhole_no)

class Pole(TimeStampModel):
    pole_no = models.CharField(max_length=100, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pole_no)


class InterceptionPoint(TimeStampModel):
    interception_point_name = models.CharField(max_length=50)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    county = models.ForeignKey(Location,related_name = 'interceptionpointftts', on_delete=models.CASCADE, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.interception_point_name)


class fttsSurveyPhotos(TimeStampModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING,related_name ='fttssurveyphotos')
    survey_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/survey/'), blank=True, null=True)
    survey_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/survey/'), blank=True, null=True)
    survey_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/survey/'), blank=True, null=True)
    survey_images_comment = models.CharField(max_length=200, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

    def ftts_survey_id(self):
        try:
            survey = fttsSurvey.objects.get(site_name=self.site_name)
            survey_id = survey.id
            return survey_id
        except Exception as e:
            return

class fttsSurvey(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.CASCADE)
    ftts_interception_point = models.ForeignKey(InterceptionPoint, on_delete=models.CASCADE, blank=True, null=True)
    site_latitude = models.FloatField(blank=True, null=True)
    site_longitude = models.FloatField(blank=True, null=True)
    distance_from_ip = models.FloatField(blank=True, null=True)
    survey_photos = models.ManyToManyField(fttsSurveyPhotos)
    high_level_design = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/survey/highleveldesigns/'), blank=True, null=True)
    county = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    survey_comment = models.CharField(max_length=200, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

##############################################END OF FTTH SURVEY#############################################33

class FttsCommercialTeam(TimeStampModel):
    site_name = models.OneToOneField(FTTSProject, on_delete=models.CASCADE,related_name ='fttscommercialteams')
    ftts_quote = models.FileField(upload_to=UploadToProjectDir(file_path ,'files/CommercialTeam/quote/'), blank=True, null=True)
    ftts_po_requisition = models.FileField(upload_to=UploadToProjectDir(file_path,'files/CommercialTeam/requisition/'), blank=True, null=True)
    ftts_po_requisition_no = models.IntegerField(blank=True, null=True)
    ftts_po_requisition_amount = models.IntegerField(blank=True, null=True)
    ftts_crq_ticketno = models.IntegerField(blank=True, null=True)
    ftts_crq_document = models.FileField(upload_to='files/SafaricomTeamftth/crq/%Y/%m/%d/', blank=True, null=True)
    ftts_crq_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_wayleave_application = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CommercialTeam/wayleaveapplication/'), blank=True, null=True)
    ftts_project_plan = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CommercialTeam/projectplan/'), blank=True, null=True)
    ftts_initial_invoice = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CommercialTeam/initialinvoice/'), blank=True, null=True)
    ftts_po_client = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CommercialTeam/poclient/'), blank=True, null=True)
    ftts_po_client_no = models.IntegerField(blank=True, null=True)
    ftts_po_client_amount = models.IntegerField(blank=True, null=True)
    ftts_accumulated_BOM_survey = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'FTTS/files/accumulatedBOM/'), blank=True, null=True)
    ftts_accumulated_BOM_survey_comment = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

class FttsProcurementTeam(TimeStampModel):
    site_name = models.OneToOneField(FTTSProject, on_delete=models.CASCADE)
    ftts_material_requisition = models.FileField(upload_to=UploadToProjectDir(file_path,'files/CommercialTeam/materialrequisition/'), blank=True, null=True)
    ftts_po_quote_serviceno = models.IntegerField(blank=True, null=True)
    ftts_po_quote_serviceamount = models.IntegerField(blank=True, null=True)
    ftts_po_subcontractors = models.FileField(upload_to=UploadToProjectDir(file_path,'files/CommercialTeam/posubcontractors/'), blank=True, null=True)
    ftts_po_quote_subconamount = models.IntegerField(blank=True, null=True)
    ftts_po_quote_subconno = models.IntegerField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

class FttsCertificates(TimeStampModel):
    site_name = models.OneToOneField(FTTSProject, on_delete=models.CASCADE)
    ftts_snag_document = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/SafaricomTeamftts/snag/'), blank=True, null=True)
    ftts_snag_document_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_crq_ticketno = models.IntegerField(blank=True, null=True)
    ftts_crq_document = models.FileField(upload_to='files/SafaricomTeamftth/crq/%Y/%m/%d/', blank=True, null=True)
    ftts_crq_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_final_acceptance_cert = models.FileField(upload_to=UploadToProjectDir(file_path ,'files/SafaricomTeamftts/finalcert/'), blank=True, null=True)
    ftts_final_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_operational_acceptance_cert = models.FileField(upload_to=UploadToProjectDir(file_path ,'files/SafaricomTeamftts/opsacceptance/'), blank=True, null=True)
    ftts_operational_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_homepass_acceptance_cert = models.FileField(upload_to=UploadToProjectDir(file_path ,'files/SafaricomTeamftts/opsacceptance/'), blank=True, null=True)
    ftts_homepass_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_conditional_acceptance_cert = models.FileField(upload_to=UploadToProjectDirSubTask(file_path ,'files/SafaricomTeamftts/conditionalcert/'), blank=True, null=True)
    ftts_conditional_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

######################################################## FIBER CIVIL TEAM ########################################################################################################################################################################################
class SiteTrenchingImage(TimeStampModel):
    day_image = models.ForeignKey('DailySiteTrenching', on_delete=models.CASCADE ,related_name='sitetrenchingimages')
    site_trenching_image_1 = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/trenching/'),max_length = 250)
    site_trenching_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Image for {}'.format(self.day_image)


class DailySiteTrenching(TimeStampModel):
    sub_task = models.ForeignKey('SiteTrenching', on_delete=models.CASCADE ,related_name='dailysitetrenchings')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path ,'files/Casuals/trenching/'),blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    distance_trenched = models.FloatField(blank=True, null=True)
    site_trenching_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

    def image_list(self):
        try:
            return [SiteTrenchingImage.objects.get(site_trenching_image_1 = _dimage.site_trenching_image_1).id for _dimage in SiteTrenchingImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e


    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class SiteTrenching(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.CASCADE,related_name='sitetrenching')
    site_trenched_distance  = models.FloatField(default=0)
    site_trenching_image_1 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/trenching/'), blank=True, null=True)
    site_trenching_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/trenching/'), blank=True, null=True)
    site_trenching_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/trenching/'), blank=True, null=True)
    site_trenching_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'SiteTrenching  : {}'.format(self.site_name)

    def days_list(self):
        try:
            return [DailySiteTrenching.objects.get(work_day= _pday.work_day).id for _pday in DailySiteTrenching.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

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
    day_image = models.ForeignKey('DailySiteDuctInstallation', on_delete=models.CASCADE ,related_name='ductimages')
    site_duct_image_1 = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/duct/'),max_length = 250)
    site_duct_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Image for {}'.format(self.day_image)


class DailySiteDuctInstallation(TimeStampModel):
    sub_task = models.ForeignKey('SiteDuctInstallation', on_delete=models.CASCADE ,related_name='dailyduct')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path ,'files/Casuals/duct/'),blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    distance_duct = models.FloatField(blank=True, null=True)
    site_duct_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

    def image_list(self):
        try:
            return [SiteDuctInstallationImage.objects.get(site_duct_image_1 = _dimage.site_duct_image_1).id for _dimage in SiteDuctInstallationImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e


    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class SiteDuctInstallation(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.CASCADE ,related_name='siteductinstallation')
    site_duct_distance  = models.FloatField(default=0)
    site_duct_installation_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/duct/'),blank=True,null=True)
    site_duct_installation_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/duct/'),blank=True,null=True)
    site_duct_installation_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/duct/'),blank=True,null=True)
    site_duct_installation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'SiteDuctInstallation  : {}'.format(self.site_name)

    def days_list(self):
        try:
            return [DailySiteDuctInstallation.objects.get(work_day= _pday.work_day).id for _pday in DailySiteDuctInstallation.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

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
    day_image = models.ForeignKey('DailyManHoleInstallation', on_delete=models.CASCADE ,related_name='manholeimages')
    manhole_image_1 = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/manhole/'))
    manhole_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Image for {}'.format(self.day_image)


class DailyManHoleInstallation(TimeStampModel):
    sub_task = models.ForeignKey('ManHoleInstallation', on_delete=models.CASCADE ,related_name='manholeinstalldays')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/manhole/'),blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    manhole_installed = models.IntegerField(blank=True, null=True)
    manhole_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

    def image_list(self):
        try:
            return [ManHoleInstallationImage.objects.get(manhole_image_1 = _dimage.manhole_image_1).id for _dimage in ManHoleInstallationImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e


    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class ManHoleInstallation(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.CASCADE ,related_name='manholeinstallations')
    site_manhole_installed = models.IntegerField(default=0)
    manhole_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/manhole/'),blank =True ,null =True)
    manhole_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/manhole/'),blank =True ,null =True)
    manhole_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/manhole/'),blank =True ,null =True)
    manhole_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'ManHoleInstallation  : {}'.format(self.site_name)

    def days_list(self):
        try:
            return [DailyManHoleInstallation.objects.get(work_day= _pday.work_day).id for _pday in DailyManHoleInstallation.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

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
    day_image = models.ForeignKey('DailySiteCableInstallation', on_delete=models.CASCADE ,related_name='cableimages')
    cable_image_1 = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/cable/'))
    cable_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Image for {}'.format(self.day_image)


class DailySiteCableInstallation(TimeStampModel):
    sub_task = models.ForeignKey('SiteCableInstallation', on_delete=models.CASCADE ,related_name='cableinstalldays')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/cable/'),blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    distance_cable = models.FloatField(blank=True, null=True)
    cable_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

    def image_list(self):
        try:
            return [SiteCableInstallationImage.objects.get(cable_image_1 = _dimage.cable_image_1).id for _dimage in SiteCableInstallationImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e


    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class SiteCableInstallation(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.CASCADE ,related_name= 'sitecableinstallation')
    site_cable_distance  = models.FloatField(default=0)
    site_cable_installation_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/cableinstallation/'),blank =True,null =True)
    site_cable_installation_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/cableinstallation/'),blank =True,null =True)
    site_cable_installation_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/cableinstallation/'),blank =True,null =True)
    site_cable_installation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'SiteCableInstallation  : {}'.format(self.site_name)

    def days_list(self):
        try:
            return [DailySiteCableInstallation.objects.get(work_day= _pday.work_day).id for _pday in DailySiteCableInstallation.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

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
    site_name = models.OneToOneField(FttsSite,related_name= 'civilaccessapproval', on_delete=models.CASCADE)
    access_approval = models.FileField(upload_to='files/CivilWorksTeam/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

"""END"""

class FttsHealthDocumentsCivilTeam(TimeStampModel):
    site_name = models.OneToOneField(FttsSite,related_name= 'civilhealthdocuments' , on_delete=models.CASCADE)
    project_safety_comm_plan = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CivilWorksTeam/projectsafety/'))
    project_safety_comm_plan_comment = models.CharField(max_length=100, blank=True, null=True)
    hazard_analysis_form = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CivilWorksTeam/hazardanalysis/'))
    hazard_analysis_form_comment = models.CharField(max_length=100, blank=True, null=True)
    attendance_form = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/CivilWorksTeam/attendanceform/'))
    attendance_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(FttsAccessApprovalCivil, on_delete=models.CASCADE, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

class FttsCivilTeam(TimeStampModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.CASCADE)
    ftts_trenching = models.OneToOneField(SiteTrenching, on_delete=models.CASCADE, blank=True, null=True)
    ftts_duct_installation = models.OneToOneField(SiteDuctInstallation, on_delete=models.CASCADE, blank=True, null=True)
    ftts_manhole_installation = models.OneToOneField(ManHoleInstallation, on_delete=models.CASCADE, blank=True, null=True)
    ftts_cable_installation = models.OneToOneField(SiteCableInstallation, on_delete=models.CASCADE, blank=True, null=True)
    health_documents = models.ManyToManyField(FttsHealthDocumentsCivilTeam, blank=True )
    ftts_civil_team_comment = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

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
    day_image = models.ForeignKey('DailySiteTerminalInHse', on_delete=models.CASCADE ,related_name='terminalinhseimage')
    terminal_image_1 = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/InstallationTeam/terminalinhse/'))
    terminal_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Image for {}'.format(self.day_image)


class DailySiteTerminalInHse(TimeStampModel):
    sub_task = models.ForeignKey('SiteTerminalInHse', on_delete=models.CASCADE ,related_name='terminalinhsedays')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/terminalinhse/'),blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    terminal_odf_no = models.IntegerField(default= 0)
    terminal_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{} :Date: {}'.format(self.sub_task,self.work_day)


    def image_list(self):
        try:
            return [SiteTerminalInHseImage.objects.get(terminal_image_1 = _dimage.terminal_image_1).id for _dimage in SiteTerminalInHseImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e


    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class SiteTerminalInHse(TimeStampModel,TimeTrackModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.CASCADE ,related_name='siteterminalinhse')
    site_terminal_in_hse_distance = models.FloatField(default=0)
    site_terminal_in_hse_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/terminalinhse/'),blank =True ,null=True)
    site_terminal_in_hse_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/terminalinhse/'),blank =True ,null=True)
    site_terminal_in_hse_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/terminalinhse/'),blank =True ,null=True)
    site_terminal_in_hse_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'SiteTerminalInHse  : {}'.format(self.site_name)

    def days_list(self):
        try:
            return [DailySiteTerminalInHse.objects.get(work_day= _pday.work_day).id for _pday in DailySiteTerminalInHse.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

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
    day_image = models.ForeignKey('DailySiteInterception', on_delete=models.CASCADE ,related_name='interceptionimages')
    interception_image_1 = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/InstallationTeam/interception/'),blank=True ,null =True)
    interception_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Image for {}'.format(self.day_image)


class DailySiteInterception(TimeStampModel):
    sub_task = models.ForeignKey('SiteInterception', on_delete=models.CASCADE ,related_name='interceptiondays')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/interception/'),blank=True, null=True)
    work_day = models.DateField(unique =True, blank=True, null=True)
    distance_interception = models.FloatField(blank=True, null=True)

    interception_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

    def image_list(self):
        try:
            return [SiteInterceptionImage.objects.get(interception_image_1 = _dimage.interception_image_1).id for _dimage in SiteInterceptionImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

class SiteInterception(TimeStampModel,TimeTrackModel):
    site_name = models.ForeignKey(FttsSite, on_delete=models.CASCADE,related_name='siteinterception')
    site_interception_distance = models.FloatField(default=0)
    manhole = models.ForeignKey(ManHole, on_delete=models.CASCADE ,blank=True, null=True)
    site_interception_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/interception/'),blank=True ,null =True)
    site_interception_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/interception/'),blank=True ,null =True)
    site_interception_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/interception/'),blank=True ,null =True)
    site_interception_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

    def days_list(self):
        try:
            return [DailySiteInterception.objects.get(work_day= _pday.work_day).id for _pday in DailySiteInterception.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e

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
    site_name = models.OneToOneField(FttsSite,related_name= 'accessapprovalcivil', on_delete=models.CASCADE)
    access_approval = models.FileField(upload_to='files/InstallationTeamFtts/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

"""END"""

class FttsHealthDocsInstallationTeam(TimeStampModel):
    site_name = models.OneToOneField(FttsSite,related_name= 'installationhealthdocuments' , on_delete=models.CASCADE)
    project_safety_comm_plan = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/InstallationTeamFtts/projectsafety/'))
    project_safety_comm_plan_comment = models.CharField(max_length=100, blank=True, null=True)
    hazard_analysis_form = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/InstallationTeamFtts/hazardanalysis/'))
    hazard_analysis_form_comment = models.CharField(max_length=100, blank=True, null=True)
    attendance_form = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/InstallationTeamFtts/attendanceform/'))
    attendance_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(FttsAccessApprovalCivil, on_delete=models.CASCADE, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

class FttsIssues(TimeStampModel):
    site_name = models.ForeignKey(FttsSite, on_delete=models.CASCADE)
    ftts_issue = models.CharField(max_length=100)
    ftts_issue_image = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeamFtts/issues/'), blank=True, null=True)
    ftts_issue_sorted_image = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeamFtts/issues/'), blank=True, null=True)
    closed = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.ftts_issue

class FttsInstallationTeam(TimeStampModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.CASCADE)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    casuals_list = models.FileField(upload_to=UploadToProjectDirSubTask(file_path,'files/Casuals/installationteam/'),blank=True, null=True)
    ftts_terminal_in_hse = models.OneToOneField(SiteTerminalInHse, on_delete=models.CASCADE, blank=True, null=True)
    ftts_interception = models.OneToOneField(SiteInterception, on_delete=models.CASCADE, blank=True, null=True)
    ftts_integration = models.BooleanField(default=False)
    ftts_integration_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_installation_team_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_asbuit_received = models.BooleanField(default=True)
    ftts_asbuilt_comment = models.CharField(max_length=100, blank=True, null=True)
    ftts_issues = models.ManyToManyField(FttsIssues, blank=True )
    health_documents = models.ManyToManyField(FttsHealthDocsInstallationTeam, blank=True )
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

    def project_issues(self):
        return [v.project_name for v in self.ftts_issues.all()]

    def health_documents_installation(self):
        return [v.site_name for v in self.health_documents.all()]

    def access_approvals(self):
        return [v.site_name for v in self.access_approvals_field.all()]

    def team_task_id(self):
        try:
            team = FttsInstallationTeam.objects.get(project_name=self.site_name)
            team_id = team.id
            return team_id
        except Exception as e:
            return

class FttsTeam(TimeStampModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.CASCADE)
    ftts_survey = models.OneToOneField(fttsSurvey, on_delete=models.CASCADE, blank=True, null=True)
    ftts_civil_team = models.OneToOneField(FttsCivilTeam, on_delete=models.CASCADE, blank=True, null=True)
    ftts_installation_team = models.OneToOneField(FttsInstallationTeam, on_delete=models.CASCADE, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_name)

######################################################## END ################################################################################################################################################################################################

####DAILY ACTIVITY

class DailyCivilWorkProduction(TimeStampModel):
    site_name = models.ForeignKey(FttsSite, on_delete=models.CASCADE)
    work_day = models.DateField(blank=True, null=True)
    trenched_distance = models.FloatField( blank=True, null=True)
    backfilled_distance = models.FloatField( blank=True, null=True)
    duct_installed_length = models.FloatField( blank=True, null=True)
    cable_installed_length = models.FloatField( blank=True, null=True)
    pole_installed =models.IntegerField(blank=True, null=True)
    manhole_installed =models.IntegerField(blank=True, null=True)
    site_dailyproduction_comment = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

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

    site_name = models.ForeignKey(FttsSite, on_delete=models.CASCADE )
    work_day = models.DateField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


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

    site_name = models.ForeignKey(FttsSite, on_delete=models.CASCADE )
    work_day = models.DateField(blank=True, null=True)
    ftts_casual =models.ManyToManyField(Casual,related_name= 'fttscasualregister')
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.work_day)
        #return 'Casual list for Site : {} of Project: {} Date : {}'.format(self.work_day,self.site_trenching,self.trenching_day)

    class Meta:
        unique_together = (['site_name', 'work_day',])
