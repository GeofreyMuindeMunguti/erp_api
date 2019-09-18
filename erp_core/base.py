from django.db import models
from users.models import *
from .fileshandler.filemixin import UploadToProjectDir
file_path = 'FTTSProjects'

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,blank=True ,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True ,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class TimeTrackModel(models.Model):
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class Project(TimeStampModel):
    project_name = models.CharField(max_length=100,unique=True)
    # PROJECT_TYPE = [('FTTS', 'Fiber FTTS'),('FTTH', 'Fiber FTTH'),('Bts-Con', 'BTS Construction'),]
    # project_type = models.CharField(max_length=225,choices=PROJECT_TYPE,blank=True, null=True)
    description =  models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class Category(TimeStampModel):
    category_name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.category_name

""" FILES """

class CommercialFiles(TimeStampModel):
      # TODO
    quote = models.FileField(upload_to=UploadToProjectDir(file_path,'FTTS/files/Quote/'), blank=True, null=True)
    wayleave_application = models.FileField(upload_to=UploadToProjectDir(file_path,'FTTS/files/wayleave_application/'), blank=True, null=True)
    wayleave_approval = models.FileField( upload_to=UploadToProjectDir(file_path,'FTTS/files/wayleave_approval/'), blank=True, null=True)

    class Meta:
        abstract = True

class ProcurementFiles(TimeStampModel):
      # TODO
    bill_of_materials = models.FileField(upload_to=UploadToProjectDir(file_path,'FTTS/files/BOM/'), blank=True, null=True)
    material_receipt_order = models.FileField(upload_to=UploadToProjectDir(file_path,'FTTS/files/MRO/'), blank=True, null=True)

    class Meta:
        abstract = True
""" END """
