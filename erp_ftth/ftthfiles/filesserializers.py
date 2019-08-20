"""Extract files and images per project.
"""
#---------
# Imports
#---------
from rest_framework import serializers  #, exceptions
from erp_ftts.models import *


############################ PROJECT FILES SERIALIZERS ###############################################


class SiteClearingFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SetSiteClearingImage
        fields = ('setting_site_clearing_image_1','setting_site_clearing_image_2','setting_site_clearing_image_3',)



class AccessApprovalFileInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessApprovalInstallation
        fields = ('access_approval',)
        read_only_fields = ('created_at', 'updated_at', 'is_active')




################### Main Project Serializer################################

class BtsSiteFilesSerializer(serializers.ModelSerializer):



    setsiteclearingimage = SiteClearingFilesSerializer ( read_only =True)
  
    accessapprovalinstallation = AccessApprovalFileInstallationSerializer(many = True,read_only=True)

 

    class Meta:
        model = FttsSite
       # fields = ('__all__')
        exclude = ("id","project_name","site_number","BTS_type","site_owner","final_acceptance_cert_comment","created_at",
           "updated_at", "is_active", "location", "created_by")

        #fields = ('geotech_file','access_letter','approved_drawing','final_acceptance_cert','setsiteclearingimage',
        #'towerbaseimage','bindingimage','steelfixformworkimage','concretepourcuringimage')
        #read_only_fields = ('created_at', 'updated_at', 'is_active')
