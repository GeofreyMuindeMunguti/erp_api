from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import *
from erp_construction.models import *
from .models import *
from rest_framework.authtoken.models import Token



class FTTSProjectSerializer(serializers.ModelSerializer):
    ftts_sites_count = serializers.IntegerField(read_only=True)
    sites_list = serializers.ListField(read_only=True)
    class Meta:
        model = FTTSProject
        fields = ('__all__')

class FttsSiteSerializer(serializers.ModelSerializer):
    ftts_sites_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = FttsSite
        fields = ('__all__')

class FttsCommercialTeamSerializer(serializers.ModelSerializer):
    ftts_turn_around_time = serializers.IntegerField(read_only=True)
    # progress = serializers.IntegerField(read_only=True)

    class Meta:
        model = FttsCommercialTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsProcurementTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsProcurementTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsCertificatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsCertificates
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

###############################FTTH SURVEY###################################

class InterceptionPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterceptionPoint
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class fttsSurveyPhotosSerializer(serializers.ModelSerializer):

    ftts_survey_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = fttsSurveyPhotos
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class fttsSurveySerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)

    class Meta:
        model = fttsSurvey
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

###############################END OF FTTH SURVEY############################

################################################ FIBER CIVIL TEAM ##############################################################################################################################################################################################################################################

class SiteTrenchingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteTrenchingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailySiteTrenchingSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailySiteTrenching
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteTrenchingSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftts_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = SiteTrenching
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteDuctInstallationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteDuctInstallationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailySiteDuctInstallationSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailySiteDuctInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteDuctInstallationSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftts_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = SiteDuctInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class ManHoleInstallationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ManHoleInstallationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailyManHoleInstallationSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyManHoleInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteManHoleInstallationSerializer(serializers.ModelSerializer):
    ftts_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = ManHoleInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteCableInstallationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteCableInstallationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailySiteCableInstallationSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailySiteCableInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteCableInstallationSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftts_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = SiteCableInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class FttsAccessApprovalCivilSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsAccessApprovalCivil
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class FttsHealthDocumentsCivilTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsHealthDocumentsCivilTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsCivilTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsCivilTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
################################################ END ##############################################################################################################################################################################################################################################################

################################################ FIBER INSTALLATION TEAM ##############################################################################################################################################################################################################################################

class SiteTerminalInHseImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteTerminalInHseImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailySiteTerminalInHseSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailySiteTerminalInHse
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteTerminalInHseSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftts_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = SiteTerminalInHse
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteInterceptionImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteInterceptionImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class DailySiteInterceptionSerializer(serializers.ModelSerializer):
    image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailySiteInterception
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteInterceptionSerializer(serializers.ModelSerializer):
    raise_flag = serializers.CharField(read_only=True)
    ftts_task_id = serializers.IntegerField(read_only=True)
    days_list = serializers.ListField(read_only=True)
    class Meta:
        model = SiteInterception
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsAccessApprovalInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsAccessApprovalInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class FttsHealthDocsInstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsHealthDocsInstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsIssuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsIssues
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsInstallationTeamSerializer(serializers.ModelSerializer):
    team_task_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = FttsInstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
################################################ END ##############################################################################################################################################################################################################################################################

class DailyCivilWorkProductionSerializer(serializers.ModelSerializer):
    #image_list = serializers.ListField(read_only=True)
    class Meta:
        model = DailyCivilWorkProduction
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class CasualDailyRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CasualDailyRegister
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FTTSCasualDailyRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = FTTSCasualDailyRegister
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
