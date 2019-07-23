from django.db import models
from erp_core.models import *
#from erp_construction.models import Site
from users.models import *
from erp_core.fileshandler.filemixin import UploadToProjectDir # create Folders(Project name) with images & files per project in /media/..


class FTTHProject(Project):
    initial_kmz = models.FileField(upload_to=UploadToProjectDir('FTTH/files/InitialKMZ/'), blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_acknowledged = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.project_name
