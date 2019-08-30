"""Extract files and images per project.
"""
#---------
# Imports
#---------
from rest_framework import serializers  #, exceptions
from erp_ftth.models import *


############################ PROJECT FILES SERIALIZERS ###############################################


class FTTHProjectFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FTTHProject
       # fields = ('ftts_final_acceptance_cert','ftts_accumulated_BOM_survey')
# Site TRENCHING  Files Serializers///////////////


class FtthPoleInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthPoleInstallationImage
        fields = ('poleinstallation_image_1', 'poleinstallation_comment',)


class FtthPoleInstallationDateFilesSerializer(serializers.ModelSerializer):
    poleinstallationimages = FtthPoleInstallationImagesSerializer(many = True ,read_only=True)

    class Meta:
        model = DailyFtthPoleInstallation
        fields = ('work_day','casuals_list','poleinstallationimages',)

class FtthPoleInstallationSubTaskFilesSerializer(serializers.ModelSerializer):
    poleinstallationdays =FtthPoleInstallationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthPoleInstallation
        fields = ('ftth_pole_installation_image_1','ftth_pole_installation_image_2','ftth_pole_installation_image_3','ftth_pole_installation_comment','poleinstallationdays',)

class FtthTrenchingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthTrenchingImage
        fields = ('trenching_image_1', 'trenching_comment',)


class FtthTrenchingDateFilesSerializer(serializers.ModelSerializer):
    ftthtrenchingimages = FtthTrenchingImagesSerializer(many = True ,read_only=True)

    class Meta:
        model = DailyFtthTrenching
        fields = ('work_day','casuals_list','ftthtrenchingimages',)

class FtthTrenchingSubTaskFilesSerializer(serializers.ModelSerializer):
    ftthtrenchingdays =FtthTrenchingDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthTrenching
        fields = ('ftth_trenching_image_2','ftth_trenching_image_3', 'ftth_trenching_comment','ftthtrenchingdays',)



class FtthBackfillingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthBackfillingImage
        fields = ('backfilling_image_1', 'backfilling_comment',)


class FtthBackfillingDateFilesSerializer(serializers.ModelSerializer):
    ftthbackfillingimages = FtthBackfillingImagesSerializer(many = True ,read_only=True)

    class Meta:
        model = DailyFtthBackfilling
        fields = ('work_day','casuals_list','ftthbackfillingimages',)

class FtthBackfillingSubTaskFilesSerializer(serializers.ModelSerializer):
    ftthbackfillingdays =FtthBackfillingDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthBackfilling
        fields = ('ftth_backfilling_image_1','ftth_backfilling_image_2', 'ftth_backfilling_image_3', 'ftth_backfilling_comment','ftthbackfillingdays',)






################### Main Project Serializer################################

class FTTHProjectFilesSerializer(serializers.ModelSerializer):
    # Civil >One per site
    #ftthpoleinstallation = FtthPoleInstallationSubTaskFilesSerializer(read_only =True)
    # sitetrenching = SiteTrenchingSubTaskFilesSerializer(read_only =True)
    # siteductinstallation = SiteDuctInstallationSubTaskFilesSerializer(read_only =True)
    # manHoleinstallation = ManHoleInstallationSubTaskFilesSerializer(read_only =True)
    # siteterminalinhse =  SiteTerminalInHseSubTaskFilesSerializer(read_only =True)

    # siteinterception  = SiteInterceptionSubTaskFilesSerializer(read_only=True)


    class Meta:
        model = FTTHProject
        #fields = ('__all__')
       # fields = ('sitetrenching','siteductinstallation','fttscommercialteam','site_name')

        exclude = ("id","signed_operation_acceptance","created_at",
           "updated_at", "is_active",)