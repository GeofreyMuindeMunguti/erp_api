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


class FtthPoleInstallationSubTaskAFilesSerializer(serializers.ModelSerializer):
    ftthpoleinstallations = FtthPoleInstallationSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = ('project_name','description',"initial_kmz",'signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment',"id","created_at","updated_at", "is_active", "created_by",'is_acknowledged',)




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
        fields = ('ftth_trenching_image_1', 'ftth_trenching_image_2','ftth_trenching_image_3', 'ftth_trenching_comment','ftthtrenchingdays',)

class FtthTrenchingSubTaskAFilesSerializer(serializers.ModelSerializer):
    ftthtrenchings = FtthTrenchingSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = ('project_name','description',"initial_kmz",'signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment',"id","created_at","updated_at", "is_active", "created_by",'is_acknowledged',)



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


class FtthBackfillingSubTaskAFilesSerializer(serializers.ModelSerializer):
    ftthbackfillings = FtthBackfillingSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = ('project_name','description',"initial_kmz",'signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment',"id","created_at","updated_at", "is_active", "created_by",'is_acknowledged',)



##


class FtthCableInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCableInstallationImage
        fields = ('cableinstallation_image_1', 'cableinstallation_comment',)


class FtthCableInstallationDateFilesSerializer(serializers.ModelSerializer):
    cableinstallationimages = FtthCableInstallationImagesSerializer(many = True ,read_only=True)

    class Meta:
        model = DailyFtthBackfilling
        fields = ('work_day','casuals_list','cableinstallationimages',)

class FtthCableInstallationSubTaskFilesSerializer(serializers.ModelSerializer):
    cableinstallationdays = FtthCableInstallationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthBackfilling
        fields = ('ftth_cable_installation_image_1','ftth_cable_installation_image_2','ftth_cable_installation_image_3','ftth_cable_installation_comment','cableinstallationdays',)


class FtthCableInstallationSubTaskAFilesSerializer(serializers.ModelSerializer):
    ftthcableinstallations = FtthCableInstallationSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = ('project_name','description',"initial_kmz",'signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment',"id","created_at","updated_at", "is_active", "created_by",'is_acknowledged',)

        # TowerBaseSubTask  Files Serializers///////////////

class FtthSplicingEnclosureImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingEnclosureImage
        fields = ('splicingencore_image_1', 'splicingencore_comment',)


class FtthSplicingEnclosureDateFilesSerializer(serializers.ModelSerializer):
    ftthsplicingenclosuresimages = FtthSplicingEnclosureImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthSplicingEnclosure
        fields = ('work_day','casuals_list','ftthsplicingenclosuresimages',)

class FtthSplicingEnclosureSubTaskFilesSerializer(serializers.ModelSerializer):
    ftthsplicingenclosuresdays =FtthSplicingEnclosureDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthSplicingEnclosure
        fields = ('ftth_splicing_encore_image_1', 'ftth_splicing_encore_image_2','ftth_splicing_encore_image_3', 'ftth_splicing_encore_comment','ftthsplicingenclosuresdays')


class FtthSplicingEnclosureASubTaskFilesSerializer(serializers.ModelSerializer):
    ftthsplicingenclosures = FtthSplicingEnclosureSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = ('project_name','description',"initial_kmz",'signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment',"id","created_at","updated_at", "is_active", "created_by",'is_acknowledged',)

        

##


        # TowerBaseSubTask  Files Serializers///////////////

class FtthSplicingFATImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingFATImage
        fields = ('splicingFAT_image_1', 'splicingFAT_comment',)


class FtthSplicingFATDateFilesSerializer(serializers.ModelSerializer):
    manholeimages = FtthSplicingFATImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthSplicingFAT
        fields = ('work_day','casuals_list','ftthsplicingfatimages',)

class FtthSplicingFATSubTaskFilesSerializer(serializers.ModelSerializer):
    ftthsplicingfatdays =FtthSplicingFATDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthSplicingFAT
        fields = ('ftth_splicing_fat_image_1', 'ftth_splicing_fat_image_2','ftth_splicing_fat_image_3', 'ftth_splicing_fat_comment','ftthsplicingfatdays',)


class FtthSplicingFATASubTaskFilesSerializer(serializers.ModelSerializer):
    ftthsplicingfats = FtthSplicingFATSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = ('project_name','description',"initial_kmz",'signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment',"id","created_at","updated_at", "is_active", "created_by",'is_acknowledged',)

        # TowerBaseSubTask  Files Serializers///////////////

class FtthSplicingFDTImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingFDTImage
        fields = ('splicingFDT_image_1', 'splicingFDT_comment',)


class FtthSplicingFDTDateFilesSerializer(serializers.ModelSerializer):
    ftthsplicingfdtimages = FtthSplicingFDTImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthSplicingFDT
        fields = ('work_day','casuals_list','ftthsplicingfdtimages',)

