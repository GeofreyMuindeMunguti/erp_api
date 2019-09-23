from django.db import models
from django.contrib.auth.models import User
#from users.models import *
from erp_construction.models import *

############################## PROCUREMENT TEAM #################################################################
class ProcurementCostTeam(models.Model):
    item = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.item)

############################# END ############################################################################
