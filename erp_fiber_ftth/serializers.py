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
        fields = (
            'id', 
            'project_name', 
            'project_type', 
            'initial_kmz', 
            'is_acknowledged', 
        )


class FtthCommercialTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCommercialTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthProcurementTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthProcurementTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

################################################ FIBER CIVIL TEAM ##############################################################################################################################################################################################################################################
class FtthPoleInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthPoleInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthTrenchingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthTrenching
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthBackfillingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthBackfilling
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthCableInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCableInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthCivilTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCivilTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
################################################ END ##############################################################################################################################################################################################################################################################

################################################ FIBER INSTALLATION TEAM ##############################################################################################################################################################################################################################################
class FtthSplicingEnclosureSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingEnclosure
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthSplicingFATSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingFAT
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthSplicingFDTSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicingFDT
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthSplicingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSplicing
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthCoreProvisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthCoreProvision
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthPowerLevelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthPowerLevels
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthOTDRTracesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthOTDRTraces
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthAsBuiltSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthAsBuilt
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthSignalTestingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthSignalTesting
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FtthInstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FtthInstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
################################################ END ##############################################################################################################################################################################################################################################################
