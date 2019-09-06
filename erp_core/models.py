from django.db import models
from django.db.models import Sum, F
from django.contrib.auth.models import User
from users.models import *
from erp_core.base import Project as BaseProject
from erp_core.base import *
from erp_construction.models import *
from .fileshandler.filemixin import UploadToProjectDir
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timezone, timedelta
from erp_ftts.models import *
from erp_ftth.models import *

# Create your models here.

"""BTS"""
####################################### BTS KPI ###############################################################################################################################
class Kpi(TimeStampModel):
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.kpi)

######################################## END #######################################################################################################################################

####################################### BTS TASKS ###############################################################################################################################
class Task(TimeStampModel):
    category_name = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    task_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.task_name)

######################################## END #######################################################################################################################################

####################################### BTS SUBTASKS ###############################################################################################################################
class SubTask(TimeStampModel):
    task_name = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    subtask_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subtask_name)

######################################## END #######################################################################################################################################
"""END"""

"""FIBER"""
####################################### BUDGET ########################################################################################################################################

class FiberBudget(TimeStampModel):
    site_name = models.OneToOneField(FttsSite, on_delete=models.DO_NOTHING, blank=True, null=True)
    project_name = models.ForeignKey(FTTHProject, on_delete=models.DO_NOTHING, blank=True, null=True)
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

    def __str__(self):
        return str(self.beneficiary_name)

    def amount(self):
        return float(self.quantity * self.rate)
####################################### END ########################################################################################################################################

####################################### FIBER KPI ###############################################################################################################################
class FiberKpi(TimeStampModel):
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.kpi)

######################################## END #######################################################################################################################################

####################################### TASKS ###############################################################################################################################
class FiberTask(TimeStampModel):
    category_name = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    task_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.task_name)

######################################## END #######################################################################################################################################

####################################### SUBTASKS ###############################################################################################################################
class FiberSubTask(TimeStampModel):
    task_name = models.ForeignKey(FiberTask, on_delete=models.DO_NOTHING)
    subtask_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subtask_name)

######################################## END #######################################################################################################################################
"""END"""



