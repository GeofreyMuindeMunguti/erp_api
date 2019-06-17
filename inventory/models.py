from django.db import models
from django.contrib.auth.models import User
from users.models import *
from erp_construction.models import *

# 
# PO_STEEL_COST_CHOICES = [
#     ('1 - 49kg': 10,000ksh),
#     ('50 - 99kg': 20,000ksh),
#     ('100 - 199kg': 30,000ksh),
#     ('200 - 299kg': 40,000ksh),
#     ]
#
# class PoSteelCost(models.Model):
#     po_steel_cost = models.CharField(max_length=120, choices=PO_STEEL_COST_CHOICES)
#
