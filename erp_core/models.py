
# Create your models here.

from django.db import models
from users.models import CustomUser


class CreateProject(models.Model):
    project_name = models.CharField(max_length=100,unique=True, )
    description =  models.CharField(max_length=100, blank=True, null=True)

    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class ProcurementCore(models.Model):
      # TODO
    po = models.CharField(max_length=100)
    description =  models.CharField(max_length=100, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
