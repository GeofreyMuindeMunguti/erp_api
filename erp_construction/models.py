from django.db import models
from django.db.models import Sum, F
from django.contrib.auth.models import User
from users.models import CustomUser, Location, Casual, Engineer, Rates
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


class ProjectIcons(models.Model):
    icon = models.ImageField(upload_to='images/Project/Icons/%Y/%m/%d/')
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
    geotech_file = models.FileField(upload_to='files/Project/geotech/%Y/%m/%d/')
    access_letter = models.FileField(upload_to='files/Project/accessletters/%Y/%m/%d/')
    approved_drawing = models.FileField(upload_to='files/Project/approveddrawings/%Y/%m/%d/')
    final_acceptance_cert = models.FileField(upload_to='files/SafaricomTeam/finalcert/%Y/%m/%d/', blank=True, null=True)
    final_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name

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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class TowerBaseImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class BindingImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class SteelFixFormworkImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class ConcretePourCuringImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class FoundationImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
    setting_site_clearing = models.OneToOneField(SetSiteClearingImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    excavation_tower_base = models.OneToOneField(TowerBaseImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    binding = models.OneToOneField(BindingImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    steel_fix_formwork = models.OneToOneField(SteelFixFormworkImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    concrete_pour_curing = models.OneToOneField(ConcretePourCuringImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    foundation_and_curing_comment = models.CharField(max_length=100, blank=True, null=True)
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

######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################


class ExcavationImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
            try:
                engineer_data = BTSAndGeneatorSlabsImage.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error


class ConcretePourCuringPeriodImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    concrete_pour_curing_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/')
    concrete_pour_curing_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/')
    concrete_pour_curing_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/ConcretePourCuringPeriod/%Y/%m/%d/')
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
            try:
                engineer_data = BTSAndGeneatorSlabsImage.objects.get(project_name=self.project_name)
                count = engineer_data.engineers_atsite.count()
                cost = (count * engineer_rate * days_spent)
                return cost
            except Exception as e:
                error = "No engineers assigned to project"
                return error
        except Exception as e:
            error = "Rates does not exist"
            return error


class BTSAndGeneatorSlabsImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
    foundation_foot_pouring = models.OneToOneField(ExcavationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    concrete_pour_period = models.OneToOneField(ConcretePourCuringPeriodImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    bts_and_generator_slabs_comment = models.CharField(max_length=100, blank=True, null=True)
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

######################################## END #######################################################################################################################################

####################################### BOUNDARY WALL ###########################################################################################################################


class FoundFootPourImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    foundfootpour_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    foundfootpour_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
    foundfootpour_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/FoundFootPour/%Y/%m/%d/')
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class BlockworkPanelConstImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class GateInstallationImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    gateinstallation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/GateInstallation/%Y/%m/%d/')
    gateinstallation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/GateInstallation/%Y/%m/%d/')
    gateinstallation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/GateInstallation/%Y/%m/%d/')
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class RazorElectricFenceImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    razorelectricfance_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/RazorElectricFence/%Y/%m/%d/')
    razorelectricfance_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/RazorElectricFence/%Y/%m/%d/')
    razorelectricfance_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/RazorElectricFence/%Y/%m/%d/')
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class BoundaryWallImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
    foundation_foot_pouring = models.OneToOneField(FoundFootPourImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    block_construction = models.OneToOneField(BlockworkPanelConstImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    gate_installation = models.OneToOneField(GateInstallationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    razor_electric_fence = models.OneToOneField(RazorElectricFenceImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    boundary_wall_comment = models.CharField(max_length=100, blank=True, null=True)
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

######################################## END #######################################################################################################################################

####################################### TOWER & ANTENNA_COAX ###########################################################################################################################


class TowerErectionImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    tower_erection_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/towererection/%Y/%m/%d/')
    tower_erection_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/towererection/%Y/%m/%d/')
    tower_erection_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/towererection/%Y/%m/%d/')
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class TowerPaintImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    tower_painting_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/towerpainting/%Y/%m/%d/')
    tower_painting_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/towerpainting/%Y/%m/%d/')
    tower_painting_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/towerpainting/%Y/%m/%d/')
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class CableWaysImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class AntennaCoaxInstallImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    antenna_coax_installation_image_1 = models.ImageField(upload_to='images/CivilWorksTeam/antennacoaxinstallation/%Y/%m/%d/')
    antenna_coax_installation_image_2 = models.ImageField(upload_to='images/CivilWorksTeam/antennacoaxinstallation/%Y/%m/%d/')
    antenna_coax_installation_image_3 = models.ImageField(upload_to='images/CivilWorksTeam/antennacoaxinstallation/%Y/%m/%d/')
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
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class TowerAntennaCoaxImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
    tower_erection = models.OneToOneField(TowerErectionImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_painting = models.OneToOneField(TowerPaintImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    cable_ways = models.OneToOneField(CableWaysImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    antenna_coax_installation = models.OneToOneField(AntennaCoaxInstallImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    tower_antenna_coax_comment = models.CharField(max_length=100, blank=True, null=True)
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
    task_name = models.CharField(blank=True, null=True, max_length=150)
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
    subtask_name = models.CharField(blank=True, null=True, max_length=150)
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
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
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


class CommercialTeam(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    approved_quote_file = models.FileField(upload_to='files/CommercialTeam/approvedquote/%Y/%m/%d/', blank=True, null=True)
    approved_quote_amount = models.IntegerField(blank=True, null=True)
    po_data = models.OneToOneField(ProjectPurchaseOrders, on_delete=models.CASCADE, blank=True, null=True)
    project_costing_data = models.OneToOneField(ProjectCosting, on_delete=models.CASCADE, blank=True, null=True)
    initial_invoice = models.FileField(upload_to='files/CommercialTeam/initialinvoice/%Y/%m/%d/', blank=True, null=True)
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
    po_steel = models.FileField(upload_to='files/ProcurementTeam/posteel/%Y/%m/%d/', blank=True, null=True)
    po_steel_cost = models.IntegerField(blank=True, null=True)
    po_electrical_materials = models.FileField(upload_to='files/ProcurementTeam/poelectrical/%Y/%m/%d/', blank=True, null=True)
    po_electrical_materials_cost = models.IntegerField(blank=True, null=True)
    po_subcontractors = models.FileField(upload_to='files/ProcurementTeam/posubcontractor/%Y/%m/%d/', blank=True, null=True)
    po_subcontractors_cost = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


######################################## END #######################################################################################################################################

class HealthDocumentsCivilTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/jobhazard/%Y/%m/%d/')
    job_hazard_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/incident/%Y/%m/%d/')
    incident_notification_form_comment = models.CharField(max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/toolbox/%Y/%m/%d/')
    toolbox_meeting_form_comment = models.CharField(max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(upload_to='files/HealthDocumentsCivilTeam/communication/%Y/%m/%d/')
    communication_plan_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class AccessApprovalCivil(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to='files/CivilWorksTeam/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class CivilWorksTeam(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsCivilTeam)
    access_approvals_field = models.ManyToManyField(AccessApprovalCivil)
    foundation_and_curing_images = models.OneToOneField(FoundationImage, on_delete=models.DO_NOTHING, blank=True, null=True)
    bts_and_generator_slabs_images = models.OneToOneField(BTSAndGeneatorSlabsImage, on_delete=models.DO_NOTHING, blank=True, null=True)
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


class HealthDocumentsInstallationTeam(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    job_hazard_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/jobhazard/%Y/%m/%d/')
    job_hazard_form_comment = models.CharField(max_length=100, blank=True, null=True)
    incident_notification_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/incident/%Y/%m/%d/')
    incident_notification_form_comment = models.CharField(max_length=100, blank=True, null=True)
    toolbox_meeting_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/toolbox/%Y/%m/%d/')
    toolbox_meeting_form_comment = models.CharField(max_length=100, blank=True, null=True)
    communication_plan_form = models.FileField(upload_to='files/HealthDocumentsInstallationTeam/communication/%Y/%m/%d/')
    communication_plan_form_comment = models.CharField(max_length=100, blank=True, null=True)
    health_documents_comment = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class AccessApprovalInstallation(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    access_approval = models.FileField(upload_to='files/InstallationTeam/accessapproval/%Y/%m/%d/')
    access_approval_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


class UndergroundTasks(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    Underground_ducting_and_manholes_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTasks/%Y/%m/%d/', blank=True, null=True)
    Underground_ducting_and_manholes_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTasks/%Y/%m/%d/', blank=True, null=True)
    Underground_ducting_and_manholes_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/UndergroundTasks/%Y/%m/%d/', blank=True, null=True)
    Underground_ducting_and_manholes_images_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class ReticulationAPSinstallation(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    Electricalreticulation_APSInstallation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/', blank=True, null=True)
    Electricalreticulation_APSInstallation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/', blank=True, null=True)
    Electricalreticulation_APSInstallation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ReticulationAPSinstallation/%Y/%m/%d/', blank=True, null=True)
    Electricalreticulation_APSInstallation_images_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class ElectricalEarthing(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    Earthing_connections_and_testing_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    Earthing_connections_and_testing_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    Earthing_connections_and_testing_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    Earthing_connections_and_testing_images_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class GeneratorInstallation(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    Generator_and_Fuel_Tank_Installation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    Generator_and_Fuel_Tank_Installation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    Generator_and_Fuel_Tank_Installation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Electrical/ElectricalEarthing/%Y/%m/%d/', blank=True, null=True)
    before_fuel_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    before_fuel_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    after_fuel_image_1 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    after_fuel_image_2 = models.ImageField(upload_to='images/InstallationTeam/Electrical/Fueling/%Y/%m/%d/')
    Generator_and_Fuel_Tank_Installation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class KPLCSolarImage(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    kplc_solar_installation_image_1 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/', blank=True, null=True)
    kplc_solar_installation_image_2 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/', blank=True, null=True)
    kplc_solar_installation_image_3 = models.ImageField(upload_to='images/InstallationTeam/KPLCSolar/%Y/%m/%d/', blank=True, null=True)
    kplc_solar_installation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class ElectricalTasks(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
    Underground_ducting_and_manholes = models.OneToOneField(UndergroundTasks, on_delete=models.CASCADE, blank=True, null=True)
    Electricalreticulation_APSInstallation = models.OneToOneField(ReticulationAPSinstallation, on_delete=models.CASCADE, blank=True, null=True)
    Earthing_connections_and_testing = models.OneToOneField(ElectricalEarthing, on_delete=models.CASCADE, blank=True, null=True)
    Generator_and_Fuel_Tank_Installation = models.OneToOneField(GeneratorInstallation, on_delete=models.CASCADE, blank=True, null=True)
    KPLC_solar_installation = models.OneToOneField(KPLCSolarImage, on_delete=models.CASCADE, blank=True, null=True)
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


class BTSinstallationTask(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    BTSinstallation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Telecom/BTSinstallation/%Y/%m/%d/', blank=True, null=True)
    BTSinstallation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Telecom/BTSinstallation/%Y/%m/%d/', blank=True, null=True)
    BTSinstallation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Telecom/BTSinstallation/%Y/%m/%d/', blank=True, null=True)
    BTSinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class MWInstallationTask(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    no_of_casuals_atsite = models.ManyToManyField(Casual)
    start_date = models.DateTimeField()
    MWinstallation_image_1 = models.ImageField(upload_to='images/InstallationTeam/Telecom/MWinstallation/%Y/%m/%d/', blank=True, null=True)
    MWinstallation_image_2 = models.ImageField(upload_to='images/InstallationTeam/Telecom/MWinstallation/%Y/%m/%d/', blank=True, null=True)
    MWinstallation_image_3 = models.ImageField(upload_to='images/InstallationTeam/Telecom/MWinstallation/%Y/%m/%d/', blank=True, null=True)
    MWinstallation_comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)

    def no_of_casuals(self):
        count = self.no_of_casuals_atsite.count()
        return "\n , ".join(str(count))

    def names_of_casuals(self):
        return [v.casual_last_name for v in self.no_of_casuals_atsite.all()]

    def casuals_cost(self):
        try:
            rate_data = Rates.objects.get(worker_type='Casual')
            casual_rate = rate_data.rate
            days_spent = date_difference(self.start_date, self.updated_at)
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
            days_spent = date_difference(self.start_date, self.updated_at)
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


class TelecomTasks(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    engineers_atsite = models.ManyToManyField(Engineer)
    Installation_of_BTS = models.OneToOneField(BTSinstallationTask, on_delete=models.CASCADE, blank=True, null=True)
    Installation_of_MW_links = models.OneToOneField(MWInstallationTask, on_delete=models.CASCADE, blank=True, null=True)
    link_commissioning = models.BooleanField(default=False);
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


class InstallationTeam(models.Model):
    project_name = models.OneToOneField(Project, on_delete=models.DO_NOTHING)
    health_documents = models.ManyToManyField(HealthDocumentsInstallationTeam)
    access_approvals_field = models.ManyToManyField(AccessApprovalInstallation)
    electrical_tasks_data = models.OneToOneField(ElectricalTasks, on_delete=models.DO_NOTHING, blank=True, null=True)
    telecom_tasks_data = models.OneToOneField(TelecomTasks, on_delete=models.DO_NOTHING, blank=True, null=True)
    as_built = models.FileField(upload_to='files/SafaricomTeam/as_built/%Y/%m/%d/', blank=True, null=True)
    signoff = models.FileField(upload_to='files/SafaricomTeam/signoff/%Y/%m/%d/', blank=True, null=True)
    signoff_comment = models.CharField(max_length=100, blank=True, null=True)
    rfi_document = models.FileField(upload_to='files/SafaricomTeam/rf/%Y/%m/%d/', blank=True, null=True)
    rfi_document_comment = models.CharField(max_length=100, blank=True, null=True)
    integration_parameter = models.BooleanField(default=False)
    integration_parameter_comment = models.CharField(max_length=100, blank=True, null=True)
    snag_document = models.FileField(upload_to='files/SafaricomTeam/snag/%Y/%m/%d/', blank=True, null=True)
    snag_document_comment = models.CharField(max_length=100, blank=True, null=True)
    conditional_acceptance_cert = models.FileField(upload_to='files/SafaricomTeam/conditionalcert/%Y/%m/%d/', blank=True, null=True)
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


def date_difference(start_date, end_date):
    diff = end_date - start_date
    no_of_days = (diff.days + 1)
    return no_of_days
