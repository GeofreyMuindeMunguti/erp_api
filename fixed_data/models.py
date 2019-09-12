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
        return f'{self.first_name} {self.second_name}'


class Technology(models.Model):
    tech_name =models.CharField(max_length=150,blank=True ,null=True)

    def __str__(self):
        return f'{self.tech_name}'


class Service(models.Model):
    service_name =models.CharField(max_length=150,blank=True ,null=True)
    technology = ForeignKey(Technology, on_delete=models.CASCADE, related_name="services" ,blank=True ,null=True)

    def __str__(self):
        return f'{self.service_name}-{self.technology}'


class Building(TimeStampModel):
    name =CharField(max_length=150, blank=True ,null=True)
    latitude = CharField(max_length=150,blank=True ,null=True)
    longitude = CharField(max_length=150,blank=True ,null=True)
    building_image_1 = models.ImageField(upload_to='images/Fixed_data/building/', blank=True, null=True)
    building_image_2 = models.ImageField(upload_to='images/Fixed_data/building/', blank=True, null=True)


    def __str__(self):
        return f'{self.name}'


class Link(TimeStampModel):

    circuit_id = IntegerField()
    survey_file = models.FileField(upload_to='files/Fixed_data/surveyfile/', blank=True, null=True)
    service = ForeignKey(Service, on_delete=models.CASCADE, related_name="servicelinks")
    client = ForeignKey(Client, on_delete=models.CASCADE, related_name="links")
    building = ForeignKey(Building, on_delete=models.CASCADE, related_name="links")

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.circuit_id}'

    def technology_id(self):
        try:
            link = Service.objects.get(technology=self.service)
        
            return link.id
        except Exception as e:
            return


    
