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


# Site TRENCHING  Files Serializers///////////////


class SiteTrenchingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteTrenchingImage
        fields = ('site_trenching_image_1','site_trenching_comment',)


class SiteTrenchingDateFilesSerializer(serializers.ModelSerializer):
    sitetrenchingimages = SiteTrenchingImagesSerializer(many = True ,read_only=True)

    class Meta:
        model = DailySiteTrenching
        fields = ('work_day','casuals_list','sitetrenchingimages',)

class SiteTrenchingSubTaskFilesSerializer(serializers.ModelSerializer):
    dailysitetrenchings =SiteTrenchingDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = SiteTrenching
        fields = ('site_trenching_image_1', 'site_trenching_image_2','site_trenching_image_3', 'site_trenching_comment','dailysitetrenchings',)

# class SiteTrenchingSubTaskAFilesSerializer(serializers.ModelSerializer):
#     sitetrenching = SiteTrenchingSubTaskFilesSerializer(read_only =True)

#     class Meta:
#         model = FttsSite
#         exclude = ("ftts_project","site_name","id","created_at","updated_at", "is_active", "location", "posted_by",)

# Duct InstallationSubTask  Files Serializers///////////////

class SiteDuctInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteDuctInstallationImage
        fields = ('site_duct_image_1', 'site_duct_comment',)

class SiteDuctInstallationDateFilesSerializer(serializers.ModelSerializer):
    ductimages = SiteDuctInstallationImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailySiteDuctInstallation
        fields = ('work_day','casuals_list','ductimages',)

class SiteDuctInstallationSubTaskFilesSerializer(serializers.ModelSerializer):
    dailyduct = SiteDuctInstallationDateFilesSerializer(many = True ,read_only =True)

    class Meta:
        model = SiteDuctInstallation
        fields = ('site_duct_installation_image_1','site_duct_installation_image_2', 'site_duct_installation_image_3', 'site_duct_installation_comment','dailyduct',)

# class SiteClearingSubTaskAFilesSerializer(serializers.ModelSerializer):
#     siteductinstallation = SiteDuctInstallationSubTaskFilesSerializer(read_only =True)

#     class Meta:
#         model = BtsSite
#         exclude = ("ftts_project","site_name","id","created_at","updated_at", "is_active", "location", "posted_by",)

        
        # TowerBaseSubTask  Files Serializers///////////////

class ManHoleInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ManHoleInstallationImage
        fields = ('manhole_image_1', 'manhole_comment',)


class ManHoleInstallationDateFilesSerializer(serializers.ModelSerializer):
    manholeimages = ManHoleInstallationImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyManHoleInstallation
        fields = ('work_day','casuals_list','manholeimages',)

class ManHoleInstallationSubTaskFilesSerializer(serializers.ModelSerializer):
    manholeinstalldays =ManHoleInstallationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = ManHoleInstallation
        fields = ('manhole_image_1','manhole_image_2','manhole_image_3','manholeinstalldays',)

# Site Clearing  Files Serializers///////////////


class SiteCableInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteCableInstallationImage
        fields = ('cable_image_1', 'cable_comment',)

class SiteCableInstallationDateFilesSerializer(serializers.ModelSerializer):
    cableimages = SiteCableInstallationImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailySiteCableInstallation
        fields = ('work_day','casuals_list','cableimages',)

class SiteCableInstallationSubTaskFilesSerializer(serializers.ModelSerializer):
    cableinstalldays =SiteCableInstallationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = SiteCableInstallation
        fields = ('site_cable_installation_image_1','site_cable_installation_image_2','site_cable_installation_image_3','site_cable_installation_comment','cableinstalldays',)

# Site Clearing  Files Serializers///////////////

class SiteTerminalInHseFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteTerminalInHseImage
        fields = ('terminal_image_1', 'terminal_comment',)


class SiteTerminalInHseDateFilesSerializer(serializers.ModelSerializer):
    terminalinhseimage = SiteCableInstallationImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailySiteTerminalInHse
        fields = ('work_day','casuals_list','terminalinhseimage',)

class SiteTerminalInHseSubTaskFilesSerializer(serializers.ModelSerializer):
    terminalinhsedays =SiteCableInstallationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = SiteTerminalInHse
        fields = ('site_terminal_in_hse_image_1','site_terminal_in_hse_image_2','site_terminal_in_hse_image_3','site_terminal_in_hse_comment','terminalinhsedays',)

# Site Clearing  Files Serializers///////////////



class SiteInterceptionImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteInterceptionImage
        fields = ('interception_image_1',  'interception_comment')


class SiteInterceptionDateFilesSerializer(serializers.ModelSerializer):
    interceptionimages = SiteInterceptionImagesSerializer(many =True,read_only=True)

    class Meta:
        model = DailySiteInterception
        fields = ('work_day','casuals_list','interceptionimages',)

class SiteInterceptionSubTaskFilesSerializer(serializers.ModelSerializer):
    interceptiondays =SiteInterceptionDateFilesSerializer(many =True ,read_only =True)

    class Meta:
        model = SiteInterception
        fields = ('site_interception_image_1', 'site_interception_image_2','site_interception_image_3', 'site_interception_comment','interceptiondays',)

# Site Clearing  Files Serializers///////////////

# Site Clearing  Files Serializers///////////////

################### Main Project Serializer################################

class FttsSiteFilesSerializer(serializers.ModelSerializer):
    # Civil >One per site
    sitetrenching = SiteTrenchingSubTaskFilesSerializer(read_only =True)
    siteductinstallation = SiteDuctInstallationSubTaskFilesSerializer(read_only =True)
    manHoleinstallation = ManHoleInstallationSubTaskFilesSerializer(read_only =True)
    siteterminalinhse =  SiteTerminalInHseSubTaskFilesSerializer(read_only =True)

    siteinterception  = SiteInterceptionSubTaskFilesSerializer(read_only=True)


    class Meta:
        model = FttsSite
        #fields = ('__all__')
       # fields = ('sitetrenching','siteductinstallation','fttscommercialteam','site_name')

        exclude = ("id","site_name","ftts_project","created_at",
           "updated_at", "is_active", "posted_by","location")

        #fields = ('geotech_file','access_letter','approved_drawing','final_acceptance_cert','setSiteTrenchingimage',
        #'towerbaseimage','bindingimage','steelfixformworkimage','concretepourcuringimage')
        #read_only_fields = ('created_at', 'updated_at', 'is_active')
