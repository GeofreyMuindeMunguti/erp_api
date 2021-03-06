from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import *
from erp_construction.models import *
from .models import *
from rest_framework.authtoken.models import Token



class FTTHProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = FTTHProject
        fields = ('__all__')

###############################FTTH SURVEY###################################
class FtthInterceptionPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthInterceptionPoint
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ftthSurveyPhotosSerializer(serializers.ModelSerializer):

    ftth_survey_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ftthSurveyPhotos
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ftthSurveySerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)

    class Meta:
        model = ftthSurvey
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

###############################END OF FTTH SURVEY############################
class FtthCommercialTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCommercialTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthPoToSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthPoToSupplier
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthProcurementTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthProcurementTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthCertificatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCertificates
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

################################################ FIBER CIVIL TEAM ##############################################################################################################################################################################################################################################

class FtthPoleInstallationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthPoleInstallationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyFtthPoleInstallationSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyFtthPoleInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthPoleInstallationSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftth_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)

    class Meta:
        model = FtthPoleInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
"""END"""

class FtthTrenchingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthTrenchingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyFtthTrenchingSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyFtthTrenching
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthTrenchingSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftth_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)

    class Meta:
        model = FtthTrenching
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
"""END"""

class FtthBackfillingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthBackfillingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyFtthBackfillingSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyFtthBackfilling
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthBackfillingSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftth_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = FtthBackfilling
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
"""END"""

class FtthCableInstallationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCableInstallationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyFtthCableInstallationSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyFtthCableInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthCableInstallationSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftth_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = FtthCableInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthCivilTeamSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = FtthCivilTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
################################################ END ##############################################################################################################################################################################################################################################################

################################################ FIBER INSTALLATION TEAM ##############################################################################################################################################################################################################################################
class FtthSplicingEnclosureImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingEnclosureImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyFtthSplicingEnclosureSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyFtthSplicingEnclosure
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthSplicingEnclosureSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftth_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = FtthSplicingEnclosure
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
"""END"""
class FtthSplicingFATImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingFATImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyFtthSplicingFATSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyFtthSplicingFAT
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthSplicingFATSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftth_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = FtthSplicingFAT
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
"""END"""
class FtthSplicingFDTImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingFDTImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyFtthSplicingFDTSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyFtthSplicingFDT
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthSplicingFDTSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftth_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = FtthSplicingFDT
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthSplicingSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = FtthSplicing
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
"""END"""

class FtthCoreProvisionImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCoreProvisionImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyFtthCoreProvisionSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyFtthCoreProvision
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthCoreProvisionSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftth_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = FtthCoreProvision
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
"""END"""
class FtthPowerLevelsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthPowerLevelsImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyFtthPowerLevelsSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyFtthPowerLevels
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthPowerLevelsSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftth_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = FtthPowerLevels
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
"""END"""
class FtthOTDRTracesImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthOTDRTracesImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyFtthOTDRTracesSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyFtthOTDRTraces
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthOTDRTracesSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftth_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = FtthOTDRTraces
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class FtthSignalTestingSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = FtthSignalTesting
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthIssuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthIssues
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthInstallationTeamSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    team_task_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = FtthInstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class FtthTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
################################################ END ##############################################################################################################################################################################################################################################################
