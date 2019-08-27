from django.db import models
from django.db.models import Sum, F
from django.contrib.auth.models import User
from users.models import *
from erp_core.models import *
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone, timedelta
from erp_core.fileshandler.filemixin import *# UploadToProjectDir ,UploadToProjectDirDate ,UploadToProjectDirSubTask ,UploadToProjectDirImage
file_path = 'BTSProjects'


class ProjectIcon(models.Model):
    icon = models.ImageField(upload_to='images/Project/Icons/%Y/%m/%d/')
    site_owner = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.site_owner


class BtsProject(models.Model):
    bts_project_name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    icon = models.ForeignKey(ProjectIcon, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.bts_project_name

    class Meta:
        verbose_name_plural = 'BTS PROJECTS'



class BtsSite(TimeStampModel):
    ''' Create site and associate with project'''
    project_name = models.ForeignKey(BtsProject, on_delete=models.CASCADE, blank=True, null=True)
    site_name = models.CharField(max_length=100, unique=True, blank=True, null=True)
     # Site details
    site_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    BTS_type = models.CharField(max_length=100, blank=True, null=True)
    site_owner = models.CharField(max_length=100, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True)
     # Site Docs
    geotech_file = models.FileField(upload_to= UploadToProjectDir(file_path,'files/Project/geotech/'), blank=True, null=True)
    access_letter = models.FileField(upload_to=UploadToProjectDir(file_path,'files/Project/accessletters/'), blank=True, null=True)
    approved_drawing = models.FileField(upload_to= UploadToProjectDir(file_path,'files/Project/approveddrawings/'), blank=True, null=True)
    final_acceptance_cert = models.FileField(upload_to=UploadToProjectDir(file_path,'files/SafaricomTeam/finalcert/'), blank=True, null=True)
    final_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)


    def __str__(self):
        #return str(self.site_name)
        return '{}:{}'.format(self.site_name,self.project_name)

    class Meta:
        verbose_name_plural = 'BTS SITES'



    def status(self):
        try:
            if bool(self.final_acceptance_cert) is False:
                project_status = "Open"
            else:
                project_status = "Closed"
            return project_status
        except Exception as e:
            return e

    def turn_around_time(self):
        if bool(self.final_acceptance_cert) is False:
            today = datetime.now(timezone.utc)
            days = date_difference(self.created_at, today)
        else:
            days = date_difference(self.created_at, self.updated_at)
        return days

    def progress(self):
        try:
            category = Category.objects.get(category_name='Commercial Team')
            category_id = category.id
            automatic_total_comtasks = Task.objects.filter(category_name=category_id).count()
            completed_ctasks = 0
            project_id = self.id
            progress_object = CommercialTeam.objects.get(project_name=project_id)
            approved_quote = progress_object.approved_quote_file
            po = progress_object.po_data
            project_costing = progress_object.project_costing_data
            initialinvoice = progress_object.initial_invoice
            if bool(po) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(initialinvoice) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(approved_quote) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            if bool(project_costing) is False:
                completed_ctasks += 0
            else:
                completed_ctasks += 1
            commercial_percentage = percentage_function(completed_ctasks, automatic_total_comtasks)
        except Exception as e:
            commercial_percentage = 0

        #PROGRESS FOR PROCUREMENTEAM
        try:
            category = Category.objects.get(category_name='Procurement Team')
            category_id = category.id
            automatic_total_protasks = Task.objects.filter(category_name=category_id).count()
            completed_ptasks = 0
            project_id = self.id
            progress_object = ProcurementTeam.objects.get(project_name=project_id)
            po_steel = progress_object.po_steel
            po_electrical_materials = progress_object.po_electrical_materials
            po_subcontractors = progress_object.po_subcontractors
            if bool(po_steel) is False:
                completed_ptasks += 0
            else:
                completed_ptasks += 1
            if bool(po_electrical_materials) is False:
                completed_ptasks += 0
            else:
                completed_ptasks += 1
            if bool(po_subcontractors) is False:
                completed_ptasks += 0
            else:
                completed_ptasks += 1
            procurement_percentage = percentage_function(completed_ptasks, automatic_total_protasks)
        except Exception as e:
            procurement_percentage = 0

        #PROGRESS FOR CIVIL TEAM
        try:
            category = Category.objects.get(category_name='Civil Team')
            category_id = category.id
            automatic_total_civtasks = Task.objects.filter(category_name=category_id).count()
            completed_cltasks = 0
            project_id = self.id
            progress_object = CivilWorksTeam.objects.get(project_name=project_id)
            foundation_and_curing_images = progress_object.foundation_and_curing_images
            bts_and_generator_slabs_images = progress_object.bts_and_generator_slabs_images
            site_walling_images_field = progress_object.site_walling_images_field
            tower_field = progress_object.tower_data
            if bool(foundation_and_curing_images) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            if bool(bts_and_generator_slabs_images) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            if bool(site_walling_images_field) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            if bool(tower_field) is False:
                completed_cltasks += 0
            else:
                completed_cltasks += 1
            civil_percentage = percentage_function(completed_cltasks, automatic_total_civtasks)
        except Exception as e:
            civil_percentage = 0

        #PROGRESS FOR INSTALLATION TEAM
        try:
            category = Category.objects.get(category_name='Installation Team')
            category_id = category.id
            automatic_total_instasks = Task.objects.filter(category_name=category_id).count()
            completed_intasks = 0
            project_id = self.id
            progress_object = InstallationTeam.objects.get(project_name=project_id)
            electrical_tasks_data = progress_object.electrical_tasks_data
            telecom_tasks_data = progress_object.telecom_tasks_data
            signoff = progress_object.signoff
            rfi_document = progress_object.rfi_document
            integration_parameter = progress_object.integration_parameter
            conditional_acceptance_cert = progress_object.conditional_acceptance_cert
            if bool(electrical_tasks_data) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(telecom_tasks_data) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(signoff) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(rfi_document) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(integration_parameter) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            if bool(conditional_acceptance_cert) is False:
                completed_intasks += 0
            else:
                completed_intasks += 1
            installation_percentage = percentage_function(completed_intasks, automatic_total_instasks)
        except Exception as e:
            installation_percentage = 0

        project_percentage = ((commercial_percentage + civil_percentage + procurement_percentage + installation_percentage )/4)

        return project_percentage


# TASK [1]: FOUNDATION CREATION TASK ########################################################################################################################################

    # SubTask (1)://///////////Site-Clearing Subtask //////////////////


