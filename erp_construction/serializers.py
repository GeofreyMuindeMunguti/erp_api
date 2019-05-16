
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import CustomUser, Project, ProcurementTeam, HealthDocumentsCivilTeam, AccessApprovalCivil, CivilWorksTeam, FoundationImage, BTSAndGeneatorSlabsImage, SiteWallingImage, CommercialTeam, SafaricomTeam,InstallationTeam,AccessApprovalInstallation,KPLCSolarImage,HealthDocumentsInstallationTeam, RFAndLinkImage,ElectricalImage


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('user_id','team','position')
        read_only_fields = ('is_active', 'is_staff')


class UserSerializer(serializers.ModelSerializer):
    """
    A UserProfile serializer to return the UserProfile details
    """
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password','profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = UserSerializer.create(UserSerializer(), validated_data=profile_data)
        user.set_password(password)
        user.save()
        userprofile = User.objects.create(user=user, **validated_data)
        return userprofile

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.team = profile_data.get('team', profile.team)
        profile.position = profile_data.get('position', profile.position)
        profile.save()

        return instance


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProcurementTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcurementTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class CommercialTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommercialTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class HealthDocumentsCivilTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthDocumentsCivilTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class AccessApprovalCivilSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessApprovalCivil
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class FoundationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BTSAndGeneatorSlabsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSAndGeneatorSlabsImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class SiteWallingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteWallingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class CivilWorksTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = CivilWorksTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class SafaricomTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = SafaricomTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class InstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class HealthDocumentsInstallationTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthDocumentsInstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

        
class AccessApprovalInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessApprovalInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class RFAndLinkImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RFAndLinkImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ElectricalImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricalImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class KPLCSolarImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPLCSolarImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')