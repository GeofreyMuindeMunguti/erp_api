from django.db import models
from erp_core.models import CommercialFiles
from erp_fibre.models import FTTHProject,FTTSProject

          #####  BTS  COMMERCIAL ########

class BTSCommercialTeam(models.Model):
    ''' All BTS commercial logic here'''
    #TODO
    def __init_(self) :
        return NotImplementedError


             #####  FTTS  COMMERCIAL ########
class FTTSCommercialTeam(CommercialFiles):
    project_name = models.OneToOneField(FTTSProject, on_delete=models.DO_NOTHING)
    project_plan = models.FileField(upload_to='files/Project/Projectplan/%Y/%m/%d/', blank=True, null=True) 
    fiber_requisition = models.FileField(upload_to='files/PO/Poservice/%Y/%m/%d/', blank=True, null=True)
    po_subcontractors = models.FileField(upload_to='files/PO/PoSubCon/%Y/%m/%d/', blank=True, null=True)
    fiber_po_client =models.FileField(upload_to='files/PO/PoSubCon/%Y/%m/%d/', blank=True, null=True)
    quote = models.FileField(upload_to='files/Quote/quote/%Y/%m/%d/', blank=True, null=True) # ftts & ftth
    approval = models.BooleanField(default=False)



            #####  FTTS  COMMERCIAL ########

class FTTHCommercialTeam(CommercialFiles):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.DO_NOTHING)
    bill_of_qualities = models.FileField(upload_to='files/BOQ/boq/%Y/%m/%d/', blank=True, null=True) #
    