class SiteClearingImage(TimeStampModel):
    day_image = models.ForeignKey('SiteClearingDate', on_delete=models.CASCADE )

    # DailyPhotos
    setting_site_clearing_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/siteclearing/') ,max_length=250,blank=True, null=True)
    setting_site_clearing_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

    def bts_site_id(self): #NN
        try:
            site_name = str(self.day_image).split(':')[1].strip()

            return BtsSite.objects.get(site_name=site_name).id
            
        except Exception as e:
            return


class SiteClearingDate(TimeStampModel):
    sub_task = models.ForeignKey('SiteClearingSubTask', on_delete=models.CASCADE,related_name='siteclearingdates')
    work_day =  models.DateField(unique = True ,blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/SiteSiteClearing/'),max_length=250,blank=True, null=True)

    def __str__(self):
        #return str(self.project_name)
        return '{}: Date: {}'.format(self.sub_task ,self.work_day)


    def image_list(self):
        try:
            return [SiteClearingImage.objects.get(setting_site_clearing_image = _dimage.setting_site_clearing_image).id for _dimage in SiteClearingImage.objects.filter(day_image_id = self.id).all()]

        except Exception as e:
            return e

class SiteClearingSubtask(TimeTrackModel,TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

        # Sammary Photos
    setting_site_clearing_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/siteclearing/'), blank=True, null=True)
    setting_site_clearing_image_2 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/siteclearing/'),blank=True, null=True)
    setting_site_clearing_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/siteclearing/'),blank=True, null=True)

    setting_site_clearing_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
       # return str(self.project_name)
        return 'SiteClearingSubTask: {}'.format(self.project_name)

    def days_list(self):
        try:
            return [SiteClearingDate.objects.get(work_day= _pday.work_day).id for _pday in SiteClearingDate.objects.filter(sub_task_id = self.id).all()]

        except Exception as e:
            return e


    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def check_cost(self):
        now = datetime.now(timezone.utc)
        date_diff = date_difference(self.start_date, now)
        return date_diff

    def date_casual_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            total_cost = 0
            default_diff = 1
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                date_diff = date_difference(self.start_date, now)
            else:
                date_diff = date_difference(self.start_date, self.end_date)
            while date_diff > default_diff:
                updated_count = self.no_of_casuals_atsite.count()
                casual_count += count
                casual_diff = casual_count - count
                cost = (casual_diff * casual_rate)
                total_cost += cost
                default_diff += 1
            return total_cost
        except Exception as e:
            return e

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = FoundationCreationTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def labour_cost(self):
        try:
            engineer_rate_data = Rates.objects.get(worker_type='Engineer')
            casual_rate_data = Rates.objects.get(worker_type='Casual')
            engineer_rate = engineer_rate_data.rate
            casual_rate = casual_rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = FoundationCreationTask.objects.get(project_name=self.project_name)
                engineer_count = engineer_data.engineers_atsite.count()
                casual_count = self.no_of_casuals_atsite.count()
                cost = (engineer_count * days_spent * engineer_rate) + (casual_count * days_spent * casual_rate)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Site Clearing Subtask')
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

    def task_id(self):
        try:
            task = FoundationCreationTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (2)://///////////Site-TowerBase Images Subtask //////////////////


class TowerBaseImage(TimeStampModel):
    day_image = models.ForeignKey('TowerBaseDate', on_delete=models.CASCADE,related_name ='towerbaseimages')

    towerbase_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/towerbase/'),blank=True, null=True)
    tower_base_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

    def bts_site_id(self):
        try:
            site_name = str(self.day_image).split(':')[1].strip()
            sitename = BtsSite.objects.get(site_name=site_name)
            sitename_id = sitename.id
            return sitename_id
            
        except Exception as e:
            return

class TowerBaseDate(TimeStampModel,):
    sub_task = models.ForeignKey('TowerBaseSubTask', on_delete=models.CASCADE ,related_name= 'towerbasedates')
    work_day = models.DateField(blank=True ,null=True )
    #Casuals
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/TowerBase/'),blank=True, null=True)

    tower_base_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        #return str(self.project_name)
        return '{}: Date: {}'.format(self.sub_task,self.work_day)

class TowerBaseSubtask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING )#,related_name = 'towerbasesubtasks')
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
 
    towerbase_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/towerbase/'),blank=True, null=True)
    towerbase_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/towerbase/'),blank=True, null=True)
    towerbase_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/towerbase/'),blank=True, null=True)
    tower_base_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
       # return str(self.project_name)
        return 'TowerBaseSubTask  : {}'.format(self.project_name)


    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = FoundationCreationTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload excavation images')
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

    def task_id(self):
        try:
            task = FoundationCreationTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (3)://///////////Blinding Subtask //////////////////

class BlindingImage(TimeStampModel):
    day_image = models.ForeignKey('BlindingDate', on_delete=models.CASCADE,related_name ='blindingimages',blank=True, null=True)

    # DailyPhotos
    blinding_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/Blinding/'),blank=True, null=True)
    blinding_image_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

    def bts_site_id(self):
        try:
            site_name = str(self.day_image).split(':')[1].strip()
            sitename = BtsSite.objects.get(site_name=site_name)
            sitename_id = sitename.id
            return sitename_id
            
        except Exception as e:
            return
class BlindingDate(TimeStampModel):
    sub_task = models.ForeignKey('BlindingSubTask', on_delete=models.CASCADE,related_name= 'blindingdates',blank=True, null=True)
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/Blinding/'),blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)


class BlindingSubtask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING,blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True ) # RM
    # Summary Photos
    blinding_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/binding/'),blank=True, null=True)
    blinding_image_2 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/binding/'),blank=True, null=True)
    blinding_image_3 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/binding/'),blank=True, null=True)
    blinding_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'BlindingSubTask  : {}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = FoundationCreationTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def raise_flag(self):
        try:

            kpi_data = SubTask.objects.get(subtask_name='Upload binding images')
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

    def task_id(self):
        try:
            task = FoundationCreationTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (3)://///////////SteelFixFormwork Subtask //////////////////

class SteelFixFormworkImage(TimeStampModel):
    day_image = models.ForeignKey('SteelFixFormworkDate', on_delete=models.CASCADE,related_name = 'steelfixformworkimages',blank=True, null=True)

    # DailyPhotos
    steel_fixformwork_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/SteelFix/'),blank=True, null=True)
    steel_fixformwork_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

    def bts_site_id(self):
        try:
            site_name = str(self.day_image).split(':')[1].strip()
            sitename = BtsSite.objects.get(site_name=site_name)
            sitename_id = sitename.id
            return sitename_id
            
        except Exception as e:
            return

