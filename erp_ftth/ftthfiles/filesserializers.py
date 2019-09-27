from rest_framework import serializers  #, exceptions
from erp_ftth.models import *

############################ PROJECT FILES SERIALIZERS ###############################################
excluded_fields = ('project_name',"initial_kmz",'signed_operation_acceptance',"id","created_at","updated_at",'posted_by','end_date','start_date', "is_active",'is_acknowledged',)


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
        exclude = excluded_fields


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
        exclude = excluded_fields



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
        exclude = excluded_fields

class FtthCableInstallationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCableInstallationImage
        fields = ('cableinstallation_image_1', 'cableinstallation_comment',)


class FtthCableInstallationDateFilesSerializer(serializers.ModelSerializer):
    cableinstallationimages = FtthCableInstallationImagesSerializer(many = True ,read_only=True)

    class Meta:
        model = DailyFtthCableInstallation
        fields = ('work_day','casuals_list','cableinstallationimages',)

class FtthCableInstallationSubTaskFilesSerializer(serializers.ModelSerializer):
    cableinstallationdays = FtthCableInstallationDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthCableInstallation
        fields = ('ftth_cable_installation_image_1','ftth_cable_installation_image_2','ftth_cable_installation_image_3','ftth_cable_installation_comment','cableinstallationdays',)


class FtthCableInstallationSubTaskAFilesSerializer(serializers.ModelSerializer):
    ftthcableinstallations = FtthCableInstallationSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = excluded_fields

        # TowerBaseSubTask  Files Serializers///////////////

class FtthSplicingEnclosureImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingEnclosureImage
        fields = ('splicingencore_image_1', 'splicingencore_comment',)


class FtthSplicingEnclosureDateFilesSerializer(serializers.ModelSerializer):
    splicingenclosureimage = FtthSplicingEnclosureImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthSplicingEnclosure
        fields = ('work_day','casuals_list','splicingenclosureimage',)

class FtthSplicingEnclosureSubTaskFilesSerializer(serializers.ModelSerializer):
    splicingencore =FtthSplicingEnclosureDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthSplicingEnclosure
        fields = ('ftth_splicing_encore_image_1', 'ftth_splicing_encore_image_2','ftth_splicing_encore_image_3', 'ftth_splicing_encore_comment','splicingencore')


class FtthSplicingEnclosureASubTaskFilesSerializer(serializers.ModelSerializer):
    ftthsplicingenclosures = FtthSplicingEnclosureSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = excluded_fields

##
        # TowerBaseSubTask  Files Serializers///////////////

class FtthSplicingFATImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingFATImage
        fields = ('splicingFAT_image_1', 'splicingFAT_comment',)


class FtthSplicingFATDateFilesSerializer(serializers.ModelSerializer):
    splicingFATimage = FtthSplicingFATImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthSplicingFAT
        fields = ('work_day','casuals_list','splicingFATimage',)

class FtthSplicingFATSubTaskFilesSerializer(serializers.ModelSerializer):
    splicingFAT =FtthSplicingFATDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthSplicingFAT
        fields = ('ftth_splicing_fat_image_1', 'ftth_splicing_fat_image_2','ftth_splicing_fat_image_3', 'ftth_splicing_fat_comment','splicingFAT',)


class FtthSplicingFATASubTaskFilesSerializer(serializers.ModelSerializer):
    ftthsplicingfats = FtthSplicingFATSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = excluded_fields

        # TowerBaseSubTask  Files Serializers///////////////

class FtthSplicingFDTImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingFDTImage
        fields = ('splicingFDT_image_1', 'splicingFDT_comment',)


class FtthSplicingFDTDateFilesSerializer(serializers.ModelSerializer):
    splicingFDTimage = FtthSplicingFDTImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthSplicingFDT
        fields = ('work_day','casuals_list','splicingFDTimage',)

class FtthSplicingFDTSubTaskFilesSerializer(serializers.ModelSerializer):
    splicingFDT =FtthSplicingFDTDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthSplicingFDT
        fields = ('ftth_splicing_fdt_image_1', 'ftth_splicing_fdt_image_2','ftth_splicing_fdt_image_3', 'ftth_splicing_fdt_comment','splicingFDT',)


