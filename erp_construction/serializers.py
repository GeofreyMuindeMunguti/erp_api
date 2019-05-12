from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import CustomUser, Project, ProcurementTeam, HealthDocumentsCivilTeam, AccessApprovalCivil, CivilWorksTeam, FoundationImage, BTSAndGeneatorSlabsImage, SiteWallingImage, CommercialTeam, SafaricomTeam


class UserloginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=5, write_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'password')
        read_only_fields = ('is_active', 'created_at', 'updated_at')

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'])
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        profile = instance.profile
        profile.team = profile_data.get('team', profile.team)
        profile.position = profile_data.get('position', profile.position)
        profile.save()
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('user_id', 'team', 'position')
        read_only_fields = ('is_active', 'is_staff')

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


class UserSerializer(serializers.ModelSerializer):
    """
    A UserProfile serializer to return the UserProfile details
    """
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'password', 'profile')


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
