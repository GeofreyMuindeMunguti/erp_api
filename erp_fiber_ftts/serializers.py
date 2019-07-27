from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import *
from erp_construction.models import *
from .models import *
from rest_framework.authtoken.models import Token

class FTTSProjectSerializer(serializers.ModelSerializer):
   # site_name = serializers.CharField(source='site_name.name')
    class Meta:
        model = FTTSProject
        fields = (
            'id', 
            'project_name',
            'site_name',
            'project_type',
            'start_date',
            'end_date',
            'created_at', 
            'updated_at', 
            'is_active', 
        )
    # def to_representation(self, instance):
    #     rep = super(FTTSProjectSerializer, self).to_representation(instance)
    #     rep['site_name'] = instance.site_name.site_name
    #     return rep

class ProjectTrenchingSerializer(serializers.ModelSerializer):
   # sitetrenchings = serializers.StringRelatedField(many=True)
    class Meta:
        model = ProjectTrenching
        fields = (
            'id', 
            'project_name',
            #'sitetrenchings',
            'start_date',
            'end_date', 
            'created_by',
            'created_at', 
            'updated_at', 
            'is_active', 
        )


class SiteTrenchingSerializer(serializers.ModelSerializer):
   # fttstrenchingimages = serializers.StringRelatedField(many=True)
    class Meta:
        model = SiteTrenching
        fields = (
            'id', 
            'start_date', 
            'end_date', 
           # 'fttstrenchingimages',
        )


class FTTSTrenchingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FTTSTrenchingImage
        fields = (
            'id', 
            'trenching_day',
            'site_trenching' ,
            'description',
            'site_trenching_image_1', 
            'site_trenching_image_2', 
            'site_trenching_image_3', 
            'site_trenching_comment',
            'posted_by',
            'is_approved',
            'created_at', 
            'updated_at', 
            'is_active', 
        )
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
class SitePoleInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitePoleInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


        # Trenching

class SiteTrenchingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteTrenching
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


         # Backfilling
 
class SiteBackfillingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteBackfilling
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SiteCableInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteCableInstallation
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

class SiteAsBuiltSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteAsBuilt
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class FttsInstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsInstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
################################################ END ##############################################################################################################################################################################################################################################################
