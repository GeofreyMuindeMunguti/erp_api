from django.db import models



class Client(models.Model):
    first_name =models.CharField(max_length=150)
    second_name =models.CharField(max_length=150)
    email =models.EmailField(max_length= 150)
    phone_no = models.PositiveIntegerField()

    created_by = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    

class Service(models.Model):
    pass

class Building(models.Model):
    pass

class Link(models.Model):
    circuit_id = models.IntegerField()
    ip_address = models.GenericIPAddressField()  #take str format e.g. 192.0.2.30 or 2a02:42fe::4

    service = models.ForeignKey('Service',on_delete =models.CASCADE)
    client = models.ForeignKey(Client ,on_delete =models.DO_NOTHING)
    building = models.ForeignKey( 'Building' ,on_delete =models.DO_NOTHING)




    






