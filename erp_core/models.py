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

# Create your models here.


class MainSite(TimeStampModel):
    site_name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE, related_name="mainsites", blank=True, null=True )

    class Meta:
        ordering = ('-pk',)


    def __str__(self):
        return str(self.site_name)


####################################### KPI ###############################################################################################################################
class Kpi(TimeStampModel):
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.kpi)

######################################## END #######################################################################################################################################

####################################### TASKS ###############################################################################################################################
class Task(TimeStampModel):
    category_name = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    task_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.task_name)

######################################## END #######################################################################################################################################

####################################### SUBTASKS ###############################################################################################################################
class SubTask(TimeStampModel):
    task_name = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    subtask_name = models.CharField(blank=True, null=True, max_length=150, unique=True)
    kpi = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subtask_name)

######################################## END #######################################################################################################################################
