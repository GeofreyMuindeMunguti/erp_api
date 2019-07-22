
# Create your models here.

from django.db import models
from users.models import CustomUser


class Project(models.Model):
    site_name = models.CharField(max_length=100,unique=True, blank=True, null=True)
    description =  models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True



class CommercialFiles(models.Model):
      # TODO
    quote = models.FileField(upload_to='files/Quote/quote/%Y/%m/%d/', blank=True, null=True) # ftts & ftth
    wayleave_application = models.FileField(upload_to='files/WayLeave/wayleave/%Y/%m/%d/', blank=True, null=True) # ftts & ftth
    wayleave_approval = models.FileField(upload_to='files/WayLeave/wayleave/%Y/%m/%d/', blank=True, null=True) # ftts & ftth

    description =  models.CharField(max_length=100, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ProcurementFiles(models.Model):
      # TODO
    bill_of_materials = models.FileField(upload_to='files/BOM/bom/%Y/%m/%d/', blank=True, null=True) # ftts & ftth
    material_receipt_order = models.FileField(upload_to='files/BRO/bro/%Y/%m/%d/', blank=True, null=True) #ftts

    description =  models.CharField(max_length=100, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True