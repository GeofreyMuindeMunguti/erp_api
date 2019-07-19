from django.db import models
from erp_core.models import CreateProject
from erp_construction.models import Project
from users.models import CustomUser

################### FTTS BLOCK  #####################


class FTTSProject(CreateProject):
    sites = models.ManyToManyField(Project, blank=True)#, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.project_name



#################### FTTH MODELS ####################

class FTTHProject(CreateProject):
    initial_kmz = models.FileField(upload_to='files/FTTHProject/Initial_kmz_file/%Y/%m/%d/', blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_acknowledged = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.project_name
