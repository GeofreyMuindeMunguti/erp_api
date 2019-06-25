from django.db import models
from django.db.models import Sum, F
from django.contrib.auth.models import User
from users.models import *
from inventory.models import *
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone, timedelta
from django.utils.deconstruct import deconstructible

@deconstructible
class UploadToProjectDir(object):
    path = "projects/{0}/{1}{2}"

    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        return self.path.format(instance.project_name, self.sub_path, filename)

#upload_dir = UploadToProjectDir('Projects/images/')

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


class ProjectIcons(models.Model):
    icon = models.ImageField(upload_to=project_directory_path('icoms/images/Project/Icons/'))
    site_owner = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.site_owner


class Project(models.Model):
    project_name = models.CharField(max_length=100, unique=True)
    site_number = models.CharField(max_length=100, unique=True)
    BTS_type = models.CharField(max_length=100)
    site_owner = models.CharField(max_length=100)
    icon = models.ForeignKey(ProjectIcons, on_delete=models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    geotech_file = models.FileField(upload_to=UploadToProjectDir('files/geotech'))
    access_letter = models.FileField(upload_to= UploadToProjectDir('files/accessletter/'))
    approved_drawing = models.FileField(upload_to=UploadToProjectDir('files/approveddrawings/'))
    final_acceptance_cert = models.FileField(upload_to=UploadToProjectDir('/files/SafaricomTeam/finalcert/'), blank=True, null=True)
    final_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name

    def delete(self, *args, **kwargs):
        if self.is_active == False:
            return "Item already deleted"
        else:
            self.is_active is False

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


#######################################START FOUNDATION IMAGES########################################################################################################################################


class SetSiteClearingImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    setting_site_clearing_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/SiteClearing/'))
    setting_site_clearing_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/SiteClearing/'))
    setting_site_clearing_image_3 = models.ImageField(upload_to= UploadToProjectDir('images/SiteClearing/'))
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

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class TowerBaseImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    towerbase_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/TowerBaseImages/'))
    towerbase_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/TowerBaseImages/'))
    towerbase_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/TowerBaseImages/'))
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class BindingImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    binding_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/BindingImages/'))
    binding_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/BindingImages/'))
    binding_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/BindingImages/'))
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class SteelFixFormworkImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    steel_fix_formwork_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/SteelFixFormWorkImages/'))
    steel_fix_formwork_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/SteelFixFormWorkImages/'))
    steel_fix_formwork_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/SteelFixFormWorkImages/'))
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class ConcretePourImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    concrete_pour_curing_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/ConcreatePourCuringImages/'))
    concrete_pour_curing_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/ConcreatePourCuringImages/'))
    concrete_pour_curing_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/ConcreatePourCuringImages/'))
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class ConcreteCuringPeriodImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    concrete_pour_curing_period_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/ConcreatePourCuringPeriodImages/'))
    concrete_pour_curing_period_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/ConcreatePourCuringPeriodImages/'))
    concrete_pour_curing_period_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/ConcreatePourCuringPeriodImages/'))
    concrete_pour_curing_period_comment = models.CharField(max_length=100, blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class FoundationImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
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

######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################


class ExcavationImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    excavation_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/FoundFootPourImages/'))
    excavation_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/FoundFootPourImages/'))
    excavation_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/FoundFootPourImages/'))
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class BS241ConcretePourCuringPeriodImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    bs241_concrete_pour_curing_period_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/Bs241ConcreatePourCuringImages/'))
    bs241_concrete_pour_curing_period_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/Bs241ConcreatePourCuringImages/'))
    bs241_concrete_pour_curing_period_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/Bs241ConcreatePourCuringImages/'))
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class BS241AndGeneatorSlabsImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
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

######################################## END #######################################################################################################################################

####################################### BOUNDARY WALL ###########################################################################################################################


class FoundFootPourImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    foundfootpour_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/FoundFootPourImages/'))
    foundfootpour_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/FoundFootPourImages/'))
    foundfootpour_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/FoundFootPourImages/'))
    foundfootpour_comment = models.CharField(max_length=100, blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class BlockworkPanelConstImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    blockwallpanelconst_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/BlockWallPanelImages/'))
    blockwallpanelconst_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/BlockWallPanelImages/'))
    blockwallpanelconst_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/BlockWallPanelImages/'))
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class GateInstallationImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    gateinstallation_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/GateInstallationImages/'))
    gateinstallation_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/GateInstallationImages/'))
    gateinstallation_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/GateInstallationImages/'))
    gateinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class RazorElectricFenceImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    razorelectricfance_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/RazorElectricalFenceImages/'))
    razorelectricfance_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/RazorElectricalFenceImages/'))
    razorelectricfance_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/RazorElectricalFenceImages/'))
    razorelectricfance_comment = models.CharField(max_length=100, blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class BoundaryWallImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
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


######################################## END #######################################################################################################################################

####################################### TOWER & ANTENNA_COAX ###########################################################################################################################


class TowerErectionImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    tower_erection_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/TowerErectionImages/'))
    tower_erection_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/TowerErectionImages/'))
    tower_erection_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/TowerErectionImages/'))
    tower_erection_comment = models.CharField(max_length=100, blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class TowerPaintImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    tower_painting_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/TowerPaintingImages/'))
    tower_painting_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/TowerPaintingImages/'))
    tower_painting_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/TowerPaintingImages/'))
    tower_painting_comment = models.CharField(max_length=100, blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class CableWaysImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    cable_ways_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/CableWayImages/'))
    cable_ways_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/CableWayImages/'))
    cable_ways_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/CableWayImages/'))
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class AntennaCoaxInstallImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    antenna_coax_installation_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/AntenaCoaxInstallationImages/'))
    antenna_coax_installation_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/AntenaCoaxInstallationImages/'))
    antenna_coax_installation_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/AntenaCoaxInstallationImages/'))
    antenna_coax_installation_comment = models.CharField(max_length=100, blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class TowerAntennaCoaxImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
    tower_erection = models.OneToOneField(TowerErectionImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_painting = models.OneToOneField(TowerPaintImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    cable_ways = models.OneToOneField(CableWaysImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    antenna_coax_installation = models.OneToOneField(AntennaCoaxInstallImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_antenna_coax_comment = models.CharField(max_length=100, blank=True, null=True)
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

######################################## END #######################################################################################################################################

####################################### KPI ###############################################################################################################################


class Kpi(models.Model):
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.kpi)

######################################## END #######################################################################################################################################

####################################### TASKS ###############################################################################################################################


class Task(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    task_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.task_name)



######################################## END #######################################################################################################################################

####################################### SUBTASKS ###############################################################################################################################


class SubTask(models.Model):
    task_name = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    subtask_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.subtask_name)


######################################## END #######################################################################################################################################

####################################### INSTALLATION ###########################################################################################################################


class ProjectPurchaseOrders(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    po_file = models.FileField(upload_to=UploadToProjectDir('files/CommercialTeam/pofile/'), blank=True, null=True)
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
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    project_costing_file = models.FileField(upload_to=UploadToProjectDir('files/CommercialTeam/projectcosting/'), blank=True, null=True)
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


class CommercialTeam(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    approved_quote_file = models.FileField(upload_to=UploadToProjectDir('files/CommercialTeam/approvedquote/'), blank=True, null=True)
    approved_quote_amount = models.IntegerField(blank=True, null=True)
    po_data = models.OneToOneField(ProjectPurchaseOrders, on_delete=models.CASCADE, blank=True, null=True)
    project_costing_data = models.OneToOneField(ProjectCosting, on_delete=models.CASCADE, blank=True, null=True)
    initial_invoice = models.FileField(upload_to=UploadToProjectDir('files/CommercialTeam/initialinvoice/'), blank=True, null=True)
    initial_invoice_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


####################################### PROCURMENT TEAM ###########################################################################################################################
class ProcurementTeam(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    po_steel = models.FileField(upload_to=UploadToProjectDir('files/ProcurementTeam/posteel/'), blank=True, null=True)
    po_steel_quantity = models.IntegerField(blank=True, null=True)
    po_electrical_materials = models.FileField(upload_to=UploadToProjectDir('files/ProcurementTeam/poelectrical/'), blank=True, null=True)
    po_electrical_materials_quantity = models.IntegerField(blank=True, null=True)
    po_subcontractors = models.FileField(upload_to=UploadToProjectDir('files/ProcurementTeam/posubcontractor/'), blank=True, null=True)
    po_subcontractors_amount = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.project_name)

############################ PROCURMENT PO COST  ###################################################################################################################################
    def po_steel_cost(self):
        try:
            steel_cost_data = ProcurementCostTeam.objects.get(item='Po Steel Cost')
            steel_cost = steel_cost_data.unit_price
            total_steel_cost = float(self.po_steel_quantity * steel_cost)
            return total_steel_cost
        except Exception as e:
            error = "Cost Does Not Exist"
            return error

    def po_electrical_material_cost(self):
        try:
            electrial_cost_data = ProcurementCostTeam.objects.get(item='Po Electrical Material Cost')
            elec_material_cost = electrial_cost_data.unit_price
            material_elec_cost = float(self.po_electrical_materials_quantity * elec_material_cost)
            return material_elec_cost
        except Exception as e:
            error = "Cost Does Not Exist"
            return error

    def total_procurpocost(self):
        """Function to return total procurement PO cost"""
        total_procur_cost = float(self.po_steel_cost() + self.po_electrical_material_cost() + self.po_subcontractors_amount)
        return total_procur_cost

######################################## END #######################################################################################################################################


class AccessApprovalCivil(models.Model):
    project_name = models.ForeignKey(Project,related_name= 'accessapprovalcivil', on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to=UploadToProjectDir('files/CivilWorksTeam/accessapproval/'))
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class HealthDocumentsCivilTeam(models.Model):
    project_name = models.ForeignKey(Project,related_name= 'healthdocumentscivilteam' ,on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(upload_to=UploadToProjectDir('files/HealthDocumentsCivilTeam/JobHazard/'))
    job_hazard_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(upload_to=UploadToProjectDir('files/HealthDocumentsCivilTeam/IncidentNotice/'))
    incident_notification_form_comment = models.CharField(max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(upload_to=UploadToProjectDir('files/HealthDocumentsCivilTeam/ToolBox/'))
    toolbox_meeting_form_comment = models.CharField(max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(upload_to=UploadToProjectDir('files/HealthDocumentsCivilTeam/CommunicationPlanForm/'))
    communication_plan_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(AccessApprovalCivil, on_delete=models.CASCADE, blank=True, null=True)
    safety_picture = models.ImageField(upload_to=UploadToProjectDir('images/HealthDocumentsCivilTeam/safetyPictures/'), blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class CivilWorksTeam(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsCivilTeam)
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
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to=UploadToProjectDir('files/InstallationTeam/accessapproval/'))
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class HealthDocumentsInstallationTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(upload_to=UploadToProjectDir('files/HealthDocumentsInstallationTeam/JobHazard/'))
    job_hazard_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(upload_to=UploadToProjectDir('files/HealthDocumentsInstallationTeam/incident/'))
    incident_notification_form_comment = models.CharField(max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(upload_to=UploadToProjectDir('images/files/HealthDocumentsInstallationTeam/toolbox/'))
    toolbox_meeting_form_comment = models.CharField(max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(upload_to=UploadToProjectDir('files/HealthDocumentsInstallationTeam/communication/'))
    communication_plan_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    access_approval = models.OneToOneField(AccessApprovalInstallation, on_delete=models.CASCADE, blank=True, null=True)
    safety_picture = models.ImageField(upload_to=UploadToProjectDir('images/HealthDocumentsInstallationTeam/SafetyPicture/'), blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class UndergroundTasks(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    Underground_ducting_and_manholes_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/UnderGroundDuctingAndManholesImages/'), blank=True, null=True)
    Underground_ducting_and_manholes_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/UnderGroundDuctingAndManholesImages/'), blank=True, null=True)
    Underground_ducting_and_manholes_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/UnderGroundDuctingAndManholesImages/'), blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class ReticulationAPSinstallation(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    Electricalreticulation_APSInstallation_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/ElectricalReticulationImages/'), blank=True, null=True)
    Electricalreticulation_APSInstallation_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/ElectricalReticulationImages/'), blank=True, null=True)
    Electricalreticulation_APSInstallation_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/ElectricalReticulationImages/'), blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class ElectricalEarthing(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    Earthing_connections_and_testing_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/ConnectionAndTestingImages/'), blank=True, null=True)
    Earthing_connections_and_testing_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/ConnectionAndTestingImages/'), blank=True, null=True)
    Earthing_connections_and_testing_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/ConnectionAndTestingImages/'), blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class GeneratorInstallation(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    Generator_and_Fuel_Tank_Installation_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/ConnectionAndTestingImages/'), blank=True, null=True)
    Generator_and_Fuel_Tank_Installation_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/ConnectionAndTestingImages/'), blank=True, null=True)
    Generator_and_Fuel_Tank_Installation_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/ConnectionAndTestingImages/'), blank=True, null=True)
    before_fuel_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/ElectricalFueling/'))
    before_fuel_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/ElectricalFueling/'))
    after_fuel_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/ElectricalFueling/'))
    after_fuel_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/ElectricalFueling/'))
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class KPLCSolarImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    kplc_solar_installation_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/KPLC_Solar/'), blank=True, null=True)
    kplc_solar_installation_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/KPLC_Solar/'), blank=True, null=True)
    kplc_solar_installation_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/KPLC_Solar/'), blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class ElectricalTasks(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
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


class BTSinstallationTask(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    BTSinstallation_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/Telecom/BTSinstallation/'), blank=True, null=True)
    BTSinstallation_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/Telecom/BTSinstallation/'), blank=True, null=True)
    BTSinstallation_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/Telecom/BTSinstallation/'), blank=True, null=True)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class MWInstallationTask(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    MWinstallation_image_1 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/Telecom/MWinstallation/'), blank=True, null=True)
    MWinstallation_image_2 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/Telecom/MWinstallation/'), blank=True, null=True)
    MWinstallation_image_3 = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/Telecom/MWinstallation/'), blank=True, null=True)
    MWinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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
            if bool(self.end_date) is False:
                days_spent = date_difference(self.start_date, self.updated_at)
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


class TelecomTasks(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
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


class Issues(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    issue = models.CharField(max_length=100)
    issue_image = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/issues/'), blank=True, null=True)
    issue_sorted_image = models.ImageField(upload_to=UploadToProjectDir('images/InstallationTeam/issues/'), blank=True, null=True)
    closed = models.BooleanField(default=False)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.issue


class InstallationTeam(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsInstallationTeam)
    electrical_tasks_data = models.OneToOneField(ElectricalTasks, on_delete=models.DO_NOTHING, blank=True, null=True)
    telecom_tasks_data = models.OneToOneField(TelecomTasks, on_delete=models.DO_NOTHING, blank=True, null=True)
    as_built = models.FileField(upload_to=UploadToProjectDir('files/SafaricomTeam/as_built/'), blank=True, null=True)
    signoff = models.FileField(upload_to=UploadToProjectDir('files/SafaricomTeam/signoff/'), blank=True, null=True)
    signoff_comment = models.CharField(max_length=100, blank=True, null=True)
    rfi_document = models.FileField(upload_to=UploadToProjectDir('files/SafaricomTeam/rf/'), blank=True, null=True)
    rfi_document_comment = models.CharField(max_length=100, blank=True, null=True)
    integration_parameter = models.BooleanField(default=False)
    integration_parameter_comment = models.CharField(max_length=100, blank=True, null=True)
    snag_document = models.FileField(upload_to=UploadToProjectDir('files/SafaricomTeam/snag/'), blank=True, null=True)
    snag_document_comment = models.CharField(max_length=100, blank=True, null=True)
    issues = models.ManyToManyField(Issues, blank=True)
    conditional_acceptance_cert = models.FileField(upload_to=UploadToProjectDir('files/SafaricomTeam/conditionalcert/'), blank=True, null=True)
    conditional_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

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
    project_name = project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
<<<<<<< HEAD
    civilworks_installation_certificate = models.FileField(upload_to=project_directory_path('files/WarrantyCertificates/civilworks/'), blank=True, null=True)
    connectors_torque_certificate = models.FileField(upload_to=project_directory_path('files/WarrantyCertificates/civilworks/'), blank=True, null=True)
    safe_to_climb_certificate = models.FileField(upload_to=project_directory_path('files/WarrantyCertificates/civilworks/'), blank=True, null=True)
=======
    civilworks_installation_certificate = models.FileField(upload_to=UploadToProjectDir('files/WarrantyCertificates/civilworks/'), blank=True, null=True)
    connectors_torque_certificate = models.FileField(upload_to=UploadToProjectDir('files/WarrantyCertificates/connectorsTorque/'), blank=True, null=True)
    safe_to_climb_certificate = models.FileField(upload_to=UploadToProjectDir('files/WarrantyCertificates/SafeToClimb/'), blank=True, null=True)
>>>>>>> feat/compressed-files
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class TestCetificate(models.Model):
    project_name = project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
<<<<<<< HEAD
    cube_test_7days = models.FileField(upload_to=project_directory_path('files/TestCertificates/Cubetest7/'), blank=True, null=True)
    cube_test_28days = models.FileField(upload_to=project_directory_path('files/TestCertificates/Cubetest7/'), blank=True, null=True)
    earth_test = models.FileField(upload_to=project_directory_path('files/TestCertificates/Cubetest7/'), blank=True, null=True)
=======
    cube_test_7days = models.FileField(upload_to=UploadToProjectDir('files/TestCertificates/cubetest7/'), blank=True, null=True)
    cube_test_28days = models.FileField(upload_to=UploadToProjectDir('files/TestCertificates/cubetest28/'), blank=True, null=True)
    earth_test = models.FileField(upload_to=UploadToProjectDir('files/TestCertificates/earthtest/'), blank=True, null=True)
>>>>>>> feat/compressed-files
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)