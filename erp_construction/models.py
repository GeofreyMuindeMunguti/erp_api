from django.db import models
from django.db.models import Sum, F
from django.contrib.auth.models import User
from users.models import *
from erp_core.base import *
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone, timedelta
import math
from erp_construction.btsfiles.filemixin import *

file_path = 'BTSProjects'

class ProjectIcons(models.Model):
    icon = models.ImageField(upload_to='images/Project/Icons/%Y/%m/%d/')
    site_owner = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.site_owner

class BtsProject(models.Model):
    bts_project_name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    icon = models.ForeignKey(ProjectIcons, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.bts_project_name

    class Meta:
        verbose_name_plural = 'BTS PROJECTS'

class BtsSite(TimeStampModel,TimeTrackModel):
    project_name = models.ForeignKey(BtsProject, on_delete=models.CASCADE, blank=True, null=True)
    site_name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    site_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    BTS_type = models.CharField(max_length=100, blank=True, null=True)
    site_owner = models.CharField(max_length=100, blank=True, null=True)
    icon = models.ForeignKey(ProjectIcons, on_delete=models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True)
    geotech_file = models.FileField(upload_to='files/Project/geotech/%Y/%m/%d/', blank=True, null=True)
    geotech_file_comment =  models.CharField(max_length=100, blank=True, null=True)
    access_letter = models.FileField(upload_to='files/Project/accessletters/%Y/%m/%d/', blank=True, null=True)
    approved_drawing = models.FileField(upload_to='files/Project/approveddrawings/%Y/%m/%d/', blank=True, null=True)
    final_acceptance_cert = models.FileField(upload_to='files/SafaricomTeam/finalcert/%Y/%m/%d/', blank=True, null=True)
    final_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    rof_8 = models.FileField(upload_to='files/Project/rof8s/%Y/%m/%d/', blank=True, null=True)
    rof_8_comment = models.CharField(max_length=100, blank=True, null=True)
    sign_off = models.FileField(upload_to='files/Project/signoffs/%Y/%m/%d/', blank=True, null=True)
    sign_off_comment = models.CharField(max_length=100, blank=True, null=True)
    rfi = models.FileField(upload_to='files/Project/rfis/%Y/%m/%d/', blank=True, null=True)
    rfi_comment = models.CharField(max_length=100, blank=True, null=True)
    integration_parameter = models.FileField(upload_to='files/Project/integrationparameters/%Y/%m/%d/', blank=True, null=True)
    integration_parameter_comment = models.CharField(max_length=100, blank=True, null=True)
    ip_plan = models.FileField(upload_to='files/Project/ipplans/%Y/%m/%d/', blank=True, null=True)
    ip_plan_comment= models.FileField(upload_to='files/Project/ipplans/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
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

#####################################IRROF7Free#########################################################################################
class IRROF7Free(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    tower_complete = models.FileField(upload_to='files/IRROF7Frees/towercomplete/%Y/%m/%d/', blank=True, null=True)
    tower_complete_comment = models.CharField(max_length=100, blank=True, null=True)
    free_issue_material = models.FileField(upload_to='files/IRROF7Frees/freeissuematerials/%Y/%m/%d/', blank=True, null=True)
    free_issue_material_comment = models.CharField(max_length=100, blank=True, null=True)
    link_material = models.FileField(upload_to='files/IRROF7Frees/linkmaterials/%Y/%m/%d/', blank=True, null=True)
    link_material_comment = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.project_name)

####################################### BUDGET ########################################################################################################################################

class BtsBudget(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    beneficiary_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=350, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    phoneNumber = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_approved = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.beneficiary_name)

    def amount(self):
        return float(self.quantity * self.rate)
####################################### END ########################################################################################################################################

"""BTS"""
####################################### BTS KPI ###############################################################################################################################
class Kpi(models.Model):
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.kpi)

######################################## END #######################################################################################################################################

####################################### BTS TASKS ###############################################################################################################################
class Task(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    task_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.task_name)

######################################## END #######################################################################################################################################

####################################### BTS SUBTASKS ###############################################################################################################################
class SubTask(models.Model):
    task_name = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    subtask_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subtask_name)

######################################## END #######################################################################################################################################
"""END"""

