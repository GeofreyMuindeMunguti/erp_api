from django.db import models
from erp_core.models import ProcurementFiles
from erp_fibre.models import FTTHProject,FTTSProject

          #####  BTS  PROCUREMENT ########

class BTSProcurementTeam(models.Model):
    ''' All BTS Procurement logic here'''
    #TODO
    def __init_(self) :
        return NotImplementedError


             #####  FTTS  PROCUREMENT ########
class FTTSProcurementTeam(ProcurementFiles):
    project_name = models.OneToOneField(FTTSProject, on_delete=models.DO_NOTHING)
    material_requisition = models.FileField(upload_to='files/MR/mr/%Y/%m/%d/', blank=True, null=True)
    perchase_request = models.FileField(upload_to='files/Quote/quote/%Y/%m/%d/', blank=True, null=True) 
    po_quote_service = models.FileField(upload_to='files/PO/Poservice/%Y/%m/%d/', blank=True, null=True)
    po_subcontractors = models.FileField(upload_to='files/PO/PoSubCon/%Y/%m/%d/', blank=True, null=True)
    



            #####  FTTS  PROCUREMENT ########

class FTTHProcurementTeam(ProcurementFiles):
    project_name = models.OneToOneField(FTTHProject, on_delete=models.DO_NOTHING)
    ten_per_cent_invoice = models.FileField(upload_to='files/Invoice/invoice/%Y/%m/%d/', blank=True, null=True) #

    # material_receipt_order = models.FileField(upload_to='files/BRO/bro/%Y/%m/%d/', blank=True, null=True) #ftts

    # description =  models.CharField(max_length=100, blank=True, null=True)
    
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # is_active = models.BooleanField(default=True)