class SteelFixFormworkDate(TimeStampModel):
    sub_task = models.ForeignKey('SteelFixFormworkSubTask', on_delete=models.CASCADE,related_name ='steelfixformworkdates',blank=True, null=True)
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/SteelFixFormwork/'),blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class SteelFixFormworkSubtask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING,blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    steel_fix_formwork_image_1 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/steelfix/'),blank=True, null=True)
    steel_fix_formwork_image_2 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/steelfix/'),blank=True, null=True)
    steel_fix_formwork_image_3 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/steelfix/'),blank=True, null=True)
    steel_fix_formwork_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'SteelFixFormworkSubTask : {}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = FoundationCreationTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload steel fixing images')
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

    def task_id(self):
        try:
            task = FoundationCreationTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


    # SubTask (4)://///////////ConcretePourImage Subtask //////////////////


class ConcretePourImage(TimeStampModel):
    day_image = models.ForeignKey('ConcretePourDate', on_delete=models.CASCADE,related_name = 'concretepourdates',blank=True, null=True)

    # DailyPhotos
    concrete_pour_curing_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/concretepour/'),blank=True, null=True)
    concrete_pour_curing_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

    def bts_site_id(self):
        try:
            site_name = str(self.day_image).split(':')[1].strip()
            sitename = BtsSite.objects.get(site_name=site_name)
            sitename_id = sitename.id
            return sitename_id
            
        except Exception as e:
            return

class ConcretePourDate(TimeStampModel):
    sub_task = models.ForeignKey('ConcretePourSubtask', on_delete=models.CASCADE,related_name= 'concretepourdates',blank=True, null=True)
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/ConcretePour/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class ConcretePourSubtask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING,blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )  #RM

    concrete_pour_curing_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/concretepour/'),blank=True, null=True)
    concrete_pour_curing_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/concretepour/'),blank=True, null=True)
    concrete_pour_curing_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/concretepour/'),blank=True, null=True)
    concrete_pour_curing_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'ConcretePourSubTask : {}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = FoundationCreationTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload concrete pour images')
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

    def task_id(self):
        try:
            task = FoundationCreationTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (5)://///////////ConcreteCuringPeriod Subtask //////////////////


class ConcreteCuringPeriodImage(TimeStampModel):
    day_image = models.ForeignKey('ConcreteCuringPeriodDate', on_delete=models.CASCADE,related_name ='concretecuringperiodimages',blank=True, null=True)

    # DailyPhotos
    concrete_curing_period_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/ConcretePourCuringPeriod/'),blank=True, null=True)
    concrete_curing_period_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class ConcreteCuringPeriodDate(TimeStampModel):
    sub_task = models.ForeignKey('ConcreteCuringPeriodSubTask', on_delete=models.CASCADE,related_name= 'concretecuringperioddates',blank=True, null=True)
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/ConcretePourCuringPeriod/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class ConcreteCuringPeriodSubtask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True ) #RM

    concrete_pour_curing_period_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/ConcretePourCuringPeriod/'),blank=True, null=True)
    concrete_pour_curing_period_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/ConcretePourCuringPeriod/'),blank=True, null=True)
    concrete_pour_curing_period_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/ConcretePourCuringPeriod/'),blank=True, null=True)
    concrete_pour_curing_period_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'ConcreteCuringPeriodSubTask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = FoundationCreationTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload concrete curing images')
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

    def task_id(self):
        try:
            task = FoundationCreationTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

#TASK (1):              |||||| FAUNDATION |||||||

