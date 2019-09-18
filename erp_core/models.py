from django.db import models
from django.db.models import Sum, F
from django.contrib.auth.models import User
from users.models import *
from erp_core.base import Project as BaseProject
from erp_core.base import *
from erp_construction.models import *
from .fileshandler.filemixin import UploadToProjectDir
from django.contrib.postgres.fields import ArrayField
from datetime import datetime,  timedelta
from erp_ftts.models import *
from erp_ftth.models import *

# Create your models here.

"""BTS"""
####################################### BTS KPI ###############################################################################################################################
class Kpi(TimeStampModel):
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.kpi)

######################################## END #######################################################################################################################################

####################################### BTS TASKS ###############################################################################################################################
class Task(TimeStampModel):
    category_name = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    task_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.task_name)

######################################## END #######################################################################################################################################

####################################### BTS SUBTASKS ###############################################################################################################################
class SubTask(TimeStampModel):
    task_name = models.ForeignKey(Task, on_delete=models.DO_NOTHING, blank=True, null=True)
    subtask_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subtask_name)

######################################## END #######################################################################################################################################
"""END"""
