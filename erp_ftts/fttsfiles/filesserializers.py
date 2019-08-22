"""Extract files and images per project.
"""
#---------
# Imports
#---------
from rest_framework import serializers  #, exceptions
from erp_ftts.models import *


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
        fields = ('site_pole_installation_image_1', 'site_pole_installation_image_2','site_pole_installation_image_3','site_pole_installation_comment',)
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteTrenchingFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteTrenching
        fields = ('site_trenching_image_1', 'site_trenching_image_2','site_trenching_image_3','site_trenching_comment',)


class SiteDuctInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteDuctInstallation
        fields = ('site_duct_installation_image_1','site_duct_installation_image_2', 'site_duct_installation_image_3','site_duct_installation_comment',)

class SiteDuctInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteDuctInstallation
        fields = ('site_duct_installation_image_1','site_duct_installation_image_2', 'site_duct_installation_image_3','site_duct_installation_comment',)

class ManHoleInstallationFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ManHoleInstallation
        fields = ('site_manhole_installation_image_1','site_duct_installation_image_2', 'site_duct_installation_image_3','site_duct_installation_comment','manhole_comment',)


class SiteCableInstallationFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteCableInstallation
        fields = ('site_cable_installation_image_1','site_cable_installation_image_2','site_cable_installation_image_3','site_cable_installation_comment',)

class SiteTerminalInHseFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteTerminalInHse
        fields = ('site_terminal_in_hse_image_1','site_terminal_in_hse_image_2','site_terminal_in_hse_image_3','site_terminal_in_hse_comment')

class SiteInterceptionFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteInterception
        fields = ('site_interception_image_1', 'site_interception_image_2','site_interception_image_3', 'site_interception_comment')

################### Main Project Serializer################################

class FttsSiteFilesSerializer(serializers.ModelSerializer):
    # Civil >many per site
    sitepoleinstallations = SitePoleInstallationFilesSerializer(many = True,read_only=True)
    sitetrenchings = SiteTrenchingFilesSerializer(many = True,read_only=True)
    siteductinstallations = SiteDuctInstallationSerializer(many = True,read_only=True)
    manholeinstallations = ManHoleInstallationFilesSerializer(many = True,read_only=True)
    sitecableinstallation  = SiteCableInstallationFilesSerializer(many = True,read_only=True)
    # Installation > Once per site
    siteterminalinhse = SiteTerminalInHseFilesSerializer(read_only=True)
    siteinterception  = SiteInterceptionFilesSerializer (read_only=True)


    class Meta:
        model = FttsSite
        #fields = ('__all__')
       # fields = ('sitetrenching','siteductinstallation','fttscommercialteam','site_name')

        exclude = ("id","site_name","ftts_project","created_at",
           "updated_at", "is_active", "created_by")

        #fields = ('geotech_file','access_letter','approved_drawing','final_acceptance_cert','setsiteclearingimage',
        #'towerbaseimage','bindingimage','steelfixformworkimage','concretepourcuringimage')
        #read_only_fields = ('created_at', 'updated_at', 'is_active')
