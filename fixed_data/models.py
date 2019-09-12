from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import IntegerField
from django.db.models import PositiveIntegerField
from django.db.models import ForeignKey
from django.conf import settings
from django.db import models
#from django.db import models as models
from erp_core.base import TimeStampModel



class Client(TimeStampModel):
    first_name =models.CharField(max_length=150)
    second_name =models.CharField(max_length=150)
    email =models.EmailField(max_length= 150)
   
    phone_no = PositiveIntegerField()

    created_by = ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING, related_name="clients" )

    class Meta:
        ordering = ('-created_by',)

    def __str__(self):
        return f'Client Name :{self.first_name} {self.second_name}'


class Technology(models.Model):
    tech_name =models.CharField(max_length=150)

    def __str__(self):
        return f'{self.tech_name}'


class Service(models.Model):
    service_name =models.CharField(max_length=150)
    technology = ForeignKey(Technology, on_delete=models.CASCADE, related_name="services" )

    def __str__(self):
        return f'Service:{self.service_name},Technology:{self.technology}'


class Building(TimeStampModel):
    name =CharField(max_length=150, blank=True ,null=True)
    latitude = CharField(max_length=150)
    longitude = CharField(max_length=150)


    def __unicode__(self):
        return f'{self.name}'


class Link(TimeStampModel):

    circuit_id = IntegerField()
    
    service = ForeignKey(Service, on_delete=models.CASCADE, related_name="servicelinks")
    client = ForeignKey(Client, on_delete=models.CASCADE, related_name="links")

    building = ForeignKey(Building, on_delete=models.CASCADE, related_name="links")

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.pk}'