class FtthSplicingFDTASubTaskFilesSerializer(serializers.ModelSerializer):
    ftthsplicingfdts = FtthSplicingFDTSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = excluded_fields
#
        # TowerBaseSubTask  Files Serializers///////////////

class FtthCoreProvisionImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCoreProvisionImage
        fields = ('coreprovision_image_1', 'coreprovision_comment',)


class FtthCoreProvisionDateFilesSerializer(serializers.ModelSerializer):
    coreprovisionimage = FtthCoreProvisionImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthCoreProvision
        fields = ('work_day','casuals_list','coreprovisionimage',)

class FtthCoreProvisionSubTaskFilesSerializer(serializers.ModelSerializer):
    ftthcoreprovisiondays =FtthCoreProvisionDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthCoreProvision
        fields = ('ftth_core_provision_image_1', 'ftth_core_provision_image_2','ftth_core_provision_image_3', 'ftth_core_provision_comment','ftthcoreprovisiondays',)


class FtthCoreProvisionASubTaskFilesSerializer(serializers.ModelSerializer):
    ftthcoreprovisions = FtthCoreProvisionSubTaskFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FTTHProject
        exclude = excluded_fields


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
    ftthpowerlevelsdays =FtthPowerLevelsDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthPowerLevels
        fields = ('ftth_power_level_image_1', 'ftth_power_level_image_2','ftth_power_level_image_3', 'ftth_power_level_comment','ftthpowerlevelsdays',)


class FtthPowerLevelsASubTaskFilesSerializer(serializers.ModelSerializer):
    ftthpowerlevels = FtthPowerLevelsSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = excluded_fields

        # TowerBaseSubTask  Files Serializers///////////////

class FtthOTDRTracesImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthOTDRTracesImage
        fields = ('OTDRTraces_image_1', 'OTDRTraces_comment',)


class FtthOTDRTracesDateFilesSerializer(serializers.ModelSerializer):
    OTDRTracesimage = FtthOTDRTracesImagesSerializer(many =True ,read_only=True)

    class Meta:
        model = DailyFtthOTDRTraces
        fields = ('work_day','casuals_list','OTDRTracesimage',)

class FtthOTDRTracesSubTaskFilesSerializer(serializers.ModelSerializer):
    otdrtracesdays =FtthOTDRTracesDateFilesSerializer(many = True,read_only =True)

    class Meta:
        model = FtthOTDRTraces
        fields = ('ftth_otdr_traces_image_1', 'ftth_otdr_traces_image_2','ftth_otdr_traces_image_3', 'ftth_otdr_traces_comment','otdrtracesdays',)


class FtthOTDRTracesASubTaskFilesSerializer(serializers.ModelSerializer):
    otdrtrace = FtthOTDRTracesSubTaskFilesSerializer(read_only =True)

    class Meta:
        model = FTTHProject
        exclude = excluded_fields

################### Main Project Serializer################################

class FTTHProjectFilesSerializer(serializers.ModelSerializer):
    # Civil >One per site
    ftthpoleinstallations = FtthPoleInstallationSubTaskFilesSerializer(read_only =True)
    ftthtrenchings = FtthTrenchingSubTaskFilesSerializer(read_only =True)
    ftthbackfillings = FtthBackfillingSubTaskFilesSerializer(read_only =True)
    ftthcableinstallations = FtthCableInstallationSubTaskFilesSerializer(read_only =True)
    ftthcoreprovisions = FtthCoreProvisionSubTaskFilesSerializer(many = True,read_only =True)
    ftthsplicingenclosures = FtthSplicingEnclosureSubTaskFilesSerializer(read_only =True)
    splicingFAT =FtthSplicingFATDateFilesSerializer(many = True,read_only =True)
    splicingFDT =FtthSplicingFDTDateFilesSerializer(many = True,read_only =True)

    otdrtrace = FtthOTDRTracesSubTaskFilesSerializer(read_only =True)


    class Meta:
        model = FTTHProject
        #fields = ('__all__')
       # fields = ('sitetrenching','siteductinstallation','fttscommercialteam','site_name')

        exclude = excluded_fields