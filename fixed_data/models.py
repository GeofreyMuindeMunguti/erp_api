from django.conf import settings
from django.db import models
from django.db import models as models
from erp_core.base import TimeStampModel



class Client(TimeStampModel):
    first_name =models.CharField(max_length=150)
    second_name =models.CharField(max_length=150)
    email =models.EmailField(max_length= 150)
   
    phone_no = models.PositiveIntegerField()

    created_by = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING, related_name="clients",blank=True ,null=True)

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
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name="services" ,blank=True ,null=True)

    def __str__(self):
        return f'{self.service_name}-{self.technology}'


class Building(TimeStampModel):
    name =models.CharField(max_length=150, blank=True ,null=True)
    latitude = models.CharField(max_length=150,blank=True ,null=True)
    longitude = models.CharField(max_length=150,blank=True ,null=True)
    building_image_1 = models.ImageField(upload_to='images/Fixed_data/building/', blank=True, null=True)
    building_image_2 = models.ImageField(upload_to='images/Fixed_data/building/', blank=True, null=True)
    fiber_ready = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Link(TimeStampModel):

    circuit_id = models.IntegerField(unique=True)
    survey_file = models.FileField(upload_to='files/Fixed_data/surveyfile/', blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="servicelinks")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="links")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="links")
    decomisioned = models.BooleanField(default=False)

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


class WiMaxtestCriteria(TimeStampModel):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="mimaxctriteria", blank=True, null=True)#reduntant
    wan_ip = models.GenericIPAddressField(blank=True,null=True)
    #radio_param = models.ForeignKey('RadioParam')
    dbm = models.IntegerField(blank =True ,null=True)
    snir = models.IntegerField(blank =True ,null=True)
    connecting_bts = models.CharField(max_length=150,blank=True ,null=True)###FK
    image = models.FileField(upload_to='files/Fixed_data/Winax/', blank=True, null=True)
    
    router_model = models.IntegerField(blank =True ,null=True)
    router_SNMP_CMP_enable = models.BooleanField(default=False)
    power_status= models.BooleanField(default=True)


    def __str__(self):
        return f'Test Criteria for {self.link}'


class Consumable(TimeStampModel):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="consumables",blank=True ,null=True)
    item = models.CharField(max_length=250 ,blank=True ,null=True)
    quantity =models.FloatField(default=0)
    unit_price =models.FloatField(blank=True,null=True)


    def __str__(self):
        return f'Consumable for {self.link}'

class WiMaxInstallation(TimeStampModel):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="mwpmaintenance",blank=True ,null=True)
    test_criteria =models.OneToOneField(WiMaxtestCriteria, on_delete=models.CASCADE, related_name="mwinstallations")
    consumable = models.ForeignKey(Consumable, on_delete=models.CASCADE, related_name="mwinstallation",blank=True ,null=True)

    def __str__(self):
        return f'{self.link}'


class WiMaxPMaintenance(TimeStampModel):
    link = models.ForeignKey(WiMaxInstallation, on_delete=models.CASCADE, related_name="mwpmaintenance",blank=True ,null=True)
    test_criteria =models.ForeignKey(WiMaxtestCriteria, on_delete=models.CASCADE, related_name="mwpmaintenances",blank=True ,null=True)
    consumable = models.ForeignKey(Consumable, on_delete=models.CASCADE, related_name="mwpmaintenamce",blank=True ,null=True)


    def __str__(self):
        return f'{self.link}'

    class Meta:
        unique_together = (['link', 'test_criteria',])

    
class Support(TimeStampModel):
    link = models.ForeignKey(WiMaxInstallation, on_delete=models.CASCADE, related_name="supports",blank=True ,null=True)
    issue = models.CharField(max_length=250 ,blank=True ,null=True)
    resolution = models.CharField(max_length=250 ,blank=True ,null=True)
    fiber_ready  = models.BooleanField(default=False)
    remacks = models.CharField(max_length=250 ,blank=True ,null=True)

    
    def __str__(self):
        return f'{self.link}'