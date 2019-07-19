
# Create your models here.

from django.db import models


from django.db import models
from django_extensions.db.fields import AutoSlugField
from django_extensions.db import fields as extension_fields

class CreateProject(models.Model):
    project_name = models.CharField(max_length=100)
    description = extension_fields.AutoSlugField(populate_from='project_name', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class ProcurementCore(models.Model):
    po = models.CharField(max_length=100)
    description = extension_fields.AutoSlugField(populate_from='project_name', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
