from django.db import models
from erp_core.models import CreateProject
from erp_construction.models import Project


################### FTTS BLOCK  #####################


class FTTSProject(CreateProject):
    #sites = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=True, null=True)
    sites = models.ManyToManyField(Project, blank=True)#, null=True)

        # Below are Fields from Absrtact class as addition to above sites field # NOTE  can be overriden

    #project_name = models.CharField(max_length=100)
    #description = extension_fields.AutoSlugField(populate_from='project_name', blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    #is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.project_name

    # def get_absolute_url(self):
    #     return reverse('erpProject_fttsproject_detail', args=(self.pk,))


    # def get_update_url(self):
    #     return reverse('erpProject_fttsproject_update', args=(self.pk,))




#################### FTTH MODELS ####################

class FTTHProject(CreateProject):
    initial_kmz = models.FileField(upload_to='files/FTTHProject/Initial_kmz_file/%Y/%m/%d/', blank=True, null=True)
    is_acknowledged = models.BooleanField(default=False)

         # Below are Fields from Absrtact class on addition of above kmz and ACK fields # NOTE  can be overriden

    #project_name = models.CharField(max_length=100)
    #description = extension_fields.AutoSlugField(populate_from='project_name', blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    #is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.project_name

    # def get_absolute_url(self):
    #     return reverse('erpProject_ftthproject_detail', args=(self.pk,))


    # def get_update_url(self):
    #     return reverse('erpProject_ftthproject_update', args=(self.pk,))