class FtthSplicingFDTSubTaskFilesSerializer(serializers.ModelSerializer):
    ftthsplicingfdtdays =FtthSplicingFDTDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthSplicingFDT
        fields = ('ftth_splicing_fdt_image_1', 'ftth_splicing_fdt_image_2','ftth_splicing_fdt_image_3', 'ftth_splicing_fdt_comment','ftthsplicingfdtdays',)


class FtthSplicingFDTASubTaskFilesSerializer(serializers.ModelSerializer):
    ftthsplicingfdts = FtthSplicingFDTSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = ('project_name','description',"initial_kmz",'signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment',"id","created_at","updated_at", "is_active", "created_by",'is_acknowledged',)



#


        # TowerBaseSubTask  Files Serializers///////////////

class FtthCoreProvisionImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCoreProvisionImage
        fields = ('coreprovision_image_1', 'coreprovision_comment',)


class FtthCoreProvisionDateFilesSerializer(serializers.ModelSerializer):
    ftthcoreprovisionimages = FtthCoreProvisionImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthCoreProvision
        fields = ('work_day','casuals_list','ftthcoreprovisionimages',)

class FtthCoreProvisionSubTaskFilesSerializer(serializers.ModelSerializer):
    ftthcoreprovisiondays =FtthCoreProvisionDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthCoreProvision
        fields = ('ftth_core_provision_image_1', 'ftth_core_provision_image_2','ftth_core_provision_image_3', 'ftth_core_provision_comment','ftthcoreprovisiondays',)


class FtthCoreProvisionASubTaskFilesSerializer(serializers.ModelSerializer):
    ftthcoreprovisions = FtthCoreProvisionSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = ('project_name','description',"initial_kmz",'signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment',"id","created_at","updated_at", "is_active", "created_by",'is_acknowledged',)


       # TowerBaseSubTask  Files Serializers///////////////

class FtthPowerLevelsImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthPowerLevelsImage
        fields = ('powerlevels_image_1', 'powerlevels_comment',)


class FtthPowerLevelsDateFilesSerializer(serializers.ModelSerializer):
    ftthpowerlevelimages = FtthPowerLevelsImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthPowerLevels
        fields = ('work_day','casuals_list','ftthpowerlevelimages',)

class FtthPowerLevelsSubTaskFilesSerializer(serializers.ModelSerializer):
    ftthpowerleveldays =FtthPowerLevelsDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthPowerLevels
        fields = ('ftth_power_level_image_1', 'ftth_power_level_image_2','ftth_power_level_image_3', 'ftth_power_level_comment','ftthpowerleveldays',)


class FtthPowerLevelsASubTaskFilesSerializer(serializers.ModelSerializer):
    ftthpowerlevels = FtthPowerLevelsSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = ('project_name','description',"initial_kmz",'signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment',"id","created_at","updated_at", "is_active", "created_by",'is_acknowledged',)

        # TowerBaseSubTask  Files Serializers///////////////

class FtthOTDRTracesImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthOTDRTracesImage
        fields = ('OTDRTraces_image_1', 'OTDRTraces_comment',)


class FtthOTDRTracesDateFilesSerializer(serializers.ModelSerializer):
    otdrtracesimages = FtthOTDRTracesImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthOTDRTraces
        fields = ('work_day','casuals_list','otdrtracesimages',)

class FtthOTDRTracesSubTaskFilesSerializer(serializers.ModelSerializer):
    otdrtracesdays =FtthOTDRTracesDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthOTDRTraces
        fields = ('ftth_otdr_traces_image_1', 'ftth_otdr_traces_image_2','ftth_otdr_traces_image_3', 'ftth_otdr_traces_comment','otdrtracesdays',)


class FtthOTDRTracesASubTaskFilesSerializer(serializers.ModelSerializer):
    otdrtraces = FtthOTDRTracesSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = ('project_name','description',"initial_kmz",'signed_operation_acceptance','ftth_final_acceptance_cert','ftth_final_acceptance_cert_comment',"id","created_at","updated_at", "is_active", "created_by",'is_acknowledged',)



################### Main Project Serializer################################

class FTTHProjectFilesSerializer(serializers.ModelSerializer):
    # Civil >One per site
    #ftthpoleinstallation = FtthPoleInstallationSubTaskFilesSerializer(read_only =True)
    # sitetrenching = SiteTrenchingSubTaskFilesSerializer(read_only =True)
    # siteductinstallation = SiteDuctInstallationSubTaskFilesSerializer(read_only =True)
    # FtthSplicingEnclosure = FtthSplicingEnclosureSubTaskFilesSerializer(read_only =True)
    # siteterminalinhse =  SiteTerminalInHseSubTaskFilesSerializer(read_only =True)

    # siteinterception  = SiteInterceptionSubTaskFilesSerializer(read_only=True)


    class Meta:
        model = FTTHProject
        #fields = ('__all__')
       # fields = ('sitetrenching','siteductinstallation','fttscommercialteam','site_name')

        exclude = ("id","signed_operation_acceptance","created_at",
           "updated_at", "is_active",)