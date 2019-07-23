from django.db import models
from erp_core.models import CreateProject
from erp_construction.models import Project
from users.models import CustomUser
from erp_core.fileshandler.filemixin import UploadToProjectDir  # create Folders(Project name) with images & files per project in /media/..



class FTTSProject(CreateProject):
    site_name = models.ManyToManyField(Project, blank=True)#, null=True)
    

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.project_name

