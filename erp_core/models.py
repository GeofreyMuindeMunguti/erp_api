
# Create your models here.

from django.db import models
from users.models import *
from .fileshandler.filemixin import UploadToProjectDir

class Project(models.Model):
    project_name = models.CharField(max_length=100,unique=True, blank=True, null=True)
    description =  models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True



class CommercialFiles(models.Model):
      # TODO
    quote = models.FileField(upload_to=UploadToProjectDir('FTTS/files/Quote/'), blank=True, null=True)
    wayleave_application = models.FileField(upload_to=UploadToProjectDir('FTTS/files/wayleave_application/'), blank=True, null=True)
    wayleave_approval = models.FileField( upload_to=UploadToProjectDir('FTTS/files/wayleave_approval/'), blank=True, null=True)

    description =  models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ProcurementFiles(models.Model):
      # TODO
    bill_of_materials = models.FileField(upload_to=UploadToProjectDir('FTTS/files/BOM/'), blank=True, null=True)
    material_receipt_order = models.FileField(upload_to=UploadToProjectDir('FTTS/files/MRO/'), blank=True, null=True)

    description =  models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
