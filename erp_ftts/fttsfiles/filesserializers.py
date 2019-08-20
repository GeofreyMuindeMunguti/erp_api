"""Extract files and images per project.
"""
#---------
# Imports
#---------
from rest_framework import serializers  #, exceptions
from erp_ftts.models import *
from erp_construction.models import SetSiteClearingImage


############################ PROJECT FILES SERIALIZERS ###############################################


class FTTSProjectFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FTTSProject
       # fields = ('ftts_final_acceptance_cert','ftts_accumulated_BOM_survey')

class FttsCommercialTeamFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsCommercialTeam
        fields = ('ftts_quote', 'ftts_po_requisition','ftts_wayleave_application', 'ftts_project_plan', 'ftts_initial_invoice','ftts_po_client',)
       # read_only_fields = ('created_at', 'updated_at', 'is_active')


class SitePoleInstallationFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitePoleInstallation
        fields = ('site_pole_installation_image_1', 'site_pole_installation_image_2','site_pole_installation_image_3',)
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteTrenchingFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteTrenching
        fields = ('site_trenching_image_1', 'site_trenching_image_2','site_trenching_image_3',)
    

class SiteDuctInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteDuctInstallation
        fields = ('site_duct_installation_image_1','site_duct_installation_image_2', 'site_duct_installation_image_3',)
        #read_only_fields = ('created_at', 'updated_at', 'is_active')



################### Main Project Serializer################################

class FttsSiteFilesSerializer(serializers.ModelSerializer):
    
    sitepoleinstallation = SitePoleInstallationFilesSerializer(many = True,read_only=True)
    sitetrenching = SiteTrenchingFilesSerializer(many = True,read_only=True)
    siteductinstallation = SiteDuctInstallationSerializer(many = True,read_only=True)

    class Meta:
        model = FttsSite
        #fields = ('__all__')
       # fields = ('sitetrenching','siteductinstallation','fttscommercialteam','site_name')

        exclude = ("id","site_name","ftts_project","created_at",
           "updated_at", "is_active", "created_by")

        #fields = ('geotech_file','access_letter','approved_drawing','final_acceptance_cert','setsiteclearingimage',
        #'towerbaseimage','bindingimage','steelfixformworkimage','concretepourcuringimage')
        #read_only_fields = ('created_at', 'updated_at', 'is_active')