class FoundationCreationTask(TimeTrackModel,TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)

    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    #Sub Tasks
    setting_site_clearing = models.OneToOneField(SiteClearingSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    excavation_tower_base = models.OneToOneField(TowerBaseSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    blinding = models.OneToOneField(BlindingSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    steel_fix_formwork = models.OneToOneField(SteelFixFormworkSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    concrete_pour_curing_period = models.OneToOneField(ConcretePourSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    concrete_curing_period = models.OneToOneField(ConcreteCuringPeriodSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)

    foundation_and_curing_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        #return str(self.project_name)
        return 'Foundation Creation for {}'.format(self.project_name)
        
    class Meta:
        verbose_name_plural  = 'Fountain Creation TASKS'

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.user.username for v in self.engineers_atsite.all()]

    def raise_flag(self):
        try:
            kpi_data =Task.objects.get(task_name='Tower foundation and curing.')
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

######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################
    
    # SubTask (1)://///////////excavation_image Subtask //////////////////


class ExcavationImage(TimeStampModel):
    day_image = models.ForeignKey('ExcavationDate', on_delete=models.CASCADE,related_name ='excavationimages',blank=True, null=True)

    # DailyPhotos
    excavation_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/Excavation/'),blank=True, null=True)
    excavation_image_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class ExcavationDate(TimeStampModel):
    sub_task = models.ForeignKey('ExcavationSubTask', on_delete=models.CASCADE,related_name= 'excavationdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/Excavation/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)


class ExcavationSubtask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    excavation_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/Excavation/'),blank=True, null=True)
    excavation_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/Excavation/'),blank=True, null=True)
    excavation_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/Excavation/'),blank=True, null=True)
    excavation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'ExcavationSubTask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = BS241AndGeneatorSlabTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload BTS and Generator excavation images')
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

    def task_id(self):
        try:
            task = BS241AndGeneatorSlabTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (2)://///////////BS241ConcretePourCuringPeriod Subtask //////////////////


class BS241ConcretePourCuringPeriodImage(TimeStampModel):
    day_image = models.ForeignKey('BS241ConcretePourCuringPeriodDate', on_delete=models.CASCADE,related_name ='bs241Concretepourcuringperiodimages',blank=True, null=True)

    # DailyPhotos
    bs241_concrete_pour_curing_period_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/BS241ConcretePourCuringPeriod/'),max_length = 250,blank=True, null=True)
    bs241_concrete_pour_curing_period_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class BS241ConcretePourCuringPeriodDate(TimeStampModel):
    sub_task = models.ForeignKey('BS241ConcretePourCuringPeriodSubTask', on_delete=models.CASCADE,related_name= 'bs241Concretepourcuringperioddates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/BS241ConcretePourCuringPeriod/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class BS241ConcretePourCuringPeriodSubtask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
   
    bs241_concrete_pour_curing_period_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/BS241ConcretePourCuringPeriod/'), blank=True, null=True)
    bs241_concrete_pour_curing_period_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/BS241ConcretePourCuringPeriod/'), blank=True, null=True)
    bs241_concrete_pour_curing_period_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/BS241ConcretePourCuringPeriod/'), blank=True, null=True)
    bs241_concrete_pour_curing_period_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
       # return str(self.project_name)
        return 'BS241ConcretePourCuringPeriodSubTask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = BS241AndGeneatorSlabTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload concerete pour and curing images')
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

    def task_id(self):
        try:
            task = BS241AndGeneatorSlabTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

# TASK [2] 

class BS241AndGeneratorSlabTask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    #Sub Tasks
    foundation_foot_pouring = models.OneToOneField(ExcavationSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    bs241_concrete_pour_pouring_period = models.OneToOneField(BS241ConcretePourCuringPeriodSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    bs241_and_generator_slabs_comment = models.CharField(max_length=100, blank=True, null=True)
  

    def __str__(self):
        return str(self.project_name)
        return 'BS241 & Generator Slab Task :{}'.format(self.project_name)
    class Meta:
        verbose_name_plural = 'BS241 and Generator Slab TASKS'

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.user.username for v in self.engineers_atsite.all()]

    def raise_flag(self):
        try:
            kpi_data = Task.objects.get(task_name='BTS and Generator Foundation')
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

######################################## END #######################################################################################################################################

####################################### BOUNDARY WALL ###########################################################################################################################

    # SubTask (1)://///////////FoundFootPour Subtask //////////////////


class FoundFootPourImage(TimeStampModel):
    day_image = models.ForeignKey('FoundFootPourDate', on_delete=models.CASCADE,related_name ='foundfootpourimages',blank=True, null=True)

    # DailyPhotos
    foundfootpour_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/FoundFootPour/'),max_length = 250,blank=True, null=True)
    foundfootpour_comment = models.CharField(max_length=100, blank=True, null=True)



    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class FoundFootPourDate(TimeStampModel):
    sub_task = models.ForeignKey('FoundFootPourSubtask', on_delete=models.CASCADE,related_name= 'foundfootpourdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/FoundFootPour/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class FoundFootPourSubtask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    foundfootpour_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/FoundFootPour/'),blank=True, null=True)
    foundfootpour_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/FoundFootPour/'),blank=True, null=True)
    foundfootpour_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/FoundFootPour/'),blank=True, null=True)
    foundfootpour_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'FoundFootPourSubtask :{}'.format(self.project_name) 

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = BoundaryWallTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload foundation, footing and pouring images')
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

    def task_id(self):
        try:
            task = BoundaryWallTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


    # SubTask (1)://///////////FoundFootPour Subtask //////////////////


class BlockworkPanelConstImage(TimeStampModel):
    day_image = models.ForeignKey('BlockworkPanelConstDate', on_delete=models.CASCADE,blank=True, null=True)

    # DailyPhotos
    blockwallpanelconst_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/BlockworkPanelConst//'),max_length = 250,blank=True, null=True)
    blockwallpanelconst_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class BlockworkPanelConstDate(TimeStampModel):
    sub_task = models.ForeignKey('BlockworkPanelConstSubtask', on_delete=models.CASCADE)
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/BlockworkPanelConst/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class BlockworkPanelConstSubtask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    blockwallpanelconst_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/BlockworkPanelConst/') ,blank=True, null=True)
    blockwallpanelconst_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/BlockworkPanelConst/') ,blank=True, null=True)
    blockwallpanelconst_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/BlockworkPanelConst/') ,blank=True, null=True)
    blockwallpanelconst_comment = models.CharField(max_length=100 ,blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'BlockworkPanelConstSubtask :{}'.format(self.project_name) 

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = BoundaryWallTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload panel construction images')
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

    def task_id(self):
        try:
            task = BoundaryWallTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return
    # SubTask (1)://///////////GateInstallation Subtask //////////////////


class GateInstallationImage(TimeStampModel):
    day_image = models.ForeignKey('GateInstallationDate', on_delete=models.CASCADE,related_name ='gateinstallationimages',blank=True, null=True)

    # DailyPhotos
    gateinstallation_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/GateInstallation/'),max_length = 250,blank=True, null=True)
    gateinstallation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class GateInstallationDate(TimeStampModel):
    sub_task = models.ForeignKey('GateInstallationSubtask', on_delete=models.CASCADE,related_name= 'gateinstallationdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/GateInstallation/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class GateInstallationSubtask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
  
    gateinstallation_image_1 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/GateInstallation/'),blank=True, null=True)
    gateinstallation_image_2 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/GateInstallation/'),blank=True, null=True)
    gateinstallation_image_3 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/GateInstallation/'),blank=True, null=True)
    gateinstallation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        #return str(self.project_name)
        return 'GateInstallationSubtask :{}'.format(self.project_name) 

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casual Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = BoundaryWallTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload gate installation images')
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

    def task_id(self):
        try:
            task = BoundaryWallTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (1)://///////////RazorElectricFence Subtask //////////////////


class RazorElectricFenceImage(TimeStampModel):
    day_image = models.ForeignKey('RazorElectricFenceDate', on_delete=models.CASCADE,related_name= 'razorelectricfenceimages',blank=True, null=True)

    # DailyPhotos
    razorelectricfance_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/CivilWorksTeam/RazorElectricFence/'),max_length = 250,blank=True, null=True)
    razorelectricfance_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class RazorElectricFenceDate(TimeStampModel):
    sub_task = models.ForeignKey('RazorElectricFenceSubtask', on_delete=models.CASCADE,related_name='razorelectricfencedates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/RazorElectricFence/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)


class RazorElectricFenceSubtask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
  
    razorelectricfance_image_1 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/RazorElectricFence/'),blank=True, null=True)
    razorelectricfance_image_2 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/RazorElectricFence/'),blank=True, null=True)
    razorelectricfance_image_3 = models.ImageField(upload_to= UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/RazorElectricFence/'),blank=True, null=True)
    razorelectricfance_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'RazorElectricFenceSubtask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casuals Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = BoundaryWallTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload razor/electric fence images')
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

    def task_id(self):
        try:
            task = BoundaryWallTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


# TASK[ BOUNDARY WALL SUBTASK]
class BoundaryWallTask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    #Subtasks
    foundation_foot_pouring = models.OneToOneField(FoundFootPourSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    block_construction = models.OneToOneField(BlockworkPanelConstSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    gate_installation = models.OneToOneField(GateInstallationSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    razor_electric_fence = models.OneToOneField(RazorElectricFenceSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    boundary_wall_comment = models.CharField(max_length=100, blank=True, null=True)
 
    def __str__(self):
        #return str(self.project_name)
        return 'BoundaryWall Task :{}'.format(self.project_name)
    class Meta:
        verbose_name_plural ='Boundary Wall TASKS'

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.user.username for v in self.engineers_atsite.all()]

    def raise_flag(self):
        try:
            kpi_data = Task.objects.get(task_name='Boundary Wall')
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

# END

######################################## END #######################################################################################################################################

####################################### TOWER & ANTENNA_COAX ###########################################################################################################################

# START 
    # SubTask (1)://///////////RazorElectricFence Subtask //////////////////


class TowerErectionImage(TimeStampModel):
    day_image = models.ForeignKey('TowerErectionDate', on_delete=models.CASCADE,related_name ='towererectionimages',blank=True, null=True)

    # DailyPhotos
    tower_erection_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/CivilWorksTeam/towererection/'),max_length = 250,blank=True, null=True)
    tower_erection_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class TowerErectionDate(TimeStampModel):
    sub_task = models.ForeignKey('TowerErectionSubtask', on_delete=models.CASCADE,related_name= 'towererectiondates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/Towererection/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class TowerErectionSubtask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    tower_erection_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/towererection/'),blank=True, null=True)
    tower_erection_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/towererection/'),blank=True, null=True)
    tower_erection_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/towererection/'),blank=True, null=True)
    tower_erection_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
       # return str(self.project_name)
        return 'TowerErectionSubtask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casuals Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Enginner')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = TowerAntennaCoaxTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload tower erection images')
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

    def task_id(self):
        try:
            task = TowerAntennaCoaxTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (1)://///////////TowerPaint Subtask //////////////////


class TowerPaintImage(TimeStampModel):
    day_image = models.ForeignKey('TowerPaintDate', on_delete=models.CASCADE,related_name ='towerpaintimages',blank=True, null=True)

    # DailyPhotos
    tower_painting_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/CivilWorksTeam/towerpainting/'),max_length = 250,blank=True, null=True)
    tower_painting_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class TowerPaintDate(TimeStampModel):
    sub_task = models.ForeignKey('TowerPaintSubtask', on_delete=models.CASCADE,related_name= 'towerpaintdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/Towerpainting/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class TowerPaintSubtask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    tower_painting_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/towerpainting/'),blank=True,null=True)
    tower_painting_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/towerpainting/'),blank=True,null=True)
    tower_painting_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/towerpainting/'),blank=True,null=True)
    tower_painting_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'TowerPaintSubtask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casual Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = TowerAntennaCoaxTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload tower painting images')
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

    def task_id(self):
        try:
            task = TowerAntennaCoaxTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (1)://///////////CableWays Subtask //////////////////


class CableWaysImage(TimeStampModel):
    day_image = models.ForeignKey('CableWaysDate', on_delete=models.CASCADE,related_name ='cablewaysimages',blank=True, null=True)

    # DailyPhotos
    cable_ways_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/CivilWorksTeam/cableways/'),max_length = 250,blank=True, null=True)
    cable_ways_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class CableWaysDate(TimeStampModel):
    sub_task = models.ForeignKey('CableWaysSubtask', on_delete=models.CASCADE,related_name= 'cablewaysdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/Cableways/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class CableWaysSubtask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    cable_ways_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/cableways/'),blank =True,null =True)
    cable_ways_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/cableways/'),blank =True,null =True)
    cable_ways_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/cableways/'),blank =True,null =True)
    cable_ways_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'CableWaysSubtask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casual Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = TowerAntennaCoaxTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload cable ways images')
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

    def task_id(self):
        try:
            task = TowerAntennaCoaxTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (1)://///////////AntennaCoaxInstall Subtask //////////////////


class AntennaCoaxInstallImage(TimeStampModel):
    day_image = models.ForeignKey('AntennaCoaxInstallDate', on_delete=models.CASCADE,related_name ='antennacoaxinstallimages',blank=True, null=True)

    # DailyPhotos
    antenna_coax_installation_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/CivilWorksTeam/antennacoaxinstallation/'),max_length = 250,blank=True, null=True)
    antenna_coax_installation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class AntennaCoaxInstallDate(TimeStampModel):
    sub_task = models.ForeignKey('AntennaCoaxInstallSubtask', on_delete=models.CASCADE,related_name= 'antennacoaxinstalldates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/Antennacoaxinstallation/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)


class AntennaCoaxInstallSubtask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    antenna_coax_installation_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/antennacoaxinstallation/'),blank =True ,null=True)
    antenna_coax_installation_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/antennacoaxinstallation/'),blank =True ,null=True)
    antenna_coax_installation_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/CivilWorksTeam/antennacoaxinstallation/'),blank =True ,null=True)
    antenna_coax_installation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        #return str(self.project_name)
        return 'AntenaCoaxInstallSubtask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casual Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = TowerAntennaCoaxTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload Antenna Coax Installation images')
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

    def task_id(self):
        try:
            task = TowerAntennaCoaxTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

# TASK [4]  

class TowerAntennaCoaxTask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    #Subtasks
    tower_erection = models.OneToOneField(TowerErectionSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_painting = models.OneToOneField(TowerPaintSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    cable_ways = models.OneToOneField(CableWaysSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    antenna_coax_installation = models.OneToOneField(AntennaCoaxInstallSubtask, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_antenna_coax_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.project_name)

    class Meta:
        verbose_name_plural ='Tower Antenna Coax TASKS'

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.user.username for v in self.engineers_atsite.all()]

    def raise_flag(self):
        try:
            kpi_data = Task.objects.get(task_name='Tower & Antenna-Coax')
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

######################################## END #######################################################################################################################################

####################################### INSTALLATION ###########################################################################################################################


class ProjectPurchaseOrder(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    po_file = models.FileField(upload_to='files/CommercialTeam/pofile/%Y/%m/%d/', blank=True, null=True)
    material_cost = models.IntegerField()
    labour_cost = models.IntegerField()
    total_cost_of_po = models.IntegerField()
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return str(self.project_name)

    def totalPOS(self):
        count = self.objects.all().count()
        return count


class ProjectCosting(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    project_costing_file = models.FileField(upload_to='files/CommercialTeam/projectcosting/%Y/%m/%d/', blank=True, null=True)
    material_cost = models.IntegerField()
    labour_cost = models.IntegerField()
    total_projected_cost = models.IntegerField()
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return str(self.project_name)

    def totalProjectCosts(self):
        count = self.objects.all().count()
        return count


class CommercialTeam(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    approved_quote_file = models.FileField(upload_to='files/CommercialTeam/approvedquote/%Y/%m/%d/', blank=True, null=True)
    approved_quote_amount = models.IntegerField(blank=True, null=True)
    po_data = models.OneToOneField(ProjectPurchaseOrder, on_delete=models.CASCADE, blank=True, null=True)
    project_costing_data = models.OneToOneField(ProjectCosting, on_delete=models.CASCADE, blank=True, null=True)
    initial_invoice = models.FileField(upload_to='files/CommercialTeam/initialinvoice/%Y/%m/%d/', blank=True, null=True)
    initial_invoice_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return str(self.project_name)


####################################### PROCURMENT TEAM ###########################################################################################################################
class ProcurementTeam(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    po_steel = models.FileField(upload_to='files/ProcurementTeam/posteel/%Y/%m/%d/', blank=True, null=True)
    # po_steel_quantity = models.IntegerField(blank=True, null=True)
    po_electrical_materials = models.FileField(upload_to=UploadToProjectDir(file_path,'files/ProcurementTeam/poelectrical/'), blank=True, null=True)
    # po_electrical_materials_quantity = models.IntegerField(blank=True, null=True)
    po_subcontractors = models.FileField(upload_to=UploadToProjectDir(file_path,'files/ProcurementTeam/posubcontractor/'), blank=True, null=True)
    po_subcontractors_amount = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return str(self.project_name)

######################################## END #######################################################################################################################################


class AccessApprovalCivil(TimeStampModel):
    project_name = models.ForeignKey(BtsSite,related_name= 'accessapprovalcivil', on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to=UploadToProjectDir(file_path,'files/CivilWorksTeam/accessapproval/'))
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)


class HealthDocumentsCivilTeam(TimeStampModel):
    project_name = models.ForeignKey(BtsSite,related_name= 'healthdocumentscivilteam' ,on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(upload_to=UploadToProjectDir(file_path,'files/HealthDocumentsCivilTeam/jobhazard/'))
    job_hazard_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(upload_to=UploadToProjectDir(file_path,'files/HealthDocumentsCivilTeam/incident/'))
    incident_notification_form_comment = models.CharField(max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(upload_to=UploadToProjectDir(file_path,'files/HealthDocumentsCivilTeam/toolbox/'))
    toolbox_meeting_form_comment = models.CharField(max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(upload_to=UploadToProjectDir(file_path,'files/HealthDocumentsCivilTeam/communication/'))
    communication_plan_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(AccessApprovalCivil, on_delete=models.DO_NOTHING, blank=True, null=True)
    safety_picture = models.ImageField(upload_to=UploadToProjectDir(file_path,'images/HealthDocumentsCivilTeam/'), blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return str(self.project_name)


class CivilWorksTeam(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsCivilTeam, blank=True )

    #TASKS
    foundation_and_curing_images = models.OneToOneField(FoundationCreationTask, on_delete=models.DO_NOTHING, blank=True, null=True)
    bs241_and_generator_slabs_images = models.OneToOneField(BS241AndGeneratorSlabTask, on_delete=models.DO_NOTHING, blank=True, null=True)
    site_walling_images_field = models.OneToOneField(BoundaryWallTask, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_data = models.OneToOneField(TowerAntennaCoaxTask, on_delete=models.DO_NOTHING, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return str(self.project_name)

    class Meta:
        verbose_name_plural = 'CIVIL WORKS TEAM'

    def health_documents_civil(self):
        return [v.project_name for v in self.health_documents.all()]

    def access_approvals(self):
        return [v.project_name for v in self.access_approvals_field.all()]

######################################################3 INSTALLATION TEAM ##################################################################################################################################################################3


class AccessApprovalInstallation(TimeStampModel):
    project_name = models.ForeignKey(BtsSite, on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to=UploadToProjectDir(file_path,'files/InstallationTeam/accessapproval/'))
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
  
    def __str__(self):
        return str(self.project_name)


class HealthDocumentsInstallationTeam(TimeStampModel):
    project_name = models.ForeignKey(BtsSite, on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(upload_to=UploadToProjectDir(file_path,'files/HealthDocumentsInstallationTeam/jobhazard/'))
    job_hazard_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(upload_to=UploadToProjectDir(file_path,'files/HealthDocumentsInstallationTeam/incident/'))
    incident_notification_form_comment = models.CharField(max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(upload_to=UploadToProjectDir(file_path,'files/HealthDocumentsInstallationTeam/toolbox/'))
    toolbox_meeting_form_comment = models.CharField(max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(upload_to=UploadToProjectDir(file_path,'files/HealthDocumentsInstallationTeam/communication/'))
    communication_plan_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(AccessApprovalInstallation, on_delete=models.CASCADE, blank=True, null=True)
    safety_picture = models.ImageField(upload_to=UploadToProjectDir(file_path,'images/HealthDocumentsInstallationTeam/'), blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return str(self.project_name)



    # SubTask (1)://///////////UndergroundTask Subtask //////////////////


class UndergroundTaskImage(TimeStampModel):
    day_image = models.ForeignKey('UndergroundTaskDate', on_delete=models.CASCADE,related_name ='undergroundtaskimages',blank=True, null=True)

    # DailyPhotos
    underground_ducting_and_manholes_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/CivilWorksTeam/antennacoaxinstallation/'),max_length = 250,blank=True, null=True)
    underground_ducting_and_manholes_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class UndergroundTaskDate(TimeStampModel):
    sub_task = models.ForeignKey('UndergroundTask', on_delete=models.CASCADE,related_name= 'undergroundtaskdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/UnderGroundTasks/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class UndergroundTask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    underground_ducting_and_manholes_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTask/%Y/%m/%d/', blank=True, null=True)
    underground_ducting_and_manholes_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTask/%Y/%m/%d/', blank=True, null=True)
    underground_ducting_and_manholes_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTask/%Y/%m/%d/', blank=True, null=True)
    underground_ducting_and_manholes_images_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'UndergroundSubtask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casuals Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = ElectricalTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload Underground ducting & manholes images')
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

    def task_id(self):
        try:
            task = ElectricalTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (1)://///////////AntennaCoaxInstall Subtask //////////////////


class ReticulationAPSinstallationImage(TimeStampModel):
    day_image = models.ForeignKey('ReticulationAPSinstallationDate', on_delete=models.CASCADE,related_name ='reticulationAPSinstallationimages',blank=True, null=True)

    # DailyPhotos
    electricalreticulation_APSInstallation_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/InstallationTeam/Electrical/ReticulationAPSinstallation/'),max_length = 250,blank=True, null=True)
    electricalreticulation_APSInstallation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class ReticulationAPSinstallationDate(TimeStampModel):
    sub_task = models.ForeignKey('ReticulationAPSinstallation', on_delete=models.CASCADE,related_name= 'reticulationAPSinstallationdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/ReticulationAPSinstallation/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class ReticulationAPSinstallation(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    electricalreticulation_APSInstallation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/', blank=True, null=True)
    electricalreticulation_APSInstallation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/', blank=True, null=True)
    electricalreticulation_APSInstallation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/', blank=True, null=True)
    electricalreticulation_APSInstallation_images_comment = models.CharField(max_length=100, blank=True, null=True)
 

    def __str__(self):
        #return str(self.project_name)
        return 'ReticulationAPSinstallationSubtask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casuals Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = ElectricalTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload Electrical reticulation/APS Installation images')
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

    def task_id(self):
        try:
            task = ElectricalTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (1)://///////////AntennaCoaxInstall Subtask //////////////////


class ElectricalEarthingImage(TimeStampModel):
    day_image = models.ForeignKey('ElectricalEarthingDate', on_delete=models.CASCADE,related_name ='electricalearthingimages',blank=True, null=True)

    # DailyPhotos
    earthing_connections_and_testing_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/InstallationTeam/Electrical/Generator_FuelTank_Install/'),max_length = 250,blank=True, null=True)
    earthing_connections_and_testing_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class ElectricalEarthingDate(TimeStampModel):
    sub_task = models.ForeignKey('ElectricalEarthing', on_delete=models.CASCADE,related_name= 'electricalearthingdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/GeneratorElectricalsInstalls/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class ElectricalEarthing(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    earthing_connections_and_testing_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Electrical/Generator_FuelTank_Install/'), blank=True, null=True)
    earthing_connections_and_testing_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Electrical/Generator_FuelTank_Install/'), blank=True, null=True)
    earthing_connections_and_testing_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Electrical/Generator_FuelTank_Install/'), blank=True, null=True)
    earthing_connections_and_testing_images_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'ElectricalEarthingSubtask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casuals Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Enginner')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = ElectricalTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Enginner Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload Earthing connections and testing images')
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

    def task_id(self):
        try:
            task = ElectricalTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (1)://///////////GeneratorInstallation Subtask //////////////////


class GeneratorInstallationImage(TimeStampModel):
    day_image = models.ForeignKey('AntennaCoaxInstallDate', on_delete=models.CASCADE,related_name ='generatorinstallationimages',blank=True, null=True)

    # DailyPhotos
    generator_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/CivilWorksTeam/generatorinstallation/'),max_length = 250,blank=True, null=True)
    generator_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class GeneratorInstallationDate(TimeStampModel):
    sub_task = models.ForeignKey('AntennaCoaxInstallSubtask', on_delete=models.CASCADE,related_name= 'generatorinstallationdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/GeneratorInstall/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class GeneratorInstallation(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    Generator_and_Fuel_Tank_Installation_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Electrical/Generator_FuelTank_Install/'), blank=True, null=True)
    Generator_and_Fuel_Tank_Installation_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Electrical/Generator_FuelTank_Install/'), blank=True, null=True)
    Generator_and_Fuel_Tank_Installation_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Electrical/Generator_FuelTank_Install/'), blank=True, null=True)
    
    before_fuel_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Electrical/Fueling/'),blank=True ,null =True)
    before_fuel_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Electrical/Fueling/'),blank=True ,null =True)
    after_fuel_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Electrical/Fueling/'),blank=True ,null =True)
    after_fuel_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Electrical/Fueling/'),blank=True ,null =True)
    Generator_and_Fuel_Tank_Installation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'GeneratorInstallationSubtask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casuals Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = ElectricalTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload Generator & Fuel Tank Installation images')
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

    def task_id(self):
        try:
            task = ElectricalTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

    # SubTask (1)://///////////KPLCSolar Subtask //////////////////


class KPLCSolarImage(TimeStampModel):
    day_image = models.ForeignKey('KPLCSolarDate', on_delete=models.CASCADE,related_name ='kplcsolarimages',blank=True, null=True)

    # DailyPhotos
    kplc_solar_installation_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/CivilWorksTeam/KPLCSolar/'),max_length = 250,blank=True, null=True)
    kplc_solar_installation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class KPLCSolarDate(TimeStampModel):
    sub_task = models.ForeignKey('KPLCSolarSubtask', on_delete=models.CASCADE,related_name= 'kplcsolardates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/KPLCSolar/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class KPLCSolarSubtask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    kplc_solar_installation_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/KPLCSolar/'), blank=True, null=True)
    kplc_solar_installation_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/KPLCSolar/'), blank=True, null=True)
    kplc_solar_installation_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/KPLCSolar/'), blank=True, null=True)
    kplc_solar_installation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'KplcSolarSubTaskSubtask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casuals Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = ElectricalTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload KPLC/solar installation images')
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

    def task_id(self):
        try:
            task = ElectricalTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class ElectricalTask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )

    underground_ducting_and_manholes = models.OneToOneField(UndergroundTask, on_delete=models.DO_NOTHING, blank=True, null=True)
    electricalreticulation_APSInstallation = models.OneToOneField(ReticulationAPSinstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    earthing_connections_and_testing = models.OneToOneField(ElectricalEarthing, on_delete=models.DO_NOTHING, blank=True, null=True)
    generator_and_Fuel_Tank_Installation = models.OneToOneField(GeneratorInstallation, on_delete=models.DO_NOTHING, blank=True, null=True)
    kPLC_solar_installation = models.OneToOneField(KPLCSolarImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.project_name)

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.user.username for v in self.engineers_atsite.all()]

    def raise_flag(self):
        try:
            kpi_data = Task.objects.get(task_name='Electrical Tasks')
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
            team = InstallationTeam.objects.get(project_name=self.project_name)
            team_id = team.id
            return team_id
        except Exception as e:
            return

    # SubTask (1)://///////////MWInstallationTaskSubtask //////////////////


class BTSinstallationTaskImage(TimeStampModel):
    day_image = models.ForeignKey('BTSinstallationTaskDate', on_delete=models.CASCADE,related_name ='btsinstallationtaskimages',blank=True, null=True)

    # DailyPhotos
    mWinstallation_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/installationTeam/Telecom/MWinstallation/'),max_length = 250,blank=True, null=True)
    mWinstallation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class BTSinstallationTaskDate(TimeStampModel):
    sub_task = models.ForeignKey('BTSinstallationTask', on_delete=models.CASCADE,related_name= 'btsinstallationtaskdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/MWInstallationTask/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class BTSinstallationTask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    
    BTSinstallation_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Telecom/BTSinstallation/'), blank=True, null=True)
    BTSinstallation_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Telecom/BTSinstallation/'), blank=True, null=True)
    BTSinstallation_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Telecom/BTSinstallation/'), blank=True, null=True)
    BTSinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
  

    def __str__(self):
       # return str(self.project_name)
        return 'BTSinstallationTask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casuals Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = TelecomTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload BTS installation images')
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

    def task_id(self):
        try:
            task = TelecomTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


    # SubTask (1)://///////////MWInstallationTaskSubtask //////////////////


class MWInstallationTaskImage(TimeStampModel):
    day_image = models.ForeignKey('MWInstallationTaskDate', on_delete=models.CASCADE,related_name ='mwinstallationtaskimages',blank=True, null=True)

    # DailyPhotos
    mWinstallation_image = models.ImageField(upload_to= UploadToProjectDirImage(file_path,'images/installationTeam/Telecom/MWinstallation/'),max_length = 250,blank=True, null=True)
    mWinstallation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        #return str(self.project_name)
        return 'Image for {}'.format(self.day_image)

class MWInstallationTaskDate(TimeStampModel):
    sub_task = models.ForeignKey('MWInstallationTask', on_delete=models.CASCADE,related_name= 'mwinstallationtaskdates')
    work_day =  models.DateField(blank=True, null=True)
    # Casuals
    casuals_list = models.FileField(upload_to=UploadToProjectDirDate(file_path,'files/Casuals/MWInstallationTask/'),blank=True, null=True)
    casuals_atsite = models.ManyToManyField(Casual, blank=True )

    def __str__(self):
        #return str(self.project_name)
        return '{} :Date: {}'.format(self.sub_task,self.work_day)

class MWInstallationTask(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )

    mWinstallation_image_1 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Telecom/MWinstallation/'), blank=True, null=True)
    mWinstallation_image_2 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Telecom/MWinstallation/'), blank=True, null=True)
    mWinstallation_image_3 = models.ImageField(upload_to=UploadToProjectDirSubTask(file_path,'images/InstallationTeam/Telecom/MWinstallation/'), blank=True, null=True)
    mWinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
 
    def __str__(self):
       # return str(self.project_name)
        return 'MWInstallationTask :{}'.format(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            count = self.no_of_casuals_atsite.count()
            cost = (count * casual_rate * days_spent)
            return cost
        except Exception as e:
            error = "Casuals Rates does not exist"
            return error

    def engineers_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Engineer')
            engineer_rate = rate_data.rate
            now = datetime.now(timezone.utc)
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, now)
            else:
                days_spent = date_difference(self.start_date, self.end_date)
            try:
                engineer_data = TelecomTask.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Engineer Rates does not exist"
            return error

    def raise_flag(self):
        try:
            kpi_data = SubTask.objects.get(subtask_name='Upload MW installation images')
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

    def task_id(self):
        try:
            task = TelecomTask.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class TelecomTask(TimeStampModel ,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    Installation_of_BTS = models.OneToOneField(BTSinstallationTask, on_delete=models.DO_NOTHING, blank=True, null=True)
    Installation_of_MW_links = models.OneToOneField(MWInstallationTask, on_delete=models.DO_NOTHING, blank=True, null=True)
    link_commissioning = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return str(self.project_name)

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.user.username for v in self.engineers_atsite.all()]

    def raise_flag(self):
        try:
            kpi_data = Task.objects.get(task_name='Telecom Tasks')
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
            team = InstallationTeam.objects.get(project_name=self.project_name)
            team_id = team.id
            return team_id
        except Exception as e:
            return


class Issue(TimeStampModel):
    project_name = models.ForeignKey(BtsSite, on_delete=models.DO_NOTHING,related_name='issues')
    issue = models.CharField(max_length=100)
    issue_image = models.ImageField(upload_to=UploadToProjectDir(file_path,'images/InstallationTeam/issue/'), blank=True, null=True)
    issue_sorted_image = models.ImageField(upload_to=UploadToProjectDir(file_path,'images/InstallationTeam/issue/%Y/%m/%d/'), blank=True, null=True)
    closed = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.issue


class InstallationTeam(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsInstallationTeam ,blank=True)
    electrical_tasks_data = models.OneToOneField(ElectricalTask, on_delete=models.DO_NOTHING, blank=True, null=True)
    telecom_tasks_data = models.OneToOneField(TelecomTask, on_delete=models.DO_NOTHING, blank=True, null=True)
    as_built = models.FileField(upload_to=UploadToProjectDir(file_path,'files/SafaricomTeam/as_built/'), blank=True, null=True)
    signoff = models.FileField(upload_to=UploadToProjectDir(file_path,'files/SafaricomTeam/signoff/'), blank=True, null=True)
    signoff_comment = models.CharField(max_length=100, blank=True, null=True)
    rfi_document = models.FileField(upload_to=UploadToProjectDir(file_path,'files/SafaricomTeam/rf/'), blank=True, null=True)
    rfi_document_comment = models.CharField(max_length=100, blank=True, null=True)
    integration_parameter = models.BooleanField(default=False)
    integration_parameter_comment = models.CharField(max_length=100, blank=True, null=True)
    snag_document = models.FileField(upload_to=UploadToProjectDir(file_path,'files/SafaricomTeam/snag/'), blank=True, null=True)
    snag_document_comment = models.CharField(max_length=100, blank=True, null=True)
    issue = models.ManyToManyField(Issue, blank=True)
    conditional_acceptance_cert = models.FileField(upload_to=UploadToProjectDir(file_path,'files/SafaricomTeam/conditionalcert/'), blank=True, null=True)
    conditional_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
 

    def __str__(self):
        return str(self.project_name)

    def health_documents_installation(self):
        return [v.project_name for v in self.health_documents.all()]

    def access_approvals(self):
        return [v.project_name for v in self.access_approvals_field.all()]

    def project_issue(self):
        return [v.project_name for v in self.issue.all()]


def date_difference(start_date, end_date):
    diff = end_date - start_date
    no_of_days = (diff.days + 1)
    return no_of_days


class WarrantyCertificate(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    civilworks_installation_certificate = models.FileField(upload_to=UploadToProjectDir(file_path,'files/WarrantyCertificates/civilworks/'), blank=True, null=True)
    connectors_torque_certificate = models.FileField(upload_to=UploadToProjectDir(file_path,'files/WarrantyCertificates/connectorsTorque/'), blank=True, null=True)
    safe_to_climb_certificate = models.FileField(upload_to=UploadToProjectDir(file_path,'files/WarrantyCertificates/SafeToClimb/'), blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return str(self.project_name)


class TestCetificate(TimeStampModel):
    project_name =models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    cube_test_7days = models.FileField(upload_to=UploadToProjectDir(file_path,'files/TestCertificates/cubetest7/'), blank=True, null=True)
    cube_test_28days = models.FileField(upload_to=UploadToProjectDir(file_path,'files/TestCertificates/cubetest28/%Y/'), blank=True, null=True)
    earth_test = models.FileField(upload_to=UploadToProjectDir(file_path,'files/TestCertificates/earthtest/'), blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.project_name)

def percentage_function(no_of_complete, total_task):
    """Function to return perecentage of progress  """
    percentage = round(((no_of_complete/total_task) * 100))
    return percentage