#######################################START FOUNDATION IMAGES########################################################################################################################################
class SetSiteClearingImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    setting_site_clearing_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/siteclearing/%Y/%m/%d/')
    setting_site_clearing_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/siteclearing/%Y/%m/%d/')
    setting_site_clearing_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/siteclearing/%Y/%m/%d/')
    setting_site_clearing_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = FoundationImage.objects.get(project_name=self.project_name)
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
                engineer_data = FoundationImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload site clearing and setting images')
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
            task = FoundationImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class TowerBaseImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    towerbase_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/towerbase/%Y/%m/%d/')
    towerbase_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/towerbase/%Y/%m/%d/')
    towerbase_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/towerbase/%Y/%m/%d/')
    tower_base_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = FoundationImage.objects.get(project_name=self.project_name)
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
            task = FoundationImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class BindingImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    binding_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/binding/%Y/%m/%d/')
    binding_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/binding/%Y/%m/%d/')
    binding_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/binding/%Y/%m/%d/')
    binding_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = FoundationImage.objects.get(project_name=self.project_name)
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
            task = FoundationImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class SteelFixFormworkImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    steel_fix_formwork_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/steelfix/%Y/%m/%d/')
    steel_fix_formwork_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/steelfix/%Y/%m/%d/')
    steel_fix_formwork_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/steelfix/%Y/%m/%d/')
    steel_fix_formwork_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = FoundationImage.objects.get(project_name=self.project_name)
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
            task = FoundationImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class ConcretePourImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    concrete_pour_curing_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/')
    concrete_pour_curing_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/')
    concrete_pour_curing_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/concretepour/%Y/%m/%d/')
    concrete_pour_curing_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = FoundationImage.objects.get(project_name=self.project_name)
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
            task = FoundationImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return
class ConcreteCuringPeriodDocs(TimeStampModel):
    Rebar_Concrete_Inspection = models. BooleanField(blank=True)
    Concrete_Inspection_Report = models. BooleanField(blank=True)
    Concrete_Cube_Test = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/ConcreteCubeTest/'),blank=True, null=True)
    def __str__(self):
        return str(self.Rebar_Concrete_Inspection)


class ConcreteCuringPeriodImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    concrete_curing_period_docs = models.OneToOneField(ConcreteCuringPeriodDocs, on_delete=models.CASCADE)
    concrete_pour_curing_period_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/')
    concrete_pour_curing_period_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/')
    concrete_pour_curing_period_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/')
    concrete_pour_curing_period_comment = models.CharField(max_length=100, blank=True, null=True)
    rebar_concrete_inspection = models.BooleanField(blank=True, null=True)
    concrete_inspection_report = models.BooleanField(blank=True, null=True)
    concrete_cube_test = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = FoundationImage.objects.get(project_name=self.project_name)
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
            task = FoundationImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class FoundationImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    setting_site_clearing = models.OneToOneField(SetSiteClearingImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    excavation_tower_base = models.OneToOneField(TowerBaseImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    binding = models.OneToOneField(BindingImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    steel_fix_formwork = models.OneToOneField(SteelFixFormworkImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    concrete_pour_curing_period = models.OneToOneField(ConcretePourImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    concrete_curing_period = models.OneToOneField(ConcreteCuringPeriodImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    foundation_and_curing_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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

####################################### ADDED #############################################################
class DeliveryOfMaterialandEquipement(TimeStampModel):

    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    material_and_equipement_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/materialandequipement/'),blank=True, null=True)
    material_and_equipement_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image)

############################################################################################


######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################


class ExcavationImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    excavation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    excavation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    excavation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    excavation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = BS241AndGeneatorSlabsImage.objects.get(project_name=self.project_name)
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
            task = BS241AndGeneatorSlabsImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class BS241ConcretePourCuringPeriodImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    bs241_concrete_pour_curing_period_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/BS241ConcretePourCuringPeriod/%Y/%m/%d/')
    bs241_concrete_pour_curing_period_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/BS241ConcretePourCuringPeriod/%Y/%m/%d/')
    bs241_concrete_pour_curing_period_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/BS241ConcretePourCuringPeriod/%Y/%m/%d/')
    bs241_concrete_pour_curing_period_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = BS241AndGeneatorSlabsImage.objects.get(project_name=self.project_name)
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
            task = BS241AndGeneatorSlabsImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class BS241Image(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    bs241_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/BS241Images/'),max_length = 250,blank=True, null=True)
    bs241_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.bs241_image)

class BS241AndGeneatorSlabsImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    foundation_foot_pouring = models.OneToOneField(ExcavationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    bs241_concrete_pour_pouring_period = models.OneToOneField(BS241ConcretePourCuringPeriodImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    bs241_and_generator_slabs_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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


class FoundFootPourImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    foundfootpour_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    foundfootpour_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    foundfootpour_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    foundfootpour_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = BoundaryWallImage.objects.get(project_name=self.project_name)
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
            task = BoundaryWallImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class BlockworkPanelConstImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    blockwallpanelconst_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/BlockworkPanelConst/%Y/%m/%d/')
    blockwallpanelconst_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/BlockworkPanelConst/%Y/%m/%d/')
    blockwallpanelconst_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/BlockworkPanelConst/%Y/%m/%d/')
    blockwallpanelconst_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = BoundaryWallImage.objects.get(project_name=self.project_name)
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
            task = BoundaryWallImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class GateInstallationImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    gateinstallation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/GateInstallation/%Y/%m/%d/')
    gateinstallation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/GateInstallation/%Y/%m/%d/')
    gateinstallation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/GateInstallation/%Y/%m/%d/')
    gateinstallation_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = BoundaryWallImage.objects.get(project_name=self.project_name)
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
            task = BoundaryWallImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class RazorElectricFenceImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    razorelectricfance_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/RazorElectricFence/%Y/%m/%d/')
    razorelectricfance_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/RazorElectricFence/%Y/%m/%d/')
    razorelectricfance_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/RazorElectricFence/%Y/%m/%d/')
    razorelectricfance_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = BoundaryWallImage.objects.get(project_name=self.project_name)
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
            task = BoundaryWallImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class BWConcretePourCuringPeriodImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    bw_concrete_pour_curing_period_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/BWConcretePourCuringPeriodImage/%Y/%m/%d/')
    bw_concrete_pour_curing_period_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/BWConcretePourCuringPeriodImage/%Y/%m/%d/')
    bw_concrete_pour_curing_period_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/BWConcretePourCuringPeriodImage/%Y/%m/%d/')
    bw_concrete_pour_curing_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = BoundaryWallImage.objects.get(project_name=self.project_name)
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
            task = BoundaryWallImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class ExcavationstripFoundationsImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    excavationstrip_foundations_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/ExcavationstripFoundationsImage/%Y/%m/%d/')
    excavationstrip_foundations_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/ExcavationstripFoundationsImage/%Y/%m/%d/')
    excavationstrip_foundations_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/ExcavationstripFoundationsImage/%Y/%m/%d/')
    excavationstrip_foundations_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = BoundaryWallImage.objects.get(project_name=self.project_name)
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
            task = BoundaryWallImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class BWBlindingImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    bw_blinding_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/BWBlindingImage/%Y/%m/%d/')
    bw_blinding_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/BWBlindingImage/%Y/%m/%d/')
    bw_blinding_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/BWBlindingImage/%Y/%m/%d/')
    bw_blinding_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = BoundaryWallImage.objects.get(project_name=self.project_name)
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
            task = BoundaryWallImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class BWCableConduitsImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    bw_cable_conduits_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/BWCableConduitsImage/%Y/%m/%d/')
    bw_cable_conduits_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/BWCableConduitsImage/%Y/%m/%d/')
    bw_cable_conduits_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/BWCableConduitsImage/%Y/%m/%d/')
    bw_cable_conduits_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = BoundaryWallImage.objects.get(project_name=self.project_name)
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
            task = BoundaryWallImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class BoundaryWallImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )

    foundation_foot_pouring = models.OneToOneField(FoundFootPourImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    block_construction = models.OneToOneField(BlockworkPanelConstImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    gate_installation = models.OneToOneField(GateInstallationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    razor_electric_fence = models.OneToOneField(RazorElectricFenceImage, on_delete=models.DO_NOTHING, blank=True, null=True)

    bw_concrete_pour_curing_period = models.OneToOneField(BWConcretePourCuringPeriodImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    excavationstrip_foundations = models.OneToOneField(ExcavationstripFoundationsImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    bw_blinding = models.OneToOneField(BWBlindingImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    bw_cable_conduits = models.OneToOneField(BWCableConduitsImage, on_delete=models.DO_NOTHING, blank=True, null=True)


    boundary_wall_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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


######################################## END #######################################################################################################################################

####################################### TOWER & ANTENNA_COAX ###########################################################################################################################


class TowerErectionImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    tower_erection_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/towererection/%Y/%m/%d/')
    tower_erection_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/towererection/%Y/%m/%d/')
    tower_erection_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/towererection/%Y/%m/%d/')
    tower_erection_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
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
            task = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@TODO REVIEW@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class CableInstallationImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    cable_installation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/CableInstallationImage/%Y/%m/%d/')
    cable_installation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/CableInstallationImage/%Y/%m/%d/')
    cable_installation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/CableInstallationImage/%Y/%m/%d/')
    cable_installation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
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
            task = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class AviationLightsInstallationImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    aviation_lights_installation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/aviationlightsinstallationimage/%Y/%m/%d/')
    aviation_lights_installation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/aviationlightsinstallationimage/%Y/%m/%d/')
    aviation_lights_installation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/aviationlightsinstallationimage/%Y/%m/%d/')
    aviation_lights_installation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
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
            task = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class TowerDeliveryImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    tower_delivery_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/towerdelivery/%Y/%m/%d/')
    tower_delivery_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/towerdelivery/%Y/%m/%d/')
    tower_delivery_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/towerdelivery/%Y/%m/%d/')
    tower_delivery_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
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
            task = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class BoundaryWallImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    #engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    foundation_foot_pouring = models.OneToOneField(FoundFootPourImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    block_construction = models.OneToOneField(BlockworkPanelConstImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    gate_installation = models.OneToOneField(GateInstallationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    razor_electric_fence = models.OneToOneField(RazorElectricFenceImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    boundary_wall_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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

class FabricationQualityInspectionImage(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    fabrication_quality_inspection_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/FabricationQualityInspectionImage/%Y/%m/%d/')
    fabrication_quality_inspection_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/FabricationQualityInspectionImage/%Y/%m/%d/')
    fabrication_quality_inspection_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/FabricationQualityInspectionImage/%Y/%m/%d/')
    fabrication_quality_inspection_image_comment = models.CharField(max_length=100, blank=True, null=True)

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
                engineer_data = FabricationRooftopImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload fabrication Quality Inspection images')
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
            task = FabricationRooftopImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class FabricationSteelDeckImage(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    fabrication_steel_deck_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/FabricationSteelDeckImage/%Y/%m/%d/')
    fabrication_steel_deck_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/FabricationSteelDeckImage/%Y/%m/%d/')
    fabrication_steel_deck_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/FabricationSteelDeckImage/%Y/%m/%d/')
    fabrication_steel_deck_image_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = FabricationRooftopImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload fabrication steel deck images')
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
            task = FabricationRooftopImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class GalvanisationImage(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    galvanisation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/GalvanisationImage/%Y/%m/%d/')
    galvanisation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/GalvanisationImage/%Y/%m/%d/')
    galvanisation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/GalvanisationImage/%Y/%m/%d/')
    galvanisation_image_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = FabricationRooftopImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload galvanisation images')
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
            task = FabricationRooftopImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class FabricationRooftopImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    fabrication_quality_inspection_image = models.OneToOneField(FabricationQualityInspectionImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    fabrication_steel_deck_image = models.OneToOneField(FabricationSteelDeckImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    galvanization_image = models.OneToOneField(GalvanisationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    fabrication_rooftop_image_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.project_name)

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.user.username for v in self.engineers_atsite.all()]

    def raise_flag(self):
        try:
            kpi_data = Task.objects.get(task_name='Fabrication Roof Top')
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


class HackingExistingColumnsImage(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    hacking_existing_columns_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/HackingExistingColumnsImage/%Y/%m/%d/')
    hacking_existing_columns_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/HackingExistingColumnsImage/%Y/%m/%d/')
    hacking_existing_columns_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/HackingExistingColumnsImage/%Y/%m/%d/')
    hacking_existing_columns_image_comment = models.CharField(max_length=100, blank=True, null=True)

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
                engineer_data = InstallationRooftopImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload Hacking Existing Columns images')
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
            task = InstallationRooftopImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return
class FormworkColumnsConcretePourCuringImage(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    formwork_columns_concrete_pour_curing_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/FormworkColumnsConcretePourCuringImage/%Y/%m/%d/')
    formwork_columns_concrete_pour_curing_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/FormworkColumnsConcretePourCuringImage/%Y/%m/%d/')
    formwork_columns_concrete_pour_curing_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/FormworkColumnsConcretePourCuringImage/%Y/%m/%d/')
    formwork_columns_concrete_pour_curing_image_comment = models.CharField(max_length=100, blank=True, null=True)

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
                engineer_data = InstallationRooftopImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload Formwork Columns Congrete Pour Curing images')
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
            task = InstallationRooftopImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class DeliveryToSiteImage(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    delivery_to_site_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/DeliveryToSiteImage/%Y/%m/%d/')
    delivery_to_site_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/DeliveryToSiteImage/%Y/%m/%d/')
    delivery_to_site_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/DeliveryToSiteImage/%Y/%m/%d/')
    delivery_to_site_image_comment = models.CharField(max_length=100, blank=True, null=True)

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
                engineer_data = InstallationRooftopImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload Delivery To Site images')
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
            task = InstallationRooftopImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class LiftingHoistingFreeIssueImage(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    lifting_hoisting_free_issue_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/LiftingHoistingFreeIssueImage/%Y/%m/%d/')
    lifting_hoisting_free_issue_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/LiftingHoistingFreeIssueImage/%Y/%m/%d/')
    lifting_hoisting_free_issue_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/LiftingHoistingFreeIssueImage/%Y/%m/%d/')
    lifting_hoisting_free_issue_image_comment = models.CharField(max_length=100, blank=True, null=True)

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
                engineer_data = InstallationRooftopImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload Lifting Hoisting Free Issue images')
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
            task = InstallationRooftopImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class FenceInstallationImage(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    fence_installation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/FenceInstallationImage/%Y/%m/%d/')
    fence_installation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/FenceInstallationImage/%Y/%m/%d/')
    fence_installation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/FenceInstallationImage/%Y/%m/%d/')
    fence_installation_image_comment = models.CharField(max_length=100, blank=True, null=True)

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
                engineer_data = InstallationRooftopImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload Fence Installation Images')
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
            task = InstallationRooftopImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class SiteRestorationImage(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    site_restoration_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/SiteRestorationImage/%Y/%m/%d/')
    site_restoration_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/SiteRestorationImage/%Y/%m/%d/')
    site_restoration_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/SiteRestorationImage/%Y/%m/%d/')
    site_restoration_image_comment = models.CharField(max_length=100, blank=True, null=True)

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
                engineer_data = InstallationRooftopImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload Site Restoration Images')
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
            task = InstallationRooftopImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class InstallationRooftopImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    hacking_existing_columns_image = models.OneToOneField(HackingExistingColumnsImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    formwork_columns_concrete_pour_curing_image = models.OneToOneField(FormworkColumnsConcretePourCuringImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    delivery_to_site_image = models.OneToOneField(DeliveryToSiteImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    lifting_hoisting_freeissue_image = models.OneToOneField(LiftingHoistingFreeIssueImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    fence_installation_image = models.OneToOneField(FenceInstallationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    site_restoration_image = models.OneToOneField(SiteRestorationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    installation_rooftop_image_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.project_name)

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.user.username for v in self.engineers_atsite.all()]

    def raise_flag(self):
        try:
            kpi_data = Task.objects.get(task_name='Installation Rooftop Image')
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

class ManholeSettingExcavationImage(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    manhole_setting_excavation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/ManholeSettingExcavationImage/%Y/%m/%d/')
    manhole_setting_excavation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/ManholeSettingExcavationImage/%Y/%m/%d/')
    manhole_setting_excavation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/ManholeSettingExcavationImage/%Y/%m/%d/')
    manhole_setting_excavation_image_comment = models.CharField(max_length=100, blank=True, null=True)

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
                engineer_data = ManholeSettingOutConstructionImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload Manhole Setting Excavation Images')
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
            task = ManholeSettingOutConstructionImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class ManholeBlinding(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    manhole_blinding_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/ManholeBlinding/%Y/%m/%d/')
    manhole_blinding_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/ManholeBlinding/%Y/%m/%d/')
    manhole_blinding_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/ManholeBlinding/%Y/%m/%d/')
    manhole_blinding_image_comment = models.CharField(max_length=100, blank=True, null=True)

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
                engineer_data = ManholeSettingOutConstructionImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload Manhole Blinding Images')
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
            task = ManholeSettingOutConstructionImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class ManholeBlockwork(TimeStampModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    manhole_blindingwork_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/ManholeBlockwork/%Y/%m/%d/')
    manhole_blindingwork_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/ManholeBlockwork/%Y/%m/%d/')
    manhole_blindingwork_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/ManholeBlockwork/%Y/%m/%d/')
    manhole_blindingwork_image_comment = models.CharField(max_length=100, blank=True, null=True)

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
                engineer_data = ManholeSettingOutConstructionImage.objects.get(project_name=self.project_name)
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
            kpi_data = SubTask.objects.get(subtask_name='Upload Manhole Blockwork Images')
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
            task = ManholeSettingOutConstructionImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class ManholeSettingOutConstructionImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    manhole_setting_excavation_image = models.OneToOneField(ManholeSettingExcavationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    manhole_blinding_image = models.OneToOneField(ManholeBlinding, on_delete=models.DO_NOTHING, blank=True, null=True)
    manhole_blockwork_image = models.OneToOneField(ManholeBlockwork, on_delete=models.DO_NOTHING, blank=True, null=True)
    manhole_setting_out_construction_image_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.project_name)

    def engineers(self):
        count = self.engineers_atsite.count()
        return "\n , ".join(str(count))

    def names_of_engineers(self):
        return [v.user.username for v in self.engineers_atsite.all()]

    def raise_flag(self):
        try:
            kpi_data = Task.objects.get(task_name='Manhole Setting Out Construction Image')
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

####################################### TOWER & ANTENNA_COAX ###########################################################################################################################


class TowerPaintImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    tower_painting_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/towerpainting/%Y/%m/%d/')
    tower_painting_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/towerpainting/%Y/%m/%d/')
    tower_painting_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/towerpainting/%Y/%m/%d/')
    tower_painting_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
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
            task = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class CableWaysImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    cable_ways_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/cableways/%Y/%m/%d/')
    cable_ways_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/cableways/%Y/%m/%d/')
    cable_ways_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/cableways/%Y/%m/%d/')
    cable_ways_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
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
            task = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class AntennaCoaxInstallImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    antenna_coax_installation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/antennacoaxinstallation/%Y/%m/%d/')
    antenna_coax_installation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/antennacoaxinstallation/%Y/%m/%d/')
    antenna_coax_installation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/antennacoaxinstallation/%Y/%m/%d/')
    antenna_coax_installation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
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
            task = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return

class EarthInstallationImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    earth_Installation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/EarthInstallationImage/%Y/%m/%d/')
    earth_Installation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/EarthInstallationImage/%Y/%m/%d/')
    earth_Installation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/EarthInstallationImage/%Y/%m/%d/')
    earth_Installation_comment = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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
                engineer_data = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
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
            task = TowerAntennaCoaxImage.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return




class TowerAntennaCoaxImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )

    tower_erection = models.OneToOneField(TowerErectionImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_painting = models.OneToOneField(TowerPaintImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    cable_ways = models.OneToOneField(CableWaysImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    cable_installation = models.OneToOneField(CableInstallationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    aviation_lights_installation_image = models.OneToOneField(AviationLightsInstallationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_delivery= models.OneToOneField(TowerDeliveryImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    antenna_coax_installation = models.OneToOneField(AntennaCoaxInstallImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    earth_installation = models.OneToOneField(EarthInstallationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_antenna_coax_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return str(self.project_name)

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


class ProjectPurchaseOrders(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
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
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
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

    def totalProjectCosts(self):
        count = self.objects.all().count()
        return count


class CommercialTeam(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    approved_quote_file = models.FileField(upload_to='files/CommercialTeam/approvedquote/%Y/%m/%d/', blank=True, null=True)
    approved_quote_amount = models.IntegerField(blank=True, null=True)
    po_data = models.OneToOneField(ProjectPurchaseOrders, on_delete=models.CASCADE, blank=True, null=True)
    drawings_revised_approved = models.FileField(upload_to='files/CommercialTeam/drawings_revised_approved/%Y/%m/%d/', blank=True, null=True)
    tower_type_allocated = models.FileField(upload_to='files/CommercialTeam/tower_type_allocated/%Y/%m/%d/', blank=True, null=True)
    material_collection_from_steel_supplier = models.FileField(upload_to='files/CommercialTeam/materia_collection_from_steel_supplier/%Y/%m/%d/', blank=True, null=True)

    customer_issued_quotation = models.FileField(upload_to='files/CommercialTeam/customer_issued_quotation/%Y/%m/%d/', blank=True, null=True)
    project_costing_data = models.OneToOneField(ProjectCosting, on_delete=models.CASCADE, blank=True, null=True)
    initial_invoice = models.FileField(upload_to='files/CommercialTeam/initialinvoice/%Y/%m/%d/', blank=True, null=True)
    initial_invoice_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return str(self.project_name)


####################################### PROCURMENT TEAM ###########################################################################################################################
class ProcurementTeam(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    po_steel = models.FileField(upload_to='files/ProcurementTeam/posteel/%Y/%m/%d/', blank=True, null=True)
    # po_steel_quantity = models.IntegerField(blank=True, null=True)
    po_electrical_materials = models.FileField(upload_to='files/ProcurementTeam/poelectrical/%Y/%m/%d/', blank=True, null=True)
    # po_electrical_materials_quantity = models.IntegerField(blank=True, null=True)
    po_subcontractors = models.FileField(upload_to='files/ProcurementTeam/posubcontractor/%Y/%m/%d/', blank=True, null=True)
    po_subcontractors_amount = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

######################################## END #######################################################################################################################################


class AccessApprovalCivil(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to='files/CivilWorksTeam/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class HealthDocumentsCivilTeam(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/jobhazard/%Y/%m/%d/')
    job_hazard_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/incident/%Y/%m/%d/')
    incident_notification_form_comment = models.CharField(max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/toolbox/%Y/%m/%d/')
    toolbox_meeting_form_comment = models.CharField(max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/communication/%Y/%m/%d/')
    communication_plan_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(AccessApprovalCivil, on_delete=models.CASCADE, blank=True, null=True)
    safety_picture = models.ImageField(upload_to='images/HealthDocumentsCivilTeam/%Y/%m/%d/', blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class CivilWorksTeam(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsCivilTeam, blank=True )
    foundation_and_curing_images = models.OneToOneField(FoundationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    bs241_and_generator_slabs_images = models.OneToOneField(BS241AndGeneatorSlabsImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    site_walling_images_field = models.OneToOneField(BoundaryWallImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_data = models.OneToOneField(TowerAntennaCoaxImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def health_documents_civil(self):
        return [v.project_name for v in self.health_documents.all()]

    def access_approvals(self):
        return [v.project_name for v in self.access_approvals_field.all()]

######################################################3 INSTALLATION TEAM ##################################################################################################################################################################3


class AccessApprovalInstallation(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to='files/InstallationTeam/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class HealthDocumentsInstallationTeam(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/jobhazard/%Y/%m/%d/')
    job_hazard_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/incident/%Y/%m/%d/')
    incident_notification_form_comment = models.CharField(max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/toolbox/%Y/%m/%d/')
    toolbox_meeting_form_comment = models.CharField(max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/communication/%Y/%m/%d/')
    communication_plan_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(AccessApprovalInstallation, on_delete=models.CASCADE, blank=True, null=True)
    safety_picture = models.ImageField(upload_to='images/HealthDocumentsInstallationTeam/%Y/%m/%d/', blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class UndergroundTasks(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    Underground_ducting_and_manholes_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTasks/%Y/%m/%d/', blank=True, null=True)
    Underground_ducting_and_manholes_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTasks/%Y/%m/%d/', blank=True, null=True)
    Underground_ducting_and_manholes_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTasks/%Y/%m/%d/', blank=True, null=True)
    Underground_ducting_and_manholes_images_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = ElectricalTasks.objects.get(project_name=self.project_name)
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
            task = ElectricalTasks.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class ReticulationAPSinstallation(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    Electricalreticulation_APSInstallation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/', blank=True, null=True)
    Electricalreticulation_APSInstallation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/', blank=True, null=True)
    Electricalreticulation_APSInstallation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/', blank=True, null=True)
    Electricalreticulation_APSInstallation_images_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = ElectricalTasks.objects.get(project_name=self.project_name)
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
            task = ElectricalTasks.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class ElectricalEarthing(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    Earthing_connections_and_testing_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    Earthing_connections_and_testing_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    Earthing_connections_and_testing_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    Earthing_connections_and_testing_images_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = ElectricalTasks.objects.get(project_name=self.project_name)
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
            task = ElectricalTasks.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return
###########################################GeneatorSlabsImage#######################################################################################################################

class GenExcavationImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    gen_excation_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/GenExcationImages/'),max_length = 250,blank=True, null=True)
    gen_excation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.generator_image)


class GenConcretePourCuringPeriodImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    gen_concrete_pourcuring_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/GenExcationCuringPeriodImages/'),max_length = 250,blank=True, null=True)
    gen_concrete_pourcuring_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.gen_concrete_pourcuring_image)

class GenCableConduitsSettingImage(TimeStampModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    gen_cable_conduits_setting_image = models.ImageField(upload_to=UploadToProjectDirImage(file_path,'images/CivilWorksTeam/GenCableConduitsImages/'),max_length = 250,blank=True, null=True)
    gen_cable_conduits_setting_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.gen_cable_conduits_setting_image)


###########################################END######################################################################################################################################


class GeneratorInstallation(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    Generator_and_Fuel_Tank_Installation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    Generator_and_Fuel_Tank_Installation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    Generator_and_Fuel_Tank_Installation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    before_fuel_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    before_fuel_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    after_fuel_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    after_fuel_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    Generator_and_Fuel_Tank_Installation_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = ElectricalTasks.objects.get(project_name=self.project_name)
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
            task = ElectricalTasks.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class KPLCSolarImage(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    kplc_solar_installation_image_1 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/', blank=True, null=True)
    kplc_solar_installation_image_2 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/', blank=True, null=True)
    kplc_solar_installation_image_3 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/', blank=True, null=True)
    kplc_solar_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = ElectricalTasks.objects.get(project_name=self.project_name)
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
            task = ElectricalTasks.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class ElectricalTasks(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    Underground_ducting_and_manholes = models.OneToOneField(UndergroundTasks, on_delete=models.CASCADE, blank=True, null=True)
    Electricalreticulation_APSInstallation = models.OneToOneField(ReticulationAPSinstallation, on_delete=models.CASCADE, blank=True, null=True)
    Earthing_connections_and_testing = models.OneToOneField(ElectricalEarthing, on_delete=models.CASCADE, blank=True, null=True)
    Generator_and_Fuel_Tank_Installation = models.OneToOneField(GeneratorInstallation, on_delete=models.CASCADE, blank=True, null=True)
    KPLC_solar_installation = models.OneToOneField(KPLCSolarImage, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
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


class BTSinstallationTask(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    start_date = models.DateTimeField()
    BTSinstallation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Telecom/BTSinstallation/%Y/%m/%d/', blank=True, null=True)
    BTSinstallation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Telecom/BTSinstallation/%Y/%m/%d/', blank=True, null=True)
    BTSinstallation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Telecom/BTSinstallation/%Y/%m/%d/', blank=True, null=True)
    BTSinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = TelecomTasks.objects.get(project_name=self.project_name)
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
            task = TelecomTasks.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class MWInstallationTask(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual, blank=True)
    MWinstallation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Telecom/MWinstallation/%Y/%m/%d/', blank=True, null=True)
    MWinstallation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Telecom/MWinstallation/%Y/%m/%d/', blank=True, null=True)
    MWinstallation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Telecom/MWinstallation/%Y/%m/%d/', blank=True, null=True)
    MWinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

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
                engineer_data = TelecomTasks.objects.get(project_name=self.project_name)
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
            task = TelecomTasks.objects.get(project_name=self.project_name)
            task_id = task.id
            return task_id
        except Exception as e:
            return


class TelecomTasks(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer, blank=True )
    Installation_of_BTS = models.OneToOneField(BTSinstallationTask, on_delete=models.CASCADE, blank=True, null=True)
    Installation_of_MW_links = models.OneToOneField(MWInstallationTask, on_delete=models.CASCADE, blank=True, null=True)
    link_commissioning = models.BooleanField(default=False);
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
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


class Issues(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    issue = models.CharField(max_length=100)
    issue_image = models.ImageField(upload_to='images/InstallationTeam/issues/%Y/%m/%d/', blank=True, null=True)
    issue_sorted_image = models.ImageField(upload_to='images/InstallationTeam/issues/%Y/%m/%d/', blank=True, null=True)
    closed = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.issue


class InstallationTeam(TimeStampModel,TimeTrackModel):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsInstallationTeam, blank=True )
    electrical_tasks_data = models.OneToOneField(ElectricalTasks, on_delete=models.DO_NOTHING, blank=True, null=True)
    telecom_tasks_data = models.OneToOneField(TelecomTasks, on_delete=models.DO_NOTHING, blank=True, null=True)
    as_built = models.FileField(upload_to='files/SafaricomTeam/as_built/%Y/%m/%d/', blank=True, null=True)
    snag_document = models.FileField(upload_to='files/SafaricomTeam/snag/%Y/%m/%d/', blank=True, null=True)
    snag_document_comment = models.CharField(max_length=100, blank=True, null=True)
    issues = models.ManyToManyField(Issues, blank=True)
    conditional_acceptance_cert = models.FileField(upload_to='files/SafaricomTeam/conditionalcert/%Y/%m/%d/', blank=True, null=True)
    conditional_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.project_name)

    def health_documents_installation(self):
        return [v.project_name for v in self.health_documents.all()]

    def access_approvals(self):
        return [v.project_name for v in self.access_approvals_field.all()]

    def project_issues(self):
        return [v.project_name for v in self.issues.all()]


def date_difference(start_date, end_date):
    diff = end_date - start_date
    no_of_days = (diff.days + 1)
    return no_of_days


class WarrantyCertificate(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    civilworks_installation_certificate = models.FileField(upload_to='files/WarrantyCertificates/civilworks/%Y/%m/%d/', blank=True, null=True)
    connectors_torque_certificate = models.FileField(upload_to='files/WarrantyCertificates/connectorsTorque/%Y/%m/%d/', blank=True, null=True)
    safe_to_climb_certificate = models.FileField(upload_to='files/WarrantyCertificates/SafeToClimb/%Y/%m/%d/', blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class TestCetificate(models.Model):
    project_name = models.OneToOneField(BtsSite, on_delete=models.DO_NOTHING)
    cube_test_7days = models.FileField(upload_to='files/TestCertificates/cubetest7/%Y/%m/%d/', blank=True, null=True)
    cube_test_28days = models.FileField(upload_to='files/TestCertificates/cubetest28/%Y/%m/%d/', blank=True, null=True)
    earth_test = models.FileField(upload_to='files/TestCertificates/earthtest/%Y/%m/%d/', blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

def percentage_function(no_of_complete, total_task):
    """Function to return perecentage of progress  """
    percentage = round(((no_of_complete/total_task) * 100))
    return percentage
