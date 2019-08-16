from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import *
from erp_construction.models import *
from .models import *
from rest_framework.authtoken.models import Token



class FTTSProjectSerializer(serializers.ModelSerializer):
    sites_no = serializers.CharField(read_only=True)
    class Meta:
        model = FTTSProject
        fields = '__all__'

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

    class Meta:
        model = fttsSurvey
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


###############################END OF FTTH SURVEY############################


class FttsCommercialTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsCommercialTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsProcurementTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsProcurementTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

################################################ FIBER CIVIL TEAM ##############################################################################################################################################################################################################################################

class SiteTrenchingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteTrenching
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteDuctInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteDuctInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteCableInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteCableInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteManHoleInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ManHoleInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class FttsCivilTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsCivilTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
################################################ END ##############################################################################################################################################################################################################################################################

################################################ FIBER INSTALLATION TEAM ##############################################################################################################################################################################################################################################
class SiteTerminalInHseSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteTerminalInHse
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteInterceptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteInterception
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteIntegrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteIntegration
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsIssuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsIssues
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsInstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsInstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
################################################ END ##############################################################################################################################################################################################################################################################

class DailyCivilWorkProductionSerializer(serializers.ModelSerializer):

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
